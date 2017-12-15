
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Parser
from parser.nxos.show_ospf import ShowIpOspf, \
                                  ShowIpOspfMplsLdpInterface, \
                                  ShowIpOspfVirtualLinks, \
                                  ShowIpOspfShamLinks

# Metaparser
from metaparser.util.exceptions import SchemaEmptyParserError


# =====================================
#  Unit test for 'show ip ospf'
#  Unit test for 'show ip ospf vrf all'
# =====================================
class test_show_ip_ospf(unittest.TestCase):

    '''Unit test for show ip ospf
       Unit test for show ip ospf vrf all'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'area_id': '0.0.0.1',
                                        'area_type': 'stub',
                                        'authentication': 'none',
                                        'default_cost': 1,
                                        'existed': '08:30:42',
                                        'numbers': 
                                            {'active_interfaces': 3,
                                            'interfaces': 3,
                                            'loopback_interfaces': 0,
                                            'passive_interfaces': 0},
                                        'ranges': 
                                            {'1.1.0.0/16': 
                                                {'advertise': False,
                                                'cost': 31,
                                                'net': 1,
                                                'prefix': '1.1.0.0/16'}},
                                        'statistics': 
                                            {'area_scope_lsa_cksum_sum': '11',
                                            'area_scope_lsa_count': 11,
                                            'spf_last_run_time': 0.000464,
                                            'spf_runs_count': 33}}},
                                'auto_cost': 
                                    {'bandwidth_unit': 'mbps',
                                    'enable': True,
                                    'reference_bandwidth': 40000},
                                'enable': True,
                                'discard_route_external': True,
                                'discard_route_internal': True,
                                'graceful_restart': 
                                    {'ietf': 
                                        {'enable': True,
                                        'exist_status': 'none',
                                        'restart_interval': 60,
                                        'state': 'Inactive',
                                        'type': 'ietf'}},
                                'instance': 1,
                                'nsr': 
                                    {'enable': True},
                                'numbers': 
                                    {'active_areas': 
                                        {'normal': 1,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 1},
                                    'areas': 
                                        {'normal': 1,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 1}},
                                'opaque_lsa_enable': True,
                                'preference': 
                                    {'single_value': {'all': 110}},
                                'router_id': '22.22.22.22',
                                'single_tos_routes_enable': True,
                                'spf_control': 
                                    {'paths': 8,
                                    'throttle': 
                                        {'lsa': 
                                            {'group_pacing': 10,
                                            'hold': 5000.0,
                                            'maximum': 5000.0,
                                            'minimum': 1000.0,
                                            'numbers': 
                                                {'external_lsas': 
                                                    {'checksum': '0',
                                                    'total': 0},
                                                'opaque_as_lsas': 
                                                    {'checksum': '0',
                                                    'total': 0}},
                                            'start': 0.0},
                                            'spf': 
                                                {'hold': 1000.0,
                                                'maximum': 5000.0,
                                                'start': 200.0}}}}}}}},
            'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'area_id': '0.0.0.0',
                                        'area_type': 'normal',
                                        'authentication': 'none',
                                        'existed': '08:30:42',
                                        'numbers': 
                                            {'active_interfaces': 4,
                                            'interfaces': 4,
                                            'loopback_interfaces': 1,
                                            'passive_interfaces': 0},
                                        'ranges': 
                                            {'1.1.1.0/24': 
                                                {'advertise': True,
                                                'cost': 33,
                                                'net': 0,
                                                'prefix': '1.1.1.0/24'}},
                                        'statistics': 
                                            {'area_scope_lsa_cksum_sum': '19',
                                            'area_scope_lsa_count': 19,
                                            'spf_last_run_time': 0.001386,
                                            'spf_runs_count': 8}}},
                                'auto_cost': 
                                    {'bandwidth_unit': 'mbps',
                                    'enable': True,
                                    'reference_bandwidth': 40000},
                                'bfd': 
                                    {'enable': True},
                                'database_control': 
                                    {'max_lsa': 123},
                                'enable': True,
                                'discard_route_external': True,
                                'discard_route_internal': True,
                                'graceful_restart': 
                                    {'ietf': 
                                        {'enable': True,
                                        'exist_status': 'none',
                                        'restart_interval': 60,
                                        'state': 'Inactive',
                                        'type': 'ietf'}},
                                'instance': 1,
                                'nsr': 
                                    {'enable': True},
                                'numbers': 
                                    {'active_areas': 
                                        {'normal': 1,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 1},
                                    'areas': 
                                        {'normal': 1,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 1}},
                                'opaque_lsa_enable': True,
                                'preference': 
                                    {'single_value': {'all': 110}},
                                'router_id': '2.2.2.2',
                                'single_tos_routes_enable': True,
                                'spf_control': 
                                    {'paths': 8,
                                    'throttle': 
                                        {'lsa': 
                                            {'group_pacing': 10,
                                            'hold': 5000.0,
                                            'maximum': 5000.0,
                                            'minimum': 1000.0,
                                            'numbers': 
                                                {'external_lsas': 
                                                    {'checksum': '0x7d61',
                                                    'total': 1},
                                                'opaque_as_lsas': 
                                                    {'checksum': '0',
                                                    'total': 0}},
                                            'start': 0.0},
                                            'spf': 
                                                {'hold': 1000.0,
                                                'maximum': 5000.0,
                                                'start': 200.0}}},
                                'stub_router': 
                                    {'always': 
                                        {'always': True}}}}}}}}}

    golden_output = {'execute.return_value': '''
        Routing Process 1 with ID 2.2.2.2 VRF default
        Routing Process Instance Number 1
        Stateful High Availability enabled
        Graceful-restart is configured
        Grace period: 60 state: Inactive
        BFD is enabled
        Last graceful restart exit status: None
        Supports only single TOS(TOS0) routes
        Supports opaque LSA
        Administrative distance 110
        Originating router LSA with maximum metric
        Reference Bandwidth is 40000 Mbps
        SPF throttling delay time of 200.000 msecs,
        SPF throttling hold time of 1000.000 msecs, 
        SPF throttling maximum wait time of 5000.000 msecs
        LSA throttling start time of 0.000 msecs,
        LSA throttling hold interval of 5000.000 msecs, 
        LSA throttling maximum wait time of 5000.000 msecs
        Minimum LSA arrival 1000.000 msec
        LSA group pacing timer 10 secs
        Maximum number of non self-generated LSA allowed 123
        Maximum paths to destination 8
        Number of external LSAs 1, checksum sum 0x7d61
        Number of opaque AS LSAs 0, checksum sum 0
        Number of areas is 1, 1 normal, 0 stub, 0 nssa
        Number of active areas is 1, 1 normal, 0 stub, 0 nssa
        Install discard route for summarized external routes.
        Install discard route for summarized internal routes.
        Area BACKBONE(0.0.0.0) 
            Area has existed for 08:30:42
            Interfaces in this area: 4 Active interfaces: 4
            Passive interfaces: 0  Loopback interfaces: 1
            No authentication available
            SPF calculation has run 8 times
             Last SPF ran for 0.001386s
            Area ranges are
            1.1.1.0/24 Passive (Num nets: 0) Advertise Cost configured 33
            Number of LSAs: 19, checksum sum 0x7a137

        Routing Process 1 with ID 22.22.22.22 VRF VRF1
        Routing Process Instance Number 1
        Domain ID type 0x0005, Value 0.0.0.0
        Stateful High Availability enabled
        Graceful-restart is configured
        Grace period: 60 state: Inactive 
        Last graceful restart exit status: None
        Supports only single TOS(TOS0) routes
        Supports opaque LSA
        This router is an area border and autonomous system boundary.
        Redistributing External Routes from
        bgp-100
        Administrative distance 110
        Reference Bandwidth is 40000 Mbps
        SPF throttling delay time of 200.000 msecs,
        SPF throttling hold time of 1000.000 msecs, 
        SPF throttling maximum wait time of 5000.000 msecs
        LSA throttling start time of 0.000 msecs,
        LSA throttling hold interval of 5000.000 msecs, 
        LSA throttling maximum wait time of 5000.000 msecs
        Minimum LSA arrival 1000.000 msec
        LSA group pacing timer 10 secs
        Maximum paths to destination 8
        Number of external LSAs 0, checksum sum 0
        Number of opaque AS LSAs 0, checksum sum 0
        Number of areas is 1, 1 normal, 0 stub, 0 nssa
        Number of active areas is 1, 1 normal, 0 stub, 0 nssa
        Install discard route for summarized external routes.
        Install discard route for summarized internal routes.
        Area (0.0.0.1)
            This area is a STUB area
            Generates stub default route with cost 1
            Area has existed for 08:30:42
            Interfaces in this area: 3 Active interfaces: 3
            Passive interfaces: 0  Loopback interfaces: 0
            No authentication available
            SPF calculation has run 33 times
             Last SPF ran for 0.000464s
            Area ranges are
            1.1.0.0/16 Active (Num nets: 1) DoNotAdvertise Cost configured 31
            Number of LSAs: 11, checksum sum 0x527f9
        '''}

    golden_parsed_output_1 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'area_id': '0.0.0.0',
                                        'area_type': 'normal',
                                        'authentication': 'none',
                                        'existed': '1w5d',
                                        'numbers': 
                                            {'active_interfaces': 4,
                                            'interfaces': 6,
                                            'loopback_interfaces': 4,
                                            'passive_interfaces': 0},
                                        'statistics': 
                                            {'area_scope_lsa_cksum_sum': '1',
                                            'area_scope_lsa_count': 1,
                                            'spf_last_run_time': 0.000447,
                                            'spf_runs_count': 2}}},
                                'auto_cost': 
                                    {'bandwidth_unit': 'mbps',
                                    'enable': True,
                                    'reference_bandwidth': 40000},
                                'enable': False,
                                'discard_route_external': True,
                                'discard_route_internal': True,
                                'graceful_restart': 
                                    {'ietf': 
                                        {'enable': True,
                                        'exist_status': 'none',
                                        'restart_interval': 60,
                                        'state': 'Inactive',
                                        'type': 'ietf'}},
                                'instance': 1,
                                'nsr': 
                                    {'enable': True},
                                'numbers': 
                                    {'active_areas': 
                                        {'normal': 1,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 1},
                                    'areas': 
                                        {'normal': 1,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 1}},
                                'opaque_lsa_enable': True,
                                'preference': 
                                    {'single_value': 
                                        {'all': 110}},
                                'router_id': '2.2.2.2',
                                'single_tos_routes_enable': True,
                                'spf_control': 
                                    {'paths': 8,
                                    'throttle': 
                                        {'lsa': 
                                            {'group_pacing': 10,
                                            'hold': 5000.0,
                                            'maximum': 5000.0,
                                            'minimum': 1000.0,
                                            'numbers': 
                                                {'external_lsas': 
                                                    {'checksum': '0',
                                                    'total': 0},
                                                'opaque_as_lsas': 
                                                    {'checksum': '0',
                                                    'total': 0}},
                                            'start': 0.0},
                                            'spf': 
                                                {'hold': 1000.0,
                                            'maximum': 5000.0,
                                            'start': 200.0}}}}}}}}}}

    golden_output_1 = {'execute.return_value': '''
        Routing Process 1 with ID 2.2.2.2 VRF default
        Routing Process Instance Number 1
        Stateful High Availability enabled
        Graceful-restart is configured
        Grace period: 60 state: Inactive 
        Last graceful restart exit status: None
        Supports only single TOS(TOS0) routes
        Supports opaque LSA
        Administrative distance 110
        Reference Bandwidth is 40000 Mbps
        SPF throttling delay time of 200.000 msecs,
        SPF throttling hold time of 1000.000 msecs, 
        SPF throttling maximum wait time of 5000.000 msecs
        LSA throttling start time of 0.000 msecs,
        LSA throttling hold interval of 5000.000 msecs, 
        LSA throttling maximum wait time of 5000.000 msecs
        Minimum LSA arrival 1000.000 msec
        LSA group pacing timer 10 secs
        Maximum paths to destination 8
        Number of external LSAs 0, checksum sum 0
        Number of opaque AS LSAs 0, checksum sum 0
        Number of areas is 1, 1 normal, 0 stub, 0 nssa
        Number of active areas is 1, 1 normal, 0 stub, 0 nssa
        Install discard route for summarized external routes.
        Install discard route for summarized internal routes.
        Area BACKBONE(0.0.0.0) (Inactive)
            Area has existed for 1w5d
            Interfaces in this area: 6 Active interfaces: 4
            Passive interfaces: 0  Loopback interfaces: 4
            No authentication available
            SPF calculation has run 2 times
             Last SPF ran for 0.000447s
            Area ranges are
            Number of LSAs: 1, checksum sum 0x9ccb
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_vrf_all(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpOspf(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_default_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpOspf(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# ========================================================
#  Unit test for 'show ip ospf mpls ldp interface'
#  Unit test for 'show ip ospf mpls ldp interface vrf all'
# ========================================================
class test_show_ip_ospf_mpls_ldp_interface(unittest.TestCase):

    '''Unit test for show ip ospf mpls ldp interface
       Unit test for show ip ospf mpls ldp interface vrf all'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'interfaces': 
                                            {'Ethernet2/1': 
                                                {'area': '0.0.0.1',
                                                'interface_type': 'broadcast',
                                                'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.1',
                                                        'igp_sync': False}},
                                                'name': 'Ethernet2/1',
                                                'state': 'bdr'}},
                                        'sham_links': 
                                            {'22.22.22.22 11.11.11.11': 
                                                {'area': '0.0.0.1',
                                                'interface_type': 'p2p',
                                                'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.1',
                                                        'igp_sync': False}},
                                                'name': '22.22.22.22 11.11.11.11',
                                                'state': 'p2p'},
                                            '22.22.22.22 33.33.33.33': 
                                                {'area': '0.0.0.1',
                                                'interface_type': 'p2p',
                                                'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.1',
                                                        'igp_sync': False}},
                                                'name': '22.22.22.22 '
                                                '33.33.33.33',
                                                'state': 'p2p'}}}}}}}}},
            'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'interfaces': 
                                            {'Ethernet2/2': 
                                                {'area': '0.0.0.0',
                                                'interface_type': 'broadcast',
                                                'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False}},
                                                'name': 'Ethernet2/2',
                                                'state': 'bdr'},
                                            'Ethernet2/3': 
                                                {'area': '0.0.0.0',
                                                'interface_type': 'broadcast',
                                                'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False}},
                                                'name': 'Ethernet2/3',
                                                'state': 'bdr'},
                                            'Ethernet2/4': 
                                                {'area': '0.0.0.0',
                                                'interface_type': 'broadcast',
                                                'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False}},
                                                'name': 'Ethernet2/4',
                                                'state': 'bdr'},
                                            'loopback0': 
                                                {'area': '0.0.0.0',
                                                'interface_type': 'loopback',
                                                'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False}},
                                                'name': 'loopback0',
                                                'state': 'loopback'}}}}}}}}}}}

    golden_output = {'execute.return_value': '''
        loopback0 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State LOOPBACK, Network type LOOPBACK
        Ethernet2/2 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State BDR, Network type BROADCAST
        Ethernet2/3 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State BDR, Network type BROADCAST
        Ethernet2/4 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State BDR, Network type BROADCAST
        Ethernet2/1 - Process ID 1 VRF VRF1, area 0.0.0.1
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State BDR, Network type BROADCAST
        SL1-0.0.0.0-22.22.22.22-11.11.11.11 - Process ID 1 VRF VRF1, area 0.0.0.1
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State P2P, Network type P2P
        SL2-0.0.0.0-22.22.22.22-33.33.33.33 - Process ID 1 VRF VRF1, area 0.0.0.1
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State P2P, Network type P2P
        '''}

    golden_parsed_output_1 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.0': 
                                        {'interfaces': 
                                            {'Ethernet4/1': 
                                                {'area': '0.0.0.0',
                                                'interface_type': 'broadcast',
                                                'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False}},
                                                'name': 'Ethernet4/1',
                                                'state': 'down'},
                                            'Ethernet4/10': 
                                                {'area': '0.0.0.0',
                                                'interface_type': 'broadcast',
                                                'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False}},
                                                'name': 'Ethernet4/10',
                                                'state': 'down'},
                                            'loopback1': 
                                                {'area': '0.0.0.0',
                                                'interface_type': 'loopback',
                                                'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False}},
                                                'name': 'loopback1',
                                                'state': 'loopback'},
                                            'loopback2': 
                                                {'area': '0.0.0.0',
                                                'interface_type': 'loopback',
                                                'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False}},
                                                'name': 'loopback2',
                                                'state': 'loopback'},
                                            'loopback3': 
                                                {'area': '0.0.0.0',
                                                'interface_type': 'loopback',
                                                'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False}},
                                                'name': 'loopback3',
                                                'state': 'loopback'},
                                            'loopback4': 
                                                {'area': '0.0.0.0',
                                                'interface_type': 'loopback',
                                                'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False}},
                                                'name': 'loopback4',
                                                'state': 'loopback'}}}}}}}}}}}

    golden_output_1 = {'execute.return_value': '''
        Ethernet4/1 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State DOWN, Network type BROADCAST
        Ethernet4/10 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State DOWN, Network type BROADCAST
        loopback1 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State LOOPBACK, Network type LOOPBACK
        loopback2 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State LOOPBACK, Network type LOOPBACK
        loopback3 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State LOOPBACK, Network type LOOPBACK
        loopback4 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State LOOPBACK, Network type LOOPBACK
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfMplsLdpInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_vrf_all(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpOspfMplsLdpInterface(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_default_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpOspfMplsLdpInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# ===================================================
#  Unit test for 'show ip ospf virtual-links'
#  Unit test for 'show ip ospf virtual-links vrf all'
# ===================================================
class test_show_ip_ospf_virtual_links(unittest.TestCase):

    '''Unit test for show ip ospf virtual-links
       Unit test for show ip ospf virtual-links vrf all'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'virtual_links': 
                                            {'0.0.0.1 4.4.4.4': 
                                                {'backbone_area_id': '0.0.0.0',
                                                'cost': 40,
                                                'dead_interval': 40,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:05',
                                                'index': 7,
                                                'interface': 'Ethernet1/5',
                                                'interface_type': 'point-to-point',
                                                'link_state': 'up',
                                                'name': 'VL1',
                                                'nbr_adjs': 1,
                                                'nbr_flood': 1,
                                                'nbr_total': 1,
                                                'neighbors': 
                                                    {'4.4.4.4': 
                                                        {'address': '20.3.4.4',
                                                        'dbd_option': '0x72',
                                                        'dead_timer': '00:00:33',
                                                        'hello_option': '0x32',
                                                        'last_change': '00:07:51',
                                                        'last_non_hello_received': '00:07:49',
                                                        'neighbor_router_id': '4.4.4.4',
                                                        'state': 'full',
                                                        'statistics': 
                                                            {'nbr_event_count': 5}}},
                                                'remote_addr': '20.3.4.4',
                                                'retransmit_interval': 5,
                                                'router_id': '4.4.4.4',
                                                'state': 'P2P',
                                                'statistics': 
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0},
                                                'transit_area_id': '0.0.0.1',
                                                'transmit_delay': 1,
                                                'unnumbered_interface': 'Ethernet1/5',
                                                'unnumbered_ip_address': '20.3.4.3',
                                                'wait_interval': 40}}}}}}}}}}}

    golden_output = {'execute.return_value': '''
        Virtual link VL1 to router 4.4.4.4 is up
            Transit area 0.0.0.1, via interface Eth1/5, remote addr 20.3.4.4
            Unnumbered interface using IP address of Ethernet1/5 (20.3.4.3)
            Process ID 1 VRF default, area 0.0.0.0
            State P2P, Network type P2P, cost 40
            Index 7, Transmit delay 1 sec
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:05
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
            Adjacency Information
            State is FULL, 5 state changes, last change 00:07:51
            Hello options 0x32, dbd options 0x72
            Last non-hello packet received 00:07:49
              Dead timer due in 00:00:33
        '''}

    def test_vrf_all(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpOspfVirtualLinks(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfVirtualLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ================================================
#  Unit test for 'show ip ospf sham-links'
#  Unit test for 'show ip ospf sham-links vrf all'
# ================================================
class test_show_ip_ospf_sham_links(unittest.TestCase):

    '''Unit test for show ip ospf sham-links
       Unit test for show ip ospf sham-links vrf all'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'1': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'sham_links': 
                                            {'22.22.22.22 11.11.11.11': 
                                                {'backbone_area_id': '0.0.0.0',
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'destination': '11.11.11.11',
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:02',
                                                'index': 6,
                                                'interface_type': 'point-to-point',
                                                'link_state': 'up',
                                                'local_id': '22.22.22.22',
                                                'name': 'SL1',
                                                'nbr_adjs': 1,
                                                'nbr_flood': 1,
                                                'nbr_total': 1,
                                                'neighbors': 
                                                    {'11.11.11.11': 
                                                        {'address': '11.11.11.11',
                                                        'area': '0.0.0.1',
                                                        'backbone_area_id': '0.0.0.0',
                                                        'dbd_option': '0x72',
                                                        'dead_timer': '00:00:38',
                                                        'hello_option': '0x32',
                                                        'instance': '1',
                                                        'last_change': '08:10:01',
                                                        'last_non_hello_received': 'never',
                                                        'local': '22.22.22.22',
                                                        'neighbor_router_id': '11.11.11.11',
                                                        'remote': '11.11.11.11',
                                                        'state': 'full',
                                                        'statistics': {'nbr_event_count': 8}}},
                                                'remote_id': '11.11.11.11',
                                                'retransmit_interval': 5,
                                                'state': 'P2P',
                                                'statistics': 
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0},
                                                'transit_area_id': '0.0.0.1',
                                                'transmit_delay': 1,
                                                'unnumbered_interface': 'loopback1',
                                                'unnumbered_ip_address': '22.22.22.22',
                                                'wait_interval': 40},
                                            '22.22.22.22 33.33.33.33': 
                                                {'authentication': 
                                                    {'auth_trailer_key': 
                                                        {'crypto_algorithm': 'simple'},
                                                    'auth_trailer_key_chain': 
                                                        {'key_chain': 'test',
                                                        'status': 'ready'}},
                                                'backbone_area_id': '0.0.0.0',
                                                'cost': 111,
                                                'dead_interval': 13,
                                                'destination': '33.33.33.33',
                                                'hello_interval': 3,
                                                'hello_timer': '00:00:01',
                                                'index': 7,
                                                'nbr_adjs': 0,
                                                'nbr_flood': 0,
                                                'nbr_total': 0,
                                                'interface_type': 'point-to-point',
                                                'link_state': 'up',
                                                'local_id': '22.22.22.22',
                                                'name': 'SL2',
                                                'remote_id': '33.33.33.33',
                                                'retransmit_interval': 5,
                                                'state': 'P2P',
                                                'statistics': 
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0},
                                                'transit_area_id': '0.0.0.1',
                                                'transmit_delay': 7,
                                                'unnumbered_interface': 'loopback1',
                                                'unnumbered_ip_address': '22.22.22.22',
                                                'wait_interval': 13}}}}}}}}}}}

    golden_output = {'execute.return_value': '''
        SL1-0.0.0.0-22.22.22.22-11.11.11.11 line protocol is up
            Unnumbered interface using IP address of loopback1 (22.22.22.22)
            Process ID 1 VRF VRF1, area 0.0.0.1
            State P2P, Network type P2P, cost 1
            Index 6, Transmit delay 1 sec
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:02
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
            Adjacency Information :
            Destination IP address: 11.11.11.11
         Neighbor 11.11.11.11, interface address 11.11.11.11
            Process ID 1 VRF VRF1, in area 0.0.0.1 via interface SL1-0.0.0.0-22.22.22.22
        -11.11.11.11
            State is FULL, 8 state changes, last change 08:10:01
            Hello options 0x32, dbd options 0x72
            Last non-hello packet received never
              Dead timer due in 00:00:38

         SL2-0.0.0.0-22.22.22.22-33.33.33.33 line protocol is up
            Unnumbered interface using IP address of loopback1 (22.22.22.22)
            Process ID 1 VRF VRF1, area 0.0.0.1
            State P2P, Network type P2P, cost 111
            Index 7, Transmit delay 7 sec
            0 Neighbors, flooding to 0, adjacent with 0
            Timer intervals: Hello 3, Dead 13, Wait 13, Retransmit 5
              Hello timer due in 00:00:01
            Simple authentication, using keychain test (ready)
            Number of opaque link LSAs: 0, checksum sum 0
            Adjacency Information :
            Destination IP address: 33.33.33.33
        '''}

    def test_vrf_all(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpOspfShamLinks(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfShamLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()



if __name__ == '__main__':
    unittest.main()
