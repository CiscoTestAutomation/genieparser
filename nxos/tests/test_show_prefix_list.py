# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from parser.nxos.show_prefix_list import ShowIpPrefixList, \
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
                 "entries": 5,
                 "protocol": "ipv4",
                 "prefix_set_name": "test",
                 "prefixes": {
                      "38.0.0.0/8 16..24": {
                           "masklength_range": "16..24",
                           "sequence": 25,
                           "prefix": "38.0.0.0/8"
                      },
                      "35.0.0.0/8 8..16": {
                           "masklength_range": "8..16",
                           "sequence": 10,
                           "prefix": "35.0.0.0/8"
                      },
                      "36.0.0.0/8 8..16": {
                           "masklength_range": "8..16",
                           "sequence": 15,
                           "prefix": "36.0.0.0/8"
                      },
                      "35.0.0.0/8 8..8": {
                           "masklength_range": "8..8",
                           "sequence": 5,
                           "prefix": "35.0.0.0/8"
                      },
                      "37.0.0.0/8 24..32": {
                           "masklength_range": "24..32",
                           "sequence": 20,
                           "prefix": "37.0.0.0/8"
                      }
                 }
            }
       }
    }

    golden_output = {'execute.return_value': '''\
        ip prefix-list test: 5 entries
         seq 5 permit 35.0.0.0/8 
         seq 10 permit 35.0.0.0/8 le 16 
         seq 15 permit 36.0.0.0/8 le 16 
         seq 20 permit 37.0.0.0/8 ge 24 
         seq 25 permit 38.0.0.0/8 ge 16 le 24 
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
                      "2001:db8:3::/64 64..128": {
                           "masklength_range": "64..128",
                           "sequence": 15,
                           "prefix": "2001:db8:3::/64"
                      },
                      "2001:db8:2::/64 65..128": {
                           "masklength_range": "65..128",
                           "sequence": 10,
                           "prefix": "2001:db8:2::/64"
                      },
                      "2001:db8:1::/64 64..64": {
                           "masklength_range": "64..64",
                           "sequence": 5,
                           "prefix": "2001:db8:1::/64"
                      },
                      "2001:db8:4::/64 65..98": {
                           "masklength_range": "65..98",
                           "sequence": 20,
                           "prefix": "2001:db8:4::/64"
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