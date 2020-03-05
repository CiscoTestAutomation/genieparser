
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_evpn
from genie.libs.parser.iosxr.show_evpn import (ShowEvpnEvi,
                                               ShowEvpnEviDetail,
                                               ShowEvpnEviMac,
                                               ShowEvpnEviMacPrivate,
                                               ShowEvpnInternalLabelDetail,
                                               ShowEvpnEthernetSegment,
                                               ShowEvpnEthernetSegmentDetail,
                                               ShowEvpnEthernetSegmentEsiDetail,
                                               ShowEvpnInternalLabel,
                                               ShowEvpnEthernetSegmentPrivate)

# ===================================================
#  Unit test for 'show evpn evi'
# ===================================================

class TestShowEvpnEvi(unittest.TestCase):

    '''Unit test for 'show evpn evi'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'evi': {
            1000: {
                'bridge_domain': 'VPWS:1000',
                'type': 'VPWS (vlan-unaware)',
            },
            2000: {
                'bridge_domain': 'XC-POD1-EVPN',
                'type': 'EVPN',
            },
            2001: {
                'bridge_domain': 'XC-POD2-EVPN',
                'type': 'EVPN',
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        RP/0/RSP1/CPU0:Router1#show evpn evi
        EVI        Bridge                       Domain Type
        ---------- ---------------------------- -------------------
        1000        VPWS:1000                   VPWS (vlan-unaware)
        2000        XC-POD1-EVPN                EVPN
        2001        XC-POD2-EVPN                EVPN

        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowEvpnEvi(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowEvpnEvi(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)

# ===================================================
#  Unit test for 'show evpn evi detail'
# ===================================================

class TestShowEvpnEviDetail(unittest.TestCase):

    '''Unit test for 'show evpn evi detail'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'evi': {
            145: {
                'bridge_domain': 'tb1-core1',
                'type': 'PBB',
                'unicast_label': '16000',
                'multicast_label': '16001',
                'rd_config': 'none',
                'rd_auto': '(auto) 10.1.100.100:145',
                'rt_auto': '100:145',
                'route_target_in_use': {
                    '100:145': {
                        'import': True,
                        'export': True,
                    },
                },
            },
            165: {
                'bridge_domain': 'tb1-core2',
                'type': 'PBB',
                'unicast_label': '16002',
                'multicast_label': '16003',
                'rd_config': 'none',
                'rd_auto': '(auto) 10.1.100.100:165',
                'rt_auto': '100:165',
                'route_target_in_use': {
                    '100:165': {
                        'import': True,
                        'export': True,
                    },
                },
            },
            185: {
                'bridge_domain': 'tb1-core3',
                'type': 'PBB',
                'unicast_label': '16004',
                'multicast_label': '16005',
                'rd_config': 'none',
                'rd_auto': '(auto) 10.1.100.100:185',
                'rt_auto': '100:185',
                'route_target_in_use': {
                    '100:185': {
                        'import': True,
                        'export': True,
                    },
                },
            },
            65535: {
                'bridge_domain': 'ES:GLOBAL',
                'type': 'BD',
                'unicast_label': '0',
                'multicast_label': '0',
                'rd_config': 'none',
                'rd_auto': '(auto) 10.1.100.100:0',
                'rt_auto': 'none',
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        RP/0/RSP0/CPU0:Router1#show evpn evi detail
        EVI        Bridge Domain                Type   
        ---------- ---------------------------- -------
        145        tb1-core1                    PBB 
        Unicast Label  : 16000
        Multicast Label: 16001
        RD Config: none
        RD Auto  : (auto) 10.1.100.100:145
        RT Auto  : 100:145
        Route Targets in Use           Type   
        ------------------------------ -------
        100:145                        Import 
        100:145                        Export 

        165        tb1-core2                    PBB 
        Unicast Label  : 16002
        Multicast Label: 16003
        RD Config: none
        RD Auto  : (auto) 10.1.100.100:165
        RT Auto  : 100:165
        Route Targets in Use           Type   
        ------------------------------ -------
        100:165                        Import 
        100:165                        Export 

        185        tb1-core3                    PBB 
        Unicast Label  : 16004
        Multicast Label: 16005
        RD Config: none
        RD Auto  : (auto) 10.1.100.100:185
        RT Auto  : 100:185
        Route Targets in Use           Type   
        ------------------------------ -------
        100:185                        Import 
        100:185                        Export 

        65535      ES:GLOBAL                    BD  
        Unicast Label  : 0
        Multicast Label: 0
        RD Config: none
        RD Auto  : (auto) 10.1.100.100:0
        RT Auto  : none
        Route Targets in Use           Type   
        ------------------------------ -------
        0100.9eff.0210                 Import 
        0100.beff.cf01                 Import 
        0100.beff.0303                 Import

        '''}
    
    golden_parsed_output2 = {
        'evi': {
            1: {
                'bridge_domain': 'core1',
                'type': 'PBB',
                'unicast_label': '24001',
                'multicast_label': '24002',
                'flow_label': 'N',
                'table-policy_name': 'forward_class_1',
                'forward-class': '1',
                'rd_config': 'none',
                'rd_auto': 'none',
                'rt_auto': 'none',
            },
        },
    }

    golden_output2 = {'execute.return_value': '''
        show evpn evi detail 
        Mon Aug 24 14:14:19.873 EDT

        EVI        Bridge Domain                Type   
        ---------- ---------------------------- -------
        1          core1                        PBB    
        Unicast Label  : 24001
        Multicast Label: 24002
        Flow Label: N
        Table-policy Name: forward_class_1
        Forward-class: 1
        RD Config: none
        RD Auto  : none
        RT Auto  : none
        Route Targets in Use           Type   
        ------------------------------ -------

        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowEvpnEviDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowEvpnEviDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)
    
    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowEvpnEviDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output2)

# ===================================================
#  Unit test for 'show evpn evi mac'
# ===================================================

