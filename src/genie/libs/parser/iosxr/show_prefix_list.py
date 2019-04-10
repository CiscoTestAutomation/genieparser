"""show_prefix_list.py

IOSXR parser for the following show command:

    * show rpl prefix-set
"""

# Python
import re

# MetaParser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

class ShowRplPrefixSetSchema(MetaParser):
    """Schema for:
        show rpl prefix-set"""

    schema = {'prefix_set_name': 
                {Any(): 
                    {'prefix_set_name': str,
                    'protocol': str,
                    'prefixes': 
                        {Any(): 
                            {'prefix': str,
                            'masklength_range': str,
                            },
                        },
                    },
                },
            }

# ================================
# Parser for 'show rpl prefix-set'
# ================================
class ShowRplPrefixSet(ShowRplPrefixSetSchema):
    """Parser for:
        show rpl prefix-set"""

    cli_command = 'show rpl prefix-set'

    def cli(self, output=None):
        out = self.device.execute(self.cli_command) if output is None else output

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # prefix-set test
            # prefix-set test6
            p1 = re.compile(r'^prefix\-set +(?P<name>\S+)$')
            m = p1.match(line)

            if m:
                name = m.groupdict()['name']

                ret_dict.setdefault('prefix_set_name', {}).setdefault(name, {})
                ret_dict['prefix_set_name'][name]['prefix_set_name'] = name
                continue

            # ipv4 version of below
            # 2001:db8:1::/64,
            # 2001:db8:2::/64 ge 65,
            # 2001:db8:3::/64 le 128,
            # 2001:db8:4::/64 ge 65 le 98
            p2 = re.compile(r'^(?P<prefixes>(?P<prefix>[\w\.:]+)\/'
                             '(?P<mask>\d+))\s*(?P<range>[lge\d\s]+)?,?$')
            m = p2.match(line)

            if m:
                prefixes = m.groupdict()['prefixes']
                prefix = m.groupdict()['prefix']
                mask = m.groupdict()['mask']

                ipv6_test = re.compile(r'^\w*:\w*:\w*:\w*:\w*$').match(prefix)
                ret_dict['prefix_set_name'][name]['protocol'] = 'ipv6' if ipv6_test else 'ip'

                ret_dict['prefix_set_name'][name].setdefault('prefixes', {})

                # masklength_range
                temp = m.groupdict()['range']
                if not temp:
                    masklength_range = '{}..{}'.format(mask, mask)
                else:
                    temp = temp.strip()

                    # ge 16 le 24
                    match = re.compile(r'^ge +(?P<val1>\d+) +le +(?P<val2>\d+)$').match(temp)
                    if match:
                        masklength_range = '{val1}..{val2}'.format(val1=match.groupdict()['val1'],
                                                                   val2=match.groupdict()['val2'])


                    # le 16
                    match = re.compile(r'^le +(?P<val2>\d+)$').match(temp)
                    if match:
                        masklength_range = '{val1}..{val2}'.format(val1=mask,
                                                                   val2=match.groupdict()['val2'])

                    # ge 16
                    match = re.compile(r'^ge +(?P<val1>\d+)$').match(temp)
                    if match:
                        max_val = '128' if ipv6_test else '32'
                        masklength_range = '{val1}..{val2}'.format(val1=match.groupdict()['val1'],
                                                                   val2=max_val)

                key = '{prefixes} {masklength_range}'.format(prefixes=prefixes,
                                                             masklength_range=masklength_range)

                ret_dict['prefix_set_name'][name]['prefixes'].setdefault(key, {})

                ret_dict['prefix_set_name'][name]['prefixes'][key]['prefix'] = prefix
                ret_dict['prefix_set_name'][name]['prefixes'][key]['masklength_range'] = masklength_range
                continue

        return ret_dict