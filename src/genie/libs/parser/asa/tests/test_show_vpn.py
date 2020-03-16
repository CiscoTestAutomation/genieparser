import unittest
from unittest.mock import Mock

# PyATS
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.asa.show_vpn import ShowVPNLoadBalancing

# ============================================
# unit test for 'show vpn load-balancing'
# =============================================
class TestShowVPN(unittest.TestCase):
    '''
       unit test for show vpn load-balancing
    '''
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
 
    golden_parsed_output = {
    }

    golden_output = {'execute.return_value': '''
        vASA-VPN-20#show vpn load-balancing
        --------------------------------------------------------------------------
        Status     Role     Failover   Encryption   Peers     Cluster IP        
        --------------------------------------------------------------------------
        Enabled    Master   n/a        Enabled          1     cluster1

        Peers:
        --------------------------------------------------------------------------
        Role    Pri  Model             Load-Balancing Version  Public IP         
        --------------------------------------------------------------------------
        Master    5  ASA-VASA                               4  10.246.0.1*
        Backup    5  ASA-VASA                               4  10.246.0.2

        Total License Load:
        --------------------------------------------------------------------------
        AnyConnect Premium/Essentials        Other VPN         Public IP         
        -----------------------------   ---------------------                    
        Limit    Used   Load          Limit    Used   Load                     
        --------------------------------------------------------------------------
            250       0      0%           250       2      1%  10.246.0.1*
        0       0      0%             0       0      0%  10.246.0.2
          '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVPNLoadBalancing(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        route_obj = ShowVPNLoadBalancing(device=self.device)
        parsed_output = route_obj.parse()
        from genie.libs.parser.utils.common import format_output
        print(format_output(parsed_output))
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()