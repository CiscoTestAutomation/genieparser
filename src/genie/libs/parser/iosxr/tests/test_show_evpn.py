
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
                'encap': 'N/A',
                'mac_address': '0000.0000.0000',
                'ip_address': '::',
                'next_hop': 'Local',
                'label': 0,
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
                'encap': 'N/A',
                'mac_address': '0000.0000.0000',
                'ip_address': '::',
                'next_hop': 'Local',
                'label': 0,
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
#  Unit test for 'show evpn evi mac'
# ===================================================

class test_show_evpn_evi_mac_private(unittest.TestCase):

    '''Unit test for 'show evpn evi mac private'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vpn_id': {
            65535: {
                'encap': 'N/A',
                'mac_address': '0000.0000.0000',
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
                'object': 'EVPN MAC',
                'base_info': {
                    'version': '0xdbdb0008',
                    'flags': '0x4000',
                    'type': 8,
                    'reserved': 0,
                },
                'num_events': 0,
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

if __name__ == '__main__':
    unittest.main()