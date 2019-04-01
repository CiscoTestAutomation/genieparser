
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# iosxe show_ospf
from genie.libs.parser.ios.show_ospf import ShowIpOspf,\
                                   ShowIpOspfInterface,\
                                   ShowIpOspfNeighborDetail,\
                                   ShowIpOspfShamLinks,\
                                   ShowIpOspfVirtualLinks,\
                                   ShowIpOspfDatabaseRouter,\
                                   ShowIpOspfDatabaseExternal,\
                                   ShowIpOspfDatabaseNetwork,\
                                   ShowIpOspfDatabaseSummary,\
                                   ShowIpOspfDatabaseOpaqueArea,\
                                   ShowIpOspfMplsLdpInterface,\
                                   ShowIpOspfMplsTrafficEngLink

from genie.libs.parser.iosxe.tests.test_show_ospf import test_show_ip_ospf as test_show_ip_ospf_iosxe,\
                                                        test_show_ip_ospf_interface as test_show_ip_ospf_interface_iosxe,\
                                                        test_show_ip_ospf_neighbor_detail as test_show_ip_ospf_neighbor_detail_iosxe,\
                                                        test_show_ip_ospf_sham_links as test_show_ip_ospf_sham_links_iosxe,\
                                                        test_show_ip_ospf_virtual_links as test_show_ip_ospf_virtual_links_iosxe,\
                                                        test_show_ip_ospf_database_router as test_show_ip_ospf_database_router_iosxe,\
                                                        test_show_ip_ospf_database_external as test_show_ip_ospf_database_external_iosxe,\
                                                        test_show_ip_ospf_database_network as test_show_ip_ospf_database_network_iosxe,\
                                                        test_show_ip_ospf_database_summary as test_show_ip_ospf_database_summary_iosxe,\
                                                        test_show_ip_ospf_mpls_traffic_eng_link as test_show_ip_ospf_mpls_traffic_eng_link_iosxe,\
                                                        test_show_ip_ospf_database_opaque_area as test_show_ip_ospf_database_opaque_area_iosxe,\
                                                        test_show_ip_ospf_mpls_ldp_interface as test_show_ip_ospf_mpls_ldp_interface_iosxe


