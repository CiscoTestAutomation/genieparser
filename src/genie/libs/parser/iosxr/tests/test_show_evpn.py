
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_evpn
from genie.libs.parser.iosxr.show_evpn import (ShowEvpnEthernetSegmentDetail)


# ===================================================
#  Unit test for 'show evpn ethernet-segment detail'
# ===================================================

class test_show_evpn_ethernet_segment_detail(unittest.TestCase):

    '''Unit test for 'show evpn ethernet-segment detail'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'segment_id': {
            '0210.0300.9e00.0210.0000': {
                'interface': {
                    'GigabitEthernet0/3/0/0': {
                        'next_hops': ['1.100.100.100', '2.100.100.100'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'Ready',
                        'main_port': {
                            'interface': 'GigabitEthernet0/3/0/0',
                            'if_handle': '0x1800300',
                            'state': 'Up',
                            'redundancy': 'Not Defined',
                        },
                        'source_mac': '0001.ed9e.0001 (PBB BSA)',
                        'topology': {
                            'operational': 'MHN',
                            'configured': 'A/A per service (default)',
                        },
                        'primary_services': 'Auto-selection',
                        'secondary_services': 'Auto-selection',
                        'service_carving_results': {
                            'bridge_ports': 3,
                            'elected': 0,
                            'not_elected': 3,
                            'i_sid_ne': '1450101, 1650205, 1850309',
                        },
                        'mac_flushing_mode': 'STP-TCN',
                        'peering_timer': '45 sec [not running]',
                        'recovery_timer': '20 sec [not running]',
                        'flush_again_timer': '60 sec',
                    },
                },
            },
            'be01.0300.be01.ce00.0001': {
                'interface': {
                    'BE1': {
                        'next_hops': ['1.100.100.100', '2.100.100.100'],
                        'es_to_bgp_gates': 'Ready',
                        'es_to_l2fib_gates': 'Ready',
                        'main_port': {
                            'interface': 'Bundle-Ether1',
                            'if_handle': '0x000480',
                            'state': 'Up',
                            'redundancy': 'Active',
                        },
                        'source_mac': '0024.be01.ce00 (Local)',
                        'topology': {
                            'operational': 'MHN',
                            'configured': 'A/A per flow (default)',
                        },
                        'primary_services': 'Auto-selection',
                        'secondary_services': 'Auto-selection',
                        'service_carving_results': {
                            'bridge_ports': 3,
                            'elected': 3,
                            'i_sid_e': '1450102, 1650206, 1850310',
                            'not_elected': 0,
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
        0210.0300.9e00.0210.0000 Gi0/3/0/0      1.100.100.100                           
                                                2.100.100.100                           
        ES to BGP Gates   : Ready
        ES to L2FIB Gates : Ready
        Main port         :
            Interface name : GigabitEthernet0/3/0/0
            IfHandle       : 0x1800300
            State          : Up
            Redundancy     : Not Defined
        Source MAC        : 0001.ed9e.0001 (PBB BSA)
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

        be01.0300.be01.ce00.0001 BE1            1.100.100.100                           
                                                2.100.100.100                           
        ES to BGP Gates   : Ready
        ES to L2FIB Gates : Ready
        Main port         :
            Interface name : Bundle-Ether1
            IfHandle       : 0x000480
            State          : Up
            Redundancy     : Active
        Source MAC        : 0024.be01.ce00 (Local)
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

if __name__ == '__main__':
    unittest.main()