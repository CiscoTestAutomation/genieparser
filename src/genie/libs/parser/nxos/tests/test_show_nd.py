
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Parser
from genie.libs.parser.nxos.show_nd import ShowIpv6NeighborDetail,\
                                ShowIpv6NdInterface,\
                                ShowIpv6IcmpNeighborDetail,\
                                ShowIpv6Routers
# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError


# ============================================
#  Unit test for 'show ipv6 neighbor detail
# ============================================

class test_show_ipv6_neighbor_detail(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces':{
            'Ethernet1/1':{
                'interface': 'Ethernet1/1',
                'neighbors': {
                    '2001:db8:c56d:4::2': {
                        'ip': '2001:db8:c56d:4::2',
                        'link_layer_address': 'fa16.3eff.e5a2',
                        'age': '00:09:27',
                        'preference': 50,
                        'origin': 'other',
                        'physical_interface': 'Ethernet1/1',
                        'packet_count': 0,
                        'byte_count': 0,
                        'best': 'Yes',
                        'throttled': 'No',
                    },
                    '2001:db8:c56d:4::33': {
                        'ip': '2001:db8:c56d:4::33',
                        'link_layer_address': 'aabb.beff.bcbc',
                        'age': '2d15h',
                        'preference': 1,
                        'origin': 'static',
                        'physical_interface': 'Ethernet1/1',
                        'packet_count': 0,
                        'byte_count': 0,
                        'best': 'Yes',
                        'throttled': 'No',
                    },
                    'fe80::f816:3eff:feff:e5a2': {
                        'ip': 'fe80::f816:3eff:feff:e5a2',
                        'link_layer_address': 'fa16.3eff.e5a2',
                        'age': '00:05:42',
                        'preference': 50,
                        'origin': 'other',
                        'physical_interface': 'Ethernet1/1',
                        'packet_count': 0,
                        'byte_count': 0,
                        'best': 'Yes',
                        'throttled': 'No',
                        },
                    '2001:db8:c56d:4::34': {
                        'ip': '2001:db8:c56d:4::34',
                        'link_layer_address': 'aaab.beff.bcbe',
                        'age': '1d18h',
                        'preference': 1,
                        'origin': 'static',
                        'physical_interface': 'Ethernet1/1',
                        'packet_count': 0,
                        'byte_count': 0,
                        'best': 'Yes',
                        'throttled': 'No',
                    },
                },
            },
            'Ethernet1/2':{
                'interface': 'Ethernet1/2',
                'neighbors':{
                    '2001:db8:c8d1:4::33': {
                        'ip': '2001:db8:c8d1:4::33',
                        'link_layer_address': 'aaaa.bbff.8888',
                        'age': '2d15h',
                        'preference': 1,
                        'origin': 'static',
                        'physical_interface': 'Ethernet1/2',
                        'packet_count': 0,
                        'byte_count': 0,
                        'best': 'Yes',
                        'throttled': 'No',
                    },
                },
            },
        },
        'adjacency_hit': {
            'GLEAN': {
                'byte_count': 0,
                'packet_count': 0
            },
            'GLOBAL DROP': {
                'byte_count': 0,
                'packet_count': 0
            },
            'GLOBAL GLEAN': {
                'byte_count': 0,
                'packet_count': 0
            },
            'GLOBAL PUNT': {
                'byte_count': 0,
                'packet_count': 0
            },
            'INVALID': {
                'byte_count': 0,
                'packet_count': 0
            },
            'NORMAL': {
                'byte_count': 0,
                'packet_count': 0
            }
        },
        'adjacency_statistics_last_updated_before': 'never',
	    'total_number_of_entries': 11
    }

    golden_output = {'execute.return_value': '''
        n9kv-3# show ipv6 neighbor detail vrf all
        No. of Adjacency hit with type INVALID: Packet count 0, Byte count 0
        No. of Adjacency hit with type GLOBAL DROP: Packet count 0, Byte count 0
        No. of Adjacency hit with type GLOBAL PUNT: Packet count 0, Byte count 0
        No. of Adjacency hit with type GLOBAL GLEAN: Packet count 0, Byte count 0
        No. of Adjacency hit with type GLEAN: Packet count 0, Byte count 0
        No. of Adjacency hit with type NORMAL: Packet count 0, Byte count 0

        Adjacency statistics last updated before: never

        IPv6 Adjacency Table for all VRFs
        Total number of entries: 11

        Address :            2001:db8:c56d:4::2
        Age :                00:09:27
        MacAddr :            fa16.3eff.e5a2
        Preference :         50
        Source :             icmpv6
        Interface :          Ethernet1/1
        Physical Interface : Ethernet1/1
        Packet Count :       0
        Byte Count :         0
        Best :               Yes
        Throttled :           No

        Address :            2001:db8:c56d:4::33
        Age :                   2d15h
        MacAddr :            aabb.beff.bcbc
        Preference :         1
        Source :             Static
        Interface :          Ethernet1/1
        Physical Interface : Ethernet1/1
        Packet Count :       0
        Byte Count :         0
        Best :               Yes
        Throttled :           No

        Address :            2001:db8:c56d:4::34
        Age :                   1d18h
        MacAddr :            aaab.beff.bcbe
        Preference :         1
        Source :             Static
        Interface :          Ethernet1/1
        Physical Interface : Ethernet1/1
        Packet Count :       0
        Byte Count :         0
        Best :               Yes
        Throttled :          No

        Address :            fe80::f816:3eff:feff:e5a2
        Age :                00:05:42
        MacAddr :            fa16.3eff.e5a2
        Preference :         50
        Source :             icmpv6
        Interface :          Ethernet1/1
        Physical Interface : Ethernet1/1
        Packet Count :       0
        Byte Count :         0
        Best :               Yes
        Throttled :          No


        Address :            2001:db8:c8d1:4::33
        Age :                   2d15h
        MacAddr :            aaaa.bbff.8888
        Preference :         1
        Source :             Static
        Interface :          Ethernet1/2
        Physical Interface : Ethernet1/2
        Packet Count :       0
        Byte Count :         0
        Best :               Yes
        Throttled :          No
    '''}

    def test_show_ipv6_neighbor_detail_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6NeighborDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_ipv6_neighbor_detail_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6NeighborDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


