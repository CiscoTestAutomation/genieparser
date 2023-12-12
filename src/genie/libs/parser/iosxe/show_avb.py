''' show_avb.py
IOSXE parsers for the following show commands:

    * 'show avb domain'
'''
import re
from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, And

# =====================================
# Schema for:
#  * 'show avb domain'
# =====================================
class ShowAvbDomainSchema(MetaParser):
    """Schema for show avb domain"""

    schema = {
        'avb': {
            Any(): {
                'vlan': int,
                'priority_code_point': int,
                'core_ports': int,
                'boundary_ports': int,
            },
        },
        'interface': {
            Any(): {
                'state': str,
                'delay': str,
                Optional('pcp'): int,
                Optional('vid'): int,
                Optional('information'): str,
                Optional('class'): {
                    Any():{
                        'pcp': int,
                        'vid': int,
                        'state': str,
                    }
                }
            }
        }        
    }
    
# =====================================
# Parser for:
#  * 'show avb domain'
# =====================================
class ShowAvbDomain(ShowAvbDomainSchema):
    """Parser for show avb domain"""

    cli_command = "show avb domain"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # AVB Class-A
        p1 = re.compile(r'^AVB\s+(?P<avb_class>[\w\s\-]+)$')

        # Priority Code Point     : 3
        p2 = re.compile(r'^(?P<pattern>[\w\s]+)\s+:\s+(?P<value>[\d]+)$')

        # Tw1/0/1          up    156ns
        p3 = re.compile(r'^(?P<interface>[\w\/\.]+)\s+(?P<state>\w+)\s+(?P<delay>[\w\/]+)$')

        # Tw1/0/1          up      N/A                    Port is not asCapable
        p4 = re.compile(r'^(?P<interface>[\w\/\.]+)\s+(?P<state>\w+)\s+(?P<delay>[\w\/]+)?\s+(?P<pcp>\d+)?\s+(?P<vid>\d+)?\s+(?P<information>[\w\s]+)?$')

        # Class-  A        core             3    2
        p5 = re.compile(r'^Class-\s+(?P<class>[\w\-\s]+)\s+(?P<state>\w+)\s+(?P<pcp>[\w\/]+)\s+(?P<vid>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # AVB Class-B
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface_dict = ret_dict.setdefault('avb',{}).setdefault(group['avb_class'],{})

            # Priority Code Point     : 3
            m = p2.match(line)
            if m:
                group = m.groupdict()
                scrubbed = (group['pattern'].strip()).replace(' ', '_')
                interface_dict.update({scrubbed.lower(): int(group['value'])})
                continue

            # Tw1/0/1          up    156ns
            m = p3.match(line)
            if m:
                int_dict = ret_dict.setdefault('interface', {}).setdefault(Common.convert_intf_name(m.groupdict()['interface']), {})
                int_dict['state'] = m.groupdict()['state']
                int_dict['delay'] = m.groupdict()['delay']
                continue

            # Tw1/0/1          up      N/A                    Port is not asCapable
            m = p4.match(line)
            if m:
                int_dict = ret_dict.setdefault('interface', {}).setdefault(Common.convert_intf_name(m.groupdict()['interface']), {})
                int_dict['state'] = m.groupdict()['state']
                int_dict['delay'] = m.groupdict()['delay']
                if m.groupdict()['pcp']:
                    int_dict['pcp'] = int(m.groupdict()['pcp'])
                if m.groupdict()['vid']:
                    int_dict['vid'] = int(m.groupdict()['vid'])
                if m.groupdict()['information']:
                    int_dict['information'] = m.groupdict()['information']
                continue

            # Class-  A        core             3    2
            m = p5.match(line)
            if m:
                class_dict = int_dict.setdefault('class', {}).setdefault(m.groupdict()['class'].strip(), {})
                class_dict['state'] = m.groupdict()['state']
                class_dict['pcp'] = int(m.groupdict()['pcp'])
                class_dict['vid'] = int(m.groupdict()['vid'])
                continue

        return ret_dict
