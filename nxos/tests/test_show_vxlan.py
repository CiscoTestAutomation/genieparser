
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Parser
from parser.nxos.show_vxlan import  ShowNvePeers,\
                                    ShowNveVniSummary,\
                                    ShowNveVni,\
                                    ShowNveInterfaceDetail,\
                                    ShowNveMultisiteFabricLinks,\
                                    ShowNveMultisiteDciLinks, \
                                    ShowNveEthernetSegment,\
                                    ShowL2routeEvpnEternetSegmentAll,\
                                    ShowL2routeTopologyDetail,\
                                    ShowL2routeMacAllDetail,\
                                    ShowL2routeMacIpAllDetail,\
                                    ShowL2routeSummary

# Metaparser
from metaparser.util.exceptions import SchemaEmptyParserError

 
# =================================
#  Unit test for 'show nve peers'
# =================================

class test_show_nve_peers(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'nve1':{
            'nve_name': 'nve1',
            'peer_ip': {
                '201.202.1.1':{
                    'peer_state': 'up',
                    'learn_type': 'CP',
                    'uptime': '01:15:09',
                    'router_mac': 'n/a',
                },
                '204.1.1.1': {
                    'peer_state': 'up',
                    'learn_type': 'CP',
                    'uptime': '00:03:05',
                    'router_mac': '5e00.0002.0007',
                }
            },
        },
     }

    golden_output = {'execute.return_value': '''
    BL1# show nve peers
    Interface Peer-IP          State LearnType Uptime   Router-Mac
    --------- ---------------  ----- --------- -------- -----------------
    nve1      201.202.1.1      Up    CP        01:15:09 n/a
    nve1      204.1.1.1        Up    CP        00:03:05 5e00.0002.0007
        '''}

    def test_show_nve_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowNvePeers(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


    def test_show_nve_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowNvePeers(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==========================================
#  Unit test for 'show nve vni summary'
# ==========================================

class test_show_nve_vni_summary(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vni': {
            'summary': {
                'cp_vni_count': 21,
                'cp_vni_up': 21,
                'cp_vni_down': 0,
                'dp_vni_count': 0,
                'dp_vni_up': 0,
                'dp_vni_down': 0,
                 },
            },
        }

    golden_output = {'execute.return_value': '''
    BL1# show nve vni summary
    Codes: CP - Control Plane        DP - Data Plane
       UC - Unconfigured

    Total CP VNIs: 21    [Up: 21, Down: 0]
    Total DP VNIs: 0    [Up: 0, Down: 0]
        '''}

    def test_show_nve_vni_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowNveVniSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_nve_vni_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowNveVniSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==========================================
#  Unit test for 'show nve vni '
# ==========================================

class test_show_nve_vni(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'nve1': {
            'vni': {
                5001:{
                    'vni': 5001,
                    'mcast': "234.1.1.1",
                    'vni_state': "up",
                    'mode': "CP",
                    'type': "L2 [1001]",
                    'flags':'',
                },
                5002: {
                    'vni': 5002,
                    'mcast': "234.1.1.1",
                    'vni_state': "up",
                    'mode': "CP",
                    'type': "L2 [1002]",
                    'flags': '',
                },
                5003: {
                    'vni': 5003,
                    'mcast': "234.1.1.1",
                    'vni_state': "up",
                    'mode': "CP",
                    'type': "L2 [1003]",
                    'flags': '',
                },
                5004: {
                    'vni': 5004,
                    'mcast': "234.1.1.1",
                    'vni_state': "up",
                    'mode': "CP",
                    'type': "L2 [1004]",
                    'flags': '',
                },
                6004: {
                    'vni': 6004,
                    'mcast': "231.1.1.1",
                    'vni_state': "up",
                    'mode': "CP",
                    'type': "L2 [1014]",
                    'flags': '',
                },
                6005: {
                    'vni': 6005,
                    'mcast': "231.1.1.1",
                    'vni_state': "up",
                    'mode': "CP",
                    'type': "L2 [1015]",
                    'flags': '',
                },
                7001: {
                    'vni': 7001,
                    'mcast': "235.1.1.1",
                    'vni_state': "up",
                    'mode': "CP",
                    'type': "L2 [1103]",
                    'flags': '',
                },
                7002: {
                    'vni': 7002,
                    'mcast': "235.1.1.1",
                    'vni_state': "up",
                    'mode': "CP",
                    'type': "L2 [1104]",
                    'flags': '',
                },
                7003: {
                    'vni': 7003,
                    'mcast': "235.1.1.1",
                    'vni_state': "up",
                    'mode': "CP",
                    'type': "L2 [1105]",
                    'flags': '',
                },
                10001: {
                    'vni': 10001,
                    'mcast': "n/a",
                    'vni_state': "up",
                    'mode': "CP",
                    'type': "L3 [vni_10001]",
                    'flags': '',
                },
                10002: {
                    'vni': 10002,
                    'mcast': "n/a",
                    'vni_state': "up",
                    'mode': "CP",
                    'type': "L3 [vni_10002]",
                    'flags': '',
                },
                10005: {
                    'vni': 10005,
                    'mcast': "n/a",
                    'vni_state': "up",
                    'mode': "CP",
                    'type': "L3 [vni_10005]",
                    'flags': '',
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''
    Interface VNI      Multicast-group   State Mode Type [BD/VRF]      Flags
    --------- -------- ----------------- ----- ---- ------------------ -----
    nve1      5001     234.1.1.1         Up    CP   L2 [1001]
    nve1      5002     234.1.1.1         Up    CP   L2 [1002]
    nve1      5003     234.1.1.1         Up    CP   L2 [1003]
    nve1      5004     234.1.1.1         Up    CP   L2 [1004]
    nve1      6004     231.1.1.1         Up    CP   L2 [1014]
    nve1      6005     231.1.1.1         Up    CP   L2 [1015]
    nve1      7001     235.1.1.1         Up    CP   L2 [1103]
    nve1      7002     235.1.1.1         Up    CP   L2 [1104]
    nve1      7003     235.1.1.1         Up    CP   L2 [1105]
    nve1      10001    n/a               Up    CP   L3 [vni_10001]
    nve1      10002    n/a               Up    CP   L3 [vni_10002]
    nve1      10005    n/a               Up    CP   L3 [vni_10005]
        '''}

    def test_show_nve_vni_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowNveVni(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_nve_vni_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowNveVni(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==================================================
#  Unit test for 'show nve interface <nve> detail '
# ==================================================
class test_show_nve_interface_detail(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'nve1': {
            'if_name': 'nve1',
            'if_state': "up",
            'encap_type': "vxlan",  # Ops Str 'vxlan'
            'vpc_capability': "vpc-vip-only [notified]",  # Ops Str 'vpc-vip-only [notified]'
            'local_rmac': "5e00.0005.0007",  # Ops Str '5e00.0005.0007'
            'host_reach_mode': "control-plane",  # Ops Str 'control-plane'
            'source_if': "loopback1",  # Conf/Ops Str 'loopback1'
            'primary_ip': "201.11.11.11",  # Ops Str '201.11.11.11'
            'secondary_ip': "201.12.11.22",  # Ops Str '201.12.11.22'
            'src_if_state': "up",  # Ops Str 'up'
            'ir_cap_mode': "no",  # Ops Str 'no'
            'adv_vmac': True,  # Ops Bool True
            'nve_flags': "",  # Ops Str ''
            'nve_if_handle': 1224736769,  # Ops Int 1224736769
            'src_if_holddown_tm': 180,  # Ops Int 180
            'src_if_holdup_tm': 30,  # Ops Int 30
            'src_if_holddown_left': 0,  # Ops Int 0
            'vip_rmac': "0200.c90c.0b16",  # Ops Str '0200.c90c.0b16'
            'sm_state': "nve-intf-add-complete",  # Ops Str 'nve-intf-add-complete'
            'peer_forwarding_mode': False,  # Ops Bool False
            'dwn_strm_vni_cfg_mode': "n/a",  # Ops Str 'n/a'
            'src_intf_last_reinit_notify_type': "port-up",  # Ops Str 'port-up'
            'mcast_src_intf_last_reinit_notify_type': "none",  # Ops Str 'none'
            'multi_src_intf_last_reinit_notify_type': "none",  # Ops Str 'none'

        },
    }

    golden_output = {'execute.return_value': '''
    BL1# show nve interface nve 1 detail
    Interface: nve1, State: Up, encapsulation: VXLAN
     VPC Capability: VPC-VIP-Only [notified]
     Local Router MAC: 5e00.0005.0007
     Host Learning Mode: Control-Plane
     Source-Interface: loopback1 (primary: 201.11.11.11, secondary: 201.12.11.22)
     Source Interface State: Up
     IR Capability Mode: No
     Virtual RMAC Advertisement: Yes
     NVE Flags:
     Interface Handle: 0x49000001
     Source Interface hold-down-time: 180
     Source Interface hold-up-time: 30
     Remaining hold-down time: 0 seconds
     Virtual Router MAC: 0200.c90c.0b16
     Interface state: nve-intf-add-complete
     unknown-peer-forwarding: disable
     down-stream vni config mode: n/a
    Nve Src node last notif sent: Port-up
    Nve Mcast Src node last notif sent: None
    Nve MultiSite Src node last notif sent: None

        '''}

    golden_parsed_output_2 = {
        'nve1': {
            'if_name': 'nve1',
            'if_state': "down",
            'encap_type': "vxlan",
            'vpc_capability': "vpc-vip-only [notified]",
            'local_rmac': "6cb2.ae24.3f17",
            'host_reach_mode': "control-plane",
            'source_if': "loopback1",
            'primary_ip': "201.0.0.11",
            'secondary_ip': "201.12.11.22",
            'src_if_state': "up",
            'ir_cap_mode': "no",
            'adv_vmac': True,
            'nve_flags': "",
            'nve_if_handle': 1224736769,
            'src_if_holddown_tm': 180,
            'src_if_holdup_tm': 30,
            'src_if_holddown_left': 0,
            'vip_rmac': "0200.c90c.0b16",
            'vip_rmac_ro': "0200.6565.6565",
            'sm_state': "nve-intf-init",
            'multisite_bgw_if': "loopback2",
            'multisite_bgw_if_ip': '101.101.101.101',
            'multisite_bgw_if_admin_state': "down",
            'multisite_bgw_if_oper_state': "down",
            'multisite_bgw_if_oper_state_down_reason': "NVE not up."

        },
    }
    golden_output_2 = {'execute.return_value': '''
    MS-VPC-BL1(config-if)# Sh nve interface nve 1 detail
    Interface: nve1, State: Down, encapsulation: VXLAN
     VPC Capability: VPC-VIP-Only [notified]
     Local Router MAC: 6cb2.ae24.3f17
     Host Learning Mode: Control-Plane
     Source-Interface: loopback1 (primary: 201.0.0.11, secondary: 201.12.11.22)
     Source Interface State: Up
     Virtual RMAC Advertisement: Yes
     NVE Flags:
     Interface Handle: 0x49000001
     Source Interface hold-down-time: 180
     Source Interface hold-up-time: 30
     Remaining hold-down time: 0 seconds
     Multi-Site delay-restore time: 180 seconds
     Multi-Site delay-restore time left: 0 seconds
     Virtual Router MAC: 0200.c90c.0b16
     Virtual Router MAC Re-origination: 0200.6565.6565
     Interface state: nve-intf-init
     Multisite bgw-if: loopback2 (ip: 101.101.101.101, admin: Down, oper: Down)
     Multisite bgw-if oper down reason: NVE not up.

    '''}

    def test_show_nve_vni_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowNveInterfaceDetail(device=self.device)
        parsed_output = obj.parse(intf="nve1")
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_nve_vni_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowNveInterfaceDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ====================================================
#  Unit test for 'show nve multisites fabric-links'
# ====================================================

class test_show_fabric_links(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'multisite': {
            'Ethernet1/53':{
                'if_name': 'Ethernet1/53',
                'if_state': 'up'
            },
            'Ethernet1/54': {
                'if_name': 'Ethernet1/54',
                'if_state': 'down'
            },
        },
    }

    golden_output = {'execute.return_value': '''
    BMS-VPC-BL1# show nve multisite fabric-links
    Interface      State
    ---------      -----
    Ethernet1/53   Up
    Ethernet1/54   Down

    '''}

    def test_show_fabric_links(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowNveMultisiteFabricLinks(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_fabric_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowNveMultisiteFabricLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

# ====================================================
#  Unit test for 'show nve multisites dci-links'
# ====================================================

class test_show_dci_links(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'multisite': {
            'Ethernet1/50':{
                'if_name': 'Ethernet1/50',
                'if_state': 'up'
            },
            'Ethernet1/52': {
                'if_name': 'Ethernet1/52',
                'if_state': 'up'
            },
        },
    }

    golden_output = {'execute.return_value': '''
    BMS-VPC-BL1# show nve multisite dci-links
    Interface      State
    ---------      -----
    Ethernet1/50   Up
    Ethernet1/52   Up

    '''}

    def test_show_dci_links(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowNveMultisiteDciLinks(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_dci_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowNveMultisiteDciLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ====================================================
#  Unit test for 'show nve ethernet-segment'
# ====================================================

class test_show_nve_ethernet_segment(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
			'ethernet_segment': {
				'esi': {
					'0300.0000.0001.2c00.0309': {
						'esi': '0300.0000.0001.2c00.0309',
						'if_name': 'nve1',
						'es_state': 'up',
						'po_state': 'n/a',
						'nve_if_name': 'nve1',
						'nve_state': 'up',
						'host_reach_mode': 'control-plane',
						'active_vlans': '1,101-105,1001-1100,2001-2100,3001-3005',
						'df_vlans': '102,104,1002,1004,1006,1008,1010,1012,1014,1016,1018,1020,1022,1024'\
                                    ',1026,1028,1030,1032,1034,1036,1038,1040,1042,1044,1046,1048,1050,1052,1054,1056'\
                                    ',1058,1060,1062,1064,1066,1068,1070,1072,1074,1076,1078,1080,1082,1084,1086,1088'\
                                    ',1090,1092,1094,1096,1098,1100,2002,2004,2006,2008,2010,2012,2014,2016,2018,2020'\
                                    ',2022,2024,2026,2028,2030,2032,2034,2036,2038,2040,2042,2044,2046,2048,2050,2052'\
                                    ',2054,2056,2058,2060,2062,2064,2066,2068,2070,2072,2074,2076,2078,2080,2082,2084'\
                                    ',2086,2088,2090,2092,2094,2096,2098,2100,3002,3004',
						'active_vnis':  '501001-501100,502001-502100,503001-503005,600101-600105',
						'cc_failed_vlans': '',
						'cc_timer_left': '0',
						'num_es_mem':  2,
						'local_ordinal': 0,
						'df_timer_st': '00:00:00',
						'config_status': 'n/a',
						'df_list': '201.0.0.55 201.0.0.66',
						'es_rt_added': True,
						'ead_rt_added': False,
						'ead_evi_rt_timer_age': 'not running',
					},
				},
			},
		}

    golden_output = {'execute.return_value': '''
    MS-BL5(config)# sh nve ethernet-segment

    ESI: 0300.0000.0001.2c00.0309
       Parent interface: nve1
      ES State: Up
      Port-channel state: N/A
      NVE Interface: nve1
       NVE State: Up
       Host Learning Mode: control-plane
      Active Vlans: 1,101-105,1001-1100,2001-2100,3001-3005
       DF Vlans: 102,104,1002,1004,1006,1008,1010,1012,1014,1016,1018,1020,1022,1024
    ,1026,1028,1030,1032,1034,1036,1038,1040,1042,1044,1046,1048,1050,1052,1054,1056
    ,1058,1060,1062,1064,1066,1068,1070,1072,1074,1076,1078,1080,1082,1084,1086,1088
    ,1090,1092,1094,1096,1098,1100,2002,2004,2006,2008,2010,2012,2014,2016,2018,2020
    ,2022,2024,2026,2028,2030,2032,2034,2036,2038,2040,2042,2044,2046,2048,2050,2052
    ,2054,2056,2058,2060,2062,2064,2066,2068,2070,2072,2074,2076,2078,2080,2082,2084
    ,2086,2088,2090,2092,2094,2096,2098,2100,3002,3004
       Active VNIs: 501001-501100,502001-502100,503001-503005,600101-600105
      CC failed for VLANs:
      VLAN CC timer: 0
      Number of ES members: 2
      My ordinal: 0
      DF timer start time: 00:00:00
      Config State: N/A
      DF List: 201.0.0.55 201.0.0.66
      ES route added to L2RIB: True
      EAD/ES routes added to L2RIB: False
      EAD/EVI route timer age: not running
    '''}

    def test_show_nve_ethernet_segment(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowNveEthernetSegment(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_nve_ethernet_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowNveEthernetSegment(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

# ==============================================================
#  Unit test for 'show l2route evpn ethernet-segment all'
# ==============================================================

class test_show_l2route_evpn_ethernet_segment(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'evpn': {
            'ethernet_segment': {
                1:{
                    'ethernet_segment': '0300.0000.0001.2c00.0309',
                    'originating_rtr': '201.0.0.55',
                    'prod_name': 'vxlan',
                    'int_ifhdl': 'nve1',
                    'client_nfn': 64,
                },
                2: {
                    'ethernet_segment': '0300.0000.0001.2c00.0309',
                    'originating_rtr': '201.0.0.66',
                    'prod_name': 'bgp',
                    'int_ifhdl': 'n/a',
                    'client_nfn': 32,
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''
    MS-BL5(config)# sh l2route evpn ethernet-segment all

    ESI                      Orig Rtr. IP Addr  Prod  Ifindex      NFN Bitmap
    ------------------------ -----------------  ----- ----------- ----------
    0300.0000.0001.2c00.0309 201.0.0.55         VXLAN nve1         64
    0300.0000.0001.2c00.0309 201.0.0.66         BGP   N/A          32

    '''}

    def test_show_l2route_links(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowL2routeEvpnEternetSegmentAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_l2route_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2routeEvpnEternetSegmentAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

# ==============================================================
#  Unit test for 'show l2route topology detail'
# ==============================================================

class test_show_l2route_topology_detail(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'topology': {
            'topo_id': {
                101: {
                    'topo_name': {
                        'Vxlan-10001': {
                            'topo_name': 'Vxlan-10001',
                            'topo_type': 'vni',
                            'vni': 10001,
                            'encap_type': 0,
                            'iod': 0,
                            'if_hdl': 1224736769,
                            'vtep_ip': '201.11.11.11',
                            'emulated_ip': '201.12.11.22',
                            'emulated_ro_ip': '201.12.11.22',
                            'tx_id': 20,
                            'rcvd_flag': 0,
                            'rmac': '5e00.0005.0007',
                            'vrf_id': 3,
                            'vmac': '0200.c90c.0b16',
                            'flags': 'L3cp',
                            'sub_flags': '--',
                            'prev_flags': '-',
                        },
                    },
                },
                102: {
                    'topo_name': {
                        'Vxlan-10002': {
                            'topo_name': 'Vxlan-10002',
                            'topo_type': 'vni',
                            'vni': 10002,
                            'encap_type': 0,
                            'iod': 0,
                            'if_hdl': 1224736769,
                            'vtep_ip': '201.11.11.11',
                            'emulated_ip': '201.12.11.22',
                            'emulated_ro_ip': '201.12.11.22',
                            'tx_id': 21,
                            'rcvd_flag': 0,
                            'rmac': '5e00.0005.0007',
                            'vrf_id': 4,
                            'vmac': '0200.c90c.0b16',
                            'flags': 'L3cp',
                            'sub_flags': '--',
                            'prev_flags': '-',
                        },
                    },
                },
                103: {
                    'topo_name': {
                        'Vxlan-10003': {
                            'topo_name': 'Vxlan-10003',
                            'topo_type': 'vni',
                            'vni': 10003,
                            'encap_type': 0,
                            'iod': 0,
                            'if_hdl': 1224736769,
                            'vtep_ip': '201.11.11.11',
                            'emulated_ip': '201.12.11.22',
                            'emulated_ro_ip': '201.12.11.22',
                            'tx_id': 22,
                            'rcvd_flag': 0,
                            'rmac': '5e00.0005.0007',
                            'vrf_id': 5,
                            'vmac': '0200.c90c.0b16',
                            'flags': 'L3cp',
                            'sub_flags': '--',
                            'prev_flags': '-',
                        },
                    },
                },
                1205: {
                    'topo_name': {
                        'Vxlan-8003': {
                            'topo_name': 'Vxlan-8003',
                            'topo_type': 'vni',
                            'vni': 8003,
                            'encap_type': 0,
                            'iod': 0,
                            'if_hdl': 1224736769,
                            'vtep_ip': '201.11.11.11',
                            'emulated_ip': '201.12.11.22',
                            'emulated_ro_ip': '201.12.11.22',
                            'tx_id': 19,
                            'rcvd_flag': 0,
                            'rmac': '0000.0000.0000',
                            'vrf_id': 0,
                            'vmac': '0200.c90c.0b16',
                            'flags': 'L2cpBgp',
                            'sub_flags': 'Adv-MAC',
                            'prev_flags': '-',
                        },
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''
    Topology ID   Topology Name   Attributes
-----------   -------------   ----------
101           Vxlan-10001     VNI: 10001
                              Encap:0 IOD:0 IfHdl:1224736769
                              VTEP IP: 201.11.11.11
                              Emulated IP: 201.12.11.22
                              Emulated RO IP: 201.12.11.22
                              TX-ID: 20 (Rcvd Ack: 0)
                              RMAC: 5e00.0005.0007, VRFID: 3
                              VMAC: 0200.c90c.0b16
                              Flags: L3cp, Sub_Flags: --, Prev_Flags: -
102           Vxlan-10002     VNI: 10002
                              Encap:0 IOD:0 IfHdl:1224736769
                              VTEP IP: 201.11.11.11
                              Emulated IP: 201.12.11.22
                              Emulated RO IP: 201.12.11.22
                              TX-ID: 21 (Rcvd Ack: 0)
                              RMAC: 5e00.0005.0007, VRFID: 4
                              VMAC: 0200.c90c.0b16
                              Flags: L3cp, Sub_Flags: --, Prev_Flags: -
103           Vxlan-10003     VNI: 10003
                              Encap:0 IOD:0 IfHdl:1224736769
                              VTEP IP: 201.11.11.11
                              Emulated IP: 201.12.11.22
                              Emulated RO IP: 201.12.11.22
                              TX-ID: 22 (Rcvd Ack: 0)
                              RMAC: 5e00.0005.0007, VRFID: 5
                              VMAC: 0200.c90c.0b16
                              Flags: L3cp, Sub_Flags: --, Prev_Flags: -
1205          Vxlan-8003      VNI: 8003
                              Encap:0 IOD:0 IfHdl:1224736769
                              VTEP IP: 201.11.11.11
                              Emulated IP: 201.12.11.22
                              Emulated RO IP: 201.12.11.22
                              TX-ID: 19 (Rcvd Ack: 0)
                              RMAC: 0000.0000.0000, VRFID: 0
                              VMAC: 0200.c90c.0b16
                              Flags: L2cpBgp, Sub_Flags: Adv-MAC, Prev_Flags: -

    4294967291    BARRIER         N/A
    4294967294    GLOBAL          N/A
    4294967295    ALL             N/A


    '''}

    def test_show_l2route_topology(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowL2routeTopologyDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_topology_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2routeTopologyDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

# ==============================================================
#  Unit test for 'show l2route mac all detail'
# ==============================================================

class test_show_l2route_mac_all_detail(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'topology': {
            'topo_id': {
                101: {
                    'mac': {
                        '5e00.0002.0007': {  # Ops Str '5e00.0002.0007'
                            'mac_addr': '5e00.0002.0007',
                            'prod_type': 'vxlan',  # Ops Str 'vxlan'
                            'flags': 'rmac',  # Ops Str 'rmac'
                            'seq_num': 0,  # Ops Int 0
                            'next_hop1': '204.1.1.1',  # Ops Str '204.1.1.1'
                            'rte_res': 'regular',  # Ops Str 'regular'
                            'fwd_state': 'Resolved (PeerID: 2)',  # Ops Str 'Resolved (PeerID: 2)'
                        },
                    },
                },
                1001: {
                    'mac': {
                        'fa16.3ea3.fb66': {
                            'mac_addr': 'fa16.3ea3.fb66',
                            'prod_type': 'local',
                            'flags': 'l',
                            'seq_num': 0,
                            'next_hop1': 'Ethernet1/5',
                            'rte_res': 'regular',
                            'fwd_state': 'Resolved',
                            'sent_to': 'bgp',
                            'soo': 774975538,
                        },
                        'fa16.3ec2.34fe': {
                            'mac_addr': 'fa16.3ec2.34fe',
                            'prod_type': 'bgp',
                            'flags': 'splrcv',
                            'seq_num': 0,
                            'next_hop1': '204.1.1.1',
                            'rte_res': 'regular',
                            'fwd_state': 'Resolved (PeerID: 2)',
                            'sent_to': 'l2fwder',
                        },
                    },
                },
            }
        }
    }

    golden_output = {'execute.return_value': '''
    BL1# show l2route mac all detail

    Flags -(Rmac):Router MAC (Stt):Static (L):Local (R):Remote (V):vPC link
    (Dup):Duplicate (Spl):Split (Rcv):Recv (AD):Auto-Delete (D):Del Pending
    (S):Stale (C):Clear, (Ps):Peer Sync (O):Re-Originated (Nho):NH-Override
    (Pf):Permanently-Frozen

    Topology    Mac Address    Prod   Flags         Seq No     Next-Hops
    ----------- -------------- ------ ------------- ---------- ----------------
    101         5e00.0002.0007 VXLAN  Rmac          0          204.1.1.1
                Route Resolution Type: Regular
                Forwarding State: Resolved (PeerID: 2)

    1001        fa16.3ea3.fb66 Local  L,            0          Eth1/5
                Route Resolution Type: Regular
                Forwarding State: Resolved
                Sent To: BGP
                SOO: 774975538

    1001        fa16.3ec2.34fe BGP    SplRcv        0          204.1.1.1
                Route Resolution Type: Regular
                Forwarding State: Resolved (PeerID: 2)
                Sent To: L2FWDER

    '''}

    def test_show_l2route_mac_all_detail(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowL2routeMacAllDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_mac_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2routeMacAllDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

# ==============================================================
#  Unit test for 'show l2route mac-ip all detail'
# ==============================================================

class test_show_l2route_mac_ip_all_detail(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'topology': {
            'topo_id': {
                1001: {
                    'mac_ip': {
                        'fa16.3ec2.34fe': {
                            'mac_addr': 'fa16.3ec2.34fe',
                            'mac_ip_prod_type': 'bgp',
                            'mac_ip_flags': '--',
                            'seq_num': 0,
                            'next_hop1': '204.1.1.1',
                            'host_ip': '5.1.10.11',
                        },
                        'fa16.3ea3.fb66': {
                            'mac_addr': 'fa16.3ea3.fb66',
                            'mac_ip_prod_type': 'hmm',
                            'mac_ip_flags': '--',
                            'seq_num': 0,
                            'next_hop1': 'local',
                            'host_ip': '5.1.10.55',
                            'sent_to': 'bgp',
                            'soo': 774975538,
                            'l3_info': 10001,
                        },
                    },
                },
            }
        }
    }

    golden_output = {'execute.return_value': '''
    BL1# show l2route mac-ip all detail
    Flags -(Rmac):Router MAC (Stt):Static (L):Local (R):Remote (V):vPC link
    (Dup):Duplicate (Spl):Split (Rcv):Recv(D):Del Pending (S):Stale (C):Clear
    (Ps):Peer Sync (Ro):Re-Originated
    Topology    Mac Address    Prod   Flags         Seq No     Host IP         Next-Hops
    ----------- -------------- ------ ---------- --------------- ---------------
    1001        fa16.3ec2.34fe BGP    --            0          5.1.10.11      204.1.1.1
    1001        fa16.3ea3.fb66 HMM    --            0          5.1.10.55      Local
                Sent To: BGP
                SOO: 774975538
                L3-Info: 10001
    '''}

    def test_show_l2route_mac_ip_all_detail(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowL2routeMacIpAllDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_mac_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2routeMacIpAllDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

# ==============================================================
#  Unit test for 'show l2route summary'
# ==============================================================
class test_show_l2route_summary(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'summary': {
            'total_memory': 6967,
            'numof_converged_tables': 47,
            'table_name': {
                'Topology': {
                    'producer_name': {
                        'vxlan': {
                            'producer_name': 'vxlan',
                            'id': 11,
                            'objects': 21,
                            'memory': 5927,
                        },
                        'total_obj': 21,
                        'total_mem': 5927,
                    },
                },
                'MAC': {
                    'producer_name': {
                        'local': {
                            'producer_name': 'local',
                            'id': 3,
                            'objects': 1,
                            'memory': 152,
                        },
                        'bgp': {
                            'producer_name': 'bgp',
                            'id': 5,
                            'objects': 1,
                            'memory': 152,
                        },
                        'vxlan': {
                            'producer_name': 'vxlan',
                            'id': 11,
                            'objects': 1,
                            'memory': 152,
                        },
                        'total_obj': 3,
                        'total_mem': 456,
                    }
                },
                'PEERID': {
                    'producer_name': {
                        'vxlan': {
                            'producer_name': 'vxlan',
                            'id': 11,
                            'objects': 2,
                            'memory': 312,
                        },
                        'total_obj': 2,
                        'total_mem': 312,
                    }
                },
                'MAC-IP': {
                    'producer_name': {
                        'bgp': {
                            'producer_name': 'bgp',
                            'id': 5,
                            'objects': 1,
                            'memory': 136,
                        },
                        'hmm': {
                            'producer_name': 'hmm',
                            'id': 12,
                            'objects': 1,
                            'memory': 136,
                        },
                        'total_obj': 2,
                        'total_mem': 272,
                    }
                },
            }
        }
    }

    golden_output = {'execute.return_value': '''
    BL1# show l2route summary
    L2ROUTE Summary
    Total Memory: 6967
    Number of Converged Tables: 47
    Table Name: Topology
    Producer   (ID)   Objects      Memory (Bytes)
    ---------------   ----------   --------------
    VXLAN     (11 )   21           5927
    ---------------------------------------------
    Total             21           5927
    ---------------------------------------------

    Table Name: MAC
    Producer   (ID)   Objects      Memory (Bytes)
    ---------------   ----------   --------------
    Local     (3  )   1            152
    BGP       (5  )   1            152
    VXLAN     (11 )   1            152
    ---------------------------------------------
    Total             3            456
    ---------------------------------------------

    Table Name: PEERID
    Producer   (ID)   Objects      Memory (Bytes)
    ---------------   ----------   --------------
    VXLAN     (11 )   2            312
    ---------------------------------------------
    Total             2            312
    ---------------------------------------------

    Table Name: MAC-IP
    Producer   (ID)   Objects      Memory (Bytes)
    ---------------   ----------   --------------
    BGP       (5  )   1            136
    HMM       (12 )   1            136
    ---------------------------------------------
    Total             2            272
    ---------------------------------------------

    '''}

    def test_show_l2route_summary(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowL2routeSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_mac_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2routeSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()