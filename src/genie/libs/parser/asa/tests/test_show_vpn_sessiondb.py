import unittest
from unittest.mock import Mock

# PyATS
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.asa.show_vpn_sessiondb import (ShowVPNSessionDBSummary)

# ============================================
# unit test for 'show vpn-sessiondb summary'
# =============================================
class TestShowVpnSessionDBSummary(unittest.TestCase):
    '''
       unit test for show vpn-sessiondb summary
    '''
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    maxDiff = None
    golden_parsed_output = {
        'device_load': 1,
        'device_total_vpn_capacity': 250,
        'ikev1_ipsec_l2tp_ip_sec': {
            'active': 2,
            'cumulative': 2,
            'peak_concurrent': 2,
        },
        'load_balancing_encryption': {
            'active': 0,
            'cumulative': 6,
            'peak_concurrent': 1,
        },
        'total_active_and_inactive': 2,
        'total_cumulative': 8,
    }

    golden_output = {'execute.return_value': '''
        vASA-VPN-20#show vpn-sessiondb summary 

        show vpn-sessiondb summary
        ---------------------------------------------------------------------------
        VPN Session Summary                                                        
        ---------------------------------------------------------------------------
                                    Active : Cumulative : Peak Concur : Inactive
                                    ----------------------------------------------
        IKEv1 IPsec/L2TP IPsec       :      2 :          2 :           2
        Load Balancing(Encryption)   :      0 :          6 :           1
        ---------------------------------------------------------------------------
        Total Active and Inactive    :      2             Total Cumulative :      8
        Device Total VPN Capacity    :    250
        Device Load                  :     1%
          '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVPNSessionDBSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        route_obj = ShowVPNSessionDBSummary(device=self.device)
        parsed_output = route_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()