"""show_prefix_list.py

IOSXE parsers for the following show commands:

    * show ip prefix-list detail
    * show ipv6 prefix-list detail
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# ==============================================
# Parser for 'show ip prefix-list detail'
# Parser for 'show ipv6 prefix-list detail'
# ==============================================

class ShowIpPrefixListDetailSchema(MetaParser):
    """Schema for
        show ip prefix-list detail
        show ipv6 prefix-list detail"""

    schema = {'prefix_set_name':         
                {Any(): {
                    'prefix_set_name': str,
                    Optional('protocol'): str,
                    Optional('count'): int,
                    Optional('range_entries'): int,
                    Optional('sequences'): str,
                    Optional('refcount'): int,
                    Optional('prefixes'):
                        {Any():
                            {Optional('prefix'): str,
                             Optional('masklength_range'): str,
                             Optional('sequence'): int,
                             Optional('hit_count'): int,
                             Optional('refcount'): int,
                             Optional('action'): str,
                            }
                        },
                    },
                },
            }

class ShowIpPrefixListDetail(ShowIpPrefixListDetailSchema):
    """Parser for:
        show ip prefix-list detail
        show ipv6 prefix-list detail"""

    cli_command = 'show {af} prefix-list detail'

    def cli(self, af='ip',output=None):
        # ip should be ip or ipv6
        assert af in ['ip', 'ipv6']
        # excute command to get output
        protocol = 'ipv4' if af == 'ip' else af

        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command.format(af=af))
        else:
            out = output

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # ip prefix-list test:
            # ipv6 prefix-list test6:
            p1 = re.compile(r'^(ipv6|ip) +prefix\-list +(?P<name>\S+)\:$')
            m = p1.match(line)
            if m:
                name = m.groupdict()['name']

                if 'prefix_set_name' not in ret_dict:
                    ret_dict['prefix_set_name'] = {}
                if name not in ret_dict['prefix_set_name']:
                    ret_dict['prefix_set_name'][name] = {}

                ret_dict['prefix_set_name'][name]['prefix_set_name'] = name
                continue

            # count: 5, range entries: 4, sequences: 5 - 25, refcount: 2
            # count: 0, range entries: 0, refcount: 1
            p2 = re.compile(r'^count: +(?P<count>\d+), +'
                             'range entries: +(?P<entries>\d+),( +'
                             'sequences: +(?P<sequences>[\d\-\s]+),)? +'
                             'refcount: +(?P<refcount>\d+)$')
            m = p2.match(line)
            if m:
                ret_dict['prefix_set_name'][name]['count'] = int(m.groupdict()['count'])
                ret_dict['prefix_set_name'][name]['range_entries'] = int(m.groupdict()['entries'])
                if m.groupdict()['sequences']:
                    ret_dict['prefix_set_name'][name]['sequences'] = m.groupdict()['sequences']
                ret_dict['prefix_set_name'][name]['refcount'] = int(m.groupdict()['refcount'])
                ret_dict['prefix_set_name'][name]['protocol'] = protocol
                continue

            # seq 5 permit 10.205.0.0/8 (hit count: 0, refcount: 1)
            # seq 5 permit 2001:DB8:1::/64 (hit count: 0, refcount: 1)
            # seq 20 permit 10.94.0.0/8 ge 24 (hit count: 0, refcount: 2)
            # seq 25 permit 10.169.0.0/8 ge 16 le 24 (hit count: 0, refcount: 3)
            p3 = re.compile(r'^seq +(?P<seq>\d+) +(?P<action>\w+) +'
                             '(?P<prefixes>(?P<prefix>[\w\.\|:]+)\/(?P<mask>\d+))'
                             '( *(?P<range>[lge\d\s]+))?'
                             ' +\(hit +count: +(?P<hit_count>\d+), +refcount: +(?P<refcount>\d+)\)$')
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
                ret_dict['prefix_set_name'][name]['prefixes'][key]['hit_count'] = int(m.groupdict()['hit_count'])
                ret_dict['prefix_set_name'][name]['prefixes'][key]['refcount'] = int(m.groupdict()['refcount'])
                continue

        return ret_dict


# ===========================================
# Parser for 'show ipv6 prefix-list detail'
# ===========================================
class ShowIpv6PrefixListDetail(ShowIpPrefixListDetail, ShowIpPrefixListDetailSchema):
    """Parser for show ipv6 prefix-list detail"""
    cli_command = 'show ipv6 prefix-list detail'

    def cli(self, af='ipv6', output=None):
        # ip should be ip or ipv6
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(af=af, output=out)
