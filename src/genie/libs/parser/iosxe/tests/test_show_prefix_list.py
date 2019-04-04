# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_prefix_list import ShowIpPrefixListDetail, \
                                          ShowIpv6PrefixListDetail


# ==============================================
# Unit test for 'show ip prefix-list detail'
# ==============================================
class test_show_ip_prefix_list_detail(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "prefix_set_name": {
          "test": {
               "sequences": "5 - 25",
               "prefixes": {
                    "10.205.0.0/8 8..16 permit": {
                         "refcount": 0,
                         "prefix": "10.205.0.0/8",
                         "sequence": 10,
                         "hit_count": 0,
                         "masklength_range": "8..16",
                         "action": "permit",
                    },
                    "10.21.0.0/8 8..16 permit": {
                         "refcount": 1,
                         "prefix": "10.21.0.0/8",
                         "sequence": 15,
                         "hit_count": 0,
                         "masklength_range": "8..16",
                         "action": "permit",
                    },
                    "10.169.0.0/8 16..24 permit": {
                         "refcount": 3,
                         "prefix": "10.169.0.0/8",
                         "sequence": 25,
                         "hit_count": 0,
                         "masklength_range": "16..24",
                         "action": "permit",
                    },
                    "10.94.0.0/8 24..32 permit": {
                         "refcount": 2,
                         "prefix": "10.94.0.0/8",
                         "sequence": 20,
                         "hit_count": 0,
                         "masklength_range": "24..32",
                         "action": "permit",
                    },
                    "10.205.0.0/8 8..8 permit": {
                         "refcount": 1,
                         "prefix": "10.205.0.0/8",
                         "sequence": 5,
                         "hit_count": 0,
                         "masklength_range": "8..8",
                         "action": "permit",
                    }
               },
               "protocol": "ipv4",
               "refcount": 2,
               "range_entries": 4,
               "count": 5,
               "prefix_set_name": "test"
          }
       }
    }

    golden_output = {'execute.return_value': '''\
        Prefix-list with the last deletion/insertion: test
        ip prefix-list test:
           count: 5, range entries: 4, sequences: 5 - 25, refcount: 2
           seq 5 permit 10.205.0.0/8 (hit count: 0, refcount: 1)
           seq 10 permit 10.205.0.0/8 le 16 (hit count: 0, refcount: 0)
           seq 15 permit 10.21.0.0/8 le 16 (hit count: 0, refcount: 1)
           seq 20 permit 10.94.0.0/8 ge 24 (hit count: 0, refcount: 2)
           seq 25 permit 10.169.0.0/8 ge 16 le 24 (hit count: 0, refcount: 3)
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPrefixListDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpPrefixListDetail(device=self.device)
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
               "sequences": "5 - 20",
               "prefixes": {
                    "2001:DB8:2::/64 65..128 permit": {
                         "refcount": 1,
                         "prefix": "2001:DB8:2::/64",
                         "sequence": 10,
                         "hit_count": 0,
                         "action": "permit",
                         "masklength_range": "65..128"
                    },
                    "2001:DB8:3::/64 64..128 permit": {
                         "refcount": 3,
                         "prefix": "2001:DB8:3::/64",
                         "sequence": 15,
                         "hit_count": 0,
                         "action": "permit",
                         "masklength_range": "64..128"
                    },
                    "2001:DB8:1::/64 64..64 permit": {
                         "refcount": 1,
                         "prefix": "2001:DB8:1::/64",
                         "sequence": 5,
                         "hit_count": 0,
                         "action": "permit",
                         "masklength_range": "64..64"
                    }
               },
               "protocol": "ipv6",
               "refcount": 2,
               "range_entries": 3,
               "count": 4,
               "prefix_set_name": "test6"
          }
       }}

    golden_output = {'execute.return_value': '''\
        Prefix-list with the last deletion/insertion: test6
        ipv6 prefix-list test6:
           count: 4, range entries: 3, sequences: 5 - 20, refcount: 2
           seq 5 permit 2001:DB8:1::/64 (hit count: 0, refcount: 1)
           seq 10 permit 2001:DB8:2::/64 ge 65 (hit count: 0, refcount: 1)
           seq 15 permit 2001:DB8:3::/64 le 128 (hit count: 0, refcount: 3)
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PrefixListDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6PrefixListDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()