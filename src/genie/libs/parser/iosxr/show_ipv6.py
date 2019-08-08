"""
    show_ipv6.py
    IOSXR parsers for the following show commands:

    * show ipv6 neighbors detail
    * show ipv6 vrf all interface (from show_interface.py)
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use


from genie.libs.parser.utils.common import Common

# ======================================================
# Parser for 'show ipv6 neighbors detail '
# ======================================================

class ShowIpv6NeighborsDetailSchema(MetaParser):
    """Schema for show ipv6 neighbors detail"""

    schema = {
        'interfaces': {
            Any(): {
                'interface': str,
                'neighbors': {
                    Any(): {
                        'ip': str,  # Conf/Ops Str '2010:1:2::1'
                        'link_layer_address': str,  # Conf/Ops Str 'aaaa.beef.cccc'
                        'age': str,
                        'neighbor_state': str,
                        'location': str,
                        'static': str,
                        'dynamic': str,
                        'sync': str,
                        'serg_flags': str
                    },
                },
            },
        },
    }

class ShowIpv6NeighborsDetail(ShowIpv6NeighborsDetailSchema):
    """Parser for show ipv6 neighbors detail"""

    cli_command = 'show ipv6 neighbors detail'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # 2010:1:2::1  82   fa16.3e19.abba REACH Gi0/0/0/0  0/0/CPU0  -  Y  - ff
        p1 = re.compile(r'^(?P<ip>\S+)\s+(?P<age>\S+)\s+(?P<link_layer_address>\S+)\s+(?P<neighbor_state>\S+)\s+(?P<interface>\S+)\s+'
                         '(?P<location>\S+)\s+(?P<static>\S+)\s+(?P<dynamic>\S+)\s+(?P<sync>\S+)\s+(?P<serg_flags>\S+)$')

        #[Mcast adjacency]                - 0000.0000.0000 REACH Gi0/0/0/0            0/0/CPU0        -      -       -            ff
        p2 = re.compile(r'^\[(?P<ip>([\w\s]+))\]\s+(?P<age>\S+)\s+(?P<link_layer_address>\S+)\s+(?P<neighbor_state>\S+)\s+'
                         '(?P<interface>\S+)\s+(?P<location>\S+)\s+(?P<static>\S+)\s+(?P<dynamic>\S+)\s+(?P<sync>\S+)\s+(?P<serg_flags>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # 2010:1:2::1  82   fa16.3e19.abba REACH Gi0/0/0/0  0/0/CPU0  -  Y  - ff
            m = p1.match(line)
            if m:
                ip = m.groupdict()['ip']
                age = m.groupdict()['age']
                link_layer_address = m.groupdict()['link_layer_address']
                neighbor_state = m.groupdict()['neighbor_state']
                interfaces = Common.convert_intf_name(m.groupdict()['interface'])
                interface = m.groupdict()['interface']
                location = m.groupdict()['location']
                static = m.groupdict()['static']
                dynamic = m.groupdict()['dynamic']
                sync = m.groupdict()['sync']
                serg_flags = m.groupdict()['serg_flags']

                interface_dict = ret_dict.setdefault('interfaces', {}).setdefault(interfaces, {})
                interface_dict['interface'] = interface

                neighbor_dict = interface_dict.setdefault('neighbors', {}).setdefault(ip, {})

                neighbor_dict['age'] = age
                neighbor_dict['ip'] = ip
                neighbor_dict['link_layer_address'] = link_layer_address
                neighbor_dict['neighbor_state'] = neighbor_state
                neighbor_dict['location'] = location
                neighbor_dict['static'] = static
                neighbor_dict['dynamic'] = dynamic
                neighbor_dict['sync'] = sync
                neighbor_dict['serg_flags'] = serg_flags
                continue

            # [Mcast adjacency]  - 0000.0000.0000 REACH Gi0/0/0/0   0/0/CPU0  -      -       -            ff
            m = p2.match(line)
            if m:
                ip = m.groupdict()['ip']
                age = m.groupdict()['age']
                link_layer_address = m.groupdict()['link_layer_address']
                neighbor_state = m.groupdict()['neighbor_state']
                interfaces = Common.convert_intf_name(m.groupdict()['interface'])
                interface = m.groupdict()['interface']
                location = m.groupdict()['location']
                static = m.groupdict()['static']
                dynamic = m.groupdict()['dynamic']
                sync = m.groupdict()['sync']
                serg_flags = m.groupdict()['serg_flags']

                interface_dict = ret_dict.setdefault('interfaces', {}).setdefault(interfaces, {})
                interface_dict['interface'] = interface

                neighbor_dict = interface_dict.setdefault('neighbors', {}).setdefault(ip, {})

                neighbor_dict['age'] = age
                neighbor_dict['ip'] = ip

                neighbor_dict['link_layer_address'] = link_layer_address
                neighbor_dict['neighbor_state'] = neighbor_state
                neighbor_dict['location'] = location
                neighbor_dict['static'] = static
                neighbor_dict['dynamic'] = dynamic
                neighbor_dict['sync'] = sync
                neighbor_dict['serg_flags'] = serg_flags
                continue

        return ret_dict
