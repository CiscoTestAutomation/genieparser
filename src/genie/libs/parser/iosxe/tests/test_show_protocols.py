# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# iosxe show_protocols
from genie.libs.parser.iosxe.show_protocols import (
    ShowIpProtocols,
    ShowIpProtocolsSectionRip,
    ShowIpv6ProtocolsSectionRip,
)

# =================================
# Unit test for 'show ip protocols'
# =================================
class TestShowIpProtocols(unittest.TestCase):
    maxDiff = None
    device = Device("aDevice")
    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        "protocols": {
            "application": {
                "flushed": 0,
                "holddown": 0,
                "incoming_filter_list": "not set",
                "invalid": 0,
                "maximum_path": 32,
                "outgoing_filter_list": "not set",
                "preference": {"single_value": {"all": 4}},
                "update_frequency": 0,
            },
            "bgp": {
                "instance": {
                    "default": {
                        "bgp_id": 100,
                        "vrf": {
                            "default": {
                                "address_family": {
                                    "ipv4": {
                                        "automatic_route_summarization": False,
                                        "igp_sync": False,
                                        "incoming_filter_list": "not set",
                                        "maximum_path": 1,
                                        "routing_information_sources": {
                                            "10.64.4.4": {
                                                "distance": 200,
                                                "last_update": "03:34:58",
                                                "neighbor_id": "10.64.4.4",
                                            }
                                        },
                                        "outgoing_filter_list": "not set",
                                        "preference": {
                                            "multi_values": {
                                                "external": 20,
                                                "internal": 200,
                                                "local": 200,
                                            }
                                        },
                                    }
                                }
                            }
                        },
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
                                        "areas": {
                                            "0.0.0.0": {
                                                "configured_interfaces": [
                                                    "Loopback0",
                                                    "GigabitEthernet2",
                                                    "GigabitEthernet1",
                                                ]
                                            }
                                        },
                                        "incoming_filter_list": "not set",
                                        "outgoing_filter_list": "not set",
                                        "preference": {
                                            "multi_values": {
                                                "external": 114,
                                                "granularity": {
                                                    "detail": {
                                                        "inter_area": 113,
                                                        "intra_area": 112,
                                                    }
                                                },
                                            },
                                            "single_value": {"all": 110},
                                        },
                                        "router_id": "10.4.1.1",
                                        "routing_information_sources": {
                                            "gateway": {
                                                "10.16.2.2": {
                                                    "distance": 110,
                                                    "last_update": "07:33:00",
                                                },
                                                "10.36.3.3": {
                                                    "distance": 110,
                                                    "last_update": "07:33:00",
                                                },
                                                "10.64.4.4": {
                                                    "distance": 110,
                                                    "last_update": "00:19:15",
                                                },
                                            }
                                        },
                                        "spf_control": {"paths": 4},
                                        "total_areas": 1,
                                        "total_normal_area": 1,
                                        "total_nssa_area": 0,
                                        "total_stub_area": 0,
                                    }
                                }
                            }
                        }
                    }
                }
            },
        }
    }

    golden_parsed_output_2 = {
        "protocols": {
            "application": {
                "update_frequency": 0,
                "invalid": 0,
                "holddown": 0,
                "flushed": 0,
                "outgoing_filter_list": "not set",
                "incoming_filter_list": "not set",
                "maximum_path": 32,
                "preference": {
                    "single_value": {
                        "all": 4}},
            },
            "ospf": {
                "vrf": {
                    "default": {
                        "address_family": {
                            "ipv4": {
                                "instance": {
                                    "1": {
                                        "outgoing_filter_list": "not set",
                                        "incoming_filter_list": "not set",
                                        "router_id": "192.168.0.10",
                                        "total_areas": 1,
                                        "total_normal_area": 1,
                                        "total_stub_area": 0,
                                        "total_nssa_area": 0,
                                        "spf_control": {"paths": 4},
                                        "network": {
                                            "10.0.0.84": {
                                                "netmask": "0.0.0.3",
                                                "area": "11",
                                            },
                                            "10.0.0.88": {
                                                "netmask": "0.0.0.3",
                                                "area": "11",
                                            },
                                            "192.168.0.10": {
                                                "netmask": "0.0.0.0",
                                                "area": "11",
                                            },
                                        },
                                        "passive_interfaces": ["Loopback0"],
                                        "routing_information_sources": {
                                            "gateway": {
                                                "192.168.0.9": {
                                                    "distance": 110,
                                                    "last_update": "01:36:38",
                                                }
                                            }
                                        },
                                        "preference": {
                                            "single_value": {
                                                "all": 110}},
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "bgp": {
                "instance": {
                    "default": {
                        "bgp_id": 1,
                        "vrf": {
                            "default": {
                                "address_family": {
                                    "ipv4": {
                                        "outgoing_filter_list": "not set",
                                        "incoming_filter_list": "not set",
                                        "igp_sync": False,
                                        "automatic_route_summarization": False,
                                        "neighbors": {
                                            "192.168.0.9": {}
                                        },
                                        "maximum_path": 1,
                                        "routing_information_sources": {
                                            "192.168.0.9": {
                                                "neighbor_id": "192.168.0.9",
                                                "distance": 200,
                                                "last_update": "01:35:12",
                                            }
                                        },
                                        "preference": {
                                            "multi_values": {
                                                "external": 20,
                                                "internal": 200,
                                                "local": 200,
                                            }
                                        },
                                    }
                                }
                            }
                        },
                    }
                }
            },
        }
    }

    golden_output_3 = {
        "execute.return_value": """
        show ip protocols
        *** IP Routing is NSF aware ***
        Routing Protocol is "application"
          Sending updates every 0 seconds
          Invalid after 0 seconds, hold down 0, flushed after 0
          Outgoing update filter list for all interfaces is not set
          Incoming update filter list for all interfaces is not set
          Maximum path: 32
          Routing for Networks:
          Routing Information Sources:
            Gateway         Distance      Last Update
          Distance: (default is 4)
        Routing Protocol is "isis banana"
          Outgoing update filter list for all interfaces is not set
          Incoming update filter list for all interfaces is not set
          Redistributing: isis banana
          Address Summarization:
            None
          Maximum path: 4
          Routing for Networks:
            TenGigabitEthernet0/0/26
            TenGigabitEthernet0/0/27
          Passive Interface(s):
            Loopback0
          Routing Information Sources:
            Gateway         Distance      Last Update
            10.60.6.3            115      05:56:34
            10.60.6.2            115      05:56:34
            10.60.6.4            115      05:56:34
            10.60.6.9            115      05:56:34
          Distance: (default is 115)
        Routing Protocol is "bgp 9999"
          Outgoing update filter list for all interfaces is not set
          Incoming update filter list for all interfaces is not set
          IGP synchronization is disabled
          Automatic route summarization is disabled
          Maximum path: 1
          Routing Information Sources:
            Gateway         Distance      Last Update
            10.60.6.3            200      12w5d
            10.60.6.2            200      14w4d
          Distance: external 20 internal 200 local 200
        """
    }

    golden_parsed_output_3 = {
        "protocols": {
            "application": {
                "flushed": 0,
                "holddown": 0,
                "incoming_filter_list": "not set",
                "invalid": 0,
                "maximum_path": 32,
                "outgoing_filter_list": "not set",
                "preference": {
                    "single_value": {
                        "all": 4}},
                "update_frequency": 0,
            },
            "bgp": {
                "instance": {
                    "default": {
                        "bgp_id": 9999,
                        "vrf": {
                            "default": {
                                "address_family": {
                                    "ipv4": {
                                        "automatic_route_summarization": False,
                                        "igp_sync": False,
                                        "incoming_filter_list": "not set",
                                        "maximum_path": 1,
                                        "routing_information_sources": {
                                            "10.60.6.2": {
                                                "distance": 200,
                                                "last_update": "14w4d",
                                                "neighbor_id": "10.60.6.2",
                                            },
                                            "10.60.6.3": {
                                                "distance": 200,
                                                "last_update": "12w5d",
                                                "neighbor_id": "10.60.6.3",
                                            },
                                        },
                                        "outgoing_filter_list": "not set",
                                        "preference": {
                                            "multi_values": {
                                                "external": 20,
                                                "internal": 200,
                                                "local": 200,
                                            }
                                        },
                                    }
                                }
                            }
                        },
                    }
                }
            },
            "isis": {
                "vrf": {
                    "default": {
                        "address_family": {
                            "ipv4": {
                                "instance": {
                                    "banana": {
                                        "configured_interfaces": [
                                            "TenGigabitEthernet0/0/26",
                                            "TenGigabitEthernet0/0/27",
                                        ],
                                        "incoming_filter_list": "not set",
                                        "maximum_path": 4,
                                        "outgoing_filter_list": "not set",
                                        "passive_interfaces": ["Loopback0"],
                                        "preference": {
                                            "single_value": {"all": 115}
                                        },
                                        "redistributing": "isis banana",
                                        "routing_information_sources": {
                                            "gateway": {
                                                "10.60.6.2": {
                                                    "distance": 115,
                                                    "last_update": "05:56:34",
                                                },
                                                "10.60.6.3": {
                                                    "distance": 115,
                                                    "last_update": "05:56:34",
                                                },
                                                "10.60.6.4": {
                                                    "distance": 115,
                                                    "last_update": "05:56:34",
                                                },
                                                "10.60.6.9": {
                                                    "distance": 115,
                                                    "last_update": "05:56:34",
                                                },
                                            }
                                        },
                                    }
                                }
                            }
                        }
                    }
                }
            },
        }
    }

    golden_output_4 = {
        "execute.return_value": """
        Router# show ip protocols
        *** IP Routing is NSF aware ***
        Routing Protocol is "isis"
          Sending updates every 0 seconds
          Invalid after 0 seconds, hold down 0, flushed after 0
          Outgoing update filter list for all interfaces is not set
          Incoming update filter list for all interfaces is not set
          Redistributing: isis
          Address Summarization:
            None
          Routing for Networks:
            Serial0
          Routing Information Sources:
          Distance: (default is 115)
        """
    }

    golden_parsed_output_4 = {
        "protocols": {
            "isis": {
                "vrf": {
                    "default": {
                        "address_family": {
                            "ipv4": {
                                "instance": {
                                    "default": {
                                        "outgoing_filter_list": "not set",
                                        "incoming_filter_list": "not set",
                                        "redistributing": "isis",
                                        "configured_interfaces": ["Serial0"],
                                        "preference": {
                                            "single_value": {
                                                "all": 115
                                            }
                                        },
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_parsed_output_5 = {
        "protocols": {
            "rip": {
                "vrf": {
                    "default": {
                        "address_family": {
                            "ipv4": {
                                "instance": {
                                    "rip": {
                                        "outgoing_update_filterlist": {
                                            "outgoing_update_filterlist": "not set"
                                        },
                                        "automatic_network_summarization_in_effect": False,
                                        "output_delay": 50,
                                        "maximum_paths": 4,
                                        "neighbors": {
                                            "10.1.2.2": {
                                                "distance": 120,
                                                "last_update": "00:00:04",
                                            },
                                            "10.1.3.3": {
                                                "distance": 120,
                                                "last_update": "00:00:00",
                                            },
                                        },
                                        "redistribute": {
                                            "rip": {},
                                            "static": {},
                                            "connected": {},
                                        },
                                        "distance": 120,
                                        "incoming_update_filterlist": {
                                            "incoming_update_filterlist": "not set"
                                        },
                                        "default_redistribution_metric": 3,
                                        "network": ["10.0.0.0"],
                                        "interfaces": {
                                            "GigabitEthernet3.100": {
                                                "triggered_rip": "no",
                                                "summary_address": {
                                                    "172.16.0.0/17": {}
                                                },
                                                "key_chain": "1",
                                                "send_version": "2",
                                                "receive_version": "2",
                                                "passive": True,
                                            }
                                        },
                                        "send_version": 2,
                                        "receive_version": 2,
                                        "timers": {
                                            "update_interval": 10,
                                            "next_update": 8,
                                            "holddown_interval": 22,
                                            "flush_interval": 23,
                                            "invalid_interval": 21,
                                        },
                                        "incoming_route_metric": {
                                            "list": "21",
                                            "added": "10",
                                        },
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "application": {
                "holddown": 0,
                "flushed": 0,
                "preference": {
                    "single_value": {
                    "all": 4}},
                "incoming_filter_list": "not set",
                "outgoing_filter_list": "not set",
                "update_frequency": 0,
                "maximum_path": 32,
                "invalid": 0,
            },
        }
    }
    golden_output_5 = {
        "execute.return_value": """\
        R1#show ip protocols
        *** IP Routing is NSF aware ***
        Routing Protocol is "application"
          Sending updates every 0 seconds
          Invalid after 0 seconds, hold down 0, flushed after 0
          Outgoing update filter list for all interfaces is not set
          Incoming update filter list for all interfaces is not set
          Maximum path: 32
          Routing for Networks:
          Routing Information Sources:
            Gateway         Distance      Last Update
          Distance: (default is 4)
        Routing Protocol is "rip"
          Output delay 50 milliseconds between packets
          Outgoing update filter list for all interfaces is not set
          Incoming update filter list for all interfaces is not set
          Incoming routes will have 10 added to metric if on list 21
          Sending updates every 10 seconds, next due in 8 seconds
          Invalid after 21 seconds, hold down 22, flushed after 23
          Default redistribution metric is 3
          Redistributing: connected, static, rip
          Neighbor(s):
            10.1.2.2
          Default version control: send version 2, receive version 2
            Interface                           Send  Recv  Triggered RIP  Key-chain
            GigabitEthernet3.100                2     2          No        1
          Automatic network summarization is not in effect
          Address Summarization:
            172.16.0.0/17 for GigabitEthernet3.100
          Maximum path: 4
          Routing for Networks:
            10.0.0.0
          Passive Interface(s):
            GigabitEthernet2.100
          Routing Information Sources:
            Gateway         Distance      Last Update
            10.1.3.3             120      00:00:00
            10.1.2.2             120      00:00:04
          Distance: (default is 120)
        """
    }

    golden_parsed_output_6 = {
        "protocols": {
            "rip": {
                "vrf": {
                    "VRF1": {
                        "address_family": {
                            "ipv4": {
                                "instance": {
                                    "rip": {
                                        "maximum_paths": 4,
                                        "incoming_update_filterlist": {
                                            "interfaces": {
                                                "GigabitEthernet2.100": {
                                                    "per_user": True,
                                                    "default": "not set",
                                                    "filter": "13",
                                                }
                                            },
                                            "incoming_update_filterlist": "100",
                                        },
                                        "network": ["10.0.0.0"],
                                        "distance": 120,
                                        "receive_version": 2,
                                        "interfaces": {
                                            "GigabitEthernet2.200": {
                                                "triggered_rip": "no",
                                                "key_chain": "none",
                                                "receive_version": "2",
                                                "send_version": "2",
                                            },
                                            "GigabitEthernet3.200": {
                                                "triggered_rip": "no",
                                                "key_chain": "none",
                                                "receive_version": "2",
                                                "send_version": "1 2",
                                            },
                                        },
                                        "outgoing_update_filterlist": {
                                            "interfaces": {
                                                "GigabitEthernet3.100": {
                                                    "per_user": True,
                                                    "default": "not set",
                                                    "filter": "130",
                                                },
                                                "GigabitEthernet2.100": {
                                                    "per_user": True,
                                                    "default": "not set",
                                                    "filter": "150",
                                                },
                                            },
                                            "outgoing_update_filterlist": "150",
                                        },
                                        "output_delay": 50,
                                        "timers": {
                                            "flush_interval": 240,
                                            "next_update": 2,
                                            "update_interval": 30,
                                            "invalid_interval": 180,
                                            "holddown_interval": 180,
                                        },
                                        "neighbors": {
                                            "10.1.2.2": {
                                                "last_update": "00:00:21",
                                                "distance": 120,
                                            },
                                            "10.1.3.3": {
                                                "last_update": "20:33:00",
                                                "distance": 120,
                                            },
                                        },
                                        "redistribute": {
                                            "rip": {},
                                            "static": {},
                                            "connected": {},
                                        },
                                        "send_version": 2,
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    golden_output_6 = {
        "execute.return_value": """
        R1#show ip protocols vrf VRF1
        Routing Protocol is "rip"
          Output delay 50 milliseconds between packets
          Outgoing update filter list for all interfaces is 150
            GigabitEthernet2.100 filtered by 150 (per-user), default is not set
            GigabitEthernet3.100 filtered by 130 (per-user), default is not set
          Incoming update filter list for all interfaces is 100
            GigabitEthernet2.100 filtered by 13 (per-user), default is not set
          Sending updates every 30 seconds, next due in 2 seconds
          Invalid after 180 seconds, hold down 180, flushed after 240
          Redistributing: connected, static, rip
          Default version control: send version 2, receive version 2
            Interface                           Send  Recv  Triggered RIP  Key-chain
            GigabitEthernet2.200                2     2          No        none
            GigabitEthernet3.200                1 2   2          No        none
          Maximum path: 4
          Routing for Networks:
             10.0.0.0
            10.0.0.0
          Routing Information Sources:
            Gateway         Distance      Last Update
            10.1.3.3             120      20:33:00
            10.1.2.2             120      00:00:21
          Distance: (default is 120)
    """
    }

    golden_parsed_output_7 = {
        "protocols": {
            "application": {
                "update_frequency": 0,
                "invalid": 0,
                "holddown": 0,
                "flushed": 0,
                "outgoing_filter_list": "not set",
                "incoming_filter_list": "not set",
                "maximum_path": 32,
                "preference": {
                    "single_value": {
                        "all": 4}},
            },
            "ospf": {
                "vrf": {
                    "default": {
                        "address_family": {
                            "ipv4": {
                                "instance": {
                                    "1": {
                                        "outgoing_filter_list": "not set",
                                        "incoming_filter_list": "not set",
                                        "router_id": "192.168.1.179",
                                        "total_areas": 2,
                                        "total_normal_area": 1,
                                        "total_stub_area": 0,
                                        "total_nssa_area": 1,
                                        "spf_control": {"paths": 4},
                                        "network": {
                                            "192.168.1.0": {
                                                "netmask": "0.0.0.255",
                                                "area": "0.0.0.0",
                                            },
                                            "192.168.100.164": {
                                                "netmask": "0.0.0.3",
                                                "area": "0.0.0.0",
                                            },
                                            "192.168.100.192": {
                                                "netmask": "0.0.0.3",
                                                "area": "0.0.0.0",
                                            },
                                        },
                                        "areas": {
                                            "0.0.0.0": {
                                                "configured_interfaces": [
                                                    "GigabitEthernet5"
                                                ]
                                            },
                                            "0.0.0.4": {
                                                "configured_interfaces": [
                                                    "GigabitEthernet7"
                                                ]
                                            },
                                        },
                                        "passive_interfaces": [
                                            "GigabitEthernet3",
                                            "GigabitEthernet4",
                                            "GigabitEthernet8",
                                            "Loopback0",
                                            "VoIP-Null0",
                                        ],
                                        "routing_information_sources": {
                                            "gateway": {
                                                "192.168.1.177": {
                                                    "distance": 110,
                                                    "last_update": "21:33:11",
                                                },
                                                "192.168.1.176": {
                                                    "distance": 110,
                                                    "last_update": "21:32:48",
                                                },
                                                "192.168.1.178": {
                                                    "distance": 110,
                                                    "last_update": "21:36:07",
                                                },
                                            }
                                        },
                                        "preference": {
                                            "single_value": {
                                                "all": 110}},
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "bgp": {
                "instance": {
                    "default": {
                        "bgp_id": 202926,
                        "vrf": {
                            "default": {
                                "address_family": {
                                    "ipv4": {
                                        "outgoing_filter_list": "not set",
                                        "incoming_filter_list": "not set",
                                        "igp_sync": False,
                                        "automatic_route_summarization": False,
                                        "neighbors": {
                                            "10.0.1.211": {},
                                            "10.0.1.221": {},
                                            "10.0.2.212": {},
                                            "10.0.2.222": {},
                                            "10.205.188.34": {},
                                            "10.205.37.149": {},
                                            "172.16.121.101": {
                                                "route_map": "ACCEPT_SCI_RICHEMONT"
                                            },
                                            "192.168.1.176": {
                                                "route_map": "INTERNET_EDGE_IN"
                                            },
                                            "192.168.1.177": {
                                                "route_map": "INTERNET_EDGE_IN"
                                            },
                                            "192.168.1.178": {},
                                        },
                                        "maximum_path": 2,
                                        "routing_information_sources": {
                                            "192.168.1.177": {
                                                "neighbor_id": "192.168.1.177",
                                                "distance": 200,
                                                "last_update": "21:33:06",
                                            },
                                            "192.168.1.176": {
                                                "neighbor_id": "192.168.1.176",
                                                "distance": 200,
                                                "last_update": "21:32:43",
                                            },
                                            "10.0.2.212": {
                                                "neighbor_id": "10.0.2.212",
                                                "distance": 20,
                                                "last_update": "21:35:39",
                                            },
                                        },
                                        "preference": {
                                            "multi_values": {
                                                "external": 20,
                                                "internal": 200,
                                                "local": 200,
                                            }
                                        },
                                    }
                                }
                            }
                        },
                    }
                }
            },
        }
    }

    golden_output_7 = {
        "execute.return_value": """
        show ip protocols
        *** IP Routing is NSF aware ***
        Routing Protocol is "application"
          Sending updates every 0 seconds
          Invalid after 0 seconds, hold down 0, flushed after 0
          Outgoing update filter list for all interfaces is not set
          Incoming update filter list for all interfaces is not set
          Maximum path: 32
          Routing for Networks:
          Routing Information Sources:
            Gateway         Distance      Last Update
          Distance: (default is 4)
        Routing Protocol is "ospf 1"
          Outgoing update filter list for all interfaces is not set
          Incoming update filter list for all interfaces is not set
          Router ID 192.168.1.179
          It is an area border and autonomous system boundary router
         Redistributing External Routes from,
          Number of areas in this router is 2. 1 normal 0 stub 1 nssa
          Address Summarization:
          Maximum path: 4
          Routing for Networks:
            192.168.1.0 0.0.0.255 area 0.0.0.0
            192.168.100.164 0.0.0.3 area 0.0.0.0
            192.168.100.192 0.0.0.3 area 0.0.0.0
          Routing on Interfaces Configured Explicitly (Area 0.0.0.0):
            GigabitEthernet5
          Routing on Interfaces Configured Explicitly (Area 4):
            GigabitEthernet7
          Passive Interface(s):
            GigabitEthernet3
            GigabitEthernet4
            GigabitEthernet8
            Loopback0
            VoIP-Null0
          Routing Information Sources:
            Gateway         Distance      Last Update
            192.168.1.177        110      21:33:11
            192.168.1.176        110      21:32:48
            192.168.1.178        110      21:36:07
          Distance: (default is 110)
        Routing Protocol is "bgp 202926"
          Outgoing update filter list for all interfaces is not set
          Incoming update filter list for all interfaces is not set
          IGP synchronization is disabled
          Automatic route summarization is disabled
          Neighbor(s):
            Address          FiltIn FiltOut DistIn DistOut Weight RouteMap
            10.0.1.211
            10.0.1.221
            10.0.2.212
            10.0.2.222
            10.205.188.34
            10.205.37.149
            172.16.121.101                                        ACCEPT_SCI_RICHEMONT
            192.168.1.176                                         INTERNET_EDGE_IN
            192.168.1.177                                         INTERNET_EDGE_IN
            192.168.1.178
          Maximum path: 2
          Routing Information Sources:
            Gateway         Distance      Last Update
            192.168.1.177        200      21:33:06
            192.168.1.176        200      21:32:43
            10.0.2.212            20      21:35:39
          Distance: external 20 internal 200 local 200"""
    }

    golden_parsed_output_8 = {
        "protocols": {
            "application": {
                "update_frequency": 0,
                "invalid": 0,
                "holddown": 0,
                "flushed": 0,
                "outgoing_filter_list": "not set",
                "incoming_filter_list": "not set",
                "maximum_path": 32,
                "preference": {
                    "single_value": {
                        "all": 4}},
            },
            "isis": {
                "vrf": {
                    "default": {
                        "address_family": {
                            "ipv4": {
                                "instance": {
                                    "default": {
                                        "outgoing_filter_list": "not set",
                                        "incoming_filter_list": "not set",
                                        "redistributing": "isis",
                                        "maximum_path": 4,
                                        "configured_interfaces": [
                                            "Loopback0",
                                            "GigabitEthernet4",
                                            "GigabitEthernet3",
                                            "GigabitEthernet5",
                                        ],
                                        "routing_information_sources": {
                                            "gateway": {
                                                "10.16.0.7": {
                                                    "distance": 115,
                                                    "last_update": "00:00:37",
                                                },
                                                "10.16.0.8": {
                                                    "distance": 115,
                                                    "last_update": "00:00:37",
                                                },
                                                "10.16.0.9": {
                                                    "distance": 115,
                                                    "last_update": "00:00:37",
                                                },
                                            }
                                        },
                                        "preference": {
                                            "single_value": {
                                                "all": 115}},
                                    }
                                }
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
                                    "200": {
                                        "outgoing_filter_list": "not set",
                                        "incoming_filter_list": "not set",
                                        "router_id": "10.16.0.2",
                                        "total_areas": 1,
                                        "total_normal_area": 1,
                                        "total_stub_area": 0,
                                        "total_nssa_area": 0,
                                        "spf_control": {"paths": 4},
                                        "network": {
                                            "10.16.0.0": {
                                                "netmask": "0.0.255.255",
                                                "area": "0",
                                            }
                                        },
                                        "routing_information_sources": {
                                            "gateway": {
                                                "10.16.0.7": {
                                                    "distance": 116,
                                                    "last_update": "2w0d",
                                                },
                                                "10.16.0.8": {
                                                    "distance": 116,
                                                    "last_update": "2w0d",
                                                },
                                                "10.16.0.9": {
                                                    "distance": 116,
                                                    "last_update": "2w0d",
                                                },
                                            }
                                        },
                                        "preference": {
                                            "single_value": {
                                                "all": 116}},
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "rip": {
                "vrf": {
                    "default": {
                        "address_family": {
                            "ipv4": {
                                "instance": {
                                    "rip": {
                                        "outgoing_update_filterlist": {
                                            "outgoing_update_filterlist": "not set"
                                        },
                                        "incoming_update_filterlist": {
                                            "incoming_update_filterlist": "not set"
                                        },
                                        "timers": {
                                            "update_interval": 30,
                                            "next_update": 0,
                                            "invalid_interval": 180,
                                            "holddown_interval": 180,
                                            "flush_interval": 240,
                                        },
                                        "redistribute": {"rip": {}},
                                        "send_version": 2,
                                        "receive_version": 2,
                                        "automatic_network_summarization_in_effect": True,
                                        "maximum_paths": 4,
                                        "distance": 120,
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "bgp": {
                "instance": {
                    "default": {
                        "bgp_id": 2,
                        "vrf": {
                            "default": {
                                "address_family": {
                                    "ipv4": {
                                        "outgoing_filter_list": "not set",
                                        "incoming_filter_list": "not set",
                                        "igp_sync": False,
                                        "automatic_route_summarization": False,
                                        "neighbors": {
                                            "10.16.0.9": {}
                                        },
                                        "maximum_path": 1,
                                        "routing_information_sources": {
                                            "10.16.0.9": {
                                                "neighbor_id": "10.16.0.9",
                                                "distance": 200,
                                                "last_update": "6d03h",
                                            }
                                        },
                                        "preference": {
                                            "multi_values": {
                                                "external": 20,
                                                "internal": 200,
                                                "local": 200,
                                            }
                                        },
                                    }
                                }
                            }
                        },
                    }
                }
            },
        }
    }

    def test_empty(self):
        device = Mock(**self.empty_output)
        obj = ShowIpProtocols(device=device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ip_protocols_1(self):

        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        raw1 = """\
            R1_ospf_xe#show ip protocols
            *** IP Routing is NSF aware ***
            Routing Protocol is "application"
              Sending updates every 0 seconds
              Invalid after 0 seconds, hold down 0, flushed after 0
              Outgoing update filter list for all interfaces is not set
              Incoming update filter list for all interfaces is not set
              Maximum path: 32
              Routing for Networks:
              Routing Information Sources:
                Gateway         Distance      Last Update
              Distance: (default is 4)
            Routing Protocol is "ospf 1"
              Outgoing update filter list for all interfaces is not set
              Incoming update filter list for all interfaces is not set
              Router ID 10.4.1.1
              Number of areas in this router is 1. 1 normal 0 stub 0 nssa
              Maximum path: 4
              Routing for Networks:
              Routing on Interfaces Configured Explicitly (Area 0):
                Loopback0
                GigabitEthernet2
                GigabitEthernet1
              Routing Information Sources:
                Gateway         Distance      Last Update
                10.36.3.3            110      07:33:00
                10.16.2.2            110      07:33:00
                10.64.4.4            110      00:19:15
              Distance: (default is 110)
              Distance: intra-area 112 inter-area 113 external 114
            Routing Protocol is "bgp 100"
              Outgoing update filter list for all interfaces is not set
              Incoming update filter list for all interfaces is not set
              IGP synchronization is disabled
              Automatic route summarization is disabled
              Maximum path: 1
              Routing Information Sources:
                Gateway         Distance      Last Update
                10.64.4.4            200      03:34:58
              Distance: external 20 internal 200 local 200
            """

        raw2 = """\
            R1_ospf_xe#show running-config | section router ospf 1
              router ospf 1
                mpls traffic-eng router-id Loopback0
                mpls traffic-eng area 0
            """

        raw3 = """\
            R1_ospf_xe#show running-config | section router ospf 2
              router ospf 2 vrf VRF1
                area 1 virtual-link 10.100.5.5
                area 1 sham-link 10.229.11.11 10.151.22.22 cost 111 ttl-security hops 3
                redistribute bgp
            """

        self.outputs = {}
        self.outputs["show ip protocols"] = raw1
        self.outputs["show running-config | section router ospf 1"] = raw2
        self.outputs["show running-config | section router ospf 2"] = raw3

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_show_ip_protocols_2(self):
        def mapper(key):
            return self.outputs[key]

        raw1 = """\
            show ip protocols
            *** IP Routing is NSF aware ***
            Routing Protocol is "application"
              Sending updates every 0 seconds
              Invalid after 0 seconds, hold down 0, flushed after 0
              Outgoing update filter list for all interfaces is not set
              Incoming update filter list for all interfaces is not set
              Maximum path: 32
              Routing for Networks:
              Routing Information Sources:
                Gateway         Distance      Last Update
              Distance: (default is 4)
            Routing Protocol is "ospf 1"
              Outgoing update filter list for all interfaces is not set
              Incoming update filter list for all interfaces is not set
              Router ID 192.168.0.10
              Number of areas in this router is 1. 1 normal 0 stub 0 nssa
              Maximum path: 4
              Routing for Networks:
                10.0.0.84 0.0.0.3 area 11
                10.0.0.88 0.0.0.3 area 11
                192.168.0.10 0.0.0.0 area 11
              Passive Interface(s):
                Loopback0
              Routing Information Sources:
                Gateway         Distance      Last Update
                192.168.0.9          110      01:36:38
              Distance: (default is 110)
            Routing Protocol is "bgp 1"
              Outgoing update filter list for all interfaces is not set
              Incoming update filter list for all interfaces is not set
              IGP synchronization is disabled
              Automatic route summarization is disabled
              Neighbor(s):
                Address          FiltIn FiltOut DistIn DistOut Weight RouteMap
                192.168.0.9
              Maximum path: 1
              Routing Information Sources:
                Gateway         Distance      Last Update
                192.168.0.9          200      01:35:12
              Distance: external 20 internal 200 local 200
            """

        raw2 = """\
            R1_ospf_xe#show running-config | section router ospf 1
              router ospf 1
                mpls traffic-eng router-id Loopback0
                mpls traffic-eng area 0
            """

        raw3 = """\
            R1_ospf_xe#show running-config | section router ospf 2
              router ospf 2 vrf VRF1
                area 1 virtual-link 10.100.5.5
                area 1 sham-link 10.229.11.11 10.151.22.22 cost 111 ttl-security hops 3
                redistribute bgp
            """

        self.outputs = {}
        self.outputs["show ip protocols"] = raw1
        self.outputs["show running-config | section router ospf 1"] = raw2
        self.outputs["show running-config | section router ospf 2"] = raw3

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper

        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_show_ip_protocols_3(self):
        device = Mock(**self.golden_output_3)
        obj = ShowIpProtocols(device=device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_show_ip_protocols_4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_4)
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)

    def test_show_ip_protocols_5(self):
        self.maxDiff = None
        device = Mock(**self.golden_output_5)
        obj = ShowIpProtocols(device=device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_5)

    def test_show_ip_protocols_6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_6)
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse(vrf="VRF1")
        self.assertEqual(parsed_output, self.golden_parsed_output_6)

    def test_show_ip_protocols_7(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_7)
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_7)

    def test_show_ip_protocols_8(self):

        def mapper(key):
            return self.outputs[key]

        raw1 = '''
            *** IP Routing is NSF aware ***
            Routing Protocol is "application"
              Sending updates every 0 seconds
              Invalid after 0 seconds, hold down 0, flushed after 0
              Outgoing update filter list for all interfaces is not set
              Incoming update filter list for all interfaces is not set
              Maximum path: 32
              Routing for Networks:
              Routing Information Sources:
                Gateway         Distance      Last Update
              Distance: (default is 4)
            Routing Protocol is "isis"
              Outgoing update filter list for all interfaces is not set
              Incoming update filter list for all interfaces is not set
              Redistributing: isis
              Address Summarization:
                None
              Maximum path: 4
              Routing for Networks:
                Loopback0
                GigabitEthernet4
                GigabitEthernet3
                GigabitEthernet5
              Routing Information Sources:
                Gateway         Distance      Last Update
                10.16.0.7              115      00:00:37
                10.16.0.8              115      00:00:37
                10.16.0.9              115      00:00:37
              Distance: (default is 115)
            Routing Protocol is "ospf 200"
              Outgoing update filter list for all interfaces is not set
              Incoming update filter list for all interfaces is not set
              Router ID 10.16.0.2
              Number of areas in this router is 1. 1 normal 0 stub 0 nssa
              Maximum path: 4
              Routing for Networks:
                10.16.0.0 0.0.255.255 area 0
              Routing Information Sources:
                Gateway         Distance      Last Update
                10.16.0.7              116      2w0d
                10.16.0.8              116      2w0d
                10.16.0.9              116      2w0d
              Distance: (default is 116)
            Routing Protocol is "rip"
              Outgoing update filter list for all interfaces is not set
              Incoming update filter list for all interfaces is not set
              Sending updates every 30 seconds, next due in 0 seconds
              Invalid after 180 seconds, hold down 180, flushed after 240
              Redistributing: rip
              Default version control: send version 2, receive version 2
              Automatic network summarization is in effect
              Maximum path: 4
              Routing for Networks:
              Routing Information Sources:
                Gateway         Distance      Last Update
              Distance: (default is 120)
            Routing Protocol is "bgp 2"
              Outgoing update filter list for all interfaces is not set
              Incoming update filter list for all interfaces is not set
              IGP synchronization is disabled
              Automatic route summarization is disabled
              Neighbor(s):
                Address          FiltIn FiltOut DistIn DistOut Weight RouteMap
                10.16.0.9
              Maximum path: 1
              Routing Information Sources:
                Gateway         Distance      Last Update
                10.16.0.9              200      6d03h
              Distance: external 20 internal 200 local 200
        '''

        raw2 = '''
            show running-config | section router ospf 200
            router ospf 200
             network 10.16.0.0 0.0.255.255 area 0
             distance 116
        '''

        self.outputs = {}
        self.outputs["show ip protocols"] = raw1
        self.outputs["show running-config | section router ospf 200"] = raw2

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_8)


if __name__ == "__main__":
    unittest.main()