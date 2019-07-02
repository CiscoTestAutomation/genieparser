
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Parser
from genie.libs.parser.iosxr.show_vrf import ShowVrfAllDetail

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

 
# =====================================
#  Unit test for 'show vrf all detail'
# =====================================

class test_show_vrf_all_detail(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "VRF1": {
            "description": "not set",
            "vrf_mode": "regular",
            "address_family": {
                 "ipv6 unicast": {
                      "route_target": {
                           "400:1": {
                                "rt_type": "import",
                                "route_target": "400:1"
                           },
                           "300:1": {
                                "rt_type": "import",
                                "route_target": "300:1"
                           },
                           "200:1": {
                                "rt_type": "both",
                                "route_target": "200:1"
                           },
                           "200:2": {
                                "rt_type": "import",
                                "route_target": "200:2"
                           }
                      }
                 },
                 "ipv4 unicast": {
                      "route_target": {
                           "400:1": {
                                "rt_type": "import",
                                "route_target": "400:1"
                           },
                           "300:1": {
                                "rt_type": "import",
                                "route_target": "300:1"
                           },
                           "200:1": {
                                "rt_type": "both",
                                "route_target": "200:1"
                           },
                           "200:2": {
                                "rt_type": "import",
                                "route_target": "200:2"
                           }
                      }
                 }
            },
            "route_distinguisher": "200:1",
            "interfaces": [
                 'GigabitEthernet0/0/0/1',
                 'GigabitEthernet0/0/0/0.415',
                 'GigabitEthernet0/0/0/0.420',
                 'GigabitEthernet0/0/0/1.390',
                 'GigabitEthernet0/0/0/1.410',
                 'GigabitEthernet0/0/0/1.415',
                 'GigabitEthernet0/0/0/1.420'
            ]
            },
        "VRF2": {
            "description": "not set",
            "vrf_mode": "regular",
            "address_family": {
                 "ipv6 unicast": {
                      "route_target": {
                           "200:2": {
                                "rt_type": "both",
                                "route_target": "200:2"
                           }
                      }
                 },
                 "ipv4 unicast": {
                      "route_target": {
                           "200:2": {
                                "rt_type": "both",
                                "route_target": "200:2"
                           }
                      }
                 }
            },
            "route_distinguisher": "200:2",
            "interfaces": [
                 "GigabitEthernet0/0/0/2"
            ]}
    }

    golden_output = {'execute.return_value': '''
        Mon Sep 18 09:36:51.507 PDT

        VRF VRF1; RD 200:1; VPN ID not set
        VRF mode: Regular
        Description not set
        Interfaces:
          GigabitEthernet0/0/0/1
          GigabitEthernet0/0/0/0.415
          GigabitEthernet0/0/0/0.420
          GigabitEthernet0/0/0/1.390
          GigabitEthernet0/0/0/1.410
          GigabitEthernet0/0/0/1.415
          GigabitEthernet0/0/0/1.420
        Address family IPV4 Unicast
          Import VPN route-target communities:
            RT:200:1
            RT:200:2
            RT:300:1
            RT:400:1
          Export VPN route-target communities:
            RT:200:1
          No import route policy
          No export route policy
        Address family IPV6 Unicast
          Import VPN route-target communities:
            RT:200:1
            RT:200:2
            RT:300:1
            RT:400:1
          Export VPN route-target communities:
            RT:200:1
          No import route policy
          No export route policy

        VRF VRF2; RD 200:2; VPN ID not set
        VRF mode: Regular
        Description not set
        Interfaces:
          GigabitEthernet0/0/0/2
        Address family IPV4 Unicast
          Import VPN route-target communities:
            RT:200:2
          Export VPN route-target communities:
            RT:200:2
          No import route policy
          No export route policy
        Address family IPV6 Unicast
          Import VPN route-target communities:
            RT:200:2
          Export VPN route-target communities:
            RT:200:2
          No import route policy
          No export route policy
    '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowVrfAllDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVrfAllDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()


# vim: ft=python et sw=4