# ============================
# Unit test for 'show ip ospf'
# ============================
class test_show_ip_ospf(test_show_ip_ospf_iosxe):
    golden_parsed_output_ios = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "1": {
                            "start_time": "00:00:20.892",
                            "enable": True,
                            "interface_flood_pacing_timer": 33,
                            "areas": {
                                "0.0.0.1": {
                                    "ranges": {},
                                    "area_id": "0.0.0.1",
                                    "area_type": "normal",
                                    "statistics": {
                                        "flood_list_length": 0,
                                        "dcbitless_lsa_count": 1,
                                        "area_scope_lsa_cksum_sum": "0x0D8C1F",
                                        "area_scope_opaque_lsa_count": 0,
                                        "area_scope_opaque_lsa_cksum_sum": "0x000000",
                                        "spf_runs_count": 3,
                                        "indication_lsa_count": 1,
                                        "area_scope_lsa_count": 28,
                                        "donotage_lsa_count": 0,
                                        "spf_last_executed": "6d06h",
                                        "interfaces_count": 1
                                    }
                                },
                                "0.0.0.0": {
                                    "ranges": {},
                                    "area_id": "0.0.0.0",
                                    "area_type": "normal",
                                    "statistics": {
                                        "area_scope_lsa_cksum_sum": "0x0848BC",
                                        "dcbitless_lsa_count": 11,
                                        "indication_lsa_count": 0,
                                        "area_scope_opaque_lsa_count": 0,
                                        "area_scope_lsa_count": 14,
                                        "flood_list_length": 0,
                                        "loopback_count": 1,
                                        "spf_runs_count": 8,
                                        "interfaces_count": 3,
                                        "donotage_lsa_count": 0,
                                        "spf_last_executed": "6d06h",
                                        "area_scope_opaque_lsa_cksum_sum": "0x000000"
                                    }
                                }
                            },
                            "event_log": {
                                "mode": "cyclic",
                                "max_events": 1000,
                                "enable": True
                            },
                            "redistribution": {
                                "static": {
                                    "subnets": "subnets",
                                    "enabled": True
                                },
                                "max_prefix": {
                                    "prefix_thld": 75
                                },
                                "connected": {
                                    "subnets": "subnets",
                                    "enabled": True
                                }
                            },
                            "nssa": True,
                            "total_areas_transit_capable": 0,
                            "bfd": {
                                "enable": False
                            },
                            "total_areas": 2,
                            "lls": True,
                            "graceful_restart": {
                                "ietf": {
                                    "helper_enable": True,
                                    "type": "ietf",
                                    "enable": False
                                },
                                "cisco": {
                                    "helper_enable": True,
                                    "type": "cisco",
                                    "enable": False
                                }
                            },
                            "external_flood_list_length": 0,
                            "nsr": {
                                "enable": False
                            },
                            "retransmission_pacing_timer": 66,
                            "db_exchange_summary_list_optimization": True,
                            "lsa_group_pacing_timer": 240,
                            "total_nssa_areas": 0,
                            "router_id": "10.1.1.1",
                            "total_stub_areas": 0,
                            "area_transit": True,
                            "stub_router": {
                                "always": {
                                    "external_lsa": False,
                                    "always": False,
                                    "include_stub": False,
                                    "summary_lsa": False
                                }
                            },
                            "auto_cost": {
                                "enable": False,
                                "reference_bandwidth": 100,
                                "bandwidth_unit": "mbps"
                            },
                            "adjacency_stagger": {
                                "initial_number": 300,
                                "maximum_number": 300
                            },
                            "database_control": {
                                "max_lsa_current": 0,
                                "max_lsa": 123,
                                "max_lsa_ignore_time": 300,
                                "max_lsa_reset_time": 600,
                                "max_lsa_ignore_count": 5,
                                "max_lsa_warning_only": False,
                                "max_lsa_current_count": 0,
                                "max_lsa_limit": 5000
                            },
                            "spf_control": {
                                "incremental_spf": False,
                                "throttle": {
                                    "lsa": {
                                        "arrival": 1000
                                    },
                                    "spf": {
                                        "maximum": 10000,
                                        "start": 5000,
                                        "hold": 10000
                                    }
                                }
                            },
                            "elapsed_time": "6d06h",
                            "opqaue_lsa": True,
                            "total_normal_areas": 2,
                            "numbers": {
                                "dc_bitless": 0,
                                "opaque_as_lsa_checksum": "0x000000",
                                "external_lsa": 0,
                                "opaque_as_lsa": 0,
                                "do_not_age": 0,
                                "external_lsa_checksum": "0x000000"
                            },
                            "flags": {
                                "abr": True
                            }
                        }
                    }
                }
            }
        }
    }
}

    golden_output_ios =  {'execute.return_value': '''
    N95_1#show ip ospf
 Routing Process "ospf 1" with ID 10.1.1.1
 Start time: 00:00:20.892, Time elapsed: 6d06h
 Supports only single TOS(TOS0) routes
 Supports opaque LSA
 Supports Link-local Signaling (LLS)
 Supports area transit capability
 Supports NSSA (compatible with RFC 3101)
 Supports Database Exchange Summary List Optimization (RFC 5243)

 Event-log enabled, Maximum number of events: 1000, Mode: cyclic
 It is an area border router
 Router is not originating router-LSAs with maximum metric
 Initial SPF schedule delay 5000 msecs
 Redistributing External Routes from,
    connected, includes subnets in redistribution
    static, includes subnets in redistribution
    Maximum limit of redistributed prefixes 5000 (warning-only)
    Threshold for warning message 90%
 Maximum number of non self-generated LSA allowed 123
    Current number of non self-generated LSA 0
    Threshold for warning message 75%
    Ignore-time 5 minutes, reset-time 10 minutes
    Ignore-count allowed 5, current ignore-count 0
 Minimum hold time between two consecutive SPFs 10000 msecs
 Maximum wait time between two consecutive SPFs 10000 msecs
 Incremental-SPF disabled
 Minimum LSA interval 5 secs
 Minimum LSA arrival 1000 msecs
 LSA group pacing timer 240 secs
 Interface flood pacing timer 33 msecs
 Retransmission pacing timer 66 msecs
 EXCHANGE/LOADING adjacency limit: initial 300, process maximum 300
 Number of external LSA 0. Checksum Sum 0x000000
 Number of opaque AS LSA 0. Checksum Sum 0x000000
 Number of DCbitless external and opaque AS LSA 0
 Number of DoNotAge external and opaque AS LSA 0
 Number of areas in this router is 2. 2 normal 0 stub 0 nssa
 Number of areas transit capable is 0
 External flood list length 0
 IETF NSF helper support enabled
 Cisco NSF helper support enabled
 Reference bandwidth unit is 100 mbps
    Area BACKBONE(0.0.0.0)
        Number of interfaces in this area is 3 (1 loopback)
        Area has no authentication
        SPF algorithm last executed 6d06h ago
        SPF algorithm executed 8 times
        Area ranges are
        Number of LSA 14. Checksum Sum 0x0848BC
        Number of opaque link LSA 0. Checksum Sum 0x000000
        Number of DCbitless LSA 11
        Number of indication LSA 0
        Number of DoNotAge LSA 0
        Flood list length 0
      Area 0.0.0.1
        Number of interfaces in this area is 1
        Area has no authentication
        SPF algorithm last executed 6d06h ago
        SPF algorithm executed 3 times
        Area ranges are
        Number of LSA 28. Checksum Sum 0x0D8C1F
        Number of opaque link LSA 0. Checksum Sum 0x000000
        Number of DCbitless LSA 1
        Number of indication LSA 1
        Number of DoNotAge LSA 0
        Flood list length 0


'''}
    def test_show_ip_ospf_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspf(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ip_ospf_ios(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_ios)
        obj = ShowIpOspf(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_ios)


# ======================================
# Unit test for 'show ip ospf interface'
# ======================================
class test_show_ip_ospf_interface(test_show_ip_ospf_interface_iosxe):

    def test_show_ip_ospf_interface_full1(self):
        super().test_show_ip_ospf_interface_full1()

        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper

        obj = ShowIpOspfInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_interface_full2(self):
        super().test_show_ip_ospf_interface_full2()

        self.maxDiff = None
        def mapper(key):
            return self.outputs[key]

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper

        obj = ShowIpOspfInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ip_ospf_interface_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ============================================
# Unit test for 'show ip ospf neighbor detail'
#============================================
class test_show_ip_ospf_neighbor_detail(test_show_ip_ospf_neighbor_detail_iosxe):

    def test_show_ip_ospf_neighbor_detail_full1(self):
        super().test_show_ip_ospf_neighbor_detail_full1()
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]


        self.device.execute = Mock()
        self.device.execute.side_effect = mapper

        obj = ShowIpOspfNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_neighbor_detail_full2(self):
        super().test_show_ip_ospf_neighbor_detail_full2()

        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper

        obj = ShowIpOspfNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ip_ospf_neighbor_detail_full3(self):
        super().test_show_ip_ospf_neighbor_detail_full3()

        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]


        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        obj = ShowIpOspfNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_ip_ospf_neighbor_detail_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfNeighborDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =======================================
