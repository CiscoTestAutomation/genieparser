'''Common functions to be used in parsers'''

# python
import re
import os
import json
import sys
import warnings
import logging
import importlib
import math

from fuzzywuzzy import fuzz
from genie.libs import parser
from genie.abstract import Lookup

log = logging.getLogger(__name__)

def _load_parser_json():
    '''get all parser data in json file'''
    try:
        mod = importlib.import_module('genie.libs.parser')
        parsers = os.path.join(mod.__path__[0], 'parsers.json')
    except Exception:
        parsers = ''
    if not os.path.isfile(parsers):
        log.warning('parsers.json does not exist, make sure you '
                    'are running with latest version of '
                    'genie.libs.parsers')
        parser_data = {}
    else:
        # Open all the parsers in json file
        with open(parsers) as f:
            parser_data = json.load(f)
    return parser_data

# Parser within Genie
parser_data = _load_parser_json()

def get_parser_commands(device, data=parser_data):
    '''Remove all commands which contain { as this requires
       extra kwargs which cannot be guessed dynamically
       Remove the ones that arent related to this os'''

    commands = []
    for command, values in data.items():
        if '{' in command or command == 'tokens' or device.os not in values:
            continue
        commands.append(command)
    return commands

def format_output(parser_data, tab=2):
    '''Format the parsed output in an aligned intended structure'''

    s = ['{\n']
    if parser_data is None:
        return parser_data
    for k,v in sorted(parser_data.items()):
        if isinstance(v, dict):
            v = format_output(v, tab+2)
        else:
            v = repr(v)
        s.append('%s%r: %s,\n' % ('  '*tab, k, v))
    s.append('%s}' % ('  '*(tab-2)))
    return ''.join(s)

def get_parser_exclude(command, device):
    try:
        return get_parser(command, device)[0].exclude
    except AttributeError:
        return []

def get_parser(command, device, regex=False):
    '''From a show command and device, return parser class and kwargs if any'''

    try:
        order_list = device.custom.get('abstraction').get('order', [])
    except AttributeError:
        order_list = None

    lookup = Lookup.from_device(device, packages={'parser': parser})
    results = _fuzzy_search_command(command, regex, device.os, order_list)
    valid_results = []
    
    for result in results:
        found_command, data, kwargs = result

        if found_command == 'tokens':
            continue

        # Check if all the tokens exists and take the farthest one
        for token in lookup._tokens:
            if token in data:
                data = data[token]

        valid_results.append((found_command, _find_parser_cls(device, data), kwargs))

    if not valid_results:
        raise Exception("Could not find parser for "
                        "'{c}' under {l}".format(c=command, l=lookup._tokens))

    if not regex:
        return valid_results[0][1], valid_results[0][2]

    return valid_results

def _fuzzy_search_command(search, use_regex, os=None, order_list=None, device=None):
    # Perfect match should return 
    if search in parser_data:
        return [(search, parser_data[search], {})]

    # Preprocess if regex
    if use_regex:
        search = search.lstrip('^').rstrip('$').replace(r'\ ', ' ').replace(
            r'\-', '-').replace('\\"', '"').replace('\\,', ',').replace(
            '\\\'', '\'').replace('\\*', '*').replace('\\:', ':').replace(
            '\\^', '^').replace('\\/', '/')

    # Fix search to remove extra spaces
    search = ' '.join(filter(None, search.split()))
    tokens = search.split()
    best_score = -math.inf
    result = []

    for command, source in parser_data.items():
        # Tokens and kwargs parameter must be non reference
        match_result = _matches_fuzzy_regex(0, 0, tokens.copy(),
                                                        command, {}, use_regex)

        if match_result: 
            kwargs, score = match_result
            
            if order_list and device and getattr(device, order_list[0]) not in source:
                continue

            if os and os not in source:
                continue

            entry = (command, source, kwargs)

            if score > best_score:
                # If we found a better match, discard everything and start new
                result = [entry]

                best_score = score
            elif score == best_score:
                result.append(entry)

    # Return only one instance if regex is not used
    # Check if any ambiguous commands
    if not use_regex and len(result) > 1:
        # If all results have the same argument positions but different names
        # It should return the first result
        if len(set(re.sub('{.*?}', '---', instance[0]) for instance in result)) == 1:
            return [result[0]]
        else:
            # Search is ambiguous
            raise Exception("\nSearch for '" + search +  "' is ambiguous. " + 
                            "Please be more specific in your keywords.\n\n" +
                            "Results matched:\n" + '\n'.join('> ' + i[0] for i in result))

    return result

