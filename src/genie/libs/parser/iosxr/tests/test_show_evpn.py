
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_evpn
from genie.libs.parser.iosxr.show_evpn import (ShowEvpnEviMac,
                                               ShowEvpnEviMacPrivate)

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
                        'esi_port_key': 0,
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
                    '001b.0100.0001': {
                        'next_hop': 'N/A',
                        'label': 24014,
                        'ip_address': '7.7.7.8',
                        'ethernet_segment': '0000.0000.0000.0000.0000',
                        'source': 'Local',
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
        001b.0100.0001 N/A                                     24014    7      
        IP Address   : 7.7.7.8
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

if __name__ == '__main__':
    unittest.main()