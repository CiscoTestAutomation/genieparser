# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.nxos.show_prefix_list import ShowIpPrefixList, \
                                         ShowIpv6PrefixList


# ==============================================
# Unit test for 'show ip prefix-list'
# ==============================================
class test_show_ip_prefix_list_detail(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "prefix_set_name": {
            "test": {
                 "entries": 6,
                 "protocol": "ipv4",
                 "prefix_set_name": "test",
                 "prefixes": {
                      "10.169.0.0/8 16..24 permit": {
                           "masklength_range": "16..24",
                           "sequence": 25,
                           "prefix": "10.169.0.0/8",
                           "action": "permit"
                      },
                      "10.205.0.0/8 8..16 permit": {
                           "masklength_range": "8..16",
                           "sequence": 10,
                           "prefix": "10.205.0.0/8",
                           "action": "permit"
                      },
                      "10.21.0.0/8 8..16 permit": {
                           "masklength_range": "8..16",
                           "sequence": 15,
                           "prefix": "10.21.0.0/8",
                           "action": "permit"
                      },
                      "10.205.0.0/8 8..8 deny": {
                           "masklength_range": "8..8",
                           "sequence": 5,
                           "prefix": "10.205.0.0/8",
                           "action": "deny"
                      },
                      "10.94.0.0/8 24..32 permit": {
                           "masklength_range": "24..32",
                           "sequence": 20,
                           "prefix": "10.94.0.0/8",
                           "action": "permit"
                      },
                      "192.0.2.0/24 25..25 permit": {
                           "masklength_range": "25..25",
                           "sequence": 30,
                           "prefix": "192.0.2.0/24",
                           "action": "permit"
                      },
                 }
            }
       }
    }

    golden_output = {'execute.return_value': '''\
        ip prefix-list test: 6 entries
         seq 5 deny 10.205.0.0/8 
         seq 10 permit 10.205.0.0/8 le 16 
         seq 15 permit 10.21.0.0/8 le 16 
         seq 20 permit 10.94.0.0/8 ge 24 
         seq 25 permit 10.169.0.0/8 ge 16 le 24 
         seq 30 permit 192.0.2.0/24 eq 25
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPrefixList(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpPrefixList(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ==============================================
# Unit test for 'show ipv6 prefix-list detail'
# ==============================================
class test_show_ipv6_prefix_list_detail(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "prefix_set_name": {
            "test6": {
                 "entries": 4,
                 "protocol": "ipv6",
                 "prefix_set_name": "test6",
                 "prefixes": {
                      "2001:db8:3::/64 64..128 permit": {
                           "masklength_range": "64..128",
                           "sequence": 15,
                           "prefix": "2001:db8:3::/64",
                           "action": "permit"
                      },
                      "2001:db8:2::/64 65..128 permit": {
                           "masklength_range": "65..128",
                           "sequence": 10,
                           "prefix": "2001:db8:2::/64",
                           "action": "permit"
                      },
                      "2001:db8:1::/64 64..64 permit": {
                           "masklength_range": "64..64",
                           "sequence": 5,
                           "prefix": "2001:db8:1::/64",
                           "action": "permit"
                      },
                      "2001:db8:4::/64 65..98 permit": {
                           "masklength_range": "65..98",
                           "sequence": 20,
                           "prefix": "2001:db8:4::/64",
                           "action": "permit"
                      }
                 }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        ipv6 prefix-list test6: 4 entries
         seq 5 permit 2001:db8:1::/64 
         seq 10 permit 2001:db8:2::/64 ge 65 
         seq 15 permit 2001:db8:3::/64 le 128 
         seq 20 permit 2001:db8:4::/64 ge 65 le 98 
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PrefixList(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6PrefixList(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()