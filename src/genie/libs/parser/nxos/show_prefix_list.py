"""show_prefix_list.py

NXOS parsers for the following show commands:

    * show ip prefix-list
    * show ipv6 prefix-list

"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# ==============================================
# Schema for 'show ip prefix-list'
# Schema for 'show ipv6 prefix-list'
# ==============================================

class ShowIpPrefixListSchema(MetaParser):
    """Schema for:
        show ip prefix-list
        show ipv6 prefix-list"""

    schema = {'prefix_set_name':         
                {Any(): {
                    'prefix_set_name': str,
                    'protocol': str,
                    'entries': int,
                    'prefixes':
                        {Any():
                            {'prefix': str,
                             'masklength_range': str,
                             'sequence': int,
                             'action': str
                            }
                        },
                    },
                },
            }

class ShowIpPrefixList(ShowIpPrefixListSchema):
    """Parser for show ip prefix-list detail"""

    cli_command = 'show {af} prefix-list'

    def cli(self, af='ip',output=None):

        # ip should be ip or ipv6
        assert af in ['ip', 'ipv6']

        # excute command to get output
        protocol = 'ipv4' if af == 'ip' else af
        if output is None:
            out = self.device.execute(self.cli_command.format(af=af))
        else:
            out = output

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # ip prefix-list test: 5 entries
            # ipv6 prefix-list test6: 4 entries
            p1 = re.compile(r'^(ipv6|ip) +prefix\-list +(?P<name>\S+)\: +'
                             '(?P<entries>\d+) +entries$')
            m = p1.match(line)
            if m:
                name = m.groupdict()['name']

                if 'prefix_set_name' not in ret_dict:
                    ret_dict['prefix_set_name'] = {}
                if name not in ret_dict['prefix_set_name']:
                    ret_dict['prefix_set_name'][name] = {}

                ret_dict['prefix_set_name'][name]['prefix_set_name'] = name
                ret_dict['prefix_set_name'][name]['protocol'] = protocol
                ret_dict['prefix_set_name'][name]['entries'] = int(m.groupdict()['entries'])
                continue

            # seq 5 permit 35.0.0.0/8
            # seq 5 permit 2001:DB8:1::/64
            # seq 20 permit 37.0.0.0/8 ge 24
            # seq 25 permit 38.0.0.0/8 ge 16 le 24
            # seq 10 permit 192.0.2.0/24 eq 25
            p3 = re.compile(r'^seq +(?P<seq>\d+) +(?P<action>\w+) +'
                             '(?P<prefixes>(?P<prefix>[\w\.\|:]+)\/(?P<mask>\d+))'
                             '( *(?P<range>[lgeq\d\s]+))?$')
            m = p3.match(line)
            if m:
                prefixes = m.groupdict()['prefixes']
                mask = m.groupdict()['mask']
                action = m.groupdict()['action']
                if 'prefixes' not in ret_dict['prefix_set_name'][name]:
                    ret_dict['prefix_set_name'][name]['prefixes'] = {}

                # masklength_range
                dummy = m.groupdict()['range']
                if not dummy:
                    masklength_range = '{val1}..{val2}'.format(val1=mask, val2=mask)
                else:
                    dummy = dummy.strip()
                    # ge 16 le 24
                    match = re.compile(r'^ge +(?P<val1>\d+) +le +(?P<val2>\d+)$').match(dummy)
                    if match:
                        masklength_range = '{val1}..{val2}'.format(val1=match.groupdict()['val1'],
                                                                   val2=match.groupdict()['val2'])


                    # le 16
                    match = re.compile(r'^le +(?P<val2>\d+)$').match(dummy)
                    if match:
                        masklength_range = '{val1}..{val2}'.format(val1=mask,
                                                                   val2=match.groupdict()['val2'])

                    # ge 16
                    match = re.compile(r'^ge +(?P<val1>\d+)$').match(dummy)
                    if match:
                        max_val = '32' if af == 'ip' else '128'
                        masklength_range = '{val1}..{val2}'.format(val1=match.groupdict()['val1'],
                                                                   val2=max_val)
                    # eq 25
                    match = re.compile(r'^eq +(?P<val1>\d+)$').match(dummy)
                    if match:
                        val = match.groupdict()['val1']
                        masklength_range = '{val1}..{val2}'.format(val1=val, val2=val)

                # compose the level key vaule
                key = '{prefixes} {masklength_range} {action}'.format(prefixes=prefixes,
                                                                      masklength_range=masklength_range,
                                                                      action=action)
                if key not in ret_dict['prefix_set_name'][name]['prefixes']:
                    ret_dict['prefix_set_name'][name]['prefixes'][key] = {}

                ret_dict['prefix_set_name'][name]['prefixes'][key]['prefix'] = prefixes
                ret_dict['prefix_set_name'][name]['prefixes'][key]['masklength_range'] = masklength_range
                ret_dict['prefix_set_name'][name]['prefixes'][key]['action'] = action
                ret_dict['prefix_set_name'][name]['prefixes'][key]['sequence'] = int(m.groupdict()['seq'])
                continue

        return ret_dict


# ===========================================
# Parser for 'show ipv6 prefix-list'
# ===========================================
class ShowIpv6PrefixList(ShowIpPrefixList):
    """Parser for show ipv6 prefix-list detail"""

    def cli(self,output=None):
        return super().cli(af='ipv6',output=output)