def _is_regular_token(token):
    token_is_regular = True

    if len(token) == 1 and token == '*':
        # Special case for `show lldp entry *`
        token_is_regular = True
    elif len(token) == 2 and token == r'\|':
        # Special case for `ps -ef | grep {grep}`
        token_is_regular = True
    elif not token.isalnum():
        # Remove escaped characters
        candidate = token.replace('/', '')
        candidate = candidate.replace('"', '')
        candidate = candidate.replace(r'\^', '')
        candidate = candidate.replace('\'', '')
        candidate = candidate.replace('-', '')
        candidate = candidate.replace('^', '')
        candidate = candidate.replace('_', '')
        candidate = candidate.replace(':', '')
        candidate = candidate.replace(',', '')
        candidate = candidate.replace(r'\.', '')
        candidate = candidate.replace(r'\|', '')

        token_is_regular = candidate.isalnum() or candidate == ''
    
    return token_is_regular

def _matches_fuzzy_regex(i, j, tokens, command, kwargs, use_regex, required_arguments=None, score=0):
    command_tokens = command.split()

    # Initialize by counting how many arguments this command needs
    if required_arguments is None:
        required_arguments = len(re.findall('{.*?}', command))

    while i < len(tokens):
        # If command token index is greater than its length, stop
        if j >= len(command_tokens):
            return None

        token = tokens[i]
        command_token = command_tokens[j]
        token_is_regular = True

        if use_regex:
            # Check if it is nonregex token
            token_is_regular = _is_regular_token(token)

        if token_is_regular:
            # Current token might be command or argument
            if '{' in command_token:
                # Right strip for `<argument>"` case
                argument_parameter = token.rstrip('"').replace('\\', '')

                # Handle the edge case of argument not being a token
                # When this is implemented there is only one case:
                # /dna/intent/api/v1/interface/{interface}
                if not command_token.startswith('{'):
                    # Find before and after string
                    groups = re.match('(.*){.*?}(.*)', command_token).groups()
                    is_found = False

                    if len(groups) == 2:
                        start, end = groups

                        # Need to have perfect match with token
                        if token.startswith(start) and token.endswith(end):
                            # Escape regex
                            start = re.escape(start)
                            end = re.escape(end)

                            # Find the argument using the escaped start and end
                            argument_parameter = re.match('{}(.*){}'
                                        .format(start, end), token).groups()[0]
                        
                            is_found = True
                            score += 1
                    
                    if not is_found: 
                        return None

                kwargs[re.search('{(.*)}', command_token).groups()[0]] = argument_parameter

                # Set current token to command token
                # For future regex match, it should not consider argument
                tokens[i] = command_token
                score += 100 
            elif token == command_token:
                # Same token, assign higher score
                score += 102
            elif not token == command_token:
                # Not matching, perform fuzzy search
                # Give perfect score for prefix matching
                if command_token.startswith(token):
                    score += 101
                else:
                    # Locality sensitive score
                    ratio = fuzz.ratio(token, command_token)

                    # Have locality sensitive cut off 
                    if ratio <= 30:
                        return None

                    # Locality insensitive score
                    partial_ratio = fuzz.partial_ratio(token, command_token)
                    
                    # Cut off
                    if partial_ratio <= 30:
                        return None

                    # Add ratio to score
                    score += ratio

                # The two tokens are similar to each other, replace it with valid one
                tokens[i] = command_token

            # Matches current, go to next token
            i += 1
            j += 1
        else:
            # Count number of regex tokens that got ate
            skipped = 1

            # Not a token, should be a regex expression
            # Keep eating if next token is also regex
            while i + 1 < len(tokens) and not _is_regular_token(tokens[i + 1]):
                i += 1
                skipped += 1

            # Match current span with command
            test = re.match(' '.join(tokens[:i + 1]), command)

            if test:
                # Perform command token lookahead
                _, end = test.span()

                # Expression matches command to end
                if i + 1 == len(tokens) and end == len(command): 
                    # Return result if from start to end there are no arguments
                    if all(not '{' in ct for ct in command_tokens[j:]):
                        return kwargs, score
                    else: 
                        # Else in range we have another unspecified argument
                        return None

                if end == 0: 
                    # If regex matched nothing, we stop because
                    # expression = "d? a b c" search in "a b c"
                    # expression = "a b d? c" search in "a b c"
                    return None

                # Span single command token
                if abs(end - sum(len(ct) for ct in command_tokens[:j + 1]) - j) <= 1:
                    if not '{' in command_token:
                        # Span single token if it is not argument
                        i += 1
                        j += 1

                        continue
                    else:
                        # Faulty match
                        return None
                else:
                    # Span multiple command tokens
                    # Find which command token it spans up to
                    current_sum = 0
                    token_end = 0

                    while current_sum + len(command_tokens[token_end]) <= end:
                        current_sum += len(command_tokens[token_end])
                        
                        if current_sum < end:
                            # Account for space 
                            current_sum += 1
                            token_end += 1
                        else:
                            break

                    # Incrememt token index
                    i += 1
                
                    # For matched range, perform submatches on next real token
                    for subindex in range(j + skipped, token_end + 1):
                        # Make sure items are passed by copies, not by reference
                        submatch_result = _matches_fuzzy_regex(i, subindex, 
                            tokens.copy(), command, kwargs.copy(),
                            use_regex, required_arguments, score)
                        
                        # If any match is found, return true
                        if submatch_result:
                            result_kwargs, score = submatch_result

                            # Result kwargs must match number of arguments this command requires
                            if required_arguments == len(result_kwargs):
                                return result_kwargs, score

                    # Fail to match
                    return None
            else:
                # Failed to match regex
                return None

    # Reached end of tokens
    if len(command_tokens) == j:
        # If command pointer is at end then it matches
        return kwargs, score
    else: 
        # It doesn't match
        return None


