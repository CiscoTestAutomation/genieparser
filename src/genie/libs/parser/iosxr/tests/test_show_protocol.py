
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_ospf
from genie.libs.parser.iosxr.show_protocol import ShowProtocolsAfiAllAll


# ===========================================
#  Unit test for 'show protocols afi-all all'
# ===========================================
class test_show_protocols_afi_all_all(unittest.TestCase):

    '''Unit test for "show protocols afi-all all" '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'protocols': 
            {'bgp': 
                {'address_family': 
                    {'vpnv4 unicast': 
                        {'distance': 
                            {'external': 20,
                            'internal': 200,
                            'local': 200},
                        'neighbors': 
                            {'10.64.4.4': 
                                {'gr_enable': 'No',
                                'last_update': '00:01:28',
                                'nsr_state': 'None'}}},
                    'vpnv6 unicast': 
                        {'distance': 
                            {'external': 20,
                            'internal': 200,
                            'local': 200},
                        'neighbors': 
                            {'10.64.4.4': 
                                {'gr_enable': 'No',
                                'last_update': '00:01:28',
                                'nsr_state': 'None'}}}},
                'bgp_pid': 100,
                'graceful_restart': 
                    {'enable': False},
                'nsr': 
                    {'current_state': 'active ready',
                    'enable': True}},
            'ospf': 
                {'vrf': 
                    {'default': 
                        {'address_family': 
                            {'ipv4': 
                                {'instance': 
                                    {'1': 
                                        {'areas': 
                                            {'0.0.0.0': 
                                                {'interfaces': ['Loopback0', 'GigabitEthernet0/0/0/0', 'GigabitEthernet0/0/0/2'],
                                                'mpls': 
                                                    {'te': 
                                                        {'enable': True}}}},
                                                'nsf': False,
                                        'preference': 
                                            {'multi_values': 
                                                {'external': 114,
                                                'granularity': 
                                                    {'detail': 
                                                        {'inter_area': 113,
                                                        'intra_area': 112}}},
                                            'single_value': 
                                                {'all': 110}},
                                        'redistribution': 
                                            {'bgp': 
                                                {'bgp_id': 100,
                                                'metric': 111},
                                            'connected': 
                                                {'enabled': True},
                                            'isis': 
                                                {'isis_pid': '10',
                                                'metric': 3333},
                                            'static': 
                                                {'enabled': True,
                                                'metric': 10}},
                                        'router_id': '10.36.3.3'}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:R3_ospf_xr#show protocols afi-all all
        Mon Jan  8 17:45:17.553 UTC

        Routing Protocol "BGP 100"
        Non-stop routing is enabled
        Graceful restart is not enabled
        Current BGP NSR state - Active Ready
        BGP NSR state not ready: Wait for standby ready msg

        Address Family VPNv4 Unicast:
          Distance: external 20 internal 200 local 200
          Routing Information Sources:
            Neighbor          State/Last update received  NSR-State  GR-Enabled
            10.64.4.4           00:01:28                    None         No

        Address Family VPNv6 Unicast:
          Distance: external 20 internal 200 local 200
          Routing Information Sources:
            Neighbor          State/Last update received  NSR-State  GR-Enabled
            10.64.4.4           00:01:28                    None         No

        Routing Protocol OSPF 1
          Router Id: 10.36.3.3
          Distance: 110
          Distance: IntraArea 112 InterArea 113 External/NSSA 114
          Non-Stop Forwarding: Disabled
          Redistribution:
            connected
            static with metric 10
            bgp 100 with metric 111
            isis 10 with metric 3333
          Area 0
            MPLS/TE enabled
            Loopback0
            GigabitEthernet0/0/0/0
            GigabitEthernet0/0/0/2
        '''}

    golden_parsed_output2 = {
        "protocols": {
              "ospf": {
                   "vrf": {
                        "default": {
                             "address_family": {
                                  "ipv4": {
                                       "instance": {
                                            "1": {
                                                 "preference": {
                                                      "single_value": {
                                                           "all": 110
                                                      }
                                                 },
                                                 "router_id": "192.168.205.1",
                                                 "nsf": True,
                                                 "areas": {
                                                      "0.0.0.1": {
                                                           "mpls": {
                                                                "te": {
                                                                     "enable": True
                                                                }
                                                           },
                                                           "interfaces": [
                                                                "Loopback5"
                                                           ]
                                                      },
                                                      "0.0.0.0": {
                                                           "interfaces": [
                                                                "Loopback0"
                                                           ]
                                                      }
                                                 }
                                            }
                                       }
                                  }
                             }
                        }
                   }
              },
              "ospfv3": {
                   "vrf": {
                        "default": {
                             "address_family": {
                                  "ipv4": {
                                       "instance": {
                                            "1": {
                                                 "preference": {
                                                      "single_value": {
                                                           "all": 110
                                                      }
                                                 },
                                                 "router_id": "0.0.0.0"
                                            }
                                       }
                                  }
                             }
                        }
                   }
              },
              "bgp": {
                   "bgp_pid": 100,
                   "nsr": {
                        "enable": True,
                        "current_state": "tcp initial sync"
                   },
                   "address_family": {
                        "vpnv6 unicast": {
                             "distance": {
                                  "internal": 200,
                                  "local": 200,
                                  "external": 20
                             }
                        },
                        "vpnv4 unicast": {
                             "distance": {
                                  "internal": 200,
                                  "local": 200,
                                  "external": 20
                             }
                        }
                   }
              }
         }
    }
    golden_output2 = {'execute.return_value': '''
        Routing Protocol "BGP 100"
        Non-stop routing is enabled
        Graceful restart is enabled
        Current BGP NSR state - TCP Initial Sync
        BGP NSR state not ready: TCP Initsync in progress

        Address Family VPNv4 Unicast:
          Distance: external 20 internal 200 local 200

        Address Family VPNv6 Unicast:
          Distance: external 20 internal 200 local 200


        IS-IS Router: 1
          System Id: 1c53.0001.0001 
          Instance Id: 0
          IS Levels: level-2-only
          Manual area address(es):
            49.0001
          Routing for area address(es):
            49.0001
          Non-stop forwarding: Disabled
          Most recent startup mode: Cold Restart
          TE connection status: Up
          Topologies supported by IS-IS:
            IPv4 Unicast
              Level-2
                Metric style (generate/accept): Narrow/Narrow
                Metric: 10
                ISPF status: Disabled
              No protocols redistributed
              Distance: 115
              Advertise Passive Interface Prefixes Only: No
            IPv6 Unicast
              Level-2
                Metric: 10
                ISPF status: Disabled
              No protocols redistributed
              Distance: 115
              Advertise Passive Interface Prefixes Only: No
          SRLB allocated: 0 - 0
          SRGB not allocated
          Interfaces supported by IS-IS:
            GigabitEthernet0/0/0/0.104 is disabled (active in configuration)
            GigabitEthernet0/0/0/1.104 is disabled (active in configuration)

        Routing Protocol OSPF 1
          Router Id: 192.168.205.1
          Distance: 110
          Non-Stop Forwarding: Enabled
          Redistribution:
            None
          Area 0
            Loopback0
          Area 1
            MPLS/TE enabled
            Loopback5

        Routing Protocol OSPFv3 1
          Router Id: 0.0.0.0
          Distance: 110
          Graceful Restart: Disabled
          Redistribution:
            None
    '''}

    golden_parsed_output3 = {
        "protocols": {
            "bgp": {
                "bgp_pid": 19108,
                "nsr": {
                    "enable": True,
                    "current_state": "active ready"
                },
                "address_family": {
                    "ipv4 unicast": {
                        "distance": {
                            "external": 20,
                            "internal": 200,
                            "local": 200
                        },
                        "sourced_networks": [
                            "10.10.10.0/30",
                            "10.20.30.40/32",
                            "10.24.24.8/30",
                            "10.108.0.0/24",
                            "10.249.130.0/25",
                            "14.14.14.14/32",
                            "19.10.8.0/24",
                            "25.1.25.0/24",
                            "66.76.44.142/31",
                            "66.76.44.154/31",
                            "66.76.44.156/31",
                            "66.76.44.166/31",
                            "66.76.44.192/31",
                            "66.76.44.194/31",
                            "66.76.44.202/31",
                            "66.76.44.242/31",
                            "66.76.44.244/31",
                            "66.76.44.248/31",
                            "66.76.150.240/28",
                            "92.168.54.1/32",
                            "100.64.0.0/21",
                            "100.64.3.0/24",
                            "169.254.1.0/30",
                            "169.254.2.2/32",
                            "169.254.11.0/24"
                        ],
                        "neighbors": {
                            "66.76.44.130": {
                                "last_update": "03:35:21",
                                "nsr_state": "None",
                                "gr_enable": "Yes"
                            },
                            "172.25.12.2": {
                                "last_update": "03:40:02",
                                "nsr_state": "None",
                                "gr_enable": "Yes"
                            },
                            "172.25.12.17": {
                                "last_update": "1w0d",
                                "nsr_state": "None",
                                "gr_enable": "Yes"
                            },
                            "172.25.12.18": {
                                "last_update": "1w0d",
                                "nsr_state": "None",
                                "gr_enable": "Yes"
                            },
                            "172.25.12.19": {
                                "last_update": "Active",
                                "nsr_state": "None",
                                "gr_enable": "Yes"
                            },
                            "173.219.15.138": {
                                "last_update": "1w0d",
                                "nsr_state": "None",
                                "gr_enable": "Yes"
                            },
                            "173.219.15.139": {
                                "last_update": "1w0d",
                                "nsr_state": "None",
                                "gr_enable": "Yes"
                            }
                        }
                    },
                    "vpnv4 unicast": {
                        "distance": {
                            "external": 20,
                            "internal": 200,
                            "local": 200
                        },
                        "neighbors": {
                            "172.25.12.2": {
                                "last_update": "03:40:02",
                                "nsr_state": "None",
                                "gr_enable": "Yes"
                            },
                            "172.25.12.17": {
                                "last_update": "1w0d",
                                "nsr_state": "None",
                                "gr_enable": "Yes"
                            },
                            "172.25.12.18": {
                                "last_update": "1w0d",
                                "nsr_state": "None",
                                "gr_enable": "Yes"
                            }
                        }
                    },
                    "ipv6 unicast": {
                        "distance": {
                            "external": 20,
                            "internal": 200,
                            "local": 200
                        },
                        "sourced_networks": [
                            "2600:5400:7000:0:172:25:12:3/128",
                            "2600:5400:7000:8::/64",
                            "2600:5400:7000:21::/64"
                        ],
                        "neighbors": {
                            "2600:5400:7000:13::1": {
                                "last_update": "1w0d",
                                "nsr_state": "None",
                                "gr_enable": "Yes"
                            }
                        }
                    },
                    "ipv6 labeled-unicast": {
                        "distance": {
                            "external": 20,
                            "internal": 200,
                            "local": 200
                        },
                        "sourced_networks": [
                            "2600:5400:7000:0:172:25:12:3/128",
                            "2600:5400:7000:8::/64",
                            "2600:5400:7000:21::/64"
                        ],
                        "neighbors": {
                            "172.25.12.2": {
                                "last_update": "03:40:02",
                                "nsr_state": "None",
                                "gr_enable": "Yes"
                            },
                            "172.25.12.17": {
                                "last_update": "1w0d",
                                "nsr_state": "None",
                                "gr_enable": "Yes"
                            },
                            "172.25.12.18": {
                                "last_update": "1w0d",
                                "nsr_state": "None",
                                "gr_enable": "Yes"
                            }
                        }
                    },
                    "ipv4 mdt": {
                        "distance": {
                            "external": 20,
                            "internal": 200,
                            "local": 200
                        },
                        "neighbors": {
                            "172.25.12.19": {
                                "last_update": "Active",
                                "nsr_state": "None",
                                "gr_enable": "Yes"
                            }
                        }
                    },
                    "l2vpn vpls": {
                        "distance": {
                            "external": 20,
                            "internal": 200,
                            "local": 200
                        },
                        "neighbors": {
                            "172.25.12.2": {
                                "last_update": "03:40:02",
                                "nsr_state": "None",
                                "gr_enable": "Yes"
                            }
                        }
                    },
                    "l2vpn evpn": {
                        "distance": {
                            "external": 20,
                            "internal": 200,
                            "local": 200
                        },
                        "neighbors": {
                            "172.25.12.2": {
                                "last_update": "03:40:02",
                                "nsr_state": "None",
                                "gr_enable": "Yes"
                            }
                        }
                    }
                }
            },
            "ospf": {
                "vrf": {
                    "default": {
                        "address_family": {
                            "ipv4": {
                                "instance": {
                                    "1": {
                                        "router_id": "172.25.12.3",
                                        "preference": {
                                            "single_value": {
                                                "all": 110
                                            }
                                        },
                                        "nsf": True,
                                        "redistribution": {
                                            "bgp": {
                                                "bgp_id": 19108
                                            },
                                            "ospf": {
                                                "ospf_id": 99
                                            }
                                        },
                                        "areas": {
                                            "0.0.0.0": {
                                                "interfaces": [
                                                    "Bundle-Ether62000",
                                                    "Loopback0",
                                                    "Loopback46",
                                                    "TenGigE0/0/0/0",
                                                    "TenGigE0/0/0/2",
                                                    "GigabitEthernet0/0/1/18"
                                                ],
                                                "mpls": {
                                                    "te": {
                                                        "enable": True
                                                    }
                                                }
                                            },
                                            "0.0.0.111": {
                                                "interfaces": [
                                                    "GigabitEthernet0/0/1/19"
                                                ]
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "ospfv3": {
                "vrf": {
                    "default": {
                        "address_family": {
                            "ipv4": {
                                "instance": {
                                    "6": {
                                        "router_id": "172.25.12.3",
                                        "preference": {
                                            "single_value": {
                                                "all": 110
                                            }
                                        },
                                        "areas": {
                                            "0.0.0.0": {
                                                "interfaces": [
                                                    "TenGigE0/0/0/0",
                                                    "Loopback0"
                                                ]
                                            },
                                            "0.0.0.46": {
                                                "interfaces": []
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output3 = {'execute.return_value': '''
        +++ LAB-9010: executing command 'show protocols afi-all all' +++
        show protocols afi-all all

        Wed Apr 24 16:08:39.728 CDT

        Routing Protocol "BGP 19108"
        Non-stop routing is enabled
        Graceful restart is enabled
        Current BGP NSR state - Active Ready
        BGP NSR state not ready: Wait for standby ready msg

        Address Family IPv4 Unicast:
          Distance: external 20 internal 200 local 200
          Sourced Networks:
            10.10.10.0/30
            10.20.30.40/32
            10.24.24.8/30
            10.108.0.0/24
            10.249.130.0/25
            14.14.14.14/32
            19.10.8.0/24
            25.1.25.0/24
            66.76.44.142/31
            66.76.44.154/31
            66.76.44.156/31
            66.76.44.166/31
            66.76.44.192/31
            66.76.44.194/31
            66.76.44.202/31
            66.76.44.242/31
            66.76.44.244/31
            66.76.44.248/31
            66.76.150.240/28
            92.168.54.1/32
            100.64.0.0/21
            100.64.3.0/24
            169.254.1.0/30
            169.254.2.2/32
            169.254.11.0/24
          Routing Information Sources:
            Neighbor          State/Last update received  NSR-State  GR-Enabled
            66.76.44.130      03:35:21                    None         Yes
            172.25.12.2       03:40:02                    None         Yes
            172.25.12.17      1w0d                        None         Yes
            172.25.12.18      1w0d                        None         Yes
            172.25.12.19      Active                      None         Yes
            173.219.15.138    1w0d                        None         Yes
            173.219.15.139    1w0d                        None         Yes

        Address Family VPNv4 Unicast:
          Distance: external 20 internal 200 local 200
          Routing Information Sources:
            Neighbor          State/Last update received  NSR-State  GR-Enabled
            172.25.12.2       03:40:02                    None         Yes
            172.25.12.17      1w0d                        None         Yes
            172.25.12.18      1w0d                        None         Yes

        Address Family IPv6 Unicast:
          Distance: external 20 internal 200 local 200
          Sourced Networks:
            2600:5400:7000:0:172:25:12:3/128
            2600:5400:7000:8::/64
            2600:5400:7000:21::/64
          Routing Information Sources:
            Neighbor                                        State/Last update received  NSR-State  GR-Enabled
            2600:5400:7000:13::1                            1w0d                        None         Yes

        Address Family IPv6 Labeled-unicast:
          Distance: external 20 internal 200 local 200
          Sourced Networks:
            2600:5400:7000:0:172:25:12:3/128
            2600:5400:7000:8::/64
            2600:5400:7000:21::/64
          Routing Information Sources:
            Neighbor                                        State/Last update received  NSR-State  GR-Enabled
            172.25.12.2                                     03:40:02                    None         Yes
            172.25.12.17                                    1w0d                        None         Yes
            172.25.12.18                                    1w0d                        None         Yes

        Address Family IPv4 MDT:
          Distance: external 20 internal 200 local 200
          Routing Information Sources:
            Neighbor          State/Last update received  NSR-State  GR-Enabled
            172.25.12.19      Active                      None         Yes

        Address Family L2VPN VPLS:
          Distance: external 20 internal 200 local 200
          Routing Information Sources:
            Neighbor          State/Last update received  NSR-State  GR-Enabled
            172.25.12.2       03:40:02                    None         Yes

        Address Family L2VPN EVPN:
          Distance: external 20 internal 200 local 200
          Routing Information Sources:
            Neighbor          State/Last update received  NSR-State  GR-Enabled
            172.25.12.2       03:40:02                    None         Yes


        Routing Protocol OSPF 1
          Router Id: 172.25.12.3
          Distance: 110
          Non-Stop Forwarding: Enabled
          Redistribution:
            bgp 19108
            ospf 99
          Area 0
            MPLS/TE enabled
            Bundle-Ether62000
            Loopback0
            Loopback46
            TenGigE0/0/0/0
            TenGigE0/0/0/2
            GigabitEthernet0/0/1/18
          Area 111
            GigabitEthernet0/0/1/19
              authentication md5

        Routing Protocol OSPFv3 6
          Router Id: 172.25.12.3
          Distance: 110
          Graceful Restart: Enabled
          Redistribution:
            None
          Area 0
            TenGigE0/0/0/0
            Loopback0
          Area 46
        RP/0/RSP0/CPU0:LAB-9010#
    '''}

    def test_show_protocols_afi_all_all_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowProtocolsAfiAllAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_protocols_afi_all_all_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowProtocolsAfiAllAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_protocols_afi_all_all_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowProtocolsAfiAllAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_protocols_afi_all_all_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowProtocolsAfiAllAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