class test_show_ipv6_nd_interface(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value':'''
        n9kv-3# show ipv6 nd interface vrf all
        ICMPv6 ND Interfaces for VRF "default"
        Ethernet1/1, Interface status: protocol-up/link-up/admin-up
        IPv6 address:
            2001:db8:c56d:4::3/64 [VALID]
        IPv6 link-local address: fe80::5c01:c0ff:fe02:7 [VALID]
        ND mac-extract : Disabled
        ICMPv6 active timers:
            Last Neighbor-Solicitation sent: 00:06:16
            Last Neighbor-Advertisement sent: 00:02:12
            Last Router-Advertisement sent: 1d18h
            Next Router-Advertisement sent in: 0.000000
        Router-Advertisement parameters:
            Periodic interval: 200 to 201 seconds
            Send "Managed Address Configuration" flag: false
            Send "Other Stateful Configuration" flag: false
            Send "Default Router Preference" value: Medium
            Send "Current Hop Limit" field: 64
            Send "MTU" option value: 1500
            Send "Router Lifetime" field: 1801 secs
            Send "Reachable Time" field: 0 ms
            Send "Retrans Timer" field: 0 ms
            Suppress RA: Enabled
            Suppress MTU in RA: Disabled
            Suppress Route Information Option in RA: Disabled
        Neighbor-Solicitation parameters:
            NS retransmit interval: 1000 ms
            ND NUD retry base: 1
            ND NUD retry interval: 1000
            ND NUD retry attempts: 3
        ICMPv6 error message parameters:
            Send redirects: true (0)
            Send unreachables: false
        ICMPv6 DAD parameters:
            Maximum DAD attempts: 1
            Current DAD attempt : 1
        Ethernet1/3, Interface status: protocol-up/link-up/admin-up
        IPv6 address:
            2001:db8:c56d:1::3/64 [VALID]
        IPv6 link-local address: fe80::5c01:c0ff:fe02:7 [VALID]
        ND mac-extract : Disabled
        ICMPv6 active timers:
            Last Neighbor-Solicitation sent: 00:07:39
            Last Neighbor-Advertisement sent: 02:39:27
            Last Router-Advertisement sent: 00:01:33
            Next Router-Advertisement sent in: 00:03:50
        Router-Advertisement parameters:
            Periodic interval: 200 to 600 seconds
            Send "Managed Address Configuration" flag: false
            Send "Other Stateful Configuration" flag: false
            Send "Default Router Preference" value: Medium
            Send "Current Hop Limit" field: 64
            Send "MTU" option value: 1500
            Send "Router Lifetime" field: 1800 secs
            Send "Reachable Time" field: 0 ms
            Send "Retrans Timer" field: 0 ms
            Suppress RA: Disabled
            Suppress MTU in RA: Disabled
            Suppress Route Information Option in RA: Disabled
        Neighbor-Solicitation parameters:
            NS retransmit interval: 1000 ms
            ND NUD retry base: 1
            ND NUD retry interval: 1000
            ND NUD retry attempts: 3
        ICMPv6 error message parameters:
            Send redirects: true (0)
            Send unreachables: false
        ICMPv6 DAD parameters:
            Maximum DAD attempts: 1
            Current DAD attempt : 1
        loopback0, Interface status: protocol-up/link-up/admin-up
        IPv6 address:
            2001:3:3::3/128 [VALID]
        IPv6 link-local address: fe80::5c01:c0ff:fe02:0 [VALID]
        ND mac-extract : Disabled
        ICMPv6 active timers:
            Last Neighbor-Solicitation sent: never
            Last Neighbor-Advertisement sent: never
            Last Router-Advertisement sent: never
            Next Router-Advertisement sent in: never
        Router-Advertisement parameters:
            Periodic interval: 200 to 600 seconds
            Send "Managed Address Configuration" flag: false
            Send "Other Stateful Configuration" flag: false
            Send "Default Router Preference" value: Medium
            Send "Current Hop Limit" field: 64
            Send "MTU" option value: 1500
            Send "Router Lifetime" field: 1800 secs
            Send "Reachable Time" field: 0 ms
            Send "Retrans Timer" field: 0 ms
            Suppress RA: Disabled
            Suppress MTU in RA: Disabled
            Suppress Route Information Option in RA: Disabled
        Neighbor-Solicitation parameters:
            NS retransmit interval: 1000 ms
            ND NUD retry base: 1
            ND NUD retry interval: 1000
            ND NUD retry attempts: 3
        ICMPv6 error message parameters:
            Send redirects: true (0)
            Send unreachables: false
        ICMPv6 DAD parameters:
            Maximum DAD attempts: 1
            Current DAD attempt : 0
        loopback1, Interface status: protocol-up/link-up/admin-up
        IPv6 address:
            2001:33:33::33/128 [VALID]
        IPv6 link-local address: fe80::5c01:c0ff:fe02:0 [VALID]
        ND mac-extract : Disabled
        ICMPv6 active timers:
            Last Neighbor-Solicitation sent: never
            Last Neighbor-Advertisement sent: never
            Last Router-Advertisement sent: never
            Next Router-Advertisement sent in: never
        Router-Advertisement parameters:
            Periodic interval: 200 to 600 seconds
            Send "Managed Address Configuration" flag: false
            Send "Other Stateful Configuration" flag: false
            Send "Default Router Preference" value: Medium
            Send "Current Hop Limit" field: 64
            Send "MTU" option value: 1500
            Send "Router Lifetime" field: 1800 secs
            Send "Reachable Time" field: 0 ms
            Send "Retrans Timer" field: 0 ms
            Suppress RA: Disabled
            Suppress MTU in RA: Disabled
            Suppress Route Information Option in RA: Disabled
        Neighbor-Solicitation parameters:
            NS retransmit interval: 1000 ms
            ND NUD retry base: 1
            ND NUD retry interval: 1000
            ND NUD retry attempts: 3
        ICMPv6 error message parameters:
            Send redirects: true (0)
            Send unreachables: false
        ICMPv6 DAD parameters:
            Maximum DAD attempts: 1
            Current DAD attempt : 0

        ICMPv6 ND Interfaces for VRF "management"

        ICMPv6 ND Interfaces for VRF "vrf1"
        Ethernet1/2, Interface status: protocol-up/link-up/admin-up
        IPv6 address:
            2001:db8:c8d1:4::3/64 [VALID]
        IPv6 link-local address: fe80::5c01:c0ff:fe02:7 [VALID]
        ND mac-extract : Disabled
        ICMPv6 active timers:
            Last Neighbor-Solicitation sent: 00:09:34
            Last Neighbor-Advertisement sent: 00:01:07
            Last Router-Advertisement sent: 00:05:42
            Next Router-Advertisement sent in: 00:01:46
        Router-Advertisement parameters:
            Periodic interval: 200 to 600 seconds
            Send "Managed Address Configuration" flag: false
            Send "Other Stateful Configuration" flag: false
            Send "Default Router Preference" value: Medium
            Send "Current Hop Limit" field: 64
            Send "MTU" option value: 1500
            Send "Router Lifetime" field: 1800 secs
            Send "Reachable Time" field: 0 ms
            Send "Retrans Timer" field: 0 ms
            Suppress RA: Disabled
            Suppress MTU in RA: Disabled
            Suppress Route Information Option in RA: Disabled
        Neighbor-Solicitation parameters:
            NS retransmit interval: 1000 ms
            ND NUD retry base: 1
            ND NUD retry interval: 1000
            ND NUD retry attempts: 3
        ICMPv6 error message parameters:
            Send redirects: true (0)
            Send unreachables: false
        ICMPv6 DAD parameters:
            Maximum DAD attempts: 1
            Current DAD attempt : 1
        Ethernet1/4, Interface status: protocol-up/link-up/admin-up
        IPv6 address:
            2001:db8:c8d1:1::3/64 [VALID]
        IPv6 link-local address: fe80::5c01:c0ff:fe02:7 [VALID]
        ND mac-extract : Disabled
        ICMPv6 active timers:
            Last Neighbor-Solicitation sent: 00:03:31
            Last Neighbor-Advertisement sent: 07:32:12
            Last Router-Advertisement sent: 00:08:09
            Next Router-Advertisement sent in: 00:01:36
        Router-Advertisement parameters:
            Periodic interval: 200 to 600 seconds
            Send "Managed Address Configuration" flag: false
            Send "Other Stateful Configuration" flag: false
            Send "Default Router Preference" value: Medium
            Send "Current Hop Limit" field: 64
            Send "MTU" option value: 1500
            Send "Router Lifetime" field: 1800 secs
            Send "Reachable Time" field: 0 ms
            Send "Retrans Timer" field: 0 ms
            Suppress RA: Disabled
            Suppress MTU in RA: Disabled
            Suppress Route Information Option in RA: Disabled
        Neighbor-Solicitation parameters:
            NS retransmit interval: 1000 ms
            ND NUD retry base: 1
            ND NUD retry interval: 1000
            ND NUD retry attempts: 3
        ICMPv6 error message parameters:
            Send redirects: true (0)
            Send unreachables: false
        ICMPv6 DAD parameters:
            Maximum DAD attempts: 1
            Current DAD attempt : 1
    '''}

    golden_parsed_output = {
        "vrf": {
            "vrf1": {
                "interfaces": {
                    "Ethernet1/2": {
                        "router_advertisement": {
                            "default_router_preference": "medium",
                            "interval": 600,
                            "retrans_timer": 0,
                            "suppress_mtu": False,
                            "current_hop_limit": 64,
                            "reachable_time": 0,
                            "mtu": 1500,
                            "suppress": False,
                            "other_stateful_configuration": False,
                            "suppress_route_information": False,
                            "lifetime": 1800,
                            "managed_address_configuration": False
                        },
                        "oper_status": "up",
                        "neighbor_solicitation": {
                            "interval": 1000,
                            "retry_interval": 1000,
                            "retry_base": 1,
                            "retry_attempts": 3
                        },
                        "dad": {
                            "maximum_attempts": 1,
                            "current_attempt": 1
                        },
                        "local_address": "fe80::5c01:c0ff:fe02:7",
                        "error_message": {
                            "unreachables": False,
                            "redirects": True
                        },
                        "enable": True,
                        "link_status": "up",
                        "ip": "2001:db8:c8d1:4::3/64",
                        "mac_extract": "disabled",
                        "active_timers": {
                            "last_router_advertisement": "00:05:42",
                            "last_neighbor_advertisement": "00:01:07",
                            "last_neighbor_solicitation": "00:09:34",
                            "next_router_advertisement": "00:01:46"
                        },
                        "interface": "Ethernet1/2"
                    },
                    "Ethernet1/4": {
                        "router_advertisement": {
                        "default_router_preference": "medium",
                            "interval": 600,
                            "retrans_timer": 0,
                            "suppress_mtu": False,
                            "current_hop_limit": 64,
                            "reachable_time": 0,
                            "mtu": 1500,
                            "suppress": False,
                            "other_stateful_configuration": False,
                            "suppress_route_information": False,
                            "lifetime": 1800,
                            "managed_address_configuration": False
                        },
                        "oper_status": "up",
                        "neighbor_solicitation": {
                            "interval": 1000,
                            "retry_interval": 1000,
                            "retry_base": 1,
                            "retry_attempts": 3
                        },
                        "dad": {
                            "maximum_attempts": 1,
                            "current_attempt": 1
                        },
                        "local_address": "fe80::5c01:c0ff:fe02:7",
                        "error_message": {
                            "unreachables": False,
                            "redirects": True
                        },
                        "enable": True,
                        "link_status": "up",
                        "ip": "2001:db8:c8d1:1::3/64",
                        "mac_extract": "disabled",
                        "active_timers": {
                            "last_router_advertisement": "00:08:09",
                            "last_neighbor_advertisement": "07:32:12",
                            "last_neighbor_solicitation": "00:03:31",
                            "next_router_advertisement": "00:01:36"
                        },
                        "interface": "Ethernet1/4"
                    }
                }
            },
            "default": {
                "interfaces": {
                    "loopback1": {
                        "router_advertisement": {
                            "default_router_preference": "medium",
                            "interval": 600,
                            "retrans_timer": 0,
                            "suppress_mtu": False,
                            "current_hop_limit": 64,
                            "reachable_time": 0,
                            "mtu": 1500,
                            "suppress": False,
                            "other_stateful_configuration": False,
                            "suppress_route_information": False,
                            "lifetime": 1800,
                            "managed_address_configuration": False
                        },
                        "oper_status": "up",
                        "neighbor_solicitation": {
                            "interval": 1000,
                            "retry_interval": 1000,
                            "retry_base": 1,
                            "retry_attempts": 3
                        },
                        "dad": {
                            "maximum_attempts": 1,
                            "current_attempt": 0
                        },
                        "local_address": "fe80::5c01:c0ff:fe02:0",
                        "error_message": {
                            "unreachables": False,
                            "redirects": True
                        },
                        "enable": True,
                        "link_status": "up",
                        "ip": "2001:33:33::33/128",
                        "mac_extract": "disabled",
                        "active_timers": {
                            "last_router_advertisement": "never",
                            "last_neighbor_advertisement": "never",
                            "last_neighbor_solicitation": "never",
                            "next_router_advertisement": "never"
                        },
                        "interface": "loopback1"
                    },
                    "Ethernet1/1": {
                        "router_advertisement": {
                            "default_router_preference": "medium",
                            "interval": 201,
                            "retrans_timer": 0,
                            "suppress_mtu": False,
                            "current_hop_limit": 64,
                            "reachable_time": 0,
                            "mtu": 1500,
                            "suppress": True,
                            "other_stateful_configuration": False,
                            "suppress_route_information": False,
                            "lifetime": 1801,
                            "managed_address_configuration": False
                        },
                        "oper_status": "up",
                        "neighbor_solicitation": {
                            "interval": 1000,
                            "retry_interval": 1000,
                            "retry_base": 1,
                            "retry_attempts": 3
                        },
                        "dad": {
                            "maximum_attempts": 1,
                            "current_attempt": 1
                        },
                        "local_address": "fe80::5c01:c0ff:fe02:7",
                        "error_message": {
                            "unreachables": False,
                            "redirects": True
                        },
                        "enable": True,
                        "link_status": "up",
                        "ip": "2001:db8:c56d:4::3/64",
                        "mac_extract": "disabled",
                        "active_timers": {
                            "last_router_advertisement": "1d18h",
                            "last_neighbor_advertisement": "00:02:12",
                            "last_neighbor_solicitation": "00:06:16",
                            "next_router_advertisement": "0.000000"
                        },
                        "interface": "Ethernet1/1"
                    },
                    "Ethernet1/3": {
                        "router_advertisement": {
                            "default_router_preference": "medium",
                            "interval": 600,
                            "retrans_timer": 0,
                            "suppress_mtu": False,
                            "current_hop_limit": 64,
                            "reachable_time": 0,
                            "mtu": 1500,
                            "suppress": False,
                            "other_stateful_configuration": False,
                            "suppress_route_information": False,
                            "lifetime": 1800,
                            "managed_address_configuration": False
                        },
                        "oper_status": "up",
                        "neighbor_solicitation": {
                            "interval": 1000,
                            "retry_interval": 1000,
                            "retry_base": 1,
                            "retry_attempts": 3
                        },
                        "dad": {
                            "maximum_attempts": 1,
                            "current_attempt": 1
                        },
                        "local_address": "fe80::5c01:c0ff:fe02:7",
                        "error_message": {
                            "unreachables": False,
                            "redirects": True
                        },
                        "enable": True,
                        "link_status": "up",
                        "ip": "2001:db8:c56d:1::3/64",
                        "mac_extract": "disabled",
                        "active_timers": {
                            "last_router_advertisement": "00:01:33",
                            "last_neighbor_advertisement": "02:39:27",
                            "last_neighbor_solicitation": "00:07:39",
                            "next_router_advertisement": "00:03:50"
                        },
                        "interface": "Ethernet1/3"
                    },
                    "loopback0": {
                        "router_advertisement": {
                            "default_router_preference": "medium",
                            "interval": 600,
                            "retrans_timer": 0,
                            "suppress_mtu": False,
                            "current_hop_limit": 64,
                            "reachable_time": 0,
                            "mtu": 1500,
                            "suppress": False,
                            "other_stateful_configuration": False,
                            "suppress_route_information": False,
                            "lifetime": 1800,
                            "managed_address_configuration": False
                        },
                        "oper_status": "up",
                        "neighbor_solicitation": {
                            "interval": 1000,
                            "retry_interval": 1000,
                            "retry_base": 1,
                            "retry_attempts": 3
                        },
                        "dad": {
                            "maximum_attempts": 1,
                            "current_attempt": 0
                        },
                        "local_address": "fe80::5c01:c0ff:fe02:0",
                        "error_message": {
                            "unreachables": False,
                            "redirects": True
                        },
                        "enable": True,
                        "link_status": "up",
                        "ip": "2001:3:3::3/128",
                        "mac_extract": "disabled",
                        "active_timers": {
                            "last_router_advertisement": "never",
                            "last_neighbor_advertisement": "never",
                            "last_neighbor_solicitation": "never",
                            "next_router_advertisement": "never"
                        },
                        "interface": "loopback0"
                    }
                }
            }
        }
    }

    golden_parsed_output1 = {
        'vrf': {
            'VRF1': {
                'interfaces': {
                    'Ethernet1/2.420': {
                        'interface': 'Ethernet1/2.420',
                        'oper_status': 'up',
                        'link_status': 'up',
                        'enable': True,
                        'ip': '2001:10:13:120::3/64',
                        'local_address': 'fe80::5c00:40ff:fe02:7',
                        'mac_extract': 'disabled',
                        'active_timers': {
                            'last_neighbor_solicitation': '00:04:07',
                            'last_neighbor_advertisement': '00:04:02',
                            'last_router_advertisement': '00:01:02',
                            'next_router_advertisement': '00:07:47',
                        },
                        'router_advertisement': {
                            'interval': 600,
                            'managed_address_configuration': False,
                            'other_stateful_configuration': False,
                            'default_router_preference': 'medium',
                            'current_hop_limit': 64,
                            'mtu': 1500,
                            'lifetime': 1800,
                            'reachable_time': 0,
                            'retrans_timer': 0,
                            'suppress': False,
                            'suppress_mtu': False,
                            'suppress_route_information': False,
                        },
                        'neighbor_solicitation': {
                            'interval': 1000,
                            'retry_base': 1,
                            'retry_interval': 1000,
                            'retry_attempts': 3,
                        },
                        'error_message': {
                            'redirects': True,
                            'unreachables': False,
                        },
                        'dad': {
                            'maximum_attempts': 1,
                            'current_attempt': 1,
                        },
                    },
                },
            },
        },
    }
    golden_output1 = {'execute.return_value':'''
        R3_nx# show ipv6 nd interface Ethernet1/2.420 vrf VRF1
        ICMPv6 ND Interfaces for VRF "VRF1"
        Ethernet1/2.420, Interface status: protocol-up/link-up/admin-up
        IPv6 address:
            2001:10:13:120::3/64 [VALID]
        IPv6 link-local address: fe80::5c00:40ff:fe02:7 [VALID]
        ND mac-extract : Disabled
        ICMPv6 active timers:
            Last Neighbor-Solicitation sent: 00:04:07
            Last Neighbor-Advertisement sent: 00:04:02
            Last Router-Advertisement sent: 00:01:02
            Next Router-Advertisement sent in: 00:07:47
        Router-Advertisement parameters:
            Periodic interval: 200 to 600 seconds
            Send "Managed Address Configuration" flag: false
            Send "Other Stateful Configuration" flag: false
            Send "Default Router Preference" value: Medium
            Send "Current Hop Limit" field: 64
            Send "MTU" option value: 1500
            Send "Router Lifetime" field: 1800 secs
            Send "Reachable Time" field: 0 ms
            Send "Retrans Timer" field: 0 ms
            Suppress RA: Disabled
            Suppress MTU in RA: Disabled
            Suppress Route Information Option in RA: Disabled
        Neighbor-Solicitation parameters:
            NS retransmit interval: 1000 ms
            ND NUD retry base: 1
            ND NUD retry interval: 1000
            ND NUD retry attempts: 3
        ICMPv6 error message parameters:
            Send redirects: true (0)
            Send unreachables: false
        ICMPv6 DAD parameters:
            Maximum DAD attempts: 1
            Current DAD attempt : 1
    '''}

    def test_show_ipv6_nd_interface_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6NdInterface(device=self.device)
        parsed_output = obj.parse(vrf="all")
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_nve_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6NdInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpv6NdInterface(device=self.device)
        parsed_output = obj.parse(vrf="VRF1", interface='Ethernet1/2.420')
        self.assertEqual(parsed_output,self.golden_parsed_output1)


class test_show_ipv6_icmp_neighbor_detail(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value':'''
        n9kv-3# show ipv6 icmp neighbor detail vrf all

        Flags: + - Adjacencies synced via CFSoE
            # - Adjacencies Throttled for Glean

        ICMPv6 Adjacency Table for all VRFs
        Address         Age       MAC Address     State      Interface  Phy-Interface
        2001:db8:c56d:4::2     00:15:02  fa16.3eff.e5a2  STALE       Eth1/1      Eth1/1
        fe80::f816:3eff:feff:e5a2
                        00:18:33  fa16.3eff.e5a2  STALE       Eth1/1      Eth1/1
        2001:db8:c8d1:4::2     00:03:30  fa16.3eff.e455  STALE       Eth1/2      Eth1/2
        fe80::f816:3eff:feff:e455
                        00:14:19  fa16.3eff.e455  STALE       Eth1/2      Eth1/2
        2001:db8:c56d:1::1     00:15:31  fa16.3eff.9f9b  STALE       Eth1/3      Eth1/3
        fe80::f816:3eff:feff:9f9b
                        00:15:31  fa16.3eff.9f9b  STALE       Eth1/3      Eth1/3
        2001:db8:c8d1:1::1     00:07:58  fa16.3eff.4908  STALE       Eth1/4      Eth1/4
        fe80::f816:3eff:feff:4908
                        00:02:41  fa16.3eff.4908  STALE       Eth1/4      Eth1/4
    '''}

    golden_parsed_output = {
        "interfaces": {
            "Ethernet1/4": {
                "neighbors": {
                    "fe80::f816:3eff:feff:4908": {
                        "neighbor_state": "stale",
                        "age": "00:02:41",
                        "ip": "fe80::f816:3eff:feff:4908",
                        "link_layer_address": "fa16.3eff.4908",
                        "physical_interface": "Ethernet1/4"
                    },
                    "2001:db8:c8d1:1::1": {
                        "neighbor_state": "stale",
                        "age": "00:07:58",
                        "ip": "2001:db8:c8d1:1::1",
                        "link_layer_address": "fa16.3eff.4908",
                        "physical_interface": "Ethernet1/4"
                    }
                },
                "interface": "Ethernet1/4"
            },
            "Ethernet1/2": {
                "neighbors": {
                    "2001:db8:c8d1:4::2": {
                        "neighbor_state": "stale",
                        "age": "00:03:30",
                        "ip": "2001:db8:c8d1:4::2",
                        "link_layer_address": "fa16.3eff.e455",
                        "physical_interface": "Ethernet1/2"
                    },
                    "fe80::f816:3eff:feff:e455": {
                        "neighbor_state": "stale",
                        "age": "00:14:19",
                        "ip": "fe80::f816:3eff:feff:e455",
                        "link_layer_address": "fa16.3eff.e455",
                        "physical_interface": "Ethernet1/2"
                    }
                },
                "interface": "Ethernet1/2"
            },
            "Ethernet1/1": {
                "neighbors": {
                    "fe80::f816:3eff:feff:e5a2": {
                        "neighbor_state": "stale",
                        "age": "00:18:33",
                        "ip": "fe80::f816:3eff:feff:e5a2",
                        "link_layer_address": "fa16.3eff.e5a2",
                        "physical_interface": "Ethernet1/1"
                    },
                    "2001:db8:c56d:4::2": {
                        "neighbor_state": "stale",
                        "age": "00:15:02",
                        "ip": "2001:db8:c56d:4::2",
                        "link_layer_address": "fa16.3eff.e5a2",
                        "physical_interface": "Ethernet1/1"
                    }
                },
                "interface": "Ethernet1/1"
            },
            "Ethernet1/3": {
                "neighbors": {
                    "2001:db8:c56d:1::1": {
                        "neighbor_state": "stale",
                        "age": "00:15:31",
                        "ip": "2001:db8:c56d:1::1",
                        "link_layer_address": "fa16.3eff.9f9b",
                        "physical_interface": "Ethernet1/3"
                    },
                    "fe80::f816:3eff:feff:9f9b": {
                        "neighbor_state": "stale",
                        "age": "00:15:31",
                        "ip": "fe80::f816:3eff:feff:9f9b",
                        "link_layer_address": "fa16.3eff.9f9b",
                        "physical_interface": "Ethernet1/3"
                    }
                },
                "interface": "Ethernet1/3"
            }
        }
    }

    golden_parsed_output1 = {
        'interfaces': {
            'Ethernet1/1.390': {
                'interface': 'Ethernet1/1.390',
                'neighbors': {
                    'fe80::f816:3eff:feff:e887': {
                        'ip': 'fe80::f816:3eff:feff:e887',
                        'link_layer_address': 'fa16.3eff.e887',
                        'neighbor_state': 'stale',
                        'age': '00:00:49',
                        'physical_interface': 'Ethernet1/1.390',
                    },
                },
            },
        },
    }
    golden_output1 = {'execute.return_value':'''
        R3_nx# show ipv6 icmp neighbor Eth1/1.390 detail vrf VRF1

        Flags: + - Adjacencies synced via CFSoE
            # - Adjacencies Throttled for Glean

        ICMPv6 Adjacency Table for VRF VRF1
        Address         Age       MAC Address     State      Interface  Phy-Interface
        fe80::f816:3eff:feff:e887
                        00:00:49  fa16.3eff.e887  STALE       Eth1/1.390  Eth1/1.390
    '''}

    def test_show_ipv6_icmp_neighbor_detail_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6IcmpNeighborDetail(device=self.device)
        parsed_output = obj.parse(vrf="all")
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_nve_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6IcmpNeighborDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpv6IcmpNeighborDetail(device=self.device)
        parsed_output = obj.parse(vrf="VRF1", interface='Eth1/1.390')
        self.assertEqual(parsed_output,self.golden_parsed_output1)


class test_show_ipv6_routers(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output= {'execute.return_value':'''
    n9kv-3# show ipv6 routers vrf all
    Router fe80::f816:3eff:feff:e5a2 on Ethernet1/1 , last update time 3.2 min
    Current_hop_limit 64, Lifetime 1800, AddrFlag 0, OtherFlag 0, MTU 1500
    HomeAgentFlag 0, Preference Medium
    Reachable time 0 msec, Retransmission time 0 msec
      Prefix 2001:db8:c56d:4::/64  onlink_flag 1 autonomous_flag 1
      valid lifetime 2592000, preferred lifetime 604800


    Router fe80::f816:3eff:feff:e455 on Ethernet1/2 , last update time 1.5 min
    Current_hop_limit 64, Lifetime 1800, AddrFlag 0, OtherFlag 0, MTU 1500
    HomeAgentFlag 0, Preference Medium
    Reachable time 0 msec, Retransmission time 0 msec
      Prefix 2001:db8:c8d1:4::/64  onlink_flag 1 autonomous_flag 1
      valid lifetime 2592000, preferred lifetime 604800
      Prefix 2001:db8:888c:4::/64   onlink_flag 1 autonomous_flag 1
      valid lifetime 2592000, preferred lifetime 604800


    Router fe80::f816:3eff:feff:9f9b on Ethernet1/3 , last update time 2.8 min
    Current_hop_limit 64, Lifetime 1800, AddrFlag 0, OtherFlag 0, MTU 1500
    HomeAgentFlag 0, Preference Medium
    Reachable time 0 msec, Retransmission time 0 msec
      Prefix 2001:db8:c56d:1::/64  onlink_flag 1 autonomous_flag 1
      valid lifetime 2592000, preferred lifetime 604800


    Router fe80::f816:3eff:feff:4908 on Ethernet1/4 , last update time 2.3 min
    Current_hop_limit 64, Lifetime 1800, AddrFlag 0, OtherFlag 0, MTU 1500
    HomeAgentFlag 0, Preference Medium
    Reachable time 0 msec, Retransmission time 0 msec
      Prefix 2001:db8:c8d1:1::/64  onlink_flag 1 autonomous_flag 1
      valid lifetime 2592000, preferred lifetime 604800
    '''}

    golden_parsed_output = {
        "interfaces": {
            "Ethernet1/3": {
                "neighbors": {
                    "fe80::f816:3eff:feff:9f9b": {
                        "homeagent_flag": 0,
                        "is_router": True,
                        "addr_flag": 0,
                        "ip": "fe80::f816:3eff:feff:9f9b",
                        "lifetime": 1800,
                        "current_hop_limit": 64,
                        "retransmission_time": 0,
                        "last_update": "2.8",
                        "mtu": 1500,
                        "preference": "medium",
                        "other_flag": 0,
                        "reachable_time": 0,
                        "prefix": {
                            "2001:db8:c56d:1::/64": {
                                "preferred_lifetime": 604800,
                                "valid_lifetime": 2592000,
                                "autonomous_flag": 1,
                                "onlink_flag": 1,
                            }
                        }
                    }
                },
                "interface": "Ethernet1/3"
            },
            "Ethernet1/1": {
                "neighbors": {
                    "fe80::f816:3eff:feff:e5a2": {
                        "homeagent_flag": 0,
                        "is_router": True,
                        "addr_flag": 0,
                        "ip": "fe80::f816:3eff:feff:e5a2",
                        "lifetime": 1800,
                        "current_hop_limit": 64,
                        "retransmission_time": 0,
                        "last_update": "3.2",
                        "mtu": 1500,
                        "preference": "medium",
                        "other_flag": 0,
                        "reachable_time": 0,
                        "prefix": {
                            "2001:db8:c56d:4::/64": {
                                "preferred_lifetime": 604800,
                                "valid_lifetime": 2592000,
                                "autonomous_flag": 1,
                                "onlink_flag": 1,
                            }
                        }
                    }
                },
                "interface": "Ethernet1/1"
            },
            "Ethernet1/4": {
                "neighbors": {
                    "fe80::f816:3eff:feff:4908": {
                        "homeagent_flag": 0,
                        "is_router": True,
                        "addr_flag": 0,
                        "ip": "fe80::f816:3eff:feff:4908",
                        "lifetime": 1800,
                        "current_hop_limit": 64,
                        "retransmission_time": 0,
                        "last_update": "2.3",
                        "mtu": 1500,
                        "preference": "medium",
                        "other_flag": 0,
                        "reachable_time": 0,
                        "prefix": {
                            "2001:db8:c8d1:1::/64": {
                                "preferred_lifetime": 604800,
                                "autonomous_flag": 1,
                                "valid_lifetime": 2592000,
                                "onlink_flag": 1,
                            }
                        }
                    }
                },
                "interface": "Ethernet1/4"
            },
            "Ethernet1/2": {
                "neighbors": {
                    "fe80::f816:3eff:feff:e455": {
                        "homeagent_flag": 0,
                        "is_router": True,
                        "addr_flag": 0,
                        "ip": "fe80::f816:3eff:feff:e455",
                        "lifetime": 1800,
                        "current_hop_limit": 64,
                        "retransmission_time": 0,
                        "last_update": "1.5",
                        "mtu": 1500,
                        "preference": "medium",
                        "other_flag": 0,
                        "reachable_time": 0,
                        "prefix": {
                            "2001:db8:c8d1:4::/64": {
                                "preferred_lifetime": 604800,
                                "onlink_flag": 1,
                                "valid_lifetime": 2592000,
                                "autonomous_flag": 1,
                            },
                            "2001:db8:888c:4::/64": {
                                "preferred_lifetime": 604800,
                                "onlink_flag": 1,
                                "valid_lifetime": 2592000,
                                "autonomous_flag": 1,
                            }
                        }
                    }
                },
                "interface": "Ethernet1/2"
            }
        }
    }

    def test_show_ipv6_icmp_neighbor_detail_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6Routers(device=self.device)
        parsed_output = obj.parse(vrf="all")
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_nve_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6Routers(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()