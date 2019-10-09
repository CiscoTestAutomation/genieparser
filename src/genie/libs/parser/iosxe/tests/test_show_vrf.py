#!/bin/env python
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Parser
from genie.libs.parser.iosxe.show_vrf import ShowVrf, \
                                             ShowVrfDetail

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError


# ================================
#  Unit test for 
#    * 'show vrf'
#    * 'show vrf {vrf}'
#    * 'show vrf detail'
#    * 'show vrf detail <vrf>'
# ================================

class TestShowVrf(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        [2019-05-10 06:56:37,856] +++ R1_xe: executing command 'show vrf' +++
        show vrf
        Name                             Default RD            Protocols   Interfaces
        Mgmt-intf                        <not set>             ipv4,ipv6   Gi1
        VRF1                             65000:1               ipv4,ipv6   Tu1
                                                                            Lo300
                                                                            Gi2.390
                                                                            Gi2.410
                                                                            Gi2.415
                                                                            Gi2.420
                                                                            Gi3.390
                                                                            Gi3.410
                                                                            Gi3.415
                                                                            Tu3
                                                                            Tu4
                                                                            Tu6
                                                                            Tu8
                                                                            Gi3.420
    '''}

    golden_parsed_output = {
        'vrf': {
            'Mgmt-intf': {
                'protocols': ['ipv4', 'ipv6'],
                'interfaces': ['GigabitEthernet1'],
            },
            'VRF1': {
                'route_distinguisher': '65000:1',
                'protocols': ['ipv4', 'ipv6'],
                'interfaces': ['Tunnel1', 
                               'Loopback300', 
                               'GigabitEthernet2.390', 
                               'GigabitEthernet2.410', 
                               'GigabitEthernet2.415', 
                               'GigabitEthernet2.420', 
                               'GigabitEthernet3.390', 
                               'GigabitEthernet3.410', 
                               'GigabitEthernet3.415', 
                               'Tunnel3', 
                               'Tunnel4', 
                               'Tunnel6', 
                               'Tunnel8', 
                               'GigabitEthernet3.420'],
            }
        }
    }

    golden_output_vrf = {'execute.return_value': '''
        [2019-05-10 06:56:43,272] +++ R1_xe: executing command 'show vrf VRF1' +++
        show vrf VRF1
        Name                             Default RD            Protocols   Interfaces
        VRF1                             65000:1               ipv4,ipv6   Tu1
                                                                            Lo300
                                                                            Gi2.390
                                                                            Gi2.410
                                                                            Gi2.415
                                                                            Gi2.420
                                                                            Gi3.390
                                                                            Gi3.410
                                                                            Gi3.415
                                                                            Tu3
                                                                            Tu4
                                                                            Tu6
                                                                            Tu8
                                                                            Gi3.420
    '''}

    golden_parsed_output_vrf = {
        'vrf': {
            'VRF1': {
                'route_distinguisher': '65000:1',
                'protocols': ['ipv4', 'ipv6'],
                'interfaces': ['Tunnel1',
                               'Loopback300',
                               'GigabitEthernet2.390',
                               'GigabitEthernet2.410',
                               'GigabitEthernet2.415',
                               'GigabitEthernet2.420',
                               'GigabitEthernet3.390',
                               'GigabitEthernet3.410',
                               'GigabitEthernet3.415',
                               'Tunnel3',
                               'Tunnel4',
                               'Tunnel6',
                               'Tunnel8',
                               'GigabitEthernet3.420'],
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVrf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowVrf(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_vrf(self):
        self.device = Mock(**self.golden_output_vrf)
        obj = ShowVrf(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_vrf)


class TestShowVrfDetail(unittest.TestCase):

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
                            "allocation_mode": "per-prefix",
                        }
                   }
              },
              "flags": "0x1808",
              "cli_format": "New",
              "support_af": "multiple address-families",
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
              "cli_format": "New",
              "support_af": "multiple address-families",
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

    golden_parsed_output1 = {
        'Mgmt-intf': {
            'vrf_id': 1,
            'flags': '0x1808',
            "cli_format": "New",
            "support_af": "multiple address-families",
            'interface': {
                'GigabitEthernet1': {
                  'vrf': 'Mgmt-intf',
                  },
                },
            'interfaces': ['GigabitEthernet1'],
            'address_family': {
                'ipv4 unicast': {
                    'flags': '0x0',
                    'table_id': '0x1',
                    'vrf_label': {
                        'allocation_mode': 'per-prefix',
              }
            }
          }
        }

    }

    golden_output1 = {'execute.return_value': '''
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
      '''
    }

    golden_parsed_output2 = {
        "GENIE": {
            "address_family": {
                "ipv4 unicast": {
                    "flags": "0x0",
                    "route_targets": {
                        "65109:1": {
                            "route_target": "65109:1",
                            "rt_type": "export"
                        },
                        "65109:110": {
                            "route_target": "65109:110",
                            "rt_type": "both"
                        },
                        "65109:4094": {
                            "route_target": "65109:4094",
                            "rt_type": "import"
                        }
                    },
                    "table_id": "0x11",
                    "vrf_label": {
                        "allocation_mode": "per-prefix"
                    }
                }
            },
            "cli_format": "New",
            "description": "VPN for GENIE parser",
            "flags": "0x180C",
            "interface": {
                "GigabitEthernet0/0/0.110": {
                    "vrf": "GENIE"
                },
                "TenGigabitEthernet0/1/2.1042": {
                    "vrf": "GENIE"
                },
                "vasileft110": {
                    "vrf": "GENIE"
                }
            },
            "interfaces": [
                "GigabitEthernet0/0/0.110",
                "TenGigabitEthernet0/1/2.1042",
                "vasileft110"
            ],
            "route_distinguisher": "65109:110",
            "support_af": "multiple address-families",
            "vrf_id": 17,
        }
    }

    golden_output2 = {'execute.return_value': '''
        VRF GENIE (VRF Id = 17); default RD 65109:110; default VPNID <not set>
          Description: VPN for GENIE parser
          New CLI format, supports multiple address-families
          Flags: 0x180C
          Interfaces:
            Gi0/0/0.110              Te0/1/2.1042             vl110
        Address family ipv4 unicast (Table ID = 0x11):
          Flags: 0x0
          Export VPN route-target communities
            RT:65109:1               RT:65109:110
          Import VPN route-target communities
            RT:65109:4094            RT:65109:110
          No import route-map
          No global export route-map
          No export route-map
          VRF label distribution protocol: not configured
          VRF label allocation mode: per-prefix
        Address family ipv6 unicast not active
        Address family ipv4 multicast not active
        Address family ipv6 multicast not active
    '''}

    golden_output_3 = {'execute.return_value': '''
        VRF GENIE-BACKUP (VRF Id = 12); default RD 50998:106; default VPNID <not set>
        Description: VPN for CHRH (Backup network)
        New CLI format, supports multiple address-families
        Flags: 0x180C
        Interfaces:
            BD106
        Address family ipv4 unicast (Table ID = 0xC):
        Flags: 0x0
        Export VPN route-target communities
            RT:50998:1               RT:50998:106
        Import VPN route-target communities
            RT:50998:106             RT:50998:4094
        No import route-map
        No global export route-map
        No export route-map
        VRF label distribution protocol: not configured
        VRF label allocation mode: per-prefix
        Address family ipv6 unicast not active
        Address family ipv4 multicast not active
        Address family ipv6 multicast not active

        VRF GENIE-LAB (VRF Id = 76); default RD 50998:11; default VPNID <not set>
        Description: VPN for Internet Direct Link Out (Internal FW)
        New CLI format, supports multiple address-families
        Flags: 0x180C
        Interfaces:
            Te0/1/1.11               vr92                     vr110
        Address family ipv4 unicast (Table ID = 0x4C):
        Flags: 0x0
        Export VPN route-target communities
            RT:50998:11
        Import VPN route-target communities
            RT:50998:11
        No import route-map
        No global export route-map
        No export route-map
        VRF label distribution protocol: not configured
        VRF label allocation mode: per-prefix
        Address family ipv6 unicast (Table ID = 0x1E000003):
        Flags: 0x0
        Export VPN route-target communities
            RT:50998:11
        Import VPN route-target communities
            RT:50998:11
        No import route-map
        No global export route-map
        No export route-map
        VRF label distribution protocol: not configured
        VRF label allocation mode: per-prefix
        Address family ipv4 multicast not active
        Address family ipv6 multicast not active

        VRF GENIE-PROD (VRF Id = 17); default RD 50998:110; default VPNID <not set>
        Description: VPN for Dame Blanche
        New CLI format, supports multiple address-families
        Flags: 0x180C
        Interfaces:
            Gi0/0/0.110              Te0/1/2.1042             vl110
        Address family ipv4 unicast (Table ID = 0x11):
        Flags: 0x0
        Export VPN route-target communities
            RT:50998:1               RT:50998:110
        Import VPN route-target communities
            RT:50998:4094            RT:50998:110
        No import route-map
        No global export route-map
        No export route-map
        VRF label distribution protocol: not configured
        VRF label allocation mode: per-prefix
        Address family ipv6 unicast not active
        Address family ipv4 multicast not active
        Address family ipv6 multicast not active
    '''
    }

    golden_parsed_output_3 = {
        'GENIE-BACKUP': {
            'address_family': {
                'ipv4 unicast': {
                    'flags': '0x0',
                    'route_targets': {
                        '50998:1': {
                            'route_target': '50998:1',
                            'rt_type': 'export'
                        },
                        '50998:106': {
                            'route_target': '50998:106',
                            'rt_type': 'both'
                        },
                        '50998:4094': {
                            'route_target': '50998:4094',
                            'rt_type': 'import'
                        }
                    },
                    'table_id': '0xC',
                    'vrf_label': {
                        'allocation_mode': 'per-prefix'
                    }
                }
            },
            'cli_format': 'New',
            'description': 'VPN for CHRH (Backup network)',
            'flags': '0x180C',
            'interface': {
                'BDI106': {
                    'vrf': 'GENIE-BACKUP'
                }
            },
            'interfaces': ['BDI106'],
            'route_distinguisher': '50998:106',
            'support_af': 'multiple address-families',
            'vrf_id': 12
        },
        'GENIE-LAB': {
            'address_family': {
                'ipv4 unicast': {
                    'flags': '0x0',
                    'route_targets': {
                        '50998:11': {
                            'route_target': '50998:11',
                            'rt_type': 'both'
                        }
                    },
                    'table_id': '0x4C',
                    'vrf_label': {
                        'allocation_mode': 'per-prefix'
                    }
                },
                'ipv6 unicast': {
                    'flags': '0x0',
                    'route_targets': {
                        '50998:11': {
                            'route_target': '50998:11',
                            'rt_type': 'both'
                        }
                    },
                    'table_id': '0x1E000003',
                    'vrf_label': {
                        'allocation_mode': 'per-prefix'
                    }
                }
            },
            'cli_format': 'New',
            'description': 'VPN for Internet Direct Link Out (Internal FW)',
            'flags': '0x180C',
            'interface': {
                'TenGigabitEthernet0/1/1.11': {
                    'vrf': 'GENIE-LAB'
                },
                'vasiright110': {
                    'vrf': 'GENIE-LAB'
                },
                'vasiright92': {
                    'vrf': 'GENIE-LAB'
                }
            },
            'interfaces': ['TenGigabitEthernet0/1/1.11',
                            'vasiright92',
                            'vasiright110'],
            'route_distinguisher': '50998:11',
            'support_af': 'multiple address-families',
            'vrf_id': 76
        },
        'GENIE-PROD': {
            'address_family': {
                'ipv4 unicast': {
                    'flags': '0x0',
                    'route_targets': {
                        '50998:1': {
                            'route_target': '50998:1',
                            'rt_type': 'export'
                        },
                        '50998:110': {
                            'route_target': '50998:110',
                            'rt_type': 'both'
                        },
                        '50998:4094': {
                            'route_target': '50998:4094',
                            'rt_type': 'import'
                        }
                    },
                    'table_id': '0x11',
                    'vrf_label': {
                        'allocation_mode': 'per-prefix'
                    }
                }
            },
            'cli_format': 'New',
            'description': 'VPN for Dame Blanche',
            'flags': '0x180C',
            'interface': {
                'GigabitEthernet0/0/0.110': {
                    'vrf': 'GENIE-PROD'
                },
                'TenGigabitEthernet0/1/2.1042': {
                    'vrf': 'GENIE-PROD'
                },
                'vasileft110': {
                    'vrf': 'GENIE-PROD'
                }
            },
            'interfaces': ['GigabitEthernet0/0/0.110',
                            'TenGigabitEthernet0/1/2.1042',
                            'vasileft110'],
            'route_distinguisher': '50998:110',
            'support_af': 'multiple address-families',
            'vrf_id': 17
        }
    }
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

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowVrfDetail(device=self.device)
        parsed_output = obj.parse(vrf='GENIE')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_empty1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVrfDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='Mgmt-intf')

    def test_golden_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowVrfDetail(device=self.device)
        parsed_output = obj.parse(vrf='GENIE')
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

if __name__ == '__main__':
    unittest.main()


# vim: ft=python et sw=4
