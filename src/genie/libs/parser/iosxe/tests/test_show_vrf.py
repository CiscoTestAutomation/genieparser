
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Parser
from genie.libs.parser.iosxe.show_vrf import ShowVrfDetail

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

 
# ================================
#  Unit test for 'show vrf detail'
#  Unit test for 'show vrf detail <vrf>'
# ================================

class test_show_vrf_detail(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "Mgmt-vrf": {
              "vrf_id": 1,
              "interfaces": [
                   "GigabitEthernet0/0"
              ],
              "interface": {
                   "GigabitEthernet0/0": {'vrf': 'Mgmt-vrf'}
              },
              "address_family": {
                   "ipv4 unicast": {
                        "table_id": "0x1",
                        "flags": "0x0",
                        "vrf_label": {
                            'allocation_mode': 'per-prefix'
                        }
                   },
                   "ipv6 unicast": {
                        "table_id": "0x1E000001",
                        "flags": "0x0",
                        "vrf_label": {
                            'allocation_mode': 'per-prefix'
                        }
                   }
              },
              "flags": "0x1808"
         },
        "VRF1": {
              "interfaces": [
                   "GigabitEthernet0/0"
              ],
              "interface": {
                   "GigabitEthernet0/0": {'vrf': 'VRF1'}
              },
              "address_family": {
                   "ipv4 unicast": {
                        "export_to_global": {
                             "export_to_global_map": "export_to_global_map",
                             "prefix_limit": 1000
                        },
                        "import_from_global": {
                             "prefix_limit": 1000,
                             "import_from_global_map": "import_from_global_map"
                        },
                        "table_id": "0x1",
                        "routing_table_limit": {
                             "routing_table_limit_action": {
                                  "enable_alert_limit_number": {
                                       "alert_limit_number": 10000
                                  }
                             }
                        },
                        "route_targets": {
                             "200:1": {
                                  "rt_type": "both",
                                  "route_target": "200:1"
                             },
                             "100:1": {
                                  "rt_type": "both",
                                  "route_target": "100:1"
                             }
                        },
                        "flags": "0x2100",
                        "vrf_label": {
                            'allocation_mode': 'per-prefix'
                        }
                   },
                   "ipv6 unicast": {
                        "export_to_global": {
                             "export_to_global_map": "export_to_global_map",
                             "prefix_limit": 1000
                        },
                        "table_id": "0x1E000001",
                        "routing_table_limit": {
                             "routing_table_limit_action": {
                                  "enable_alert_percent": {
                                       "alert_percent_value": 70
                                  },
                                  "enable_alert_limit_number": {
                                       "alert_limit_number": 7000
                                  }
                             },
                             "routing_table_limit_number": 10000
                        },
                        "route_targets": {
                             "200:1": {
                                  "rt_type": "import",
                                  "route_target": "200:1"
                             },
                             "400:1": {
                                  "rt_type": "import",
                                  "route_target": "400:1"
                             },
                             "300:1": {
                                  "rt_type": "export",
                                  "route_target": "300:1"
                             },
                             "100:1": {
                                  "rt_type": "export",
                                  "route_target": "100:1"
                             }
                        },
                        "flags": "0x100",
                        "vrf_label": {
                            'allocation_mode': 'per-prefix'
                        }
                   }
              },
              "flags": "0x180C",
              "route_distinguisher": "100:1",
              "vrf_id": 1
         }
    }

    golden_output = {'execute.return_value': '''
        VRF VRF1 (VRF Id = 1); default RD 100:1; default VPNID <not set>
          New CLI format, supports multiple address-families
          Flags: 0x180C
            Interfaces:
                Gi0/0
        Address family ipv4 unicast (Table ID = 0x1):
          Flags: 0x2100
          Export VPN route-target communities
            RT:100:1                 RT:200:1                
          Import VPN route-target communities
            RT:100:1                 RT:200:1                
          Import route-map for ipv4 unicast: import_from_global_map (prefix limit: 1000)
          Global export route-map for ipv4 unicast: export_to_global_map (prefix limit: 1000)
          No export route-map
          Route warning limit 10000, current count 0
          VRF label distribution protocol: not configured
          VRF label allocation mode: per-prefix
        Address family ipv6 unicast (Table ID = 0x1E000001):
          Flags: 0x100
          Export VPN route-target communities
            RT:100:1                 RT:300:1                
          Import VPN route-target communities
            RT:200:1                 RT:400:1                
          No import route-map
          Global export route-map for ipv6 unicast: export_to_global_map (prefix limit: 1000)
          No export route-map
          Route limit 10000, warning limit 70% (7000), current count 1
          VRF label distribution protocol: not configured
          VRF label allocation mode: per-prefix
        Address family ipv4 multicast not active

        VRF Mgmt-vrf (VRF Id = 1); default RD <not set>; default VPNID <not set>
          New CLI format, supports multiple address-families
          Flags: 0x1808
          Interfaces:
            Gi0/0                   
        Address family ipv4 unicast (Table ID = 0x1):
          Flags: 0x0
          No Export VPN route-target communities
          No Import VPN route-target communities
          No import route-map
          No global export route-map
          No export route-map
          VRF label distribution protocol: not configured
          VRF label allocation mode: per-prefix
        Address family ipv6 unicast (Table ID = 0x1E000001):
          Flags: 0x0
          No Export VPN route-target communities
          No Import VPN route-target communities
          No import route-map
          No global export route-map
          No export route-map
          VRF label distribution protocol: not configured
          VRF label allocation mode: per-prefix
        Address family ipv4 multicast not active
        Address family ipv6 multicast not active
        '''}

    golden_parsed_output1 = {'Mgmt-intf': 
        {'vrf_id': 1,
        'flags': '0x1808',
         'interface': {'GigabitEthernet1': {'vrf': 'Mgmt-intf'}},
         'interfaces': ['GigabitEthernet1'],
         'address_family': 
          {'ipv4 unicast': {'flags': '0x0',
                           'table_id': '0x1',
                           'vrf_label': {'allocation_mode': 'per-prefix'}
                           }}
        }
    }

    golden_output1 = {'execute.return_value': '''
R1_xe#show ip vrf detail Mgmt-intf
VRF Mgmt-intf (VRF Id = 1); default RD <not set>; default VPNID <not set>
  New CLI format, supports multiple address-families
  Flags: 0x1808
  Interfaces:
    Gi1                     
Address family ipv4 unicast (Table ID = 0x1):
  Flags: 0x0
  No Export VPN route-target communities
  No Import VPN route-target communities
  No import route-map
  No global export route-map
  No export route-map
  VRF label distribution protocol: not configured
  VRF label allocation mode: per-prefix
    '''}
    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowVrfDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVrfDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowVrfDetail(device=self.device)
        parsed_output = obj.parse(vrf='Mgmt-intf')
        self.assertEqual(parsed_output, self.golden_parsed_output1)


    def test_empty1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVrfDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='Mgmt-intf')


if __name__ == '__main__':
    unittest.main()


# vim: ft=python et sw=4
