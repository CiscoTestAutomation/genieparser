''' show_ospfv3.py

NXOS parsers for the following show commands:
    * show ipv6 ospfv3 neighbors detail
    * show ipv6 ospfv3 neighbors detail vrf <WORD>
'''

# Python
import re
from netaddr import IPNetwork

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional
from genie.libs.parser.utils.common import Common

# =======================================================
# Schema for 'show ipv6 ospfv3 neighbors detail [vrf <WORD>]'
# =======================================================


class ShowIpv6Ospfv3NeighborsDetailSchema(MetaParser):
    """Schema for:
        show ipv6 ospfv3 neighbors detail
        show ipv6 ospfv3 neighbors detail vrf <vrf>"""

    schema = {
        'vrf':
            {Any():
                {'address_family':
                    {Any():
                        {'instance':
                            {Any():
                                {'areas':
                                    {Any():
                                        {'interfaces':
                                            {Any():
                                                {'neighbors':
                                                 {Any():
                                                  {'neighbor_router_id': str,
                                                   'address': str,
                                                   'state': str,
                                                   'last_state_change': str,
                                                   Optional('priority'): int,
                                                   Optional('nbr_intf_id'): int,
                                                   Optional('dr_ip_addr'): str,
                                                   Optional('bdr_ip_addr'): str,
                                                   Optional('dr_router_id'): str,
                                                   Optional('bdr_router_id'): str,
                                                   'hello_options': str,
                                                   'dbd_options': str,
                                                   'last_non_hello_packet_received': str,
                                                   'dead_timer': str,
                                                   Optional('statistics'): {
                                                       Optional('nbr_event_count'): int,
                                                   },
                                                   },
                                                  },
                                                 },
                                             },
                                         Optional('virtual_links'):
                                            {Any():
                                                {'neighbors':
                                                 {Any():
                                                  {'neighbor_router_id': str,
                                                   'address': str,
                                                   'state': str,
                                                   'last_state_change': str,
                                                   Optional('priority'): int,
                                                   Optional('nbr_intf_id'): int,
                                                   Optional('dr_ip_addr'): str,
                                                   Optional('bdr_ip_addr'): str,
                                                   Optional('dr_router_id'): str,
                                                   Optional('bdr_router_id'): str,
                                                   'hello_options': str,
                                                   'dbd_options': str,
                                                   'last_non_hello_packet_received': str,
                                                   'dead_timer': str,
                                                   Optional('statistics'): {
                                                       Optional('nbr_event_count'): int,
                                                   },
                                                   },
                                                  },
                                                 },
                                             },
                                         },
                                     },
                                 },
                             },
                         },
                     },
                 },
             },
    }