def _find_parser_cls(device, data):
    lookup = Lookup.from_device(device, packages={'parser':importlib.import_module(data['package'])})

    return getattr(getattr(lookup.parser, data['module_name']), data['class'])


class Common():
    '''Common functions to be used in parsers.'''

    @classmethod
    def regexp(self, expression):
        def match(value):
            if re.match(expression, value):
                return value
            else:
                raise TypeError("Value '%s' doesnt match regex '%s'"
                                % (value, expression))
        return match

    @classmethod
    def convert_intf_name(self, intf):
        '''return the full interface name

            Args:
                intf (`str`): Short version of the interface name

            Returns:
                Full interface name fit the standard

            Raises:
                None

            example:

                >>> convert_intf_name(intf='Eth2/1')
        '''

        # Please add more when face other type of interface
        convert = {'Eth': 'Ethernet',
                   'Lo': 'Loopback',
                   'Fa': 'FastEthernet',
                   'Fas': 'FastEthernet',
                   'Po': 'Port-channel',
                   'PO': 'Port-channel',
                   'Null': 'Null',
                   'Gi': 'GigabitEthernet',
                   'Gig': 'GigabitEthernet',
                   'GE': 'GigabitEthernet',
                   'Te': 'TenGigabitEthernet',
                   'mgmt': 'mgmt',
                   'Vl': 'Vlan',
                   'Tu': 'Tunnel',
                   'Fe': '',
                   'Hs': 'HSSI',
                   'AT': 'ATM',
                   'Et': 'Ethernet',
                   'BD': 'BDI',
                   'Se': 'Serial',
                   'Fo': 'FortyGigabitEthernet',
                   'Hu': 'HundredGigE',
                   'vl': 'vasileft',
                   'vr': 'vasiright',
                   'BE': 'Bundle-Ether'
                   }
        m = re.search('([a-zA-Z]+)', intf) 
        m1 = re.search('([\d\/\.]+)', intf)
        if hasattr(m, 'group') and hasattr(m1, 'group'):
            int_type = m.group(0)
            int_port = m1.group(0)
            if int_type in convert.keys():
                return(convert[int_type] + int_port)
            else:
                # Unifying interface names
                converted_intf = intf[0].capitalize()+intf[1:].replace(
                    ' ','').replace('ethernet', 'Ethernet')
                return(converted_intf)
        else:
            return(intf)


    @classmethod
    def retrieve_xml_child(self, root, key):
        '''return the root which contains the key from xml

            Args:

                root (`obj`): ElementTree Object, point to top of the tree
                key (`str`): Expceted tag name. ( without namespace)

            Returns:
                Element object of the given tag

            Raises:
                None

            example:

                >>> retrieve_xml_child(
                        root=<Element '{urn:ietf:params:xml:ns:netconf:base:1.0}rpc-reply' at 0xf760434c>,
                        key='TABLE_vrf')
        '''
        for item in root:
            if key in item.tag:
                return item
            else:
                root = item
                return self.retrieve_xml_child(root, key)


    @classmethod
    def compose_compare_command(self, root, namespace, expect_command):
        '''compose commmand from the xml Element object from the root,
           then compare with the command with the expect_command.
           Only work for cisco standard output.

            Args:

                root (`obj`): ElementTree Object, point to top of the tree
                namespace (`str`): Namesapce. Ex. {http://www.cisco.com/nxos:8.2.0.SK.1.:rip}
                expect_command (`str`): expected command.

            Returns:
                None

            Raises:
                AssertionError: xml tag cli and command is not matched
                Exception: No mandatory tag __readonly__ in output

            example:

                >>> compose_compare_command(
                        root=<Element '{urn:ietf:params:xml:ns:netconf:base:1.0}rpc-reply' at 0xf760434c>,
                        namespace='{http://www.cisco.com/nxos:8.2.0.SK.1.:rip}',
                        expect_command='show bgp all dampening flap-statistics')
        '''
        # get to data node
        cmd_node = root.getchildren()[0]
        # compose command from element tree
        # ex.  <nf:data>
        #        <show>
        #         <bgp>
        #          <all>
        #           <dampening>
        #            <flap-statistics>
        #             <__readonly__>
        cli = ''
        while True:
            # get next node
            try:
                cmd_node = cmd_node.getchildren()
                if len(cmd_node) == 1:

                    # when only have one child
                    cmd_node = cmd_node[0]

                    # <__XML__PARAM__vrf-name>
                    #  <__XML__value>VRF1</__XML__value>
                    # </__XML__PARAM__vrf-name>
                    if '__XML__value' in cmd_node.tag:
                        cli += ' ' + cmd_node.text

                elif len(cmd_node) > 1:

                   # <__XML__PARAM__interface>
                   #   <__XML__value>loopback100</__XML__value>
                   #   <vrf>
                   for item in cmd_node:
                       if '__XML__value' in item.tag:
                           cli += ' ' + item.text
                       else:
                           cmd_node = item
                           break
                else:
                    break
            except Exception:
                pass

            # get tag name
            tag = cmd_node.tag.replace(namespace, '')

            # __readonly__ is the end of the command
            if '__readonly__' not in tag:
                if '__XML__PARAM__' not in tag and \
                   '__XML__value' not in tag and \
                   'TABLE' not in tag:
                    cli += ' ' + tag
            else:
                break

            # if there is no __readonly__ but the command has outputs
            # should be warining
            if 'TABLE' in tag:
                warnings.warn('Tag "__readonly__" should exsist in output when '
                              'there are actual values in output')
                break

        cli = cli.strip()
        # compare the commands
        assert cli == expect_command, \
            'Cli created from XML tags does not match the actual cli:\n'\
            'XML Tags cli: {c}\nCli command: {e}'.format(c=cli, e=expect_command)



    @classmethod
    def convert_xml_time(self, xml_time):
        '''Convert xml time "PT1H4M41S" to normal time "01:04:41"

            Args:
                xml_time (`str`): XML time

            Returns:
                Standard time string

            Raises:
                None

            example:

                >>> convert_xml_time(xml_time='PT1H4M41S')
                >>> "01:04:41"
        '''
        # P4DT12M38S
        # PT1H4M41S
        p = re.compile(r'^P((?P<day>\d+)D)?T((?P<hour>\d+)H)?((?P<minute>\d+)M)?((?P<second>\d+)S)?$')
        m = p.match(xml_time)
        if m:
            day = m.groupdict()['day']
            hour = m.groupdict()['hour']
            hour = 0 if not hour else int(hour)
            minute = m.groupdict()['minute']
            minute = 0 if not  minute else int(minute)
            second = m.groupdict()['second']
            second = 0 if not  second else int(second)

            if day:
                standard_time = "{d}d{h}h".format(d=day, h="%02d"% (hour))
            else:
                standard_time = ''
                standard_time += format("%02d"% (hour))
                standard_time += ' ' + format("%02d"% (minute))
                standard_time += ' ' +  format("%02d"% (second))

                standard_time = ':'.join(standard_time.strip().split())
        else:
            # P4M13DT21H21M19S
            standard_time = xml_time
        return standard_time


    @classmethod
    def find_keys(self, key, dictionary):
        '''
        find all keys in dictionary
        Args:
            dictionary:

        Returns:

        '''
        for k, v in dictionary.items():
            if k == key:
                yield v
            elif isinstance(v, dict):
                for result in self.find_keys(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in self.find_keys(key, d):
                        yield result


    @classmethod
    def combine_units_of_time(self, hours=None, minutes=None, seconds=None):
        '''Combine seperate units of time to 'normal time': HH:MM:SS

            Args (All are optional. Nothing returns 00:00:00):
                hours (`int`): number of hours
                minutes (`int`): number of minutes
                seconds (`int`): number of seconds

            Returns:
                Standard time string

            Raises:
                None

            example:

                >>> convert_xml_time(minutes=500)
                >>> "08:20:00"
        '''
        total_combined_seconds = 0

        if hours:
            total_combined_seconds += hours * 60 * 60

        if minutes:
            total_combined_seconds += minutes * 60

        if seconds:
            total_combined_seconds += seconds

        final_seconds = total_combined_seconds % 60
        if final_seconds <= 9:
            final_seconds = "0{}".format(final_seconds)

        final_minutes = (total_combined_seconds // 60) % 60
        if final_minutes <= 9:
            final_minutes = "0{}".format(final_minutes)

        final_hours = (total_combined_seconds // 60) // 60
        if final_hours <= 9:
            final_hours = "0{}".format(final_hours)

        normal_time = "{}:{}:{}".format(final_hours, final_minutes,
                                        final_seconds)

        return normal_time