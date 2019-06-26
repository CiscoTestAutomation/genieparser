"""
    show_ipv6.py
    NXOS parsers for the following show commands:

    * show ipv6 neighbor detail vrf all
    * show ipv6 nd interface vrf all
    * show ipv6 icmp neighbor detail vrf all
    * show ipv6 routers vrf all


"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use
from genie.libs.parser.utils.common import Common

# ======================================================
# Parser for 'show ipv6 neighbor detail vrf all'
# ======================================================

class ShowIpv6NeighborsDetailVrfAllSchema(MetaParser):
    """
       Schema for "show ipv6 neighbor detail vrf all"
    """

    schema = {
        'interfaces': {
            Any(): {
                'interface': str,
                'neighbors': {
                    Any(): {
                        'ip': str,
                        'age': str,
                        'physical_interface': str,
                        'mac_addr': str,
                        'preference': str,
                        'source': str,
                        'packet_count': int,
                        'byte_count': int,
                        'best': str,
                        'throttled': str
                    },
                },
            },
        },
        'adjacency_hit': {
            Any(): {
                'packet_count': int,
                'byte_count': int
            },
        },
        'adjacency_statistics_last_updated_before': str,
        'total_number_of_entries': int
    }

class ShowIpv6NeighborsDetailVrfAll(ShowIpv6NeighborsDetailVrfAllSchema):
    """
       Parser for "show ipv6 neighbor detail vrf all"
    """

    cli_command = 'show ipv6 neighbor detail vrf all'
    exclude = ['age']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}


        # No. of Adjacency hit with type INVALID: Packet count 0, Byte count 0
        # No. of Adjacency hit with type GLOBAL DROP: Packet count 0, Byte count 0
        # No. of Adjacency hit with type GLOBAL PUNT: Packet count 0, Byte count 0
        # No. of Adjacency hit with type GLOBAL GLEAN: Packet count 0, Byte count 0
        # No. of Adjacency hit with type GLEAN: Packet count 0, Byte count 0
        # No. of Adjacency hit with type NORMAL: Packet count 0, Byte count 0
        p1 = re.compile(r'^No. +of +Adjacency +hit +with +type +(?P<adjacency>([\w\s]+)): +Packet +count +'
                         '(?P<packet_count>(\d+)), +Byte +count +(?P<byte_count>(\d+))$')

        # Adjacency statistics last updated before: never
        p2 = re.compile(r'^Adjacency +statistics +last +updated +before: +(?P<adjacency_statistics_last_updated_before>(\w+))$')

        # IPv6 Adjacency Table for all VRFs
        # Total number of entries: 11
        p3 = re.compile(r'^Total +number +of +entries: +(?P<total_number_of_entries>(\d+))$')

        #Address :   2010:2:3::2
        p4_1 = re.compile(r'Address : +(?P<ip>\S+)$')

        #Age :                00:09:27
        p4_2 =re.compile(r'Age : +(?P<age>\S+)$')

        #MacAddr :            fa16.3e82.6320
        p4_3 = re.compile(r'MacAddr : +(?P<mac_addr>\S+)$')

        #Preference :         50  
        p4_4 = re.compile(r'Preference : +(?P<preference>\S+)$')

        #Source :             icmpv6         
        p4_5 = re.compile(r'Source : +(?P<source>(\w+))$')

        # Interface :          Ethernet1/1    
        p4_6 = re.compile(r'^Interface : +(?P<interface>\S+)$')

        #Physical Interface : Ethernet1/1      
        p4_7 = re.compile(r'Physical Interface : +(?P<physical_interface>(\S+))$')

        #Packet Count :       0   
        p4_8 = re.compile(r'Packet Count : +(?P<packet_count>(\d+))$')

        #Byte Count :         0   
        p4_9 = re.compile(r'Byte Count : +(?P<byte_count>(\d+))$')

        #Best :               Yes
        p4_10 = re.compile(r'Best : +(?P<best>(\w+))$')

        #Throttled :           No
        p4_11 = re.compile(r'Throttled : +(?P<throttled>(\w+))$')

        for line in out.splitlines():

            line = line.strip()

            # No. of Adjacency hit with type NORMAL: Packet count 0, Byte count 0
            m = p1.match(line)
            if m:
                adjacency = m.groupdict()['adjacency']
                packet_count = int(m.groupdict()['packet_count'])
                byte_count = int(m.groupdict()['byte_count'])

                adjacency_dict = ret_dict.setdefault('adjacency_hit', {}).setdefault(adjacency, {})
                adjacency_dict['packet_count'] = packet_count
                adjacency_dict['byte_count'] = byte_count
                continue

            # Adjacency statistics last updated before: never
            m = p2.match(line)
            if m:
                ret_dict['adjacency_statistics_last_updated_before'] = m.groupdict()['adjacency_statistics_last_updated_before']
                continue

            # Total number of entries: 11
            m = p3.match(line)
            if m:
                ret_dict['total_number_of_entries'] = int(m.groupdict()['total_number_of_entries'])
                continue

            # Address :       2010:2:3::2
            m = p4_1.match(line)
            if m:
                flag = 1
                ip = m.groupdict()['ip']
                continue

            # Age :                00:09:27
            m = p4_2.match(line)
            if m:
                age = m.groupdict()['age']
                flag = 1
                continue

            # MacAddr :            fa16.3e82.6320
            m = p4_3.match(line)
            if m:
                mac_addr = m.groupdict()['mac_addr']
                flag = 1
                continue

            # Preference :         50  
            m = p4_4.match(line)
            if m:
                preference = m.groupdict()['preference']
                flag = 1
                continue

            # Source :             icmpv6         
            m = p4_5.match(line)
            if m:
                source = m.groupdict()['source']
                flag = 1
                continue


            # Interface :          Ethernet1/1    
            m = p4_6.match(line)
            if m:
                interface_flag = 1
                interface = m.groupdict()['interface']
                interface_dict = ret_dict.setdefault('interfaces', {}).setdefault(interface, {})
                interface_dict['interface'] = interface
                continue


            # Physical Interface : Ethernet1/1      
            m = p4_7.match(line)
            if m:
                physical_interface = m.groupdict()['physical_interface']
                continue

            # Packet Count :       0   
            m = p4_8.match(line)
            if m:
                packet_count = m.groupdict()['packet_count']
                continue

            # Byte Count :         0   
            m = p4_9.match(line)
            if m:
                byte_count = m.groupdict()['byte_count']
                continue

            # Best :               Yes
            m = p4_10.match(line)
            if m:
                best = m.groupdict()['best']
                continue

            # Throttled :           No
            m = p4_11.match(line)
            if m:
                throttled = m.groupdict()['throttled']

                if interface_flag == 1 and flag == 1:
                    neighbour_dict = interface_dict.setdefault('neighbors', {}).setdefault(ip, {})
                    neighbour_dict['best'] = best
                    neighbour_dict['throttled'] = throttled
                    neighbour_dict['byte_count'] = int(byte_count)
                    neighbour_dict['packet_count'] = int(packet_count)
                    neighbour_dict['age'] = age
                    neighbour_dict['ip'] = ip
                    neighbour_dict['source'] = source
                    neighbour_dict['preference'] = preference
                    neighbour_dict['mac_addr'] = mac_addr
                    neighbour_dict['physical_interface'] = physical_interface

                continue

        return ret_dict

# ======================================================
# Parser for 'show ipv6 nd interface vrf all'
# ======================================================

class ShowIpv6NdInterfaceVrfAllSchema(MetaParser):
    """
       Schema for "show ipv6 nd interface vrf all"
    """

    schema = {        
        Optional('interfaces'): {
            Any(): {
                'vrf': str,
                'interface': str,
                'interface_status': str,
                'ipv6_address': {
                    Any(): {
                        'status': str,
                    },
                },
                'ipv6_link_local_address': {
                    Any(): {
                        'status': str,
                    },
                },
                'nd_mac_extract': str,
                'icmpv6_active_timers': {
                    'last_neighbor_solicitation_sent': str,
                    'last_neighbor_advertisement_sent': str,
                    'last_router_advertisement_sent': str,
                    'next_router_advertisement_sent': str},
                'router_advertisement': {
                    'periodic_interval_seconds': str,
                    'send_managed_address_configuration_flag': str,
                    'send_other_stateful_configuration_flag': str,
                    'send_default_router_preference_value': str,
                    'send_current_hop_limit': int,
                    'send_mtu': int,
                    'send_router_lifetime_secs': int,
                    'send_reachable_time_ms': int,
                    'send_retrans_timer_ms': int,
                    'suppress_ra': str,
                    'suppress_mtu_ra': str,
                    'suppress_route_information_option_ra': str,
                },
                'neighbor_solicitation': {
                    'ns_retransmit_interval_ms': int,
                    'nd_nud_retry_base': int,
                    'nd_nud_retry_interval': int,
                    'nd_nud_retry_attempts': int,
                },
                'icmpv6_error_message': {
                    'send_redirects_num': int,
                    'send_unreachables': str,
                },
                'icmpv6_dad': {
                    'maximum_dad_attempts': int,
                    'current_dad_attempt': int,
                }
            },
        },
    }


class ShowIpv6NdInterfaceVrfAll(ShowIpv6NdInterfaceVrfAllSchema):
    """
       Parser for "show ipv6 nd interface vrf all"
    """

    cli_command = 'show ipv6 nd interface vrf all'
    exclude = ['last_router_advertisement_sent' , 'next_router_advertisement_sent',
                'last_neighbor_advertisement_sent', 'last_neighbor_solicitation_sent']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}

        # ICMPv6 ND Interfaces for VRF "default"
        p1 = re.compile(r'^(?P<nd_interface>([\w\s]+)) +Interfaces +for +VRF +"(?P<vrf>(\w+))"$')

        # Ethernet1/1, Interface status: protocol-up/link-up/admin-up
        p2 = re.compile(r'^(?P<interface>\S+), +Interface +status: +(?P<interface_status>([\w\-\/]+))$')

        # IPv6 address:
        p3 = re.compile(r'IPv6 +address:$')

        # 2010:2:3::3/64 [VALID]
        p3_1 = re.compile(r'^(?P<ipv6_address>([\w\/\:]+)) +\[(?P<status>(\w+))\]$')

        # IPv6 link-local address: fe80::5c01:c0ff:fe02:7 [VALID]
        p4 = re.compile(r'^IPv6 +link-local +address: +(?P<ipv6_link_local_address>([\w\:]+)) +'
                         '\[(?P<status>(\w+))\]$')
        # ND mac-extract : Disabled
        p5 = re.compile(r'^ND +mac-extract : +(?P<nd_mac_extract>(\w+))$')

        # ICMPv6 active timers:
        p6 = re.compile(r'ICMPv6 +active +timers:$')

        # Last Neighbor-Solicitation sent: 00:06:16
        p6_1 = re.compile(r'^Last +Neighbor-Solicitation +sent: +(?P<last_neighbor_solicitation_sent>([\w\:]+))$')

        # Last Neighbor-Advertisement sent: 00:02:12
        p6_2 = re.compile(r'^Last +Neighbor-Advertisement +sent: +(?P<last_neighbor_advertisement_sent>([\w\:]+))$')

        # Last Router-Advertisement sent: 1d18h
        p6_3 = re.compile(r'^Last +Router-Advertisement +sent: +(?P<last_router_advertisement_sent>([\w\:]+))$')

        # Next Router-Advertisement sent in: 0.000000
        p6_4 = re.compile(r'^Next +Router-Advertisement +sent +in: +(?P<next_router_advertisement_sent>([\w\:\.]+))$')

        # Router-Advertisement parameters:
        p7 = re.compile(r'^Router-Advertisement +parameters:$')

        # Periodic interval: 200 to 201 seconds
        p7_1 = re.compile(r'^Periodic +interval: +(?P<periodic_interval_seconds>([\s\w]+)) seconds$')

        # Send "Managed Address Configuration" flag: false
        p7_2 = re.compile(r'^Send +"Managed Address Configuration" +flag: +(?P<managed_address_configuration_flag>(\w+))$')

        # Send "Other Stateful Configuration" flag: false
        p7_3 = re.compile(r'^Send +"Other Stateful Configuration" +flag: +(?P<other_stateful_configuration_flag>(\w+))$')

        # Send "Default Router Preference" value: Medium
        p7_4 = re.compile(r'^Send +"Default Router Preference" +value: +(?P<default_router_preference_value>(\w+))$')

        # Send "Current Hop Limit" field: 64
        p7_5 = re.compile(r'^Send +"Current Hop Limit" +field: +(?P<current_hop_limit>(\d+))$')

        # Send "MTU" option value: 1500
        p7_6 = re.compile(r'^Send +"MTU" +option +value: +(?P<mtu>(\d+))$')

        # Send "Router Lifetime" field: 1801 secs
        p7_7 = re.compile(r'^Send +"Router Lifetime" +field: +(?P<router_lifetime_secs>(\d+)) secs$')

        # Send "Reachable Time" field: 0 ms
        p7_8 = re.compile(r'^Send +"Reachable Time" +field: +(?P<reachable_time_ms>(\d+)) ms$')

        # Send "Retrans Timer" field: 0 ms
        p7_9 = re.compile(r'^Send +"Retrans Timer" +field: +(?P<retrans_timer_ms>(\d+)) ms$')

        # Suppress RA: Enabled
        p7_10 = re.compile(r'^Suppress +RA: +(?P<suppress_ra>(\w+))$')

        # Suppress MTU in RA: Disabled
        p7_11 = re.compile(r'^Suppress +MTU +in +RA: +(?P<suppress_mtu_ra>(\w+))$')

        # Suppress Route Information Option in RA: Disabled
        p7_12 = re.compile(r'^Suppress +Route +Information +Option +in +RA: +(?P<suppress_route_information_option_ra>(\w+))$')

        # Neighbor-Solicitation parameters:
        p8 = re.compile(r'^Neighbor-Solicitation +parameters:$')

        # NS retransmit interval: 1000 ms
        p8_1 = re.compile(r'^NS +retransmit +interval: +(?P<ns_retransmit_interval_ms>(\d+)) ms$')

        # ND NUD retry base: 1
        p8_2 = re.compile(r'^ND +NUD +retry +base: +(?P<nd_nud_retry_base>(\d+))$')

        # ND NUD retry interval: 1000
        p8_3 = re.compile(r'^ND +NUD +retry +interval: +(?P<nd_nud_retry_interval>(\d+))$')

        # ND NUD retry attempts: 3
        p8_4 = re.compile(r'^ND +NUD +retry +attempts: +(?P<nd_nud_retry_attempts>(\d+))$')

        # ICMPv6 error message parameters:
        p9 = re.compile(r'^ICMPv6 +error +message +parameters:$')

        # Send redirects: true (0)
        p9_1 = re.compile(r'^Send +redirects: +(?P<send_redirects>(\w+))\s+\((?P<send_redirects_num>(\d+))\)$')

        # Send unreachables: false
        p9_2 = re.compile(r'^Send unreachables: +(?P<send_unreachables>(\w+))$')

        # ICMPv6 DAD parameters:
        p10 = re.compile(r'^ICMPv6 +DAD +parameters:$')

        # Maximum DAD attempts: 1
        p10_1 = re.compile(r'^Maximum +DAD +attempts: +(?P<maximum_dad_attempts>(\d+))$')

        # Current DAD attempt : 1
        p10_2 = re.compile(r'Current +DAD +attempt : +(?P<current_dad_attempt>(\d+))$')

        for line in out.splitlines():

            line = line.strip()

            # ICMPv6 ND Interfaces for VRF "default"
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                continue

            # Ethernet1/1, Interface status: protocol-up/link-up/admin-up
            m = p2.match(line)
            if m:
                interface = m.groupdict()['interface']
                interface_status = m.groupdict()['interface_status']

                interface_dict = ret_dict.setdefault('interfaces', {}).setdefault(interface, {})
                interface_dict['interface'] = interface
                interface_dict['interface_status'] = interface_status
                interface_dict['vrf'] = vrf
                continue

            # IPv6 address:
            m = p3.match(line)
            if m:
                ipv6_address_dict = interface_dict.setdefault('ipv6_address', {})
                continue

            # 2010:2:3::3/64 [VALID]
            m = p3_1.match(line)
            if m:
                ipv6_address= m.groupdict()['ipv6_address']
                status = m.groupdict()['status']
                ipv6_dict = ipv6_address_dict.setdefault(ipv6_address, {})
                ipv6_dict['status'] = status
                continue

            # IPv6 link-local address: fe80::5c01:c0ff:fe02:7 [VALID]
            m = p4.match(line)
            if m:
                ipv6_link_local_address = m.groupdict()['ipv6_link_local_address']
                status = m.groupdict()['status']
                ipv6_link_local_address_dict = interface_dict.setdefault('ipv6_link_local_address', {}).setdefault(ipv6_link_local_address, {})
                ipv6_link_local_address_dict['status'] = status
                continue

            # ND mac-extract : Disabled
            m = p5.match(line)
            if m:
                interface_dict['nd_mac_extract'] = m.groupdict()['nd_mac_extract']
                continue

            # ICMPv6 active timers:
            m = p6.match(line)
            if m:
                icmp_dict = interface_dict.setdefault('icmpv6_active_timers', {})
                continue

            # Last Neighbor-Solicitation sent: 00:06:16
            m = p6_1.match(line)
            if m:
                icmp_dict['last_neighbor_solicitation_sent'] = m.groupdict()['last_neighbor_solicitation_sent']
                continue

            # Last Neighbor-Advertisement sent: 00:02:12
            m = p6_2.match(line)
            if m:
                icmp_dict['last_neighbor_advertisement_sent'] = m.groupdict()['last_neighbor_advertisement_sent']
                continue

            # Last Router-Advertisement sent: 1d18h
            m = p6_3.match(line)
            if m:
                icmp_dict['last_router_advertisement_sent'] = m.groupdict()['last_router_advertisement_sent']
                continue

            # Next Router-Advertisement sent in: 0.000000
            m = p6_4.match(line)
            if m:
                icmp_dict['next_router_advertisement_sent'] = m.groupdict()['next_router_advertisement_sent']
                continue

            # Router-Advertisement parameters:
            m = p7.match(line)
            if m:
                router_dict = interface_dict.setdefault('router_advertisement', {})
                continue

            # Periodic interval: 200 to 201 seconds
            m = p7_1.match(line)
            if m:
                periodic_interval_seconds = m.groupdict()['periodic_interval_seconds']
                periodic_interval_seconds = periodic_interval_seconds.replace(' ', '').replace('to', '-')
                router_dict['periodic_interval_seconds'] = periodic_interval_seconds
                continue

            # Send "Managed Address Configuration" flag: false
            m = p7_2.match(line)
            if m:
                router_dict['send_managed_address_configuration_flag'] = m.groupdict()['managed_address_configuration_flag']
                continue

            # Send "Other Stateful Configuration" flag: false
            m = p7_3.match(line)
            if m:
                router_dict['send_other_stateful_configuration_flag'] = m.groupdict()['other_stateful_configuration_flag']
                continue

            # Send "Default Router Preference" value: Medium
            m = p7_4.match(line)
            if m:
                router_dict['send_default_router_preference_value'] = m.groupdict()['default_router_preference_value']
                continue

            # Send "Current Hop Limit" field: 64
            m = p7_5.match(line)
            if m:
                router_dict['send_current_hop_limit'] = int(m.groupdict()['current_hop_limit'])
                continue

            # Send "MTU" option value: 1500
            m = p7_6.match(line)
            if m:
                router_dict['send_mtu'] = int(m.groupdict()['mtu'])
                continue

            # Send "Router Lifetime" field: 1801 secs
            m = p7_7.match(line)
            if m:
                router_dict['send_router_lifetime_secs'] = int(m.groupdict()['router_lifetime_secs'])
                continue

            # Send "Reachable Time" field: 0 ms
            m = p7_8.match(line)
            if m:
                router_dict['send_reachable_time_ms'] = int(m.groupdict()['reachable_time_ms'])
                continue

            # Send "Retrans Timer" field: 0 ms
            m = p7_9.match(line)
            if m:
                router_dict['send_retrans_timer_ms'] = int(m.groupdict()['retrans_timer_ms'])
                continue

            # Suppress RA: Enabled
            m = p7_10.match(line)
            if m:
                router_dict['suppress_ra'] = m.groupdict()['suppress_ra']
                continue

            # Suppress MTU in RA: Disabled
            m = p7_11.match(line)
            if m:
                router_dict['suppress_mtu_ra'] = m.groupdict()['suppress_mtu_ra']
                continue

            # Suppress Route Information Option in RA: Disabled
            m = p7_12.match(line)
            if m:
                router_dict['suppress_route_information_option_ra'] = m.groupdict()['suppress_route_information_option_ra']
                continue

            # Neighbor-Solicitation parameters:
            m = p8.match(line)
            if m:
                neighbor_dict = interface_dict.setdefault('neighbor_solicitation', {})
                continue

            # NS retransmit interval: 1000 ms
            m = p8_1.match(line)
            if m:
                neighbor_dict['ns_retransmit_interval_ms'] = int(m.groupdict()['ns_retransmit_interval_ms'])
                continue

            # ND NUD retry base: 1
            m = p8_2.match(line)
            if m:
                neighbor_dict['nd_nud_retry_base'] = int(m.groupdict()['nd_nud_retry_base'])
                continue

            # ND NUD retry interval: 1000
            m = p8_3.match(line)
            if m:
                neighbor_dict['nd_nud_retry_interval'] = int(m.groupdict()['nd_nud_retry_interval'])
                continue

            # ND NUD retry attempts: 3
            m = p8_4.match(line)
            if m:
                neighbor_dict['nd_nud_retry_attempts'] = int(m.groupdict()['nd_nud_retry_attempts'])
                continue

            # ICMPv6 error message parameters:
            m = p9.match(line)
            if m:
                icmp_error_dict = interface_dict.setdefault('icmpv6_error_message', {})
                continue

            # Send redirects: true (0)
            m = p9_1.match(line)
            if m:
                icmp_error_dict['send_redirects_num'] = int(m.groupdict()['send_redirects_num'])
                continue

            # Send unreachables: false
            m = p9_2.match(line)
            if m:
                icmp_error_dict['send_unreachables'] = m.groupdict()['send_unreachables']
                continue

            # ICMPv6 DAD parameters:
            m = p10.match(line)
            if m:
                icmp_dad_dict = interface_dict.setdefault('icmpv6_dad', {})
                continue

            # Maximum DAD attempts: 1
            m = p10_1.match(line)
            if m:
                icmp_dad_dict['maximum_dad_attempts'] = int(m.groupdict()['maximum_dad_attempts'])
                continue

            # Current DAD attempt : 1
            m = p10_2.match(line)
            if m:
                icmp_dad_dict['current_dad_attempt'] = int(m.groupdict()['current_dad_attempt'])
                continue

        return ret_dict


# ===========================================================
# Parser for 'show ipv6 icmp neighbor detail vrf all'
# ===========================================================
class ShowIpv6IcmpNeighborDetailVrfAllSchema(MetaParser):
    """
        Schema for "show ipv6 icmp neighbor detail vrf all"
    """

    schema = {
        'interfaces': {
            Any(): {
                'interface': str,
                'phy_interface': str,
                'neighbors': {
                    Any(): {
                        'ip': str,
                        'age': str,
                        'mac_address': str,
                        'state': str
                    },
                },
            },
        },
    }

class ShowIpv6IcmpNeighborDetailVrfAll(ShowIpv6IcmpNeighborDetailVrfAllSchema):
    """
        Parser for "show ipv6 icmp neighbor detail vrf all"
    """

    cli_command = 'show ipv6 icmp neighbor detail vrf all'
    exclude = ['age']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}

        # ICMPv6 Adjacency Table for all VRFs 
        p0 = re.compile(r'^ICMPv6 Adjacency Table for all VRFs$')

        # Address         Age       MAC Address     State      Interface  Phy-Interface
        # 2010:2:3::2     00:15:02  fa16.3e82.6320  STALE       Eth1/1      Eth1/1    
        p1 = re.compile(r'^(?P<ip>([\w\:]+)) +(?P<age>([\w\:]+)) +(?P<mac_address>([\w\.]+)) +(?P<state>(\w+)) +'
                         '(?P<interface>\S+) +(?P<phy_interface>(\S+))$')

        # fe80::f816:3eff:fe82:6320
        p2 = re.compile(r'^(?P<ip>([\w\:]+))$')

        #                 00:18:33  fa16.3e82.6320  STALE       Eth1/1      Eth1/1    
        p3 = re.compile(r'^(?P<age>([\w\:]+)) +(?P<mac_address>([\w\.]+)) +(?P<state>(\w+)) +(?P<interface>(\S+)) +'
                         '(?P<phy_interface>(\S+))$')

        for line in out.splitlines():

            line = line.strip()

            # ICMPv6 Adjacency Table for all VRFs 
            m = p0.match(line)
            if m:
                continue

            # 2010:2:3::2     00:15:02  fa16.3e82.6320  STALE       Eth1/1      Eth1/1    
            m = p1.match(line)
            if m:
                interfaces = Common.convert_intf_name(m.groupdict()['interface'])
                interface = m.groupdict()['interface']
                ip = m.groupdict()['ip']
                age = m.groupdict()['age']
                mac_address = m.groupdict()['mac_address']
                state = m.groupdict()['state']
                phy_interface = m.groupdict()['phy_interface']

                interface_dict = ret_dict.setdefault('interfaces', {}).setdefault(interfaces, {})
                interface_dict['interface'] = interface
                interface_dict['phy_interface'] = phy_interface

                neighbor_dict = interface_dict.setdefault('neighbors', {}).setdefault(ip, {})
                neighbor_dict['ip'] = ip
                neighbor_dict['age'] = age
                neighbor_dict['mac_address'] = mac_address
                neighbor_dict['state'] = state
                continue

            # fe80::f816:3eff:fe82:6320
            m = p2.match(line)
            if m:
                ip = m.groupdict()['ip']
                ip_flag = 1
                continue

            #                 00:18:33  fa16.3e82.6320  STALE       Eth1/1      Eth1/1    
            m = p3.match(line)
            if m:
                interfaces = Common.convert_intf_name(m.groupdict()['interface'])
                interface = m.groupdict()['interface']
                age = m.groupdict()['age']
                mac_address = m.groupdict()['mac_address']
                state = m.groupdict()['state']
                phy_interface = m.groupdict()['phy_interface']

                interface_dict = ret_dict.setdefault('interfaces', {}).setdefault(interfaces, {})
                interface_dict['interface'] = interface
                interface_dict['phy_interface'] = phy_interface

                if ip_flag == 1:
                    neighbor_dict = interface_dict.setdefault('neighbors', {}).setdefault(ip, {})
                    neighbor_dict['ip'] = ip
                    neighbor_dict['age'] = age
                    neighbor_dict['mac_address'] = mac_address
                    neighbor_dict['state'] = state
                continue

        return ret_dict


# ======================================================
# Parser for 'show ipv6 routers vrf all'
# ======================================================

class ShowIpv6RoutersVrfAllSchema(MetaParser):
    """
       Schema for "show ipv6 routers vrf all"
    """

    schema = {
        'interfaces': {
            Any(): {
                'interface': str,  # Conf/Ops Str
                'router_advertisement': {
                    'router': str,
                    'last_update_time_min': str,
                    'current_hop_limit': int,
                    'lifetime': int,
                    'addrFlag': int,
                    'other_flag': int,
                    'mtu': int,
                    'home_agent_flag': int,
                    'preference': str,
                    'reachable_time_msec': int,
                    'retransmission_time': int,
                    'prefix': {
                        Any(): {
                            'onlink_flag': int,
                            'autonomous_flag': int,
                            'valid_lifetime': int,
                            'preferred_lifetime': int
                        },
                    },
                },
            }
        }
    }

class ShowIpv6RoutersVrfAll(ShowIpv6RoutersVrfAllSchema):
    """
       Parser for "show ipv6 routers vrf all"
    """

    cli_command = 'show ipv6 routers vrf all'
    exclude = ['last_update_time_min']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}

        # Router fe80::f816:3eff:fe82:6320 on Ethernet1/1 , last update time 3.2 min
        p1 = re.compile(r'^Router +(?P<router>\S+) +on +(?P<interface>\S+) , +last +update +time +(?P<last_update_time_min>\S+) min$')

        # Current_hop_limit 64, Lifetime 1800, AddrFlag 0, OtherFlag 0, MTU 1500
        p2 = re.compile(r'^Current_hop_limit +(?P<current_hop_limit>(\d+)), +Lifetime +(?P<lifetime>(\d+)), +AddrFlag +'
                         '(?P<addrFlag>(\d+)), +OtherFlag +(?P<other_flag>(\d+)), +MTU +(?P<mtu>(\d+))$')

        # HomeAgentFlag 0, Preference Medium
        p3 = re.compile(r'^HomeAgentFlag +(?P<home_agent_flag>(\d+)), +Preference +(?P<preference>(\w+))$')

        # Reachable time 0 msec, Retransmission time 0 msec
        p4 = re.compile(r'^Reachable +time +(?P<reachable_time_msec>(\d+)) msec, +Retransmission +time +'
                         '(?P<retransmission_time>(\d+)) msec$')

        #   Prefix 2010:2:3::/64  onlink_flag 1 autonomous_flag 1
        p5 = re.compile(r'^Prefix +(?P<prefix>([\w\:\/]+))\s+onlink_flag +(?P<onlink_flag>(\d+)) +autonomous_flag +'
                         '(?P<autonomous_flag>(\d+))')

        #   valid lifetime 2592000, preferred lifetime 604800
        p6 = re.compile(r'^valid +lifetime +(?P<valid_lifetime>(\d+)), +preferred +lifetime +(?P<preferred_lifetime>(\d+))$')

        for line in out.splitlines():

            line = line.strip()

            # Router fe80::f816:3eff:fe82:6320 on Ethernet1/1 , last update time 3.2 min
            m = p1.match(line)
            if m:
                router = m.groupdict()['router']
                interface = m.groupdict()['interface']
                last_update_time_min = m.groupdict()['last_update_time_min']

                interface_dict = ret_dict.setdefault('interfaces', {}).setdefault(interface, {})
                interface_dict['interface'] = interface

                router_dict = interface_dict.setdefault('router_advertisement', {})
                router_dict['router'] = router
                router_dict['last_update_time_min'] = last_update_time_min
                continue

            # Current_hop_limit 64, Lifetime 1800, AddrFlag 0, OtherFlag 0, MTU
            m = p2.match(line)
            if m:
                router_dict['current_hop_limit'] = int(m.groupdict()['current_hop_limit'])
                router_dict['lifetime'] = int(m.groupdict()['lifetime'])
                router_dict['addrFlag'] = int(m.groupdict()['addrFlag'])
                router_dict['other_flag'] = int(m.groupdict()['other_flag'])
                router_dict['mtu'] = int(m.groupdict()['mtu'])
                continue

            # HomeAgentFlag 0, Preference Medium
            m = p3.match(line)
            if m:
                router_dict['home_agent_flag'] = int(m.groupdict()['home_agent_flag'])
                router_dict['preference'] = m.groupdict()['preference']
                continue

            # Reachable time 0 msec, Retransmission time 0 msec
            m = p4.match(line)
            if m:
                router_dict['reachable_time_msec'] = int(m.groupdict()['reachable_time_msec'])
                router_dict['retransmission_time'] = int(m.groupdict()['retransmission_time'])
                continue

            #   Prefix 2010:2:3::/64  onlink_flag 1 autonomous_flag 1
            m = p5.match(line)
            if m:
                prefix = m.groupdict()['prefix']
                prefix_dict = router_dict.setdefault('prefix', {}).setdefault(prefix, {})
                prefix_dict['onlink_flag'] = int(m.groupdict()['onlink_flag'])
                prefix_dict['autonomous_flag'] = int(m.groupdict()['autonomous_flag'])
                continue

            #   valid lifetime 2592000, preferred lifetime 604800
            m = p6.match(line)
            if m:
                prefix_dict['valid_lifetime'] = int(m.groupdict()['valid_lifetime'])
                prefix_dict['preferred_lifetime'] = int(m.groupdict()['preferred_lifetime'])
                continue

        return ret_dict