class test_show_evpn_evi_mac(unittest.TestCase):

    '''Unit test for 'show evpn evi mac'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vpn_id': {
            65535: {
                'mac_address': {
                    '0000.0000.0000': {
                        'encap': 'N/A',
                        'ip_address': '::',
                        'next_hop': 'Local',
                        'label': 0,
                    },
                },
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        show evpn evi mac
        Tue Sep 17 20:04:11.302 UTC

        VPN-ID     Encap  MAC address    IP address                               Nexthop                                 Label 
        ---------- ------ -------------- ---------------------------------------- --------------------------------------- --------
        65535      N/A    0000.0000.0000 ::                                       Local                                   0     

        '''}
    
    golden_parsed_output2 = {
        'vpn_id': {
            65535: {
                'mac_address': {
                    '0000.0000.0000': {
                        'encap': 'N/A',
                        'ip_address': '::',
                        'next_hop': 'Local',
                        'label': 0,
                    },
                },
            },
        },
    }

    golden_output2 = {'execute.return_value': '''
        show evpn evi vpn-id 65535 mac
        Tue Sep 17 20:04:11.302 UTC

        VPN-ID     Encap  MAC address    IP address                               Nexthop                                 Label 
        ---------- ------ -------------- ---------------------------------------- --------------------------------------- --------
        65535      N/A    0000.0000.0000 ::                                       Local                                   0     

        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowEvpnEviMac(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowEvpnEviMac(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)
    
    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowEvpnEviMac(device=self.device)
        parsed_output = obj.parse(vpn_id='65535')
        self.assertEqual(parsed_output,self.golden_parsed_output2)

# ===================================================
#  Unit test for 'show evpn evi mac private'
# ===================================================

class test_show_evpn_evi_mac_private(unittest.TestCase):

    '''Unit test for 'show evpn evi mac private'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vpn_id': {
            65535: {
                'mac_address': {
                    '0000.0000.0000': {
                        'encap': 'N/A',
                        'ip_address': '::',
                        'next_hop': 'Local',
                        'label': 0,
                        'ethernet_tag': 0,
                        'multipaths_resolved': 'False',
                        'multipaths_internal_label': 0,
                        'local_static': 'No',
                        'remote_static': 'No',
                        'local_ethernet_segment': '0000.0000.0000.0000.0000',
                        'remote_ethernet_segment': '0000.0000.0000.0000.0000',
                        'local_sequence_number': 0,
                        'remote_sequence_number': 0,
                        'local_encapsulation': 'N/A',
                        'remote_encapsulation': 'N/A',
                        'esi_port_key': '0',
                        'source': 'Local',
                        'flush_requested': 0,
                        'flush_received': 0,
                        'soo_nexthop': '::',
                        'bp_xcid': '0xffffffff',
                        'mac_state': 'Init',
                        'mac_producers': '0x0 (Best: 0x0)',
                        'local_router_mac': '0000.0000.0000',
                        'l3_label': 0,
                        'object': {
                            'EVPN MAC': {
                                'base_info': {
                                    'version': '0xdbdb0008',
                                    'flags': '0x4000',
                                    'type': 8,
                                    'reserved': 0,
                                },
                                'num_events': 0,
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output1 = {'execute.return_value': '''
        show evpn evi mac private
        Tue Sep 17 20:08:26.843 UTC

        VPN-ID     Encap  MAC address    IP address                               Nexthop                                 Label 
        ---------- ------ -------------- ---------------------------------------- --------------------------------------- --------
        65535      N/A    0000.0000.0000 ::                                       Local                                   0     
        Ethernet Tag                            : 0
        Multi-paths Resolved                    : False
        Multi-paths Internal label              : 0
        Local Static                            : No
        Remote Static                           : No
        Local Ethernet Segment                  : 0000.0000.0000.0000.0000
        Remote Ethernet Segment                 : 0000.0000.0000.0000.0000
        Local Sequence Number                   : 0
        Remote Sequence Number                  : 0
        Local Encapsulation                     : N/A
        Remote Encapsulation                    : N/A
        ESI Port Key                            : 0
        Source                                  : Local
        Flush Requested                         : 0
        Flush Received                          : 0
        SOO Nexthop                             : ::
        BP XCID                                 : 0xffffffff
        MAC State                               : Init
        MAC Producers                           : 0x0 (Best: 0x0)
        Local Router MAC                        : 0000.0000.0000
        L3 Label                                : 0

        Object: EVPN MAC
        Base info: version=0xdbdb0008, flags=0x4000, type=8, reserved=0
        EVPN MAC event history  [Num events: 0]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags
            ====                =====                         =====      =====
        ---------------------------------------------------------------------------- 

        '''}
    
    golden_parsed_output2 = {
        'vpn_id': {
            7: {
                'mac_address': {
                    '001b.01ff.0001': {
                        'next_hop': 'N/A',
                        'label': 24014,
                        'ip_address': '10.196.7.8',
                        'ethernet_segment': '0000.0000.0000.0000.0000',
                        'source': 'Local',
                        'flush_count': 0,
                        'bp_ifh': '0',
                        'flush_seq_id': 0,
                        'static': 'No',
                        'object': {
                            'EVPN MAC': {
                                'base_info': {
                                    'version': '0xdbdb0008',
                                    'flags': '0x204100',
                                    'type': 2113792,
                                    'reserved': 0,
                                },
                                'num_events': 12,
                                'event_history': {
                                    1: {
                                        'time': 'Jun 14 14:02:12.864',
                                        'event': 'Create',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    2: {
                                        'time': 'Jun 14 14:02:12.864',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '00000003',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    3: {
                                        'time': 'Jun 14 14:07:33.376',
                                        'event': 'Redundant path buffer',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    4: {
                                        'time': 'Jun 14 14:07:33.376',
                                        'event': 'Modify',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    5: {
                                        'time': 'Jun 14 14:07:33.376',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '00000003',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    6: {
                                        'time': 'Jun 14 14:55:40.544',
                                        'event': 'Redundant path buffer',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    7: {
                                        'time': 'Jun 14 14:55:40.544',
                                        'event': 'Modify',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    8: {
                                        'time': 'Jun 14 14:55:40.544',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '00000003',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    9: {
                                        'time': 'Jun 14 15:00:53.888',
                                        'event': 'Redundant path buffer',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    10: {
                                        'time': 'Jun 14 15:00:53.888',
                                        'event': 'Modify',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    11: {
                                        'time': 'Jun 14 15:00:53.888',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '00000003',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    12: {
                                        'time': 'Jun 14 15:13:16.800',
                                        'event': 'Advertise to BGP',
                                        'flag_1': '00004110',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output2 = {'execute.return_value': '''
        sh evpn evi mac private
        Tue Jun 14 15:14:25.359 UTC
        
        MAC address    Nexthop                                 Label    vpn-id 
        -------------- --------------------------------------- -------- --------
        001b.01ff.0001 N/A                                     24014    7      
        IP Address   : 10.196.7.8
        Ether.Segment: 0000.0000.0000.0000.0000
        ESI port key : 0x0000
        Source       : Local
        Multi-paths resolved: FALSE
        Multi-paths local label: 0        
        Flush Count  : 0
        BP IFH: 0
        Flush Seq ID : 0
        Static: No
        
        Object: EVPN MAC
        Base info: version=0xdbdb0008, flags=0x204100, type=2113792, reserved=0
        EVPN MAC event history  [Num events: 12]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags     
            ====                =====                         =====      =====     
            Jun 14 14:02:12.864 Create                        00000000, 00000000 -  -
            Jun 14 14:02:12.864 MAC advertise rejected        00000003, 00000000 -  -
            Jun 14 14:07:33.376 Redundant path buffer         00000000, 00000000 -  -
            Jun 14 14:07:33.376 Modify                        00000000, 00000000 -  -
            Jun 14 14:07:33.376 MAC advertise rejected        00000003, 00000000 -  -
            Jun 14 14:55:40.544 Redundant path buffer         00000000, 00000000 -  -
            Jun 14 14:55:40.544 Modify                        00000000, 00000000 -  -
            Jun 14 14:55:40.544 MAC advertise rejected        00000003, 00000000 -  -
            Jun 14 15:00:53.888 Redundant path buffer         00000000, 00000000 -  -
            Jun 14 15:00:53.888 Modify                        00000000, 00000000 -  -
            Jun 14 15:00:53.888 MAC advertise rejected        00000003, 00000000 -  -
            Jun 14 15:13:16.800 Advertise to BGP              00004110, 00000000 -  -
        ----------------------------------------------------------------------------

        '''}
    
    golden_parsed_output3 = {
        'vpn_id': {
            19: {
                'mac_address': {
                    '0000.00ff.0019': {
                        'ip_address': '::',
                        'next_hop': 'BVI19',
                        'label': 114012,
                        'ethernet_tag': 0,
                        'multipaths_resolved': 'False',
                        'static': 'Yes',
                        'local_ethernet_segment': '0000.0000.0000.0000.0000',
                        'remote_ethernet_segment': '0000.0000.0000.0000.0000',
                        'local_sequence_number': 0,
                        'remote_sequence_number': 0,
                        'local_encapsulation': 'N/A',
                        'remote_encapsulation': 'N/A',
                        'esi_port_key': '0',
                        'source': 'Local',
                        'flush_requested': 0,
                        'flush_received': 0,
                        'multipaths_local_label': 0,
                        'soo_nexthop': '::',
                        'bp_xcid': '0x800001a1',
                        'mac_state': 'Static',
                        'local_router_mac': '0000.0000.0000',
                        'l3_label': 0,
                        'object': {
                            'EVPN MAC': {
                                'base_info': {
                                    'version': '0xdbdb0008',
                                    'flags': '0x40024100',
                                    'type': 8,
                                    'reserved': 0,
                                },
                                'num_events': 16,
                                'event_history': {
                                    1: {
                                        'time': 'May  1 09:10:13.248',
                                        'event': 'Got L2RIB update',
                                        'flag_1': '40024000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    2: {
                                        'time': 'May  1 09:10:13.248',
                                        'event': 'Modify Redundant',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    3: {
                                        'time': 'May  1 09:10:13.248',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '00000011',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    4: {
                                        'time': 'May  1 09:10:13.248',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000001',
                                        'flag_2': '00020002',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    5: {
                                        'time': 'May  8 14:32:40.192',
                                        'event': 'Got L2RIB update',
                                        'flag_1': '40024100',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    6: {
                                        'time': 'May  8 14:32:40.192',
                                        'event': 'Modify Redundant',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    7: {
                                        'time': 'May  8 14:32:40.192',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '00000011',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    8: {
                                        'time': 'May  8 14:32:40.192',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000001',
                                        'flag_2': '00020002',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    9: {
                                        'time': 'May 22 09:53:49.568',
                                        'event': 'Got L2RIB update',
                                        'flag_1': '40024100',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    10: {
                                        'time': 'May 22 09:53:49.568',
                                        'event': 'Modify Redundant',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    11: {
                                        'time': 'May 22 09:53:49.568',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '00000011',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    12: {
                                        'time': 'May 22 09:53:49.568',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000001',
                                        'flag_2': '00020002',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    13: {
                                        'time': 'May 25 18:08:39.936',
                                        'event': 'Got L2RIB update',
                                        'flag_1': '40024100',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    14: {
                                        'time': 'May 25 18:08:39.936',
                                        'event': 'Modify Redundant',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    15: {
                                        'time': 'May 25 18:08:39.936',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '00000011',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    16: {
                                        'time': 'May 25 18:08:39.936',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000001',
                                        'flag_2': '00020002',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                },
                            },
                        },
                    },
                    '0009.0fff.0916': {
                        'ip_address': '10.169.19.4',
                        'next_hop': 'Bundle-Ether1.19',
                        'label': 114012,
                        'ethernet_tag': 0,
                        'multipaths_resolved': 'False',
                        'static': 'No',
                        'local_ethernet_segment': '0000.01ff.acce.7700.cccc',
                        'remote_ethernet_segment': '0000.0000.0000.0000.0000',
                        'local_sequence_number': 0,
                        'remote_sequence_number': 0,
                        'local_encapsulation': 'N/A',
                        'remote_encapsulation': 'N/A',
                        'esi_port_key': 'bef5',
                        'source': 'Local',
                        'flush_requested': 0,
                        'flush_received': 0,
                        'multipaths_local_label': 0,
                        'soo_nexthop': '::',
                        'bp_xcid': '0xc0000002',
                        'mac_state': 'Local',
                        'local_router_mac': '0000.0000.0000',
                        'l3_label': 0,
                        'object': {
                            'EVPN MAC': {
                                'base_info': {
                                    'version': '0xdbdb0008',
                                    'flags': '0x8004100',
                                    'type': 8,
                                    'reserved': 0,
                                },
                                'num_events': 16,
                                'event_history': {
                                    17: {
                                        'time': 'Jul  2 16:06:33.728',
                                        'event': 'Advertise to BGP',
                                        'flag_1': '09206110',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    18: {
                                        'time': 'Jul  2 16:06:33.728',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000006',
                                        'flag_2': '00010006',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    19: {
                                        'time': 'Jul  2 16:06:33.728',
                                        'event': 'Encode NLRI',
                                        'flag_1': '09206110',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    20: {
                                        'time': 'Jul  2 16:06:33.728',
                                        'event': 'L2RIB Download',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    21: {
                                        'time': 'Jul  2 16:06:33.728',
                                        'event': 'Got BGP update',
                                        'flag_1': '01010001',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    22: {
                                        'time': 'Jul  2 16:06:33.728',
                                        'event': 'Modify',
                                        'flag_1': '00000019',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    23: {
                                        'time': 'Jul  2 16:06:33.728',
                                        'event': 'Advertise to BGP',
                                        'flag_1': '083c6110',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    24: {
                                        'time': 'Jul  2 16:06:33.728',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000003',
                                        'flag_2': '00060001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    25: {
                                        'time': 'Jul  2 16:06:33.728',
                                        'event': 'Encode NLRI',
                                        'flag_1': '08bc6110',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    26: {
                                        'time': 'Jul  2 16:06:33.728',
                                        'event': 'L2RIB Download',
                                        'flag_1': '00000000',
                                        'flag_2': '01000100',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    27: {
                                        'time': 'Jul 23 11:30:27.968',
                                        'event': 'Delete',
                                        'flag_1': '00000001',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    28: {
                                        'time': 'Jul 23 11:30:27.968',
                                        'event': 'Advertise to BGP',
                                        'flag_1': '09206110',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    29: {
                                        'time': 'Jul 23 11:30:27.968',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000006',
                                        'flag_2': '00010006',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    30: {
                                        'time': 'Jul 23 11:30:27.968',
                                        'event': 'Encode NLRI',
                                        'flag_1': '09206110',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    31: {
                                        'time': 'Jul 23 11:30:27.968',
                                        'event': 'L2RIB Download',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    32: {
                                        'time': 'Aug 21 09:09:20.512',
                                        'event': 'Ignore BGP update',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    33: {
                                        'time': 'Oct  5 19:36:44.800',
                                        'event': 'Got L2RIB update',
                                        'flag_1': '083c4110',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    34: {
                                        'time': 'Oct  5 19:36:44.800',
                                        'event': 'Modify Redundant',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    35: {
                                        'time': 'Oct  5 19:36:44.800',
                                        'event': 'Advertise to BGP',
                                        'flag_1': '083c4110',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    36: {
                                        'time': 'Oct  5 19:36:44.800',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000000',
                                        'flag_2': '00060006',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    37: {
                                        'time': 'Oct  5 19:36:44.800',
                                        'event': 'Encode NLRI',
                                        'flag_1': '083c4110',
                                        'flag_2': '00000061',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    38: {
                                        'time': 'Oct  5 23:25:46.880',
                                        'event': 'Delete',
                                        'flag_1': '00000001',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    39: {
                                        'time': 'Oct  5 23:25:46.880',
                                        'event': 'Advertise to BGP',
                                        'flag_1': '09204110',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    40: {
                                        'time': 'Oct  5 23:25:46.880',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000007',
                                        'flag_2': '00010006',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    41: {
                                        'time': 'Oct  5 23:25:46.880',
                                        'event': 'Got BGP update',
                                        'flag_1': '00000001',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    42: {
                                        'time': 'Oct  5 23:25:46.880',
                                        'event': 'Encode NLRI',
                                        'flag_1': '09204110',
                                        'flag_2': '00000061',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    43: {
                                        'time': 'Oct  5 23:25:46.880',
                                        'event': 'L2RIB Download',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    44: {
                                        'time': 'Oct  5 23:25:47.904',
                                        'event': 'Got L2RIB update',
                                        'flag_1': '08004100',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    45: {
                                        'time': 'Oct  5 23:25:47.904',
                                        'event': 'Modify Redundant',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    46: {
                                        'time': 'Oct  5 23:25:47.904',
                                        'event': 'Advertise to BGP',
                                        'flag_1': '08204110',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    47: {
                                        'time': 'Oct  5 23:25:47.904',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    48: {
                                        'time': 'Oct  5 23:25:47.904',
                                        'event': 'Encode NLRI',
                                        'flag_1': '08204110',
                                        'flag_2': '00000061',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            1994: {
                'mac_address': {
                    '78ba.f9ff.106d': {
                        'ip_address': '::',
                        'next_hop': 'BVI900',
                        'label': 114416,
                        'ethernet_tag': 0,
                        'multipaths_resolved': 'False',
                        'static': 'Yes',
                        'local_ethernet_segment': '0000.0000.0000.0000.0000',
                        'remote_ethernet_segment': '0000.0000.0000.0000.0000',
                        'local_sequence_number': 0,
                        'remote_sequence_number': 0,
                        'local_encapsulation': 'N/A',
                        'remote_encapsulation': 'N/A',
                        'esi_port_key': '0',
                        'source': 'Local',
                        'flush_requested': 0,
                        'flush_received': 0,
                        'multipaths_local_label': 0,
                        'soo_nexthop': '::',
                        'bp_xcid': '0x800001a5',
                        'mac_state': 'Static',
                        'local_router_mac': '0000.0000.0000',
                        'l3_label': 0,
                        'object': {
                            'EVPN MAC': {
                                'base_info': {
                                    'version': '0xdbdb0008',
                                    'flags': '0x40024100',
                                    'type': 8,
                                    'reserved': 0,
                                },
                                'num_events': 16,
                                'event_history': {
                                    49: {
                                        'time': 'May  1 09:10:13.248',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '0000000b',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    50: {
                                        'time': 'May  1 09:10:13.248',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000001',
                                        'flag_2': '00020002',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    51: {
                                        'time': 'May  8 14:32:40.192',
                                        'event': 'Got L2RIB update',
                                        'flag_1': '40024100',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    52: {
                                        'time': 'May  8 14:32:40.192',
                                        'event': 'Modify Redundant',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    53: {
                                        'time': 'May  8 14:32:40.192',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '0000000b',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    54: {
                                        'time': 'May  8 14:32:40.192',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000001',
                                        'flag_2': '00020002',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    55: {
                                        'time': 'May 22 09:53:49.568',
                                        'event': 'Got L2RIB update',
                                        'flag_1': '40024100',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    56: {
                                        'time': 'May 22 09:53:49.568',
                                        'event': 'Modify Redundant',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    57: {
                                        'time': 'May 22 09:53:49.568',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '0000000b',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    58: {
                                        'time': 'May 22 09:53:49.568',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000001',
                                        'flag_2': '00020002',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    59: {
                                        'time': 'May 25 18:08:39.936',
                                        'event': 'Got L2RIB update',
                                        'flag_1': '40024100',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    60: {
                                        'time': 'May 25 18:08:39.936',
                                        'event': 'Modify Redundant',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    61: {
                                        'time': 'May 25 18:08:39.936',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '0000000b',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    62: {
                                        'time': 'May 25 18:08:39.936',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000001',
                                        'flag_2': '00020002',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    63: {
                                        'time': 'May 25 18:09:23.456',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '00000011',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    64: {
                                        'time': 'Jun 12 12:01:15.776',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '0000000b',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            2112: {
                'mac_address': {
                    '0000.25ff.e485': {
                        'ip_address': '::',
                        'next_hop': '10.154.219.101',
                        'label': 100965,
                        'ethernet_tag': 0,
                        'multipaths_resolved': 'False',
                        'static': 'No',
                        'local_ethernet_segment': '0000.0000.0000.0000.0000',
                        'remote_ethernet_segment': '0000.0000.0000.0000.0000',
                        'local_sequence_number': 0,
                        'remote_sequence_number': 0,
                        'local_encapsulation': 'N/A',
                        'remote_encapsulation': 'MPLS',
                        'esi_port_key': '0',
                        'source': 'Remote',
                        'flush_requested': 0,
                        'flush_received': 0,
                        'multipaths_local_label': 0,
                        'soo_nexthop': '10.154.219.101',
                        'bp_xcid': '0x0',
                        'mac_state': 'Remote (w/ SOO)',
                        'local_router_mac': '0000.0000.0000',
                        'l3_label': 0,
                        'object': {
                            'EVPN MAC': {
                                'base_info': {
                                    'version': '0xdbdb0008',
                                    'flags': '0xc0100',
                                    'type': 8,
                                    'reserved': 0,
                                },
                                'num_events': 9,
                                'event_history': {
                                    65: {
                                        'time': 'Oct  5 19:36:45.824',
                                        'event': 'Create',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    66: {
                                        'time': 'Oct  5 19:36:45.824',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '00000007',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    67: {
                                        'time': 'Oct  5 19:36:45.824',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000003',
                                        'flag_2': '00040000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    68: {
                                        'time': 'Oct  5 19:36:45.824',
                                        'event': 'L2RIB Download',
                                        'flag_1': '00018a65',
                                        'flag_2': '01000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    69: {
                                        'time': 'Oct  5 19:36:45.824',
                                        'event': 'Got BGP update',
                                        'flag_1': '00010000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    70: {
                                        'time': 'Oct  5 19:36:45.824',
                                        'event': 'Modify',
                                        'flag_1': '00000040',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    71: {
                                        'time': 'Oct  5 19:36:45.824',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '00000007',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    72: {
                                        'time': 'Oct  5 19:36:45.824',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000003',
                                        'flag_2': '00040004',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    73: {
                                        'time': 'Oct  5 19:36:45.824',
                                        'event': 'L2RIB Download',
                                        'flag_1': '00018a65',
                                        'flag_2': '01000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                },
                            },
                        },
                    },
                    '0000.25ff.c4da': {
                        'ip_address': '::',
                        'next_hop': '10.154.219.150',
                        'label': 114483,
                        'ethernet_tag': 0,
                        'multipaths_resolved': 'False',
                        'static': 'No',
                        'local_ethernet_segment': '0000.0000.0000.0000.0000',
                        'remote_ethernet_segment': '0000.0000.0000.0000.0000',
                        'local_sequence_number': 0,
                        'remote_sequence_number': 0,
                        'local_encapsulation': 'N/A',
                        'remote_encapsulation': 'MPLS',
                        'esi_port_key': '0',
                        'source': 'Remote',
                        'flush_requested': 0,
                        'flush_received': 0,
                        'multipaths_local_label': 0,
                        'soo_nexthop': '10.154.219.150',
                        'bp_xcid': '0x0',
                        'mac_state': 'Remote (w/ SOO)',
                        'local_router_mac': '0000.0000.0000',
                        'l3_label': 0,
                        'object': {
                            'EVPN MAC': {
                                'base_info': {
                                    'version': '0xdbdb0008',
                                    'flags': '0xc0000',
                                    'type': 8,
                                    'reserved': 0,
                                },
                                'num_events': 4,
                                'event_history': {
                                    74: {
                                        'time': 'Oct  5 19:36:45.824',
                                        'event': 'Create',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    75: {
                                        'time': 'Oct  5 19:36:45.824',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '00000007',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    76: {
                                        'time': 'Oct  5 19:36:45.824',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000003',
                                        'flag_2': '00040000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    77: {
                                        'time': 'Oct  5 19:36:45.824',
                                        'event': 'L2RIB Download',
                                        'flag_1': '0001bf33',
                                        'flag_2': '01000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                },
                            },
                        },
                    },
                    '4c96.14ff.df15': {
                        'ip_address': '::',
                        'next_hop': '10.154.219.101',
                        'label': 100965,
                        'ethernet_tag': 0,
                        'multipaths_resolved': 'True',
                        'static': 'No',
                        'local_ethernet_segment': '0000.0000.0000.0000.0000',
                        'remote_ethernet_segment': '0100.23ff.a315.5080.1600',
                        'local_sequence_number': 0,
                        'remote_sequence_number': 0,
                        'local_encapsulation': 'N/A',
                        'remote_encapsulation': 'MPLS',
                        'esi_port_key': '0',
                        'source': 'Remote',
                        'flush_requested': 0,
                        'flush_received': 0,
                        'multipaths_local_label': 100490,
                        'soo_nexthop': '10.154.219.101',
                        'bp_xcid': '0x0',
                        'mac_state': 'Remote (w/ SOO)',
                        'local_router_mac': '0000.0000.0000',
                        'l3_label': 0,
                        'object': {
                            'EVPN MAC': {
                                'base_info': {
                                    'version': '0xdbdb0008',
                                    'flags': '0xc0000',
                                    'type': 8,
                                    'reserved': 0,
                                },
                                'num_events': 4,
                                'event_history': {
                                    78: {
                                        'time': 'Sep 24 07:09:11.040',
                                        'event': 'Create',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    79: {
                                        'time': 'Sep 24 07:09:11.040',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '00000007',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    80: {
                                        'time': 'Sep 24 07:09:11.040',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000003',
                                        'flag_2': '00040000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    81: {
                                        'time': 'Sep 24 07:09:27.424',
                                        'event': 'L2RIB Download',
                                        'flag_1': '0001888a',
                                        'flag_2': '01010000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                },
                            },
                        },
                    },
                    '10.246.100.1': {
                        'encap': '4c96.14ff.df15',
                        'ip_address': '10.154.219.101',
                        'next_hop': '',
                        'label': 100965,
                        'ethernet_tag': 0,
                        'multipaths_resolved': 'True',
                        'static': 'No',
                        'local_ethernet_segment': '0000.0000.0000.0000.0000',
                        'remote_ethernet_segment': '0100.23ff.a315.5080.1600',
                        'local_sequence_number': 0,
                        'remote_sequence_number': 0,
                        'local_encapsulation': 'N/A',
                        'remote_encapsulation': 'MPLS',
                        'esi_port_key': '0',
                        'source': 'Remote',
                        'flush_requested': 0,
                        'flush_received': 0,
                        'multipaths_local_label': 100490,
                        'soo_nexthop': '10.154.219.101',
                        'bp_xcid': '0x0',
                        'mac_state': 'Remote (w/ SOO)',
                        'local_router_mac': '0000.0000.0000',
                        'l3_label': 0,
                        'object': {
                            'EVPN MAC': {
                                'base_info': {
                                    'version': '0xdbdb0008',
                                    'flags': '0xc0000',
                                    'type': 8,
                                    'reserved': 0,
                                },
                                'num_events': 4,
                                'event_history': {
                                    82: {
                                        'time': 'Sep 24 07:09:11.040',
                                        'event': 'Create',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    83: {
                                        'time': 'Sep 24 07:09:11.040',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '00000007',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    84: {
                                        'time': 'Sep 24 07:09:11.040',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000003',
                                        'flag_2': '00040000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    85: {
                                        'time': 'Sep 24 07:09:27.424',
                                        'event': 'L2RIB Download',
                                        'flag_1': '0001888a',
                                        'flag_2': '01010000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            65535: {
                'mac_address': {
                    '78ba.f9ff.106c': {
                        'ip_address': '::',
                        'next_hop': 'Local',
                        'label': 0,
                        'ethernet_tag': 0,
                        'multipaths_resolved': 'False',
                        'static': 'No',
                        'local_ethernet_segment': '0000.0000.0000.0000.0000',
                        'remote_ethernet_segment': '0000.0000.0000.0000.0000',
                        'local_sequence_number': 0,
                        'remote_sequence_number': 0,
                        'local_encapsulation': 'N/A',
                        'remote_encapsulation': 'N/A',
                        'esi_port_key': '0',
                        'source': 'Local',
                        'flush_requested': 0,
                        'flush_received': 0,
                        'multipaths_local_label': 0,
                        'soo_nexthop': '::',
                        'bp_xcid': '0x0',
                        'mac_state': 'Local',
                        'local_router_mac': '0000.0000.0000',
                        'l3_label': 0,
                        'object': {
                            'EVPN MAC': {
                                'base_info': {
                                    'version': '0xdbdb0008',
                                    'flags': '0x4100',
                                    'type': 8,
                                    'reserved': 0,
                                },
                                'num_events': 8,
                                'event_history': {
                                    86: {
                                        'time': 'May  1 09:00:02.944',
                                        'event': 'Create',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    87: {
                                        'time': 'May  1 09:00:02.944',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    88: {
                                        'time': 'May  1 09:00:02.944',
                                        'event': 'FSM Event (event, state)',
                                        'flag_1': '00000000',
                                        'flag_2': '00010000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    89: {
                                        'time': 'May  1 09:00:02.944',
                                        'event': 'Modify Redundant',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    90: {
                                        'time': 'May  1 09:02:05.312',
                                        'event': 'Replay EVI to BGP',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    91: {
                                        'time': 'May  1 09:02:05.312',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    92: {
                                        'time': 'May  1 09:05:20.896',
                                        'event': 'Replay EVI to BGP',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    93: {
                                        'time': 'May  1 09:05:20.896',
                                        'event': 'MAC advertise rejected',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output3 = {'execute.return_value': '''
        +++ genie-Router: executing command 'show evpn evi mac private' +++
        show evpn evi mac private

        Mon Oct 14 17:57:12.677 EDT

        EVI        MAC address    IP address                               Nexthop                                 Label   
        ---------- -------------- ---------------------------------------- --------------------------------------- --------
        19         0000.00ff.0019 ::                                       BVI19                                   114012  
        Ethernet Tag                            : 0
        Multi-paths Resolved                    : False
        Static                                  : Yes
        Local Ethernet Segment                  : 0000.0000.0000.0000.0000
        Remote Ethernet Segment                 : 0000.0000.0000.0000.0000
        Local Sequence Number                   : 0
        Remote Sequence Number                  : 0
        Local Encapsulation                     : N/A
        Remote Encapsulation                    : N/A
        ESI Port Key                            : 0
        Source                                  : Local
        Flush Requested                         : 0
        Flush Received                          : 0
        Multi-paths Local Label                 : 0
        SOO Nexthop                             : ::
        BP XCID                                 : 0x800001a1
        MAC State                               : Static
        Local Router MAC                        : 0000.0000.0000
        L3 Label                                : 0

        Object: EVPN MAC
        Base info: version=0xdbdb0008, flags=0x40024100, type=8, reserved=0
        EVPN MAC event history  [Num events: 16]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            May  1 09:10:13.248 Got L2RIB update              40024000, 00000000 -  - 
            May  1 09:10:13.248 Modify Redundant              00000000, 00000000 -  - 
            May  1 09:10:13.248 MAC advertise rejected        00000011, 00000000 -  - 
            May  1 09:10:13.248 FSM Event (event, state)      00000001, 00020002 -  - 
            May  8 14:32:40.192 Got L2RIB update              40024100, 00000000 -  - 
            May  8 14:32:40.192 Modify Redundant              00000000, 00000000 -  - 
            May  8 14:32:40.192 MAC advertise rejected        00000011, 00000000 -  - 
            May  8 14:32:40.192 FSM Event (event, state)      00000001, 00020002 -  - 
            May 22 09:53:49.568 Got L2RIB update              40024100, 00000000 -  - 
            May 22 09:53:49.568 Modify Redundant              00000000, 00000000 -  - 
            May 22 09:53:49.568 MAC advertise rejected        00000011, 00000000 -  - 
            May 22 09:53:49.568 FSM Event (event, state)      00000001, 00020002 -  - 
            May 25 18:08:39.936 Got L2RIB update              40024100, 00000000 -  - 
            May 25 18:08:39.936 Modify Redundant              00000000, 00000000 -  - 
            May 25 18:08:39.936 MAC advertise rejected        00000011, 00000000 -  - 
            May 25 18:08:39.936 FSM Event (event, state)      00000001, 00020002 -  - 
        ----------------------------------------------------------------------------
        19         0009.0fff.0916 ::                                       Bundle-Ether1.19                        114012  
        Ethernet Tag                            : 0
        Multi-paths Resolved                    : False
        Static                                  : No
        Local Ethernet Segment                  : 0000.01ff.acce.7700.cccc
        Remote Ethernet Segment                 : 0000.0000.0000.0000.0000
        Local Sequence Number                   : 7
        Remote Sequence Number                  : 0
        Local Encapsulation                     : N/A
        Remote Encapsulation                    : N/A
        ESI Port Key                            : bef5
        Source                                  : Local
        Flush Requested                         : 0
        Flush Received                          : 0
        Multi-paths Local Label                 : 0
        SOO Nexthop                             : ::
        BP XCID                                 : 0xc0000002
        MAC State                               : Local
        Local Router MAC                        : 0000.0000.0000
        L3 Label                                : 0

        Object: EVPN MAC
        Base info: version=0xdbdb0008, flags=0x8004100, type=8, reserved=0
        EVPN MAC event history  [Num events: 16]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Jul  2 16:06:33.728 Advertise to BGP              09206110, 00000000 -  - 
            Jul  2 16:06:33.728 FSM Event (event, state)      00000006, 00010006 -  - 
            Jul  2 16:06:33.728 Encode NLRI                   09206110, 00000000 M  - 
            Jul  2 16:06:33.728 L2RIB Download                00000000, 00000000 -  - 
            Jul  2 16:06:33.728 Got BGP update                01010001, 00000001 -  - 
            Jul  2 16:06:33.728 Modify                        00000019, 00000000 -  - 
            Jul  2 16:06:33.728 Advertise to BGP              083c6110, 00000000 -  - 
            Jul  2 16:06:33.728 FSM Event (event, state)      00000003, 00060001 -  - 
            Jul  2 16:06:33.728 Encode NLRI                   08bc6110, 00000000 M  - 
            Jul  2 16:06:33.728 L2RIB Download                00000000, 01000100 -  - 
            Jul 23 11:30:27.968 Delete                        00000001, 00000000 -  - 
            Jul 23 11:30:27.968 Advertise to BGP              09206110, 00000000 -  - 
            Jul 23 11:30:27.968 FSM Event (event, state)      00000006, 00010006 -  - 
            Jul 23 11:30:27.968 Encode NLRI                   09206110, 00000000 M  - 
            Jul 23 11:30:27.968 L2RIB Download                00000000, 00000000 -  - 
            Aug 21 09:09:20.512 Ignore BGP update             00000000, 00000000 M  - 
        ----------------------------------------------------------------------------
        19         0009.0fff.0916 10.169.19.4                               Bundle-Ether1.19                        114012  
        Ethernet Tag                            : 0
        Multi-paths Resolved                    : False
        Static                                  : No
        Local Ethernet Segment                  : 0000.01ff.acce.7700.cccc
        Remote Ethernet Segment                 : 0000.0000.0000.0000.0000
        Local Sequence Number                   : 0
        Remote Sequence Number                  : 0
        Local Encapsulation                     : N/A
        Remote Encapsulation                    : N/A
        ESI Port Key                            : bef5
        Source                                  : Local
        Flush Requested                         : 0
        Flush Received                          : 0
        Multi-paths Local Label                 : 0
        SOO Nexthop                             : ::
        BP XCID                                 : 0xc0000002
        MAC State                               : Local
        Local Router MAC                        : 0000.0000.0000
        L3 Label                                : 0

        Object: EVPN MAC
        Base info: version=0xdbdb0008, flags=0x8004100, type=8, reserved=0
        EVPN MAC event history  [Num events: 16]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Oct  5 19:36:44.800 Got L2RIB update              083c4110, 00000000 -  - 
            Oct  5 19:36:44.800 Modify Redundant              00000000, 00000000 -  - 
            Oct  5 19:36:44.800 Advertise to BGP              083c4110, 00000000 -  - 
            Oct  5 19:36:44.800 FSM Event (event, state)      00000000, 00060006 -  - 
            Oct  5 19:36:44.800 Encode NLRI                   083c4110, 00000061 M  - 
            Oct  5 23:25:46.880 Delete                        00000001, 00000000 -  - 
            Oct  5 23:25:46.880 Advertise to BGP              09204110, 00000000 -  - 
            Oct  5 23:25:46.880 FSM Event (event, state)      00000007, 00010006 -  - 
            Oct  5 23:25:46.880 Got BGP update                00000001, 00000000 -  - 
            Oct  5 23:25:46.880 Encode NLRI                   09204110, 00000061 M  - 
            Oct  5 23:25:46.880 L2RIB Download                00000000, 00000000 -  - 
            Oct  5 23:25:47.904 Got L2RIB update              08004100, 00000000 -  - 
            Oct  5 23:25:47.904 Modify Redundant              00000000, 00000000 -  - 
            Oct  5 23:25:47.904 Advertise to BGP              08204110, 00000000 -  - 
            Oct  5 23:25:47.904 FSM Event (event, state)      00000000, 00010001 -  - 
            Oct  5 23:25:47.904 Encode NLRI                   08204110, 00000061 M  - 
        ----------------------------------------------------------------------------
        1994       78ba.f9ff.106d ::                                       BVI900                                  114416  
        Ethernet Tag                            : 0
        Multi-paths Resolved                    : False
        Static                                  : Yes
        Local Ethernet Segment                  : 0000.0000.0000.0000.0000
        Remote Ethernet Segment                 : 0000.0000.0000.0000.0000
        Local Sequence Number                   : 0
        Remote Sequence Number                  : 0
        Local Encapsulation                     : N/A
        Remote Encapsulation                    : N/A
        ESI Port Key                            : 0
        Source                                  : Local
        Flush Requested                         : 0
        Flush Received                          : 0
        Multi-paths Local Label                 : 0
        SOO Nexthop                             : ::
        BP XCID                                 : 0x800001a5
        MAC State                               : Static
        Local Router MAC                        : 0000.0000.0000
        L3 Label                                : 0

        Object: EVPN MAC
        Base info: version=0xdbdb0008, flags=0x40024100, type=8, reserved=0
        EVPN MAC event history  [Num events: 16]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            May  1 09:10:13.248 MAC advertise rejected        0000000b, 00000000 -  - 
            May  1 09:10:13.248 FSM Event (event, state)      00000001, 00020002 -  - 
            May  8 14:32:40.192 Got L2RIB update              40024100, 00000000 -  - 
            May  8 14:32:40.192 Modify Redundant              00000000, 00000000 -  - 
            May  8 14:32:40.192 MAC advertise rejected        0000000b, 00000000 -  - 
            May  8 14:32:40.192 FSM Event (event, state)      00000001, 00020002 -  - 
            May 22 09:53:49.568 Got L2RIB update              40024100, 00000000 -  - 
            May 22 09:53:49.568 Modify Redundant              00000000, 00000000 -  - 
            May 22 09:53:49.568 MAC advertise rejected        0000000b, 00000000 -  - 
            May 22 09:53:49.568 FSM Event (event, state)      00000001, 00020002 -  - 
            May 25 18:08:39.936 Got L2RIB update              40024100, 00000000 -  - 
            May 25 18:08:39.936 Modify Redundant              00000000, 00000000 -  - 
            May 25 18:08:39.936 MAC advertise rejected        0000000b, 00000000 -  - 
            May 25 18:08:39.936 FSM Event (event, state)      00000001, 00020002 -  - 
            May 25 18:09:23.456 MAC advertise rejected        00000011, 00000000 -  - 
            Jun 12 12:01:15.776 MAC advertise rejected        0000000b, 00000000 -  - 
        ----------------------------------------------------------------------------
        2112       0000.25ff.e485 ::                                       10.154.219.101                           100965  
        Ethernet Tag                            : 0
        Multi-paths Resolved                    : False
        Static                                  : No
        Local Ethernet Segment                  : 0000.0000.0000.0000.0000
        Remote Ethernet Segment                 : 0000.0000.0000.0000.0000
        Local Sequence Number                   : 0
        Remote Sequence Number                  : 0
        Local Encapsulation                     : N/A
        Remote Encapsulation                    : MPLS
        ESI Port Key                            : 0
        Source                                  : Remote
        Flush Requested                         : 0
        Flush Received                          : 0
        Multi-paths Local Label                 : 0
        SOO Nexthop                             : 10.154.219.101
        BP XCID                                 : 0x0
        MAC State                               : Remote (w/ SOO)
        Local Router MAC                        : 0000.0000.0000
        L3 Label                                : 0

        Object: EVPN MAC
        Base info: version=0xdbdb0008, flags=0xc0100, type=8, reserved=0
        EVPN MAC event history  [Num events: 9]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Oct  5 19:36:45.824 Create                        00000000, 00000000 -  - 
            Oct  5 19:36:45.824 MAC advertise rejected        00000007, 00000000 -  - 
            Oct  5 19:36:45.824 FSM Event (event, state)      00000003, 00040000 -  - 
            Oct  5 19:36:45.824 L2RIB Download                00018a65, 01000000 -  - 
            Oct  5 19:36:45.824 Got BGP update                00010000, 00000001 -  - 
            Oct  5 19:36:45.824 Modify                        00000040, 00000000 -  - 
            Oct  5 19:36:45.824 MAC advertise rejected        00000007, 00000000 -  - 
            Oct  5 19:36:45.824 FSM Event (event, state)      00000003, 00040004 -  - 
            Oct  5 19:36:45.824 L2RIB Download                00018a65, 01000000 -  - 
        ----------------------------------------------------------------------------
        2112       0000.25ff.c4da ::                                       10.154.219.150                           114483  
        Ethernet Tag                            : 0
        Multi-paths Resolved                    : False
        Static                                  : No
        Local Ethernet Segment                  : 0000.0000.0000.0000.0000
        Remote Ethernet Segment                 : 0000.0000.0000.0000.0000
        Local Sequence Number                   : 0
        Remote Sequence Number                  : 0
        Local Encapsulation                     : N/A
        Remote Encapsulation                    : MPLS
        ESI Port Key                            : 0
        Source                                  : Remote
        Flush Requested                         : 0
        Flush Received                          : 0
        Multi-paths Local Label                 : 0
        SOO Nexthop                             : 10.154.219.150
        BP XCID                                 : 0x0
        MAC State                               : Remote (w/ SOO)
        Local Router MAC                        : 0000.0000.0000
        L3 Label                                : 0

        Object: EVPN MAC
        Base info: version=0xdbdb0008, flags=0xc0000, type=8, reserved=0
        EVPN MAC event history  [Num events: 4]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Oct  5 19:36:45.824 Create                        00000000, 00000000 -  - 
            Oct  5 19:36:45.824 MAC advertise rejected        00000007, 00000000 -  - 
            Oct  5 19:36:45.824 FSM Event (event, state)      00000003, 00040000 -  - 
            Oct  5 19:36:45.824 L2RIB Download                0001bf33, 01000000 -  - 
        ----------------------------------------------------------------------------
        2112       4c96.14ff.df15 ::                                       10.154.219.101                           100965  
        Ethernet Tag                            : 0
        Multi-paths Resolved                    : True
        Static                                  : No
        Local Ethernet Segment                  : 0000.0000.0000.0000.0000
        Remote Ethernet Segment                 : 0100.23ff.a315.5080.1600
        Local Sequence Number                   : 0
        Remote Sequence Number                  : 0
        Local Encapsulation                     : N/A
        Remote Encapsulation                    : MPLS
        ESI Port Key                            : 0
        Source                                  : Remote
        Flush Requested                         : 0
        Flush Received                          : 0
        Multi-paths Local Label                 : 100490
        SOO Nexthop                             : 10.154.219.101
        BP XCID                                 : 0x0
        MAC State                               : Remote (w/ SOO)
        Local Router MAC                        : 0000.0000.0000
        L3 Label                                : 0

        Object: EVPN MAC
        Base info: version=0xdbdb0008, flags=0xc0000, type=8, reserved=0
        EVPN MAC event history  [Num events: 4]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Sep 24 07:09:11.040 Create                        00000000, 00000000 -  - 
            Sep 24 07:09:11.040 MAC advertise rejected        00000007, 00000000 -  - 
            Sep 24 07:09:11.040 FSM Event (event, state)      00000003, 00040000 -  - 
            Sep 24 07:09:27.424 L2RIB Download                0001888a, 01010000 -  - 
        ----------------------------------------------------------------------------
        2112       4c96.14ff.df15 10.246.100.1                             10.154.219.101                           100965  
        Ethernet Tag                            : 0
        Multi-paths Resolved                    : True
        Static                                  : No
        Local Ethernet Segment                  : 0000.0000.0000.0000.0000
        Remote Ethernet Segment                 : 0100.23ff.a315.5080.1600
        Local Sequence Number                   : 0
        Remote Sequence Number                  : 0
        Local Encapsulation                     : N/A
        Remote Encapsulation                    : MPLS
        ESI Port Key                            : 0
        Source                                  : Remote
        Flush Requested                         : 0
        Flush Received                          : 0
        Multi-paths Local Label                 : 100490
        SOO Nexthop                             : 10.154.219.101
        BP XCID                                 : 0x0
        MAC State                               : Remote (w/ SOO)
        Local Router MAC                        : 0000.0000.0000
        L3 Label                                : 0

        Object: EVPN MAC
        Base info: version=0xdbdb0008, flags=0xc0000, type=8, reserved=0
        EVPN MAC event history  [Num events: 4]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Sep 24 07:09:11.040 Create                        00000000, 00000000 -  - 
            Sep 24 07:09:11.040 MAC advertise rejected        00000007, 00000000 -  - 
            Sep 24 07:09:11.040 FSM Event (event, state)      00000003, 00040000 -  - 
            Sep 24 07:09:27.424 L2RIB Download                0001888a, 01010000 -  - 
        ----------------------------------------------------------------------------
        65535      78ba.f9ff.106c ::                                       Local                                   0       
        Ethernet Tag                            : 0
        Multi-paths Resolved                    : False
        Static                                  : No
        Local Ethernet Segment                  : 0000.0000.0000.0000.0000
        Remote Ethernet Segment                 : 0000.0000.0000.0000.0000
        Local Sequence Number                   : 0
        Remote Sequence Number                  : 0
        Local Encapsulation                     : N/A
        Remote Encapsulation                    : N/A
        ESI Port Key                            : 0
        Source                                  : Local
        Flush Requested                         : 0
        Flush Received                          : 0
        Multi-paths Local Label                 : 0
        SOO Nexthop                             : ::
        BP XCID                                 : 0x0
        MAC State                               : Local
        Local Router MAC                        : 0000.0000.0000
        L3 Label                                : 0

        Object: EVPN MAC
        Base info: version=0xdbdb0008, flags=0x4100, type=8, reserved=0
        EVPN MAC event history  [Num events: 8]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            May  1 09:00:02.944 Create                        00000000, 00000000 -  - 
            May  1 09:00:02.944 MAC advertise rejected        00000000, 00000000 -  - 
            May  1 09:00:02.944 FSM Event (event, state)      00000000, 00010000 -  - 
            May  1 09:00:02.944 Modify Redundant              00000000, 00000000 -  - 
            May  1 09:02:05.312 Replay EVI to BGP             00000000, 00000000 -  - 
            May  1 09:02:05.312 MAC advertise rejected        00000000, 00000000 -  - 
            May  1 09:05:20.896 Replay EVI to BGP             00000000, 00000000 -  - 
            May  1 09:05:20.896 MAC advertise rejected        00000000, 00000000 -  - 
        ----------------------------------------------------------------------------
        RP/0/RSP0/CPU0:genie-Router#

    '''}
    
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowEvpnEviMacPrivate(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowEvpnEviMacPrivate(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)
    
    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowEvpnEviMacPrivate(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output2)
    
    def test_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowEvpnEviMacPrivate(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output3)

# ================================================
#  Unit test for 'show evpn internal-label detail'
# ================================================
class TestShowEvpnInternalLabelDetail(unittest.TestCase):
    '''Unit test for 'show evpn internal-label detail'''

    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'evi':
            {5:
                {'esi': '0012.12ff.0000.0000.0002',
                'eth_tag': 0,
                'evi': 5,
                'label': 24114,
                'mp_resolved': True,
                'mp_info': 'Remote single-active',
                'pathlists':
                    {'ead_es':
                        {'nexthop':
                            {'10.10.10.10':
                                {'label': 0}}},
                    'ead_evi':
                        {'nexthop':
                            {'10.10.10.10':
                                {'label': 24012}}},
                    'mac':
                        {'nexthop':
                            {'10.70.20.20':
                                {'label': 24212},
                            '10.70.21.21':
                                {'label': 0}}},
                    'summary':
                        {'nexthop':
                            {'10.10.10.10':
                                {'df_role': 'B',
                                'label': 24012},
                            '10.70.20.20':
                                {'label': 24212}}}}},
            100:
                {'esi': '0100.00ff.acce.5500.0100',
                'eth_tag': 0,
                'evi': 100,
                'label': 24005}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:PE1#show evpn internal-label detail
        Wed Jul 13 13:55:17.592 EDT

        EVI   Ethernet Segment Id                     EtherTag Label   
        ----- --------------------------------------- -------- --------
        100   0100.00ff.acce.5500.0100                0        24005
        5     0012.12ff.0000.0000.0002                0        24114

              Multi-paths resolved: TRUE (Remote single-active)
              MAC     10.70.20.20                              24212
                      10.70.21.21                              0
              EAD/ES  10.10.10.10                              0
              EAD/EVI 10.10.10.10                              24012
              Summary 10.70.20.20                              24212
                      10.10.10.10 (B)                          24012
        '''}

    golden_parsed_output2 = {
        'evi': 
            {145: 
                {'esi': 'ff00.00ff.c025.ce01.0000',
                'eth_tag': 0,
                'evi': 145,
                'label': 24005,
                'pathlists':
                    {'summary':
                        {'nexthop':
                            {'192.168.0.3':
                                {'label': 524288}}}}}}}

    golden_output2 = {'execute.return_value': '''
        RP/0/0/CPU0:PE1#show evpn internal-label detail
        Thu May  5 10:16:51.447 EDT

        EVI   Ethernet Segment Id                     EtherTag Label   
        ----- --------------------------------------- -------- --------
        145   ff00.00ff.c025.ce01.0000                0        24005
              Summary 192.168.0.3                              524288

        '''}

    golden_parsed_output3 = {
        'vpn_id':
            {16001:
                {'encap': 'VXLAN',
                'esi': '0001.04ff.0b0c.0607.0811',
                'eth_tag': 0,
                'label': 24002,
                'mp_internal_label': 24002,
                'mp_resolved': True,
                'mp_info': 'Remote all-active',
                'pathlists': 
                    {'ead_es': 
                        {'nexthop': 
                            {'10.76.1.2': 
                                {'label': 0}}},
                    'summary': 
                        {'nexthop': 
                            {'10.76.1.2': 
                                {'label': 16001,
                                'value': '0x03000001'}}},
                    'ead_evi': 
                        {'nexthop': 
                            {'10.76.1.2': 
                                {'label': 16001}}}},
                'vpn_id': 16001},
            16002:
                {'encap': 'VXLAN',
                'esi': '0001.04ff.0b0c.0607.0811',
                'eth_tag': 0,
                'label': 24003,
                'mp_internal_label': 24003,
                'mp_resolved': True,
                'mp_info': 'Remote all-active',
                'pathlists': 
                    {'ead_es': 
                        {'nexthop': 
                            {'10.76.1.2': 
                                {'label': 0}}},
                    'summary': 
                        {'nexthop': 
                            {'10.76.1.2': 
                                {'label': 16002,
                                    'value': '0x03000001'}}},
                    'ead_evi': 
                        {'nexthop': 
                            {'10.76.1.2': 
                                {'label': 16002}}}},
                'vpn_id': 16002},
            16003: 
                {'encap': 'VXLAN',
                'esi': '0001.04ff.0b0c.0607.0811',
                'eth_tag': 0,
                'label': 24004,
                'mp_resolved': True,
                'mp_info': 'Remote all-active',
                'vpn_id': 16003}}}

    golden_output3 = {'execute.return_value': '''
        RP/0/RP0/CPU0:RGT-HVS-1#show evpn internal-label detail location 0/RP0/CPU0 
        Sat Jun  9 10:20:21.939 UTC

        VPN-ID     Encap  Ethernet Segment Id         EtherTag   Label   
        ---------- ------ --------------------------- --------   --------
        16001      VXLAN  0001.04ff.0b0c.0607.0811    0          24002   
           Multi-paths resolved: TRUE (Remote all-active) 
           Multi-paths Internal label: 24002
           Pathlists:
             EAD/ES     10.76.1.2                                0              
             EAD/EVI    10.76.1.2                                16001          
           Summary pathlist:
             0x03000001 10.76.1.2                                16001          

        16002      VXLAN  0001.04ff.0b0c.0607.0811    0          24003   
           Multi-paths resolved: TRUE (Remote all-active) 
           Multi-paths Internal label: 24003
           Pathlists:
             EAD/ES     10.76.1.2                                0              
             EAD/EVI    10.76.1.2                                16002          
           Summary pathlist:
             0x03000001 10.76.1.2                                16002          

        16003      VXLAN  0001.04ff.0b0c.0607.0811    0          24004   
           Multi-paths resolved: TRUE (Remote all-active) 
        '''}

    device_output = {'execute.return_value': '''
            VPN-ID     Encap  Ethernet Segment Id         EtherTag     Label   
        ---------- ------ --------------------------- ----------   --------
        1000       MPLS   0001.00ff.0102.0000.0011    0            100001  
           Multi-paths resolved: TRUE (Remote all-active) (ECMP Disable)
           Multi-paths Internal label: None
            MAC         172.16.2.89                              100001         
            EAD/ES      172.16.2.89                              0              
            EAD/EVI     172.16.2.89                              100001         
           Summary pathlist:
         0xffffffff (P) 172.16.2.89                              100001         
    '''}

    deivce_parsed_output = {
        'vpn_id': {
            1000: {
                'encap': 'MPLS',
                'esi': '0001.00ff.0102.0000.0011',
                'eth_tag': 0,
                'label': 100001,
                'mp_info': 'Remote all-active, ECMP Disable',
                'mp_resolved': True,
                'pathlists': {
                    'ead_es': {
                        'nexthop': {
                            '172.16.2.89': {
                                'label': 0,
                            },
                        },
                    },
                    'ead_evi': {
                        'nexthop': {
                            '172.16.2.89': {
                                'label': 100001,
                            },
                        },
                    },
                    'mac': {
                        'nexthop': {
                            '172.16.2.89': {
                                'label': 100001,
                            },
                        },
                    },
                    'summary': {
                        'nexthop': {
                            '172.16.2.89': {
                                'df_role': '(P)',
                                'label': 100001,
                                'value': '0xffffffff',
                            },
                        },
                    },
                },
                'vpn_id': 1000,
            },
        },
    }

    golden_output4 = {'execute.return_value': ''' 
        +++ genie-Device: executing command 'show evpn internal-label detail' +++
        show evpn internal-label detail

        Mon Oct 22 10:43:37.980 EDT

        VPN-ID     Encap  Ethernet Segment Id         EtherTag     Label   
        ---------- ------ --------------------------- ----------   --------
        1000       MPLS   0001.00ff.0102.0000.0011    0                    
        Multi-paths resolved: FALSE (Remote all-active) (ECMP Disable)
            Reason: No EAD/ES
        Multi-paths Internal label: None
            EAD/EVI     10.94.2.88                              100010         

        RP/0/RP0/CPU0:genie-Device#

    '''}

    deivce_parsed_output4 = {
        'vpn_id': {
            1000: {
                'vpn_id': 1000,
                'encap': 'MPLS',
                'esi': '0001.00ff.0102.0000.0011',
                'eth_tag': 0,
                'mp_resolved': True,
                'mp_info': 'Remote all-active, ECMP Disable',
                'pathlists': {
                    'ead_evi': {
                        'nexthop': {
                            '10.94.2.88': {
                                'label': 100010,
                            },
                        },
                    },
                },
            },
        },
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowEvpnInternalLabelDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowEvpnInternalLabelDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowEvpnInternalLabelDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_golden3(self):
        self.device = Mock(**self.golden_output3)
        obj = ShowEvpnInternalLabelDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test(self):
        self.device = Mock(**self.device_output)
        obj = ShowEvpnInternalLabelDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.deivce_parsed_output)
    
    def test_golden4(self):
        self.device = Mock(**self.golden_output4)
        obj = ShowEvpnInternalLabelDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.deivce_parsed_output4)

# ===================================================
#  Unit test for 'show evpn ethernet-segment'
# ===================================================

class test_show_evpn_ethernet_segment(unittest.TestCase):

    '''Unit test for 'show evpn ethernet-segment'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'segment_id': {
            '0012.12ff.0000.0000.0000': {
                'interface': {
                    'Nv101': {
                        'next_hops': ['10.10.10.10'],
                    },
                },
            },
            '0012.12ff.0001.0000.0001': {
                'interface': {
                    'PW:10.25.40.40,10001': {
                        'next_hops': ['10.10.10.10'],
                    },
                },
            },
            '0012.12ff.0001.0000.0002': {
                'interface': {
                    'Bundle-Ether1': {
                        'next_hops': ['10.10.10.10'],
                    },
                },
            },
            '0012.12ff.0001.0000.0003': {
                'interface': {
                    'VFI:ves-vfi-1': {
                        'next_hops': ['10.10.10.10'],
                    },
                },
            },
            '0012.12ff.0002.0000.0001': {
                'interface': {
                    'PW:10.25.40.40,10011': {
                        'next_hops': ['10.10.10.10'],
                    },
                },
            },
            '0012.12ff.0002.0000.0003': {
                'interface': {
                    'VFI:ves-vfi-2': {
                        'next_hops': ['10.10.10.10'],
                    },
                },
            },
            'N/A': {
                'interface': {
                    'PW:10.25.40.40,10007': {
                        'next_hops': ['10.10.10.10'],
                    },
                    'PW:10.25.40.40,10017': {
                        'next_hops': ['10.10.10.10'],
                    },
                },
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        show evpn ethernet-segment

        Ethernet Segment Id      Interface                          Nexthops
        ------------------------ ---------------------------------- --------------------
        0012.12ff.0000.0000.0000 nv101                              10.10.10.10
        0012.12ff.0001.0000.0001 PW:10.25.40.40,10001               10.10.10.10
        0012.12ff.0001.0000.0002 BE1                                10.10.10.10
        0012.12ff.0001.0000.0003 VFI:ves-vfi-1                      10.10.10.10
        0012.12ff.0002.0000.0001 PW:10.25.40.40,10011               10.10.10.10
        0012.12ff.0002.0000.0003 VFI:ves-vfi-2                      10.10.10.10
        N/A                      PW:10.25.40.40,10007               10.10.10.10
        N/A                      PW:10.25.40.40,10017               10.10.10.10
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowEvpnEthernetSegment(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowEvpnEthernetSegment(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)

# ===================================================
#  Unit test for 'show evpn ethernet-segment detail'
# ===================================================

class test_show_evpn_ethernet_segment_detail(unittest.TestCase):

    '''Unit test for 'show evpn ethernet-segment detail'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'segment_id': {
            '0210.03ff.9e00.0210.0000': {
                'interface': {
                    'GigabitEthernet0/3/0/0': {
                        'next_hops': ['10.1.100.100', '10.204.100.100'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'Ready',
                        'main_port': {
                            'interface': 'GigabitEthernet0/3/0/0',
                            'if_handle': '0x1800300',
                            'state': 'Up',
                            'redundancy': 'Not Defined',
                        },
                        'source_mac': '0001.edff.9e9f (PBB BSA)',
                        'topology': {
                            'operational': 'MHN',
                            'configured': 'A/A per service (default)',
                        },
                        'primary_services': 'Auto-selection',
                        'secondary_services': 'Auto-selection',
                        'service_carving_results': {
                            'bridge_ports': {
                                'num_of_total': 3,
                            },
                            'elected': {
                                'num_of_total': 0,
                            },
                            'not_elected': {
                                'num_of_total': 3,
                                'i_sid_ne': ['1450101', '1650205', '1850309'],
                            },
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '45 sec [not running]',
                        'recovery_timer': '20 sec [not running]',
                        'flush_again_timer': '60 sec',
                    },
                },
            },
            'be01.03ff.be01.ce00.0001': {
                'interface': {
                    'Bundle-Ether1': {
                        'next_hops': ['10.1.100.100', '10.204.100.100'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'Ready',
                        'main_port': {
                            'interface': 'Bundle-Ether1',
                            'if_handle': '0x000480',
                            'state': 'Up',
                            'redundancy': 'Active',
                        },
                        'source_mac': '0024.beff.cf01 (Local)',
                        'topology': {
                            'operational': 'MHN',
                            'configured': 'A/A per flow (default)',
                        },
                        'primary_services': 'Auto-selection',
                        'secondary_services': 'Auto-selection',
                        'service_carving_results': {
                            'bridge_ports': {
                                'num_of_total': 3,
                            },
                            'elected': {
                                'num_of_total': 3,
                                'i_sid_e': ['1450102', '1650206', '1850310'],
                            },
                            'not_elected': {
                                'num_of_total': 0,
                            },
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '45 sec [not running]',
                        'recovery_timer': '20 sec [not running]',
                        'flush_again_timer': '60 sec',
                    },
                },
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        Router#show evpn ethernet-segment detail
        Tue Jun 25 14:17:09.610 EDT
        Legend:
        A- PBB-EVPN load-balancing mode and Access Protection incompatible,
        B- no Bridge Ports PBB-EVPN enabled,
        C- Backbone Source MAC missing,
        E- ESI missing,
        H- Interface handle missing,
        I- Interface name missing,
        M- Interface in Down state,
        O- BGP End of Download missing,
        P- Interface already Access Protected,
        Pf-Interface forced single-homed,
        R- BGP RID not received,
        S- Interface in redundancy standby state,
        X- ESI-extracted MAC Conflict

        Ethernet Segment Id      Interface      Nexthops                                
        ------------------------ -------------- ----------------------------------------
        0210.03ff.9e00.0210.0000 Gi0/3/0/0      10.1.100.100                           
                                                10.204.100.100                           
        ES to BGP Gates   : Ready
        ES to L2FIB Gates : Ready
        Main port         :
            Interface name : GigabitEthernet0/3/0/0
            IfHandle       : 0x1800300
            State          : Up
            Redundancy     : Not Defined
        Source MAC        : 0001.edff.9e9f (PBB BSA)
        Topology          :
            Operational    : MHN
            Configured     : A/A per service (default)
        Primary Services  : Auto-selection
        Secondary Services: Auto-selection
        Service Carving Results:
            Bridge ports   : 3
            Elected        : 0
            Not Elected    : 3
                I-Sid NE  :  1450101, 1650205, 1850309
        MAC Flushing mode : STP-TCN
        Peering timer     : 45 sec [not running]
        Recovery timer    : 20 sec [not running]
        Flushagain timer  : 60 sec

        be01.03ff.be01.ce00.0001 BE1            10.1.100.100                           
                                                10.204.100.100                           
        ES to BGP Gates   : Ready
        ES to L2FIB Gates : Ready
        Main port         :
            Interface name : Bundle-Ether1
            IfHandle       : 0x000480
            State          : Up
            Redundancy     : Active
        Source MAC        : 0024.beff.cf01 (Local)
        Topology          :
            Operational    : MHN
            Configured     : A/A per flow (default)
        Primary Services  : Auto-selection
        Secondary Services: Auto-selection
        Service Carving Results:
            Bridge ports   : 3
            Elected        : 3
                I-Sid E   :  1450102, 1650206, 1850310
            Not Elected    : 0
        MAC Flushing mode : STP-TCN
        Peering timer     : 45 sec [not running]
        Recovery timer    : 20 sec [not running]
        Flushagain timer  : 60 sec
        '''}

    golden_parsed_output2 = {
        'segment_id': {
            '0001.00ff.aaab.00ff.0003': {
                'interface': {
                    'Bundle-Ether3': {
                        'next_hops': ['10.154.219.84'],
                        'es_to_bgp_gates': 'M',
                        'es_to_l2fib_gates': 'Ready',
                        'main_port': {
                            'interface': 'Bundle-Ether3',
                            'interface_mac': '00c1.64ff.a415',
                            'if_handle': '0x080002a0',
                            'state': 'Down',
                            'redundancy': 'Not Defined',
                        },
                        'esi': {
                            'type': '0',
                            'value': '01.0000.aaff.abab.0003',
                        },
                        'es_import_rt': 'aaab.00ff.0003 (Local)',
                        'source_mac': '0000.0000.0000 (N/A)',
                        'topology': {
                            'operational': 'SH',
                            'configured': 'All-active (AApF) (default)',
                        },
                        'service_carving': 'Auto-selection',
                        'peering_details': ['10.154.219.84[MOD:P:00]'],
                        'service_carving_results': {
                            'forwarders': 1,
                            'permanent': 0,
                            'elected': {
                                'num_of_total': 0,
                            },
                            'not_elected': {
                                'num_of_total': 1,
                            },
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '3 sec [not running]',
                        'recovery_timer': '30 sec [not running]',
                        'carving_timer': '0 sec [not running]',
                        'local_shg_label': '100564',
                        'remote_shg_labels': {
                            '0': {
                            },
                        },
                    },
                },
            },
            '0001.00ff.aaab.00ff.0004': {
                'interface': {
                    'Bundle-Ether4': {
                        'next_hops': ['10.154.219.84'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'Ready',
                        'main_port': {
                            'interface': 'Bundle-Ether4',
                            'interface_mac': '00c1.64ff.a414',
                            'if_handle': '0x080002e0',
                            'state': 'Up',
                            'redundancy': 'Not Defined',
                        },
                        'esi': {
                            'type': '0',
                            'value': '01.0000.aaff.abab.0004',
                        },
                        'es_import_rt': 'aaab.00ff.0004 (Local)',
                        'source_mac': '0000.0000.0000 (N/A)',
                        'topology': {
                            'operational': 'SH',
                            'configured': 'All-active (AApF) (default)',
                        },
                        'service_carving': 'Auto-selection',
                        'peering_details': ['10.154.219.84[MOD:P:00]'],
                        'service_carving_results': {
                            'forwarders': 1,
                            'permanent': 0,
                            'elected': {
                                'num_of_total': 1,
                            },
                            'not_elected': {
                                'num_of_total': 0,
                            },
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '3 sec [not running]',
                        'recovery_timer': '30 sec [not running]',
                        'carving_timer': '0 sec [not running]',
                        'local_shg_label': '100565',
                        'remote_shg_labels': {
                            '0': {
                            },
                        },
                    },
                },
            },
            'N/A': {
                'interface': {
                    'GigabitEthernet0/0/0/12': {
                        'next_hops': ['10.154.219.84'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'Ready',
                        'main_port': {
                            'interface': 'GigabitEthernet0/0/0/12',
                            'interface_mac': '00c1.64ff.7f67',
                            'if_handle': '0x000005c0',
                            'state': 'Up',
                            'redundancy': 'Not Defined',
                        },
                        'esi': {
                            'type': 'Invalid',
                        },
                        'es_import_rt': '0000.0000.0000 (Incomplete Configuration)',
                        'source_mac': '00c1.64ff.a411 (PBB BSA, no ESI)',
                        'topology': {
                            'operational': 'SH',
                            'configured': 'Single-active (AApS) (default)',
                        },
                        'service_carving': 'Auto-selection',
                        'peering_details': ['10.154.219.84[MOD:P:00]'],
                        'service_carving_results': {
                            'forwarders': 1,
                            'permanent': 1,
                            'elected': {
                                'num_of_total': 0,
                            },
                            'not_elected': {
                                'num_of_total': 0,
                            },
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '3 sec [not running]',
                        'recovery_timer': '30 sec [not running]',
                        'carving_timer': '0 sec [not running]',
                        'local_shg_label': 'None',
                        'remote_shg_labels': {
                            '0': {
                            },
                        },
                    },
                },
            },
        },
    }
    
    golden_output2 = {'execute.return_value': '''
        show evpn ethernet-segment detail

        Mon Oct  7 16:18:26.810 EDT
        Legend:
        B   - No Forwarders EVPN-enabled,
        C   - Backbone Source MAC missing (PBB-EVPN),
        RT  - ES-Import Route Target missing,
        E   - ESI missing,
        H   - Interface handle missing,
        I   - Name (Interface or Virtual Access) missing,
        M   - Interface in Down state,
        O   - BGP End of Download missing,
        P   - Interface already Access Protected,
        Pf  - Interface forced single-homed,
        R   - BGP RID not received,
        S   - Interface in redundancy standby state,
        X   - ESI-extracted MAC Conflict
        SHG - No local split-horizon-group label allocated

        Ethernet Segment Id      Interface                          Nexthops            
        ------------------------ ---------------------------------- --------------------
        0001.00ff.aaab.00ff.0003 BE3                                10.154.219.84
        ES to BGP Gates   : M
        ES to L2FIB Gates : Ready
        Main port         :
            Interface name : Bundle-Ether3
        Interface MAC  : 00c1.64ff.a415
            IfHandle       : 0x080002a0
            State          : Down
            Redundancy     : Not Defined
        ESI type          : 0
            Value          : 01.0000.aaff.abab.0003
        ES Import RT      : aaab.00ff.0003 (Local)
        Source MAC        : 0000.0000.0000 (N/A)
        Topology          :
            Operational    : SH
            Configured     : All-active (AApF) (default)
        Service Carving   : Auto-selection
        Peering Details   : 10.154.219.84[MOD:P:00]
        Service Carving Results:
            Forwarders     : 1
            Permanent      : 0
            Elected        : 0
            Not Elected    : 1
        MAC Flushing mode : STP-TCN
        Peering timer     : 3 sec [not running]
        Recovery timer    : 30 sec [not running]
        Carving timer     : 0 sec [not running]
        Local SHG label   : 100564
        Remote SHG labels : 0

        0001.00ff.aaab.00ff.0004 BE4                                10.154.219.84
        ES to BGP Gates   : Ready
        ES to L2FIB Gates : Ready
        Main port         :
            Interface name : Bundle-Ether4
            Interface MAC  : 00c1.64ff.a414
            IfHandle       : 0x080002e0
            State          : Up
            Redundancy     : Not Defined
        ESI type          : 0
            Value          : 01.0000.aaff.abab.0004
        ES Import RT      : aaab.00ff.0004 (Local)
        Source MAC        : 0000.0000.0000 (N/A)
        Topology          :
            Operational    : SH
            Configured     : All-active (AApF) (default)
        Service Carving   : Auto-selection
        Peering Details   : 10.154.219.84[MOD:P:00]
        Service Carving Results:
            Forwarders     : 1
            Permanent      : 0
        Elected        : 1
            Not Elected    : 0
        MAC Flushing mode : STP-TCN
        Peering timer     : 3 sec [not running]
        Recovery timer    : 30 sec [not running]
        Carving timer     : 0 sec [not running]
        Local SHG label   : 100565
        Remote SHG labels : 0

        N/A                      Gi0/0/0/12                         10.154.219.84
        ES to BGP Gates   : Ready
        ES to L2FIB Gates : Ready
        Main port         :
            Interface name : GigabitEthernet0/0/0/12
            Interface MAC  : 00c1.64ff.7f67
            IfHandle       : 0x000005c0
            State          : Up
            Redundancy     : Not Defined
        ESI type          : Invalid
        ES Import RT      : 0000.0000.0000 (Incomplete Configuration)
        Source MAC        : 00c1.64ff.a411 (PBB BSA, no ESI)
        Topology          :
            Operational    : SH
        Configured     : Single-active (AApS) (default)
        Service Carving   : Auto-selection
        Peering Details   : 10.154.219.84[MOD:P:00]
        Service Carving Results:
            Forwarders     : 1
            Permanent      : 1
            Elected        : 0
            Not Elected    : 0
        MAC Flushing mode : STP-TCN
        Peering timer     : 3 sec [not running]
        Recovery timer    : 30 sec [not running]
        Carving timer     : 0 sec [not running]
        Local SHG label   : None
        Remote SHG labels : 0

    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowEvpnEthernetSegmentDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowEvpnEthernetSegmentDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)
    
    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowEvpnEthernetSegmentDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output2)

# ============================================================
#  Unit test for 'show evpn ethernet-segment esi {esi} detail'
# ============================================================

class TestShowEvpnEthernetSegmentEsiDetail(unittest.TestCase):

    '''Unit test for 'show evpn ethernet-segment esi {esi} detail'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'segment_id': {
            '0047.47ff.0000.0000.2200': {
                'interface': {
                    'Bundle-Ether200': {
                        'next_hops': ['10.64.4.47', '10.64.4.48'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'Ready',
                        'main_port': {
                            'interface': 'Bundle-Ether100',
                            'interface_mac': '119b.17ff.3f44',
                            'if_handle': '0x0900001c',
                            'state': 'Up',
                            'redundancy': 'Not Defined',
                        },
                        'esi': {
                            'type': '0',
                            'value': '47.4811.11ff.2222.2211',
                        },
                        'es_import_rt': '4748.11ff.2222 (from ESI)',
                        'source_mac': '1111.11ff.2222 (N/A)',
                        'topology': {
                            'operational': 'MH, All-active',
                            'configured': 'All-active (AApF) (default)',
                        },
                        'service_carving': 'Auto-selection',
                        'peering_details': ['10.64.4.47[MOD:P:00]', '10.64.4.48[MOD:P:00]'],
                        'service_carving_results': {
                            'forwarders': 1,
                            'permanent': 0,
                            'elected': {
                                'num_of_total': 1,
                            },
                            'not_elected': {
                                'num_of_total': 0,
                            },
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '3 sec [not running]',
                        'recovery_timer': '30 sec [not running]',
                        'carving_timer': '0 sec [not running]',
                        'local_shg_label': '75116',
                        'remote_shg_labels': {
                            '1': {
                                'label': {
                                    '75116': {
                                        'nexthop': '10.64.4.48',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        show evpn ethernet-segment esi 0047.47ff.0000.0000.2200 detail

        Legend:

        B   - No Forwarders EVPN-enabled,

        C   - Backbone Source MAC missing (PBB-EVPN),

        RT  - ES-Import Route Target missing,

        E   - ESI missing,

        H   - Interface handle missing,

        I   - Name (Interface or Virtual Access) missing,

        M   - Interface in Down state,

        O   - BGP End of Download missing,

        P   - Interface already Access Protected,

        Pf  - Interface forced single-homed,

        R   - BGP RID not received,

        S   - Interface in redundancy standby state,

        X   - ESI-extracted MAC Conflict

        SHG - No local split-horizon-group label allocated

        

        Ethernet Segment Id      Interface                          Nexthops

        ------------------------ ---------------------------------- --------------------

        0047.47ff.0000.0000.2200 BE200                              10.64.4.47

                                                                    10.64.4.48

        ES to BGP Gates   : Ready

        ES to L2FIB Gates : Ready

        Main port         :

            Interface name : Bundle-Ether100

            Interface MAC  : 119b.17ff.3f44

            IfHandle       : 0x0900001c

            State          : Up

            Redundancy     : Not Defined

        ESI type          : 0

            Value          : 47.4811.11ff.2222.2211

        ES Import RT      : 4748.11ff.2222 (from ESI)

        Source MAC        : 1111.11ff.2222 (N/A)

        Topology          :

            Operational    : MH, All-active

            Configured     : All-active (AApF) (default)

        Service Carving   : Auto-selection

        Peering Details   : 10.64.4.47[MOD:P:00] 10.64.4.48[MOD:P:00]

        Service Carving Results:

            Forwarders     : 1

            Permanent      : 0

            Elected        : 1

            Not Elected    : 0

        MAC Flushing mode : STP-TCN

        Peering timer     : 3 sec [not running]

        Recovery timer    : 30 sec [not running]

        Carving timer     : 0 sec [not running]

        Local SHG label   : 75116

        Remote SHG labels : 1

                    75116 : nexthop 10.64.4.48
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowEvpnEthernetSegmentEsiDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(esi='0047.47ff.0000.0000.2200')

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowEvpnEthernetSegmentEsiDetail(device=self.device)
        parsed_output = obj.parse(esi='0047.47ff.0000.0000.2200')
        self.assertEqual(parsed_output,self.golden_parsed_output1)

# ===================================================
#  Unit test for 'show evpn internal-label'
# ===================================================
class TestShowEvpnInternalLabel(unittest.TestCase):

    '''Unit test for 'show evpn internal-label'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output1 = {
        'evi': {
            1000: {
                'ethernet_segment_id': {
                    '0000.01ff.0506.0506.07aa': {
                        'index': {
                            1: {
                                'ether_tag': '0',
                                'label': 'None',
                            },
                            2: {
                                'ether_tag': '200',
                                'label': '24011',
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        EVI     Ethernet    Segment Id                 EtherTag Label
        ----- --------------------------------------- -------- --------
        1000    0000.01ff.0506.0506.07aa                0       None
        1000    0000.01ff.0506.0506.07aa                200     24011
        '''}

    golden_parsed_output2 = {
        'evi': {
            1: {
                'ethernet_segment_id': {
                    '0055.55ff.aaaa.5555.5555': {
                        'index': {
                            1: {
                                'ether_tag': '0',
                                'label': 'None',
                                'encap': 'MPLS',
                            },
                            2: {
                                'ether_tag': '1',
                                'label': '29348',
                                'encap': 'MPLS',
                                'summary_pathlist': {
                                    'index': {
                                        1: {
                                            'tep_id': '0xffffffff',
                                            'df_role': '(P)',
                                            'nexthop': '192.168.0.3',
                                            'label': '29213',
                                        },
                                    },
                                },
                            },
                            3: {
                                'ether_tag': '3',
                                'label': '29352',
                                'encap': 'MPLS',
                                'summary_pathlist': {
                                    'index': {
                                        2: {
                                            'tep_id': '0xffffffff',
                                            'df_role': '(P)',
                                            'nexthop': '192.168.0.3',
                                            'label': '29224',
                                        },
                                    },
                                },
                            },
                        },
                    },
                    '0088.88ff.1111.8888.8888': {
                        'index': {
                            1: {
                                'ether_tag': '0',
                                'label': 'None',
                                'encap': 'MPLS',
                            },
                            2: {
                                'ether_tag': '1',
                                'label': '29350',
                                'encap': 'MPLS',
                                'summary_pathlist': {
                                    'index': {
                                        3: {
                                            'tep_id': '0xffffffff',
                                            'df_role': '(P)',
                                            'nexthop': '192.168.0.4',
                                            'label': '29340',
                                        },
                                    },
                                },
                            },
                            3: {
                                'ether_tag': '2',
                                'label': '29349',
                                'encap': 'MPLS',
                                'summary_pathlist': {
                                    'index': {
                                        4: {
                                            'tep_id': '0xffffffff',
                                            'df_role': '(P)',
                                            'nexthop': '192.168.0.3',
                                            'label': '29216',
                                        },
                                        5: {
                                            'tep_id': '0x00000000',
                                            'df_role': '(B)',
                                            'nexthop': '192.168.0.4',
                                            'label': '29341',
                                        },
                                    },
                                },
                            },
                            4: {
                                'ether_tag': '3',
                                'label': '29355',
                                'encap': 'MPLS',
                                'summary_pathlist': {
                                    'index': {
                                        6: {
                                            'tep_id': '0xffffffff',
                                            'df_role': '(P)',
                                            'nexthop': '192.168.0.4',
                                            'label': '29352',
                                        },
                                    },
                                },
                            },
                            5: {
                                'ether_tag': '4',
                                'label': '29354',
                                'encap': 'MPLS',
                                'summary_pathlist': {
                                    'index': {
                                        7: {
                                            'tep_id': '0xffffffff',
                                            'df_role': '(P)',
                                            'nexthop': '192.168.0.3',
                                            'label': '29226',
                                        },
                                        8: {
                                            'tep_id': '0x00000000',
                                            'df_role': '(B)',
                                            'nexthop': '192.168.0.4',
                                            'label': '29353',
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

    golden_output2 = {'execute.return_value': '''
    Device#show evpn internal-label
    Fri Jun 28 13:42:20.616 EST

    VPN-ID     Encap  Ethernet Segment Id         EtherTag     Label
    ---------- ------ --------------------------- ----------   --------
    1          MPLS   0055.55ff.aaaa.5555.5555    0            None

    1          MPLS   0055.55ff.aaaa.5555.5555    1            29348
    Summary pathlist:
    0xffffffff (P) 192.168.0.3                              29213

    1          MPLS   0055.55ff.aaaa.5555.5555    3            29352
    Summary pathlist:
    0xffffffff (P) 192.168.0.3                              29224

    1          MPLS   0088.88ff.1111.8888.8888    0            None

    1          MPLS   0088.88ff.1111.8888.8888    1            29350
    Summary pathlist:
    0xffffffff (P) 192.168.0.4                              29340

    1          MPLS   0088.88ff.1111.8888.8888    2            29349
    Summary pathlist:
    0xffffffff (P) 192.168.0.3                              29216
    0x00000000 (B) 192.168.0.4                              29341

    1          MPLS   0088.88ff.1111.8888.8888    3            29355
    Summary pathlist:
    0xffffffff (P) 192.168.0.4                              29352

    1          MPLS   0088.88ff.1111.8888.8888    4            29354
    Summary pathlist:
    0xffffffff (P) 192.168.0.3                              29226
    0x00000000 (B) 192.168.0.4                              29353
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowEvpnInternalLabel(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowEvpnInternalLabel(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)
    
    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowEvpnInternalLabel(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output2)

# ===================================================
#  Unit test for 'show evpn ethernet-segment private'
# ===================================================
class TestShowEvpnEthernetSegmentPrivate(unittest.TestCase):

    '''Unit test for 'show evpn ethernet-segment private'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'segment_id': {
            '0001.00ff.aaab.00ff.0003': {
                'interface': {
                    'Bundle-Ether3': {
                        'next_hops': ['10.154.219.84<'],
                        'es_to_bgp_gates': 'M',
                        'es_to_l2fib_gates': 'Ready',
                        'main_port': {
                            'interface': 'Bundle-Ether3',
                            'interface_mac': '00c1.64ff.a415',
                            'if_handle': '0x080002a0',
                            'state': 'Down',
                            'redundancy': 'Not Defined',
                        },
                        'esi': {
                            'type': '0',
                            'value': '01.0000.aaff.abab.0003',
                        },
                        'es_import_rt': 'aaab.00ff.0003 (Local)',
                        'source_mac': '0000.0000.0000 (N/A)',
                        'topology': {
                            'operational': 'SH',
                            'configured': 'All-active (AApF) (default)',
                        },
                        'service_carving': 'Auto-selection',
                        'peering_details': ['10.154.219.84[MOD:P:00][1]'],
                        'service_carving_results': {
                            'forwarders': 1,
                            'permanent': 0,
                            'elected': {
                                'num_of_total': 0,
                            },
                            'not_elected': {
                                'num_of_total': 1,
                            },
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '3',
                        'recovery_timer': '30',
                        'carving_timer': '0',
                        'local_shg_label': '100564',
                        'remote_shg_labels': {
                            '0': {
                            },
                        },
                        'object': {
                            'EVPN ES': {
                                'base_info': {
                                    'version': '0xdbdb0007',
                                    'flags': '0x0',
                                    'type': 7,
                                    'reserved': 0,
                                },
                                'num_events': 55,
                                'event_history': {
                                    1: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'ES DB Bind',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    2: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Create',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    3: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API Config Ifname Add',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    4: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    5: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API Config Local RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    6: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'ES DB Bind',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    7: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action L2FIB Instance Upd',
                                        'flag_1': '00000000',
                                        'flag_2': 'c1400000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    8: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    9: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API Config ESI complete',
                                        'flag_1': '00000000',
                                        'flag_2': '00000003',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    10: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API Provision',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    11: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    12: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    13: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    14: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    15: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    16: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    17: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    18: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    19: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    20: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    21: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    22: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    23: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    24: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    25: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    26: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    27: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    28: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    29: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    30: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    31: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    32: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    33: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    34: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    35: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    36: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    37: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    38: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    39: {
                                        'time': 'Aug 27 09:46:04.160',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c014',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    40: {
                                        'time': 'Aug 27 09:46:04.160',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0140000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    41: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'ES DB Unbind - tid',
                                        'flag_1': '00100001',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    42: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'Action Create RT',
                                        'flag_1': '00000000',
                                        'flag_2': 'aaab0000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    43: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'Action Advertise RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    44: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': 'c8040000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    45: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'API BP Ifname update',
                                        'flag_1': '00000000',
                                        'flag_2': '03e803e8',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    46: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': 'c8040000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    47: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'API BGP RID update',
                                        'flag_1': 'a5138011',
                                        'flag_2': '00011043',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    48: {
                                        'time': 'Aug 27 09:49:16.160',
                                        'event': 'Action EAD/EVI',
                                        'flag_1': '00000add',
                                        'flag_2': '000103e8',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    49: {
                                        'time': 'Aug 27 09:49:16.160',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0040000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    50: {
                                        'time': 'Aug 27 09:49:16.160',
                                        'event': 'API Recv LSD Local SHGLabel',
                                        'flag_1': '00000000',
                                        'flag_2': '000188d4',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    51: {
                                        'time': 'Aug 27 09:49:16.160',
                                        'event': 'Action EAD/EVI',
                                        'flag_1': '00000add',
                                        'flag_2': '000103e8',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    52: {
                                        'time': 'Aug 27 09:49:16.160',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0040000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    53: {
                                        'time': 'Aug 27 09:49:16.160',
                                        'event': 'API BGP mark / sweep',
                                        'flag_1': '00de1e7e',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    54: {
                                        'time': 'Aug 27 09:49:37.152',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    55: {
                                        'time': 'Aug 27 09:49:37.152',
                                        'event': 'API L2FIB Replay',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                },
                                'statistics': {
                                    'rt': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '27/08 09:49:15.582',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'localbmac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'esi': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_es': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_evi': {
                                        'adv_cnt': 2,
                                        'adv_last_time': '27/08 09:49:16.091',
                                        'adv_last_arg': '000003e8',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mst_ag_vpw': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'df_electfw': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '27/08 09:49:15.582',
                                        'adv_last_arg': '00000000',
                                    },
                                    'updatemac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushpe': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushce': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'instance': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mp_info': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '27/08 09:49:37.024',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                },
                            },
                        },
                        'diagnostic_esi': 'N/A',
                        'interface_name': 'N/A',
                        'diagnostic_ifh': '0x00000000',
                        'diagnostic_flag': '0x00000043',
                        'diagnostic_es_rt': '0000.0000.0000',
                        'port_key': '0x000088d4',
                        'mac_winner': '1',
                        'number_of_evis': '1',
                        'recovery_timer_per_es': 'global',
                        'peering_timer_per_es': 'global',
                        'carving_timer_per_es': 'global',
                        'rt_advertised': '1',
                        'esi_advertised': '0',
                        'msti_state_mask': '0x0000',
                        'hrw_msti_set': '0x3',
                        'es_ead_pulse': '0',
                        'mp_advertised': '1',
                        'nve_anycastvtep': '0',
                        'nve_ingrreplic': '0',
                        'peering_done': '0',
                        'carving_done': '1',
                        'inval_redundfwd': '0x00000000/0x00000000',
                        'inval_redund_nh': '0x00000000/0x00000000',
                        'chkpt_objid': '0x0',
                        'es_ead_update': {
                            'num_rds': 0,
                        },
                    },
                },
            },
            '0001.00ff.aaab.00ff.0004': {
                'interface': {
                    'Bundle-Ether4': {
                        'next_hops': ['10.154.219.84<'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'Ready',
                        'main_port': {
                            'interface': 'Bundle-Ether4',
                            'interface_mac': '00c1.64ff.a414',
                            'if_handle': '0x080002e0',
                            'state': 'Up',
                            'redundancy': 'Not Defined',
                        },
                        'esi': {
                            'type': '0',
                            'value': '01.0000.aaff.abab.0004',
                        },
                        'es_import_rt': 'aaab.00ff.0004 (Local)',
                        'source_mac': '0000.0000.0000 (N/A)',
                        'topology': {
                            'operational': 'SH',
                            'configured': 'All-active (AApF) (default)',
                        },
                        'service_carving': 'Auto-selection',
                        'peering_details': ['10.154.219.84[MOD:P:00][1]'],
                        'service_carving_results': {
                            'forwarders': 1,
                            'permanent': 0,
                            'elected': {
                                'num_of_total': 1,
                            },
                            'not_elected': {
                                'num_of_total': 0,
                            },
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '3',
                        'recovery_timer': '30',
                        'carving_timer': '0',
                        'local_shg_label': '100565',
                        'remote_shg_labels': {
                            '0': {
                            },
                        },
                        'object': {
                            'EVPN ES': {
                                'base_info': {
                                    'version': '0xdbdb0007',
                                    'flags': '0x0',
                                    'type': 7,
                                    'reserved': 0,
                                },
                                'num_events': 64,
                                'event_history': {
                                    56: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API Config Ifname Add',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    57: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    58: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API Config Local RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    59: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'ES DB Bind',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    60: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action L2FIB Instance Upd',
                                        'flag_1': '00000000',
                                        'flag_2': 'c1400000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    61: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    62: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API Config ESI complete',
                                        'flag_1': '00000000',
                                        'flag_2': '00000003',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    63: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API Provision',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    64: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    65: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    66: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    67: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    68: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    69: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    70: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    71: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    72: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    73: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    74: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    75: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    76: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    77: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    78: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    79: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    80: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    81: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    82: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    83: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    84: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    85: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    86: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    87: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    88: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    89: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    90: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    91: {
                                        'time': 'Aug 27 09:44:15.616',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0160000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    92: {
                                        'time': 'Aug 27 09:46:04.160',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c014',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    93: {
                                        'time': 'Aug 27 09:46:04.160',
                                        'event': 'API BGP Replay',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0140000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    94: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'ES DB Unbind - tid',
                                        'flag_1': '00100001',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    95: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'Action Create RT',
                                        'flag_1': '00000000',
                                        'flag_2': 'aaab0000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    96: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'Action Advertise RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    97: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': 'c8040000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    98: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'API BP Ifname update',
                                        'flag_1': '00000000',
                                        'flag_2': '03e803e8',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    99: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': 'c8040000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    100: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'API BGP RID update',
                                        'flag_1': 'a5138011',
                                        'flag_2': '00011043',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    101: {
                                        'time': 'Aug 27 09:49:16.160',
                                        'event': 'Action EAD/EVI',
                                        'flag_1': '00000add',
                                        'flag_2': '000103e8',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    102: {
                                        'time': 'Aug 27 09:49:16.160',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0040000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    103: {
                                        'time': 'Aug 27 09:49:16.160',
                                        'event': 'API Recv LSD Local SHGLabel',
                                        'flag_1': '00000000',
                                        'flag_2': '000188d5',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    104: {
                                        'time': 'Aug 27 09:49:16.160',
                                        'event': 'Action EAD/EVI',
                                        'flag_1': '00000add',
                                        'flag_2': '000103e8',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    105: {
                                        'time': 'Aug 27 09:49:16.160',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0040000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    106: {
                                        'time': 'Aug 27 09:49:16.160',
                                        'event': 'API BGP mark / sweep',
                                        'flag_1': '00de1e7e',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    107: {
                                        'time': 'Aug 27 09:49:37.152',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    108: {
                                        'time': 'Aug 27 09:49:37.152',
                                        'event': 'API L2FIB Replay',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    109: {
                                        'time': 'Aug 27 09:49:41.760',
                                        'event': 'Action L2FIB Instance Upd',
                                        'flag_1': '000f0001',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    110: {
                                        'time': 'Aug 27 09:49:41.760',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    111: {
                                        'time': 'Aug 27 09:49:41.760',
                                        'event': 'Action Advertise ESI',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    112: {
                                        'time': 'Aug 27 09:49:41.760',
                                        'event': 'Action EAD/ES',
                                        'flag_1': '00000001',
                                        'flag_2': '000188d5',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    113: {
                                        'time': 'Aug 27 09:49:41.760',
                                        'event': 'Action EAD/EVI',
                                        'flag_1': '00000add',
                                        'flag_2': '000103e8',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    114: {
                                        'time': 'Aug 27 09:49:41.760',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    115: {
                                        'time': 'Aug 27 09:49:41.760',
                                        'event': 'API IM MP | AToM state',
                                        'flag_1': '00000000',
                                        'flag_2': '00320002',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    116: {
                                        'time': 'Aug 27 09:49:41.760',
                                        'event': 'Action EAD/ES',
                                        'flag_1': '00000add',
                                        'flag_2': '000b89d5',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    117: {
                                        'time': 'Aug 27 09:49:44.832',
                                        'event': 'Action L2FIB Instance Upd',
                                        'flag_1': '000f7fff',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    118: {
                                        'time': 'Aug 27 09:49:44.832',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    119: {
                                        'time': 'Aug 27 09:49:44.832',
                                        'event': 'API Peer Timer Expiry',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                },
                                'statistics': {
                                    'rt': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '27/08 09:49:15.582',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'localbmac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'esi': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '27/08 09:49:41.604',
                                        'adv_last_arg': '00000001',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_es': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '27/08 09:49:41.606',
                                        'adv_last_arg': '0000000a',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_evi': {
                                        'adv_cnt': 3,
                                        'adv_last_time': '27/08 09:49:41.604',
                                        'adv_last_arg': '000003e8',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mst_ag_vpw': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'df_electfw': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '27/08 09:49:15.582',
                                        'adv_last_arg': '00000000',
                                    },
                                    'updatemac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushpe': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushce': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'instance': {
                                        'adv_cnt': 2,
                                        'adv_last_time': '27/08 09:49:44.606',
                                        'adv_last_arg': '00007fff',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mp_info': {
                                        'adv_cnt': 3,
                                        'adv_last_time': '27/08 09:49:44.606',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                },
                            },
                        },
                        'diagnostic_esi': 'N/A',
                        'interface_name': 'N/A',
                        'diagnostic_ifh': '0x00000000',
                        'diagnostic_flag': '0x00000043',
                        'diagnostic_es_rt': '0000.0000.0000',
                        'port_key': '0x000088d5',
                        'mac_winner': '1',
                        'number_of_evis': '1',
                        'recovery_timer_per_es': 'global',
                        'peering_timer_per_es': 'global',
                        'carving_timer_per_es': 'global',
                        'rt_advertised': '1',
                        'esi_advertised': '1',
                        'msti_state_mask': '0x7fff',
                        'hrw_msti_set': '0x3',
                        'es_ead_pulse': '0',
                        'mp_advertised': '1',
                        'nve_anycastvtep': '0',
                        'nve_ingrreplic': '0',
                        'peering_done': '1',
                        'carving_done': '1',
                        'inval_redundfwd': '0x00000000/0x00000000',
                        'inval_redund_nh': '0x00000000/0x00000000',
                        'chkpt_objid': '0x40002f18',
                        'checkpoint_info': {
                            'msti_mask': '0x7fff',
                        },
                        'es_ead_update': {
                            'num_rds': 1,
                            'rd': {
                                '10.154.219.84:1': {
                                    'num_rts': 1,
                                    'rt_list': ['4:1000'],
                                },
                            },
                        },
                    },
                },
            },
            'N/A': {
                'interface': {
                    'GigabitEthernet0/0/0/12': {
                        'next_hops': ['10.154.219.84<'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'Ready',
                        'main_port': {
                            'interface': 'GigabitEthernet0/0/0/12',
                            'interface_mac': '00c1.64ff.7f67',
                            'if_handle': '0x000005c0',
                            'state': 'Up',
                            'redundancy': 'Not Defined',
                        },
                        'esi': {
                            'type': 'Invalid',
                        },
                        'es_import_rt': '0000.0000.0000 (Incomplete Configuration)',
                        'source_mac': '00c1.64ff.a411 (PBB BSA, no ESI)',
                        'topology': {
                            'operational': 'SH',
                            'configured': 'Single-active (AApS) (default)',
                        },
                        'service_carving': 'Auto-selection',
                        'peering_details': ['10.154.219.84[MOD:P:00][1]'],
                        'service_carving_results': {
                            'forwarders': 1,
                            'permanent': 1,
                            'elected': {
                                'num_of_total': 0,
                            },
                            'not_elected': {
                                'num_of_total': 0,
                            },
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '3',
                        'recovery_timer': '30',
                        'carving_timer': '0',
                        'local_shg_label': 'None',
                        'remote_shg_labels': {
                            '0': {
                            },
                        },
                        'object': {
                            'EVPN ES': {
                                'base_info': {
                                    'version': '0xdbdb0007',
                                    'flags': '0x0',
                                    'type': 7,
                                    'reserved': 0,
                                },
                                'num_events': 20,
                                'event_history': {
                                    120: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'ES DB Bind',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    121: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'Create',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    122: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'Action L2FIB Instance Upd',
                                        'flag_1': '000f7fff',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    123: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'Action Advertise RT',
                                        'flag_1': 'a5138016',
                                        'flag_2': '0000ffff',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    124: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    125: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': '00008001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    126: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'API BP Ifname update',
                                        'flag_1': '00000000',
                                        'flag_2': '08400000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    127: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'Action Advertise RT',
                                        'flag_1': 'a5138016',
                                        'flag_2': '0000ffff',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    128: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    129: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': '00008001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    130: {
                                        'time': 'Aug 27 09:49:15.648',
                                        'event': 'API BGP RID update',
                                        'flag_1': 'a5138011',
                                        'flag_2': '00010040',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    131: {
                                        'time': 'Aug 27 09:49:16.160',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    132: {
                                        'time': 'Aug 27 09:49:16.160',
                                        'event': 'API L2FIB Replay',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    133: {
                                        'time': 'Aug 27 09:49:16.160',
                                        'event': 'API BGP mark / sweep',
                                        'flag_1': '00de1e7e',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    134: {
                                        'time': 'Aug 27 09:49:18.720',
                                        'event': 'Action L2FIB Instance Upd',
                                        'flag_1': '000f7fff',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    135: {
                                        'time': 'Aug 27 09:49:18.720',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    136: {
                                        'time': 'Aug 27 09:49:18.720',
                                        'event': 'API Peer Timer Expiry',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    137: {
                                        'time': 'Aug 27 09:49:37.152',
                                        'event': 'Action L2FIB Instance Upd',
                                        'flag_1': '000f7fff',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    138: {
                                        'time': 'Aug 27 09:49:37.152',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    139: {
                                        'time': 'Aug 27 09:49:37.152',
                                        'event': 'API L2FIB Replay',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                },
                                'statistics': {
                                    'rt': {
                                        'adv_cnt': 2,
                                        'adv_last_time': '27/08 09:49:15.583',
                                        'adv_last_arg': 'a5138016',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'localbmac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'esi': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_es': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_evi': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mst_ag_vpw': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'df_electfw': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'updatemac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushpe': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushce': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'instance': {
                                        'adv_cnt': 3,
                                        'adv_last_time': '27/08 09:49:37.025',
                                        'adv_last_arg': '00007fff',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mp_info': {
                                        'adv_cnt': 5,
                                        'adv_last_time': '27/08 09:49:37.025',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                },
                            },
                        },
                        'diagnostic_esi': 'N/A',
                        'interface_name': 'N/A',
                        'diagnostic_ifh': '0x00000000',
                        'diagnostic_flag': '0x00000040',
                        'diagnostic_es_rt': '0000.0000.0000',
                        'port_key': '0x00000001',
                        'mac_winner': '1',
                        'number_of_evis': '1',
                        'recovery_timer_per_es': 'global',
                        'peering_timer_per_es': 'global',
                        'carving_timer_per_es': 'global',
                        'rt_advertised': '0',
                        'esi_advertised': '0',
                        'msti_state_mask': '0x7fff',
                        'hrw_msti_set': '0x3',
                        'es_ead_pulse': '0',
                        'mp_advertised': '1',
                        'nve_anycastvtep': '0',
                        'nve_ingrreplic': '0',
                        'peering_done': '1',
                        'carving_done': '1',
                        'inval_redundfwd': '0x00000000/0x00000000',
                        'inval_redund_nh': '0x00000000/0x00000000',
                        'chkpt_objid': '0x40002f58',
                        'checkpoint_info': {
                            'msti_mask': '0x7fff',
                        },
                        'es_ead_update': {
                            'num_rds': 0,
                        },
                    },
                },
            },
        },
    }
    golden_output1 = {'execute.return_value': '''
        +++ Router: executing command 'show evpn ethernet-segment private' +++
        show evpn ethernet-segment private

        Mon Oct  7 16:18:27.805 EDT
        Legend:
        B   - No Forwarders EVPN-enabled,
        C   - Backbone Source MAC missing (PBB-EVPN),
        RT  - ES-Import Route Target missing,
        E   - ESI missing,
        H   - Interface handle missing,
        I   - Name (Interface or Virtual Access) missing,
        M   - Interface in Down state,
        O   - BGP End of Download missing,
        P   - Interface already Access Protected,
        Pf  - Interface forced single-homed,
        R   - BGP RID not received,
        S   - Interface in redundancy standby state,
        X   - ESI-extracted MAC Conflict
        SHG - No local split-horizon-group label allocated

        Ethernet Segment Id      Interface                          Nexthops (*stale)   
        ------------------------ ---------------------------------- --------------------
        0001.00ff.aaab.00ff.0003 BE3                                10.154.219.84<
        ES to BGP Gates   : M
        ES to L2FIB Gates : Ready
        Main port         :
            Interface name : Bundle-Ether3
        Interface MAC  : 00c1.64ff.a415
            IfHandle       : 0x080002a0
            State          : Down
            Redundancy     : Not Defined
        ESI type          : 0
            Value          : 01.0000.aaff.abab.0003
        ES Import RT      : aaab.00ff.0003 (Local)
        Source MAC        : 0000.0000.0000 (N/A)
        Topology          :
            Operational    : SH
            Configured     : All-active (AApF) (default)
        Service Carving   : Auto-selection
        Peering Details   : 10.154.219.84[MOD:P:00][1]
        Service Carving Results:
            Forwarders     : 1
            Permanent      : 0
            Elected        : 0
            Not Elected    : 1
        MAC Flushing mode : STP-TCN
        Peering timer     : 3 sec [not running]
        Recovery timer    : 30 sec [not running]
        Carving timer     : 0 sec [not running]
        Local SHG label   : 100564
        Remote SHG labels : 0

        Object: EVPN ES
        Base info: version=0xdbdb0007, flags=0x0, type=7, reserved=0
        EVPN ES event history  [Num events: 55]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Aug 27 09:44:15.616  ES DB Bind                   00000000, 00000001 -  - 
            Aug 27 09:44:15.616  Create                       00000000, 00000001 -  - 
            Aug 27 09:44:15.616 API Config Ifname Add         00000000, 00000001 -  - 
            Aug 27 09:44:15.616  Action Peering Sequence      00000000, c0160000 -  - 
            Aug 27 09:44:15.616 API Config Local RT           00000000, 00000000 -  - 
            Aug 27 09:44:15.616  ES DB Bind                   00000000, 00010001 -  - 
            Aug 27 09:44:15.616  Action L2FIB Instance Upd    00000000, c1400000 -  - 
            Aug 27 09:44:15.616  Action Peering Sequence      00000000, c0160000 -  - 
            Aug 27 09:44:15.616 API Config ESI complete       00000000, 00000003 -  - 
            Aug 27 09:44:15.616 API Provision                 00000000, 00000000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
        Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
        Aug 27 09:46:04.160  Action Advertise MAC         00000000, 0000c014 -  - 
            Aug 27 09:46:04.160 API BGP Replay                00000000, c0140000 -  - 
            Aug 27 09:49:15.648  ES DB Unbind - tid           00100001, 00000000 -  - 
            Aug 27 09:49:15.648  Action Create RT             00000000, aaab0000 -  - 
            Aug 27 09:49:15.648  Action Advertise RT          00000000, 00010001 -  - 
            Aug 27 09:49:15.648  Action Peering Sequence      00000000, c8040000 -  - 
            Aug 27 09:49:15.648 API BP Ifname update          00000000, 03e803e8 M  - 
            Aug 27 09:49:15.648  Action Peering Sequence      00000000, c8040000 -  - 
            Aug 27 09:49:15.648 API BGP RID update            a5138011, 00011043 -  - 
            Aug 27 09:49:16.160  Action EAD/EVI               00000add, 000103e8 -  - 
            Aug 27 09:49:16.160  Action Peering Sequence      00000000, c0040000 -  - 
            Aug 27 09:49:16.160 API Recv LSD Local SHGLabel   00000000, 000188d4 -  - 
            Aug 27 09:49:16.160  Action EAD/EVI               00000add, 000103e8 -  - 
            Aug 27 09:49:16.160  Action Peering Sequence      00000000, c0040000 -  - 
            Aug 27 09:49:16.160 API BGP mark / sweep          00de1e7e, 00000001 -  - 
            Aug 27 09:49:37.152  Action L2FIB MP Info Upd     00000000, 00000001 -  - 
            Aug 27 09:49:37.152 API L2FIB Replay              00000000, 00000000 -  - 
        ----------------------------------------------------------------------------
        EVPN ES Statistics
                    |Adv                             |Wdw                             
                    | Cnt Last Time          Last Arg| Cnt Last Time          Last Arg
                RT|   1 27/08 09:49:15.582 00000000|   0                    00000000
            LocalBMAC|   0                    00000000|   0                    00000000
            ESI|   0                    00000000|   0                    00000000
            EAD/ES|   0                    00000000|   0                    00000000
            EAD/EVI|   2 27/08 09:49:16.091 000003e8|   0                    00000000
        MST-AG VPW|   0                    00000000|   0                    00000000
        DF ElectFW|   1 27/08 09:49:15.582 00000000|
            UpdateMAC|   0                    00000000|
        MacFlushPE|   0                    00000000|
        MacFlushCE|   0                    00000000|
            Instance|   0                    00000000|   0                    00000000
            MP Info|   1 27/08 09:49:37.024 00000000|   0                    00000000
        ----------------------------------------------------------------------------
        Diagnostic ESI : N/A                     Interface Name : N/A
        Diagnostic Ifh : 0x00000000
        Diagnostic Flag: 0x00000043              DiagnosticES-RT: 0000.0000.0000
        Port Key       : 0x000088d4              MAC winner     : 1
        Number of EVIs : 1
        Recovery Timer : 30   (global)           Peering Timer  : 3    (global)  
        Carving Timer  : 0    (global)  
        RT Advertised  : 1                       ESI Advertised : 0
        MSTi state mask: 0x0000                  HRW MSTi Set   : 0x3
        ES EAD Pulse   : 0                       MP Advertised  : 1
        NVE AnycastVTEP: 0                       NVE Ingr-Replic: 0
        Peering Done   : 0                       Carving Done   : 1
            Inval/RedundFWD: 0x00000000/0x00000000
        Inval/Redund NH: 0x00000000/0x00000000
        Chkpt ObjId    : 0x0
        ES EAD Update     :
            Num RDs:       : 0

        0001.00ff.aaab.00ff.0004 BE4                                10.154.219.84<
        ES to BGP Gates   : Ready
        ES to L2FIB Gates : Ready
        Main port         :
            Interface name : Bundle-Ether4
            Interface MAC  : 00c1.64ff.a414
            IfHandle       : 0x080002e0
            State          : Up
            Redundancy     : Not Defined
        ESI type          : 0
            Value          : 01.0000.aaff.abab.0004
        ES Import RT      : aaab.00ff.0004 (Local)
        Source MAC        : 0000.0000.0000 (N/A)
        Topology          :
            Operational    : SH
            Configured     : All-active (AApF) (default)
        Service Carving   : Auto-selection
        Peering Details   : 10.154.219.84[MOD:P:00][1]
        Service Carving Results:
            Forwarders     : 1
            Permanent      : 0
            Elected        : 1
            Not Elected    : 0
        MAC Flushing mode : STP-TCN
        Peering timer     : 3 sec [not running]
        Recovery timer    : 30 sec [not running]
        Carving timer     : 0 sec [not running]
        Local SHG label   : 100565
        Remote SHG labels : 0

        Object: EVPN ES
        Base info: version=0xdbdb0007, flags=0x0, type=7, reserved=0
        EVPN ES event history  [Num events: 64]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Aug 27 09:44:15.616 API Config Ifname Add         00000000, 00000001 -  - 
            Aug 27 09:44:15.616  Action Peering Sequence      00000000, c0160000 -  - 
            Aug 27 09:44:15.616 API Config Local RT           00000000, 00000000 -  - 
            Aug 27 09:44:15.616  ES DB Bind                   00000000, 00010001 -  - 
        Aug 27 09:44:15.616  Action L2FIB Instance Upd    00000000, c1400000 -  - 
            Aug 27 09:44:15.616  Action Peering Sequence      00000000, c0160000 -  - 
            Aug 27 09:44:15.616 API Config ESI complete       00000000, 00000003 -  - 
            Aug 27 09:44:15.616 API Provision                 00000000, 00000000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
        Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:44:15.616  Action Advertise MAC         00000000, 0000c016 -  - 
            Aug 27 09:44:15.616 API BGP Replay                00000000, c0160000 -  - 
            Aug 27 09:46:04.160  Action Advertise MAC         00000000, 0000c014 -  - 
            Aug 27 09:46:04.160 API BGP Replay                00000000, c0140000 -  - 
            Aug 27 09:49:15.648  ES DB Unbind - tid           00100001, 00000000 -  - 
            Aug 27 09:49:15.648  Action Create RT             00000000, aaab0000 -  - 
            Aug 27 09:49:15.648  Action Advertise RT          00000000, 00010001 -  - 
            Aug 27 09:49:15.648  Action Peering Sequence      00000000, c8040000 -  - 
            Aug 27 09:49:15.648 API BP Ifname update          00000000, 03e803e8 M  - 
            Aug 27 09:49:15.648  Action Peering Sequence      00000000, c8040000 -  - 
            Aug 27 09:49:15.648 API BGP RID update            a5138011, 00011043 -  - 
            Aug 27 09:49:16.160  Action EAD/EVI               00000add, 000103e8 -  - 
            Aug 27 09:49:16.160  Action Peering Sequence      00000000, c0040000 -  - 
            Aug 27 09:49:16.160 API Recv LSD Local SHGLabel   00000000, 000188d5 -  - 
            Aug 27 09:49:16.160  Action EAD/EVI               00000add, 000103e8 -  - 
            Aug 27 09:49:16.160  Action Peering Sequence      00000000, c0040000 -  - 
        Aug 27 09:49:16.160 API BGP mark / sweep          00de1e7e, 00000001 -  - 
            Aug 27 09:49:37.152  Action L2FIB MP Info Upd     00000000, 00000001 -  - 
            Aug 27 09:49:37.152 API L2FIB Replay              00000000, 00000000 -  - 
            Aug 27 09:49:41.760  Action L2FIB Instance Upd    000f0001, 00000000 -  - 
            Aug 27 09:49:41.760  Action L2FIB MP Info Upd     00000000, 00000001 -  - 
            Aug 27 09:49:41.760  Action Advertise ESI         00000000, 00010001 -  - 
            Aug 27 09:49:41.760  Action EAD/ES                00000001, 000188d5 -  - 
            Aug 27 09:49:41.760  Action EAD/EVI               00000add, 000103e8 -  - 
            Aug 27 09:49:41.760  Action Peering Sequence      00000000, 00000000 -  - 
            Aug 27 09:49:41.760 API IM MP | AToM state        00000000, 00320002 -  - 
            Aug 27 09:49:41.760  Action EAD/ES                00000add, 000b89d5 -  - 
            Aug 27 09:49:44.832  Action L2FIB Instance Upd    000f7fff, 00000000 -  - 
            Aug 27 09:49:44.832  Action L2FIB MP Info Upd     00000000, 00000001 -  - 
            Aug 27 09:49:44.832 API Peer Timer Expiry         00000000, 00000001 -  - 
        ----------------------------------------------------------------------------
        EVPN ES Statistics
                    |Adv                             |Wdw                             
                    | Cnt Last Time          Last Arg| Cnt Last Time          Last Arg
                RT|   1 27/08 09:49:15.582 00000000|   0                    00000000
            LocalBMAC|   0                    00000000|   0                    00000000
                ESI|   1 27/08 09:49:41.604 00000001|   0                    00000000
            EAD/ES|   1 27/08 09:49:41.606 0000000a|   0                    00000000
            EAD/EVI|   3 27/08 09:49:41.604 000003e8|   0                    00000000
            MST-AG VPW|   0                    00000000|   0                    00000000
        DF ElectFW|   1 27/08 09:49:15.582 00000000|
            UpdateMAC|   0                    00000000|
        MacFlushPE|   0                    00000000|
        MacFlushCE|   0                    00000000|
            Instance|   2 27/08 09:49:44.606 00007fff|   0                    00000000
            MP Info|   3 27/08 09:49:44.606 00000000|   0                    00000000
        ----------------------------------------------------------------------------
        Diagnostic ESI : N/A                     Interface Name : N/A
        Diagnostic Ifh : 0x00000000
        Diagnostic Flag: 0x00000043              DiagnosticES-RT: 0000.0000.0000
        Port Key       : 0x000088d5              MAC winner     : 1
        Number of EVIs : 1
        Recovery Timer : 30   (global)           Peering Timer  : 3    (global)  
        Carving Timer  : 0    (global)  
        RT Advertised  : 1                       ESI Advertised : 1
        MSTi state mask: 0x7fff                  HRW MSTi Set   : 0x3
        ES EAD Pulse   : 0                       MP Advertised  : 1
        NVE AnycastVTEP: 0                       NVE Ingr-Replic: 0
        Peering Done   : 1                       Carving Done   : 1
        Inval/RedundFWD: 0x00000000/0x00000000
        Inval/Redund NH: 0x00000000/0x00000000
        Chkpt ObjId    : 0x40002f18
            MSTi Mask      : 0x7fff
        ES EAD Update     :
            Num RDs:       : 1

            RD: 10.154.219.84:1, Num RTs: 1      RT List:
                4:1000, 
        N/A                      Gi0/0/0/12                         10.154.219.84<
        ES to BGP Gates   : Ready
        ES to L2FIB Gates : Ready
        Main port         :
            Interface name : GigabitEthernet0/0/0/12
            Interface MAC  : 00c1.64ff.7f67
            IfHandle       : 0x000005c0
            State          : Up
            Redundancy     : Not Defined
        ESI type          : Invalid
        ES Import RT      : 0000.0000.0000 (Incomplete Configuration)
        Source MAC        : 00c1.64ff.a411 (PBB BSA, no ESI)
        Topology          :
            Operational    : SH
            Configured     : Single-active (AApS) (default)
        Service Carving   : Auto-selection
        Peering Details   : 10.154.219.84[MOD:P:00][1]
        Service Carving Results:
            Forwarders     : 1
            Permanent      : 1
            Elected        : 0
            Not Elected    : 0
        MAC Flushing mode : STP-TCN
        Peering timer     : 3 sec [not running]
        Recovery timer    : 30 sec [not running]
        Carving timer     : 0 sec [not running]
        Local SHG label   : None
        Remote SHG labels : 0

        Object: EVPN ES
        Base info: version=0xdbdb0007, flags=0x0, type=7, reserved=0
        EVPN ES event history  [Num events: 20]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Aug 27 09:49:15.648  ES DB Bind                   00000000, 00000001 -  - 
            Aug 27 09:49:15.648  Create                       00000000, 00000001 -  - 
            Aug 27 09:49:15.648  Action L2FIB Instance Upd    000f7fff, 00000000 -  - 
            Aug 27 09:49:15.648  Action Advertise RT          a5138016, 0000ffff -  - 
            Aug 27 09:49:15.648  Action L2FIB MP Info Upd     00000000, 00000001 -  - 
        Aug 27 09:49:15.648  Action Peering Sequence      00000000, 00008001 -  - 
            Aug 27 09:49:15.648 API BP Ifname update          00000000, 08400000 M  - 
            Aug 27 09:49:15.648  Action Advertise RT          a5138016, 0000ffff -  - 
            Aug 27 09:49:15.648  Action L2FIB MP Info Upd     00000000, 00000001 -  - 
            Aug 27 09:49:15.648  Action Peering Sequence      00000000, 00008001 -  - 
            Aug 27 09:49:15.648 API BGP RID update            a5138011, 00010040 -  - 
            Aug 27 09:49:16.160  Action L2FIB MP Info Upd     00000000, 00000001 -  - 
            Aug 27 09:49:16.160 API L2FIB Replay              00000000, 00000000 -  - 
            Aug 27 09:49:16.160 API BGP mark / sweep          00de1e7e, 00000001 -  - 
            Aug 27 09:49:18.720  Action L2FIB Instance Upd    000f7fff, 00000000 -  - 
            Aug 27 09:49:18.720  Action L2FIB MP Info Upd     00000000, 00000001 -  - 
            Aug 27 09:49:18.720 API Peer Timer Expiry         00000000, 00000001 -  - 
            Aug 27 09:49:37.152  Action L2FIB Instance Upd    000f7fff, 00000000 -  - 
            Aug 27 09:49:37.152  Action L2FIB MP Info Upd     00000000, 00000001 -  - 
            Aug 27 09:49:37.152 API L2FIB Replay              00000000, 00000000 -  - 
        ----------------------------------------------------------------------------
        EVPN ES Statistics
                    |Adv                             |Wdw                             
                    | Cnt Last Time          Last Arg| Cnt Last Time          Last Arg
                RT|   2 27/08 09:49:15.583 a5138016|   0                    00000000
            LocalBMAC|   0                    00000000|   0                    00000000
                ESI|   0                    00000000|   0                    00000000
            EAD/ES|   0                    00000000|   0                    00000000
        EAD/EVI|   0                    00000000|   0                    00000000
        MST-AG VPW|   0                    00000000|   0                    00000000
        DF ElectFW|   0                    00000000|
            UpdateMAC|   0                    00000000|
        MacFlushPE|   0                    00000000|
        MacFlushCE|   0                    00000000|
            Instance|   3 27/08 09:49:37.025 00007fff|   0                    00000000
            MP Info|   5 27/08 09:49:37.025 00000000|   0                    00000000
        ----------------------------------------------------------------------------
        Diagnostic ESI : N/A                     Interface Name : N/A
        Diagnostic Ifh : 0x00000000
        Diagnostic Flag: 0x00000040              DiagnosticES-RT: 0000.0000.0000
        Port Key       : 0x00000001              MAC winner     : 1
        Number of EVIs : 1
        Recovery Timer : 30   (global)           Peering Timer  : 3    (global)  
        Carving Timer  : 0    (global)  
        RT Advertised  : 0                       ESI Advertised : 0
        MSTi state mask: 0x7fff                  HRW MSTi Set   : 0x3
        ES EAD Pulse   : 0                       MP Advertised  : 1
        NVE AnycastVTEP: 0                       NVE Ingr-Replic: 0
        Peering Done   : 1                       Carving Done   : 1
        Inval/RedundFWD: 0x00000000/0x00000000
        Inval/Redund NH: 0x00000000/0x00000000
            Chkpt ObjId    : 0x40002f58
        MSTi Mask      : 0x7fff
        ES EAD Update     :
            Num RDs:       : 0

        Router#
        '''}

    golden_output2 = {'execute.return_value':'''
     RP/0/0/CPU0:PE1#show evpn ethernet-segment private 
        Thu Aug 15 22:11:12.864 PDT
        Legend:
        B   - No Forwarders EVPN-enabled,
        C   - Backbone Source MAC missing (PBB-EVPN),
        RT  - ES-Import Route Target missing,
        E   - ESI missing,
        H   - Interface handle missing,
        I   - Name (Interface or Virtual Access) missing,
        M   - Interface in Down state,
        O   - BGP End of Download missing,
        P   - Interface already Access Protected,
        Pf  - Interface forced single-homed,
        R   - BGP RID not received,
        S   - Interface in redundancy standby state,
        X   - ESI-extracted MAC Conflict
        SHG - No local split-horizon-group label allocated

        Ethernet Segment Id      Interface                          Nexthops (*stale)   
        ------------------------ ---------------------------------- --------------------
        0001.00ff.0108.0001.0007 BE7                                192.168.0.1
                                                                    192.168.0.3
        ES to BGP Gates   : Ready
        ES to L2FIB Gates : O
        Main port         :
            Interface name : Bundle-Ether7
            Interface MAC  : 02ef.afff.0e8f
            IfHandle       : 0x00004110
            State          : Standby
            Redundancy     : Active
        ESI type          : 0
            Value          : 01.0001.00ff.0708.0007
        ES Import RT      : 0100.01ff.0700 (from ESI)
        Source MAC        : 0000.0000.0000 (N/A)
        Topology          :
            Operational    : MH
            Configured     : Port-Active
        Service Carving   : Auto-selection
            Multicast      : Disabled
        Peering Details   :
            192.168.0.1 [MOD:P:00][1]
            192.168.0.3 [MOD:P:00][2]

        Service Carving Results:
            Forwarders     : 24
            Elected        : 0
            Not Elected    : 6
        EVPN-VPWS Service Carving Results:
            Primary        : 0
            Backup         : 0
            Non-DF         : 18
        MAC Flushing mode : STP-TCN
        Peering timer     : 3 sec [not running]
        Recovery timer    : 30 sec [not running]
        Carving timer     : 0 sec [not running]
        Local SHG label   : 28534
        Remote SHG labels : 1
                    28425 : nexthop 192.168.0.3

        Object: EVPN ES
        Base info: version=0xdbdb0007, flags=0x0, type=7, reserved=0
        EVPN ES event history  [Num events: 28]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Aug 15 22:10:12.736  Create                       00000000 00000001 -  - 
            Aug 15 22:10:12.736 API Config Ifname Add         00000000 00000001 -  - 
            Aug 15 22:10:12.992  Action Advertise MAC         00000000 0000c016 -  - 
            Aug 15 22:10:12.992 API L2VPN RG MP Role          00000000 00000101 -  - 
            Aug 15 22:10:12.992 API Config Local RT           00000000 00000000 -  - 
            Aug 15 22:10:12.992  ES DB Bind                   00000000 00010001 M  - 
            Aug 15 22:10:12.992 API Config ESI complete       00000000 00000003 -  - 
            Aug 15 22:10:12.992  Action Withdraw MAC          00000000 0000c016 -  - 
            Aug 15 22:10:12.992  Mgr Withdraw BGP             00000000 c0060003 -  - 
            Aug 15 22:10:12.992  Action Create RT             00000000 01000100 -  - 
            Aug 15 22:10:12.992  Action Advertise RT          00000000 00010001 -  - 
            Aug 15 22:10:12.992 API Config LB mode            00000005 00000005 -  - 
            Aug 15 22:10:12.992 API Provision                 00000000 00000000 -  - 
            Aug 15 22:10:12.992 API BP Ifname delete          45138200 0aa6b7f0 M  - 
            Aug 15 22:10:26.560 API BP Ifname update          00000000 00030003 M  - 
            Aug 15 22:10:26.560 API BGP RID update            00000000 00011043 -  - 
            Aug 15 22:10:26.560 API IM MP | AToM state        00000000 00440004 M  - 
            Aug 15 22:10:26.560  Action Advertise ESI         00000000 00010001 -  - 
            Aug 15 22:10:26.560  Action EAD/EVI               00000add 0006000f -  - 
            Aug 15 22:10:26.560  Action Peering Sequence      00000000 00000000 M  - 
            Aug 15 22:10:26.560 API Recv LSD Local SHGLabel   00000000 00006f76 -  - 
            Aug 15 22:10:29.504 API Peer Timer Expiry         8513800b 00000000 -  - 
            Aug 15 22:10:29.504  Action EAD/ES                00000add 000a6f76 M  - 
            Aug 15 22:10:46.528 API L2FIB Replay              00000000 00000000 M  - 
            Aug 15 22:10:46.528  Modify                       00000000 00010000 M  - 
            Aug 15 22:10:46.528  Action L2FIB MP Info Upd     00000000 c0400000 M  - 
            Aug 15 22:10:46.528  Action L2FIB Instance Upd    00002001 c0400000 M  - 
            Aug 15 22:10:46.528 API BGP nexthop update        00000000 00000002 M  - 
        ----------------------------------------------------------------------------
        EVPN ES Statistics
                    |Adv                             |Wdw                             
                    | Cnt Last Time          Last Arg| Cnt Last Time          Last Arg
                RT|   1 15/08 22:10:12.997 00000000|   0                    00000000
            LocalBMAC|   0                    00000000|   0                    00000000
                ESI|   1 15/08 22:10:26.616 00000001|   0                    00000000
            EAD/ES|   1 15/08 22:10:29.619 0000000a|   0                    00000000
            EAD/EVI|   6 15/08 22:10:26.616 0000000f|   0                    00000000
        MST-AG VPW|   0                    00000000|   0                    00000000
        DF ElectFW|  24 15/08 22:10:26.559 00000000|
            UpdateMAC|   0                    00000000|
        MacFlushPE|   0                    00000000|
        MacFlushCE|   0                    00000000|
            Instance|   0                    00000000|   0                    00000000
            MP Info|   0                    00000000|   0                    00000000
        ----------------------------------------------------------------------------
        Diagnostic ESI : N/A                     Interface Name : N/A
        Diagnostic Ifh : 0x00000000
        Diagnostic Flag: 0x00000043              DiagnosticES-RT: 0000.0000.0000
        Port Key       : 0x00006f76              MAC winner     : 1
        Number of EVIs : 12
        Recovery Timer : 30   (global)           Peering Timer  : 3    (global)  
        Carving Timer  : 0    (global)  
        RT Advertised  : 1                       ESI Advertised : 1
        MSTi state mask: 0x2001                  HRW MSTi Set   : 0x3
        ES EAD Pulse   : 0                       MP Advertised  : 0
        NVE AnycastVTEP: 0                       NVE Ingr-Replic: 0
        Peering Done   : 1                       Carving Done   : 1
        Inval/RedundFWD: 0x00000000/0x00000000
        Inval/Redund NH: 0x00000000/0x00000000
        Checkpoint Info:
            IF Type      : 1
            MSTi Mask    : 0x2001
            Nexthop Info :
            192.168.0.1 [MOD:P:00][1]
            192.168.0.3 [MOD:P:00][2]
        ES EAD Update  :
            Num RDs:     : 1

            RD: 192.168.0.1:6, Num RTs: 12      RT List:
                100:1, 100:2, 100:3, 100:4, 100:5, 
                100:6, 100:13, 100:14, 100:15, 100:16, 
                100:17, 100:18, 
        0001.00ff.010c.0001.000b Gi0/3/0/3                          192.168.0.1
                                                                    192.168.0.3
        ES to BGP Gates   : Ready
        ES to L2FIB Gates : O
        Main port         :
            Interface name : GigabitEthernet0/3/0/3
            Interface MAC  : 02d4.6fff.3c45
            IfHandle       : 0x018040c0
            State          : Up
            Redundancy     : Not Defined
        ESI type          : 0
            Value          : 01.0001.00ff.0b0c.000b
        ES Import RT      : 0100.01ff.0b00 (from ESI)
        Source MAC        : 0000.0000.0000 (N/A)
        Topology          :
            Operational    : MH, Single-active
            Configured     : Single-active (AApS) (default)
        Service Carving   : Auto-selection
            Multicast      : Disabled
        Peering Details   :
            192.168.0.1 [MOD:P:00][1]
            192.168.0.3 [MOD:P:00][2]

        Service Carving Results:
            Forwarders     : 18
            Elected        : 0
            Not Elected    : 0
        EVPN-VPWS Service Carving Results:
            Primary        : 6
            Backup         : 12
            Non-DF         : 0
        MAC Flushing mode : STP-TCN
        Peering timer     : 3 sec [not running]
        Recovery timer    : 30 sec [not running]
        Carving timer     : 0 sec [not running]
        Local SHG label   : 28238
        Remote SHG labels : 1
                    28426 : nexthop 192.168.0.3

        Object: EVPN ES
        Base info: version=0xdbdb0007, flags=0x0, type=7, reserved=0
        EVPN ES event history  [Num events: 22]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Aug 15 22:10:12.736  Create                       00000000 00000001 -  - 
            Aug 15 22:10:12.736 API Config Ifname Add         00000000 00000001 -  - 
            Aug 15 22:10:12.992 API Config Local RT           00000000 00000000 -  - 
            Aug 15 22:10:12.992  ES DB Bind                   00000000 00010001 M  - 
            Aug 15 22:10:12.992 API Config ESI complete       00000000 00000003 -  - 
            Aug 15 22:10:12.992 API Provision                 00000000 00000000 -  - 
            Aug 15 22:10:12.992 API BP Ifname delete          45138200 0aa6e9f8 M  - 
            Aug 15 22:10:26.432  Action Create RT             00000000 01000100 -  - 
            Aug 15 22:10:26.432  Action Advertise RT          00000000 00010001 -  - 
            Aug 15 22:10:26.432 API BP Ifname update          00000000 00060033 M  - 
            Aug 15 22:10:26.560 API BGP RID update            00000000 00011043 -  - 
            Aug 15 22:10:26.560  Action Advertise ESI         00000000 00010001 -  - 
            Aug 15 22:10:26.560  Action EAD/EVI               00000add 00000000 -  - 
            Aug 15 22:10:26.560  Action Peering Sequence      00000000 00000000 M  - 
            Aug 15 22:10:26.560 API Recv LSD Local SHGLabel   00000000 00006e4e -  - 
            Aug 15 22:10:29.504 API Peer Timer Expiry         8513800b 00000000 -  - 
            Aug 15 22:10:29.504  Action EAD/ES                00000add 000a6f4e M  - 
            Aug 15 22:10:46.528 API L2FIB Replay              00000000 00000000 M  - 
            Aug 15 22:10:46.528  Modify                       00000000 00010000 M  - 
            Aug 15 22:10:46.528  Action L2FIB MP Info Upd     00000000 c0400000 M  - 
            Aug 15 22:10:46.528  Action L2FIB Instance Upd    00002aab c0400000 M  - 
            Aug 15 22:10:46.528 API BGP nexthop update        00000000 00000002 M  - 
        ----------------------------------------------------------------------------
        EVPN ES Statistics
                    |Adv                             |Wdw                             
                    | Cnt Last Time          Last Arg| Cnt Last Time          Last Arg
                RT|   1 15/08 22:10:26.476 00000000|   0                    00000000
            LocalBMAC|   0                    00000000|   0                    00000000
                ESI|   1 15/08 22:10:26.616 00000001|   0                    00000000
            EAD/ES|   1 15/08 22:10:29.619 0000000a|   0                    00000000
            EAD/EVI|   0                    00000000|   0                    00000000
        MST-AG VPW|   0                    00000000|   0                    00000000
        DF ElectFW|  18 15/08 22:10:26.553 00000000|
            UpdateMAC|   0                    00000000|
        MacFlushPE|   0                    00000000|
        MacFlushCE|   0                    00000000|
            Instance|   0                    00000000|   0                    00000000
            MP Info|   0                    00000000|   0                    00000000
        ----------------------------------------------------------------------------
        Diagnostic ESI : N/A                     Interface Name : N/A
        Diagnostic Ifh : 0x00000000
        Diagnostic Flag: 0x00000043              DiagnosticES-RT: 0000.0000.0000
        Port Key       : 0x00006e4e              MAC winner     : 1
        Number of EVIs : 6
        Recovery Timer : 30   (global)           Peering Timer  : 3    (global)  
        Carving Timer  : 0    (global)  
        RT Advertised  : 1                       ESI Advertised : 1
        MSTi state mask: 0x2aab                  HRW MSTi Set   : 0x3
        ES EAD Pulse   : 0                       MP Advertised  : 0
        NVE AnycastVTEP: 0                       NVE Ingr-Replic: 0
        Peering Done   : 1                       Carving Done   : 1
        Inval/RedundFWD: 0x00000000/0x00000000
        Inval/Redund NH: 0x00000000/0x00000000
        Checkpoint Info:
            IF Type      : 1
            MSTi Mask    : 0x2aab
            Nexthop Info :
            192.168.0.1 [MOD:P:00][1]
            192.168.0.3 [MOD:P:00][2]
        ES EAD Update  :
            Num RDs:     : 1

            RD: 192.168.0.1:1, Num RTs: 6      RT List:
                100:4, 100:5, 100:6, 100:16, 100:17, 
                100:18, 
        0001.00ff.0116.0001.0015 BE21                               192.168.0.1
                                                                    192.168.0.3
        ES to BGP Gates   : Ready
        ES to L2FIB Gates : O
        Main port         :
            Interface name : Bundle-Ether21
            Interface MAC  : 02ef.afff.0e95
            IfHandle       : 0x00004190
            State          : Up
            Redundancy     : Active
        ESI type          : 0
            Value          : 01.0001.00ff.1516.0015
        ES Import RT      : 0100.01ff.1500 (from ESI)
        Source MAC        : 0000.0000.0000 (N/A)
        Topology          :
            Operational    : MH, Single-active
            Configured     : Single-active (AApS)
        Service Carving   : Auto-selection
            Multicast      : Disabled
        Peering Details   :
            192.168.0.1 [MOD:P:00][1]
            192.168.0.3 [MOD:P:00][2]

        Service Carving Results:
            Forwarders     : 18
            Elected        : 0
            Not Elected    : 0
        EVPN-VPWS Service Carving Results:
            Primary        : 0
            Backup         : 18
            Non-DF         : 0
        MAC Flushing mode : STP-TCN
        Peering timer     : 3 sec [not running]
        Recovery timer    : 30 sec [not running]
        Carving timer     : 0 sec [not running]
        Local SHG label   : 28537
        Remote SHG labels : 1
                    28427 : nexthop 192.168.0.3

        Object: EVPN ES
        Base info: version=0xdbdb0007, flags=0x0, type=7, reserved=0
        EVPN ES event history  [Num events: 27]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Aug 15 22:10:12.736  Create                       00000000 00000001 -  - 
            Aug 15 22:10:12.736 API Config Ifname Add         00000000 00000001 -  - 
            Aug 15 22:10:12.992  Action Advertise MAC         00000000 0000c016 -  - 
            Aug 15 22:10:12.992 API L2VPN RG MP Role          00000000 00000101 -  - 
            Aug 15 22:10:12.992 API Config Local RT           00000000 00000000 -  - 
            Aug 15 22:10:12.992  ES DB Bind                   00000000 00010001 M  - 
            Aug 15 22:10:12.992 API Config ESI complete       00000000 00000003 -  - 
            Aug 15 22:10:12.992  Action Withdraw MAC          00000000 0000c016 -  - 
            Aug 15 22:10:12.992  Mgr Withdraw BGP             00000000 c0060003 -  - 
            Aug 15 22:10:12.992 API Config LB mode            00000003 00000003 -  - 
            Aug 15 22:10:12.992 API Provision                 00000000 00000000 -  - 
            Aug 15 22:10:12.992 API BP Ifname delete          45138200 0aa715c0 M  - 
            Aug 15 22:10:26.432  Action Create RT             00000000 01000100 -  - 
            Aug 15 22:10:26.432  Action Advertise RT          00000000 00010001 -  - 
            Aug 15 22:10:26.432 API BP Ifname update          00000000 0006003b M  - 
            Aug 15 22:10:26.560 API BGP RID update            00000000 00011043 -  - 
            Aug 15 22:10:26.560  Action Advertise ESI         00000000 00010001 -  - 
            Aug 15 22:10:26.560  Action EAD/EVI               00000add 00000000 -  - 
            Aug 15 22:10:26.560  Action Peering Sequence      00000000 00000000 M  - 
            Aug 15 22:10:26.560 API Recv LSD Local SHGLabel   00000000 00006f79 -  - 
            Aug 15 22:10:29.504 API Peer Timer Expiry         8513800b 00000000 -  - 
            Aug 15 22:10:29.504  Action EAD/ES                00000add 000a6f79 M  - 
            Aug 15 22:10:46.528 API L2FIB Replay              00000000 00000000 M  - 
            Aug 15 22:10:46.528  Modify                       00000000 00010000 M  - 
            Aug 15 22:10:46.528  Action L2FIB MP Info Upd     00000000 c0400000 M  - 
            Aug 15 22:10:46.528  Action L2FIB Instance Upd    00002aab c0400000 M  - 
            Aug 15 22:10:46.528 API BGP nexthop update        00000000 00000002 M  - 
        ----------------------------------------------------------------------------
        EVPN ES Statistics
                    |Adv                             |Wdw                             
                    | Cnt Last Time          Last Arg| Cnt Last Time          Last Arg
                RT|   1 15/08 22:10:26.477 00000000|   0                    00000000
            LocalBMAC|   0                    00000000|   0                    00000000
                ESI|   1 15/08 22:10:26.616 00000001|   0                    00000000
            EAD/ES|   1 15/08 22:10:29.620 0000000a|   0                    00000000
            EAD/EVI|   0                    00000000|   0                    00000000
        MST-AG VPW|   0                    00000000|   0                    00000000
        DF ElectFW|  18 15/08 22:10:26.553 00000000|
            UpdateMAC|   0                    00000000|
        MacFlushPE|   0                    00000000|
        MacFlushCE|   0                    00000000|
            Instance|   0                    00000000|   0                    00000000
            MP Info|   0                    00000000|   0                    00000000
        ----------------------------------------------------------------------------
        Diagnostic ESI : N/A                     Interface Name : N/A
        Diagnostic Ifh : 0x00000000
        Diagnostic Flag: 0x00000043              DiagnosticES-RT: 0000.0000.0000
        Port Key       : 0x00006f79              MAC winner     : 1
        Number of EVIs : 6
        Recovery Timer : 30   (global)           Peering Timer  : 3    (global)  
        Carving Timer  : 0    (global)  
        RT Advertised  : 1                       ESI Advertised : 1
        MSTi state mask: 0x2aab                  HRW MSTi Set   : 0x3
        ES EAD Pulse   : 0                       MP Advertised  : 0
        NVE AnycastVTEP: 0                       NVE Ingr-Replic: 0
        Peering Done   : 1                       Carving Done   : 1
        Inval/RedundFWD: 0x00000000/0x00000000
        Inval/Redund NH: 0x00000000/0x00000000
        Checkpoint Info:
            IF Type      : 1
            MSTi Mask    : 0x2aab
            Nexthop Info :
            192.168.0.1 [MOD:P:00][1]
            192.168.0.3 [MOD:P:00][2]
        ES EAD Update  :
            Num RDs:     : 1

            RD: 192.168.0.1:7, Num RTs: 6      RT List:
                100:4, 100:5, 100:6, 100:16, 100:17, 
                100:18, 
        0100.01ff.b1d3.5500.0500 BE5                                192.168.0.1
                                                                    192.168.0.3
        ES to BGP Gates   : Ready
        ES to L2FIB Gates : O
        Main port         :
            Interface name : Bundle-Ether5
            Interface MAC  : 02ef.afff.0e91
            IfHandle       : 0x000040d0
            State          : Up
            Redundancy     : Active
        ESI type          : 1
            System-id      : 0001.05ff.7b02
            Port key       : 0005
        ES Import RT      : 0001.05ff.7b02 (from ESI)
        Source MAC        : 0201.05ff.7b02 (from ESI)
        Topology          :
            Operational    : MH, All-active
            Configured     : All-active (AApF) (default)
        Service Carving   : Auto-selection
            Multicast      : Disabled
        Peering Details   :
            192.168.0.1 [MOD:P:00][1]
            192.168.0.3 [MOD:P:00][2]

        Service Carving Results:
            Forwarders     : 9
            Elected        : 5
            Not Elected    : 4
        EVPN-VPWS Service Carving Results:
            Primary        : 0
            Backup         : 0
            Non-DF         : 0
        MAC Flushing mode : STP-TCN
        Peering timer     : 3 sec [not running]
        Recovery timer    : 30 sec [not running]
        Carving timer     : 0 sec [not running]
        Local SHG label   : 28532
        Remote SHG labels : 0

        Object: EVPN ES
        Base info: version=0xdbdb0007, flags=0x0, type=7, reserved=0
        EVPN ES event history  [Num events: 23]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Aug 15 22:10:12.736  Create                       00000000 00000001 -  - 
            Aug 15 22:10:12.736 API Config Ifname Add         00000000 00000001 -  - 
            Aug 15 22:10:12.992 API L2VPN RG MP Role          00000000 00000101 -  - 
            Aug 15 22:10:12.992 API Config Local RT           00000000 00000000 -  - 
            Aug 15 22:10:12.992 API Provision                 00000000 00000000 -  - 
            Aug 15 22:10:26.560  Action Create RT             00000000 000105ac -  - 
            Aug 15 22:10:26.560  Action Advertise RT          00000000 00010001 -  - 
            Aug 15 22:10:26.560  ES DB Bind                   00000000 00010001 M  - 
            Aug 15 22:10:26.560 API IM ESI BGP match          00000000 00001441 -  - 
            Aug 15 22:10:26.560 API BP Ifname update          00000000 000c0126 M  - 
            Aug 15 22:10:26.560 API BGP RID update            00000000 00011441 -  - 
            Aug 15 22:10:26.560 API IM ESI match              00000000 00001641 -  - 
            Aug 15 22:10:26.560  Action Advertise MAC         00000000 00000000 M  - 
            Aug 15 22:10:26.560  Action Advertise ESI         00000000 00010001 -  - 
            Aug 15 22:10:26.560  Action EAD/EVI               00000add 00000000 -  - 
            Aug 15 22:10:26.560  Action Peering Sequence      00000000 00000000 M  - 
            Aug 15 22:10:26.560 API Recv LSD Local SHGLabel   00000000 00006f74 -  - 
            Aug 15 22:10:29.504 API Peer Timer Expiry         8513800b 00000000 -  - 
            Aug 15 22:10:46.528 API L2FIB Replay              00000000 00000000 M  - 
            Aug 15 22:10:46.528  Modify                       00000000 00010000 -  - 
            Aug 15 22:10:46.528  Action L2FIB MP Info Upd     00000000 c0400000 M  - 
            Aug 15 22:10:46.528  Action L2FIB Instance Upd    00002aab c0400000 M  - 
            Aug 15 22:10:46.528 API BGP nexthop update        00000000 00000002 -  - 
        ----------------------------------------------------------------------------
        EVPN ES Statistics
                    |Adv                             |Wdw                             
                    | Cnt Last Time          Last Arg| Cnt Last Time          Last Arg
                RT|   1 15/08 22:10:26.563 00000000|   0                    00000000
            LocalBMAC|   9 15/08 22:10:26.616 0000000c|   0                    00000000
                ESI|   1 15/08 22:10:26.616 00000001|   0                    00000000
            EAD/ES|   0                    00000000|   0                    00000000
            EAD/EVI|   0                    00000000|   0                    00000000
        MST-AG VPW|   0                    00000000|   0                    00000000
        DF ElectFW|   9 15/08 22:10:26.566 00000000|
            UpdateMAC|   0                    00000000|
        MacFlushPE|   0                    00000000|
        MacFlushCE|   0                    00000000|
            Instance|   0                    00000000|   0                    00000000
            MP Info|   1 15/08 22:10:26.563 00000000|   0                    00000000
        ----------------------------------------------------------------------------
        Diagnostic ESI : N/A                     Interface Name : N/A
        Diagnostic Ifh : 0x00000000
        Diagnostic Flag: 0x00000641              DiagnosticES-RT: 0000.0000.0000
        Port Key       : 0x00006f74              MAC winner     : 1
        Number of EVIs : 3
        Recovery Timer : 30   (global)           Peering Timer  : 3    (global)  
        Carving Timer  : 0    (global)  
        RT Advertised  : 1                       ESI Advertised : 1
        MSTi state mask: 0x2aab                  HRW MSTi Set   : 0x3
        ES EAD Pulse   : 0                       MP Advertised  : 1
        NVE AnycastVTEP: 0                       NVE Ingr-Replic: 0
        Peering Done   : 1                       Carving Done   : 1
        Inval/RedundFWD: 0x00000000/0x00000000
        Inval/Redund NH: 0x00000000/0x00000000
        Checkpoint Info:
            IF Type      : 1
            MSTi Mask    : 0x2aab
            Nexthop Info :
            192.168.0.1 [MOD:P:00][1]
            192.168.0.3 [MOD:P:00][2]
        ES EAD Update  :
            Num RDs:     : 0

        0100.01ff.b2d4.5500.0600 BE6                                192.168.0.1
                                                                    192.168.0.3
        ES to BGP Gates   : Ready
        ES to L2FIB Gates : O
        Main port         :
            Interface name : Bundle-Ether6
            Interface MAC  : 02ef.afff.0e90
            IfHandle       : 0x000040f0
            State          : Up
            Redundancy     : Active
        ESI type          : 1
            System-id      : 0001.06ff.7b02
            Port key       : 0006
        ES Import RT      : 0001.06ff.7b02 (from ESI)
        Source MAC        : 0000.0000.0000 (N/A)
        Topology          :
            Operational    : MH, All-active
            Configured     : All-active (AApF) (default)
        Service Carving   : Auto-selection
            Multicast      : Disabled
        Peering Details   :
            192.168.0.1 [MOD:P:00][1]
            192.168.0.3 [MOD:P:00][2]

        Service Carving Results:
            Forwarders     : 99
            Elected        : 2
            Not Elected    : 4
        EVPN-VPWS Service Carving Results:
            Primary        : 93
            Backup         : 0
            Non-DF         : 0
        MAC Flushing mode : STP-TCN
        Peering timer     : 3 sec [not running]
        Recovery timer    : 30 sec [not running]
        Carving timer     : 0 sec [not running]
        Local SHG label   : 28533
        Remote SHG labels : 1
                    28418 : nexthop 192.168.0.3

        Object: EVPN ES
        Base info: version=0xdbdb0007, flags=0x0, type=7, reserved=0
        EVPN ES event history  [Num events: 25]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Aug 15 22:10:12.736  Create                       00000000 00000001 -  - 
            Aug 15 22:10:12.736 API Config Ifname Add         00000000 00000001 -  - 
            Aug 15 22:10:12.992  Action Advertise MAC         00000000 0000c016 -  - 
            Aug 15 22:10:12.992 API L2VPN RG MP Role          00000000 00000101 -  - 
            Aug 15 22:10:12.992 API Config Local RT           00000000 00000000 -  - 
            Aug 15 22:10:12.992 API Provision                 00000000 00000000 -  - 
            Aug 15 22:10:12.992 API BP Ifname delete          45138200 0aa6ab70 M  - 
            Aug 15 22:10:26.432  Action Create RT             00000000 000106ac -  - 
            Aug 15 22:10:26.432  Action Advertise RT          00000000 00010001 -  - 
            Aug 15 22:10:26.432  ES DB Bind                   00000000 00010001 M  - 
            Aug 15 22:10:26.432 API IM ESI BGP match          00000000 00001441 -  - 
            Aug 15 22:10:26.560 API BP Ifname update          00000000 00090003 M  - 
            Aug 15 22:10:26.560 API BGP RID update            00000000 00011441 -  - 
            Aug 15 22:10:26.560 API IM ESI match              00000000 00001641 -  - 
            Aug 15 22:10:26.560  Action Advertise ESI         00000000 00010001 -  - 
            Aug 15 22:10:26.560  Action EAD/EVI               00000add 0006000f -  - 
            Aug 15 22:10:26.560  Action Peering Sequence      00000000 00000000 M  - 
            Aug 15 22:10:26.560 API Recv LSD Local SHGLabel   00000000 00006f75 -  - 
            Aug 15 22:10:29.504 API Peer Timer Expiry         8513800b 00000000 -  - 
            Aug 15 22:10:29.504  Action EAD/ES                00000add 000a6f75 M  - 
            Aug 15 22:10:46.528 API L2FIB Replay              00000000 00000000 M  - 
            Aug 15 22:10:46.528  Modify                       00000000 00010000 -  - 
            Aug 15 22:10:46.528  Action L2FIB MP Info Upd     00000000 c0400000 M  - 
            Aug 15 22:10:46.528  Action L2FIB Instance Upd    00002aab c0400000 M  - 
            Aug 15 22:10:46.656 API BGP nexthop update        00000000 00000002 -  - 
        ----------------------------------------------------------------------------
        EVPN ES Statistics
                    |Adv                             |Wdw                             
                    | Cnt Last Time          Last Arg| Cnt Last Time          Last Arg
                RT|   1 15/08 22:10:26.475 00000000|   0                    00000000
            LocalBMAC|   0                    00000000|   0                    00000000
                ESI|   1 15/08 22:10:26.615 00000001|   0                    00000000
            EAD/ES|   1 15/08 22:10:29.531 0000000a|   0                    00000000
            EAD/EVI|   6 15/08 22:10:26.615 0000000f|   0                    00000000
        MST-AG VPW|   0                    00000000|   0                    00000000
        DF ElectFW|  99 15/08 22:10:26.563 00000000|
            UpdateMAC|   0                    00000000|
        MacFlushPE|   0                    00000000|
        MacFlushCE|   0                    00000000|
            Instance|   0                    00000000|   0                    00000000
            MP Info|   1 15/08 22:10:26.475 00000000|   0                    00000000
        ----------------------------------------------------------------------------
        Diagnostic ESI : N/A                     Interface Name : N/A
        Diagnostic Ifh : 0x00000000
        Diagnostic Flag: 0x00000641              DiagnosticES-RT: 0000.0000.0000
        Port Key       : 0x00006f75              MAC winner     : 1
        Number of EVIs : 15
        Recovery Timer : 30   (global)           Peering Timer  : 3    (global)  
        Carving Timer  : 0    (global)  
        RT Advertised  : 1                       ESI Advertised : 1
        MSTi state mask: 0x2aab                  HRW MSTi Set   : 0x3
        ES EAD Pulse   : 0                       MP Advertised  : 1
        NVE AnycastVTEP: 0                       NVE Ingr-Replic: 0
        Peering Done   : 1                       Carving Done   : 1
        Inval/RedundFWD: 0x00000000/0x00000000
        Inval/Redund NH: 0x00000000/0x00000000
        Checkpoint Info:
            IF Type      : 1
            MSTi Mask    : 0x2aab
            Nexthop Info :
            192.168.0.1 [MOD:P:00][1]
            192.168.0.3 [MOD:P:00][2]
        ES EAD Update  :
            Num RDs:     : 1

            RD: 192.168.0.1:2, Num RTs: 15      RT List:
                100:1, 100:2, 100:3, 100:4, 100:5, 
                100:6, 100:7, 100:8, 100:9, 100:13, 
                100:14, 100:15, 100:16, 100:17, 100:18, 
                
        0100.01ff.bddf.5500.1100 BE17                               192.168.0.1
                                                                    192.168.0.3
        ES to BGP Gates   : Ready
        ES to L2FIB Gates : O
        Main port         :
            Interface name : Bundle-Ether17
            Interface MAC  : 02ef.afff.0e97
            IfHandle       : 0x00004150
            State          : Up
            Redundancy     : Active
        ESI type          : 1
            System-id      : 0001.11ff.7b02
            Port key       : 0011
        ES Import RT      : 0001.11ff.7b02 (from ESI)
        Source MAC        : 0000.0000.0000 (N/A)
        Topology          :
            Operational    : MH, All-active
            Configured     : All-active (AApF) (default)
        Service Carving   : Auto-selection
            Multicast      : Disabled
        Peering Details   :
            192.168.0.1 [MOD:P:00][1]
            192.168.0.3 [MOD:P:00][2]

        Service Carving Results:
            Forwarders     : 6
            Elected        : 2
            Not Elected    : 4
        EVPN-VPWS Service Carving Results:
            Primary        : 0
            Backup         : 0
            Non-DF         : 0
        MAC Flushing mode : STP-TCN
        Peering timer     : 3 sec [not running]
        Recovery timer    : 30 sec [not running]
        Carving timer     : 0 sec [not running]
        Local SHG label   : 28535
        Remote SHG labels : 1
                    28428 : nexthop 192.168.0.3

        Object: EVPN ES
        Base info: version=0xdbdb0007, flags=0x0, type=7, reserved=0
        EVPN ES event history  [Num events: 24]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Aug 15 22:10:12.736  Create                       00000000 00000001 -  - 
            Aug 15 22:10:12.736 API Config Ifname Add         00000000 00000001 -  - 
            Aug 15 22:10:12.992  Action Advertise MAC         00000000 0000c016 -  - 
            Aug 15 22:10:12.992 API L2VPN RG MP Role          00000000 00000101 -  - 
            Aug 15 22:10:12.992 API Config Local RT           00000000 00000000 -  - 
            Aug 15 22:10:12.992 API Provision                 00000000 00000000 -  - 
            Aug 15 22:10:26.432  Action Create RT             00000000 000111ac -  - 
            Aug 15 22:10:26.432  Action Advertise RT          00000000 00010001 -  - 
            Aug 15 22:10:26.560  ES DB Bind                   00000000 00010001 M  - 
            Aug 15 22:10:26.560 API IM ESI BGP match          00000000 00001441 -  - 
            Aug 15 22:10:26.560 API BP Ifname update          00000000 00030003 M  - 
            Aug 15 22:10:26.560 API BGP RID update            00000000 00011441 -  - 
            Aug 15 22:10:26.560 API IM ESI match              00000000 00001641 -  - 
            Aug 15 22:10:26.560  Action Advertise ESI         00000000 00010001 -  - 
            Aug 15 22:10:26.560  Action EAD/EVI               00000add 0006000f -  - 
            Aug 15 22:10:26.560  Action Peering Sequence      00000000 00000000 M  - 
            Aug 15 22:10:26.560 API Recv LSD Local SHGLabel   00000000 00006f77 -  - 
            Aug 15 22:10:29.504 API Peer Timer Expiry         8513800b 00000000 -  - 
            Aug 15 22:10:29.504  Action EAD/ES                00000add 000a6f77 M  - 
            Aug 15 22:10:46.528 API L2FIB Replay              00000000 00000000 M  - 
            Aug 15 22:10:46.656  Modify                       00000000 00010000 -  - 
            Aug 15 22:10:46.656  Action L2FIB MP Info Upd     00000000 c0400000 M  - 
            Aug 15 22:10:46.656  Action L2FIB Instance Upd    00002aab c0400000 M  - 
            Aug 15 22:10:46.656 API BGP nexthop update        00000000 00000002 -  - 
        ----------------------------------------------------------------------------
        EVPN ES Statistics
                    |Adv                             |Wdw                             
                    | Cnt Last Time          Last Arg| Cnt Last Time          Last Arg
                RT|   1 15/08 22:10:26.554 00000000|   0                    00000000
            LocalBMAC|   0                    00000000|   0                    00000000
                ESI|   1 15/08 22:10:26.616 00000001|   0                    00000000
            EAD/ES|   1 15/08 22:10:29.555 0000000a|   0                    00000000
            EAD/EVI|   6 15/08 22:10:26.616 0000000f|   0                    00000000
        MST-AG VPW|   0                    00000000|   0                    00000000
        DF ElectFW|   6 15/08 22:10:26.559 00000000|
            UpdateMAC|   0                    00000000|
        MacFlushPE|   0                    00000000|
        MacFlushCE|   0                    00000000|
            Instance|   0                    00000000|   0                    00000000
            MP Info|   1 15/08 22:10:26.554 00000000|   0                    00000000
        ----------------------------------------------------------------------------
        Diagnostic ESI : N/A                     Interface Name : N/A
        Diagnostic Ifh : 0x00000000
        Diagnostic Flag: 0x00000641              DiagnosticES-RT: 0000.0000.0000
        Port Key       : 0x00006f77              MAC winner     : 1
        Number of EVIs : 6
        Recovery Timer : 30   (global)           Peering Timer  : 3    (global)  
        Carving Timer  : 0    (global)  
        RT Advertised  : 1                       ESI Advertised : 1
        MSTi state mask: 0x2aab                  HRW MSTi Set   : 0x3
        ES EAD Pulse   : 0                       MP Advertised  : 1
        NVE AnycastVTEP: 0                       NVE Ingr-Replic: 0
        Peering Done   : 1                       Carving Done   : 1
        Inval/RedundFWD: 0x00000000/0x00000000
        Inval/Redund NH: 0x00000000/0x00000000
        Checkpoint Info:
            IF Type      : 1
            MSTi Mask    : 0x2aab
            Nexthop Info :
            192.168.0.1 [MOD:P:00][1]
            192.168.0.3 [MOD:P:00][2]
        ES EAD Update  :
            Num RDs:     : 1

            RD: 192.168.0.1:4, Num RTs: 6      RT List:
                100:1, 100:2, 100:3, 100:13, 100:14, 
                100:15, 
        0100.01ff.bee0.5500.1200 BE18                               192.168.0.1
                                                                    192.168.0.3
        ES to BGP Gates   : Ready
        ES to L2FIB Gates : O
        Main port         :
            Interface name : Bundle-Ether18
            Interface MAC  : 02ef.afff.0e96
            IfHandle       : 0x00004170
            State          : Up
            Redundancy     : Active
        ESI type          : 1
            System-id      : 0001.12ff.7b02
            Port key       : 0012
        ES Import RT      : 0001.12ff.7b02 (from ESI)
        Source MAC        : 0000.0000.0000 (N/A)
        Topology          :
            Operational    : MH, All-active
            Configured     : All-active (AApF) (default)
        Service Carving   : Auto-selection
            Multicast      : Disabled
        Peering Details   :
            192.168.0.1 [MOD:P:00][1]
            192.168.0.3 [MOD:P:00][2]

        Service Carving Results:
            Forwarders     : 84
            Elected        : 0
            Not Elected    : 0
        EVPN-VPWS Service Carving Results:
            Primary        : 84
            Backup         : 0
            Non-DF         : 0
        MAC Flushing mode : STP-TCN
        Peering timer     : 3 sec [not running]
        Recovery timer    : 30 sec [not running]
        Carving timer     : 0 sec [not running]
        Local SHG label   : 28536
        Remote SHG labels : 1
                    28422 : nexthop 192.168.0.3

        Object: EVPN ES
        Base info: version=0xdbdb0007, flags=0x0, type=7, reserved=0
        EVPN ES event history  [Num events: 25]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Aug 15 22:10:12.736  Create                       00000000 00000001 -  - 
            Aug 15 22:10:12.736 API Config Ifname Add         00000000 00000001 -  - 
            Aug 15 22:10:12.992  Action Advertise MAC         00000000 0000c016 -  - 
            Aug 15 22:10:12.992 API L2VPN RG MP Role          00000000 00000101 -  - 
            Aug 15 22:10:12.992 API Config Local RT           00000000 00000000 -  - 
            Aug 15 22:10:12.992 API Provision                 00000000 00000000 -  - 
            Aug 15 22:10:12.992 API BP Ifname delete          45138200 0aa70f80 M  - 
            Aug 15 22:10:26.432  Action Create RT             00000000 000112ac -  - 
            Aug 15 22:10:26.432  Action Advertise RT          00000000 00010001 -  - 
            Aug 15 22:10:26.432  ES DB Bind                   00000000 00010001 M  - 
            Aug 15 22:10:26.432 API IM ESI BGP match          00000000 00001441 -  - 
            Aug 15 22:10:26.432 API BP Ifname update          00000000 0006003a M  - 
            Aug 15 22:10:26.560 API BGP RID update            00000000 00011441 -  - 
            Aug 15 22:10:26.560 API IM ESI match              00000000 00001641 -  - 
            Aug 15 22:10:26.560  Action Advertise ESI         00000000 00010001 -  - 
            Aug 15 22:10:26.560  Action EAD/EVI               00000add 00000000 -  - 
            Aug 15 22:10:26.560  Action Peering Sequence      00000000 00000000 M  - 
            Aug 15 22:10:26.560 API Recv LSD Local SHGLabel   00000000 00006f78 -  - 
            Aug 15 22:10:29.504 API Peer Timer Expiry         8513800b 00000000 -  - 
            Aug 15 22:10:29.504  Action EAD/ES                00000add 000a6f78 M  - 
            Aug 15 22:10:46.528 API L2FIB Replay              00000000 00000000 M  - 
            Aug 15 22:10:46.656  Modify                       00000000 00010000 -  - 
            Aug 15 22:10:46.656  Action L2FIB MP Info Upd     00000000 c0400000 M  - 
            Aug 15 22:10:46.656  Action L2FIB Instance Upd    00002aab c0400000 M  - 
            Aug 15 22:10:46.656 API BGP nexthop update        00000000 00000002 -  - 
        ----------------------------------------------------------------------------
        EVPN ES Statistics
                    |Adv                             |Wdw                             
                    | Cnt Last Time          Last Arg| Cnt Last Time          Last Arg
                RT|   1 15/08 22:10:26.476 00000000|   0                    00000000
            LocalBMAC|   0                    00000000|   0                    00000000
                ESI|   1 15/08 22:10:26.616 00000001|   0                    00000000
            EAD/ES|   1 15/08 22:10:29.531 0000000a|   0                    00000000
            EAD/EVI|   0                    00000000|   0                    00000000
        MST-AG VPW|   0                    00000000|   0                    00000000
        DF ElectFW|  84 15/08 22:10:26.553 00000000|
            UpdateMAC|   0                    00000000|
        MacFlushPE|   0                    00000000|
        MacFlushCE|   0                    00000000|
            Instance|   0                    00000000|   0                    00000000
            MP Info|   1 15/08 22:10:26.476 00000000|   0                    00000000
        ----------------------------------------------------------------------------
        Diagnostic ESI : N/A                     Interface Name : N/A
        Diagnostic Ifh : 0x00000000
        Diagnostic Flag: 0x00000641              DiagnosticES-RT: 0000.0000.0000
        Port Key       : 0x00006f78              MAC winner     : 1
        Number of EVIs : 6
        Recovery Timer : 30   (global)           Peering Timer  : 3    (global)  
        Carving Timer  : 0    (global)  
        RT Advertised  : 1                       ESI Advertised : 1
        MSTi state mask: 0x2aab                  HRW MSTi Set   : 0x3
        ES EAD Pulse   : 0                       MP Advertised  : 1
        NVE AnycastVTEP: 0                       NVE Ingr-Replic: 0
        Peering Done   : 1                       Carving Done   : 1
        Inval/RedundFWD: 0x00000000/0x00000000
        Inval/Redund NH: 0x00000000/0x00000000
        Checkpoint Info:
            IF Type      : 1
            MSTi Mask    : 0x2aab
            Nexthop Info :
            192.168.0.1 [MOD:P:00][1]
            192.168.0.3 [MOD:P:00][2]
        ES EAD Update  :
            Num RDs:     : 1

            RD: 192.168.0.1:3, Num RTs: 6      RT List:
                100:4, 100:5, 100:6, 100:16, 100:17, 
                100:18, 
        0100.01ff.c3e5.5500.1700 BE23                               192.168.0.1
                                                                    192.168.0.3
        ES to BGP Gates   : Ready
        ES to L2FIB Gates : O
        Main port         :
            Interface name : Bundle-Ether23
            Interface MAC  : 02ef.afff.0e94
            IfHandle       : 0x000041b0
            State          : Up
            Redundancy     : Active
        ESI type          : 1
            System-id      : 0001.17ff.7b02
            Port key       : 0017
        ES Import RT      : 0001.17ff.7b02 (from ESI)
        Source MAC        : 0000.0000.0000 (N/A)
        Topology          :
            Operational    : MH, All-active
            Configured     : All-active (AApF) (default)
        Service Carving   : Auto-selection
            Multicast      : Disabled
        Peering Details   :
            192.168.0.1 [MOD:P:00][1]
            192.168.0.3 [MOD:P:00][2]

        Service Carving Results:
            Forwarders     : 9
            Elected        : 0
            Not Elected    : 0
        EVPN-VPWS Service Carving Results:
            Primary        : 9
            Backup         : 0
            Non-DF         : 0
        MAC Flushing mode : STP-TCN
        Peering timer     : 3 sec [not running]
        Recovery timer    : 30 sec [not running]
        Carving timer     : 0 sec [not running]
        Local SHG label   : 28538
        Remote SHG labels : 1
                    28430 : nexthop 192.168.0.3

        Object: EVPN ES
        Base info: version=0xdbdb0007, flags=0x0, type=7, reserved=0
        EVPN ES event history  [Num events: 24]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Aug 15 22:10:12.736  Create                       00000000 00000001 -  - 
            Aug 15 22:10:12.736 API Config Ifname Add         00000000 00000001 -  - 
            Aug 15 22:10:12.992  Action Advertise MAC         00000000 0000c016 -  - 
            Aug 15 22:10:12.992 API L2VPN RG MP Role          00000000 00000101 -  - 
            Aug 15 22:10:12.992 API Config Local RT           00000000 00000000 -  - 
            Aug 15 22:10:12.992 API Provision                 00000000 00000000 -  - 
            Aug 15 22:10:26.560  Action Create RT             00000000 000117ac -  - 
            Aug 15 22:10:26.560  Action Advertise RT          00000000 00010001 -  - 
            Aug 15 22:10:26.560  ES DB Bind                   00000000 00010001 M  - 
            Aug 15 22:10:26.560 API IM ESI BGP match          00000000 00001441 -  - 
            Aug 15 22:10:26.560 API BP Ifname update          00000000 00090006 M  - 
            Aug 15 22:10:26.560 API BGP RID update            00000000 00011441 -  - 
            Aug 15 22:10:26.560 API IM ESI match              00000000 00001641 -  - 
            Aug 15 22:10:26.560  Action Advertise ESI         00000000 00010001 -  - 
            Aug 15 22:10:26.560  Action EAD/EVI               00000add 00000000 -  - 
            Aug 15 22:10:26.560  Action Peering Sequence      00000000 00000000 M  - 
            Aug 15 22:10:26.560 API Recv LSD Local SHGLabel   00000000 00006f7a -  - 
            Aug 15 22:10:29.504 API Peer Timer Expiry         8513800b 00000000 -  - 
            Aug 15 22:10:29.504  Action EAD/ES                00000add 000a6f7a M  - 
            Aug 15 22:10:46.528 API L2FIB Replay              00000000 00000000 M  - 
            Aug 15 22:10:46.656  Modify                       00000000 00010000 -  - 
            Aug 15 22:10:46.656  Action L2FIB MP Info Upd     00000000 c0400000 M  - 
            Aug 15 22:10:46.656  Action L2FIB Instance Upd    00002aab c0400000 M  - 
            Aug 15 22:10:46.656 API BGP nexthop update        00000000 00000002 -  - 
        ----------------------------------------------------------------------------
        EVPN ES Statistics
                    |Adv                             |Wdw                             
                    | Cnt Last Time          Last Arg| Cnt Last Time          Last Arg
                RT|   1 15/08 22:10:26.560 00000000|   0                    00000000
            LocalBMAC|   0                    00000000|   0                    00000000
                ESI|   1 15/08 22:10:26.616 00000001|   0                    00000000
            EAD/ES|   1 15/08 22:10:29.561 0000000a|   0                    00000000
            EAD/EVI|   0                    00000000|   0                    00000000
        MST-AG VPW|   0                    00000000|   0                    00000000
        DF ElectFW|   9 15/08 22:10:26.563 00000000|
            UpdateMAC|   0                    00000000|
        MacFlushPE|   0                    00000000|
        MacFlushCE|   0                    00000000|
            Instance|   0                    00000000|   0                    00000000
            MP Info|   1 15/08 22:10:26.560 00000000|   0                    00000000
        ----------------------------------------------------------------------------
        Diagnostic ESI : N/A                     Interface Name : N/A
        Diagnostic Ifh : 0x00000000
        Diagnostic Flag: 0x00000641              DiagnosticES-RT: 0000.0000.0000
        Port Key       : 0x00006f7a              MAC winner     : 1
        Number of EVIs : 3
        Recovery Timer : 30   (global)           Peering Timer  : 3    (global)  
        Carving Timer  : 0    (global)  
        RT Advertised  : 1                       ESI Advertised : 1
        MSTi state mask: 0x2aab                  HRW MSTi Set   : 0x3
        ES EAD Pulse   : 0                       MP Advertised  : 1
        NVE AnycastVTEP: 0                       NVE Ingr-Replic: 0
        Peering Done   : 1                       Carving Done   : 1
        Inval/RedundFWD: 0x00000000/0x00000000
        Inval/Redund NH: 0x00000000/0x00000000
        Checkpoint Info:
            IF Type      : 1
            MSTi Mask    : 0x2aab
            Nexthop Info :
            192.168.0.1 [MOD:P:00][1]
            192.168.0.3 [MOD:P:00][2]
        ES EAD Update  :
            Num RDs:     : 1

            RD: 192.168.0.1:5, Num RTs: 3      RT List:
                100:7, 100:8, 100:9, 
        N/A                      Gi0/3/0/0                          192.168.0.1
        ES to BGP Gates   : Ready
        ES to L2FIB Gates : Ready
        Main port         :
            Interface name : GigabitEthernet0/3/0/0
            Interface MAC  : 023f.e8ff.f581
            IfHandle       : 0x01804060
            State          : Up
            Redundancy     : Not Defined
        ESI type          : Invalid
        ES Import RT      : 0000.0000.0000 (Incomplete Configuration)
        Source MAC        : 0001.edff.9e9f (PBB BSA, no ESI)
        Topology          :
            Operational    : SH
            Configured     : Single-active (AApS) (default)
        Service Carving   : Auto-selection
            Multicast      : Disabled
        Peering Details   :
            192.168.0.1 [MOD:P:00][1]

        Service Carving Results:
            Forwarders     : 9
            Elected        : 9
            Not Elected    : 0
        EVPN-VPWS Service Carving Results:
            Primary        : 0
            Backup         : 0
            Non-DF         : 0
        MAC Flushing mode : STP-TCN
        Peering timer     : 3 sec [not running]
        Recovery timer    : 30 sec [not running]
        Carving timer     : 0 sec [not running]
        Local SHG label   : None
        Remote SHG labels : 0

        Object: EVPN ES
        Base info: version=0xdbdb0007, flags=0x0, type=7, reserved=0
        EVPN ES event history  [Num events: 14]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Aug 15 22:10:12.736  ES DB Bind                   00000000 00000001 -  - 
            Aug 15 22:10:12.736  Create                       00000000 00000001 -  - 
            Aug 15 22:10:12.736 API Config Ifname Add         00000000 00000001 -  - 
            Aug 15 22:10:12.992 API Config Local RT           00000000 00000000 -  - 
            Aug 15 22:10:12.992 API Provision                 00000000 00000000 -  - 
            Aug 15 22:10:26.560 API BP Ifname update          00000000 000c0126 M  - 
            Aug 15 22:10:26.560  Action Advertise RT          a5138016 0000ffff M  - 
            Aug 15 22:10:26.560  Action Peering Sequence      00000000 00008001 M  - 
            Aug 15 22:10:26.560 API BGP RID update            00000000 00010041 -  - 
            Aug 15 22:10:29.504 API Peer Timer Expiry         00000000 00000001 -  - 
            Aug 15 22:10:46.528  Action L2FIB Instance Upd    000f7fff 00000000 M  - 
            Aug 15 22:10:46.528  Action L2FIB MP Info Upd     00000000 00000304 M  - 
            Aug 15 22:10:46.528 API L2FIB Replay              00000000 00000000 -  - 
            Aug 15 22:10:46.528 API MAC Flush propagation     00000000 00000000 M  - 
        ----------------------------------------------------------------------------
        EVPN ES Statistics
                    |Adv                             |Wdw                             
                    | Cnt Last Time          Last Arg| Cnt Last Time          Last Arg
                RT|   2 15/08 22:10:26.570 a5138016|   0                    00000000
            LocalBMAC|   0                    00000000|   0                    00000000
                ESI|   0                    00000000|   0                    00000000
            EAD/ES|   0                    00000000|   0                    00000000
            EAD/EVI|   0                    00000000|   0                    00000000
        MST-AG VPW|   0                    00000000|   0                    00000000
        DF ElectFW|   9 15/08 22:10:26.566 00000000|
            UpdateMAC|   0                    00000000|
        MacFlushPE|   3 15/08 22:10:46.640 00030000|
        MacFlushCE|   3 15/08 22:10:46.640 00000001|
            Instance|   3 15/08 22:10:46.636 00007fff|   0                    00000000
            MP Info|   4 15/08 22:10:46.636 00000000|   0                    00000000
        ----------------------------------------------------------------------------
        Diagnostic ESI : N/A                     Interface Name : N/A
        Diagnostic Ifh : 0x00000000
        Diagnostic Flag: 0x00000041              DiagnosticES-RT: 0000.0000.0000
        Port Key       : 0x00000001              MAC winner     : 1
        Number of EVIs : 3
        Recovery Timer : 30   (global)           Peering Timer  : 3    (global)  
        Carving Timer  : 0    (global)  
        RT Advertised  : 0                       ESI Advertised : 0
        MSTi state mask: 0x7fff                  HRW MSTi Set   : 0x3
        ES EAD Pulse   : 0                       MP Advertised  : 1
        NVE AnycastVTEP: 0                       NVE Ingr-Replic: 0
        Peering Done   : 1                       Carving Done   : 1
        Inval/RedundFWD: 0x00000000/0x00000000
        Inval/Redund NH: 0x00000000/0x00000000
        Checkpoint Info:
            IF Type      : 1
            MSTi Mask    : 0x7fff
            Nexthop Info :
            192.168.0.1 [MOD:P:00][1]
        ES EAD Update  :
            Num RDs:     : 0

        N/A                      Gi0/4/0/0                          192.168.0.1
        ES to BGP Gates   : Ready
        ES to L2FIB Gates : Ready
        Main port         :
            Interface name : GigabitEthernet0/4/0/0
            Interface MAC  : 0259.cdff.85ea
            IfHandle       : 0x02004060
            State          : Up
            Redundancy     : Not Defined
        ESI type          : Invalid
        ES Import RT      : 0000.0000.0000 (Incomplete Configuration)
        Source MAC        : 0001.edff.9e9f (PBB BSA, no ESI)
        Topology          :
            Operational    : SH
            Configured     : Single-active (AApS) (default)
        Service Carving   : Auto-selection
            Multicast      : Disabled
        Peering Details   :
            192.168.0.1 [MOD:P:00][1]

        Service Carving Results:
            Forwarders     : 79
            Elected        : 6
            Not Elected    : 0
        EVPN-VPWS Service Carving Results:
            Primary        : 73
            Backup         : 0
            Non-DF         : 0
        MAC Flushing mode : STP-TCN
        Peering timer     : 3 sec [not running]
        Recovery timer    : 30 sec [not running]
        Carving timer     : 0 sec [not running]
        Local SHG label   : None
        Remote SHG labels : 0

        Object: EVPN ES
        Base info: version=0xdbdb0007, flags=0x0, type=7, reserved=0
        EVPN ES event history  [Num events: 15]
        ----------------------------------------------------------------------------
            Time                Event                         Flags      Flags      
            ====                =====                         =====      =====      
            Aug 15 22:10:12.736  ES DB Bind                   00000000 00000001 -  - 
            Aug 15 22:10:12.736  Create                       00000000 00000001 -  - 
            Aug 15 22:10:12.736 API Config Ifname Add         00000000 00000001 -  - 
            Aug 15 22:10:12.992 API Config Local RT           00000000 00000000 -  - 
            Aug 15 22:10:12.992 API Provision                 00000000 00000000 -  - 
            Aug 15 22:10:12.992 API BP Ifname delete          45138200 0aa62e60 M  - 
            Aug 15 22:10:26.560 API BP Ifname update          00000000 00030003 M  - 
            Aug 15 22:10:26.560  Action Advertise RT          a5138016 0000ffff M  - 
            Aug 15 22:10:26.560  Action Peering Sequence      00000000 00008001 M  - 
            Aug 15 22:10:26.560 API BGP RID update            00000000 00010041 -  - 
            Aug 15 22:10:29.376 API Peer Timer Expiry         00000000 00000001 -  - 
            Aug 15 22:10:46.528  Action L2FIB Instance Upd    000f7fff 00000000 M  - 
            Aug 15 22:10:46.528  Action L2FIB MP Info Upd     00000000 00000104 M  - 
            Aug 15 22:10:46.528 API L2FIB Replay              00000000 00000000 -  - 
            Aug 15 22:10:46.528 API MAC Flush propagation     00000000 00000000 M  - 
        ----------------------------------------------------------------------------
        EVPN ES Statistics
                    |Adv                             |Wdw                             
                    | Cnt Last Time          Last Arg| Cnt Last Time          Last Arg
                RT|   3 15/08 22:10:26.570 a5138016|   0                    00000000
            LocalBMAC|   0                    00000000|   0                    00000000
                ESI|   0                    00000000|   0                    00000000
            EAD/ES|   0                    00000000|   0                    00000000
            EAD/EVI|   0                    00000000|   0                    00000000
        MST-AG VPW|   0                    00000000|   0                    00000000
        DF ElectFW|  79 15/08 22:10:26.559 00000000|
            UpdateMAC|   0                    00000000|
        MacFlushPE|   0                    00000000|
        MacFlushCE|   4 15/08 22:10:46.641 00000001|
            Instance|   4 15/08 22:10:46.639 00007fff|   0                    00000000
            MP Info|   5 15/08 22:10:46.639 00000000|   0                    00000000
        ----------------------------------------------------------------------------
        Diagnostic ESI : N/A                     Interface Name : N/A
        Diagnostic Ifh : 0x00000000
        Diagnostic Flag: 0x00000041              DiagnosticES-RT: 0000.0000.0000
        Port Key       : 0x00000001              MAC winner     : 1
        Number of EVIs : 13
        Recovery Timer : 30   (global)           Peering Timer  : 3    (global)  
        Carving Timer  : 0    (global)  
        RT Advertised  : 0                       ESI Advertised : 0
        MSTi state mask: 0x7fff                  HRW MSTi Set   : 0x3
        ES EAD Pulse   : 0                       MP Advertised  : 1
        NVE AnycastVTEP: 0                       NVE Ingr-Replic: 0
        Peering Done   : 1                       Carving Done   : 1
        Inval/RedundFWD: 0x00000000/0x00000000
        Inval/Redund NH: 0x00000000/0x00000000
        Checkpoint Info:
            IF Type      : 1
            MSTi Mask    : 0x7fff
            Nexthop Info :
            192.168.0.1 [MOD:P:00][1]
        ES EAD Update  :
            Num RDs:     : 0

        RP/0/0/CPU0:PE1#
     '''}
    
    golden_parsed_output2 = {
        'segment_id': {
            '0001.00ff.0108.0001.0007': {
                'interface': {
                    'Bundle-Ether7': {
                        'next_hops': ['192.168.0.1', '192.168.0.3'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'O',
                        'main_port': {
                            'interface': 'Bundle-Ether7',
                            'interface_mac': '02ef.afff.0e8f',
                            'if_handle': '0x00004110',
                            'state': 'Standby',
                            'redundancy': 'Active',
                        },
                        'esi': {
                            'type': '0',
                            'value': '01.0001.00ff.0708.0007',
                        },
                        'es_import_rt': '0100.01ff.0700 (from ESI)',
                        'source_mac': '0000.0000.0000 (N/A)',
                        'topology': {
                            'operational': 'MH',
                            'configured': 'Port-Active',
                        },
                        'service_carving': 'Auto-selection',
                        'multicast': 'Disabled',
                        'peering_details': ['192.168.0.1 [MOD:P:00][1]', '192.168.0.3 [MOD:P:00][2]'],
                        'service_carving_results': {
                            'forwarders': 24,
                            'elected': {
                                'num_of_total': 0,
                            },
                            'not_elected': {
                                'num_of_total': 6,
                            },
                        },
                        'evpn_vpws_service_carving_results': {
                            'primary': '0',
                            'backup': '0',
                            'non_df': '18',
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '3',
                        'recovery_timer': '30',
                        'carving_timer': '0',
                        'local_shg_label': '28534',
                        'remote_shg_labels': {
                            '1': {
                                'label': {
                                    '28425': {
                                        'nexthop': '192.168.0.3',
                                    },
                                },
                            },
                        },
                        'object': {
                            'EVPN ES': {
                                'base_info': {
                                    'version': '0xdbdb0007',
                                    'flags': '0x0',
                                    'type': 7,
                                    'reserved': 0,
                                },
                                'num_events': 28,
                                'event_history': {
                                    1: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'Create',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    2: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'API Config Ifname Add',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    3: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    4: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API L2VPN RG MP Role',
                                        'flag_1': '00000000',
                                        'flag_2': '00000101',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    5: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Config Local RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    6: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'ES DB Bind',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    7: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Config ESI complete',
                                        'flag_1': '00000000',
                                        'flag_2': '00000003',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    8: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'Action Withdraw MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    9: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'Mgr Withdraw BGP',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0060003',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    10: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'Action Create RT',
                                        'flag_1': '00000000',
                                        'flag_2': '01000100',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    11: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'Action Advertise RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    12: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Config LB mode',
                                        'flag_1': '00000005',
                                        'flag_2': '00000005',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    13: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Provision',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    14: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API BP Ifname delete',
                                        'flag_1': '45138200',
                                        'flag_2': '0aa6b7f0',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    15: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API BP Ifname update',
                                        'flag_1': '00000000',
                                        'flag_2': '00030003',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    16: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API BGP RID update',
                                        'flag_1': '00000000',
                                        'flag_2': '00011043',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    17: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API IM MP | AToM state',
                                        'flag_1': '00000000',
                                        'flag_2': '00440004',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    18: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Advertise ESI',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    19: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action EAD/EVI',
                                        'flag_1': '00000add',
                                        'flag_2': '0006000f',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    20: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    21: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API Recv LSD Local SHGLabel',
                                        'flag_1': '00000000',
                                        'flag_2': '00006f76',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    22: {
                                        'time': 'Aug 15 22:10:29.504',
                                        'event': 'API Peer Timer Expiry',
                                        'flag_1': '8513800b',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    23: {
                                        'time': 'Aug 15 22:10:29.504',
                                        'event': 'Action EAD/ES',
                                        'flag_1': '00000add',
                                        'flag_2': '000a6f76',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    24: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'API L2FIB Replay',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    25: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Modify',
                                        'flag_1': '00000000',
                                        'flag_2': '00010000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    26: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0400000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    27: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Action L2FIB Instance Upd',
                                        'flag_1': '00002001',
                                        'flag_2': 'c0400000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    28: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'API BGP nexthop update',
                                        'flag_1': '00000000',
                                        'flag_2': '00000002',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                },
                                'statistics': {
                                    'rt': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:12.997',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'localbmac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'esi': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.616',
                                        'adv_last_arg': '00000001',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_es': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:29.619',
                                        'adv_last_arg': '0000000a',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_evi': {
                                        'adv_cnt': 6,
                                        'adv_last_time': '15/08 22:10:26.616',
                                        'adv_last_arg': '0000000f',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mst_ag_vpw': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'df_electfw': {
                                        'adv_cnt': 24,
                                        'adv_last_time': '15/08 22:10:26.559',
                                        'adv_last_arg': '00000000',
                                    },
                                    'updatemac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushpe': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushce': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'instance': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mp_info': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                },
                            },
                        },
                        'diagnostic_esi': 'N/A',
                        'interface_name': 'N/A',
                        'diagnostic_ifh': '0x00000000',
                        'diagnostic_flag': '0x00000043',
                        'diagnostic_es_rt': '0000.0000.0000',
                        'port_key': '0x00006f76',
                        'mac_winner': '1',
                        'number_of_evis': '12',
                        'recovery_timer_per_es': 'global',
                        'peering_timer_per_es': 'global',
                        'carving_timer_per_es': 'global',
                        'rt_advertised': '1',
                        'esi_advertised': '1',
                        'msti_state_mask': '0x2001',
                        'hrw_msti_set': '0x3',
                        'es_ead_pulse': '0',
                        'mp_advertised': '0',
                        'nve_anycastvtep': '0',
                        'nve_ingrreplic': '0',
                        'peering_done': '1',
                        'carving_done': '1',
                        'inval_redundfwd': '0x00000000/0x00000000',
                        'inval_redund_nh': '0x00000000/0x00000000',
                        'checkpoint_info': {
                            'if_type': 1,
                            'msti_mask': '0x2001',
                            'nexthop': ['192.168.0.1 [MOD:P:00][1]', '192.168.0.3 [MOD:P:00][2]'],
                        },
                        'es_ead_update': {
                            'num_rds': 1,
                            'rd': {
                                '192.168.0.1:6': {
                                    'num_rts': 12,
                                    'rt_list': ['100:1', '100:2', '100:3', '100:4', '100:5', '100:6', '100:13', '100:14', '100:15', '100:16', '100:17', '100:18'],
                                },
                            },
                        },
                    },
                },
            },
            '0001.00ff.010c.0001.000b': {
                'interface': {
                    'GigabitEthernet0/3/0/3': {
                        'next_hops': ['192.168.0.1', '192.168.0.3'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'O',
                        'main_port': {
                            'interface': 'GigabitEthernet0/3/0/3',
                            'interface_mac': '02d4.6fff.3c45',
                            'if_handle': '0x018040c0',
                            'state': 'Up',
                            'redundancy': 'Not Defined',
                        },
                        'esi': {
                            'type': '0',
                            'value': '01.0001.00ff.0b0c.000b',
                        },
                        'es_import_rt': '0100.01ff.0b00 (from ESI)',
                        'source_mac': '0000.0000.0000 (N/A)',
                        'topology': {
                            'operational': 'MH, Single-active',
                            'configured': 'Single-active (AApS) (default)',
                        },
                        'service_carving': 'Auto-selection',
                        'multicast': 'Disabled',
                        'peering_details': ['192.168.0.1 [MOD:P:00][1]', '192.168.0.3 [MOD:P:00][2]'],
                        'service_carving_results': {
                            'forwarders': 18,
                            'elected': {
                                'num_of_total': 0,
                            },
                            'not_elected': {
                                'num_of_total': 0,
                            },
                        },
                        'evpn_vpws_service_carving_results': {
                            'primary': '6',
                            'backup': '12',
                            'non_df': '0',
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '3',
                        'recovery_timer': '30',
                        'carving_timer': '0',
                        'local_shg_label': '28238',
                        'remote_shg_labels': {
                            '1': {
                                'label': {
                                    '28426': {
                                        'nexthop': '192.168.0.3',
                                    },
                                },
                            },
                        },
                        'object': {
                            'EVPN ES': {
                                'base_info': {
                                    'version': '0xdbdb0007',
                                    'flags': '0x0',
                                    'type': 7,
                                    'reserved': 0,
                                },
                                'num_events': 22,
                                'event_history': {
                                    29: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'Create',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    30: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'API Config Ifname Add',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    31: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Config Local RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    32: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'ES DB Bind',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    33: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Config ESI complete',
                                        'flag_1': '00000000',
                                        'flag_2': '00000003',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    34: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Provision',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    35: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API BP Ifname delete',
                                        'flag_1': '45138200',
                                        'flag_2': '0aa6e9f8',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    36: {
                                        'time': 'Aug 15 22:10:26.432',
                                        'event': 'Action Create RT',
                                        'flag_1': '00000000',
                                        'flag_2': '01000100',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    37: {
                                        'time': 'Aug 15 22:10:26.432',
                                        'event': 'Action Advertise RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    38: {
                                        'time': 'Aug 15 22:10:26.432',
                                        'event': 'API BP Ifname update',
                                        'flag_1': '00000000',
                                        'flag_2': '00060033',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    39: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API BGP RID update',
                                        'flag_1': '00000000',
                                        'flag_2': '00011043',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    40: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Advertise ESI',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    41: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action EAD/EVI',
                                        'flag_1': '00000add',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    42: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    43: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API Recv LSD Local SHGLabel',
                                        'flag_1': '00000000',
                                        'flag_2': '00006e4e',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    44: {
                                        'time': 'Aug 15 22:10:29.504',
                                        'event': 'API Peer Timer Expiry',
                                        'flag_1': '8513800b',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    45: {
                                        'time': 'Aug 15 22:10:29.504',
                                        'event': 'Action EAD/ES',
                                        'flag_1': '00000add',
                                        'flag_2': '000a6f4e',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    46: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'API L2FIB Replay',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    47: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Modify',
                                        'flag_1': '00000000',
                                        'flag_2': '00010000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    48: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0400000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    49: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Action L2FIB Instance Upd',
                                        'flag_1': '00002aab',
                                        'flag_2': 'c0400000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    50: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'API BGP nexthop update',
                                        'flag_1': '00000000',
                                        'flag_2': '00000002',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                },
                                'statistics': {
                                    'rt': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.476',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'localbmac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'esi': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.616',
                                        'adv_last_arg': '00000001',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_es': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:29.619',
                                        'adv_last_arg': '0000000a',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_evi': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mst_ag_vpw': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'df_electfw': {
                                        'adv_cnt': 18,
                                        'adv_last_time': '15/08 22:10:26.553',
                                        'adv_last_arg': '00000000',
                                    },
                                    'updatemac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushpe': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushce': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'instance': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mp_info': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                },
                            },
                        },
                        'diagnostic_esi': 'N/A',
                        'interface_name': 'N/A',
                        'diagnostic_ifh': '0x00000000',
                        'diagnostic_flag': '0x00000043',
                        'diagnostic_es_rt': '0000.0000.0000',
                        'port_key': '0x00006e4e',
                        'mac_winner': '1',
                        'number_of_evis': '6',
                        'recovery_timer_per_es': 'global',
                        'peering_timer_per_es': 'global',
                        'carving_timer_per_es': 'global',
                        'rt_advertised': '1',
                        'esi_advertised': '1',
                        'msti_state_mask': '0x2aab',
                        'hrw_msti_set': '0x3',
                        'es_ead_pulse': '0',
                        'mp_advertised': '0',
                        'nve_anycastvtep': '0',
                        'nve_ingrreplic': '0',
                        'peering_done': '1',
                        'carving_done': '1',
                        'inval_redundfwd': '0x00000000/0x00000000',
                        'inval_redund_nh': '0x00000000/0x00000000',
                        'checkpoint_info': {
                            'if_type': 1,
                            'msti_mask': '0x2aab',
                            'nexthop': ['192.168.0.1 [MOD:P:00][1]', '192.168.0.3 [MOD:P:00][2]'],
                        },
                        'es_ead_update': {
                            'num_rds': 1,
                            'rd': {
                                '192.168.0.1:1': {
                                    'num_rts': 6,
                                    'rt_list': ['100:4', '100:5', '100:6', '100:16', '100:17', '100:18'],
                                },
                            },
                        },
                    },
                },
            },
            '0001.00ff.0116.0001.0015': {
                'interface': {
                    'Bundle-Ether21': {
                        'next_hops': ['192.168.0.1', '192.168.0.3'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'O',
                        'main_port': {
                            'interface': 'Bundle-Ether21',
                            'interface_mac': '02ef.afff.0e95',
                            'if_handle': '0x00004190',
                            'state': 'Up',
                            'redundancy': 'Active',
                        },
                        'esi': {
                            'type': '0',
                            'value': '01.0001.00ff.1516.0015',
                        },
                        'es_import_rt': '0100.01ff.1500 (from ESI)',
                        'source_mac': '0000.0000.0000 (N/A)',
                        'topology': {
                            'operational': 'MH, Single-active',
                            'configured': 'Single-active (AApS)',
                        },
                        'service_carving': 'Auto-selection',
                        'multicast': 'Disabled',
                        'peering_details': ['192.168.0.1 [MOD:P:00][1]', '192.168.0.3 [MOD:P:00][2]'],
                        'service_carving_results': {
                            'forwarders': 18,
                            'elected': {
                                'num_of_total': 0,
                            },
                            'not_elected': {
                                'num_of_total': 0,
                            },
                        },
                        'evpn_vpws_service_carving_results': {
                            'primary': '0',
                            'backup': '18',
                            'non_df': '0',
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '3',
                        'recovery_timer': '30',
                        'carving_timer': '0',
                        'local_shg_label': '28537',
                        'remote_shg_labels': {
                            '1': {
                                'label': {
                                    '28427': {
                                        'nexthop': '192.168.0.3',
                                    },
                                },
                            },
                        },
                        'object': {
                            'EVPN ES': {
                                'base_info': {
                                    'version': '0xdbdb0007',
                                    'flags': '0x0',
                                    'type': 7,
                                    'reserved': 0,
                                },
                                'num_events': 27,
                                'event_history': {
                                    51: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'Create',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    52: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'API Config Ifname Add',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    53: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    54: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API L2VPN RG MP Role',
                                        'flag_1': '00000000',
                                        'flag_2': '00000101',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    55: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Config Local RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    56: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'ES DB Bind',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    57: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Config ESI complete',
                                        'flag_1': '00000000',
                                        'flag_2': '00000003',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    58: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'Action Withdraw MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    59: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'Mgr Withdraw BGP',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0060003',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    60: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Config LB mode',
                                        'flag_1': '00000003',
                                        'flag_2': '00000003',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    61: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Provision',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    62: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API BP Ifname delete',
                                        'flag_1': '45138200',
                                        'flag_2': '0aa715c0',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    63: {
                                        'time': 'Aug 15 22:10:26.432',
                                        'event': 'Action Create RT',
                                        'flag_1': '00000000',
                                        'flag_2': '01000100',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    64: {
                                        'time': 'Aug 15 22:10:26.432',
                                        'event': 'Action Advertise RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    65: {
                                        'time': 'Aug 15 22:10:26.432',
                                        'event': 'API BP Ifname update',
                                        'flag_1': '00000000',
                                        'flag_2': '0006003b',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    66: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API BGP RID update',
                                        'flag_1': '00000000',
                                        'flag_2': '00011043',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    67: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Advertise ESI',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    68: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action EAD/EVI',
                                        'flag_1': '00000add',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    69: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    70: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API Recv LSD Local SHGLabel',
                                        'flag_1': '00000000',
                                        'flag_2': '00006f79',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    71: {
                                        'time': 'Aug 15 22:10:29.504',
                                        'event': 'API Peer Timer Expiry',
                                        'flag_1': '8513800b',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    72: {
                                        'time': 'Aug 15 22:10:29.504',
                                        'event': 'Action EAD/ES',
                                        'flag_1': '00000add',
                                        'flag_2': '000a6f79',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    73: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'API L2FIB Replay',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    74: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Modify',
                                        'flag_1': '00000000',
                                        'flag_2': '00010000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    75: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0400000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    76: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Action L2FIB Instance Upd',
                                        'flag_1': '00002aab',
                                        'flag_2': 'c0400000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    77: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'API BGP nexthop update',
                                        'flag_1': '00000000',
                                        'flag_2': '00000002',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                },
                                'statistics': {
                                    'rt': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.477',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'localbmac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'esi': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.616',
                                        'adv_last_arg': '00000001',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_es': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:29.620',
                                        'adv_last_arg': '0000000a',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_evi': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mst_ag_vpw': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'df_electfw': {
                                        'adv_cnt': 18,
                                        'adv_last_time': '15/08 22:10:26.553',
                                        'adv_last_arg': '00000000',
                                    },
                                    'updatemac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushpe': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushce': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'instance': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mp_info': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                },
                            },
                        },
                        'diagnostic_esi': 'N/A',
                        'interface_name': 'N/A',
                        'diagnostic_ifh': '0x00000000',
                        'diagnostic_flag': '0x00000043',
                        'diagnostic_es_rt': '0000.0000.0000',
                        'port_key': '0x00006f79',
                        'mac_winner': '1',
                        'number_of_evis': '6',
                        'recovery_timer_per_es': 'global',
                        'peering_timer_per_es': 'global',
                        'carving_timer_per_es': 'global',
                        'rt_advertised': '1',
                        'esi_advertised': '1',
                        'msti_state_mask': '0x2aab',
                        'hrw_msti_set': '0x3',
                        'es_ead_pulse': '0',
                        'mp_advertised': '0',
                        'nve_anycastvtep': '0',
                        'nve_ingrreplic': '0',
                        'peering_done': '1',
                        'carving_done': '1',
                        'inval_redundfwd': '0x00000000/0x00000000',
                        'inval_redund_nh': '0x00000000/0x00000000',
                        'checkpoint_info': {
                            'if_type': 1,
                            'msti_mask': '0x2aab',
                            'nexthop': ['192.168.0.1 [MOD:P:00][1]', '192.168.0.3 [MOD:P:00][2]'],
                        },
                        'es_ead_update': {
                            'num_rds': 1,
                            'rd': {
                                '192.168.0.1:7': {
                                    'num_rts': 6,
                                    'rt_list': ['100:4', '100:5', '100:6', '100:16', '100:17', '100:18'],
                                },
                            },
                        },
                    },
                },
            },
            '0100.01ff.b1d3.5500.0500': {
                'interface': {
                    'Bundle-Ether5': {
                        'next_hops': ['192.168.0.1', '192.168.0.3'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'O',
                        'main_port': {
                            'interface': 'Bundle-Ether5',
                            'interface_mac': '02ef.afff.0e91',
                            'if_handle': '0x000040d0',
                            'state': 'Up',
                            'redundancy': 'Active',
                        },
                        'esi': {
                            'type': '1',
                        },
                        'systemid': '0001.05ff.7b02',
                        'port_key': '0x00006f74',
                        'es_import_rt': '0001.05ff.7b02 (from ESI)',
                        'source_mac': '0201.05ff.7b02 (from ESI)',
                        'topology': {
                            'operational': 'MH, All-active',
                            'configured': 'All-active (AApF) (default)',
                        },
                        'service_carving': 'Auto-selection',
                        'multicast': 'Disabled',
                        'peering_details': ['192.168.0.1 [MOD:P:00][1]', '192.168.0.3 [MOD:P:00][2]'],
                        'service_carving_results': {
                            'forwarders': 9,
                            'elected': {
                                'num_of_total': 5,
                            },
                            'not_elected': {
                                'num_of_total': 4,
                            },
                        },
                        'evpn_vpws_service_carving_results': {
                            'primary': '0',
                            'backup': '0',
                            'non_df': '0',
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '3',
                        'recovery_timer': '30',
                        'carving_timer': '0',
                        'local_shg_label': '28532',
                        'remote_shg_labels': {
                            '0': {
                            },
                        },
                        'object': {
                            'EVPN ES': {
                                'base_info': {
                                    'version': '0xdbdb0007',
                                    'flags': '0x0',
                                    'type': 7,
                                    'reserved': 0,
                                },
                                'num_events': 23,
                                'event_history': {
                                    78: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'Create',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    79: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'API Config Ifname Add',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    80: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API L2VPN RG MP Role',
                                        'flag_1': '00000000',
                                        'flag_2': '00000101',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    81: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Config Local RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    82: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Provision',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    83: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Create RT',
                                        'flag_1': '00000000',
                                        'flag_2': '000105ac',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    84: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Advertise RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    85: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'ES DB Bind',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    86: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API IM ESI BGP match',
                                        'flag_1': '00000000',
                                        'flag_2': '00001441',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    87: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API BP Ifname update',
                                        'flag_1': '00000000',
                                        'flag_2': '000c0126',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    88: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API BGP RID update',
                                        'flag_1': '00000000',
                                        'flag_2': '00011441',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    89: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API IM ESI match',
                                        'flag_1': '00000000',
                                        'flag_2': '00001641',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    90: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    91: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Advertise ESI',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    92: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action EAD/EVI',
                                        'flag_1': '00000add',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    93: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    94: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API Recv LSD Local SHGLabel',
                                        'flag_1': '00000000',
                                        'flag_2': '00006f74',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    95: {
                                        'time': 'Aug 15 22:10:29.504',
                                        'event': 'API Peer Timer Expiry',
                                        'flag_1': '8513800b',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    96: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'API L2FIB Replay',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    97: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Modify',
                                        'flag_1': '00000000',
                                        'flag_2': '00010000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    98: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0400000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    99: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Action L2FIB Instance Upd',
                                        'flag_1': '00002aab',
                                        'flag_2': 'c0400000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    100: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'API BGP nexthop update',
                                        'flag_1': '00000000',
                                        'flag_2': '00000002',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                },
                                'statistics': {
                                    'rt': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.563',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'localbmac': {
                                        'adv_cnt': 9,
                                        'adv_last_time': '15/08 22:10:26.616',
                                        'adv_last_arg': '0000000c',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'esi': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.616',
                                        'adv_last_arg': '00000001',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_es': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_evi': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mst_ag_vpw': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'df_electfw': {
                                        'adv_cnt': 9,
                                        'adv_last_time': '15/08 22:10:26.566',
                                        'adv_last_arg': '00000000',
                                    },
                                    'updatemac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushpe': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushce': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'instance': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mp_info': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.563',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                },
                            },
                        },
                        'diagnostic_esi': 'N/A',
                        'interface_name': 'N/A',
                        'diagnostic_ifh': '0x00000000',
                        'diagnostic_flag': '0x00000641',
                        'diagnostic_es_rt': '0000.0000.0000',
                        'mac_winner': '1',
                        'number_of_evis': '3',
                        'recovery_timer_per_es': 'global',
                        'peering_timer_per_es': 'global',
                        'carving_timer_per_es': 'global',
                        'rt_advertised': '1',
                        'esi_advertised': '1',
                        'msti_state_mask': '0x2aab',
                        'hrw_msti_set': '0x3',
                        'es_ead_pulse': '0',
                        'mp_advertised': '1',
                        'nve_anycastvtep': '0',
                        'nve_ingrreplic': '0',
                        'peering_done': '1',
                        'carving_done': '1',
                        'inval_redundfwd': '0x00000000/0x00000000',
                        'inval_redund_nh': '0x00000000/0x00000000',
                        'checkpoint_info': {
                            'if_type': 1,
                            'msti_mask': '0x2aab',
                            'nexthop': ['192.168.0.1 [MOD:P:00][1]', '192.168.0.3 [MOD:P:00][2]'],
                        },
                        'es_ead_update': {
                            'num_rds': 0,
                        },
                    },
                },
            },
            '0100.01ff.b2d4.5500.0600': {
                'interface': {
                    'Bundle-Ether6': {
                        'next_hops': ['192.168.0.1', '192.168.0.3'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'O',
                        'main_port': {
                            'interface': 'Bundle-Ether6',
                            'interface_mac': '02ef.afff.0e90',
                            'if_handle': '0x000040f0',
                            'state': 'Up',
                            'redundancy': 'Active',
                        },
                        'esi': {
                            'type': '1',
                        },
                        'systemid': '0001.06ff.7b02',
                        'port_key': '0x00006f75',
                        'es_import_rt': '0001.06ff.7b02 (from ESI)',
                        'source_mac': '0000.0000.0000 (N/A)',
                        'topology': {
                            'operational': 'MH, All-active',
                            'configured': 'All-active (AApF) (default)',
                        },
                        'service_carving': 'Auto-selection',
                        'multicast': 'Disabled',
                        'peering_details': ['192.168.0.1 [MOD:P:00][1]', '192.168.0.3 [MOD:P:00][2]'],
                        'service_carving_results': {
                            'forwarders': 99,
                            'elected': {
                                'num_of_total': 2,
                            },
                            'not_elected': {
                                'num_of_total': 4,
                            },
                        },
                        'evpn_vpws_service_carving_results': {
                            'primary': '93',
                            'backup': '0',
                            'non_df': '0',
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '3',
                        'recovery_timer': '30',
                        'carving_timer': '0',
                        'local_shg_label': '28533',
                        'remote_shg_labels': {
                            '1': {
                                'label': {
                                    '28418': {
                                        'nexthop': '192.168.0.3',
                                    },
                                },
                            },
                        },
                        'object': {
                            'EVPN ES': {
                                'base_info': {
                                    'version': '0xdbdb0007',
                                    'flags': '0x0',
                                    'type': 7,
                                    'reserved': 0,
                                },
                                'num_events': 25,
                                'event_history': {
                                    101: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'Create',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    102: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'API Config Ifname Add',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    103: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    104: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API L2VPN RG MP Role',
                                        'flag_1': '00000000',
                                        'flag_2': '00000101',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    105: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Config Local RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    106: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Provision',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    107: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API BP Ifname delete',
                                        'flag_1': '45138200',
                                        'flag_2': '0aa6ab70',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    108: {
                                        'time': 'Aug 15 22:10:26.432',
                                        'event': 'Action Create RT',
                                        'flag_1': '00000000',
                                        'flag_2': '000106ac',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    109: {
                                        'time': 'Aug 15 22:10:26.432',
                                        'event': 'Action Advertise RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    110: {
                                        'time': 'Aug 15 22:10:26.432',
                                        'event': 'ES DB Bind',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    111: {
                                        'time': 'Aug 15 22:10:26.432',
                                        'event': 'API IM ESI BGP match',
                                        'flag_1': '00000000',
                                        'flag_2': '00001441',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    112: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API BP Ifname update',
                                        'flag_1': '00000000',
                                        'flag_2': '00090003',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    113: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API BGP RID update',
                                        'flag_1': '00000000',
                                        'flag_2': '00011441',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    114: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API IM ESI match',
                                        'flag_1': '00000000',
                                        'flag_2': '00001641',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    115: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Advertise ESI',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    116: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action EAD/EVI',
                                        'flag_1': '00000add',
                                        'flag_2': '0006000f',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    117: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    118: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API Recv LSD Local SHGLabel',
                                        'flag_1': '00000000',
                                        'flag_2': '00006f75',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    119: {
                                        'time': 'Aug 15 22:10:29.504',
                                        'event': 'API Peer Timer Expiry',
                                        'flag_1': '8513800b',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    120: {
                                        'time': 'Aug 15 22:10:29.504',
                                        'event': 'Action EAD/ES',
                                        'flag_1': '00000add',
                                        'flag_2': '000a6f75',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    121: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'API L2FIB Replay',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    122: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Modify',
                                        'flag_1': '00000000',
                                        'flag_2': '00010000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    123: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0400000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    124: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Action L2FIB Instance Upd',
                                        'flag_1': '00002aab',
                                        'flag_2': 'c0400000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    125: {
                                        'time': 'Aug 15 22:10:46.656',
                                        'event': 'API BGP nexthop update',
                                        'flag_1': '00000000',
                                        'flag_2': '00000002',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                },
                                'statistics': {
                                    'rt': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.475',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'localbmac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'esi': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.615',
                                        'adv_last_arg': '00000001',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_es': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:29.531',
                                        'adv_last_arg': '0000000a',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_evi': {
                                        'adv_cnt': 6,
                                        'adv_last_time': '15/08 22:10:26.615',
                                        'adv_last_arg': '0000000f',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mst_ag_vpw': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'df_electfw': {
                                        'adv_cnt': 99,
                                        'adv_last_time': '15/08 22:10:26.563',
                                        'adv_last_arg': '00000000',
                                    },
                                    'updatemac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushpe': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushce': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'instance': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mp_info': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.475',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                },
                            },
                        },
                        'diagnostic_esi': 'N/A',
                        'interface_name': 'N/A',
                        'diagnostic_ifh': '0x00000000',
                        'diagnostic_flag': '0x00000641',
                        'diagnostic_es_rt': '0000.0000.0000',
                        'mac_winner': '1',
                        'number_of_evis': '15',
                        'recovery_timer_per_es': 'global',
                        'peering_timer_per_es': 'global',
                        'carving_timer_per_es': 'global',
                        'rt_advertised': '1',
                        'esi_advertised': '1',
                        'msti_state_mask': '0x2aab',
                        'hrw_msti_set': '0x3',
                        'es_ead_pulse': '0',
                        'mp_advertised': '1',
                        'nve_anycastvtep': '0',
                        'nve_ingrreplic': '0',
                        'peering_done': '1',
                        'carving_done': '1',
                        'inval_redundfwd': '0x00000000/0x00000000',
                        'inval_redund_nh': '0x00000000/0x00000000',
                        'checkpoint_info': {
                            'if_type': 1,
                            'msti_mask': '0x2aab',
                            'nexthop': ['192.168.0.1 [MOD:P:00][1]', '192.168.0.3 [MOD:P:00][2]'],
                        },
                        'es_ead_update': {
                            'num_rds': 1,
                            'rd': {
                                '192.168.0.1:2': {
                                    'num_rts': 15,
                                    'rt_list': ['100:1', '100:2', '100:3', '100:4', '100:5', '100:6', '100:7', '100:8', '100:9', '100:13', '100:14', '100:15', '100:16', '100:17', '100:18'],
                                },
                            },
                        },
                    },
                },
            },
            '0100.01ff.bddf.5500.1100': {
                'interface': {
                    'Bundle-Ether17': {
                        'next_hops': ['192.168.0.1', '192.168.0.3'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'O',
                        'main_port': {
                            'interface': 'Bundle-Ether17',
                            'interface_mac': '02ef.afff.0e97',
                            'if_handle': '0x00004150',
                            'state': 'Up',
                            'redundancy': 'Active',
                        },
                        'esi': {
                            'type': '1',
                        },
                        'systemid': '0001.11ff.7b02',
                        'port_key': '0x00006f77',
                        'es_import_rt': '0001.11ff.7b02 (from ESI)',
                        'source_mac': '0000.0000.0000 (N/A)',
                        'topology': {
                            'operational': 'MH, All-active',
                            'configured': 'All-active (AApF) (default)',
                        },
                        'service_carving': 'Auto-selection',
                        'multicast': 'Disabled',
                        'peering_details': ['192.168.0.1 [MOD:P:00][1]', '192.168.0.3 [MOD:P:00][2]'],
                        'service_carving_results': {
                            'forwarders': 6,
                            'elected': {
                                'num_of_total': 2,
                            },
                            'not_elected': {
                                'num_of_total': 4,
                            },
                        },
                        'evpn_vpws_service_carving_results': {
                            'primary': '0',
                            'backup': '0',
                            'non_df': '0',
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '3',
                        'recovery_timer': '30',
                        'carving_timer': '0',
                        'local_shg_label': '28535',
                        'remote_shg_labels': {
                            '1': {
                                'label': {
                                    '28428': {
                                        'nexthop': '192.168.0.3',
                                    },
                                },
                            },
                        },
                        'object': {
                            'EVPN ES': {
                                'base_info': {
                                    'version': '0xdbdb0007',
                                    'flags': '0x0',
                                    'type': 7,
                                    'reserved': 0,
                                },
                                'num_events': 24,
                                'event_history': {
                                    126: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'Create',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    127: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'API Config Ifname Add',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    128: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    129: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API L2VPN RG MP Role',
                                        'flag_1': '00000000',
                                        'flag_2': '00000101',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    130: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Config Local RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    131: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Provision',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    132: {
                                        'time': 'Aug 15 22:10:26.432',
                                        'event': 'Action Create RT',
                                        'flag_1': '00000000',
                                        'flag_2': '000111ac',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    133: {
                                        'time': 'Aug 15 22:10:26.432',
                                        'event': 'Action Advertise RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    134: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'ES DB Bind',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    135: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API IM ESI BGP match',
                                        'flag_1': '00000000',
                                        'flag_2': '00001441',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    136: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API BP Ifname update',
                                        'flag_1': '00000000',
                                        'flag_2': '00030003',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    137: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API BGP RID update',
                                        'flag_1': '00000000',
                                        'flag_2': '00011441',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    138: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API IM ESI match',
                                        'flag_1': '00000000',
                                        'flag_2': '00001641',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    139: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Advertise ESI',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    140: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action EAD/EVI',
                                        'flag_1': '00000add',
                                        'flag_2': '0006000f',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    141: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    142: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API Recv LSD Local SHGLabel',
                                        'flag_1': '00000000',
                                        'flag_2': '00006f77',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    143: {
                                        'time': 'Aug 15 22:10:29.504',
                                        'event': 'API Peer Timer Expiry',
                                        'flag_1': '8513800b',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    144: {
                                        'time': 'Aug 15 22:10:29.504',
                                        'event': 'Action EAD/ES',
                                        'flag_1': '00000add',
                                        'flag_2': '000a6f77',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    145: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'API L2FIB Replay',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    146: {
                                        'time': 'Aug 15 22:10:46.656',
                                        'event': 'Modify',
                                        'flag_1': '00000000',
                                        'flag_2': '00010000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    147: {
                                        'time': 'Aug 15 22:10:46.656',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0400000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    148: {
                                        'time': 'Aug 15 22:10:46.656',
                                        'event': 'Action L2FIB Instance Upd',
                                        'flag_1': '00002aab',
                                        'flag_2': 'c0400000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    149: {
                                        'time': 'Aug 15 22:10:46.656',
                                        'event': 'API BGP nexthop update',
                                        'flag_1': '00000000',
                                        'flag_2': '00000002',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                },
                                'statistics': {
                                    'rt': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.554',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'localbmac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'esi': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.616',
                                        'adv_last_arg': '00000001',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_es': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:29.555',
                                        'adv_last_arg': '0000000a',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_evi': {
                                        'adv_cnt': 6,
                                        'adv_last_time': '15/08 22:10:26.616',
                                        'adv_last_arg': '0000000f',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mst_ag_vpw': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'df_electfw': {
                                        'adv_cnt': 6,
                                        'adv_last_time': '15/08 22:10:26.559',
                                        'adv_last_arg': '00000000',
                                    },
                                    'updatemac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushpe': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushce': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'instance': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mp_info': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.554',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                },
                            },
                        },
                        'diagnostic_esi': 'N/A',
                        'interface_name': 'N/A',
                        'diagnostic_ifh': '0x00000000',
                        'diagnostic_flag': '0x00000641',
                        'diagnostic_es_rt': '0000.0000.0000',
                        'mac_winner': '1',
                        'number_of_evis': '6',
                        'recovery_timer_per_es': 'global',
                        'peering_timer_per_es': 'global',
                        'carving_timer_per_es': 'global',
                        'rt_advertised': '1',
                        'esi_advertised': '1',
                        'msti_state_mask': '0x2aab',
                        'hrw_msti_set': '0x3',
                        'es_ead_pulse': '0',
                        'mp_advertised': '1',
                        'nve_anycastvtep': '0',
                        'nve_ingrreplic': '0',
                        'peering_done': '1',
                        'carving_done': '1',
                        'inval_redundfwd': '0x00000000/0x00000000',
                        'inval_redund_nh': '0x00000000/0x00000000',
                        'checkpoint_info': {
                            'if_type': 1,
                            'msti_mask': '0x2aab',
                            'nexthop': ['192.168.0.1 [MOD:P:00][1]', '192.168.0.3 [MOD:P:00][2]'],
                        },
                        'es_ead_update': {
                            'num_rds': 1,
                            'rd': {
                                '192.168.0.1:4': {
                                    'num_rts': 6,
                                    'rt_list': ['100:1', '100:2', '100:3', '100:13', '100:14', '100:15'],
                                },
                            },
                        },
                    },
                },
            },
            '0100.01ff.bee0.5500.1200': {
                'interface': {
                    'Bundle-Ether18': {
                        'next_hops': ['192.168.0.1', '192.168.0.3'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'O',
                        'main_port': {
                            'interface': 'Bundle-Ether18',
                            'interface_mac': '02ef.afff.0e96',
                            'if_handle': '0x00004170',
                            'state': 'Up',
                            'redundancy': 'Active',
                        },
                        'esi': {
                            'type': '1',
                        },
                        'systemid': '0001.12ff.7b02',
                        'port_key': '0x00006f78',
                        'es_import_rt': '0001.12ff.7b02 (from ESI)',
                        'source_mac': '0000.0000.0000 (N/A)',
                        'topology': {
                            'operational': 'MH, All-active',
                            'configured': 'All-active (AApF) (default)',
                        },
                        'service_carving': 'Auto-selection',
                        'multicast': 'Disabled',
                        'peering_details': ['192.168.0.1 [MOD:P:00][1]', '192.168.0.3 [MOD:P:00][2]'],
                        'service_carving_results': {
                            'forwarders': 84,
                            'elected': {
                                'num_of_total': 0,
                            },
                            'not_elected': {
                                'num_of_total': 0,
                            },
                        },
                        'evpn_vpws_service_carving_results': {
                            'primary': '84',
                            'backup': '0',
                            'non_df': '0',
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '3',
                        'recovery_timer': '30',
                        'carving_timer': '0',
                        'local_shg_label': '28536',
                        'remote_shg_labels': {
                            '1': {
                                'label': {
                                    '28422': {
                                        'nexthop': '192.168.0.3',
                                    },
                                },
                            },
                        },
                        'object': {
                            'EVPN ES': {
                                'base_info': {
                                    'version': '0xdbdb0007',
                                    'flags': '0x0',
                                    'type': 7,
                                    'reserved': 0,
                                },
                                'num_events': 25,
                                'event_history': {
                                    150: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'Create',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    151: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'API Config Ifname Add',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    152: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    153: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API L2VPN RG MP Role',
                                        'flag_1': '00000000',
                                        'flag_2': '00000101',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    154: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Config Local RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    155: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Provision',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    156: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API BP Ifname delete',
                                        'flag_1': '45138200',
                                        'flag_2': '0aa70f80',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    157: {
                                        'time': 'Aug 15 22:10:26.432',
                                        'event': 'Action Create RT',
                                        'flag_1': '00000000',
                                        'flag_2': '000112ac',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    158: {
                                        'time': 'Aug 15 22:10:26.432',
                                        'event': 'Action Advertise RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    159: {
                                        'time': 'Aug 15 22:10:26.432',
                                        'event': 'ES DB Bind',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    160: {
                                        'time': 'Aug 15 22:10:26.432',
                                        'event': 'API IM ESI BGP match',
                                        'flag_1': '00000000',
                                        'flag_2': '00001441',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    161: {
                                        'time': 'Aug 15 22:10:26.432',
                                        'event': 'API BP Ifname update',
                                        'flag_1': '00000000',
                                        'flag_2': '0006003a',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    162: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API BGP RID update',
                                        'flag_1': '00000000',
                                        'flag_2': '00011441',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    163: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API IM ESI match',
                                        'flag_1': '00000000',
                                        'flag_2': '00001641',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    164: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Advertise ESI',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    165: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action EAD/EVI',
                                        'flag_1': '00000add',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    166: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    167: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API Recv LSD Local SHGLabel',
                                        'flag_1': '00000000',
                                        'flag_2': '00006f78',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    168: {
                                        'time': 'Aug 15 22:10:29.504',
                                        'event': 'API Peer Timer Expiry',
                                        'flag_1': '8513800b',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    169: {
                                        'time': 'Aug 15 22:10:29.504',
                                        'event': 'Action EAD/ES',
                                        'flag_1': '00000add',
                                        'flag_2': '000a6f78',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    170: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'API L2FIB Replay',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    171: {
                                        'time': 'Aug 15 22:10:46.656',
                                        'event': 'Modify',
                                        'flag_1': '00000000',
                                        'flag_2': '00010000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    172: {
                                        'time': 'Aug 15 22:10:46.656',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0400000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    173: {
                                        'time': 'Aug 15 22:10:46.656',
                                        'event': 'Action L2FIB Instance Upd',
                                        'flag_1': '00002aab',
                                        'flag_2': 'c0400000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    174: {
                                        'time': 'Aug 15 22:10:46.656',
                                        'event': 'API BGP nexthop update',
                                        'flag_1': '00000000',
                                        'flag_2': '00000002',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                },
                                'statistics': {
                                    'rt': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.476',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'localbmac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'esi': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.616',
                                        'adv_last_arg': '00000001',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_es': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:29.531',
                                        'adv_last_arg': '0000000a',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_evi': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mst_ag_vpw': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'df_electfw': {
                                        'adv_cnt': 84,
                                        'adv_last_time': '15/08 22:10:26.553',
                                        'adv_last_arg': '00000000',
                                    },
                                    'updatemac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushpe': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushce': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'instance': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mp_info': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.476',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                },
                            },
                        },
                        'diagnostic_esi': 'N/A',
                        'interface_name': 'N/A',
                        'diagnostic_ifh': '0x00000000',
                        'diagnostic_flag': '0x00000641',
                        'diagnostic_es_rt': '0000.0000.0000',
                        'mac_winner': '1',
                        'number_of_evis': '6',
                        'recovery_timer_per_es': 'global',
                        'peering_timer_per_es': 'global',
                        'carving_timer_per_es': 'global',
                        'rt_advertised': '1',
                        'esi_advertised': '1',
                        'msti_state_mask': '0x2aab',
                        'hrw_msti_set': '0x3',
                        'es_ead_pulse': '0',
                        'mp_advertised': '1',
                        'nve_anycastvtep': '0',
                        'nve_ingrreplic': '0',
                        'peering_done': '1',
                        'carving_done': '1',
                        'inval_redundfwd': '0x00000000/0x00000000',
                        'inval_redund_nh': '0x00000000/0x00000000',
                        'checkpoint_info': {
                            'if_type': 1,
                            'msti_mask': '0x2aab',
                            'nexthop': ['192.168.0.1 [MOD:P:00][1]', '192.168.0.3 [MOD:P:00][2]'],
                        },
                        'es_ead_update': {
                            'num_rds': 1,
                            'rd': {
                                '192.168.0.1:3': {
                                    'num_rts': 6,
                                    'rt_list': ['100:4', '100:5', '100:6', '100:16', '100:17', '100:18'],
                                },
                            },
                        },
                    },
                },
            },
            '0100.01ff.c3e5.5500.1700': {
                'interface': {
                    'Bundle-Ether23': {
                        'next_hops': ['192.168.0.1', '192.168.0.3'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'O',
                        'main_port': {
                            'interface': 'Bundle-Ether23',
                            'interface_mac': '02ef.afff.0e94',
                            'if_handle': '0x000041b0',
                            'state': 'Up',
                            'redundancy': 'Active',
                        },
                        'esi': {
                            'type': '1',
                        },
                        'systemid': '0001.17ff.7b02',
                        'port_key': '0x00006f7a',
                        'es_import_rt': '0001.17ff.7b02 (from ESI)',
                        'source_mac': '0000.0000.0000 (N/A)',
                        'topology': {
                            'operational': 'MH, All-active',
                            'configured': 'All-active (AApF) (default)',
                        },
                        'service_carving': 'Auto-selection',
                        'multicast': 'Disabled',
                        'peering_details': ['192.168.0.1 [MOD:P:00][1]', '192.168.0.3 [MOD:P:00][2]'],
                        'service_carving_results': {
                            'forwarders': 9,
                            'elected': {
                                'num_of_total': 0,
                            },
                            'not_elected': {
                                'num_of_total': 0,
                            },
                        },
                        'evpn_vpws_service_carving_results': {
                            'primary': '9',
                            'backup': '0',
                            'non_df': '0',
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '3',
                        'recovery_timer': '30',
                        'carving_timer': '0',
                        'local_shg_label': '28538',
                        'remote_shg_labels': {
                            '1': {
                                'label': {
                                    '28430': {
                                        'nexthop': '192.168.0.3',
                                    },
                                },
                            },
                        },
                        'object': {
                            'EVPN ES': {
                                'base_info': {
                                    'version': '0xdbdb0007',
                                    'flags': '0x0',
                                    'type': 7,
                                    'reserved': 0,
                                },
                                'num_events': 24,
                                'event_history': {
                                    175: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'Create',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    176: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'API Config Ifname Add',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    177: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'Action Advertise MAC',
                                        'flag_1': '00000000',
                                        'flag_2': '0000c016',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    178: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API L2VPN RG MP Role',
                                        'flag_1': '00000000',
                                        'flag_2': '00000101',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    179: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Config Local RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    180: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Provision',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    181: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Create RT',
                                        'flag_1': '00000000',
                                        'flag_2': '000117ac',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    182: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Advertise RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    183: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'ES DB Bind',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    184: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API IM ESI BGP match',
                                        'flag_1': '00000000',
                                        'flag_2': '00001441',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    185: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API BP Ifname update',
                                        'flag_1': '00000000',
                                        'flag_2': '00090006',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    186: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API BGP RID update',
                                        'flag_1': '00000000',
                                        'flag_2': '00011441',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    187: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API IM ESI match',
                                        'flag_1': '00000000',
                                        'flag_2': '00001641',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    188: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Advertise ESI',
                                        'flag_1': '00000000',
                                        'flag_2': '00010001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    189: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action EAD/EVI',
                                        'flag_1': '00000add',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    190: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    191: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API Recv LSD Local SHGLabel',
                                        'flag_1': '00000000',
                                        'flag_2': '00006f7a',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    192: {
                                        'time': 'Aug 15 22:10:29.504',
                                        'event': 'API Peer Timer Expiry',
                                        'flag_1': '8513800b',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    193: {
                                        'time': 'Aug 15 22:10:29.504',
                                        'event': 'Action EAD/ES',
                                        'flag_1': '00000add',
                                        'flag_2': '000a6f7a',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    194: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'API L2FIB Replay',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    195: {
                                        'time': 'Aug 15 22:10:46.656',
                                        'event': 'Modify',
                                        'flag_1': '00000000',
                                        'flag_2': '00010000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    196: {
                                        'time': 'Aug 15 22:10:46.656',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': 'c0400000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    197: {
                                        'time': 'Aug 15 22:10:46.656',
                                        'event': 'Action L2FIB Instance Upd',
                                        'flag_1': '00002aab',
                                        'flag_2': 'c0400000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    198: {
                                        'time': 'Aug 15 22:10:46.656',
                                        'event': 'API BGP nexthop update',
                                        'flag_1': '00000000',
                                        'flag_2': '00000002',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                },
                                'statistics': {
                                    'rt': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.560',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'localbmac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'esi': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.616',
                                        'adv_last_arg': '00000001',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_es': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:29.561',
                                        'adv_last_arg': '0000000a',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_evi': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mst_ag_vpw': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'df_electfw': {
                                        'adv_cnt': 9,
                                        'adv_last_time': '15/08 22:10:26.563',
                                        'adv_last_arg': '00000000',
                                    },
                                    'updatemac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushpe': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushce': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'instance': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mp_info': {
                                        'adv_cnt': 1,
                                        'adv_last_time': '15/08 22:10:26.560',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                },
                            },
                        },
                        'diagnostic_esi': 'N/A',
                        'interface_name': 'N/A',
                        'diagnostic_ifh': '0x00000000',
                        'diagnostic_flag': '0x00000641',
                        'diagnostic_es_rt': '0000.0000.0000',
                        'mac_winner': '1',
                        'number_of_evis': '3',
                        'recovery_timer_per_es': 'global',
                        'peering_timer_per_es': 'global',
                        'carving_timer_per_es': 'global',
                        'rt_advertised': '1',
                        'esi_advertised': '1',
                        'msti_state_mask': '0x2aab',
                        'hrw_msti_set': '0x3',
                        'es_ead_pulse': '0',
                        'mp_advertised': '1',
                        'nve_anycastvtep': '0',
                        'nve_ingrreplic': '0',
                        'peering_done': '1',
                        'carving_done': '1',
                        'inval_redundfwd': '0x00000000/0x00000000',
                        'inval_redund_nh': '0x00000000/0x00000000',
                        'checkpoint_info': {
                            'if_type': 1,
                            'msti_mask': '0x2aab',
                            'nexthop': ['192.168.0.1 [MOD:P:00][1]', '192.168.0.3 [MOD:P:00][2]'],
                        },
                        'es_ead_update': {
                            'num_rds': 1,
                            'rd': {
                                '192.168.0.1:5': {
                                    'num_rts': 3,
                                    'rt_list': ['100:7', '100:8', '100:9'],
                                },
                            },
                        },
                    },
                },
            },
            'N/A': {
                'interface': {
                    'GigabitEthernet0/3/0/0': {
                        'next_hops': ['192.168.0.1'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'Ready',
                        'main_port': {
                            'interface': 'GigabitEthernet0/3/0/0',
                            'interface_mac': '023f.e8ff.f581',
                            'if_handle': '0x01804060',
                            'state': 'Up',
                            'redundancy': 'Not Defined',
                        },
                        'esi': {
                            'type': 'Invalid',
                        },
                        'es_import_rt': '0000.0000.0000 (Incomplete Configuration)',
                        'source_mac': '0001.edff.9e9f (PBB BSA, no ESI)',
                        'topology': {
                            'operational': 'SH',
                            'configured': 'Single-active (AApS) (default)',
                        },
                        'service_carving': 'Auto-selection',
                        'multicast': 'Disabled',
                        'peering_details': ['192.168.0.1 [MOD:P:00][1]'],
                        'service_carving_results': {
                            'forwarders': 9,
                            'elected': {
                                'num_of_total': 9,
                            },
                            'not_elected': {
                                'num_of_total': 0,
                            },
                        },
                        'evpn_vpws_service_carving_results': {
                            'primary': '0',
                            'backup': '0',
                            'non_df': '0',
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '3',
                        'recovery_timer': '30',
                        'carving_timer': '0',
                        'local_shg_label': 'None',
                        'remote_shg_labels': {
                            '0': {
                            },
                        },
                        'object': {
                            'EVPN ES': {
                                'base_info': {
                                    'version': '0xdbdb0007',
                                    'flags': '0x0',
                                    'type': 7,
                                    'reserved': 0,
                                },
                                'num_events': 14,
                                'event_history': {
                                    199: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'ES DB Bind',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    200: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'Create',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    201: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'API Config Ifname Add',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    202: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Config Local RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    203: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Provision',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    204: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API BP Ifname update',
                                        'flag_1': '00000000',
                                        'flag_2': '000c0126',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    205: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Advertise RT',
                                        'flag_1': 'a5138016',
                                        'flag_2': '0000ffff',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    206: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': '00008001',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    207: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API BGP RID update',
                                        'flag_1': '00000000',
                                        'flag_2': '00010041',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    208: {
                                        'time': 'Aug 15 22:10:29.504',
                                        'event': 'API Peer Timer Expiry',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    209: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Action L2FIB Instance Upd',
                                        'flag_1': '000f7fff',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    210: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': '00000304',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    211: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'API L2FIB Replay',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    212: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'API MAC Flush propagation',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                },
                                'statistics': {
                                    'rt': {
                                        'adv_cnt': 2,
                                        'adv_last_time': '15/08 22:10:26.570',
                                        'adv_last_arg': 'a5138016',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'localbmac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'esi': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_es': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_evi': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mst_ag_vpw': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'df_electfw': {
                                        'adv_cnt': 9,
                                        'adv_last_time': '15/08 22:10:26.566',
                                        'adv_last_arg': '00000000',
                                    },
                                    'updatemac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushpe': {
                                        'adv_cnt': 3,
                                        'adv_last_time': '15/08 22:10:46.640',
                                        'adv_last_arg': '00030000',
                                    },
                                    'macflushce': {
                                        'adv_cnt': 3,
                                        'adv_last_time': '15/08 22:10:46.640',
                                        'adv_last_arg': '00000001',
                                    },
                                    'instance': {
                                        'adv_cnt': 3,
                                        'adv_last_time': '15/08 22:10:46.636',
                                        'adv_last_arg': '00007fff',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mp_info': {
                                        'adv_cnt': 4,
                                        'adv_last_time': '15/08 22:10:46.636',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                },
                            },
                        },
                        'diagnostic_esi': 'N/A',
                        'interface_name': 'N/A',
                        'diagnostic_ifh': '0x00000000',
                        'diagnostic_flag': '0x00000041',
                        'diagnostic_es_rt': '0000.0000.0000',
                        'port_key': '0x00000001',
                        'mac_winner': '1',
                        'number_of_evis': '3',
                        'recovery_timer_per_es': 'global',
                        'peering_timer_per_es': 'global',
                        'carving_timer_per_es': 'global',
                        'rt_advertised': '0',
                        'esi_advertised': '0',
                        'msti_state_mask': '0x7fff',
                        'hrw_msti_set': '0x3',
                        'es_ead_pulse': '0',
                        'mp_advertised': '1',
                        'nve_anycastvtep': '0',
                        'nve_ingrreplic': '0',
                        'peering_done': '1',
                        'carving_done': '1',
                        'inval_redundfwd': '0x00000000/0x00000000',
                        'inval_redund_nh': '0x00000000/0x00000000',
                        'checkpoint_info': {
                            'if_type': 1,
                            'msti_mask': '0x7fff',
                            'nexthop': ['192.168.0.1 [MOD:P:00][1]'],
                        },
                        'es_ead_update': {
                            'num_rds': 0,
                        },
                    },
                    'GigabitEthernet0/4/0/0': {
                        'next_hops': ['192.168.0.1'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'Ready',
                        'main_port': {
                            'interface': 'GigabitEthernet0/4/0/0',
                            'interface_mac': '0259.cdff.85ea',
                            'if_handle': '0x02004060',
                            'state': 'Up',
                            'redundancy': 'Not Defined',
                        },
                        'esi': {
                            'type': 'Invalid',
                        },
                        'es_import_rt': '0000.0000.0000 (Incomplete Configuration)',
                        'source_mac': '0001.edff.9e9f (PBB BSA, no ESI)',
                        'topology': {
                            'operational': 'SH',
                            'configured': 'Single-active (AApS) (default)',
                        },
                        'service_carving': 'Auto-selection',
                        'multicast': 'Disabled',
                        'peering_details': ['192.168.0.1 [MOD:P:00][1]'],
                        'service_carving_results': {
                            'forwarders': 79,
                            'elected': {
                                'num_of_total': 6,
                            },
                            'not_elected': {
                                'num_of_total': 0,
                            },
                        },
                        'evpn_vpws_service_carving_results': {
                            'primary': '73',
                            'backup': '0',
                            'non_df': '0',
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '3',
                        'recovery_timer': '30',
                        'carving_timer': '0',
                        'local_shg_label': 'None',
                        'remote_shg_labels': {
                            '0': {
                            },
                        },
                        'object': {
                            'EVPN ES': {
                                'base_info': {
                                    'version': '0xdbdb0007',
                                    'flags': '0x0',
                                    'type': 7,
                                    'reserved': 0,
                                },
                                'num_events': 15,
                                'event_history': {
                                    213: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'ES DB Bind',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    214: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'Create',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    215: {
                                        'time': 'Aug 15 22:10:12.736',
                                        'event': 'API Config Ifname Add',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    216: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Config Local RT',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    217: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API Provision',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    218: {
                                        'time': 'Aug 15 22:10:12.992',
                                        'event': 'API BP Ifname delete',
                                        'flag_1': '45138200',
                                        'flag_2': '0aa62e60',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    219: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API BP Ifname update',
                                        'flag_1': '00000000',
                                        'flag_2': '00030003',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    220: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Advertise RT',
                                        'flag_1': 'a5138016',
                                        'flag_2': '0000ffff',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    221: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'Action Peering Sequence',
                                        'flag_1': '00000000',
                                        'flag_2': '00008001',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    222: {
                                        'time': 'Aug 15 22:10:26.560',
                                        'event': 'API BGP RID update',
                                        'flag_1': '00000000',
                                        'flag_2': '00010041',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    223: {
                                        'time': 'Aug 15 22:10:29.376',
                                        'event': 'API Peer Timer Expiry',
                                        'flag_1': '00000000',
                                        'flag_2': '00000001',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    224: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Action L2FIB Instance Upd',
                                        'flag_1': '000f7fff',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    225: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'Action L2FIB MP Info Upd',
                                        'flag_1': '00000000',
                                        'flag_2': '00000104',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                    226: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'API L2FIB Replay',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': '-',
                                        'code_2': '-',
                                    },
                                    227: {
                                        'time': 'Aug 15 22:10:46.528',
                                        'event': 'API MAC Flush propagation',
                                        'flag_1': '00000000',
                                        'flag_2': '00000000',
                                        'code_1': 'M',
                                        'code_2': '-',
                                    },
                                },
                                'statistics': {
                                    'rt': {
                                        'adv_cnt': 3,
                                        'adv_last_time': '15/08 22:10:26.570',
                                        'adv_last_arg': 'a5138016',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'localbmac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'esi': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_es': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'ead_evi': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mst_ag_vpw': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'df_electfw': {
                                        'adv_cnt': 79,
                                        'adv_last_time': '15/08 22:10:26.559',
                                        'adv_last_arg': '00000000',
                                    },
                                    'updatemac': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushpe': {
                                        'adv_cnt': 0,
                                        'adv_last_arg': '00000000',
                                    },
                                    'macflushce': {
                                        'adv_cnt': 4,
                                        'adv_last_time': '15/08 22:10:46.641',
                                        'adv_last_arg': '00000001',
                                    },
                                    'instance': {
                                        'adv_cnt': 4,
                                        'adv_last_time': '15/08 22:10:46.639',
                                        'adv_last_arg': '00007fff',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                    'mp_info': {
                                        'adv_cnt': 5,
                                        'adv_last_time': '15/08 22:10:46.639',
                                        'adv_last_arg': '00000000',
                                        'wdw_cnt': 0,
                                        'wdw_last_arg': '00000000',
                                    },
                                },
                            },
                        },
                        'diagnostic_esi': 'N/A',
                        'interface_name': 'N/A',
                        'diagnostic_ifh': '0x00000000',
                        'diagnostic_flag': '0x00000041',
                        'diagnostic_es_rt': '0000.0000.0000',
                        'port_key': '0x00000001',
                        'mac_winner': '1',
                        'number_of_evis': '13',
                        'recovery_timer_per_es': 'global',
                        'peering_timer_per_es': 'global',
                        'carving_timer_per_es': 'global',
                        'rt_advertised': '0',
                        'esi_advertised': '0',
                        'msti_state_mask': '0x7fff',
                        'hrw_msti_set': '0x3',
                        'es_ead_pulse': '0',
                        'mp_advertised': '1',
                        'nve_anycastvtep': '0',
                        'nve_ingrreplic': '0',
                        'peering_done': '1',
                        'carving_done': '1',
                        'inval_redundfwd': '0x00000000/0x00000000',
                        'inval_redund_nh': '0x00000000/0x00000000',
                        'checkpoint_info': {
                            'if_type': 1,
                            'msti_mask': '0x7fff',
                            'nexthop': ['192.168.0.1 [MOD:P:00][1]'],
                        },
                        'es_ead_update': {
                            'num_rds': 0,
                        },
                    },
                },
            },
        },
    }
    
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowEvpnEthernetSegmentPrivate(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowEvpnEthernetSegmentPrivate(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)
    
    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowEvpnEthernetSegmentPrivate(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output2)

if __name__ == '__main__':
    unittest.main()