# Unit test for 'show ip ospf sham-links'
# =======================================
class test_show_ip_ospf_sham_links(test_show_ip_ospf_sham_links_iosxe):

    def test_show_ip_ospf_sham_links_full1(self):
        super().test_show_ip_ospf_sham_links_full1()
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper

        obj = ShowIpOspfShamLinks(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_sham_links_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfShamLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==========================================
# Unit test for 'show ip ospf virtual-links'
# ==========================================
class test_show_ip_ospf_virtual_links(test_show_ip_ospf_virtual_links_iosxe):

    golden_parsed_output1 = {
        'vrf': 
            {'VRF1': 
                {'address_family': 
                    {'ipv4': 
                        {'instance': 
                            {'2': 
                                {'areas': 
                                    {'0.0.0.1': 
                                        {'virtual_links': 
                                            {'0.0.0.1 10.36.3.3': 
                                                {'adjacency_state': 'full',
                                                'dcbitless_lsa_count': 7,
                                                'dead_interval': 40,
                                                'demand_circuit': True,
                                                'donotage_lsa': 'not allowed',
                                                'first': '0x0(0)/0x0(0)',
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:08',
                                                'index': '1/3',
                                                'interface': 'GigabitEthernet0/1',
                                                'last_retransmission_max_length': 0,
                                                'last_retransmission_max_scan': 0,
                                                'last_retransmission_scan_length': 0,
                                                'last_retransmission_scan_time': 0,
                                                'link_state': 'up',
                                                'name': 'VL0',
                                                'next': '0x0(0)/0x0(0)',
                                                'retrans_qlen': 0,
                                                'retransmit_interval': 5,
                                                'router_id': '10.36.3.3',
                                                'state': 'point-to-point,',
                                                'topology': 
                                                    {0: 
                                                        {'cost': 1,
                                                        'disabled': False,
                                                        'name': 'Base',
                                                        'shutdown': False}},
                                                'total_retransmission': 0,
                                                'transit_area_id': '0.0.0.1',
                                                'transmit_delay': 1,
                                                'wait_interval': 40}}}}}}}}}}}

    def test_show_ip_ospf_virtual_links_full1(self):
        super().test_show_ip_ospf_virtual_links_full1()
        
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpOspfVirtualLinks(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_sham_links_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfVirtualLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ============================================
# Unit test for 'show ip ospf database router'
# ============================================
class test_show_ip_ospf_database_router(test_show_ip_ospf_database_router_iosxe):

    def test_show_ip_ospf_database_router_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseRouter(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_database_router_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseRouter(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==============================================
# Unit test for 'show ip ospf database external'
# ==============================================
class test_show_ip_ospf_database_external(test_show_ip_ospf_database_external_iosxe):

    def test_show_ip_ospf_database_external_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseExternal(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_database_external_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseExternal(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==============================================
# Unit test for 'show ip ospf database netwwork'
# ==============================================
class test_show_ip_ospf_database_network(test_show_ip_ospf_database_network_iosxe):

    def test_show_ip_ospf_database_network_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseNetwork(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_database_network_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseNetwork(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==============================================
# Unit test for 'show ip ospf database summary'
# ==============================================
class test_show_ip_ospf_database_summary(test_show_ip_ospf_database_summary_iosxe):

    def test_show_ip_ospf_database_summary_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_database_summary_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =================================================
# Unit test for 'show ip ospf database opaque-area'
# =================================================
class test_show_ip_ospf_database_opaque_area(test_show_ip_ospf_database_opaque_area_iosxe):

    def test_show_ip_ospf_database_opaque_area_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseOpaqueArea(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_database_opaque_area_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseOpaqueArea(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ===============================================
# Unit test for 'show ip ospf mpls ldp interface'
# ===============================================
class test_show_ip_ospf_mpls_ldp_interface(test_show_ip_ospf_mpls_ldp_interface_iosxe):

    def test_show_ip_ospf_mpls_ldp_interface_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfMplsLdpInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_mpls_ldp_interface_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfMplsLdpInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==================================================
# Unit test for 'show ip ospf mpls traffic-eng link'
# ==================================================
class test_show_ip_ospf_mpls_traffic_eng_link(test_show_ip_ospf_mpls_traffic_eng_link_iosxe):

    def test_show_ip_ospf_mpls_traffic_eng_link_full1(self):

        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        raw1 = '''\
            R1_ospf_xe#show ip ospf mpls traffic-eng link

            OSPF Router with ID (10.4.1.1) (Process ID 1)

            Area 0 has 2 MPLS TE links. Area instance is 2.

            Links in hash bucket 8.
            Link is associated with fragment 2. Link instance is 2
              Link connected to Broadcast network
              Link ID : 10.1.2.1
              Interface Address : 10.1.2.1
              Admin Metric te: 1 igp: 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth : 93750000
              Number of Priority : 8
              Priority 0 : 93750000     Priority 1 : 93750000
              Priority 2 : 93750000     Priority 3 : 93750000
              Priority 4 : 93750000     Priority 5 : 93750000
              Priority 6 : 93750000     Priority 7 : 93750000
              Affinity Bit : 0x0

            Links in hash bucket 9.
            Link is associated with fragment 1. Link instance is 2
              Link connected to Broadcast network
              Link ID : 10.1.4.4
              Interface Address : 10.1.4.1
              Admin Metric te: 1 igp: 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth : 93750000
              Number of Priority : 8
              Priority 0 : 93750000     Priority 1 : 93750000
              Priority 2 : 93750000     Priority 3 : 93750000
              Priority 4 : 93750000     Priority 5 : 93750000
              Priority 6 : 93750000     Priority 7 : 93750000
              Affinity Bit : 0x0

                OSPF Router with ID (10.229.11.11) (Process ID 2)

            Area 1 MPLS TE not initialized
            '''
        raw2 = '''\
            R1_ospf_xe#show running-config | section router ospf 1
              router ospf 1
            '''
        raw3 = '''\
            R1_ospf_xe#show running-config | section router ospf 2
              router ospf 2 vrf VRF1
            '''

        self.outputs = {}
        self.outputs['show ip ospf mpls traffic-eng link'] = raw1
        self.outputs['show running-config | section router ospf 1'] = raw2
        self.outputs['show running-config | section router ospf 2'] = raw3
        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        obj = ShowIpOspfMplsTrafficEngLink(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_mpls_traffic_eng_link_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfMplsTrafficEngLink(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
