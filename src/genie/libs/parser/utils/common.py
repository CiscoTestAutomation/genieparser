'''Common functions to be used in parsers'''

# python
import re
import os
import json
import sys
import warnings
import logging
import importlib


from genie.libs import parser
from genie.abstract import Lookup

log = logging.getLogger(__name__)
# Parser within Genie
try:
    mod = importlib.import_module('genie.libs.parser')
    parsers = os.path.join(mod.__path__[0], 'parsers.json')
except Exception:
    parsers = ''

if not os.path.isfile(parsers):
    log.warning('parsers.json does not exists, make sure you '
                'are running with latest version of '
                'genie.libs.parsers')
    parser_data = {}
else:
    # Open all the parsers in json file
    with open(parsers) as f:
        parser_data = json.load(f)

def format_output(parser_data, tab=0):
    '''Format the parsed output in an aligned intended structure'''

    s = ['{\n']
    if parser_data is None:
        return parser_data
    for k,v in parser_data.items():
        if isinstance(v, dict):
            v = format_output(v, tab+2)
        else:
            v = repr(v)
        s.append('%s%r: %s,\n' % ('  '*tab, k, v))
    s.append('%s}' % ('  '*tab))
    return ''.join(s)

def get_parser(command, device):
    '''From a show command and device, return parser class and kwargs if any'''

    kwargs = {}
    if command in parser_data:
        # Then just return it
        lookup = Lookup.from_device(device, packages={'parser':parser})
        # Check if all the tokens exists; take the farthest one
        data = parser_data[command]
        for token in lookup._tokens:
            if token in data:
                data = data[token]

        try:
            return _find_parser_cls(device, data), kwargs
        except KeyError:
            # Case when the show command is only found under one of
            # the child level tokens
            raise Exception("Could not find parser for "
                            "'{c}' under {l}".format(
                                c=command, l=lookup._tokens)) from None
    else:
        # Regex world!
        try:
            found_data, kwargs = _find_command(command, parser_data, device)
        except SyntaxError:
            # Could not find a match
            raise Exception("Could not find parser for "
                            "'{c}'".format(c=command)) from None

        return _find_parser_cls(device, found_data), kwargs

def _find_command(command, data, device):
    ratio = 0
    max_lenght = 0
    matches = None
    for key in data:
        if not '{' in key:
            # Disregard the non regex ones
            continue

        # Okay... this is not optimal
        patterns = re.findall('{.*?}', key)
        len_normal_words = len(set(key.split()) - set(patterns))
        reg = key

        for pattern in patterns:
            word = pattern.replace('{', '').replace('}', '')
            new_pattern = '(?P<{p}>.*)'.format(p=word)
            reg = re.sub(pattern, new_pattern, reg)
        reg += '$'
        # Convert | to \|
        reg = reg.replace('|', '\|')

        match = re.match(reg, command)
        if match:
            # Found a match!
            lookup = Lookup.from_device(device, packages={'parser':parser})
            # Check if all the tokens exists; take the farthest one
            ret_data = data[key]
            for token in lookup._tokens:
                if token in ret_data:
                    ret_data = ret_data[token]

            if len_normal_words > max_lenght:
                max_lenght = len_normal_words
                matches = (ret_data, match.groupdict())

    if matches:
        return matches
    raise SyntaxError('Could not find a parser match')


def _find_parser_cls(device, data):
    lookup = Lookup.from_device(device, packages={'parser':parser})
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
                   'BD': 'BridgeDomain',
                   'Se': 'Serial',
                   'Fo': 'FortyGigabitEthernet',
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