# =======================================================
# Parser for 'show ipv6 ospfv3 neighbors detail [vrf <WORD>]'
# =======================================================
class ShowIpv6Ospfv3NeighborsDetail(ShowIpv6Ospfv3NeighborsDetailSchema):
    """Parser for:
        show ipv6 ospfv3 neighbors detail
        show ipv6 ospfv3 neighbors {neighbor} detail
        show ipv6 ospfv3 neighbors detail vrf {vrf}
        show ipv6 ospfv3 neighbors {neighbor} detail vrf {vrf}"""

    cli_command = ['show ipv6 ospfv3 neighbors detail vrf {vrf}',
                   'show ipv6 ospfv3 neighbors {neighbor} detail vrf {vrf}',
                   'show ipv6 ospfv3 neighbors {neighbor} detail',
                   'show ipv6 ospfv3 neighbors detail']
    exclude = [
        'dead_timer',
        'last_non_hello_packet_received',
        'last_state_change',
        'bdr_ip_addr',
        'dr_ip_addr',
        'nbr_event_count']

    def cli(self, vrf='', neighbor='', output=None):
        if vrf:
            if neighbor:
                cmd = self.cli_command[1].format(vrf=vrf, neighbor=neighbor)
            else:
                cmd = self.cli_command[0].format(vrf=vrf)
        else:
            if neighbor:
                cmd = self.cli_command[2].format(neighbor=neighbor)
            else:
                cmd = self.cli_command[3]

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}
        af = 'ipv4'
        # Neighbor 1.1.1.1, interface address fe80::2de:fbff:fed4:89c7
        p1 = re.compile(r'^Neighbor +(?P<neighbor_router_id>(\S+)),'
                        ' +interface +address +(?P<address>(\S+))$')
        # Process ID ospfv3_l3uls VRF default, in area 0.0.0.0 via interface Ethernet1/33
        p2 = re.compile(r'^Process +ID +(?P<instance>(\S+)) +VRF'
                        ' +(?P<vrf>(\S+)), +in +area +(?P<area>(\S+))'
                        ' +via +interface +(?P<interface>(\S+))$')
        # State is FULL, 5 state changes, last change 04:06:04
        p3 = re.compile(r'^State +is +(?P<state>(\S+)),'
                        ' +(?P<changes>(\d+)) +state +changes,'
                        ' +last +change +(?P<last>(\S+))$')
        # Neighbor priority is 1, Neighbor interface ID 37
        p4 = re.compile(
            r'^Neighbor +priority +is +(?P<priority>(\S+)),\s+Neighbor\s+interface\s+ID\s+(?P<nbr_intf_id>(\S+))$')
        # DR is 2.2.2.2 BDR is 1.1.1.1
        p5 = re.compile(r'^DR +is +(?P<dr_ip>(\S+)) +BDR +is'
                        ' +(?P<bdr_ip>(\S+))$')
        # Hello options 0x13, dbd options 0x13
        p6 = re.compile(r'^Hello +options +(?P<hello_options>(\S+)),'
                        ' +dbd +options +(?P<dbd_options>(\S+))$')
        # Last non-hello packet received 00:03:17
        p7 = re.compile(r'^Last +non-hello +packet +received'
                        ' +(?P<non_hello>(\S+))$')
        # Dead timer due in 00:00:33
        p8 = re.compile(r'^Dead +timer +due +in +(?P<dead_timer>(\S+))$')

        # capture vl interface
        # VL1-0.0.0.1-10.64.4.4
        vl_pattern = re.compile(r'(?P<link>\w+)-(?P<area_id>[\w\.\:]+)-(?P<router_id>[\w\.\:]+)')

        for line in out.splitlines():
            line = line.strip()

            # Neighbor 10.36.3.3, interface address 10.2.3.3
            m = p1.match(line)
            if m:
                neighbor = str(m.groupdict()['neighbor_router_id'])
                address = str(m.groupdict()['address'])
                continue

            # Process ID 1 VRF default, in area 0.0.0.0 via interface Ethernet2/2
            # Process ID 1 VRF default, in area 0.0.0.0 via interface VL1-0.0.0.1-10.64.4.4
            m = p2.match(line)
            if m:
                instance = str(m.groupdict()['instance'])
                vrf = str(m.groupdict()['vrf'])
                area = str(m.groupdict()['area'])
                interface = str(m.groupdict()['interface'])

                vrf_dict=ret_dict.setdefault('vrf',{})
                vrf_dict.setdefault(vrf, {})
                af_dict= vrf_dict[vrf].setdefault('address_family', {})
                af_dict.setdefault(af,{})
                inst_dict= af_dict[af].setdefault('instance',{})
                inst_dict.setdefault(instance,{})
                area_dict= inst_dict[instance].setdefault('areas',{})
                area_dict.setdefault(area,{})

                n = vl_pattern.match(interface)
                if n:
                    link = n.groupdict()['link']
                    area_id = n.groupdict()['area_id']
                    router_id = n.groupdict()['router_id']
                    # Set values for dict
                    intf_type = 'virtual_links'
                    intf_name = area_id + ' ' + router_id
                else:
                    # Set values for dict
                    intf_type = 'interfaces'
                    intf_name = interface

                # Set interface/virtual_link dict
                intf_dict=area_dict[area].setdefault(intf_type, {})
                intf_dict.setdefault(intf_name,{})
                neighbor_dict=intf_dict[intf_name].setdefault('neighbors',{})
                sub_dict=neighbor_dict.setdefault(neighbor,{})

                # Set previously parsed keys
                sub_dict['neighbor_router_id'] = neighbor
                sub_dict['address'] = address
                continue

            # State is FULL, 5 state changes, last change 08:38:40
            m = p3.match(line)
            if m:
                sub_dict['state'] = m.groupdict()['state'].lower()
                sub_dict['last_state_change'] = m.groupdict()['last']
                if 'statistics' not in sub_dict:
                    sub_dict['statistics'] = {}
                    sub_dict['statistics']['nbr_event_count'] = int(
                        m.groupdict()['changes'])
                    continue

            # Neighbor priority is 1, Neighbor interface ID 37
            m = p4.match(line)
            if m:
                sub_dict['priority'] = int(m.groupdict()['priority'])
                sub_dict['nbr_intf_id'] = int(m.groupdict()['nbr_intf_id'])
                continue

            # DR is 10.2.3.3 BDR is 10.2.3.2
            m = p5.match(line)
            if m:
                sub_dict['dr_ip_addr'] = m.groupdict()['dr_ip']
                sub_dict['bdr_ip_addr'] = m.groupdict()['bdr_ip']
                continue

            # Hello options 0x12, dbd options 0x52
            m = p6.match(line)
            if m:
                sub_dict['hello_options'] = m.groupdict()['hello_options']
                sub_dict['dbd_options'] = m.groupdict()['dbd_options']
                continue

            # Last non-hello packet received never
            m = p7.match(line)
            if m:
                sub_dict['last_non_hello_packet_received'] = \
                    m.groupdict()['non_hello']
                continue

            # Dead timer due in 00:00:39
            m = p8.match(line)
            if m:
                sub_dict['dead_timer'] = m.groupdict()['dead_timer']
                continue

        return ret_dict
