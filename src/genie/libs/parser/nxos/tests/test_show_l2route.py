import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.nxos.show_l2route import ShowL2routeEvpnMac

# =========================================
#  show l2route evpn mac all
# =========================================
class test_show_l2route_evpn_mac(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_output = {'execute.return_value': '''
        N95_1# sh l2route evpn mac all

        Flags -(Rmac):Router MAC (Stt):Static (L):Local (R):Remote (V):vPC link 
        (Dup):Duplicate (Spl):Split (Rcv):Recv (AD):Auto-Delete (D):Del Pending
        (S):Stale (C):Clear, (Ps):Peer Sync (O):Re-Originated (Nho):NH-Override
        (Pf):Permanently-Frozen

        Topology    Mac Address    Prod   Flags         Seq No     Next-Hops      
        ----------- -------------- ------ ------------- ---------- ----------------
        100         fa16.3e59.d0b2 BGP    SplRcv        0          93.1.1.1       
        100         fa16.3ec1.a96f Local  L,            0          Eth1/4         
        1000        5e01.8002.0007 VXLAN  Rmac          0          93.1.1.1     
    '''}

    golden_parsed_output = {
        'topology':
            {'100':
                {'mac_address':
                    {'fa16.3e59.d0b2':
                        {'flags': 'SplRcv',
                         'next_hops': '93.1.1.1',
                         'prod': 'BGP',
                         'seq_no': '0'},
                     'fa16.3ec1.a96f':
                        {'flags': 'L,',
                         'next_hops': 'Eth1/4',
                         'prod': 'Local',
                         'seq_no': '0'}}},
             '1000':
                {'mac_address':
                    {'5e01.8002.0007':
                        {'flags': 'Rmac',
                         'next_hops': '93.1.1.1',
                         'prod': 'VXLAN',
                         'seq_no': '0'}
                    }
                }
            }
        }

    def test_show_l2route_evpn_mac(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowL2routeEvpnMac(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty_output(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2routeEvpnMac(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()