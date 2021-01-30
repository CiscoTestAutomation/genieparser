"""
    show_ipv6.py
    IOSXR parsers for the following show commands:

    * show ipv6 neighbors detail
    * show ipv6 vrf all interface (from show_interface.py)
    * show ipv6 neighbors
    * show ipv6 neighbors vrf {vrf}
    * show ipv6 neighbors {interface}
    * show ipv6 neighbors vrf {vrf} {interface}
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
                        'ip': str,  # Conf/Ops Str '2001:db8:8548:1::1'
                        'link_layer_address': str,  # Conf/Ops Str 'aaaa.beff.bcbc'
                        'age': str,
                        'neighbor_state': str,
                        'location': str,
                        Optional('static'): str,
                        Optional('dynamic'): str,
                        Optional('sync'): str,
                        Optional('origin'): str,
                        Optional('serg_flags'): str
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

        # 2001:db8:8548:1::1  82   fa16.3eff.c4d3 REACH Gi0/0/0/0  0/0/CPU0  -  Y  - ff
        # fe80::f816:3eff:feff:384a  119  fa16.3eff.384a REACH Gi0/0/0/0.90         0/0/CPU0
        p1 = re.compile(r'^(?P<ip>\S+)\s+(?P<age>\S+)\s+(?P<link_layer_address>\S+)\s+(?P<neighbor_state>\S+)\s+(?P<interface>\S+)\s+'
                         '(?P<location>\S+)(\s+(?P<static>\S+)\s+(?P<dynamic>\S+)\s+(?P<sync>\S+)\s+(?P<serg_flags>\S+))?$')

        # [Mcast adjacency]                - 0000.0000.0000 REACH Gi0/0/0/0            0/0/CPU0        -      -       -            ff
        # [Mcast adjacency]                - 0000.0000.0000 REACH Gi0/0/0/0.90         0/0/CPU0
        p2 = re.compile(r'^\[(?P<ip>([\w\s]+))\]\s+(?P<age>\S+)\s+(?P<link_layer_address>\S+)\s+(?P<neighbor_state>\S+)\s+'
                         '(?P<interface>\S+)\s+(?P<location>\S+)(\s+(?P<static>\S+)\s+(?P<dynamic>\S+)\s+(?P<sync>\S+)\s+(?P<serg_flags>\S+))?$')

        for line in out.splitlines():
            line = line.strip()

            # 2001:db8:8548:1::1  82   fa16.3eff.c4d3 REACH Gi0/0/0/0  0/0/CPU0  -  Y  - ff 
            m = p1.match(line)
            if m:
                ip = m.groupdict()['ip']
                age = m.groupdict()['age']
                link_layer_address = m.groupdict()['link_layer_address']
                neighbor_state = m.groupdict()['neighbor_state']
                interface = Common.convert_intf_name(m.groupdict()['interface'])
                location = m.groupdict()['location']
                static = m.groupdict()['static']
                dynamic = m.groupdict()['dynamic']
                sync = m.groupdict()['sync']
                serg_flags = m.groupdict()['serg_flags']

                interface_dict = ret_dict.setdefault('interfaces', {}).setdefault(interface, {})
                interface_dict['interface'] = interface

                neighbor_dict = interface_dict.setdefault('neighbors', {}).setdefault(ip, {})

                neighbor_dict['age'] = age
                neighbor_dict['ip'] = ip
                neighbor_dict['link_layer_address'] = link_layer_address
                neighbor_dict['neighbor_state'] = neighbor_state
                neighbor_dict['location'] = location
                if static:
                    neighbor_dict['static'] = static
                    neighbor_dict['dynamic'] = dynamic
                    neighbor_dict['sync'] = sync
                    neighbor_dict['serg_flags'] = serg_flags

                    if static == 'Y':
                        origin = 'static'
                    elif dynamic == 'Y':
                        origin = 'dynamic'
                    elif sync == 'Y':
                        origin = 'sync'
                    else:
                        origin = 'other'
                    neighbor_dict['origin'] = origin

                continue

            # [Mcast adjacency]  - 0000.0000.0000 REACH Gi0/0/0/0   0/0/CPU0  -      -       -            ff
            m = p2.match(line)
            if m:
                ip = m.groupdict()['ip']
                age = m.groupdict()['age']
                link_layer_address = m.groupdict()['link_layer_address']
                neighbor_state = m.groupdict()['neighbor_state']
                interface = Common.convert_intf_name(m.groupdict()['interface'])
                location = m.groupdict()['location']
                static = m.groupdict()['static']
                dynamic = m.groupdict()['dynamic']
                sync = m.groupdict()['sync']
                serg_flags = m.groupdict()['serg_flags']

                interface_dict = ret_dict.setdefault('interfaces', {}).setdefault(interface, {})
                interface_dict['interface'] = interface

                neighbor_dict = interface_dict.setdefault('neighbors', {}).setdefault(ip, {})

                neighbor_dict['age'] = age
                neighbor_dict['ip'] = ip
                neighbor_dict['link_layer_address'] = link_layer_address
                neighbor_dict['neighbor_state'] = neighbor_state
                neighbor_dict['location'] = location
                if static:
                    neighbor_dict['static'] = static
                    neighbor_dict['dynamic'] = dynamic
                    neighbor_dict['sync'] = sync
                    neighbor_dict['serg_flags'] = serg_flags

                    if static == 'Y':
                        origin = 'static'
                    elif dynamic == 'Y':
                        origin = 'dynamic'
                    elif sync == 'Y':
                        origin = 'sync'
                    else:
                        origin = 'other'
                    neighbor_dict['origin'] = origin

                continue

        return ret_dict


class ShowIpv6Neighbors(ShowIpv6NeighborsDetail):
    """Parser for :
        'show ipv6 neighbors'
        'show ipv6 neighbors vrf {vrf}'
        'show ipv6 neighbors {interface}'
        'show ipv6 neighbors vrf {vrf} {interface}'
        """

    cli_command = ['show ipv6 neighbors vrf {vrf} {interface}',
                   'show ipv6 neighbors {interface}',
                   'show ipv6 neighbors vrf {vrf}',
                   'show ipv6 neighbors',]

    def cli(self, vrf='', interface='', output=None):
        if output is None:
            if vrf and interface:
                if vrf == 'all':
                    cmd = self.cli_command[1].format(interface=interface)
                else:
                    cmd = self.cli_command[0].format(vrf=vrf, interface=interface)
            elif interface:
                cmd = self.cli_command[1].format(interface=interface)
            elif vrf and vrf != 'all':
                cmd = self.cli_command[2].format(vrf=vrf)
            else:
                cmd = self.cli_command[3]

            out = self.device.execute(cmd)
        else:
            out = output

        return super().cli(output=out)

        
