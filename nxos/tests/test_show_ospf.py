
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Parser
from parser.nxos.show_ospf import ShowIpOspf, \
                                  ShowIpOspfMplsLdpInterface, \
                                  ShowIpOspfVirtualLinks, \
                                  ShowIpOspfShamLinks

# Metaparser
from metaparser.util.exceptions import SchemaEmptyParserError

# =============================================================
#  Unit test for 'show ip ospf'
#  Unit test for 'show ip ospf vrf all'
# =============================================================

class test_show_ip_ospf(unittest.TestCase):

    '''Unit test for show ip ospf
       Unit test for show ip ospf vrf all'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "vrf": {
              "VRF1": {
                   "address_family": {
                        "ipv4": {
                             "instance": {
                                  "1": {
                                       "single_tos_routes_enable": True,
                                       "nsr": {
                                            "enable": True
                                       },
                                       "router_id": "22.22.22.22",
                                       "enable": True,
                                       "spf_control": {
                                            "throttle": {
                                                 "lsa": {
                                                      "start": 0,
                                                      "checksum": "0",
                                                      "opaque_as_checksum": "0",
                                                      "external": 0,
                                                      "hold": 5000000,
                                                      "opaque_as": 0,
                                                      "maximum": 5000000,
                                                      "group_pacing": 10
                                                 },
                                                 "spf": {
                                                      "start": 200000,
                                                      "hold": 1000000,
                                                      "maximum": 5000000
                                                 }
                                            },
                                            "paths": 8
                                       },
                                       "area": {
                                            "0.0.0.1": {
                                                 "ranges": {
                                                      "advertise": False,
                                                      "net": 1,
                                                      "prefix": "1.1.0.0/16",
                                                      "cost": 31
                                                 },
                                                 "area_type": "stub",
                                                 "existed": "08:30:42",
                                                 "area_id": "0.0.0.1",
                                                 "default_cost": 1,
                                                 "statistics": {
                                                      "spf_last_run_time": 0.000464,
                                                      "spf_runs_count": 33,
                                                      "area_scope_lsa_count": 11,
                                                      "area_scope_lsa_cksum_sum": "11"
                                                 },
                                                 "number": {
                                                      "passive_interfaces": 0,
                                                      "loopback_interfaces": 0,
                                                      "active_interfaces": 3,
                                                      "interfaces": 3
                                                 }
                                            }
                                       },

                                       "instance": 1,
                                       "graceful_restart": {
                                            "ietf": {
                                                 "type": "ietf",
                                                 "exist_status": "none",
                                                 "enable": True,
                                                 "restart_interval": 60
                                            }
                                       },
                                       "opaque_lsa_enable": True,
                                       "preference": {
                                            "single_value": {
                                                 "all": 110
                                            }
                                       },
                                       "numbers": {
                                            "areas": {
                                                 "normal": 1,
                                                 "nssa": 0,
                                                 "stub": 0,
                                                 "number": 1
                                            },
                                            "active_areas": {
                                                 "normal": 1,
                                                 "nssa": 0,
                                                 "stub": 0,
                                                 "number": 1
                                            }
                                       },
                                       "auto_cost": {
                                            "reference_bandwidth": 40000,
                                            "bandwidth_unit": "Mbps",
                                            "enable": True
                                       }
                                  }
                             }
                        }
                   }
              },
              "default": {
                   "address_family": {
                        "ipv4": {
                             "instance": {
                                  "1": {
                                       "single_tos_routes_enable": True,
                                       "nsr": {
                                            "enable": True
                                       },
                                       "router_id": "2.2.2.2",
                                       "enable": True,
                                       "spf_control": {
                                            "throttle": {
                                                 "lsa": {
                                                      "start": 0,
                                                      "checksum": "0x7d61",
                                                      "opaque_as_checksum": "0",
                                                      "external": 1,
                                                      "hold": 5000000,
                                                      "opaque_as": 0,
                                                      "maximum": 5000000,
                                                      "group_pacing": 10
                                                 },
                                                 "spf": {
                                                      "start": 200000,
                                                      "hold": 1000000,
                                                      "maximum": 5000000
                                                 }
                                            },
                                            "paths": 8
                                       },
                                       "instance": 1,
                                       "stub_router": {
                                            "always": {
                                                 "always": True
                                            }
                                       },
                                       "database_control": {
                                            "max_lsa": 123
                                       },
                                       "opaque_lsa_enable": True,
                                       "bfd": {
                                            "enable": True
                                       },
                                       "numbers": {
                                            "areas": {
                                                 "normal": 1,
                                                 "nssa": 0,
                                                 "stub": 0,
                                                 "number": 1
                                            },
                                            "active_areas": {
                                                 "normal": 1,
                                                 "nssa": 0,
                                                 "stub": 0,
                                                 "number": 1
                                            }
                                       },
                                       "graceful_restart": {
                                            "ietf": {
                                                 "type": "ietf",
                                                 "exist_status": "none",
                                                 "enable": True,
                                                 "restart_interval": 60
                                            }
                                       },
                                       "area": {
                                            "0.0.0.0": {
                                                 "ranges": {
                                                      "advertise": True,
                                                      "net": 0,
                                                      "prefix": "1.1.1.0/24",
                                                      "cost": 33
                                                 },
                                                 "area_type": "normal",
                                                 "existed": "08:30:42",
                                                 "area_id": "0.0.0.0",
                                                 "statistics": {
                                                      "spf_last_run_time": 0.001386,
                                                      "spf_runs_count": 8,
                                                      "area_scope_lsa_count": 19,
                                                      "area_scope_lsa_cksum_sum": "19"
                                                 },
                                                 "number": {
                                                      "passive_interfaces": 0,
                                                      "loopback_interfaces": 1,
                                                      "active_interfaces": 4,
                                                      "interfaces": 4
                                                 }
                                            }
                                       },
                                       "auto_cost": {
                                            "reference_bandwidth": 40000,
                                            "bandwidth_unit": "Mbps",
                                            "enable": True
                                       },
                                       "preference": {
                                            "single_value": {
                                                 "all": 110
                                            }
                                       }
                                  }
                             }
                        }
                   }
              }
         }
    }

    golden_output = {'execute.return_value': '''
        Routing Process 1 with ID 2.2.2.2 VRF default
        Routing Process Instance Number 1
        Stateful High Availability enabled
        Graceful-restart is configured
        Grace period: 60 state: Inactive
        BFD is enabled
        Last graceful restart exit status: None
        Supports only single TOS(TOS0) routes
        Supports opaque LSA
        Administrative distance 110
        Originating router LSA with maximum metric
        Reference Bandwidth is 40000 Mbps
        SPF throttling delay time of 200.000 msecs,
        SPF throttling hold time of 1000.000 msecs, 
        SPF throttling maximum wait time of 5000.000 msecs
        LSA throttling start time of 0.000 msecs,
        LSA throttling hold interval of 5000.000 msecs, 
        LSA throttling maximum wait time of 5000.000 msecs
        Minimum LSA arrival 1000.000 msec
        LSA group pacing timer 10 secs
        Maximum number of non self-generated LSA allowed 123
        Maximum paths to destination 8
        Number of external LSAs 1, checksum sum 0x7d61
        Number of opaque AS LSAs 0, checksum sum 0
        Number of areas is 1, 1 normal, 0 stub, 0 nssa
        Number of active areas is 1, 1 normal, 0 stub, 0 nssa
        Install discard route for summarized external routes.
        Install discard route for summarized internal routes.
        Area BACKBONE(0.0.0.0) 
            Area has existed for 08:30:42
            Interfaces in this area: 4 Active interfaces: 4
            Passive interfaces: 0  Loopback interfaces: 1
            No authentication available
            SPF calculation has run 8 times
             Last SPF ran for 0.001386s
            Area ranges are
            1.1.1.0/24 Passive (Num nets: 0) Advertise Cost configured 33
            Number of LSAs: 19, checksum sum 0x7a137

        Routing Process 1 with ID 22.22.22.22 VRF VRF1
        Routing Process Instance Number 1
        Domain ID type 0x0005, Value 0.0.0.0
        Stateful High Availability enabled
        Graceful-restart is configured
        Grace period: 60 state: Inactive 
        Last graceful restart exit status: None
        Supports only single TOS(TOS0) routes
        Supports opaque LSA
        This router is an area border and autonomous system boundary.
        Redistributing External Routes from
        bgp-100
        Administrative distance 110
        Reference Bandwidth is 40000 Mbps
        SPF throttling delay time of 200.000 msecs,
        SPF throttling hold time of 1000.000 msecs, 
        SPF throttling maximum wait time of 5000.000 msecs
        LSA throttling start time of 0.000 msecs,
        LSA throttling hold interval of 5000.000 msecs, 
        LSA throttling maximum wait time of 5000.000 msecs
        Minimum LSA arrival 1000.000 msec
        LSA group pacing timer 10 secs
        Maximum paths to destination 8
        Number of external LSAs 0, checksum sum 0
        Number of opaque AS LSAs 0, checksum sum 0
        Number of areas is 1, 1 normal, 0 stub, 0 nssa
        Number of active areas is 1, 1 normal, 0 stub, 0 nssa
        Install discard route for summarized external routes.
        Install discard route for summarized internal routes.
        Area (0.0.0.1)
            This area is a STUB area
            Generates stub default route with cost 1
            Area has existed for 08:30:42
            Interfaces in this area: 3 Active interfaces: 3
            Passive interfaces: 0  Loopback interfaces: 0
            No authentication available
            SPF calculation has run 33 times
             Last SPF ran for 0.000464s
            Area ranges are
            1.1.0.0/16 Active (Num nets: 1) DoNotAdvertise Cost configured 31
            Number of LSAs: 11, checksum sum 0x527f9
        '''}

    golden_parsed_output_1 = {
        "vrf": {
              "default": {
                   "address_family": {
                        "ipv4": {
                             "instance": {
                                  "1": {
                                       "area": {
                                            "0.0.0.0": {
                                                 "area_id": "0.0.0.0",
                                                 "area_type": "normal",
                                                 "number": {
                                                      "interfaces": 6,
                                                      "loopback_interfaces": 4,
                                                      "passive_interfaces": 0,
                                                      "active_interfaces": 4
                                                 },
                                                 "statistics": {
                                                      "spf_runs_count": 2,
                                                      "spf_last_run_time": 0.000447,
                                                      "area_scope_lsa_cksum_sum": "1",
                                                      "area_scope_lsa_count": 1
                                                 },
                                                 "existed": "1w5d"
                                            }
                                       },
                                       "preference": {
                                            "single_value": {
                                                 "all": 110
                                            }
                                       },
                                       "spf_control": {
                                            "throttle": {
                                                 "lsa": {
                                                      "start": 0,
                                                      "opaque_as_checksum": "0",
                                                      "checksum": "0",
                                                      "hold": 5000000,
                                                      "group_pacing": 10,
                                                      "external": 0,
                                                      "maximum": 5000000,
                                                      "opaque_as": 0
                                                 },
                                                 "spf": {
                                                      "start": 200000,
                                                      "maximum": 5000000,
                                                      "hold": 1000000
                                                 }
                                            },
                                            "paths": 8
                                       },
                                       "graceful_restart": {
                                            "ietf": {
                                                 "exist_status": "none",
                                                 "restart_interval": 60,
                                                 "type": "ietf",
                                                 "enable": True
                                            }
                                       },
                                       "opaque_lsa_enable": True,
                                       "numbers": {
                                            "active_areas": {
                                                 "stub": 0,
                                                 "normal": 1,
                                                 "number": 1,
                                                 "nssa": 0
                                            },
                                            "areas": {
                                                 "stub": 0,
                                                 "normal": 1,
                                                 "number": 1,
                                                 "nssa": 0
                                            }
                                       },
                                       "nsr": {
                                            "enable": True
                                       },
                                       "instance": 1,
                                       "router_id": "2.2.2.2",
                                       "single_tos_routes_enable": True,
                                       "auto_cost": {
                                            "reference_bandwidth": 40000,
                                            "bandwidth_unit": "Mbps",
                                            "enable": True
                                       },
                                       "enable": False
                                  }
                             }
                        }
                   }
              }
         }
    }

    golden_output_1 = {'execute.return_value': '''
        Routing Process 1 with ID 2.2.2.2 VRF default
        Routing Process Instance Number 1
        Stateful High Availability enabled
        Graceful-restart is configured
        Grace period: 60 state: Inactive 
        Last graceful restart exit status: None
        Supports only single TOS(TOS0) routes
        Supports opaque LSA
        Administrative distance 110
        Reference Bandwidth is 40000 Mbps
        SPF throttling delay time of 200.000 msecs,
        SPF throttling hold time of 1000.000 msecs, 
        SPF throttling maximum wait time of 5000.000 msecs
        LSA throttling start time of 0.000 msecs,
        LSA throttling hold interval of 5000.000 msecs, 
        LSA throttling maximum wait time of 5000.000 msecs
        Minimum LSA arrival 1000.000 msec
        LSA group pacing timer 10 secs
        Maximum paths to destination 8
        Number of external LSAs 0, checksum sum 0
        Number of opaque AS LSAs 0, checksum sum 0
        Number of areas is 1, 1 normal, 0 stub, 0 nssa
        Number of active areas is 1, 1 normal, 0 stub, 0 nssa
        Install discard route for summarized external routes.
        Install discard route for summarized internal routes.
        Area BACKBONE(0.0.0.0) (Inactive)
            Area has existed for 1w5d
            Interfaces in this area: 6 Active interfaces: 4
            Passive interfaces: 0  Loopback interfaces: 4
            No authentication available
            SPF calculation has run 2 times
             Last SPF ran for 0.000447s
            Area ranges are
            Number of LSAs: 1, checksum sum 0x9ccb
        '''
    }

    def test_vrf_all(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpOspf(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_default_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpOspf(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

# =============================================================
#  Unit test for 'show ip ospf mpls ldp interface'
#  Unit test for 'show ip ospf mpls ldp interface vrf all'
# =============================================================

class test_show_ip_ospf_mpls_ldp_interface(unittest.TestCase):

    '''Unit test for show ip ospf mpls ldp interface
       Unit test for show ip ospf mpls ldp interface vrf all'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "vrf": {
              "VRF1": {
                   "address_family": {
                        "ipv4": {
                             "instance": {
                                  "1": {
                                       "interface": {
                                            "Ethernet2/1": {
                                                 "ldp": {
                                                      "autoconfig": False,
                                                      "igp_sync": False,
                                                      "autoconfig_area_id": "0.0.0.1"
                                                 },
                                                 "interface": "Ethernet2/1",
                                                 "network_type": "broadcast",
                                                 "state": "bdr",
                                                 "area": "0.0.0.1"
                                            },
                                            "SL2-0.0.0.0-22.22.22.22-33.33.33.33": {
                                                 "ldp": {
                                                      "autoconfig": False,
                                                      "igp_sync": False,
                                                      "autoconfig_area_id": "0.0.0.1"
                                                 },
                                                 "interface": "SL2-0.0.0.0-22.22.22.22-33.33.33.33",
                                                 "network_type": "p2p",
                                                 "state": "p2p",
                                                 "area": "0.0.0.1"
                                            },
                                            "SL1-0.0.0.0-22.22.22.22-11.11.11.11": {
                                                 "ldp": {
                                                      "autoconfig": False,
                                                      "igp_sync": False,
                                                      "autoconfig_area_id": "0.0.0.1"
                                                 },
                                                 "interface": "SL1-0.0.0.0-22.22.22.22-11.11.11.11",
                                                 "network_type": "p2p",
                                                 "state": "p2p",
                                                 "area": "0.0.0.1"
                                            }
                                       }
                                  }
                             }
                        }
                   }
              },
              "default": {
                   "address_family": {
                        "ipv4": {
                             "instance": {
                                  "1": {
                                       "interface": {
                                            "loopback0": {
                                                 "ldp": {
                                                      "autoconfig": False,
                                                      "igp_sync": False,
                                                      "autoconfig_area_id": "0.0.0.0"
                                                 },
                                                 "interface": "loopback0",
                                                 "network_type": "loopback",
                                                 "state": "loopback",
                                                 "area": "0.0.0.0"
                                            },
                                            "Ethernet2/4": {
                                                 "ldp": {
                                                      "autoconfig": False,
                                                      "igp_sync": False,
                                                      "autoconfig_area_id": "0.0.0.0"
                                                 },
                                                 "interface": "Ethernet2/4",
                                                 "network_type": "broadcast",
                                                 "state": "bdr",
                                                 "area": "0.0.0.0"
                                            },
                                            "Ethernet2/2": {
                                                 "ldp": {
                                                      "autoconfig": False,
                                                      "igp_sync": False,
                                                      "autoconfig_area_id": "0.0.0.0"
                                                 },
                                                 "interface": "Ethernet2/2",
                                                 "network_type": "broadcast",
                                                 "state": "bdr",
                                                 "area": "0.0.0.0"
                                            },
                                            "Ethernet2/3": {
                                                 "ldp": {
                                                      "autoconfig": False,
                                                      "igp_sync": False,
                                                      "autoconfig_area_id": "0.0.0.0"
                                                 },
                                                 "interface": "Ethernet2/3",
                                                 "network_type": "broadcast",
                                                 "state": "bdr",
                                                 "area": "0.0.0.0"
                                            }
                                       }
                                  }
                             }
                        }
                   }
              }
         }
    }

    golden_output = {'execute.return_value': '''
        loopback0 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State LOOPBACK, Network type LOOPBACK
        Ethernet2/2 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State BDR, Network type BROADCAST
        Ethernet2/3 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State BDR, Network type BROADCAST
        Ethernet2/4 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State BDR, Network type BROADCAST
        Ethernet2/1 - Process ID 1 VRF VRF1, area 0.0.0.1
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State BDR, Network type BROADCAST
        SL1-0.0.0.0-22.22.22.22-11.11.11.11 - Process ID 1 VRF VRF1, area 0.0.0.1
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State P2P, Network type P2P
        SL2-0.0.0.0-22.22.22.22-33.33.33.33 - Process ID 1 VRF VRF1, area 0.0.0.1
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State P2P, Network type P2P
    '''}

    golden_parsed_output_1 = {
        "vrf": {
              "default": {
                   "address_family": {
                        "ipv4": {
                             "instance": {
                                  "1": {
                                       "interface": {
                                            "Ethernet4/1": {
                                                 "ldp": {
                                                      "autoconfig": False,
                                                      "igp_sync": False,
                                                      "autoconfig_area_id": "0.0.0.0"
                                                 },
                                                 "interface": "Ethernet4/1",
                                                 "network_type": "broadcast",
                                                 "state": "down",
                                                 "area": "0.0.0.0"
                                            },
                                            "loopback3": {
                                                 "ldp": {
                                                      "autoconfig": False,
                                                      "igp_sync": False,
                                                      "autoconfig_area_id": "0.0.0.0"
                                                 },
                                                 "interface": "loopback3",
                                                 "network_type": "loopback",
                                                 "state": "loopback",
                                                 "area": "0.0.0.0"
                                            },
                                            "loopback4": {
                                                 "ldp": {
                                                      "autoconfig": False,
                                                      "igp_sync": False,
                                                      "autoconfig_area_id": "0.0.0.0"
                                                 },
                                                 "interface": "loopback4",
                                                 "network_type": "loopback",
                                                 "state": "loopback",
                                                 "area": "0.0.0.0"
                                            },
                                            "loopback1": {
                                                 "ldp": {
                                                      "autoconfig": False,
                                                      "igp_sync": False,
                                                      "autoconfig_area_id": "0.0.0.0"
                                                 },
                                                 "interface": "loopback1",
                                                 "network_type": "loopback",
                                                 "state": "loopback",
                                                 "area": "0.0.0.0"
                                            },
                                            "Ethernet4/10": {
                                                 "ldp": {
                                                      "autoconfig": False,
                                                      "igp_sync": False,
                                                      "autoconfig_area_id": "0.0.0.0"
                                                 },
                                                 "interface": "Ethernet4/10",
                                                 "network_type": "broadcast",
                                                 "state": "down",
                                                 "area": "0.0.0.0"
                                            },
                                            "loopback2": {
                                                 "ldp": {
                                                      "autoconfig": False,
                                                      "igp_sync": False,
                                                      "autoconfig_area_id": "0.0.0.0"
                                                 },
                                                 "interface": "loopback2",
                                                 "network_type": "loopback",
                                                 "state": "loopback",
                                                 "area": "0.0.0.0"
                                            }
                                       }
                                  }
                             }
                        }
                   }
              }
         }
    }

    golden_output_1 = {'execute.return_value': '''
        Ethernet4/1 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State DOWN, Network type BROADCAST
        Ethernet4/10 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State DOWN, Network type BROADCAST
        loopback1 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State LOOPBACK, Network type LOOPBACK
        loopback2 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State LOOPBACK, Network type LOOPBACK
        loopback3 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State LOOPBACK, Network type LOOPBACK
        loopback4 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State LOOPBACK, Network type LOOPBACK
        '''
    }

    def test_vrf_all(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpOspfMplsLdpInterface(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfMplsLdpInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_default_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpOspfMplsLdpInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# =============================================================
#  Unit test for 'show ip ospf virtual-links'
#  Unit test for 'show ip ospf virtual-links vrf all'
# =============================================================

class test_show_ip_ospf_virtual_links(unittest.TestCase):

    '''Unit test for show ip ospf virtual-links
       Unit test for show ip ospf virtual-links vrf all'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "vrf": {
              "default": {
                   "address_family": {
                        "ipv4": {
                             "instance": {
                                  "1": {
                                       "area": {
                                            "0.0.0.1": {
                                                 "virtual_links": {
                                                      "0.0.0.1 4.4.4.4": {
                                                           "dead_interval": 40,
                                                           "network_type": "P2P",
                                                           "interface": "Ethernet1/5",
                                                           "backbone_area_id": "0.0.0.0",
                                                           "wait_interval": 40,
                                                           "hello_timer": "00:00:05",
                                                           "neighbors": {
                                                                "4.4.4.4": {
                                                                     "last_change": "00:07:51",
                                                                     "address": "20.3.4.4",
                                                                     "state": "full",
                                                                     "neighbor_router_id": "4.4.4.4",
                                                                     "dbd_option": "0x72",
                                                                     "last_non_hello_received": "00:07:49",
                                                                     "statistics": {
                                                                          "nbr_event_count": 5
                                                                     },
                                                                     "dead_timer": "00:00:33",
                                                                     "hello_option": "0x32"
                                                                }
                                                           },
                                                           "transmit_delay": 1,
                                                           "ip_address": "20.3.4.3",
                                                           "statistics": {
                                                                "link_scope_lsa_count": 0,
                                                                "link_scope_lsa_cksum_sum": 0
                                                           },
                                                           "unnumbered_interface": "Ethernet1/5",
                                                           "state": "P2P",
                                                           "index": 7,
                                                           "remote_addr": "20.3.4.4",
                                                           "hello_interval": 10,
                                                           "link": "VL1",
                                                           "router_id": "4.4.4.4",
                                                           "transit_area_id": "0.0.0.1",
                                                           "retransmit_interval": 5,
                                                           "link_state": "up",
                                                           "cost": 40
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

    golden_output = {'execute.return_value': '''        
        Virtual link VL1 to router 4.4.4.4 is up
            Transit area 0.0.0.1, via interface Eth1/5, remote addr 20.3.4.4
            Unnumbered interface using IP address of Ethernet1/5 (20.3.4.3)
            Process ID 1 VRF default, area 0.0.0.0
            State P2P, Network type P2P, cost 40
            Index 7, Transmit delay 1 sec
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:05
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
            Adjacency Information
            State is FULL, 5 state changes, last change 00:07:51
            Hello options 0x32, dbd options 0x72
            Last non-hello packet received 00:07:49
              Dead timer due in 00:00:33
    '''}

    def test_vrf_all(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpOspfVirtualLinks(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfVirtualLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =============================================================
#  Unit test for 'show ip ospf sham-links'
#  Unit test for 'show ip ospf sham-links vrf all'
# =============================================================

class test_show_ip_ospf_sham_links(unittest.TestCase):

    '''Unit test for show ip ospf sham-links
       Unit test for show ip ospf sham-links vrf all'''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "vrf": {
              "VRF1": {
                   "address_family": {
                        "ipv4": {
                             "instance": {
                                  "1": {
                                       "area": {
                                            "0.0.0.1": {
                                                 "sham_links": {
                                                      "22.22.22.22 11.11.11.11": {
                                                           "hello_interval": 10,
                                                           "transmit_delay": 1,
                                                           "unnumbered_interface": "loopback1",
                                                           "link": "SL1",
                                                           "neighbors": {
                                                                "11.11.11.11": {
                                                                     "neighbor_router_id": "11.11.11.11",
                                                                     "address": "11.11.11.11",
                                                                     "dbd_option": "0x72",
                                                                     "last_non_hello_received": "never",
                                                                     "remote": "11.11.11.11",
                                                                     "backbone_area_id": "0.0.0.0",
                                                                     "state": "full",
                                                                     "area": "0.0.0.1",
                                                                     "hello_option": "0x32",
                                                                     "local": "22.22.22.22",
                                                                     "statistics": {
                                                                          "nbr_event_count": 8
                                                                     },
                                                                     "instance": "1",
                                                                     "dead_timer": "00:00:38",
                                                                     "last_change": "08:10:01"
                                                                }
                                                           },
                                                           "index": 6,
                                                           "local_id": "22.22.22.22",
                                                           "retransmit_interval": 5,
                                                           "hello_timer": "00:00:02",
                                                           "cost": 1,
                                                           "dead_interval": 40,
                                                           "ip_address": "22.22.22.22",
                                                           "backbone_area_id": "0.0.0.0",
                                                           "state": "P2P",
                                                           "wait_interval": 40,
                                                           "transit_area_id": "0.0.0.1",
                                                           "network_type": "P2P",
                                                           "link_state": "up",
                                                           "statistics": {
                                                                "link_scope_lsa_count": 0,
                                                                "link_scope_lsa_cksum_sum": 0
                                                           },
                                                           "destination": "11.11.11.11",
                                                           "remote_id": "11.11.11.11"
                                                      },
                                                      "22.22.22.22 33.33.33.33": {
                                                           "hello_interval": 3,
                                                           "transmit_delay": 7,
                                                           "unnumbered_interface": "loopback1",
                                                           "link": "SL2",
                                                           "index": 7,
                                                           "local_id": "22.22.22.22",
                                                           "retransmit_interval": 5,
                                                           "hello_timer": "00:00:01",
                                                           "cost": 111,
                                                           "dead_interval": 13,
                                                           "ip_address": "22.22.22.22",
                                                           "backbone_area_id": "0.0.0.0",
                                                           "state": "P2P",
                                                           "wait_interval": 13,
                                                           "transit_area_id": "0.0.0.1",
                                                           "network_type": "P2P",
                                                           "link_state": "up",
                                                           "statistics": {
                                                                "link_scope_lsa_count": 0,
                                                                "link_scope_lsa_cksum_sum": 0
                                                           },
                                                           "authentication": {
                                                                "auth_trailer_key": {
                                                                     "crypto_algorithm": "simple"
                                                                },
                                                                "auth_trailer_key_chain": {
                                                                     "key_chain": "test",
                                                                     "status": "ready"
                                                                }
                                                           },
                                                           "destination": "33.33.33.33",
                                                           "remote_id": "33.33.33.33"
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

    golden_output = {'execute.return_value': '''        
        SL1-0.0.0.0-22.22.22.22-11.11.11.11 line protocol is up
            Unnumbered interface using IP address of loopback1 (22.22.22.22)
            Process ID 1 VRF VRF1, area 0.0.0.1
            State P2P, Network type P2P, cost 1
            Index 6, Transmit delay 1 sec
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:02
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
            Adjacency Information :
            Destination IP address: 11.11.11.11
         Neighbor 11.11.11.11, interface address 11.11.11.11
            Process ID 1 VRF VRF1, in area 0.0.0.1 via interface SL1-0.0.0.0-22.22.22.22
        -11.11.11.11
            State is FULL, 8 state changes, last change 08:10:01
            Hello options 0x32, dbd options 0x72
            Last non-hello packet received never
              Dead timer due in 00:00:38

         SL2-0.0.0.0-22.22.22.22-33.33.33.33 line protocol is up
            Unnumbered interface using IP address of loopback1 (22.22.22.22)
            Process ID 1 VRF VRF1, area 0.0.0.1
            State P2P, Network type P2P, cost 111
            Index 7, Transmit delay 7 sec
            0 Neighbors, flooding to 0, adjacent with 0
            Timer intervals: Hello 3, Dead 13, Wait 13, Retransmit 5
              Hello timer due in 00:00:01
            Simple authentication, using keychain test (ready)
            Number of opaque link LSAs: 0, checksum sum 0
            Adjacency Information :
            Destination IP address: 33.33.33.33
    '''}

    def test_vrf_all(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpOspfShamLinks(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfShamLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()




if __name__ == '__main__':
    unittest.main()


# vim: ft=python et sw=4
