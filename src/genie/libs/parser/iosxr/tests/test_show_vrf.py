
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

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

    maxDiff = None

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

    golden_output_2 = {'execute.return_value': '''
    show vrf all detail
    
    Wed Apr 29 12:45:39.793 CET
    
    VRF AWS-DNB-AppSharedServices-PROD; RD 201627:373; VPN ID not set
    VRF mode: Regular
    Description not set
    Interfaces:
      Bundle-Ether15.244
    Address family IPV4 Unicast
      Import VPN route-target communities:
        RT:201627:373
      Export VPN route-target communities:
        RT:201627:373
      No import route policy
      No export route policy
    Address family IPV6 Unicast
      No import VPN route-target communities
      No export VPN route-target communities
      No import route policy
      No export route policy
    
    VRF Administrasjon; RD not set; VPN ID not set
    VRF mode: Regular
    Description not set
    Address family IPV4 Unicast
      Import VPN route-target communities:
        RT:65100:30
      Export VPN route-target communities:
        RT:65100:30
      No import route policy
      No export route policy
    Address family IPV6 Unicast
      No import VPN route-target communities
      No export VPN route-target communities
      No import route policy
      No export route policy
    
    VRF BT-HCL-DNB; RD 201627:600; VPN ID not set
    VRF mode: Regular
    Description not set
    Interfaces:
      Bundle-Ether15.2942
    Address family IPV4 Unicast
      Import VPN route-target communities:
        RT:201627:600
      Export VPN route-target communities:
        RT:201627:600
      No import route policy
      No export route policy
    Address family IPV6 Unicast
      No import VPN route-target communities
      No export VPN route-target communities
      No import route policy
      No export route policy

    VRF DNB-TATA; RD 201627:241; VPN ID not set
    VRF mode: Regular
    Description not set
    Interfaces:
      Bundle-Ether15.514
      Bundle-Ether15.1285
      TenGigE0/0/2/1.600
    Address family IPV4 Unicast
      Import VPN route-target communities:
        RT:201627:241
      Export VPN route-target communities:
        RT:201627:241
      No import route policy
      No export route policy
    Address family IPV6 Unicast
      No import VPN route-target communities
      No export VPN route-target communities
      No import route policy
      No export route policy
    '''}

    golden_parsed_output_2 = {
        'AWS-DNB-AppSharedServices-PROD': {
            'address_family': {
                'ipv4 unicast': {
                    'route_target': {
                        '201627:373': {
                            'route_target': '201627:373',
                            'rt_type': 'both',
                        },
                    },
                },
                'ipv6 unicast': {
                },
            },
            'description': 'not set',
            'interfaces': ['Bundle-Ether15.244'],
            'route_distinguisher': '201627:373',
            'vrf_mode': 'regular',
        },
        'Administrasjon': {
            'address_family': {
                'ipv4 unicast': {
                    'route_target': {
                        '65100:30': {
                            'route_target': '65100:30',
                            'rt_type': 'both',
                        },
                    },
                },
                'ipv6 unicast': {
                },
            },
            'description': 'not set',
            'vrf_mode': 'regular',
        },
        'BT-HCL-DNB': {
            'address_family': {
                'ipv4 unicast': {
                    'route_target': {
                        '201627:600': {
                            'route_target': '201627:600',
                            'rt_type': 'both',
                        },
                    },
                },
                'ipv6 unicast': {
                },
            },
            'description': 'not set',
            'interfaces': ['Bundle-Ether15.2942'],
            'route_distinguisher': '201627:600',
            'vrf_mode': 'regular',
        },
        'DNB-TATA': {
            'address_family': {
                'ipv4 unicast': {
                    'route_target': {
                        '201627:241': {
                            'route_target': '201627:241',
                            'rt_type': 'both',
                        },
                    },
                },
                'ipv6 unicast': {
                },
            },
            'description': 'not set',
            'interfaces': ['Bundle-Ether15.514', 'Bundle-Ether15.1285', 'TenGigE0/0/2/1.600'],
            'route_distinguisher': '201627:241',
            'vrf_mode': 'regular',
        },
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVrfAllDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowVrfAllDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowVrfAllDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


if __name__ == '__main__':
    unittest.main()


# vim: ft=python et sw=4
