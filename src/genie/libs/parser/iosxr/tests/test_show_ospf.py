# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import (
    SchemaEmptyParserError,
    SchemaMissingKeyError,
)

# iosxr show_ospf
from genie.libs.parser.iosxr.show_ospf import (
    ShowOspfVrfAllInclusiveInterface,
    ShowOspfVrfAllInclusiveNeighborDetail,
    ShowOspfVrfAllInclusive,
    ShowOspfVrfAllInclusiveShamLinks,
    ShowOspfVrfAllInclusiveVirtualLinks,
    ShowOspfMplsTrafficEngLink,
    ShowOspfVrfAllInclusiveDatabaseRouter,
    ShowOspfVrfAllInclusiveDatabaseExternal,
    ShowOspfVrfAllInclusiveDatabaseNetwork,
    ShowOspfVrfAllInclusiveDatabaseSummary,
    ShowOspfVrfAllInclusiveDatabaseOpaqueArea,
)


# ======================================================
#  Unit test for 'show ospf vrf all-inclusive interface'
# ======================================================
class test_show_ospf_vrf_all_inclusive_interface(unittest.TestCase):

    """Unit test for "show ospf vrf all-inclusive interface" """

    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    golden_parsed_output1 = {
        "vrf": {
            "VRF1": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "1": {
                                "areas": {
                                    "0.0.0.1": {
                                        "interfaces": {
                                            "GigabitEthernet0/0/0/1": {
                                                "bdr_ip_addr": "10.19.7.3",
                                                "bdr_router_id": "10.36.3.3",
                                                "bfd": {
                                                    "enable": True,
                                                    "interval": 12345,
                                                    "mode": "default",
                                                    "multiplier": 50,
                                                },
                                                "cost": 1,
                                                "dead_interval": 40,
                                                "demand_circuit": False,
                                                "dr_ip_addr": "10.19.7.7",
                                                "dr_router_id": "10.1.77.77",
                                                "enable": True,
                                                "flood_queue_length": 0,
                                                "hello_timer": "00:00:03:040",
                                                "hello_interval": 10,
                                                "index": "1/1",
                                                "interface_type": "broadcast",
                                                "ip_address": "10.19.7.3/24",
                                                "last_flood_scan_length": 1,
                                                "last_flood_scan_time_msec": 0,
                                                "line_protocol": True,
                                                "ls_ack_list": "current",
                                                "ls_ack_list_length": 0,
                                                "high_water_mark": 11,
                                                "max_flood_scan_length": 5,
                                                "max_flood_scan_time_msec": 0,
                                                "max_pkt_sz": 1500,
                                                "mtu": 1500,
                                                "name": "GigabitEthernet0/0/0/1",
                                                "next": "0(0)/0(0)",
                                                "passive": False,
                                                "priority": 1,
                                                "process_id": "1",
                                                "retransmit_interval": 5,
                                                "router_id": "10.36.3.3",
                                                "state": "bdr",
                                                "transmit_delay": 1,
                                                "wait_interval": 40,
                                                "statistics": {
                                                    "adj_nbr_count": 1,
                                                    "nbr_count": 1,
                                                    "num_nbrs_suppress_hello": 0,
                                                    "multi_area_intf_count": 0,
                                                },
                                                "neighbors": {
                                                    "10.1.77.77": {
                                                        "dr_router_id": "10.1.77.77"
                                                    },
                                                },
                                            }
                                        },
                                        "sham_links": {
                                            "10.21.33.33 10.151.22.22": {
                                                "bfd": {"enable": False},
                                                "cost": 111,
                                                "dead_interval": 13,
                                                "demand_circuit": True,
                                                "donotage_lsa": False,
                                                "enable": False,
                                                "flood_queue_length": 0,
                                                "hello_timer": "00:00:00:864",
                                                "hello_interval": 3,
                                                "high_water_mark": 9,
                                                "index": "2/2",
                                                "interface_type": "sham-link",
                                                "ip_address": "0.0.0.0/0",
                                                "last_flood_scan_length": 1,
                                                "last_flood_scan_time_msec": 0,
                                                "line_protocol": True,
                                                "ls_ack_list": "current",
                                                "ls_ack_list_length": 0,
                                                "max_flood_scan_length": 7,
                                                "max_flood_scan_time_msec": 0,
                                                "max_pkt_sz": 1500,
                                                "mtu": 0,
                                                "name": "SL0",
                                                "next": "0(0)/0(0)",
                                                "passive": False,
                                                "process_id": "1",
                                                "retransmit_interval": 5,
                                                "router_id": "10.36.3.3",
                                                "state": "point-to-point",
                                                "transmit_delay": 7,
                                                "wait_interval": 13,
                                                "statistics": {
                                                    "adj_nbr_count": 0,
                                                    "nbr_count": 0,
                                                    "num_nbrs_suppress_hello": 0,
                                                    "multi_area_intf_count": 0,
                                                },
                                                "total_dcbitless_lsa": 1,
                                            }
                                        },
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
                                "areas": {
                                    "0.0.0.0": {
                                        "interfaces": {
                                            "GigabitEthernet0/0/0/0": {
                                                "bdr_ip_addr": "10.3.4.3",
                                                "bdr_router_id": "10.36.3.3",
                                                "bfd": {"enable": False},
                                                "cost": 1,
                                                "dead_interval": 40,
                                                "demand_circuit": False,
                                                "dr_ip_addr": "10.3.4.4",
                                                "dr_router_id": "10.64.4.4",
                                                "enable": True,
                                                "flood_queue_length": 0,
                                                "hello_timer": "00:00:07:171",
                                                "hello_interval": 10,
                                                "index": "1/1",
                                                "interface_type": "broadcast",
                                                "ip_address": "10.3.4.3/24",
                                                "last_flood_scan_length": 1,
                                                "last_flood_scan_time_msec": 0,
                                                "line_protocol": True,
                                                "ls_ack_list": "current",
                                                "ls_ack_list_length": 0,
                                                "high_water_mark": 5,
                                                "max_flood_scan_length": 3,
                                                "max_flood_scan_time_msec": 0,
                                                "max_pkt_sz": 1500,
                                                "mtu": 1500,
                                                "name": "GigabitEthernet0/0/0/0",
                                                "next": "0(0)/0(0)",
                                                "passive": False,
                                                "priority": 1,
                                                "process_id": "1",
                                                "retransmit_interval": 5,
                                                "router_id": "10.36.3.3",
                                                "state": "bdr",
                                                "transmit_delay": 1,
                                                "wait_interval": 40,
                                                "statistics": {
                                                    "adj_nbr_count": 1,
                                                    "nbr_count": 1,
                                                    "num_nbrs_suppress_hello": 0,
                                                    "multi_area_intf_count": 0,
                                                },
                                                "neighbors": {
                                                    "10.64.4.4": {
                                                        "dr_router_id": "10.64.4.4"
                                                    },
                                                },
                                            },
                                            "GigabitEthernet0/0/0/2": {
                                                "bdr_router_id": "10.16.2.2",
                                                "bdr_ip_addr": "10.2.3.2",
                                                "bfd": {"enable": False},
                                                "cost": 1,
                                                "dead_interval": 40,
                                                "demand_circuit": False,
                                                "dr_ip_addr": "10.2.3.3",
                                                "dr_router_id": "10.36.3.3",
                                                "enable": True,
                                                "flood_queue_length": 0,
                                                "hello_timer": "00:00:07:587",
                                                "hello_interval": 10,
                                                "index": "2/2",
                                                "interface_type": "broadcast",
                                                "ip_address": "10.2.3.3/24",
                                                "last_flood_scan_length": 1,
                                                "last_flood_scan_time_msec": 0,
                                                "line_protocol": True,
                                                "ls_ack_list": "current",
                                                "ls_ack_list_length": 0,
                                                "high_water_mark": 7,
                                                "max_flood_scan_length": 3,
                                                "max_flood_scan_time_msec": 0,
                                                "max_pkt_sz": 1500,
                                                "mtu": 1500,
                                                "name": "GigabitEthernet0/0/0/2",
                                                "next": "0(0)/0(0)",
                                                "passive": False,
                                                "priority": 1,
                                                "process_id": "1",
                                                "retransmit_interval": 5,
                                                "router_id": "10.36.3.3",
                                                "state": "dr",
                                                "transmit_delay": 1,
                                                "wait_interval": 40,
                                                "statistics": {
                                                    "nbr_count": 1,
                                                    "adj_nbr_count": 1,
                                                    "multi_area_intf_count": 0,
                                                    "num_nbrs_suppress_hello": 0,
                                                },
                                                "neighbors": {
                                                    "10.16.2.2": {
                                                        "bdr_router_id": "10.16.2.2"
                                                    },
                                                },
                                            },
                                            "Loopback0": {
                                                "bfd": {"enable": False},
                                                "cost": 1,
                                                "demand_circuit": False,
                                                "enable": True,
                                                "interface_type": "loopback",
                                                "ip_address": "10.36.3.3/32",
                                                "line_protocol": True,
                                                "name": "Loopback0",
                                                "process_id": "1",
                                                "router_id": "10.36.3.3",
                                            },
                                            "tunnel-te31": {
                                                "bfd": {"enable": False},
                                                "dead_interval": 40,
                                                "demand_circuit": False,
                                                "enable": True,
                                                "flood_queue_length": 0,
                                                "hello_interval": 10,
                                                "index": "0/0",
                                                "interface_type": "point-to-point",
                                                "ip_address": "0.0.0.0/0",
                                                "last_flood_scan_length": 0,
                                                "last_flood_scan_time_msec": 0,
                                                "line_protocol": True,
                                                "ls_ack_list": "current",
                                                "ls_ack_list_length": 0,
                                                "high_water_mark": 0,
                                                "max_flood_scan_length": 0,
                                                "max_flood_scan_time_msec": 0,
                                                "max_pkt_sz": 576,
                                                "mtu": 0,
                                                "name": "tunnel-te31",
                                                "next": "0(0)/0(0)",
                                                "passive": True,
                                                "process_id": "1",
                                                "retransmit_interval": 5,
                                                "router_id": "10.36.3.3",
                                                "state": "point-to-point",
                                                "transmit_delay": 1,
                                                "wait_interval": 0,
                                                "statistics": {
                                                    "adj_nbr_count": 0,
                                                    "multi_area_intf_count": 0,
                                                    "nbr_count": 0,
                                                    "num_nbrs_suppress_hello": 0,
                                                },
                                            },
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
        }
    }

    golden_parsed_output2 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "1": {
                                "areas": {
                                    "0.0.0.0": {
                                        "interfaces": {
                                            "GigabitEthernet0/0/0/0": {
                                                "bfd": {"enable": False},
                                                "cost": 1,
                                                "dead_interval": 40,
                                                "demand_circuit": False,
                                                "dr_ip_addr": "10.2.3.2",
                                                "dr_router_id": "10.16.2.2",
                                                "enable": True,
                                                "flood_queue_length": 0,
                                                "hello_timer": "00:00:09:266",
                                                "hello_interval": 10,
                                                "high_water_mark": 0,
                                                "index": "2/3",
                                                "interface_type": "broadcast",
                                                "ip_address": "10.2.3.2/24",
                                                "last_flood_scan_length": 0,
                                                "last_flood_scan_time_msec": 0,
                                                "line_protocol": True,
                                                "ls_ack_list": "current",
                                                "ls_ack_list_length": 0,
                                                "max_flood_scan_length": 0,
                                                "max_flood_scan_time_msec": 0,
                                                "max_pkt_sz": 1500,
                                                "mtu": 1500,
                                                "name": "GigabitEthernet0/0/0/0",
                                                "next": "0(0)/0(0)",
                                                "passive": False,
                                                "priority": 1,
                                                "process_id": "1",
                                                "retransmit_interval": 5,
                                                "router_id": "10.16.2.2",
                                                "state": "dr",
                                                "transmit_delay": 1,
                                                "wait_interval": 40,
                                                "statistics": {
                                                    "adj_nbr_count": 0,
                                                    "nbr_count": 0,
                                                    "num_nbrs_suppress_hello": 0,
                                                    "multi_area_intf_count": 0,
                                                },
                                            },
                                            "GigabitEthernet0/0/0/2": {
                                                "bfd": {"enable": False},
                                                "cost": 1,
                                                "dead_interval": 40,
                                                "demand_circuit": False,
                                                "dr_ip_addr": "10.1.2.2",
                                                "dr_router_id": "10.16.2.2",
                                                "enable": True,
                                                "flood_queue_length": 0,
                                                "hello_timer": "00:00:08:733",
                                                "hello_interval": 10,
                                                "high_water_mark": 0,
                                                "index": "3/4",
                                                "interface_type": "broadcast",
                                                "ip_address": "10.1.2.2/24",
                                                "last_flood_scan_length": 0,
                                                "last_flood_scan_time_msec": 0,
                                                "line_protocol": True,
                                                "ls_ack_list": "current",
                                                "ls_ack_list_length": 0,
                                                "max_flood_scan_length": 0,
                                                "max_flood_scan_time_msec": 0,
                                                "max_pkt_sz": 1500,
                                                "mtu": 1500,
                                                "name": "GigabitEthernet0/0/0/2",
                                                "next": "0(0)/0(0)",
                                                "passive": False,
                                                "priority": 1,
                                                "process_id": "1",
                                                "retransmit_interval": 5,
                                                "router_id": "10.16.2.2",
                                                "state": "dr",
                                                "transmit_delay": 1,
                                                "wait_interval": 40,
                                                "statistics": {
                                                    "adj_nbr_count": 0,
                                                    "nbr_count": 0,
                                                    "num_nbrs_suppress_hello": 0,
                                                    "multi_area_intf_count": 0,
                                                },
                                            },
                                            "Loopback0": {
                                                "bfd": {"enable": False},
                                                "cost": 1,
                                                "demand_circuit": False,
                                                "enable": True,
                                                "interface_type": "loopback",
                                                "ip_address": "10.16.2.2/32",
                                                "line_protocol": True,
                                                "name": "Loopback0",
                                                "process_id": "1",
                                                "router_id": "10.16.2.2",
                                            },
                                        }
                                    },
                                    "0.0.0.1": {
                                        "interfaces": {
                                            "GigabitEthernet0/0/0/1": {
                                                "bdr_ip_addr": "10.229.3.2",
                                                "bdr_router_id": "10.16.2.2",
                                                "bfd": {"enable": False},
                                                "cost": 1,
                                                "dead_interval": 40,
                                                "demand_circuit": False,
                                                "dr_ip_addr": "10.229.3.3",
                                                "dr_router_id": "10.36.3.3",
                                                "enable": True,
                                                "flood_queue_length": 0,
                                                "hello_timer": "00:00:00:698",
                                                "hello_interval": 10,
                                                "high_water_mark": 3,
                                                "index": "2/5",
                                                "interface_type": "broadcast",
                                                "ip_address": "10.229.3.2/24",
                                                "last_flood_scan_length": 9,
                                                "last_flood_scan_time_msec": 0,
                                                "line_protocol": True,
                                                "ls_ack_list": "current",
                                                "ls_ack_list_length": 0,
                                                "max_flood_scan_length": 9,
                                                "max_flood_scan_time_msec": 0,
                                                "max_pkt_sz": 1500,
                                                "mtu": 1500,
                                                "name": "GigabitEthernet0/0/0/1",
                                                "next": "0(0)/0(0)",
                                                "passive": False,
                                                "priority": 1,
                                                "process_id": "1",
                                                "retransmit_interval": 5,
                                                "router_id": "10.16.2.2",
                                                "state": "bdr",
                                                "transmit_delay": 1,
                                                "wait_interval": 40,
                                                "neighbors": {
                                                    "10.36.3.3": {
                                                        "dr_router_id": "10.36.3.3"
                                                    },
                                                },
                                                "statistics": {
                                                    "adj_nbr_count": 1,
                                                    "nbr_count": 1,
                                                    "num_nbrs_suppress_hello": 0,
                                                    "multi_area_intf_count": 0,
                                                },
                                            },
                                            "GigabitEthernet0/0/0/3": {
                                                "bdr_ip_addr": "10.229.4.2",
                                                "bdr_router_id": "10.16.2.2",
                                                "bfd": {"enable": False},
                                                "cost": 1,
                                                "dead_interval": 40,
                                                "demand_circuit": False,
                                                "dr_ip_addr": "10.229.4.4",
                                                "dr_router_id": "10.64.4.4",
                                                "enable": True,
                                                "flood_queue_length": 0,
                                                "hello_timer": "00:00:00:840",
                                                "hello_interval": 10,
                                                "high_water_mark": 21,
                                                "index": "3/6",
                                                "interface_type": "broadcast",
                                                "ip_address": "10.229.4.2/24",
                                                "last_flood_scan_length": 9,
                                                "last_flood_scan_time_msec": 0,
                                                "line_protocol": True,
                                                "ls_ack_list": "current",
                                                "ls_ack_list_length": 0,
                                                "max_flood_scan_length": 9,
                                                "max_flood_scan_time_msec": 0,
                                                "max_pkt_sz": 1500,
                                                "mtu": 1500,
                                                "name": "GigabitEthernet0/0/0/3",
                                                "next": "0(0)/0(0)",
                                                "passive": False,
                                                "priority": 1,
                                                "process_id": "1",
                                                "retransmit_interval": 5,
                                                "router_id": "10.16.2.2",
                                                "state": "bdr",
                                                "transmit_delay": 1,
                                                "wait_interval": 40,
                                                "neighbors": {
                                                    "10.64.4.4": {
                                                        "dr_router_id": "10.64.4.4"
                                                    },
                                                },
                                                "statistics": {
                                                    "adj_nbr_count": 1,
                                                    "nbr_count": 1,
                                                    "num_nbrs_suppress_hello": 0,
                                                    "multi_area_intf_count": 0,
                                                },
                                            },
                                            "Loopback1": {
                                                "bfd": {"enable": False},
                                                "cost": 1,
                                                "demand_circuit": False,
                                                "enable": True,
                                                "interface_type": "loopback",
                                                "ip_address": "10.151.22.22/32",
                                                "line_protocol": True,
                                                "name": "Loopback1",
                                                "process_id": "1",
                                                "router_id": "10.16.2.2",
                                            },
                                        },
                                        "virtual_links": {
                                            "0.0.0.1 10.16.2.2": {
                                                "bfd": {"enable": False},
                                                "cost": 1,
                                                "dead_interval": 40,
                                                "demand_circuit": True,
                                                "donotage_lsa": False,
                                                "enable": False,
                                                "flood_queue_length": 0,
                                                "hello_timer": "00:00:01:281",
                                                "hello_interval": 10,
                                                "high_water_mark": 20,
                                                "index": "4/7",
                                                "interface_type": "virtual-link",
                                                "ip_address": "0.0.0.0/0",
                                                "last_flood_scan_length": 7,
                                                "last_flood_scan_time_msec": 0,
                                                "line_protocol": True,
                                                "ls_ack_list": "current",
                                                "ls_ack_list_length": 0,
                                                "max_flood_scan_length": 7,
                                                "max_flood_scan_time_msec": 0,
                                                "max_pkt_sz": 1500,
                                                "mtu": 0,
                                                "name": "VL0",
                                                "next": "0(0)/0(0)",
                                                "passive": False,
                                                "process_id": "1",
                                                "retransmit_interval": 5,
                                                "router_id": "10.16.2.2",
                                                "state": "point-to-point",
                                                "transmit_delay": 1,
                                                "wait_interval": 40,
                                                "total_dcbitless_lsa": 7,
                                                "neighbors": {"10.64.4.4": {},},
                                                "statistics": {
                                                    "adj_nbr_count": 1,
                                                    "nbr_count": 1,
                                                    "num_nbrs_suppress_hello": 1,
                                                    "multi_area_intf_count": 0,
                                                },
                                            }
                                        },
                                    },
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    def test_show_ospf_vrf_all_inclusive_interface_full1(self):

        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        raw1 = """\
            RP/0/0/CPU0:R3_ospf_xr#show ospf vrf all-inclusive interface
            Interfaces for OSPF 1

            Loopback0 is up, line protocol is up
              Internet Address 10.36.3.3/32, Area 0
              Process ID 1, Router ID 10.36.3.3, Network Type LOOPBACK, Cost: 1
              Loopback interface is treated as a stub Host
            GigabitEthernet0/0/0/0 is up, line protocol is up
              Internet Address 10.3.4.3/24, Area 0
              Process ID 1, Router ID 10.36.3.3, Network Type BROADCAST, Cost: 1
              Transmit Delay is 1 sec, State BDR, Priority 1, MTU 1500, MaxPktSz 1500
              Designated Router (ID) 10.64.4.4, Interface address 10.3.4.4
              Backup Designated router (ID) 10.36.3.3, Interface address 10.3.4.3
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                Hello due in 00:00:07:171
              Index 1/1, flood queue length 0
              Next 0(0)/0(0)
              Last flood scan length is 1, maximum is 3
              Last flood scan time is 0 msec, maximum is 0 msec
              LS Ack List: current length 0, high water mark 5
              Neighbor Count is 1, Adjacent neighbor count is 1
                Adjacent with neighbor 10.64.4.4  (Designated Router)
              Suppress hello for 0 neighbor(s)
              Multi-area interface Count is 0
            GigabitEthernet0/0/0/2 is up, line protocol is up
              Internet Address 10.2.3.3/24, Area 0
              Process ID 1, Router ID 10.36.3.3, Network Type BROADCAST, Cost: 1
              Transmit Delay is 1 sec, State DR, Priority 1, MTU 1500, MaxPktSz 1500
              Designated Router (ID) 10.36.3.3, Interface address 10.2.3.3
              Backup Designated router (ID) 10.16.2.2, Interface address 10.2.3.2
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                Hello due in 00:00:07:587
              Index 2/2, flood queue length 0
              Next 0(0)/0(0)
              Last flood scan length is 1, maximum is 3
              Last flood scan time is 0 msec, maximum is 0 msec
              LS Ack List: current length 0, high water mark 7
              Neighbor Count is 1, Adjacent neighbor count is 1
                Adjacent with neighbor 10.16.2.2  (Backup Designated Router)
              Suppress hello for 0 neighbor(s)
              Multi-area interface Count is 0
            tunnel-te31 is up, line protocol is up
              Internet Address 0.0.0.0/0, Area 0
              Process ID 1, Router ID 10.36.3.3, Network Type POINT_TO_POINT
              Interface is a tunnel igp-shortcut
              Transmit Delay is 1 sec, State POINT_TO_POINT, MTU 0, MaxPktSz 576
              Timer intervals configured, Hello 10, Dead 40, Wait 0, Retransmit 5
                No Hellos (Passive interface)
              Index 0/0, flood queue length 0
              Next 0(0)/0(0)
              Last flood scan length is 0, maximum is 0
              Last flood scan time is 0 msec, maximum is 0 msec
              LS Ack List: current length 0, high water mark 0
              Neighbor Count is 0, Adjacent neighbor count is 0
              Suppress hello for 0 neighbor(s)
              Multi-area interface Count is 0


            Interfaces for OSPF 1, VRF VRF1

            OSPF_SL0 is unknown, line protocol is up
              Internet Address 0.0.0.0/0, Area 1
              Process ID 1, VRF VRF1, Router ID 10.36.3.3, Network Type SHAM_LINK, Cost: 111
              Configured as demand circuit.
              Run as demand circuit.
              DoNotAge LSA not allowed (Number of DCbitless LSA is 1).
              Transmit Delay is 7 sec, State POINT_TO_POINT, MTU 0, MaxPktSz 1500
              Timer intervals configured, Hello 3, Dead 13, Wait 13, Retransmit 5
                Hello due in 00:00:00:864
              Index 2/2, flood queue length 0
              Next 0(0)/0(0)
              Last flood scan length is 1, maximum is 7
              Last flood scan time is 0 msec, maximum is 0 msec
              LS Ack List: current length 0, high water mark 9
              Neighbor Count is 0, Adjacent neighbor count is 0
              Suppress hello for 0 neighbor(s)
              Multi-area interface Count is 0
            GigabitEthernet0/0/0/1 is up, line protocol is up
              Internet Address 10.19.7.3/24, Area 1
              Process ID 1, VRF VRF1, Router ID 10.36.3.3, Network Type BROADCAST, Cost: 1
              BFD enabled, BFD interval 12345 msec, BFD multiplier 50, Mode: Default
              Transmit Delay is 1 sec, State BDR, Priority 1, MTU 1500, MaxPktSz 1500
              Designated Router (ID) 10.1.77.77, Interface address 10.19.7.7
              Backup Designated router (ID) 10.36.3.3, Interface address 10.19.7.3
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                Hello due in 00:00:03:040
              Index 1/1, flood queue length 0
              Next 0(0)/0(0)
              Last flood scan length is 1, maximum is 5
              Last flood scan time is 0 msec, maximum is 0 msec
              LS Ack List: current length 0, high water mark 11
              Neighbor Count is 1, Adjacent neighbor count is 1
                Adjacent with neighbor 10.1.77.77  (Designated Router)
              Suppress hello for 0 neighbor(s)
              Multi-area interface Count is 0
            """

        raw2 = """\
            RP/0/0/CPU0:R3_ospf_xr#show ospf vrf all-inclusive sham-links | i OSPF_SL0
            Sham Link OSPF_SL0 to address 10.151.22.22 is up
            """

        raw3 = """\
            RP/0/0/CPU0:R3_ospf_xr#show run formal router ospf | i sham | i 10.151.22.22
            router ospf 1 vrf VRF1 area 1 sham-link 10.21.33.33 10.151.22.22
            """

        self.outputs = {}
        self.outputs["show ospf vrf all-inclusive interface"] = raw1
        self.outputs["show ospf vrf all-inclusive sham-links | i OSPF_SL0"] = raw2
        self.outputs["show run formal router ospf | i sham | i 10.151.22.22"] = raw3

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper

        obj = ShowOspfVrfAllInclusiveInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_interface_full2(self):

        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        raw1 = """\
            RP/0/0/CPU0:R2_ospf_xr#show ospf vrf all-inclusive interface
            Tue Dec 12 20:23:16.958 UTC

            Interfaces for OSPF 1

            Loopback0 is up, line protocol is up
              Internet Address 10.16.2.2/32, Area 0
              Process ID 1, Router ID 10.16.2.2, Network Type LOOPBACK, Cost: 1
              Loopback interface is treated as a stub Host
            OSPF_VL0 is unknown, line protocol is up
              Internet Address 0.0.0.0/0, Area 0
              Process ID 1, Router ID 10.16.2.2, Network Type VIRTUAL_LINK, Cost: 1
              Configured as demand circuit.
              Run as demand circuit.
              DoNotAge LSA not allowed (Number of DCbitless LSA is 7).
              Transmit Delay is 1 sec, State POINT_TO_POINT, MTU 0, MaxPktSz 1500
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                Hello due in 00:00:01:281
              Index 4/7, flood queue length 0
              Next 0(0)/0(0)
              Last flood scan length is 7, maximum is 7
              Last flood scan time is 0 msec, maximum is 0 msec
              LS Ack List: current length 0, high water mark 20
              Neighbor Count is 1, Adjacent neighbor count is 1
                Adjacent with neighbor 10.64.4.4  (Hello suppressed)
              Suppress hello for 1 neighbor(s)
              Multi-area interface Count is 0
            GigabitEthernet0/0/0/0 is up, line protocol is up
              Internet Address 10.2.3.2/24, Area 0
              Process ID 1, Router ID 10.16.2.2, Network Type BROADCAST, Cost: 1
              Transmit Delay is 1 sec, State DR, Priority 1, MTU 1500, MaxPktSz 1500
              Designated Router (ID) 10.16.2.2, Interface address 10.2.3.2
              No backup designated router on this network
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                Hello due in 00:00:09:266
              Index 2/3, flood queue length 0
              Next 0(0)/0(0)
              Last flood scan length is 0, maximum is 0
              Last flood scan time is 0 msec, maximum is 0 msec
              LS Ack List: current length 0, high water mark 0
              Neighbor Count is 0, Adjacent neighbor count is 0
              Suppress hello for 0 neighbor(s)
              Multi-area interface Count is 0
            GigabitEthernet0/0/0/2 is up, line protocol is up
              Internet Address 10.1.2.2/24, Area 0
              Process ID 1, Router ID 10.16.2.2, Network Type BROADCAST, Cost: 1
              Transmit Delay is 1 sec, State DR, Priority 1, MTU 1500, MaxPktSz 1500
              Designated Router (ID) 10.16.2.2, Interface address 10.1.2.2
              No backup designated router on this network
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                Hello due in 00:00:08:733
              Index 3/4, flood queue length 0
              Next 0(0)/0(0)
              Last flood scan length is 0, maximum is 0
              Last flood scan time is 0 msec, maximum is 0 msec
              LS Ack List: current length 0, high water mark 0
              Neighbor Count is 0, Adjacent neighbor count is 0
              Suppress hello for 0 neighbor(s)
              Multi-area interface Count is 0
            Loopback1 is up, line protocol is up
              Internet Address 10.151.22.22/32, Area 1
              Process ID 1, Router ID 10.16.2.2, Network Type LOOPBACK, Cost: 1
              Loopback interface is treated as a stub Host
            GigabitEthernet0/0/0/1 is up, line protocol is up
              Internet Address 10.229.3.2/24, Area 1
              Process ID 1, Router ID 10.16.2.2, Network Type BROADCAST, Cost: 1
              Transmit Delay is 1 sec, State BDR, Priority 1, MTU 1500, MaxPktSz 1500
              Designated Router (ID) 10.36.3.3, Interface address 10.229.3.3
              Backup Designated router (ID) 10.16.2.2, Interface address 10.229.3.2
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                Hello due in 00:00:00:698
              Index 2/5, flood queue length 0
              Next 0(0)/0(0)
              Last flood scan length is 9, maximum is 9
              Last flood scan time is 0 msec, maximum is 0 msec
              LS Ack List: current length 0, high water mark 3
              Neighbor Count is 1, Adjacent neighbor count is 1
                Adjacent with neighbor 10.36.3.3  (Designated Router)
              Suppress hello for 0 neighbor(s)
              Multi-area interface Count is 0
            GigabitEthernet0/0/0/3 is up, line protocol is up
              Internet Address 10.229.4.2/24, Area 1
              Process ID 1, Router ID 10.16.2.2, Network Type BROADCAST, Cost: 1
              Transmit Delay is 1 sec, State BDR, Priority 1, MTU 1500, MaxPktSz 1500
              Designated Router (ID) 10.64.4.4, Interface address 10.229.4.4
              Backup Designated router (ID) 10.16.2.2, Interface address 10.229.4.2
              Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
                Hello due in 00:00:00:840
              Index 3/6, flood queue length 0
              Next 0(0)/0(0)
              Last flood scan length is 9, maximum is 9
              Last flood scan time is 0 msec, maximum is 0 msec
              LS Ack List: current length 0, high water mark 21
              Neighbor Count is 1, Adjacent neighbor count is 1
                Adjacent with neighbor 10.64.4.4  (Designated Router)
              Suppress hello for 0 neighbor(s)
              Multi-area interface Count is 0
            """

        raw2 = """\
            RP/0/0/CPU0:R2_ospf_xr#show ospf vrf all-inclusive virtual-links
            Fri Nov  3 01:25:44.845 UTC

            Virtual Links for OSPF 1

            Virtual Link OSPF_VL0 to router 10.64.4.4 is up

              DoNotAge LSA not allowed Run as demand circuit (Number of DCbitless LSA is 1).
              Transit area 1, via interface GigabitEthernet0/0/0/3, Cost of using 65535
              Transmit Delay is 5 sec, State POINT_TO_POINT,
              Non-Stop Forwarding (NSF) enabled, last NSF restart 00:18:16 ago
              Timer intervals configured, Hello 4, Dead 16, Wait 16, Retransmit 44
                Hello due in 00:00:03:179
              Clear text authentication enabled
            """

        self.outputs = {}
        self.outputs["show ospf vrf all-inclusive interface"] = raw1
        self.outputs["show ospf vrf all-inclusive virtual-links"] = raw2

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper

        obj = ShowOspfVrfAllInclusiveInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ospf_vrf_all_inclusive_interface_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ============================================================
#  Unit test for 'show ospf vrf all-inclusive neighbor detail'
# ============================================================
class test_show_ospf_vrf_all_inclusive_neighbor_detail(unittest.TestCase):

    """Unit test for "show ospf vrf all-inclusive neighbor detail" """

    device = Device(name="aDevice")
    empty_output = {"execute.return_value": ""}
    golden_output0 = {
        "execute.return_value": """
    show ospf vrf all-inclusive neighbor detail

    Tue Apr  9 09:54:13.528 UTC

    * Indicates MADJ interface
    # Indicates Neighbor awaiting BFD session up

    Neighbors for OSPF 1

     Neighbor 10.1.1.1, interface address 10.1.1.8
        In the area 0.0.0.0 via interface GigabitEthernet0/0/0/0 , BFD enabled, Mode: Default
        Neighbor priority is 1, State is FULL, 6 state changes
        DR is 192.168.1.19 BDR is 192.168.1.18
        Options is 0x52
        LLS Options is 0x1 (LR)
        Dead timer due in 00:00:35
        Neighbor is up for 21:29:29
        Number of DBD retrans during last exchange 0
        Index 4/4, retransmission queue length 0, number of retransmission 0
        First 0(0)/0(0) Next 0(0)/0(0)
        Last retransmission scan length is 0, maximum is 0
        Last retransmission scan time is 0 msec, maximum is 0 msec
        LS Ack list: NSR-sync pending 0, high water mark 0
        Neighbor BFD status: Waiting for BFD session up #

    Total neighbor count: 1
            """
    }
    golden_parsed_output0 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "1": {
                                "areas": {
                                    "0.0.0.0": {
                                        "interfaces": {
                                            "GigabitEthernet0/0/0/0": {
                                                "neighbors": {
                                                    "10.1.1.1": {
                                                        "neighbor_router_id": "10.1.1.1",
                                                        "bfd_enable": True,
                                                        "bfd_mode": "Default",
                                                        "address": "10.1.1.8",
                                                        "priority": 1,
                                                        "state": "full",
                                                        "statistics": {
                                                            "nbr_event_count": 6,
                                                            "total_dbd_retrans": 0,
                                                            "nbr_retrans_qlen": 0,
                                                            "total_retransmission": 0,
                                                            "last_retrans_scan_length": 0,
                                                            "last_retrans_max_scan_length": 0,
                                                            "last_retrans_scan_time_msec": 0,
                                                            "last_retrans_max_scan_time_msec": 0,
                                                        },
                                                        "dr_ip_addr": "192.168.1.19",
                                                        "bdr_ip_addr": "192.168.1.18",
                                                        "options": "0x52",
                                                        "lls_options": "0x1 (LR)",
                                                        "dead_timer": "00:00:35",
                                                        "neighbor_uptime": "21:29:29",
                                                        "index": "4/4,",
                                                        "first": "0(0)/0(0)",
                                                        "next": "0(0)/0(0)",
                                                        "ls_ack_list": "NSR-sync",
                                                        "ls_ack_list_pending": 0,
                                                        "high_water_mark": 0,
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "total_neighbor_count": 1,
                            }
                        }
                    }
                }
            }
        }
    }

    golden_parsed_output1 = {
        "vrf": {
            "VRF1": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "1": {
                                "areas": {
                                    "0.0.0.1": {
                                        "interfaces": {
                                            "GigabitEthernet0/0/0/1": {
                                                "neighbors": {
                                                    "10.1.77.77": {
                                                        "address": "10.19.7.7",
                                                        "bdr_ip_addr": "10.19.7.3",
                                                        "dead_timer": "00:00:32",
                                                        "dr_ip_addr": "10.19.7.7",
                                                        "first": "0(0)/0(0)",
                                                        "high_water_mark": 0,
                                                        "index": "1/1,",
                                                        "lls_options": "0x1 (LR)",
                                                        "ls_ack_list": "NSR-sync",
                                                        "ls_ack_list_pending": 0,
                                                        "neighbor_router_id": "10.1.77.77",
                                                        "neighbor_uptime": "23:24:56",
                                                        "next": "0(0)/0(0)",
                                                        "options": "0x52",
                                                        "priority": 1,
                                                        "state": "full",
                                                        "statistics": {
                                                            "nbr_event_count": 6,
                                                            "nbr_retrans_qlen": 0,
                                                            "total_retransmission": 15,
                                                            "total_dbd_retrans": 0,
                                                            "last_retrans_max_scan_length": 3,
                                                            "last_retrans_max_scan_time_msec": 0,
                                                            "last_retrans_scan_length": 3,
                                                            "last_retrans_scan_time_msec": 0,
                                                        },
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "total_neighbor_count": 1,
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
                                "areas": {
                                    "0.0.0.0": {
                                        "interfaces": {
                                            "GigabitEthernet0/0/0/0": {
                                                "neighbors": {
                                                    "10.64.4.4": {
                                                        "address": "10.3.4.4",
                                                        "bdr_ip_addr": "10.3.4.3",
                                                        "dead_timer": "00:00:30",
                                                        "dr_ip_addr": "10.3.4.4",
                                                        "first": "0(0)/0(0)",
                                                        "high_water_mark": 0,
                                                        "index": "2/2,",
                                                        "lls_options": "0x1 (LR)",
                                                        "ls_ack_list": "NSR-sync",
                                                        "ls_ack_list_pending": 0,
                                                        "neighbor_router_id": "10.64.4.4",
                                                        "neighbor_uptime": "1d01h",
                                                        "next": "0(0)/0(0)",
                                                        "options": "0x52",
                                                        "priority": 1,
                                                        "state": "full",
                                                        "statistics": {
                                                            "nbr_event_count": 6,
                                                            "nbr_retrans_qlen": 0,
                                                            "total_retransmission": 0,
                                                            "total_dbd_retrans": 0,
                                                            "last_retrans_max_scan_length": 0,
                                                            "last_retrans_max_scan_time_msec": 0,
                                                            "last_retrans_scan_length": 0,
                                                            "last_retrans_scan_time_msec": 0,
                                                        },
                                                    }
                                                }
                                            },
                                            "GigabitEthernet0/0/0/2": {
                                                "neighbors": {
                                                    "10.16.2.2": {
                                                        "address": "10.2.3.2",
                                                        "bdr_ip_addr": "10.2.3.2",
                                                        "dead_timer": "00:00:38",
                                                        "dr_ip_addr": "10.2.3.3",
                                                        "first": "0(0)/0(0)",
                                                        "high_water_mark": 0,
                                                        "index": "1/1,",
                                                        "ls_ack_list": "NSR-sync",
                                                        "ls_ack_list_pending": 0,
                                                        "neighbor_router_id": "10.16.2.2",
                                                        "neighbor_uptime": "08:22:07",
                                                        "next": "0(0)/0(0)",
                                                        "options": "0x42",
                                                        "priority": 1,
                                                        "state": "full",
                                                        "statistics": {
                                                            "nbr_event_count": 6,
                                                            "nbr_retrans_qlen": 0,
                                                            "total_retransmission": 0,
                                                            "total_dbd_retrans": 0,
                                                            "last_retrans_max_scan_length": 0,
                                                            "last_retrans_max_scan_time_msec": 0,
                                                            "last_retrans_scan_length": 0,
                                                            "last_retrans_scan_time_msec": 0,
                                                        },
                                                    }
                                                }
                                            },
                                        }
                                    }
                                },
                                "total_neighbor_count": 2,
                            }
                        }
                    }
                }
            },
        }
    }

    golden_output1 = {
        "execute.return_value": """
        RP/0/0/CPU0:R3_ospf_xr#show ospf vrf all-inclusive neighbor detail
        Thu Nov  2 21:28:53.636 UTC

        * Indicates MADJ interface
        # Indicates Neighbor awaiting BFD session up

        Neighbors for OSPF 1

         Neighbor 10.64.4.4, interface address 10.3.4.4
            In the area 0 via interface GigabitEthernet0/0/0/0
            Neighbor priority is 1, State is FULL, 6 state changes
            DR is 10.3.4.4 BDR is 10.3.4.3
            Options is 0x52
            LLS Options is 0x1 (LR)
            Dead timer due in 00:00:30
            Neighbor is up for 1d01h
            Number of DBD retrans during last exchange 0
            Index 2/2, retransmission queue length 0, number of retransmission 0
            First 0(0)/0(0) Next 0(0)/0(0)
            Last retransmission scan length is 0, maximum is 0
            Last retransmission scan time is 0 msec, maximum is 0 msec
            LS Ack list: NSR-sync pending 0, high water mark 0

         Neighbor 10.16.2.2, interface address 10.2.3.2
            In the area 0 via interface GigabitEthernet0/0/0/2
            Neighbor priority is 1, State is FULL, 6 state changes
            DR is 10.2.3.3 BDR is 10.2.3.2
            Options is 0x42
            Dead timer due in 00:00:38
            Neighbor is up for 08:22:07
            Number of DBD retrans during last exchange 0
            Index 1/1, retransmission queue length 0, number of retransmission 0
            First 0(0)/0(0) Next 0(0)/0(0)
            Last retransmission scan length is 0, maximum is 0
            Last retransmission scan time is 0 msec, maximum is 0 msec
            LS Ack list: NSR-sync pending 0, high water mark 0

        Total neighbor count: 2

        * Indicates MADJ interface
        # Indicates Neighbor awaiting BFD session up

        Neighbors for OSPF 1, VRF VRF1

         Neighbor 10.1.77.77, interface address 10.19.7.7
            In the area 1 via interface GigabitEthernet0/0/0/1
            Neighbor priority is 1, State is FULL, 6 state changes
            DR is 10.19.7.7 BDR is 10.19.7.3
            Options is 0x52
            LLS Options is 0x1 (LR)
            Dead timer due in 00:00:32
            Neighbor is up for 23:24:56
            Number of DBD retrans during last exchange 0
            Index 1/1, retransmission queue length 0, number of retransmission 15
            First 0(0)/0(0) Next 0(0)/0(0)
            Last retransmission scan length is 3, maximum is 3
            Last retransmission scan time is 0 msec, maximum is 0 msec
            LS Ack list: NSR-sync pending 0, high water mark 0

        Total neighbor count: 1
        """
    }

    golden_parsed_output2 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "1": {
                                "areas": {
                                    "0.0.0.1": {
                                        "virtual_links": {
                                            "0.0.0.1 10.64.4.4": {
                                                "neighbors": {
                                                    "10.64.4.4": {
                                                        "address": "10.229.4.4",
                                                        "bdr_ip_addr": "0.0.0.0",
                                                        "dr_ip_addr": "0.0.0.0",
                                                        "first": "0(0)/0(0)",
                                                        "high_water_mark": 0,
                                                        "index": "1/3,",
                                                        "lls_options": "0x1 (LR)",
                                                        "ls_ack_list": "NSR-sync",
                                                        "ls_ack_list_pending": 0,
                                                        "neighbor_router_id": "10.64.4.4",
                                                        "neighbor_uptime": "04:58:24",
                                                        "next": "0(0)/0(0)",
                                                        "options": "0x72",
                                                        "priority": 1,
                                                        "state": "full",
                                                        "statistics": {
                                                            "nbr_event_count": 7,
                                                            "nbr_retrans_qlen": 0,
                                                            "total_retransmission": 0,
                                                            "total_dbd_retrans": 0,
                                                            "last_retrans_max_scan_length": 0,
                                                            "last_retrans_max_scan_time_msec": 0,
                                                            "last_retrans_scan_length": 0,
                                                            "last_retrans_scan_time_msec": 0,
                                                        },
                                                    }
                                                }
                                            }
                                        },
                                        "interfaces": {
                                            "GigabitEthernet0/0/0/1": {
                                                "neighbors": {
                                                    "10.36.3.3": {
                                                        "address": "10.229.3.3",
                                                        "bdr_ip_addr": "10.229.3.2",
                                                        "dead_timer": "00:00:31",
                                                        "dr_ip_addr": "10.229.3.3",
                                                        "first": "0(0)/0(0)",
                                                        "high_water_mark": 0,
                                                        "index": "2/2,",
                                                        "ls_ack_list": "NSR-sync",
                                                        "ls_ack_list_pending": 0,
                                                        "neighbor_router_id": "10.36.3.3",
                                                        "neighbor_uptime": "05:00:13",
                                                        "next": "0(0)/0(0)",
                                                        "options": "0x42",
                                                        "priority": 1,
                                                        "state": "full",
                                                        "statistics": {
                                                            "nbr_event_count": 6,
                                                            "nbr_retrans_qlen": 0,
                                                            "total_retransmission": 2,
                                                            "total_dbd_retrans": 0,
                                                            "last_retrans_max_scan_length": 1,
                                                            "last_retrans_max_scan_time_msec": 0,
                                                            "last_retrans_scan_length": 1,
                                                            "last_retrans_scan_time_msec": 0,
                                                        },
                                                    }
                                                }
                                            },
                                            "GigabitEthernet0/0/0/3": {
                                                "neighbors": {
                                                    "10.64.4.4": {
                                                        "address": "10.229.4.4",
                                                        "bdr_ip_addr": "10.229.4.2",
                                                        "dead_timer": "00:00:32",
                                                        "dr_ip_addr": "10.229.4.4",
                                                        "first": "0(0)/0(0)",
                                                        "high_water_mark": 0,
                                                        "index": "1/1,",
                                                        "lls_options": "0x1 (LR)",
                                                        "ls_ack_list": "NSR-sync",
                                                        "ls_ack_list_pending": 0,
                                                        "neighbor_router_id": "10.64.4.4",
                                                        "neighbor_uptime": "05:00:21",
                                                        "next": "0(0)/0(0)",
                                                        "options": "0x52",
                                                        "priority": 1,
                                                        "state": "full",
                                                        "statistics": {
                                                            "nbr_event_count": 6,
                                                            "nbr_retrans_qlen": 0,
                                                            "total_retransmission": 0,
                                                            "total_dbd_retrans": 0,
                                                            "last_retrans_max_scan_length": 0,
                                                            "last_retrans_max_scan_time_msec": 0,
                                                            "last_retrans_scan_length": 0,
                                                            "last_retrans_scan_time_msec": 0,
                                                        },
                                                    }
                                                }
                                            },
                                        },
                                    }
                                },
                                "total_neighbor_count": 3,
                            }
                        }
                    }
                }
            }
        }
    }

    def test_show_ospf_vrf_all_inclusive_neighbor_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_neighbor_full2(self):
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        raw1 = """\
            RP/0/0/CPU0:R2_ospf_xr#show ospf vrf all-inclusive neighbor detail
            Tue Dec 12 20:21:16.846 UTC

            * Indicates MADJ interface
            # Indicates Neighbor awaiting BFD session up

            Neighbors for OSPF 1

             Neighbor 10.64.4.4, interface address 10.229.4.4
                In the area 0 via interface OSPF_VL0
                Neighbor priority is 1, State is FULL, 7 state changes
                DR is 0.0.0.0 BDR is 0.0.0.0
                Options is 0x72
                LLS Options is 0x1 (LR)
                Neighbor is up for 04:58:24
                Number of DBD retrans during last exchange 0
                Index 1/3, retransmission queue length 0, number of retransmission 0
                First 0(0)/0(0) Next 0(0)/0(0)
                Last retransmission scan length is 0, maximum is 0
                Last retransmission scan time is 0 msec, maximum is 0 msec
                LS Ack list: NSR-sync pending 0, high water mark 0

             Neighbor 10.36.3.3, interface address 10.229.3.3
                In the area 1 via interface GigabitEthernet0/0/0/1
                Neighbor priority is 1, State is FULL, 6 state changes
                DR is 10.229.3.3 BDR is 10.229.3.2
                Options is 0x42
                Dead timer due in 00:00:31
                Neighbor is up for 05:00:13
                Number of DBD retrans during last exchange 0
                Index 2/2, retransmission queue length 0, number of retransmission 2
                First 0(0)/0(0) Next 0(0)/0(0)
                Last retransmission scan length is 1, maximum is 1
                Last retransmission scan time is 0 msec, maximum is 0 msec
                LS Ack list: NSR-sync pending 0, high water mark 0

             Neighbor 10.64.4.4, interface address 10.229.4.4
                In the area 1 via interface GigabitEthernet0/0/0/3
                Neighbor priority is 1, State is FULL, 6 state changes
                DR is 10.229.4.4 BDR is 10.229.4.2
                Options is 0x52
                LLS Options is 0x1 (LR)
                Dead timer due in 00:00:32
                Neighbor is up for 05:00:21
                Number of DBD retrans during last exchange 0
                Index 1/1, retransmission queue length 0, number of retransmission 0
                First 0(0)/0(0) Next 0(0)/0(0)
                Last retransmission scan length is 0, maximum is 0
                Last retransmission scan time is 0 msec, maximum is 0 msec
                LS Ack list: NSR-sync pending 0, high water mark 0

            Total neighbor count: 3
        """

        raw2 = """\
            RP/0/0/CPU0:R2_ospf_xr#show ospf vrf all-inclusive virtual-links
            Fri Nov  3 01:25:44.845 UTC

            Virtual Links for OSPF 1

            Virtual Link OSPF_VL0 to router 10.64.4.4 is up

              DoNotAge LSA not allowed Run as demand circuit (Number of DCbitless LSA is 1).
              Transit area 1, via interface GigabitEthernet0/0/0/3, Cost of using 65535
              Transmit Delay is 5 sec, State POINT_TO_POINT,
              Non-Stop Forwarding (NSF) enabled, last NSF restart 00:18:16 ago
              Timer intervals configured, Hello 4, Dead 16, Wait 16, Retransmit 44
                Hello due in 00:00:03:179
              Clear text authentication enabled
            """

        self.outputs = {}
        self.outputs["show ospf vrf all-inclusive neighbor detail"] = raw1
        self.outputs["show ospf vrf all-inclusive virtual-links"] = raw2

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper

        obj = ShowOspfVrfAllInclusiveNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ospf_vrf_all_inclusive_neighbor_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveNeighborDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ospf_vrf_all_inclusive_neighbor_0(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output0)
        obj = ShowOspfVrfAllInclusiveNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output0)


# ============================================
#  Unit test for 'show ospf vrf all-inclusive'
# ============================================
class test_show_ospf_vrf_all_inclusive(unittest.TestCase):

    """Unit test for "show ospf vrf all-inclusive" """

    device = Device(name="aDevice")
    empty_output = {"execute.return_value": ""}

    golden_parsed_output1 = {
        "vrf": {
            "VRF1": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "1": {
                                "adjacency_stagger": {
                                    "disable": False,
                                    "initial_number": 2,
                                    "maximum_number": 64,
                                    "nbrs_forming": 0,
                                    "nbrs_full": 1,
                                },
                                "areas": {
                                    "0.0.0.1": {
                                        "area_type": "normal",
                                        "area_id": "0.0.0.1",
                                        "statistics": {
                                            "area_scope_lsa_cksum_sum": "0x04f437",
                                            "area_scope_lsa_count": 11,
                                            "area_scope_opaque_lsa_cksum_sum": "00000000",
                                            "area_scope_opaque_lsa_count": 0,
                                            "dcbitless_lsa_count": 1,
                                            "donotage_lsa_count": 0,
                                            "flood_list_length": 0,
                                            "indication_lsa_count": 0,
                                            "interfaces_count": 2,
                                            "lfa_interface_count": 0,
                                            "lfa_per_prefix_interface_count": 0,
                                            "lfa_revision": 0,
                                            "nbrs_full": 1,
                                            "nbrs_staggered_mode": 0,
                                            "spf_runs_count": 79,
                                        },
                                    }
                                },
                                "database_control": {"max_lsa": 123},
                                "external_flood_list_length": 0,
                                "flags": {"abr": True, "asbr": True},
                                "flood_pacing_interval_msec": 33,
                                "lsd_revision": 1,
                                "lsd_state": "connected, registered, bound",
                                "maximum_interfaces": 1024,
                                "nsr": {"enable": True},
                                "numbers": {
                                    "dc_bitless": 0,
                                    "do_not_age": 0,
                                    "external_lsa": 0,
                                    "external_lsa_checksum": "00000000",
                                    "opaque_as_lsa": 0,
                                    "opaque_as_lsa_checksum": "00000000",
                                },
                                "redistribution": {
                                    "bgp": {"bgp_id": 100},
                                    "max_prefix": {
                                        "num_of_prefix": 10240,
                                        "prefix_thld": 75,
                                        "warn_only": False,
                                    },
                                },
                                "retransmission_pacing_interval": 66,
                                "role": "primary active",
                                "router_id": "10.36.3.3",
                                "segment_routing_global_block_default": "16000-23999",
                                "segment_routing_global_block_status": "not allocated",
                                "snmp_trap": False,
                                "spf_control": {
                                    "throttle": {
                                        "lsa": {
                                            "arrival": 100,
                                            "hold": 200,
                                            "interval": 200,
                                            "maximum": 5000,
                                            "refresh_interval": 1800,
                                            "start": 50,
                                        },
                                        "spf": {
                                            "hold": 200,
                                            "maximum": 5000,
                                            "start": 50,
                                        },
                                    }
                                },
                                "strict_spf": True,
                                "total_areas": 1,
                                "total_normal_areas": 1,
                                "total_nssa_areas": 0,
                                "total_stub_areas": 0,
                                "stub_router": {
                                    "always": {
                                        "always": False,
                                        "external_lsa": False,
                                        "include_stub": False,
                                        "summary_lsa": False,
                                    }
                                },
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
                                "adjacency_stagger": {
                                    "disable": False,
                                    "initial_number": 2,
                                    "maximum_number": 64,
                                    "nbrs_forming": 0,
                                    "nbrs_full": 2,
                                },
                                "areas": {
                                    "0.0.0.0": {
                                        "area_type": "normal",
                                        "area_id": "0.0.0.0",
                                        "rrr_enabled": True,
                                        "statistics": {
                                            "area_scope_lsa_cksum_sum": "0x0a2fb5",
                                            "area_scope_lsa_count": 19,
                                            "area_scope_opaque_lsa_cksum_sum": "00000000",
                                            "area_scope_opaque_lsa_count": 0,
                                            "dcbitless_lsa_count": 5,
                                            "donotage_lsa_count": 0,
                                            "flood_list_length": 0,
                                            "indication_lsa_count": 0,
                                            "interfaces_count": 3,
                                            "lfa_interface_count": 0,
                                            "lfa_per_prefix_interface_count": 0,
                                            "lfa_revision": 0,
                                            "nbrs_full": 2,
                                            "nbrs_staggered_mode": 0,
                                            "spf_runs_count": 26,
                                        },
                                        "topology_version": 15,
                                    }
                                },
                                "external_flood_list_length": 0,
                                "flood_pacing_interval_msec": 33,
                                "lsd_revision": 1,
                                "lsd_state": "connected, registered, bound",
                                "maximum_interfaces": 1024,
                                "mpls": {
                                    "ldp": {
                                        "ldp_igp_sync": True,
                                        "ldp_sync_status": "not achieved",
                                    }
                                },
                                "nsr": {"enable": True},
                                "numbers": {
                                    "dc_bitless": 0,
                                    "do_not_age": 0,
                                    "external_lsa": 1,
                                    "external_lsa_checksum": "0x00607f",
                                    "opaque_as_lsa": 0,
                                    "opaque_as_lsa_checksum": "00000000",
                                },
                                "retransmission_pacing_interval": 66,
                                "role": "primary active",
                                "router_id": "10.36.3.3",
                                "segment_routing_global_block_default": "16000-23999",
                                "segment_routing_global_block_status": "not allocated",
                                "snmp_trap": True,
                                "spf_control": {
                                    "throttle": {
                                        "lsa": {
                                            "arrival": 100,
                                            "hold": 200,
                                            "interval": 200,
                                            "maximum": 5000,
                                            "refresh_interval": 1800,
                                            "start": 50,
                                        },
                                        "spf": {
                                            "hold": 200,
                                            "maximum": 5000,
                                            "start": 50,
                                        },
                                    }
                                },
                                "strict_spf": True,
                                "total_areas": 1,
                                "total_normal_areas": 1,
                                "total_nssa_areas": 0,
                                "total_stub_areas": 0,
                                "stub_router": {
                                    "always": {
                                        "always": True,
                                        "external_lsa": True,
                                        "external_lsa_metric": 16711680,
                                        "include_stub": True,
                                        "state": "active",
                                        "summary_lsa": True,
                                        "summary_lsa_metric": 16711680,
                                    },
                                    "on_startup": {
                                        "on_startup": 5,
                                        "external_lsa": True,
                                        "external_lsa_metric": 16711680,
                                        "include_stub": True,
                                        "state": "inactive",
                                        "summary_lsa": True,
                                        "summary_lsa_metric": 16711680,
                                    },
                                    "on_switchover": {
                                        "on_switchover": 10,
                                        "external_lsa": True,
                                        "external_lsa_metric": 16711680,
                                        "include_stub": True,
                                        "state": "inactive",
                                        "summary_lsa": True,
                                        "summary_lsa_metric": 16711680,
                                    },
                                },
                            }
                        }
                    }
                }
            },
        }
    }

    golden_output1 = {
        "execute.return_value": """
        RP/0/0/CPU0:R3_ospf_xr#show ospf vrf all-inclusive
        Thu Nov  2 21:14:35.895 UTC

         Routing Process "ospf 1" with ID 10.36.3.3
         Role: Primary Active
         NSR (Non-stop routing) is Enabled
         Supports only single TOS(TOS0) routes
         Supports opaque LSA
         Originating router-LSAs with maximum metric
         Condition: on switch-over for 10 seconds, State: inactive
            Advertise stub links with maximum metric in router-LSAs
            Advertise summary-LSAs with metric 16711680
            Advertise external-LSAs with metric 16711680
         Condition: on start-up for 5 seconds, State: inactive
            Advertise stub links with maximum metric in router-LSAs
            Advertise summary-LSAs with metric 16711680
            Advertise external-LSAs with metric 16711680
         Condition: always State: active
            Advertise stub links with maximum metric in router-LSAs
            Advertise summary-LSAs with metric 16711680
            Advertise external-LSAs with metric 16711680
         Initial SPF schedule delay 50 msecs
         Minimum hold time between two consecutive SPFs 200 msecs
         Maximum wait time between two consecutive SPFs 5000 msecs
         Initial LSA throttle delay 50 msecs
         Minimum hold time for LSA throttle 200 msecs
         Maximum wait time for LSA throttle 5000 msecs
         Minimum LSA interval 200 msecs. Minimum LSA arrival 100 msecs
         LSA refresh interval 1800 seconds
         Flood pacing interval 33 msecs. Retransmission pacing interval 66 msecs
         Adjacency stagger enabled; initial (per area): 2, maximum: 64
            Number of neighbors forming: 0, 2 full
         Maximum number of configured interfaces 1024
         Number of external LSA 1. Checksum Sum 0x00607f
         Number of opaque AS LSA 0. Checksum Sum 00000000
         Number of DCbitless external and opaque AS LSA 0
         Number of DoNotAge external and opaque AS LSA 0
         Number of areas in this router is 1. 1 normal 0 stub 0 nssa
         External flood list length 0
         SNMP trap is enabled
         LDP Sync Enabled, Sync Status: Not Achieved
         LSD connected, registered, bound, revision 1
         Segment Routing Global Block default (16000-23999), not allocated
         Strict-SPF capability is enabled
            Area BACKBONE(0)
                Number of interfaces in this area is 3
                Area has RRR enabled, topology version 15
                SPF algorithm executed 26 times
                Number of LSA 19.  Checksum Sum 0x0a2fb5
                Number of opaque link LSA 0.  Checksum Sum 00000000
                Number of DCbitless LSA 5
                Number of indication LSA 0
                Number of DoNotAge LSA 0
                Flood list length 0
                Number of LFA enabled interfaces 0, LFA revision 0
                Number of Per Prefix LFA enabled interfaces 0
                Number of neighbors forming in staggered mode 0, 2 full


         VRF VRF1 in Routing Process "ospf 1" with ID 10.36.3.3
         Role: Primary Active
         NSR (Non-stop routing) is Enabled
         Supports only single TOS(TOS0) routes
         Supports opaque LSA
         It is an area border and autonomous system boundary router
         Redistributing External Routes from,
            bgp 100
            Maximum number of redistributed prefixes 10240
            Threshold for warning message 75%
         Router is not originating router-LSAs with maximum metric
         Initial SPF schedule delay 50 msecs
         Minimum hold time between two consecutive SPFs 200 msecs
         Maximum wait time between two consecutive SPFs 5000 msecs
         Initial LSA throttle delay 50 msecs
         Minimum hold time for LSA throttle 200 msecs
         Maximum wait time for LSA throttle 5000 msecs
         Minimum LSA interval 200 msecs. Minimum LSA arrival 100 msecs
         LSA refresh interval 1800 seconds
         Flood pacing interval 33 msecs. Retransmission pacing interval 66 msecs
         Adjacency stagger enabled; initial (per area): 2, maximum: 64
            Number of neighbors forming: 0, 1 full
         Maximum number of configured interfaces 1024
         Maximum number of non self-generated LSA allowed 123
         Number of external LSA 0. Checksum Sum 00000000
         Number of opaque AS LSA 0. Checksum Sum 00000000
         Number of DCbitless external and opaque AS LSA 0
         Number of DoNotAge external and opaque AS LSA 0
         Number of areas in this router is 1. 1 normal 0 stub 0 nssa
         External flood list length 0
         SNMP trap is disabled
         LSD connected, registered, bound, revision 1
         Segment Routing Global Block default (16000-23999), not allocated
         Strict-SPF capability is enabled
            Area 1
                Number of interfaces in this area is 2
                SPF algorithm executed 79 times
                Number of LSA 11.  Checksum Sum 0x04f437
                Number of opaque link LSA 0.  Checksum Sum 00000000
                Number of DCbitless LSA 1
                Number of indication LSA 0
                Number of DoNotAge LSA 0
                Flood list length 0
                Number of LFA enabled interfaces 0, LFA revision 0
                Number of Per Prefix LFA enabled interfaces 0
                Number of neighbors forming in staggered mode 0, 1 full
        """
    }

    golden_parsed_output2 = {
        "vrf": {
            "VRF1": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "1": {
                                "adjacency_stagger": {
                                    "disable": False,
                                    "initial_number": 2,
                                    "maximum_number": 64,
                                    "nbrs_forming": 0,
                                    "nbrs_full": 1,
                                },
                                "areas": {
                                    "0.0.0.1": {
                                        "area_id": "0.0.0.1",
                                        "area_type": "normal",
                                        "statistics": {
                                            "area_scope_lsa_cksum_sum": "0x04b760",
                                            "area_scope_lsa_count": 9,
                                            "area_scope_opaque_lsa_cksum_sum": "00000000",
                                            "area_scope_opaque_lsa_count": 0,
                                            "dcbitless_lsa_count": 0,
                                            "donotage_lsa_count": 0,
                                            "flood_list_length": 0,
                                            "indication_lsa_count": 0,
                                            "interfaces_count": 2,
                                            "lfa_interface_count": 0,
                                            "lfa_per_prefix_interface_count": 0,
                                            "lfa_revision": 0,
                                            "nbrs_full": 1,
                                            "nbrs_staggered_mode": 0,
                                            "spf_runs_count": 3,
                                        },
                                    }
                                },
                                "external_flood_list_length": 0,
                                "flags": {"abr": True, "asbr": True},
                                "flood_pacing_interval_msec": 33,
                                "graceful_restart": {
                                    "ietf": {"enable": True, "type": "ietf"}
                                },
                                "lsd_revision": 1,
                                "lsd_state": "connected, registered, bound",
                                "maximum_interfaces": 1024,
                                "nsr": {"enable": True},
                                "numbers": {
                                    "dc_bitless": 0,
                                    "do_not_age": 0,
                                    "external_lsa": 3,
                                    "external_lsa_checksum": "0x01df46",
                                    "opaque_as_lsa": 0,
                                    "opaque_as_lsa_checksum": "00000000",
                                },
                                "redistribution": {
                                    "bgp": {"bgp_id": 100, "metric": 111},
                                    "connected": {"enabled": True, "metric": 10},
                                    "isis": {"isis_pid": "10", "metric": 3333},
                                    "max_prefix": {
                                        "num_of_prefix": 4000,
                                        "prefix_thld": 70,
                                        "warn_only": False,
                                    },
                                    "static": {"enabled": True},
                                },
                                "retransmission_pacing_interval": 66,
                                "role": "primary active",
                                "router_id": "10.36.3.3",
                                "segment_routing_global_block_default": "16000-23999",
                                "segment_routing_global_block_status": "not allocated",
                                "snmp_trap": False,
                                "spf_control": {
                                    "throttle": {
                                        "lsa": {
                                            "arrival": 100,
                                            "hold": 200,
                                            "interval": 200,
                                            "maximum": 5000,
                                            "refresh_interval": 1800,
                                            "start": 50,
                                        },
                                        "spf": {
                                            "hold": 200,
                                            "maximum": 5000,
                                            "start": 50,
                                        },
                                    }
                                },
                                "strict_spf": True,
                                "stub_router": {
                                    "always": {
                                        "always": False,
                                        "external_lsa": False,
                                        "include_stub": False,
                                        "summary_lsa": False,
                                    }
                                },
                                "total_areas": 1,
                                "total_normal_areas": 1,
                                "total_nssa_areas": 0,
                                "total_stub_areas": 0,
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
                                "adjacency_stagger": {
                                    "disable": False,
                                    "initial_number": 2,
                                    "maximum_number": 64,
                                    "nbrs_forming": 0,
                                    "nbrs_full": 1,
                                },
                                "areas": {
                                    "0.0.0.0": {
                                        "area_id": "0.0.0.0",
                                        "area_type": "normal",
                                        "rrr_enabled": True,
                                        "statistics": {
                                            "area_scope_lsa_cksum_sum": "0x07a597",
                                            "area_scope_lsa_count": 14,
                                            "area_scope_opaque_lsa_cksum_sum": "00000000",
                                            "area_scope_opaque_lsa_count": 0,
                                            "dcbitless_lsa_count": 0,
                                            "donotage_lsa_count": 0,
                                            "flood_list_length": 0,
                                            "indication_lsa_count": 0,
                                            "interfaces_count": 5,
                                            "lfa_interface_count": 0,
                                            "lfa_per_prefix_interface_count": 0,
                                            "lfa_revision": 0,
                                            "nbrs_full": 1,
                                            "nbrs_staggered_mode": 0,
                                            "spf_runs_count": 12,
                                        },
                                        "topology_version": 7,
                                    },
                                    "0.0.0.1": {
                                        "area_id": "0.0.0.1",
                                        "area_type": "stub",
                                        "summary": True,
                                        "default_cost": 111,
                                        "ranges": {
                                            "10.4.0.0/16": {
                                                "advertise": True,
                                                "prefix": "10.4.0.0/16",
                                            }
                                        },
                                        "statistics": {
                                            "area_scope_lsa_cksum_sum": "0x05adf0",
                                            "area_scope_lsa_count": 13,
                                            "area_scope_opaque_lsa_cksum_sum": "00000000",
                                            "area_scope_opaque_lsa_count": 0,
                                            "dcbitless_lsa_count": 0,
                                            "donotage_lsa_count": 0,
                                            "flood_list_length": 0,
                                            "indication_lsa_count": 0,
                                            "interfaces_count": 1,
                                            "lfa_interface_count": 0,
                                            "lfa_per_prefix_interface_count": 0,
                                            "lfa_revision": 0,
                                            "nbrs_full": 0,
                                            "nbrs_staggered_mode": 0,
                                            "spf_runs_count": 8,
                                        },
                                    },
                                    "0.0.0.2": {
                                        "area_id": "0.0.0.2",
                                        "area_type": "stub",
                                        "summary": False,
                                        "default_cost": 222,
                                        "ranges": {
                                            "10.4.1.0/24": {
                                                "advertise": True,
                                                "prefix": "10.4.1.0/24",
                                            }
                                        },
                                        "statistics": {
                                            "area_scope_lsa_cksum_sum": "0x0076bf",
                                            "area_scope_lsa_count": 2,
                                            "area_scope_opaque_lsa_cksum_sum": "00000000",
                                            "area_scope_opaque_lsa_count": 0,
                                            "dcbitless_lsa_count": 0,
                                            "donotage_lsa_count": 0,
                                            "flood_list_length": 0,
                                            "indication_lsa_count": 0,
                                            "interfaces_count": 1,
                                            "lfa_interface_count": 0,
                                            "lfa_per_prefix_interface_count": 0,
                                            "lfa_revision": 0,
                                            "nbrs_full": 0,
                                            "nbrs_staggered_mode": 0,
                                            "spf_runs_count": 4,
                                        },
                                    },
                                    "0.0.0.3": {
                                        "area_id": "0.0.0.3",
                                        "area_type": "nssa",
                                        "lsa_translation": "type-7/type-5",
                                        "ranges": {
                                            "10.16.2.0/24": {
                                                "advertise": True,
                                                "prefix": "10.16.2.0/24",
                                            }
                                        },
                                        "statistics": {
                                            "area_scope_lsa_cksum_sum": "0x09166c",
                                            "area_scope_lsa_count": 14,
                                            "area_scope_opaque_lsa_cksum_sum": "00000000",
                                            "area_scope_opaque_lsa_count": 0,
                                            "dcbitless_lsa_count": 0,
                                            "donotage_lsa_count": 0,
                                            "flood_list_length": 0,
                                            "indication_lsa_count": 0,
                                            "interfaces_count": 1,
                                            "lfa_interface_count": 0,
                                            "lfa_per_prefix_interface_count": 0,
                                            "lfa_revision": 0,
                                            "nbrs_full": 0,
                                            "nbrs_staggered_mode": 0,
                                            "spf_runs_count": 4,
                                        },
                                    },
                                    "0.0.0.4": {
                                        "area_id": "0.0.0.4",
                                        "area_type": "nssa",
                                        "lsa_translation": "type-7/type-5",
                                        "statistics": {
                                            "area_scope_lsa_cksum_sum": "0x022418",
                                            "area_scope_lsa_count": 4,
                                            "area_scope_opaque_lsa_cksum_sum": "00000000",
                                            "area_scope_opaque_lsa_count": 0,
                                            "dcbitless_lsa_count": 0,
                                            "donotage_lsa_count": 0,
                                            "flood_list_length": 0,
                                            "indication_lsa_count": 0,
                                            "interfaces_count": 1,
                                            "lfa_interface_count": 0,
                                            "lfa_per_prefix_interface_count": 0,
                                            "lfa_revision": 0,
                                            "nbrs_full": 0,
                                            "nbrs_staggered_mode": 0,
                                            "spf_runs_count": 4,
                                        },
                                    },
                                },
                                "external_flood_list_length": 0,
                                "flags": {"abr": True, "asbr": True},
                                "flood_pacing_interval_msec": 33,
                                "graceful_restart": {
                                    "cisco": {"enable": True, "type": "cisco"}
                                },
                                "lsd_revision": 1,
                                "lsd_state": "connected, registered, bound",
                                "maximum_interfaces": 1024,
                                "nsr": {"enable": True},
                                "numbers": {
                                    "dc_bitless": 0,
                                    "do_not_age": 0,
                                    "external_lsa": 3,
                                    "external_lsa_checksum": "0x01b657",
                                    "opaque_as_lsa": 0,
                                    "opaque_as_lsa_checksum": "00000000",
                                },
                                "redistribution": {
                                    "bgp": {"bgp_id": 100, "metric": 111},
                                    "connected": {"enabled": True},
                                    "isis": {"isis_pid": "10", "metric": 3333},
                                    "max_prefix": {
                                        "num_of_prefix": 3000,
                                        "prefix_thld": 90,
                                        "warn_only": True,
                                    },
                                    "static": {"enabled": True, "metric": 10},
                                },
                                "retransmission_pacing_interval": 66,
                                "role": "primary active",
                                "router_id": "10.36.3.3",
                                "segment_routing_global_block_default": "16000-23999",
                                "segment_routing_global_block_status": "not allocated",
                                "snmp_trap": True,
                                "spf_control": {
                                    "throttle": {
                                        "lsa": {
                                            "arrival": 100,
                                            "hold": 200,
                                            "interval": 200,
                                            "maximum": 5000,
                                            "refresh_interval": 1800,
                                            "start": 50,
                                        },
                                        "spf": {
                                            "hold": 200,
                                            "maximum": 5000,
                                            "start": 50,
                                        },
                                    }
                                },
                                "strict_spf": True,
                                "stub_router": {
                                    "always": {
                                        "always": False,
                                        "external_lsa": False,
                                        "include_stub": False,
                                        "summary_lsa": False,
                                    }
                                },
                                "total_areas": 5,
                                "total_normal_areas": 1,
                                "total_nssa_areas": 2,
                                "total_stub_areas": 2,
                            }
                        }
                    }
                }
            },
        }
    }

    golden_output2 = {
        "execute.return_value": """

        RP/0/0/CPU0:R3_ospf_xr#show run formal router ospf | i nsf
            router ospf 1 nsf cisco
            router ospf 1 vrf VRF1 nsf ietf

        RP/0/0/CPU0:R3_ospf_xr#show ospf vrf all-inclusive
        Mon Jan  8 22:09:54.605 UTC

         Routing Process "ospf 1" with ID 10.36.3.3
         Role: Primary Active
         NSR (Non-stop routing) is Enabled
         Supports only single TOS(TOS0) routes
         Supports opaque LSA
         It is an area border and autonomous system boundary router
         Redistributing External Routes from,
            connected
            static with metric mapped to 10
            bgp 100 with metric mapped to 111
            isis 10 with metric mapped to 3333
            Maximum number of redistributed prefixes 3000 (warning-only)
            Threshold for warning message 90%
         Router is not originating router-LSAs with maximum metric
         Initial SPF schedule delay 50 msecs
         Minimum hold time between two consecutive SPFs 200 msecs
         Maximum wait time between two consecutive SPFs 5000 msecs
         Initial LSA throttle delay 50 msecs
         Minimum hold time for LSA throttle 200 msecs
         Maximum wait time for LSA throttle 5000 msecs
         Minimum LSA interval 200 msecs. Minimum LSA arrival 100 msecs
         LSA refresh interval 1800 seconds
         Flood pacing interval 33 msecs. Retransmission pacing interval 66 msecs
         Adjacency stagger enabled; initial (per area): 2, maximum: 64
            Number of neighbors forming: 0, 1 full
         Maximum number of configured interfaces 1024
         Number of external LSA 3. Checksum Sum 0x01b657
         Number of opaque AS LSA 0. Checksum Sum 00000000
         Number of DCbitless external and opaque AS LSA 0
         Number of DoNotAge external and opaque AS LSA 0
         Number of areas in this router is 5. 1 normal 2 stub 2 nssa
         External flood list length 0
         Non-Stop Forwarding enabled
         SNMP trap is enabled
         LSD connected, registered, bound, revision 1
         Segment Routing Global Block default (16000-23999), not allocated
         Strict-SPF capability is enabled
            Area BACKBONE(0)
                Number of interfaces in this area is 5
                Area has RRR enabled, topology version 7
                SPF algorithm executed 12 times
                Number of LSA 14.  Checksum Sum 0x07a597
                Number of opaque link LSA 0.  Checksum Sum 00000000
                Number of DCbitless LSA 0
                Number of indication LSA 0
                Number of DoNotAge LSA 0
                Flood list length 0
                Number of LFA enabled interfaces 0, LFA revision 0
                Number of Per Prefix LFA enabled interfaces 0
                Number of neighbors forming in staggered mode 0, 1 full
            Area 1
                Number of interfaces in this area is 1
                It is a stub area
                  generates stub default route with cost 111
                SPF algorithm executed 8 times
                Area ranges are
                   10.4.0.0/16 Passive DoNotAdvertise
                Number of LSA 13.  Checksum Sum 0x05adf0
                Number of opaque link LSA 0.  Checksum Sum 00000000
                Number of DCbitless LSA 0
                Number of indication LSA 0
                Number of DoNotAge LSA 0
                Flood list length 0
                Number of LFA enabled interfaces 0, LFA revision 0
                Number of Per Prefix LFA enabled interfaces 0
                Number of neighbors forming in staggered mode 0, 0 full
            Area 2
                Number of interfaces in this area is 1
                It is a stub area, no summary LSA in this area
                  generates stub default route with cost 222
                SPF algorithm executed 4 times
                Area ranges are
                   10.4.1.0/24 Passive Advertise
                Number of LSA 2.  Checksum Sum 0x0076bf
                Number of opaque link LSA 0.  Checksum Sum 00000000
                Number of DCbitless LSA 0
                Number of indication LSA 0
                Number of DoNotAge LSA 0
                Flood list length 0
                Number of LFA enabled interfaces 0, LFA revision 0
                Number of Per Prefix LFA enabled interfaces 0
                Number of neighbors forming in staggered mode 0, 0 full
            Area 3
                Number of interfaces in this area is 1
                It is a NSSA area
                Perform type-7/type-5 LSA translation
                SPF algorithm executed 4 times
                Area ranges are
                   10.16.2.0/24 Passive Advertise
                Number of LSA 14.  Checksum Sum 0x09166c
                Number of opaque link LSA 0.  Checksum Sum 00000000
                Number of DCbitless LSA 0
                Number of indication LSA 0
                Number of DoNotAge LSA 0
                Flood list length 0
                Number of LFA enabled interfaces 0, LFA revision 0
                Number of Per Prefix LFA enabled interfaces 0
                Number of neighbors forming in staggered mode 0, 0 full
            Area 4
                Number of interfaces in this area is 1
                It is a NSSA area
                Perform type-7/type-5 LSA translation
                SPF algorithm executed 4 times
                Number of LSA 4.  Checksum Sum 0x022418
                Number of opaque link LSA 0.  Checksum Sum 00000000
                Number of DCbitless LSA 0
                Number of indication LSA 0
                Number of DoNotAge LSA 0
                Flood list length 0
                Number of LFA enabled interfaces 0, LFA revision 0
                Number of Per Prefix LFA enabled interfaces 0
                Number of neighbors forming in staggered mode 0, 0 full


         VRF VRF1 in Routing Process "ospf 1" with ID 10.36.3.3
         Role: Primary Active
         NSR (Non-stop routing) is Enabled
         Supports only single TOS(TOS0) routes
         Supports opaque LSA
         It is an area border and autonomous system boundary router
         Redistributing External Routes from,
            connected with metric mapped to 10
            bgp 100 with metric mapped to 111
            static
            isis 10 with metric mapped to 3333
            Maximum number of redistributed prefixes 4000
            Threshold for warning message 70%
         Router is not originating router-LSAs with maximum metric
         Initial SPF schedule delay 50 msecs
         Minimum hold time between two consecutive SPFs 200 msecs
         Maximum wait time between two consecutive SPFs 5000 msecs
         Initial LSA throttle delay 50 msecs
         Minimum hold time for LSA throttle 200 msecs
         Maximum wait time for LSA throttle 5000 msecs
         Minimum LSA interval 200 msecs. Minimum LSA arrival 100 msecs
         LSA refresh interval 1800 seconds
         Flood pacing interval 33 msecs. Retransmission pacing interval 66 msecs
         Adjacency stagger enabled; initial (per area): 2, maximum: 64
            Number of neighbors forming: 0, 1 full
         Maximum number of configured interfaces 1024
         Number of external LSA 3. Checksum Sum 0x01df46
         Number of opaque AS LSA 0. Checksum Sum 00000000
         Number of DCbitless external and opaque AS LSA 0
         Number of DoNotAge external and opaque AS LSA 0
         Number of areas in this router is 1. 1 normal 0 stub 0 nssa
         External flood list length 0
         Non-Stop Forwarding enabled
         SNMP trap is disabled
         LSD connected, registered, bound, revision 1
         Segment Routing Global Block default (16000-23999), not allocated
         Strict-SPF capability is enabled
            Area 1
                Number of interfaces in this area is 2
                SPF algorithm executed 3 times
                Number of LSA 9.  Checksum Sum 0x04b760
                Number of opaque link LSA 0.  Checksum Sum 00000000
                Number of DCbitless LSA 0
                Number of indication LSA 0
                Number of DoNotAge LSA 0
                Flood list length 0
                Number of LFA enabled interfaces 0, LFA revision 0
                Number of Per Prefix LFA enabled interfaces 0
                Number of neighbors forming in staggered mode 0, 1 full
        """
    }

    golden_output3 = {
        "execute.return_value": """
        show ospf vrf all-inclusive

Wed Jun 17 11:14:00.030 UTC

 Routing Process "ospf 10" with ID 10.0.12.56
 Role: Primary Active
 NSR (Non-stop routing) is Enabled
 Supports only single TOS(TOS0) routes
 Supports opaque LSA
 Originating router-LSAs with maximum metric
    Condition: on start-up while BGP is converging, State: inactive
       Advertise stub links with maximum metric in router-LSAs
    Last max-metric unset reason: unconfigured
    Last max-metric set condition: always
    Last max-metric unset time: Apr  6 10:18:36.777, Time elapsed: 2y10w
 Initial SPF schedule delay 100 msecs
 Minimum hold time between two consecutive SPFs 500 msecs
 Maximum wait time between two consecutive SPFs 10000 msecs
 Initial LSA throttle delay 0 msecs
 Minimum hold time for LSA throttle 25 msecs
 Maximum wait time for LSA throttle 10000 msecs
 Minimum LSA interval 25 msecs. Minimum LSA arrival 0 msecs
 LSA refresh interval 1800 seconds
 Flood pacing interval 33 msecs. Retransmission pacing interval 66 msecs
 Adjacency stagger enabled; initial (per area): 2, maximum: 64
    Number of neighbors forming: 0, 2 full
 Maximum number of configured interfaces 1024
 Number of external LSA 145. Checksum Sum 0x40c673
 Number of opaque AS LSA 0. Checksum Sum 00000000
 Number of DCbitless external and opaque AS LSA 0
 Number of DoNotAge external and opaque AS LSA 0
 Number of areas in this router is 1. 1 normal 0 stub 0 nssa
 External flood list length 0
 IPFRR per-prefix tiebreakers:
    Name                    Index
    No Tunnel (Implicit)    255
    Node Protection         40
    Line-card Disjoint      30
    Lowest Metric           20
    Primary Path            10
    Downstream              0
    Secondary Path          0
    SRLG Disjoint           0
    Post Convergence Path   0
 SNMP trap is enabled
 LSD connected, registered, bound, revision 1
 Segment Routing Global Block default (16000-23999), not allocated
    Area BACKBONE(0)
	Number of interfaces in this area is 6
	Area has RRR enabled, topology version 390659
	SPF algorithm executed 366720 times
	Number of LSA 786.  Checksum Sum 0x1849b5b
	Number of opaque link LSA 0.  Checksum Sum 00000000
	Number of DCbitless LSA 166
	Number of indication LSA 0
	Number of DoNotAge LSA 0
	Flood list length 0
	Number of LFA enabled interfaces 2, LFA revision 366718
	Number of Per Prefix LFA enabled interfaces 0
	Number of neighbors forming in staggered mode 0, 2 full
    """
    }

    golden_parsed_output3 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "10": {
                                "ipfrr_per_prefix_tiebreakers": {
                                    "post_convergence_path": "0",
                                    "srlg_disjoint": "0",
                                    "downstream": "0",
                                    "line_card_disjoint": "30",
                                    "lowest_metric": "20",
                                    "name": "Index",
                                    "no_tunnel": "255",
                                    "node_protection": "40",
                                    "primary_path": "10",
                                    "secondary_path": "0",
                                },
                                "adjacency_stagger": {
                                    "disable": False,
                                    "initial_number": 2,
                                    "maximum_number": 64,
                                    "nbrs_forming": 0,
                                    "nbrs_full": 2,
                                },
                                "areas": {
                                    "0.0.0.0": {
                                        "area_id": "0.0.0.0",
                                        "area_type": "normal",
                                        "rrr_enabled": True,
                                        "statistics": {
                                            "area_scope_lsa_cksum_sum": "0x1849b5b",
                                            "area_scope_lsa_count": 786,
                                            "area_scope_opaque_lsa_cksum_sum": "00000000",
                                            "area_scope_opaque_lsa_count": 0,
                                            "dcbitless_lsa_count": 166,
                                            "donotage_lsa_count": 0,
                                            "flood_list_length": 0,
                                            "indication_lsa_count": 0,
                                            "interfaces_count": 6,
                                            "lfa_interface_count": 2,
                                            "lfa_per_prefix_interface_count": 0,
                                            "lfa_revision": 366718,
                                            "nbrs_full": 2,
                                            "nbrs_staggered_mode": 0,
                                            "spf_runs_count": 366720,
                                        },
                                        "topology_version": 390659,
                                    }
                                },
                                "external_flood_list_length": 0,
                                "flood_pacing_interval_msec": 33,
                                "lsd_revision": 1,
                                "lsd_state": "connected, " "registered, " "bound",
                                "maximum_interfaces": 1024,
                                "nsr": {"enable": True},
                                "numbers": {
                                    "dc_bitless": 0,
                                    "do_not_age": 0,
                                    "external_lsa": 145,
                                    "external_lsa_checksum": "0x40c673",
                                    "opaque_as_lsa": 0,
                                    "opaque_as_lsa_checksum": "00000000",
                                },
                                "retransmission_pacing_interval": 66,
                                "role": "primary " "active",
                                "router_id": "10.0.12.56",
                                "segment_routing_global_block_default": "16000-23999",
                                "segment_routing_global_block_status": "not "
                                "allocated",
                                "snmp_trap": True,
                                "spf_control": {
                                    "throttle": {
                                        "lsa": {
                                            "arrival": 0,
                                            "hold": 25,
                                            "interval": 25,
                                            "maximum": 10000,
                                            "refresh_interval": 1800,
                                            "start": 0,
                                        },
                                        "spf": {
                                            "hold": 500,
                                            "maximum": 10000,
                                            "start": 100,
                                        },
                                    }
                                },
                                "stub_router": {"always": {"include_stub": True}},
                                "total_areas": 1,
                                "total_normal_areas": 1,
                                "total_nssa_areas": 0,
                                "total_stub_areas": 0,
                            }
                        }
                    }
                }
            }
        }
    }

    def test_show_ospf_vrf_all_inclusive_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowOspfVrfAllInclusive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ospf_vrf_all_inclusive_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowOspfVrfAllInclusive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_ospf_vrf_all_inclusive_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =======================================================
#  Unit test for 'show ospf vrf all-inclusive sham-links'
# =======================================================
class test_show_ospf_vrf_all_inclusive_sham_links(unittest.TestCase):

    """Unit test for "show ospf vrf all-inclusive sham-links" """

    device = Device(name="aDevice")
    empty_output = {"execute.return_value": ""}

    golden_parsed_output1 = {
        "vrf": {
            "VRF1": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "1": {
                                "areas": {
                                    "0.0.0.1": {
                                        "sham_links": {
                                            "10.21.33.33 10.151.22.22": {
                                                "cost": 111,
                                                "dcbitless_lsa_count": 1,
                                                "donotage_lsa": "not allowed",
                                                "dead_interval": 13,
                                                "demand_circuit": True,
                                                "hello_interval": 3,
                                                "hello_timer": "00:00:00:772",
                                                "if_index": 2,
                                                "local_id": "10.21.33.33",
                                                "name": "SL0",
                                                "link_state": "up",
                                                "remote_id": "10.151.22.22",
                                                "retransmit_interval": 5,
                                                "state": "point-to-point,",
                                                "transit_area_id": "0.0.0.1",
                                                "transmit_delay": 7,
                                                "wait_interval": 13,
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

    golden_output1 = {
        "execute.return_value": """
        RP/0/0/CPU0:R3_ospf_xr#show ospf vrf all-inclusive sham-links

        Sham Links for OSPF 1, VRF VRF1

        Sham Link OSPF_SL0 to address 10.151.22.22 is up
        Area 1, source address 10.21.33.33
        IfIndex = 2
          Run as demand circuit
          DoNotAge LSA not allowed (Number of DCbitless LSA is 1)., Cost of using 111
          Transmit Delay is 7 sec, State POINT_TO_POINT,
          Timer intervals configured, Hello 3, Dead 13, Wait 13, Retransmit 5
            Hello due in 00:00:00:772
        """
    }

    def test_show_ospf_vrf_all_inclusive_sham_links_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveShamLinks(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_sham_links_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveShamLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==========================================================
#  Unit test for 'show ospf vrf all-inclusive virtual-links'
# ==========================================================
class test_show_ospf_vrf_all_inclusive_virtual_links(unittest.TestCase):

    """Unit test for "show ospf vrf all-inclusive virtual-links" """

    device = Device(name="aDevice")
    empty_output = {"execute.return_value": ""}

    golden_parsed_output1 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "1": {
                                "areas": {
                                    "0.0.0.1": {
                                        "virtual_links": {
                                            "0.0.0.1 10.16.2.2": {
                                                "authentication": {
                                                    "auth_trailer_key": {
                                                        "crypto_algorithm": "simple"
                                                    }
                                                },
                                                "cost": 65535,
                                                "dcbitless_lsa_count": 1,
                                                "donotage_lsa": "not allowed",
                                                "dead_interval": 16,
                                                "demand_circuit": True,
                                                "hello_interval": 4,
                                                "hello_timer": "00:00:03:179",
                                                "interface": "GigabitEthernet0/0/0/3",
                                                "name": "VL0",
                                                "link_state": "up",
                                                "nsf": {
                                                    "enable": True,
                                                    "last_restart": "00:18:16",
                                                },
                                                "retransmit_interval": 44,
                                                "router_id": "10.16.2.2",
                                                "state": "point-to-point,",
                                                "transit_area_id": "0.0.0.1",
                                                "transmit_delay": 5,
                                                "wait_interval": 16,
                                            },
                                            "0.0.0.1 10.100.5.5": {
                                                "authentication": {
                                                    "auth_trailer_key": {
                                                        "crypto_algorithm": "md5",
                                                        "youngest_key_id": 1,
                                                    }
                                                },
                                                "cost": 65535,
                                                "dcbitless_lsa_count": 1,
                                                "donotage_lsa": "not allowed",
                                                "dead_interval": 16,
                                                "demand_circuit": True,
                                                "hello_interval": 4,
                                                "hello_timer": "00:00:03:179",
                                                "interface": "GigabitEthernet0/0/0/4",
                                                "name": "VL1",
                                                "link_state": "up",
                                                "nsf": {
                                                    "enable": True,
                                                    "last_restart": "00:18:16",
                                                },
                                                "retransmit_interval": 44,
                                                "router_id": "10.100.5.5",
                                                "state": "point-to-point,",
                                                "transit_area_id": "0.0.0.1",
                                                "transmit_delay": 5,
                                                "wait_interval": 16,
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
    }

    golden_output1 = {
        "execute.return_value": """
        RP/0/0/CPU0:R2_ospf_xr#show ospf vrf all-inclusive virtual-links
        Fri Nov  3 01:25:44.845 UTC

        Virtual Links for OSPF 1

        Virtual Link OSPF_VL0 to router 10.16.2.2 is up

          DoNotAge LSA not allowed Run as demand circuit (Number of DCbitless LSA is 1).
          Transit area 1, via interface GigabitEthernet0/0/0/3, Cost of using 65535
          Transmit Delay is 5 sec, State POINT_TO_POINT,
          Non-Stop Forwarding (NSF) enabled, last NSF restart 00:18:16 ago
          Timer intervals configured, Hello 4, Dead 16, Wait 16, Retransmit 44
            Hello due in 00:00:03:179
          Clear text authentication enabled

        Virtual Link OSPF_VL1 to router 10.100.5.5 is up

          DoNotAge LSA not allowed Run as demand circuit (Number of DCbitless LSA is 1).
          Transit area 1, via interface GigabitEthernet0/0/0/4, Cost of using 65535
          Transmit Delay is 5 sec, State POINT_TO_POINT,
          Non-Stop Forwarding (NSF) enabled, last NSF restart 00:18:16 ago
          Timer intervals configured, Hello 4, Dead 16, Wait 16, Retransmit 44
            Hello due in 00:00:03:179
          Message digest authentication enabled
          Youngest key id is 1
        """
    }

    def test_show_ospf_vrf_all_inclusive_virtual_links_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveVirtualLinks(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_virtual_links_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveVirtualLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ================================================
#  Unit test for 'show ospf mpls traffic-eng link'
# ================================================
class test_show_ospf_mpls_traffic_eng_link(unittest.TestCase):

    """Unit test for "show ospf vrf all-inclusive traffic-eng link" """

    device = Device(name="aDevice")
    empty_output = {"execute.return_value": ""}

    golden_parsed_output1 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "1": {
                                "areas": {
                                    "0.0.0.0": {
                                        "mpls": {
                                            "te": {
                                                "area_instance": 2,
                                                "enable": True,
                                                "link_fragments": {
                                                    1: {
                                                        "affinity_bit": "0",
                                                        "extended_admin_groups": {
                                                            0: {"value": 0},
                                                            1: {"value": 0},
                                                            2: {"value": 0},
                                                            3: {"value": 0},
                                                            4: {"value": 0},
                                                            5: {"value": 0},
                                                            6: {"value": 0},
                                                            7: {"value": 0},
                                                        },
                                                        "interface_address": "10.3.4.3",
                                                        "link_id": "10.3.4.4",
                                                        "link_instance": 2,
                                                        "maximum_bandwidth": 125000000,
                                                        "maximum_reservable_bandwidth": 93750000,
                                                        "network_type": "broadcast",
                                                        "out_interface_id": 4,
                                                        "te_admin_metric": 1,
                                                        "total_extended_admin_group": 8,
                                                        "total_priority": 8,
                                                        "unreserved_bandwidths": {
                                                            "0 93750000": {
                                                                "priority": 0,
                                                                "unreserved_bandwidth": 93750000,
                                                            },
                                                            "1 93750000": {
                                                                "priority": 1,
                                                                "unreserved_bandwidth": 93750000,
                                                            },
                                                            "2 93750000": {
                                                                "priority": 2,
                                                                "unreserved_bandwidth": 93750000,
                                                            },
                                                            "3 93750000": {
                                                                "priority": 3,
                                                                "unreserved_bandwidth": 93750000,
                                                            },
                                                            "4 93750000": {
                                                                "priority": 4,
                                                                "unreserved_bandwidth": 93750000,
                                                            },
                                                            "5 93750000": {
                                                                "priority": 5,
                                                                "unreserved_bandwidth": 93750000,
                                                            },
                                                            "6 93750000": {
                                                                "priority": 6,
                                                                "unreserved_bandwidth": 93750000,
                                                            },
                                                            "7 93750000": {
                                                                "priority": 7,
                                                                "unreserved_bandwidth": 93750000,
                                                            },
                                                        },
                                                    },
                                                    2: {
                                                        "affinity_bit": "0",
                                                        "extended_admin_groups": {
                                                            0: {"value": 0},
                                                            1: {"value": 0},
                                                            2: {"value": 0},
                                                            3: {"value": 0},
                                                            4: {"value": 0},
                                                            5: {"value": 0},
                                                            6: {"value": 0},
                                                            7: {"value": 0},
                                                        },
                                                        "interface_address": "10.2.3.3",
                                                        "link_id": "10.2.3.3",
                                                        "link_instance": 2,
                                                        "maximum_bandwidth": 125000000,
                                                        "maximum_reservable_bandwidth": 93750000,
                                                        "network_type": "broadcast",
                                                        "out_interface_id": 6,
                                                        "te_admin_metric": 1,
                                                        "total_extended_admin_group": 8,
                                                        "total_priority": 8,
                                                        "unreserved_bandwidths": {
                                                            "0 93750000": {
                                                                "priority": 0,
                                                                "unreserved_bandwidth": 93750000,
                                                            },
                                                            "1 93750000": {
                                                                "priority": 1,
                                                                "unreserved_bandwidth": 93750000,
                                                            },
                                                            "2 93750000": {
                                                                "priority": 2,
                                                                "unreserved_bandwidth": 93750000,
                                                            },
                                                            "3 93750000": {
                                                                "priority": 3,
                                                                "unreserved_bandwidth": 93750000,
                                                            },
                                                            "4 93750000": {
                                                                "priority": 4,
                                                                "unreserved_bandwidth": 93750000,
                                                            },
                                                            "5 93750000": {
                                                                "priority": 5,
                                                                "unreserved_bandwidth": 93750000,
                                                            },
                                                            "6 93750000": {
                                                                "priority": 6,
                                                                "unreserved_bandwidth": 93750000,
                                                            },
                                                            "7 93750000": {
                                                                "priority": 7,
                                                                "unreserved_bandwidth": 93750000,
                                                            },
                                                        },
                                                    },
                                                },
                                                "total_links": 2,
                                            }
                                        }
                                    },
                                    "0.0.0.1": {"mpls": {"te": {"enable": False}}},
                                },
                                "mpls": {"te": {"router_id": "10.36.3.3"}},
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output1 = {
        "execute.return_value": """
        RP/0/0/CPU0:R3_ospf_xr#show ospf mpls traffic-eng link
        Thu Nov  2 21:15:42.880 UTC

                OSPF Router with ID (10.36.3.3) (Process ID 1)

      Area 0 has 2 MPLS TE links. Area instance is 2.
        Link is associated with fragment 1. Link instance is 2
          Link connected to Broadcast network
          Link ID : 10.3.4.4
          Interface Address : 10.3.4.3
          Admin Metric : TE: 1
          (all bandwidths in bytes/sec)
          Maximum bandwidth : 125000000
          Maximum global pool reservable bandwidth : 93750000
          Number of Priority : 8
          Global pool unreserved BW
          Priority 0 :             93750000  Priority 1 :             93750000
          Priority 2 :             93750000  Priority 3 :             93750000
          Priority 4 :             93750000  Priority 5 :             93750000
          Priority 6 :             93750000  Priority 7 :             93750000
          Out Interface ID : 4
          Affinity Bit : 0
          Extended Admin Group : 8
           EAG[0]: 0
           EAG[1]: 0
           EAG[2]: 0
           EAG[3]: 0
           EAG[4]: 0
           EAG[5]: 0
           EAG[6]: 0
           EAG[7]: 0

        Link is associated with fragment 2. Link instance is 2
          Link connected to Broadcast network
          Link ID : 10.2.3.3
          Interface Address : 10.2.3.3
          Admin Metric : TE: 1
          (all bandwidths in bytes/sec)
          Maximum bandwidth : 125000000
          Maximum global pool reservable bandwidth : 93750000
          Number of Priority : 8
          Global pool unreserved BW
          Priority 0 :             93750000  Priority 1 :             93750000
          Priority 2 :             93750000  Priority 3 :             93750000
          Priority 4 :             93750000  Priority 5 :             93750000
          Priority 6 :             93750000  Priority 7 :             93750000
          Out Interface ID : 6
          Affinity Bit : 0
          Extended Admin Group : 8
           EAG[0]: 0
           EAG[1]: 0
           EAG[2]: 0
           EAG[3]: 0
           EAG[4]: 0
           EAG[5]: 0
           EAG[6]: 0
           EAG[7]: 0

      Area 1 MPLS TE not initialized
        """
    }

    device_output = {
        "execute.return_value": """
                  OSPF Router with ID (10.154.219.96) (Process ID 64577)

    Area 0 has 9 MPLS TE links. Area instance is 13.
      Link is associated with fragment 1. Link instance is 13
        Link connected to Point-to-Point network
        Link ID : 10.154.219.75
        Interface Address : 172.16.1.216
        Neighbor Address : 172.16.1.217
        Admin Metric : TE: 65535
        (all bandwidths in bytes/sec)
        Maximum bandwidth : 1250000000
        Maximum global pool reservable bandwidth : 2985974784
        Maximum sub pool reservable bandwidth    : 1492987392
        Number of Priority : 8
        Global pool unreserved BW
        Priority 0 :           2985974784  Priority 1 :           2985974784
        Priority 2 :           2985974784  Priority 3 :           2985974784
        Priority 4 :           2985974784  Priority 5 :           2985974784
        Priority 6 :           2985974784  Priority 7 :           2985974784
        Sub pool unreserved BW
        Priority 0 :           1492987392  Priority 1 :           1492987392
        Priority 2 :           1492987392  Priority 3 :           1492987392
        Priority 4 :           1492987392  Priority 5 :           1492987392
        Priority 6 :           1492987392  Priority 7 :           1492987392
        Out Interface ID : 40
        Affinity Bit : 0x100000
        Extended Admin Group : 8
         EAG[0]: 0x100000
         EAG[1]: 0
         EAG[2]: 0
         EAG[3]: 0
         EAG[4]: 0
         EAG[5]: 0
         EAG[6]: 0
         EAG[7]: 0

      """
    }

    device_parsed_output = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "64577": {
                                "areas": {
                                    "0.0.0.0": {
                                        "mpls": {
                                            "te": {
                                                "area_instance": 13,
                                                "enable": True,
                                                "link_fragments": {
                                                    1: {
                                                        "affinity_bit": "0x100000",
                                                        "extended_admin_groups": {
                                                            1: {"value": 0,},
                                                            2: {"value": 0,},
                                                            3: {"value": 0,},
                                                            4: {"value": 0,},
                                                            5: {"value": 0,},
                                                            6: {"value": 0,},
                                                            7: {"value": 0,},
                                                        },
                                                        "interface_address": "172.16.1.216",
                                                        "link_id": "10.154.219.75",
                                                        "link_instance": 13,
                                                        "maximum_bandwidth": 1250000000,
                                                        "maximum_reservable_bandwidth": 2985974784,
                                                        "network_type": "point-to-point",
                                                        "out_interface_id": 40,
                                                        "te_admin_metric": 65535,
                                                        "total_extended_admin_group": 8,
                                                        "total_priority": 8,
                                                        "unreserved_bandwidths": {
                                                            "0 1492987392": {
                                                                "priority": 0,
                                                                "unreserved_bandwidth": 1492987392,
                                                            },
                                                            "0 2985974784": {
                                                                "priority": 0,
                                                                "unreserved_bandwidth": 2985974784,
                                                            },
                                                            "1 1492987392": {
                                                                "priority": 1,
                                                                "unreserved_bandwidth": 1492987392,
                                                            },
                                                            "1 2985974784": {
                                                                "priority": 1,
                                                                "unreserved_bandwidth": 2985974784,
                                                            },
                                                            "2 1492987392": {
                                                                "priority": 2,
                                                                "unreserved_bandwidth": 1492987392,
                                                            },
                                                            "2 2985974784": {
                                                                "priority": 2,
                                                                "unreserved_bandwidth": 2985974784,
                                                            },
                                                            "3 1492987392": {
                                                                "priority": 3,
                                                                "unreserved_bandwidth": 1492987392,
                                                            },
                                                            "3 2985974784": {
                                                                "priority": 3,
                                                                "unreserved_bandwidth": 2985974784,
                                                            },
                                                            "4 1492987392": {
                                                                "priority": 4,
                                                                "unreserved_bandwidth": 1492987392,
                                                            },
                                                            "4 2985974784": {
                                                                "priority": 4,
                                                                "unreserved_bandwidth": 2985974784,
                                                            },
                                                            "5 1492987392": {
                                                                "priority": 5,
                                                                "unreserved_bandwidth": 1492987392,
                                                            },
                                                            "5 2985974784": {
                                                                "priority": 5,
                                                                "unreserved_bandwidth": 2985974784,
                                                            },
                                                            "6 1492987392": {
                                                                "priority": 6,
                                                                "unreserved_bandwidth": 1492987392,
                                                            },
                                                            "6 2985974784": {
                                                                "priority": 6,
                                                                "unreserved_bandwidth": 2985974784,
                                                            },
                                                            "7 1492987392": {
                                                                "priority": 7,
                                                                "unreserved_bandwidth": 1492987392,
                                                            },
                                                            "7 2985974784": {
                                                                "priority": 7,
                                                                "unreserved_bandwidth": 2985974784,
                                                            },
                                                        },
                                                    },
                                                },
                                                "total_links": 9,
                                            },
                                        },
                                    },
                                },
                                "mpls": {"te": {"router_id": "10.154.219.96",},},
                            },
                        },
                    },
                },
            },
        },
    }

    def test_show_ospf_mpls_traffic_eng_link_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfMplsTrafficEngLink(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_mpls_traffic_eng_link_full_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output)
        obj = ShowOspfMplsTrafficEngLink(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.device_parsed_output)

    def test_show_ospf_mpls_traffic_eng_link_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfMplsTrafficEngLink(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ============================================================
#  Unit test for 'show ospf vrf all-inclusive database router'
# ============================================================
class test_show_ospf_vrf_all_inclusive_database_router(unittest.TestCase):

    """Unit test for "show ospf vrf all-inclusive database router" """

    device = Device(name="aDevice")
    empty_output = {"execute.return_value": ""}

    golden_parsed_output1 = {
        "vrf": {
            "VRF1": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "mpls1": {
                                "areas": {
                                    "0.0.0.1": {
                                        "database": {
                                            "lsa_types": {
                                                1: {
                                                    "lsa_type": 1,
                                                    "lsas": {
                                                        "10.229.11.11 10.229.11.11": {
                                                            "adv_router": "10.229.11.11",
                                                            "lsa_id": "10.229.11.11",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "router": {
                                                                        "links": {
                                                                            "10.186.5.1": {
                                                                                "link_data": "10.186.5.1",
                                                                                "link_id": "10.186.5.1",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            },
                                                                            "10.151.22.22": {
                                                                                "link_data": "0.0.0.14",
                                                                                "link_id": "10.151.22.22",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 111,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "another router (point-to-point)",
                                                                            },
                                                                        },
                                                                        "num_of_links": 2,
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.229.11.11",
                                                                    "age": 1713,
                                                                    "area_border_router": True,
                                                                    "as_boundary_router": True,
                                                                    "checksum": "0x9ce3",
                                                                    "length": 48,
                                                                    "lsa_id": "10.229.11.11",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "8000003e",
                                                                    "type": 1,
                                                                },
                                                            },
                                                        },
                                                        "10.151.22.22 10.151.22.22": {
                                                            "adv_router": "10.151.22.22",
                                                            "lsa_id": "10.151.22.22",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "router": {
                                                                        "links": {
                                                                            "10.229.11.11": {
                                                                                "link_data": "0.0.0.6",
                                                                                "link_id": "10.229.11.11",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "another router (point-to-point)",
                                                                            },
                                                                            "10.229.6.6": {
                                                                                "link_data": "10.229.6.2",
                                                                                "link_id": "10.229.6.6",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 40,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            },
                                                                        },
                                                                        "num_of_links": 2,
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.151.22.22",
                                                                    "age": 1539,
                                                                    "area_border_router": True,
                                                                    "as_boundary_router": True,
                                                                    "checksum": "0xc41a",
                                                                    "length": 48,
                                                                    "lsa_id": "10.151.22.22",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "No "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "80000019",
                                                                    "type": 1,
                                                                },
                                                            },
                                                        },
                                                        "10.36.3.3 10.36.3.3": {
                                                            "adv_router": "10.36.3.3",
                                                            "lsa_id": "10.36.3.3",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "router": {
                                                                        "links": {
                                                                            "10.19.7.7": {
                                                                                "link_data": "10.19.7.3",
                                                                                "link_id": "10.19.7.7",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            }
                                                                        },
                                                                        "num_of_links": 1,
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.36.3.3",
                                                                    "age": 217,
                                                                    "area_border_router": True,
                                                                    "as_boundary_router": True,
                                                                    "checksum": "0x5646",
                                                                    "length": 36,
                                                                    "lsa_id": "10.36.3.3",
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "seq_num": "80000036",
                                                                    "type": 1,
                                                                },
                                                            },
                                                        },
                                                        "10.115.55.55 10.115.55.55": {
                                                            "adv_router": "10.115.55.55",
                                                            "lsa_id": "10.115.55.55",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "router": {
                                                                        "links": {
                                                                            "10.186.5.1": {
                                                                                "link_data": "10.186.5.5",
                                                                                "link_id": "10.186.5.1",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            },
                                                                            "10.115.6.6": {
                                                                                "link_data": "10.115.6.5",
                                                                                "link_id": "10.115.6.6",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 30,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            },
                                                                            "10.115.55.55": {
                                                                                "link_data": "255.255.255.255",
                                                                                "link_id": "10.115.55.55",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "stub network",
                                                                            },
                                                                        },
                                                                        "num_of_links": 3,
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.115.55.55",
                                                                    "age": 1378,
                                                                    "checksum": "0xe7bc",
                                                                    "length": 60,
                                                                    "lsa_id": "10.115.55.55",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "80000037",
                                                                    "type": 1,
                                                                },
                                                            },
                                                        },
                                                        "10.84.66.66 10.84.66.66": {
                                                            "adv_router": "10.84.66.66",
                                                            "lsa_id": "10.84.66.66",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "router": {
                                                                        "links": {
                                                                            "10.229.6.6": {
                                                                                "link_data": "10.229.6.6",
                                                                                "link_id": "10.229.6.6",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            },
                                                                            "10.115.6.6": {
                                                                                "link_data": "10.115.6.6",
                                                                                "link_id": "10.115.6.6",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 30,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            },
                                                                            "10.166.7.6": {
                                                                                "link_data": "10.166.7.6",
                                                                                "link_id": "10.166.7.6",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 30,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            },
                                                                            "10.84.66.66": {
                                                                                "link_data": "255.255.255.255",
                                                                                "link_id": "10.84.66.66",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "stub "
                                                                                "network",
                                                                            },
                                                                        },
                                                                        "num_of_links": 4,
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.84.66.66",
                                                                    "age": 1578,
                                                                    "checksum": "0x1282",
                                                                    "length": 72,
                                                                    "lsa_id": "10.84.66.66",
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "8000003c",
                                                                    "type": 1,
                                                                },
                                                            },
                                                        },
                                                        "10.1.77.77 10.1.77.77": {
                                                            "adv_router": "10.1.77.77",
                                                            "lsa_id": "10.1.77.77",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "router": {
                                                                        "links": {
                                                                            "10.19.7.7": {
                                                                                "link_data": "10.19.7.7",
                                                                                "link_id": "10.19.7.7",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            },
                                                                            "10.166.7.6": {
                                                                                "link_data": "10.166.7.7",
                                                                                "link_id": "10.166.7.6",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 30,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit "
                                                                                "network",
                                                                            },
                                                                            "10.1.77.77": {
                                                                                "link_data": "255.255.255.255",
                                                                                "link_id": "10.1.77.77",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "stub network",
                                                                            },
                                                                        },
                                                                        "num_of_links": 3,
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.1.77.77",
                                                                    "age": 1344,
                                                                    "checksum": "0x1379",
                                                                    "length": 60,
                                                                    "lsa_id": "10.1.77.77",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "80000030",
                                                                    "type": 1,
                                                                },
                                                            },
                                                        },
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
            },
            "default": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "mpls1": {
                                "areas": {
                                    "0.0.0.0": {
                                        "database": {
                                            "lsa_types": {
                                                1: {
                                                    "lsa_type": 1,
                                                    "lsas": {
                                                        "10.4.1.1 10.4.1.1": {
                                                            "adv_router": "10.4.1.1",
                                                            "lsa_id": "10.4.1.1",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "router": {
                                                                        "links": {
                                                                            "10.4.1.1": {
                                                                                "link_data": "255.255.255.255",
                                                                                "link_id": "10.4.1.1",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "stub network",
                                                                            },
                                                                            "10.1.2.1": {
                                                                                "link_data": "10.1.2.1",
                                                                                "link_id": "10.1.2.1",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            },
                                                                            "10.1.4.4": {
                                                                                "link_data": "10.1.4.1",
                                                                                "link_id": "10.1.4.4",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            },
                                                                        },
                                                                        "num_of_links": 3,
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.4.1.1",
                                                                    "age": 1802,
                                                                    "checksum": "0x6228",
                                                                    "length": 60,
                                                                    "lsa_id": "10.4.1.1",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "8000003d",
                                                                    "type": 1,
                                                                },
                                                            },
                                                        },
                                                        "10.16.2.2 10.16.2.2": {
                                                            "adv_router": "10.16.2.2",
                                                            "lsa_id": "10.16.2.2",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "router": {
                                                                        "links": {
                                                                            "10.1.2.1": {
                                                                                "link_data": "10.1.2.2",
                                                                                "link_id": "10.1.2.1",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            },
                                                                            "10.2.3.3": {
                                                                                "link_data": "10.2.3.2",
                                                                                "link_id": "10.2.3.3",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            },
                                                                            "10.2.4.4": {
                                                                                "link_data": "10.2.4.2",
                                                                                "link_id": "10.2.4.4",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            },
                                                                            "10.16.2.2": {
                                                                                "link_data": "255.255.255.255",
                                                                                "link_id": "10.16.2.2",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "stub network",
                                                                            },
                                                                        },
                                                                        "num_of_links": 4,
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.16.2.2",
                                                                    "age": 756,
                                                                    "checksum": "0x652b",
                                                                    "length": 72,
                                                                    "lsa_id": "10.16.2.2",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "No "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "80000014",
                                                                    "type": 1,
                                                                },
                                                            },
                                                        },
                                                        "10.36.3.3 10.36.3.3": {
                                                            "adv_router": "10.36.3.3",
                                                            "lsa_id": "10.36.3.3",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "router": {
                                                                        "links": {
                                                                            "10.2.3.3": {
                                                                                "link_data": "10.2.3.3",
                                                                                "link_id": "10.2.3.3",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            },
                                                                            "10.3.4.4": {
                                                                                "link_data": "10.3.4.3",
                                                                                "link_id": "10.3.4.4",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            },
                                                                            "10.36.3.3": {
                                                                                "link_data": "255.255.255.255",
                                                                                "link_id": "10.36.3.3",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "stub network",
                                                                            },
                                                                        },
                                                                        "num_of_links": 3,
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.36.3.3",
                                                                    "age": 1291,
                                                                    "checksum": "0x75f8",
                                                                    "length": 60,
                                                                    "lsa_id": "10.36.3.3",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "seq_num": "80000033",
                                                                    "type": 1,
                                                                },
                                                            },
                                                        },
                                                        "10.64.4.4 10.64.4.4": {
                                                            "adv_router": "10.64.4.4",
                                                            "lsa_id": "10.64.4.4",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "router": {
                                                                        "links": {
                                                                            "10.1.4.4": {
                                                                                "link_data": "10.1.4.4",
                                                                                "link_id": "10.1.4.4",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            },
                                                                            "10.2.4.4": {
                                                                                "link_data": "10.2.4.4",
                                                                                "link_id": "10.2.4.4",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            },
                                                                            "10.3.4.4": {
                                                                                "link_data": "10.3.4.4",
                                                                                "link_id": "10.3.4.4",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "transit network",
                                                                            },
                                                                            "10.64.4.4": {
                                                                                "link_data": "255.255.255.255",
                                                                                "link_id": "10.64.4.4",
                                                                                "num_tos_metrics": 0,
                                                                                "topologies": {
                                                                                    0: {
                                                                                        "metric": 1,
                                                                                        "mt_id": 0,
                                                                                        "tos": 0,
                                                                                    }
                                                                                },
                                                                                "type": "stub network",
                                                                            },
                                                                        },
                                                                        "num_of_links": 4,
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.64.4.4",
                                                                    "age": 505,
                                                                    "as_boundary_router": True,
                                                                    "checksum": "0xa37d",
                                                                    "length": 72,
                                                                    "lsa_id": "10.64.4.4",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "80000037",
                                                                    "type": 1,
                                                                },
                                                            },
                                                        },
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
            },
        }
    }

    golden_output1 = {
        "execute.return_value": """
        RP/0/0/CPU0:R3_ospf_xr#show ospf vrf all-inclusive database router
        Thu Nov  2 21:25:10.231 UTC

                    OSPF Router with ID (10.36.3.3) (Process ID mpls1)

                        Router Link States (Area 0)

          Routing Bit Set on this LSA
          LS age: 1802
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.4.1.1
          Advertising Router: 10.4.1.1
          LS Seq Number: 8000003d
          Checksum: 0x6228
          Length: 60
           Number of Links: 3

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 10.4.1.1
             (Link Data) Network Mask: 255.255.255.255
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.1.2.1
             (Link Data) Router Interface address: 10.1.2.1
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.1.4.4
             (Link Data) Router Interface address: 10.1.4.1
              Number of TOS metrics: 0
               TOS 0 Metrics: 1


          Routing Bit Set on this LSA
          LS age: 756
          Options: (No TOS-capability, No DC)
          LS Type: Router Links
          Link State ID: 10.16.2.2
          Advertising Router: 10.16.2.2
          LS Seq Number: 80000014
          Checksum: 0x652b
          Length: 72
           Number of Links: 4

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 10.16.2.2
             (Link Data) Network Mask: 255.255.255.255
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.2.3.3
             (Link Data) Router Interface address: 10.2.3.2
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.2.4.4
             (Link Data) Router Interface address: 10.2.4.2
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.1.2.1
             (Link Data) Router Interface address: 10.1.2.2
              Number of TOS metrics: 0
               TOS 0 Metrics: 1


          LS age: 1291
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.36.3.3
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000033
          Checksum: 0x75f8
          Length: 60
           Number of Links: 3

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 10.36.3.3
             (Link Data) Network Mask: 255.255.255.255
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.3.4.4
             (Link Data) Router Interface address: 10.3.4.3
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.2.3.3
             (Link Data) Router Interface address: 10.2.3.3
              Number of TOS metrics: 0
               TOS 0 Metrics: 1


          Routing Bit Set on this LSA
          LS age: 505
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.64.4.4
          Advertising Router: 10.64.4.4
          LS Seq Number: 80000037
          Checksum: 0xa37d
          Length: 72
          AS Boundary Router
           Number of Links: 4

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 10.64.4.4
             (Link Data) Network Mask: 255.255.255.255
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.2.4.4
             (Link Data) Router Interface address: 10.2.4.4
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.3.4.4
             (Link Data) Router Interface address: 10.3.4.4
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.1.4.4
             (Link Data) Router Interface address: 10.1.4.4
              Number of TOS metrics: 0
               TOS 0 Metrics: 1


                    OSPF Router with ID (10.36.3.3) (Process ID mpls1, VRF VRF1)

                        Router Link States (Area 1)

          LS age: 217
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.36.3.3
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000036
          Checksum: 0x5646
          Length: 36
          Area Border Router
          AS Boundary Router
           Number of Links: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.19.7.7
             (Link Data) Router Interface address: 10.19.7.3
              Number of TOS metrics: 0
               TOS 0 Metrics: 1


          Routing Bit Set on this LSA
          LS age: 1713
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.229.11.11
          Advertising Router: 10.229.11.11
          LS Seq Number: 8000003e
          Checksum: 0x9ce3
          Length: 48
          Area Border Router
          AS Boundary Router
           Number of Links: 2

            Link connected to: another Router (point-to-point)
             (Link ID) Neighboring Router ID: 10.151.22.22
             (Link Data) Router Interface address: 0.0.0.14
              Number of TOS metrics: 0
               TOS 0 Metrics: 111

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.186.5.1
             (Link Data) Router Interface address: 10.186.5.1
              Number of TOS metrics: 0
               TOS 0 Metrics: 1


          Routing Bit Set on this LSA
          LS age: 1539
          Options: (No TOS-capability, No DC)
          LS Type: Router Links
          Link State ID: 10.151.22.22
          Advertising Router: 10.151.22.22
          LS Seq Number: 80000019
          Checksum: 0xc41a
          Length: 48
          Area Border Router
          AS Boundary Router
           Number of Links: 2

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.229.6.6
             (Link Data) Router Interface address: 10.229.6.2
              Number of TOS metrics: 0
               TOS 0 Metrics: 40

            Link connected to: another Router (point-to-point)
             (Link ID) Neighboring Router ID: 10.229.11.11
             (Link Data) Router Interface address: 0.0.0.6
              Number of TOS metrics: 0
               TOS 0 Metrics: 1


          Routing Bit Set on this LSA
          LS age: 1378
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.115.55.55
          Advertising Router: 10.115.55.55
          LS Seq Number: 80000037
          Checksum: 0xe7bc
          Length: 60
           Number of Links: 3

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 10.115.55.55
             (Link Data) Network Mask: 255.255.255.255
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.115.6.6
             (Link Data) Router Interface address: 10.115.6.5
              Number of TOS metrics: 0
               TOS 0 Metrics: 30

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.186.5.1
             (Link Data) Router Interface address: 10.186.5.5
              Number of TOS metrics: 0
               TOS 0 Metrics: 1


          Routing Bit Set on this LSA
          LS age: 1578
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.84.66.66
          Advertising Router: 10.84.66.66
          LS Seq Number: 8000003c
          Checksum: 0x1282
          Length: 72
           Number of Links: 4

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 10.84.66.66
             (Link Data) Network Mask: 255.255.255.255
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.166.7.6
             (Link Data) Router Interface address: 10.166.7.6
              Number of TOS metrics: 0
               TOS 0 Metrics: 30

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.229.6.6
             (Link Data) Router Interface address: 10.229.6.6
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.115.6.6
             (Link Data) Router Interface address: 10.115.6.6
              Number of TOS metrics: 0
               TOS 0 Metrics: 30


          Routing Bit Set on this LSA
          LS age: 1344
          Options: (No TOS-capability, DC)
          LS Type: Router Links
          Link State ID: 10.1.77.77
          Advertising Router: 10.1.77.77
          LS Seq Number: 80000030
          Checksum: 0x1379
          Length: 60
           Number of Links: 3

            Link connected to: a Stub Network
             (Link ID) Network/subnet number: 10.1.77.77
             (Link Data) Network Mask: 255.255.255.255
              Number of TOS metrics: 0
               TOS 0 Metrics: 1

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.166.7.6
             (Link Data) Router Interface address: 10.166.7.7
              Number of TOS metrics: 0
               TOS 0 Metrics: 30

            Link connected to: a Transit Network
             (Link ID) Designated Router address: 10.19.7.7
             (Link Data) Router Interface address: 10.19.7.7
              Number of TOS metrics: 0
               TOS 0 Metrics: 1
        """
    }

    def test_show_ospf_vrf_all_inclusive_database_router_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveDatabaseRouter(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_database_router_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveDatabaseRouter(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==============================================================
#  Unit test for 'show ospf vrf all-inclusive database external'
# ==============================================================
class test_show_ospf_vrf_all_inclusive_database_external(unittest.TestCase):

    """Unit test for "show ospf vrf all-inclusive database external" """

    device = Device(name="aDevice")
    empty_output = {"execute.return_value": ""}

    golden_parsed_output1 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "1": {
                                "areas": {
                                    "0.0.0.0": {
                                        "database": {
                                            "lsa_types": {
                                                5: {
                                                    "lsa_type": 5,
                                                    "lsas": {
                                                        "10.94.44.44 10.64.4.4": {
                                                            "adv_router": "10.64.4.4",
                                                            "lsa_id": "10.94.44.44",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "external": {
                                                                        "network_mask": "255.255.255.255",
                                                                        "topologies": {
                                                                            0: {
                                                                                "external_route_tag": 0,
                                                                                "flags": "E",
                                                                                "forwarding_address": "0.0.0.0",
                                                                                "metric": 20,
                                                                                "mt_id": 0,
                                                                                "tos": 0,
                                                                            }
                                                                        },
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.64.4.4",
                                                                    "age": 608,
                                                                    "checksum": "0x7d61",
                                                                    "length": 36,
                                                                    "lsa_id": "10.94.44.44",
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "80000002",
                                                                    "type": 5,
                                                                },
                                                            },
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
            }
        }
    }

    golden_output1 = {
        "execute.return_value": """
        RP/0/0/CPU0:R3_ospf_xr#show ospf vrf all-inclusive database external
        Thu Nov  2 21:26:53.724 UTC


                    OSPF Router with ID (10.36.3.3) (Process ID 1)

                        Type-5 AS External Link States

          Routing Bit Set on this LSA
          LS age: 608
          Options: (No TOS-capability, DC)
          LS Type: AS External Link
          Link State ID: 10.94.44.44 (External Network Number)
          Advertising Router: 10.64.4.4
          LS Seq Number: 80000002
          Checksum: 0x7d61
          Length: 36
          Network Mask: /32
                Metric Type: 2 (Larger than any link state path)
                TOS: 0
                Metric: 20
                Forward Address: 0.0.0.0
                External Route Tag: 0
        """
    }

    def test_show_ospf_vrf_all_inclusive_database_external_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveDatabaseExternal(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_database_external_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveDatabaseExternal(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =============================================================
#  Unit test for 'show ospf vrf all-inclusive database network'
# =============================================================
class test_show_ospf_vrf_all_inclusive_database_network(unittest.TestCase):

    """Unit test for "show ospf vrf all-inclusive database network" """

    device = Device(name="aDevice")
    empty_output = {"execute.return_value": ""}

    golden_parsed_output1 = {
        "vrf": {
            "VRF1": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "1": {
                                "areas": {
                                    "0.0.0.1": {
                                        "database": {
                                            "lsa_types": {
                                                2: {
                                                    "lsa_type": 2,
                                                    "lsas": {
                                                        "10.186.5.1 10.229.11.11": {
                                                            "adv_router": "10.229.11.11",
                                                            "lsa_id": "10.186.5.1",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "network": {
                                                                        "attached_routers": {
                                                                            "10.229.11.11": {},
                                                                            "10.115.55.55": {},
                                                                        },
                                                                        "network_mask": "255.255.255.0",
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.229.11.11",
                                                                    "age": 522,
                                                                    "checksum": "0xddd9",
                                                                    "length": 32,
                                                                    "lsa_id": "10.186.5.1",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "80000033",
                                                                    "type": 2,
                                                                },
                                                            },
                                                        },
                                                        "10.229.6.6 10.84.66.66": {
                                                            "adv_router": "10.84.66.66",
                                                            "lsa_id": "10.229.6.6",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "network": {
                                                                        "attached_routers": {
                                                                            "10.151.22.22": {},
                                                                            "10.84.66.66": {},
                                                                        },
                                                                        "network_mask": "255.255.255.0",
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.84.66.66",
                                                                    "age": 146,
                                                                    "checksum": "0x3f5f",
                                                                    "length": 32,
                                                                    "lsa_id": "10.229.6.6",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "80000010",
                                                                    "type": 2,
                                                                },
                                                            },
                                                        },
                                                        "10.19.7.7 10.1.77.77": {
                                                            "adv_router": "10.1.77.77",
                                                            "lsa_id": "10.19.7.7",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "network": {
                                                                        "attached_routers": {
                                                                            "10.36.3.3": {},
                                                                            "10.1.77.77": {},
                                                                        },
                                                                        "network_mask": "255.255.255.0",
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.1.77.77",
                                                                    "age": 1903,
                                                                    "checksum": "0x5c19",
                                                                    "length": 32,
                                                                    "lsa_id": "10.19.7.7",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "8000002a",
                                                                    "type": 2,
                                                                },
                                                            },
                                                        },
                                                        "10.115.6.6 10.84.66.66": {
                                                            "adv_router": "10.84.66.66",
                                                            "lsa_id": "10.115.6.6",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "network": {
                                                                        "attached_routers": {
                                                                            "10.115.55.55": {},
                                                                            "10.84.66.66": {},
                                                                        },
                                                                        "network_mask": "255.255.255.0",
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.84.66.66",
                                                                    "age": 1620,
                                                                    "checksum": "0x619c",
                                                                    "length": 32,
                                                                    "lsa_id": "10.115.6.6",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "80000029",
                                                                    "type": 2,
                                                                },
                                                            },
                                                        },
                                                        "10.166.7.6 10.84.66.66": {
                                                            "adv_router": "10.84.66.66",
                                                            "lsa_id": "10.166.7.6",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "network": {
                                                                        "attached_routers": {
                                                                            "10.84.66.66": {},
                                                                            "10.1.77.77": {},
                                                                        },
                                                                        "network_mask": "255.255.255.0",
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.84.66.66",
                                                                    "age": 884,
                                                                    "checksum": "0x960b",
                                                                    "length": 32,
                                                                    "lsa_id": "10.166.7.6",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "8000002b",
                                                                    "type": 2,
                                                                },
                                                            },
                                                        },
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
            },
            "default": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "1": {
                                "areas": {
                                    "0.0.0.0": {
                                        "database": {
                                            "lsa_types": {
                                                2: {
                                                    "lsa_type": 2,
                                                    "lsas": {
                                                        "10.1.2.1 10.4.1.1": {
                                                            "adv_router": "10.4.1.1",
                                                            "lsa_id": "10.1.2.1",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "network": {
                                                                        "attached_routers": {
                                                                            "10.4.1.1": {},
                                                                            "10.16.2.2": {},
                                                                        },
                                                                        "network_mask": "255.255.255.0",
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.4.1.1",
                                                                    "age": 1844,
                                                                    "checksum": "0x3dd0",
                                                                    "length": 32,
                                                                    "lsa_id": "10.1.2.1",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "8000000f",
                                                                    "type": 2,
                                                                },
                                                            },
                                                        },
                                                        "10.1.4.4 10.64.4.4": {
                                                            "adv_router": "10.64.4.4",
                                                            "lsa_id": "10.1.4.4",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "network": {
                                                                        "attached_routers": {
                                                                            "10.4.1.1": {},
                                                                            "10.64.4.4": {},
                                                                        },
                                                                        "network_mask": "255.255.255.0",
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.64.4.4",
                                                                    "age": 546,
                                                                    "checksum": "0xa232",
                                                                    "length": 32,
                                                                    "lsa_id": "10.1.4.4",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "8000002f",
                                                                    "type": 2,
                                                                },
                                                            },
                                                        },
                                                        "10.2.3.3 10.36.3.3": {
                                                            "adv_router": "10.36.3.3",
                                                            "lsa_id": "10.2.3.3",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "network": {
                                                                        "attached_routers": {
                                                                            "10.16.2.2": {},
                                                                            "10.36.3.3": {},
                                                                        },
                                                                        "network_mask": "255.255.255.0",
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.36.3.3",
                                                                    "age": 1828,
                                                                    "checksum": "0x2acf",
                                                                    "length": 32,
                                                                    "lsa_id": "10.2.3.3",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "8000000f",
                                                                    "type": 2,
                                                                },
                                                            },
                                                        },
                                                        "10.2.4.4 10.64.4.4": {
                                                            "adv_router": "10.64.4.4",
                                                            "lsa_id": "10.2.4.4",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "network": {
                                                                        "attached_routers": {
                                                                            "10.16.2.2": {},
                                                                            "10.64.4.4": {},
                                                                        },
                                                                        "network_mask": "255.255.255.0",
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.64.4.4",
                                                                    "age": 1803,
                                                                    "checksum": "0x9e6",
                                                                    "length": 32,
                                                                    "lsa_id": "10.2.4.4",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "8000000f",
                                                                    "type": 2,
                                                                },
                                                            },
                                                        },
                                                        "10.3.4.4 10.64.4.4": {
                                                            "adv_router": "10.64.4.4",
                                                            "lsa_id": "10.3.4.4",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "network": {
                                                                        "attached_routers": {
                                                                            "10.36.3.3": {},
                                                                            "10.64.4.4": {},
                                                                        },
                                                                        "network_mask": "255.255.255.0",
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.64.4.4",
                                                                    "age": 52,
                                                                    "checksum": "0xeedb",
                                                                    "length": 32,
                                                                    "lsa_id": "10.3.4.4",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "8000002f",
                                                                    "type": 2,
                                                                },
                                                            },
                                                        },
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
            },
        }
    }

    golden_output1 = {
        "execute.return_value": """
        P/0/0/CPU0:R3_ospf_xr#show ospf vrf all-inclusive database network
        Thu Nov  2 21:25:51.748 UTC

                    OSPF Router with ID (10.36.3.3) (Process ID 1)

                        Net Link States (Area 0)

          Routing Bit Set on this LSA
          LS age: 1844
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.1.2.1 (address of Designated Router)
          Advertising Router: 10.4.1.1
          LS Seq Number: 8000000f
          Checksum: 0x3dd0
          Length: 32
          Network Mask: /24
                Attached Router: 10.4.1.1
                Attached Router: 10.16.2.2

          Routing Bit Set on this LSA
          LS age: 546
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.1.4.4 (address of Designated Router)
          Advertising Router: 10.64.4.4
          LS Seq Number: 8000002f
          Checksum: 0xa232
          Length: 32
          Network Mask: /24
                Attached Router: 10.64.4.4
                Attached Router: 10.4.1.1

          Routing Bit Set on this LSA
          LS age: 1828
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.2.3.3 (address of Designated Router)
          Advertising Router: 10.36.3.3
          LS Seq Number: 8000000f
          Checksum: 0x2acf
          Length: 32
          Network Mask: /24
                Attached Router: 10.16.2.2
                Attached Router: 10.36.3.3

          Routing Bit Set on this LSA
          LS age: 1803
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.2.4.4 (address of Designated Router)
          Advertising Router: 10.64.4.4
          LS Seq Number: 8000000f
          Checksum: 0x9e6
          Length: 32
          Network Mask: /24
                Attached Router: 10.64.4.4
                Attached Router: 10.16.2.2

          Routing Bit Set on this LSA
          LS age: 52
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.3.4.4 (address of Designated Router)
          Advertising Router: 10.64.4.4
          LS Seq Number: 8000002f
          Checksum: 0xeedb
          Length: 32
          Network Mask: /24
                Attached Router: 10.64.4.4
                Attached Router: 10.36.3.3


                    OSPF Router with ID (10.36.3.3) (Process ID 1, VRF VRF1)

                        Net Link States (Area 1)

          Routing Bit Set on this LSA
          LS age: 522
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.186.5.1 (address of Designated Router)
          Advertising Router: 10.229.11.11
          LS Seq Number: 80000033
          Checksum: 0xddd9
          Length: 32
          Network Mask: /24
                Attached Router: 10.229.11.11
                Attached Router: 10.115.55.55

          Routing Bit Set on this LSA
          LS age: 146
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.229.6.6 (address of Designated Router)
          Advertising Router: 10.84.66.66
          LS Seq Number: 80000010
          Checksum: 0x3f5f
          Length: 32
          Network Mask: /24
                Attached Router: 10.84.66.66
                Attached Router: 10.151.22.22

          Routing Bit Set on this LSA
          LS age: 1903
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.19.7.7 (address of Designated Router)
          Advertising Router: 10.1.77.77
          LS Seq Number: 8000002a
          Checksum: 0x5c19
          Length: 32
          Network Mask: /24
                Attached Router: 10.1.77.77
                Attached Router: 10.36.3.3

          Routing Bit Set on this LSA
          LS age: 1620
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.115.6.6 (address of Designated Router)
          Advertising Router: 10.84.66.66
          LS Seq Number: 80000029
          Checksum: 0x619c
          Length: 32
          Network Mask: /24
                Attached Router: 10.84.66.66
                Attached Router: 10.115.55.55

          Routing Bit Set on this LSA
          LS age: 884
          Options: (No TOS-capability, DC)
          LS Type: Network Links
          Link State ID: 10.166.7.6 (address of Designated Router)
          Advertising Router: 10.84.66.66
          LS Seq Number: 8000002b
          Checksum: 0x960b
          Length: 32
          Network Mask: /24
                Attached Router: 10.84.66.66
                Attached Router: 10.1.77.77
        """
    }

    def test_show_ospf_vrf_all_inclusive_database_network_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveDatabaseNetwork(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_database_network_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveDatabaseNetwork(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =============================================================
#  Unit test for 'show ospf vrf all-inclusive database summary'
# =============================================================
class test_show_ospf_vrf_all_inclusive_database_summary(unittest.TestCase):

    """Unit test for "show ospf vrf all-inclusive database summary" """

    device = Device(name="aDevice")
    maxDiff = None
    empty_output = {"execute.return_value": ""}

    golden_parsed_output1 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "1": {
                                "areas": {
                                    "0.0.0.0": {
                                        "database": {
                                            "lsa_types": {
                                                3: {
                                                    "lsa_type": 3,
                                                    "lsas": {
                                                        "10.186.3.0 10.16.2.2": {
                                                            "adv_router": "10.16.2.2",
                                                            "lsa_id": "10.186.3.0",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "summary": {
                                                                        "network_mask": "255.255.255.0",
                                                                        "topologies": {
                                                                            0: {
                                                                                "metric": 65575,
                                                                                "mt_id": 0,
                                                                                "tos": 0,
                                                                            }
                                                                        },
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.16.2.2",
                                                                    "age": 520,
                                                                    "checksum": "0xaa4a",
                                                                    "length": 28,
                                                                    "lsa_id": "10.186.3.0",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "seq_num": "80000001",
                                                                    "type": 3,
                                                                },
                                                            },
                                                        },
                                                        "10.229.3.0 10.16.2.2": {
                                                            "adv_router": "10.16.2.2",
                                                            "lsa_id": "10.229.3.0",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "summary": {
                                                                        "network_mask": "255.255.255.0",
                                                                        "topologies": {
                                                                            0: {
                                                                                "metric": 65535,
                                                                                "mt_id": 0,
                                                                                "tos": 0,
                                                                            }
                                                                        },
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.16.2.2",
                                                                    "age": 519,
                                                                    "checksum": "0xd0e",
                                                                    "length": 28,
                                                                    "lsa_id": "10.229.3.0",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "seq_num": "80000002",
                                                                    "type": 3,
                                                                },
                                                            },
                                                        },
                                                        "10.229.4.0 10.16.2.2": {
                                                            "adv_router": "10.16.2.2",
                                                            "lsa_id": "10.229.4.0",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "summary": {
                                                                        "network_mask": "255.255.255.0",
                                                                        "topologies": {
                                                                            0: {
                                                                                "metric": 65535,
                                                                                "mt_id": 0,
                                                                                "tos": 0,
                                                                            }
                                                                        },
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.16.2.2",
                                                                    "age": 297,
                                                                    "checksum": "0x218",
                                                                    "length": 28,
                                                                    "lsa_id": "10.229.4.0",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "seq_num": "80000002",
                                                                    "type": 3,
                                                                },
                                                            },
                                                        },
                                                        "10.19.4.0 10.16.2.2": {
                                                            "adv_router": "10.16.2.2",
                                                            "lsa_id": "10.19.4.0",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "summary": {
                                                                        "network_mask": "255.255.255.0",
                                                                        "topologies": {
                                                                            0: {
                                                                                "metric": 65536,
                                                                                "mt_id": 0,
                                                                                "tos": 0,
                                                                            }
                                                                        },
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.16.2.2",
                                                                    "age": 294,
                                                                    "checksum": "0xfd1a",
                                                                    "length": 28,
                                                                    "lsa_id": "10.19.4.0",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "seq_num": "80000002",
                                                                    "type": 3,
                                                                },
                                                            },
                                                        },
                                                        "10.64.4.4 10.16.2.2": {
                                                            "adv_router": "10.16.2.2",
                                                            "lsa_id": "10.64.4.4",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "summary": {
                                                                        "network_mask": "255.255.255.255",
                                                                        "topologies": {
                                                                            0: {
                                                                                "metric": 65536,
                                                                                "mt_id": 0,
                                                                                "tos": 0,
                                                                            }
                                                                        },
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.16.2.2",
                                                                    "age": 295,
                                                                    "checksum": "0x9c87",
                                                                    "length": 28,
                                                                    "lsa_id": "10.64.4.4",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "seq_num": "80000001",
                                                                    "type": 3,
                                                                },
                                                            },
                                                        },
                                                    },
                                                }
                                            }
                                        }
                                    },
                                    "0.0.0.1": {
                                        "database": {
                                            "lsa_types": {
                                                3: {
                                                    "lsa_type": 3,
                                                    "lsas": {
                                                        "10.1.2.0 10.16.2.2": {
                                                            "adv_router": "10.16.2.2",
                                                            "lsa_id": "10.1.2.0",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "summary": {
                                                                        "network_mask": "255.255.255.0",
                                                                        "topologies": {
                                                                            0: {
                                                                                "metric": 4294,
                                                                                "mt_id": 0,
                                                                                "tos": 0,
                                                                            }
                                                                        },
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.16.2.2",
                                                                    "age": 675,
                                                                    "checksum": "0xfc54",
                                                                    "length": 28,
                                                                    "lsa_id": "10.1.2.0",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "seq_num": "80000001",
                                                                    "type": 3,
                                                                },
                                                            },
                                                        },
                                                        "10.1.2.0 10.36.3.3": {
                                                            "adv_router": "10.36.3.3",
                                                            "lsa_id": "10.1.2.0",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "summary": {
                                                                        "network_mask": "255.255.255.0",
                                                                        "topologies": {
                                                                            0: {
                                                                                "metric": 151,
                                                                                "mt_id": 0,
                                                                                "tos": 0,
                                                                            }
                                                                        },
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.36.3.3",
                                                                    "age": 521,
                                                                    "checksum": "0x5655",
                                                                    "length": 28,
                                                                    "lsa_id": "10.1.2.0",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "No "
                                                                    "DC",
                                                                    "seq_num": "80000002",
                                                                    "type": 3,
                                                                },
                                                            },
                                                        },
                                                        "10.1.3.0 10.36.3.3": {
                                                            "adv_router": "10.36.3.3",
                                                            "lsa_id": "10.1.3.0",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "summary": {
                                                                        "network_mask": "255.255.255.0",
                                                                        "topologies": {
                                                                            0: {
                                                                                "metric": 40,
                                                                                "mt_id": 0,
                                                                                "tos": 0,
                                                                            }
                                                                        },
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.36.3.3",
                                                                    "age": 531,
                                                                    "checksum": "0xf029",
                                                                    "length": 28,
                                                                    "lsa_id": "10.1.3.0",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "No "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "80000002",
                                                                    "type": 3,
                                                                },
                                                            },
                                                        },
                                                        "10.2.3.0 10.16.2.2": {
                                                            "adv_router": "10.16.2.2",
                                                            "lsa_id": "10.2.3.0",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "summary": {
                                                                        "network_mask": "255.255.255.0",
                                                                        "topologies": {
                                                                            0: {
                                                                                "metric": 222,
                                                                                "mt_id": 0,
                                                                                "tos": 0,
                                                                            }
                                                                        },
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.16.2.2",
                                                                    "age": 675,
                                                                    "checksum": "0x4601",
                                                                    "length": 28,
                                                                    "lsa_id": "10.2.3.0",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "seq_num": "80000001",
                                                                    "type": 3,
                                                                },
                                                            },
                                                        },
                                                        "10.2.3.0 10.36.3.3": {
                                                            "adv_router": "10.36.3.3",
                                                            "lsa_id": "10.2.3.0",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "summary": {
                                                                        "network_mask": "255.255.255.0",
                                                                        "topologies": {
                                                                            0: {
                                                                                "metric": 262,
                                                                                "mt_id": 0,
                                                                                "tos": 0,
                                                                            }
                                                                        },
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.36.3.3",
                                                                    "age": 287,
                                                                    "checksum": "0x96a2",
                                                                    "length": 28,
                                                                    "lsa_id": "10.2.3.0",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "No "
                                                                    "DC",
                                                                    "seq_num": "80000003",
                                                                    "type": 3,
                                                                },
                                                            },
                                                        },
                                                        "10.16.2.2 10.16.2.2": {
                                                            "adv_router": "10.16.2.2",
                                                            "lsa_id": "10.16.2.2",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "summary": {
                                                                        "network_mask": "255.255.255.255",
                                                                        "topologies": {
                                                                            0: {
                                                                                "metric": 1,
                                                                                "mt_id": 0,
                                                                                "tos": 0,
                                                                            }
                                                                        },
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.16.2.2",
                                                                    "age": 676,
                                                                    "checksum": "0xfa31",
                                                                    "length": 28,
                                                                    "lsa_id": "10.16.2.2",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "seq_num": "80000001",
                                                                    "type": 3,
                                                                },
                                                            },
                                                        },
                                                        "10.36.3.3 10.36.3.3": {
                                                            "adv_router": "10.36.3.3",
                                                            "lsa_id": "10.36.3.3",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "summary": {
                                                                        "network_mask": "255.255.255.255",
                                                                        "topologies": {
                                                                            0: {
                                                                                "metric": 1,
                                                                                "mt_id": 0,
                                                                                "tos": 0,
                                                                            }
                                                                        },
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.36.3.3",
                                                                    "age": 531,
                                                                    "checksum": "0x8eb4",
                                                                    "length": 28,
                                                                    "lsa_id": "10.36.3.3",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "No "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "80000002",
                                                                    "type": 3,
                                                                },
                                                            },
                                                        },
                                                        "10.94.44.44 10.64.4.4": {
                                                            "adv_router": "10.64.4.4",
                                                            "lsa_id": "10.94.44.44",
                                                            "ospfv2": {
                                                                "body": {
                                                                    "summary": {
                                                                        "network_mask": "255.255.255.255",
                                                                        "topologies": {
                                                                            0: {
                                                                                "metric": 1,
                                                                                "mt_id": 0,
                                                                                "tos": 0,
                                                                            }
                                                                        },
                                                                    }
                                                                },
                                                                "header": {
                                                                    "adv_router": "10.64.4.4",
                                                                    "age": 291,
                                                                    "checksum": "0x2b50",
                                                                    "length": 28,
                                                                    "lsa_id": "10.94.44.44",
                                                                    "option": "None",
                                                                    "option_desc": "No "
                                                                    "TOS-capability, "
                                                                    "DC",
                                                                    "routing_bit_enable": True,
                                                                    "seq_num": "80000001",
                                                                    "type": 3,
                                                                },
                                                            },
                                                        },
                                                    },
                                                }
                                            }
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

    golden_output1 = {
        "execute.return_value": """
        RP/0/0/CPU0:R2_ospf_xr#show ospf vrf all-inclusive database summary
        Fri Nov  3 01:24:47.719 UTC


                    OSPF Router with ID (10.16.2.2) (Process ID 1)

                        Summary Net Link States (Area 0.0.0.0)

          LS age: 295
          Options: (No TOS-capability, DC)
          LS Type: Summary Links (Network)
          Link State ID: 10.64.4.4 (Summary Network Number)
          Advertising Router: 10.16.2.2
          LS Seq Number: 80000001
          Checksum: 0x9c87
          Length: 28
          Network Mask: /32
                TOS: 0  Metric: 65536

          LS age: 520
          Options: (No TOS-capability, DC)
          LS Type: Summary Links (Network)
          Link State ID: 10.186.3.0 (Summary Network Number)
          Advertising Router: 10.16.2.2
          LS Seq Number: 80000001
          Checksum: 0xaa4a
          Length: 28
          Network Mask: /24
                TOS: 0  Metric: 65575

          LS age: 519
          Options: (No TOS-capability, DC)
          LS Type: Summary Links (Network)
          Link State ID: 10.229.3.0 (Summary Network Number)
          Advertising Router: 10.16.2.2
          LS Seq Number: 80000002
          Checksum: 0xd0e
          Length: 28
          Network Mask: /24
                TOS: 0  Metric: 65535

          LS age: 297
          Options: (No TOS-capability, DC)
          LS Type: Summary Links (Network)
          Link State ID: 10.229.4.0 (Summary Network Number)
          Advertising Router: 10.16.2.2
          LS Seq Number: 80000002
          Checksum: 0x218
          Length: 28
          Network Mask: /24
                TOS: 0  Metric: 65535

          LS age: 294
          Options: (No TOS-capability, DC)
          LS Type: Summary Links (Network)
          Link State ID: 10.19.4.0 (Summary Network Number)
          Advertising Router: 10.16.2.2
          LS Seq Number: 80000002
          Checksum: 0xfd1a
          Length: 28
          Network Mask: /24
                TOS: 0  Metric: 65536


                        Summary Net Link States (Area 1)

          LS age: 676
          Options: (No TOS-capability, DC)
          LS Type: Summary Links (Network)
          Link State ID: 10.16.2.2 (Summary Network Number)
          Advertising Router: 10.16.2.2
          LS Seq Number: 80000001
          Checksum: 0xfa31
          Length: 28
          Network Mask: /32
                TOS: 0  Metric: 1

          Routing Bit Set on this LSA
          LS age: 531
          Options: (No TOS-capability, No DC)
          LS Type: Summary Links (Network)
          Link State ID: 10.36.3.3 (Summary Network Number)
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000002
          Checksum: 0x8eb4
          Length: 28
          Network Mask: /32
                TOS: 0  Metric: 1

          LS age: 675
          Options: (No TOS-capability, DC)
          LS Type: Summary Links (Network)
          Link State ID: 10.1.2.0 (Summary Network Number)
          Advertising Router: 10.16.2.2
          LS Seq Number: 80000001
          Checksum: 0xfc54
          Length: 28
          Network Mask: /24
                TOS: 0  Metric: 4294

          LS age: 521
          Options: (No TOS-capability, No DC)
          LS Type: Summary Links (Network)
          Link State ID: 10.1.2.0 (Summary Network Number)
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000002
          Checksum: 0x5655
          Length: 28
          Network Mask: /24
                TOS: 0  Metric: 151

          Routing Bit Set on this LSA
          LS age: 531
          Options: (No TOS-capability, No DC)
          LS Type: Summary Links (Network)
          Link State ID: 10.1.3.0 (Summary Network Number)
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000002
          Checksum: 0xf029
          Length: 28
          Network Mask: /24
                TOS: 0  Metric: 40

          LS age: 675
          Options: (No TOS-capability, DC)
          LS Type: Summary Links (Network)
          Link State ID: 10.2.3.0 (Summary Network Number)
          Advertising Router: 10.16.2.2
          LS Seq Number: 80000001
          Checksum: 0x4601
          Length: 28
          Network Mask: /24
                TOS: 0  Metric: 222

          LS age: 287
          Options: (No TOS-capability, No DC)
          LS Type: Summary Links (Network)
          Link State ID: 10.2.3.0 (Summary Network Number)
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000003
          Checksum: 0x96a2
          Length: 28
          Network Mask: /24
                TOS: 0  Metric: 262

          Routing Bit Set on this LSA
          LS age: 291
          Options: (No TOS-capability, DC)
          LS Type: Summary Links (Network)
          Link State ID: 10.94.44.44 (Summary Network Number)
          Advertising Router: 10.64.4.4
          LS Seq Number: 80000001
          Checksum: 0x2b50
          Length: 28
          Network Mask: /32
                TOS: 0  Metric: 1
        """
    }

    def test_show_ospf_vrf_all_inclusive_database_summary_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveDatabaseSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_database_summary_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveDatabaseSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =================================================================
#  Unit test for 'show ospf vrf all-inclusive database opaque-area'
# =================================================================
class test_show_ospf_vrf_all_inclusive_database_opaque_area(unittest.TestCase):

    """Unit test for "show ospf vrf all-inclusive database opaque-area" """

    device = Device(name="aDevice")
    empty_output = {"execute.return_value": ""}

    golden_parsed_output1 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "1": {
                                "areas": {
                                    "0.0.0.0": {
                                        "database": {
                                            "lsa_types": {
                                                10: {
                                                    "lsa_type": 10,
                                                    "lsas": {
                                                        "10.1.0.0 10.4.1.1": {
                                                            "adv_router": "10.4.1.1",
                                                            "lsa_id": "10.1.0.0",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 1427,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.0.0",
                                                                    "adv_router": "10.4.1.1",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 0,
                                                                    "seq_num": "80000002",
                                                                    "checksum": "0x56d2",
                                                                    "length": 28,
                                                                    "mpls_te_router_id": "10.4.1.1",
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "num_of_links": 0,
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        "10.1.0.0 10.16.2.2": {
                                                            "adv_router": "10.16.2.2",
                                                            "lsa_id": "10.1.0.0",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 653,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, No DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.0.0",
                                                                    "adv_router": "10.16.2.2",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 0,
                                                                    "seq_num": "80000003",
                                                                    "checksum": "0x1c22",
                                                                    "length": 28,
                                                                    "mpls_te_router_id": "10.16.2.2",
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "num_of_links": 0,
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        "10.1.0.0 10.36.3.3": {
                                                            "adv_router": "10.36.3.3",
                                                            "lsa_id": "10.1.0.0",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 1175,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.0.0",
                                                                    "adv_router": "10.36.3.3",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 0,
                                                                    "seq_num": "80000002",
                                                                    "checksum": "0x5eba",
                                                                    "length": 28,
                                                                    "mpls_te_router_id": "10.36.3.3",
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "num_of_links": 0,
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        "10.1.0.1 10.4.1.1": {
                                                            "adv_router": "10.4.1.1",
                                                            "lsa_id": "10.1.0.1",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 1427,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.0.1",
                                                                    "adv_router": "10.4.1.1",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 1,
                                                                    "seq_num": "80000002",
                                                                    "checksum": "0x6586",
                                                                    "length": 124,
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "link_tlvs": {
                                                                            1: {
                                                                                "link_type": 2,
                                                                                "link_name": "broadcast network",
                                                                                "remote_if_ipv4_addrs": {
                                                                                    "remote_if_ipv4_addr": "0.0.0.0",
                                                                                },
                                                                                "link_id": "10.1.4.4",
                                                                                "local_if_ipv4_addrs": {
                                                                                    "10.1.4.1": {},
                                                                                },
                                                                                "te_metric": 1,
                                                                                "max_bandwidth": 125000000,
                                                                                "max_reservable_bandwidth": 93750000,
                                                                                "total_priority": 8,
                                                                                "unreserved_bandwidths": {
                                                                                    "0 93750000": {
                                                                                        "priority": 0,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "1 93750000": {
                                                                                        "priority": 1,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "2 93750000": {
                                                                                        "priority": 2,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "3 93750000": {
                                                                                        "priority": 3,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "4 93750000": {
                                                                                        "priority": 4,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "5 93750000": {
                                                                                        "priority": 5,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "6 93750000": {
                                                                                        "priority": 6,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "7 93750000": {
                                                                                        "priority": 7,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                },
                                                                                "admin_group": "0",
                                                                                "igp_metric": 1,
                                                                            },
                                                                        },
                                                                        "num_of_links": 1,
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        "10.1.0.2 10.4.1.1": {
                                                            "adv_router": "10.4.1.1",
                                                            "lsa_id": "10.1.0.2",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 1427,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.0.2",
                                                                    "adv_router": "10.4.1.1",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 2,
                                                                    "seq_num": "80000002",
                                                                    "checksum": "0xb43d",
                                                                    "length": 124,
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "link_tlvs": {
                                                                            1: {
                                                                                "link_type": 2,
                                                                                "link_name": "broadcast network",
                                                                                "remote_if_ipv4_addrs": {
                                                                                    "remote_if_ipv4_addr": "0.0.0.0",
                                                                                },
                                                                                "link_id": "10.1.2.1",
                                                                                "local_if_ipv4_addrs": {
                                                                                    "10.1.2.1": {},
                                                                                },
                                                                                "te_metric": 1,
                                                                                "max_bandwidth": 125000000,
                                                                                "max_reservable_bandwidth": 93750000,
                                                                                "total_priority": 8,
                                                                                "unreserved_bandwidths": {
                                                                                    "0 93750000": {
                                                                                        "priority": 0,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "1 93750000": {
                                                                                        "priority": 1,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "2 93750000": {
                                                                                        "priority": 2,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "3 93750000": {
                                                                                        "priority": 3,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "4 93750000": {
                                                                                        "priority": 4,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "5 93750000": {
                                                                                        "priority": 5,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "6 93750000": {
                                                                                        "priority": 6,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "7 93750000": {
                                                                                        "priority": 7,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                },
                                                                                "admin_group": "0",
                                                                                "igp_metric": 1,
                                                                            },
                                                                        },
                                                                        "num_of_links": 1,
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        "10.1.0.4 10.36.3.3": {
                                                            "adv_router": "10.36.3.3",
                                                            "lsa_id": "10.1.0.4",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 1175,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.0.4",
                                                                    "adv_router": "10.36.3.3",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 4,
                                                                    "seq_num": "80000002",
                                                                    "checksum": "0x915d",
                                                                    "length": 160,
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "link_tlvs": {
                                                                            1: {
                                                                                "link_type": 2,
                                                                                "link_name": "broadcast network",
                                                                                "remote_if_ipv4_addrs": {
                                                                                    "remote_if_ipv4_addr": "0.0.0.0",
                                                                                },
                                                                                "link_id": "10.3.4.4",
                                                                                "local_if_ipv4_addrs": {
                                                                                    "10.3.4.3": {},
                                                                                },
                                                                                "te_metric": 1,
                                                                                "max_bandwidth": 125000000,
                                                                                "max_reservable_bandwidth": 93750000,
                                                                                "total_priority": 8,
                                                                                "unreserved_bandwidths": {
                                                                                    "0 93750000": {
                                                                                        "priority": 0,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "1 93750000": {
                                                                                        "priority": 1,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "2 93750000": {
                                                                                        "priority": 2,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "3 93750000": {
                                                                                        "priority": 3,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "4 93750000": {
                                                                                        "priority": 4,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "5 93750000": {
                                                                                        "priority": 5,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "6 93750000": {
                                                                                        "priority": 6,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "7 93750000": {
                                                                                        "priority": 7,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                },
                                                                                "admin_group": "0",
                                                                                "igp_metric": 1,
                                                                                "extended_admin_group": {
                                                                                    "length": 8,
                                                                                    "groups": {
                                                                                        0: {
                                                                                            "value": 0,
                                                                                        },
                                                                                        1: {
                                                                                            "value": 0,
                                                                                        },
                                                                                        2: {
                                                                                            "value": 0,
                                                                                        },
                                                                                        3: {
                                                                                            "value": 0,
                                                                                        },
                                                                                        4: {
                                                                                            "value": 0,
                                                                                        },
                                                                                        5: {
                                                                                            "value": 0,
                                                                                        },
                                                                                        6: {
                                                                                            "value": 0,
                                                                                        },
                                                                                        7: {
                                                                                            "value": 0,
                                                                                        },
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                        "num_of_links": 1,
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        "10.1.0.6 10.36.3.3": {
                                                            "adv_router": "10.36.3.3",
                                                            "lsa_id": "10.1.0.6",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 1175,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.0.6",
                                                                    "adv_router": "10.36.3.3",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 6,
                                                                    "seq_num": "80000002",
                                                                    "checksum": "0x5ec",
                                                                    "length": 160,
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "link_tlvs": {
                                                                            1: {
                                                                                "link_type": 2,
                                                                                "link_name": "broadcast network",
                                                                                "remote_if_ipv4_addrs": {
                                                                                    "remote_if_ipv4_addr": "0.0.0.0",
                                                                                },
                                                                                "link_id": "10.2.3.3",
                                                                                "local_if_ipv4_addrs": {
                                                                                    "10.2.3.3": {},
                                                                                },
                                                                                "te_metric": 1,
                                                                                "max_bandwidth": 125000000,
                                                                                "max_reservable_bandwidth": 93750000,
                                                                                "total_priority": 8,
                                                                                "unreserved_bandwidths": {
                                                                                    "0 93750000": {
                                                                                        "priority": 0,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "1 93750000": {
                                                                                        "priority": 1,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "2 93750000": {
                                                                                        "priority": 2,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "3 93750000": {
                                                                                        "priority": 3,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "4 93750000": {
                                                                                        "priority": 4,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "5 93750000": {
                                                                                        "priority": 5,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "6 93750000": {
                                                                                        "priority": 6,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "7 93750000": {
                                                                                        "priority": 7,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                },
                                                                                "admin_group": "0",
                                                                                "igp_metric": 1,
                                                                                "extended_admin_group": {
                                                                                    "length": 8,
                                                                                    "groups": {
                                                                                        0: {
                                                                                            "value": 0,
                                                                                        },
                                                                                        1: {
                                                                                            "value": 0,
                                                                                        },
                                                                                        2: {
                                                                                            "value": 0,
                                                                                        },
                                                                                        3: {
                                                                                            "value": 0,
                                                                                        },
                                                                                        4: {
                                                                                            "value": 0,
                                                                                        },
                                                                                        5: {
                                                                                            "value": 0,
                                                                                        },
                                                                                        6: {
                                                                                            "value": 0,
                                                                                        },
                                                                                        7: {
                                                                                            "value": 0,
                                                                                        },
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                        "num_of_links": 1,
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        "10.1.0.37 10.16.2.2": {
                                                            "adv_router": "10.16.2.2",
                                                            "lsa_id": "10.1.0.37",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 242,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, No DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.0.37",
                                                                    "adv_router": "10.16.2.2",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 37,
                                                                    "seq_num": "80000004",
                                                                    "checksum": "0xe492",
                                                                    "length": 116,
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "link_tlvs": {
                                                                            1: {
                                                                                "link_type": 2,
                                                                                "link_name": "broadcast network",
                                                                                "remote_if_ipv4_addrs": {
                                                                                    "remote_if_ipv4_addr": "0.0.0.0",
                                                                                },
                                                                                "link_id": "10.2.3.3",
                                                                                "local_if_ipv4_addrs": {
                                                                                    "10.2.3.2": {},
                                                                                },
                                                                                "te_metric": 1,
                                                                                "max_bandwidth": 125000000,
                                                                                "max_reservable_bandwidth": 93750000,
                                                                                "total_priority": 8,
                                                                                "unreserved_bandwidths": {
                                                                                    "0 93750000": {
                                                                                        "priority": 0,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "1 93750000": {
                                                                                        "priority": 1,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "2 93750000": {
                                                                                        "priority": 2,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "3 93750000": {
                                                                                        "priority": 3,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "4 93750000": {
                                                                                        "priority": 4,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "5 93750000": {
                                                                                        "priority": 5,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "6 93750000": {
                                                                                        "priority": 6,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "7 93750000": {
                                                                                        "priority": 7,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                },
                                                                                "admin_group": "0",
                                                                            },
                                                                        },
                                                                        "num_of_links": 1,
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        "10.1.0.38 10.16.2.2": {
                                                            "adv_router": "10.16.2.2",
                                                            "lsa_id": "10.1.0.38",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 233,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, No DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.0.38",
                                                                    "adv_router": "10.16.2.2",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 38,
                                                                    "seq_num": "80000004",
                                                                    "checksum": "0x2350",
                                                                    "length": 116,
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "link_tlvs": {
                                                                            1: {
                                                                                "link_type": 2,
                                                                                "link_name": "broadcast network",
                                                                                "remote_if_ipv4_addrs": {
                                                                                    "remote_if_ipv4_addr": "0.0.0.0",
                                                                                },
                                                                                "link_id": "10.2.4.4",
                                                                                "local_if_ipv4_addrs": {
                                                                                    "10.2.4.2": {},
                                                                                },
                                                                                "te_metric": 1,
                                                                                "max_bandwidth": 125000000,
                                                                                "max_reservable_bandwidth": 93750000,
                                                                                "total_priority": 8,
                                                                                "unreserved_bandwidths": {
                                                                                    "0 93750000": {
                                                                                        "priority": 0,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "1 93750000": {
                                                                                        "priority": 1,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "2 93750000": {
                                                                                        "priority": 2,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "3 93750000": {
                                                                                        "priority": 3,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "4 93750000": {
                                                                                        "priority": 4,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "5 93750000": {
                                                                                        "priority": 5,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "6 93750000": {
                                                                                        "priority": 6,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "7 93750000": {
                                                                                        "priority": 7,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                },
                                                                                "admin_group": "0",
                                                                            },
                                                                        },
                                                                        "num_of_links": 1,
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        "10.1.0.39 10.16.2.2": {
                                                            "adv_router": "10.16.2.2",
                                                            "lsa_id": "10.1.0.39",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 232,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, No DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.0.39",
                                                                    "adv_router": "10.16.2.2",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 39,
                                                                    "seq_num": "80000004",
                                                                    "checksum": "0x4239",
                                                                    "length": 116,
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "link_tlvs": {
                                                                            1: {
                                                                                "link_type": 2,
                                                                                "link_name": "broadcast network",
                                                                                "remote_if_ipv4_addrs": {
                                                                                    "remote_if_ipv4_addr": "0.0.0.0",
                                                                                },
                                                                                "link_id": "10.1.2.1",
                                                                                "local_if_ipv4_addrs": {
                                                                                    "10.1.2.2": {},
                                                                                },
                                                                                "te_metric": 1,
                                                                                "max_bandwidth": 125000000,
                                                                                "max_reservable_bandwidth": 93750000,
                                                                                "total_priority": 8,
                                                                                "unreserved_bandwidths": {
                                                                                    "0 93750000": {
                                                                                        "priority": 0,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "1 93750000": {
                                                                                        "priority": 1,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "2 93750000": {
                                                                                        "priority": 2,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "3 93750000": {
                                                                                        "priority": 3,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "4 93750000": {
                                                                                        "priority": 4,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "5 93750000": {
                                                                                        "priority": 5,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "6 93750000": {
                                                                                        "priority": 6,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                    "7 93750000": {
                                                                                        "priority": 7,
                                                                                        "unreserved_bandwidth": 93750000,
                                                                                    },
                                                                                },
                                                                                "admin_group": "0",
                                                                            },
                                                                        },
                                                                        "num_of_links": 1,
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            "VRF1": {"address_family": {"ipv4": {"instance": {"1": {},},},},},
        },
    }

    golden_output1 = {
        "execute.return_value": """
        RP/0/0/CPU0:R3_ospf_xr#show ospf vrf all-inclusive database opaque-area
        Thu Nov  2 21:27:17.362 UTC

                    OSPF Router with ID (10.36.3.3) (Process ID 1)

                        Type-10 Opaque Link Area Link States (Area 0)

          LS age: 1427
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.0
          Opaque Type: 1
          Opaque ID: 0
          Advertising Router: 10.4.1.1
          LS Seq Number: 80000002
          Checksum: 0x56d2
          Length: 28

            MPLS TE router ID : 10.4.1.1

            Number of Links : 0

          LS age: 653
          Options: (No TOS-capability, No DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.0
          Opaque Type: 1
          Opaque ID: 0
          Advertising Router: 10.16.2.2
          LS Seq Number: 80000003
          Checksum: 0x1c22
          Length: 28

            MPLS TE router ID : 10.16.2.2

            Number of Links : 0

          LS age: 1175
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.0
          Opaque Type: 1
          Opaque ID: 0
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000002
          Checksum: 0x5eba
          Length: 28

            MPLS TE router ID : 10.36.3.3

            Number of Links : 0

          LS age: 1427
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.1
          Opaque Type: 1
          Opaque ID: 1
          Advertising Router: 10.4.1.1
          LS Seq Number: 80000002
          Checksum: 0x6586
          Length: 124

            Link connected to Broadcast network
              Link ID : 10.1.4.4
              (all bandwidths in bytes/sec)
              Interface Address : 10.1.4.1
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth global: 93750000
              Number of Priority : 8
              Priority 0 :             93750000  Priority 1 :             93750000
              Priority 2 :             93750000  Priority 3 :             93750000
              Priority 4 :             93750000  Priority 5 :             93750000
              Priority 6 :             93750000  Priority 7 :             93750000
              Affinity Bit : 0
              IGP Metric : 1

            Number of Links : 1

          LS age: 1427
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.2
          Opaque Type: 1
          Opaque ID: 2
          Advertising Router: 10.4.1.1
          LS Seq Number: 80000002
          Checksum: 0xb43d
          Length: 124

            Link connected to Broadcast network
              Link ID : 10.1.2.1
              (all bandwidths in bytes/sec)
              Interface Address : 10.1.2.1
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth global: 93750000
              Number of Priority : 8
              Priority 0 :             93750000  Priority 1 :             93750000
              Priority 2 :             93750000  Priority 3 :             93750000
              Priority 4 :             93750000  Priority 5 :             93750000
              Priority 6 :             93750000  Priority 7 :             93750000
              Affinity Bit : 0
              IGP Metric : 1

            Number of Links : 1

          LS age: 1175
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.4
          Opaque Type: 1
          Opaque ID: 4
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000002
          Checksum: 0x915d
          Length: 160

            Link connected to Broadcast network
              Link ID : 10.3.4.4
              (all bandwidths in bytes/sec)
              Interface Address : 10.3.4.3
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth global: 93750000
              Number of Priority : 8
              Priority 0 :             93750000  Priority 1 :             93750000
              Priority 2 :             93750000  Priority 3 :             93750000
              Priority 4 :             93750000  Priority 5 :             93750000
              Priority 6 :             93750000  Priority 7 :             93750000
              Affinity Bit : 0
              IGP Metric : 1
              Extended Administrative Group : Length: 8
               EAG[0]: 0
               EAG[1]: 0
               EAG[2]: 0
               EAG[3]: 0
               EAG[4]: 0
               EAG[5]: 0
               EAG[6]: 0
               EAG[7]: 0

            Number of Links : 1

          LS age: 1175
          Options: (No TOS-capability, DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.6
          Opaque Type: 1
          Opaque ID: 6
          Advertising Router: 10.36.3.3
          LS Seq Number: 80000002
          Checksum: 0x5ec
          Length: 160

            Link connected to Broadcast network
              Link ID : 10.2.3.3
              (all bandwidths in bytes/sec)
              Interface Address : 10.2.3.3
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth global: 93750000
              Number of Priority : 8
              Priority 0 :             93750000  Priority 1 :             93750000
              Priority 2 :             93750000  Priority 3 :             93750000
              Priority 4 :             93750000  Priority 5 :             93750000
              Priority 6 :             93750000  Priority 7 :             93750000
              Affinity Bit : 0
              IGP Metric : 1
              Extended Administrative Group : Length: 8
               EAG[0]: 0
               EAG[1]: 0
               EAG[2]: 0
               EAG[3]: 0
               EAG[4]: 0
               EAG[5]: 0
               EAG[6]: 0
               EAG[7]: 0

            Number of Links : 1

          LS age: 242
          Options: (No TOS-capability, No DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.37
          Opaque Type: 1
          Opaque ID: 37
          Advertising Router: 10.16.2.2
          LS Seq Number: 80000004
          Checksum: 0xe492
          Length: 116

            Link connected to Broadcast network
              Link ID : 10.2.3.3
              (all bandwidths in bytes/sec)
              Interface Address : 10.2.3.2
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth global: 93750000
              Number of Priority : 8
              Priority 0 :             93750000  Priority 1 :             93750000
              Priority 2 :             93750000  Priority 3 :             93750000
              Priority 4 :             93750000  Priority 5 :             93750000
              Priority 6 :             93750000  Priority 7 :             93750000
              Affinity Bit : 0

            Number of Links : 1

          LS age: 233
          Options: (No TOS-capability, No DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.38
          Opaque Type: 1
          Opaque ID: 38
          Advertising Router: 10.16.2.2
          LS Seq Number: 80000004
          Checksum: 0x2350
          Length: 116

            Link connected to Broadcast network
              Link ID : 10.2.4.4
              (all bandwidths in bytes/sec)
              Interface Address : 10.2.4.2
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth global: 93750000
              Number of Priority : 8
              Priority 0 :             93750000  Priority 1 :             93750000
              Priority 2 :             93750000  Priority 3 :             93750000
              Priority 4 :             93750000  Priority 5 :             93750000
              Priority 6 :             93750000  Priority 7 :             93750000
              Affinity Bit : 0

            Number of Links : 1

          LS age: 232
          Options: (No TOS-capability, No DC)
          LS Type: Opaque Area Link
          Link State ID: 10.1.0.39
          Opaque Type: 1
          Opaque ID: 39
          Advertising Router: 10.16.2.2
          LS Seq Number: 80000004
          Checksum: 0x4239
          Length: 116

            Link connected to Broadcast network
              Link ID : 10.1.2.1
              (all bandwidths in bytes/sec)
              Interface Address : 10.1.2.2
              Admin Metric : 1
              Maximum bandwidth : 125000000
              Maximum reservable bandwidth global: 93750000
              Number of Priority : 8
              Priority 0 :             93750000  Priority 1 :             93750000
              Priority 2 :             93750000  Priority 3 :             93750000
              Priority 4 :             93750000  Priority 5 :             93750000
              Priority 6 :             93750000  Priority 7 :             93750000
              Affinity Bit : 0

            Number of Links : 1

                    OSPF Router with ID (10.36.3.3) (Process ID 1, VRF VRF1)
        """
    }

    def test_show_ospf_vrf_all_inclusive_database_opaque_area_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowOspfVrfAllInclusiveDatabaseOpaqueArea(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ospf_vrf_all_inclusive_database_opaque_area_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowOspfVrfAllInclusiveDatabaseOpaqueArea(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    golden_parsed_output2 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "64577": {
                                "areas": {
                                    "0.0.0.0": {
                                        "database": {
                                            "lsa_types": {
                                                10: {
                                                    "lsa_type": 10,
                                                    "lsas": {
                                                        "10.16.0.0 10.154.219.84": {
                                                            "adv_router": "10.154.219.84",
                                                            "lsa_id": "10.16.0.0",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 65,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.16.0.0",
                                                                    "adv_router": "10.154.219.84",
                                                                    "opaque_type": 4,
                                                                    "opaque_id": 0,
                                                                    "seq_num": "80004c15",
                                                                    "checksum": "0xadfd",
                                                                    "length": 76,
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "router_capabilities_tlv": {
                                                                            1: {
                                                                                "length": 4,
                                                                                "information_capabilities": {
                                                                                    "graceful_restart_helper": True,
                                                                                    "stub_router": True,
                                                                                    "capability_bits": "0x60000000",
                                                                                },
                                                                            },
                                                                        },
                                                                        "sr_algorithm_tlv": {
                                                                            1: {
                                                                                "length": 2,
                                                                                "algorithm": {
                                                                                    "0": True,
                                                                                    "1": True,
                                                                                },
                                                                            },
                                                                        },
                                                                        "sid_range_tlvs": {
                                                                            1: {
                                                                                "length": 12,
                                                                                "tlv_type": "Segment Routing Range",
                                                                                "range_size": 65535,
                                                                                "sub_tlvs": {
                                                                                    1: {
                                                                                        "length": 3,
                                                                                        "type": "SID",
                                                                                        "label": 16000,
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                        "node_msd_tlvs": {
                                                                            1: {
                                                                                "length": 2,
                                                                                "node_type": 1,
                                                                                "value": 10,
                                                                            },
                                                                        },
                                                                        "local_block_tlvs": {
                                                                            1: {
                                                                                "length": 12,
                                                                                "range_size": 1000,
                                                                                "sub_tlvs": {
                                                                                    1: {
                                                                                        "length": 3,
                                                                                        "type": "SID",
                                                                                        "label": 15000,
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        "10.49.0.1 10.154.219.84": {
                                                            "adv_router": "10.154.219.84",
                                                            "lsa_id": "10.49.0.1",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 65,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.49.0.1",
                                                                    "adv_router": "10.154.219.84",
                                                                    "opaque_type": 7,
                                                                    "opaque_id": 1,
                                                                    "seq_num": "800009be",
                                                                    "checksum": "0xf6d0",
                                                                    "length": 48,
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "extended_prefix_tlvs": {
                                                                            1: {
                                                                                "length": 24,
                                                                                "af": 0,
                                                                                "prefix": "10.246.254.0/32",
                                                                                "range_size": 256,
                                                                                "flags": "0x0",
                                                                                "sub_tlvs": {
                                                                                    1: {
                                                                                        "length": 8,
                                                                                        "type": "SID",
                                                                                        "flags": "0x60",
                                                                                        "mt_id": "0",
                                                                                        "algo": 0,
                                                                                        "sid": 1028,
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        "10.64.0.78 10.154.219.85": {
                                                            "adv_router": "10.154.219.85",
                                                            "lsa_id": "10.64.0.78",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 1057,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.64.0.78",
                                                                    "adv_router": "10.154.219.85",
                                                                    "opaque_type": 8,
                                                                    "opaque_id": 78,
                                                                    "seq_num": "800004bf",
                                                                    "checksum": "0x9a5b",
                                                                    "length": 100,
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "extended_link_tlvs": {
                                                                            1: {
                                                                                "length": 76,
                                                                                "link_type": 1,
                                                                                "link_id": "10.154.219.57",
                                                                                "link_data": "172.16.0.91",
                                                                                "sub_tlvs": {
                                                                                    1: {
                                                                                        "length": 7,
                                                                                        "type": "Adj",
                                                                                        "flags": "0x60",
                                                                                        "mt_id": "0",
                                                                                        "weight": 0,
                                                                                        "label": 100479,
                                                                                    },
                                                                                    2: {
                                                                                        "length": 8,
                                                                                        "type": "Local-ID Remote-ID",
                                                                                        "local_interface_id": 78,
                                                                                        "remote_interface_id": 76,
                                                                                    },
                                                                                    3: {
                                                                                        "length": 4,
                                                                                        "type": "Remote If Address",
                                                                                        "neighbor_address": "172.16.0.90",
                                                                                    },
                                                                                    4: {
                                                                                        "length": 2,
                                                                                        "type": "Link MSD",
                                                                                        "node_type": 1,
                                                                                        "value": 10,
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        "10.1.0.3 10.154.219.51": {
                                                            "adv_router": "10.154.219.51",
                                                            "lsa_id": "10.1.0.3",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 586,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.0.3",
                                                                    "adv_router": "10.154.219.51",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 3,
                                                                    "seq_num": "80004036",
                                                                    "checksum": "0xe06c",
                                                                    "length": 136,
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "link_tlvs": {
                                                                            1: {
                                                                                "link_type": 1,
                                                                                "link_name": "point-to-point network",
                                                                                "link_id": "10.154.219.106",
                                                                                "local_if_ipv4_addrs": {
                                                                                    "172.16.1.153": {},
                                                                                },
                                                                                "neighbor_address": "172.16.1.152",
                                                                                "te_metric": 10000,
                                                                                "max_bandwidth": 750000000,
                                                                                "max_reservable_bandwidth": 750000000,
                                                                                "total_priority": 8,
                                                                                "unreserved_bandwidths": {
                                                                                    "0 750000000": {
                                                                                        "priority": 0,
                                                                                        "unreserved_bandwidth": 750000000,
                                                                                    },
                                                                                    "1 750000000": {
                                                                                        "priority": 1,
                                                                                        "unreserved_bandwidth": 750000000,
                                                                                    },
                                                                                    "2 750000000": {
                                                                                        "priority": 2,
                                                                                        "unreserved_bandwidth": 750000000,
                                                                                    },
                                                                                    "3 750000000": {
                                                                                        "priority": 3,
                                                                                        "unreserved_bandwidth": 750000000,
                                                                                    },
                                                                                    "4 750000000": {
                                                                                        "priority": 4,
                                                                                        "unreserved_bandwidth": 750000000,
                                                                                    },
                                                                                    "5 750000000": {
                                                                                        "priority": 5,
                                                                                        "unreserved_bandwidth": 750000000,
                                                                                    },
                                                                                    "6 750000000": {
                                                                                        "priority": 6,
                                                                                        "unreserved_bandwidth": 750000000,
                                                                                    },
                                                                                    "7 750000000": {
                                                                                        "priority": 7,
                                                                                        "unreserved_bandwidth": 750000000,
                                                                                    },
                                                                                },
                                                                                "admin_group": "0",
                                                                            },
                                                                        },
                                                                        "num_of_links": 1,
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        "10.1.17.240 10.154.219.85": {
                                                            "adv_router": "10.154.219.85",
                                                            "lsa_id": "10.1.17.240",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 1057,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.17.240",
                                                                    "adv_router": "10.154.219.85",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 4592,
                                                                    "seq_num": "800004c1",
                                                                    "checksum": "0x827c",
                                                                    "length": 80,
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "link_tlvs": {
                                                                            1: {
                                                                                "link_type": 1,
                                                                                "link_name": "point-to-point network",
                                                                                "link_id": "10.154.219.58",
                                                                                "local_if_ipv4_addrs": {
                                                                                    "172.16.0.99": {},
                                                                                },
                                                                                "neighbor_address": "172.16.0.98",
                                                                                "te_metric": 1000,
                                                                                "max_bandwidth": 1250000000,
                                                                                "igp_metric": 1000,
                                                                            },
                                                                        },
                                                                        "num_of_links": 1,
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output2 = {
        "execute.return_value": """
        show ospf vrf all-inclusive database opaque-area

        Wed Oct  9 14:37:02.679 EDT

                OSPF Router with ID (10.154.219.84) (Process ID 64577)

        Type-10 Opaque Link Area Link States (Area 0)

        LS age: 65
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.16.0.0
        Opaque Type: 4
        Opaque ID: 0
        Advertising Router: 10.154.219.84
        LS Seq Number: 80004c15
        Checksum: 0xadfd
        Length: 76

            Router Information TLV: Length: 4
            Capabilities:
            Graceful Restart Helper Capable
            Stub Router Capable
            All capability bits: 0x60000000

            Segment Routing Algorithm TLV: Length: 2
            Algorithm: 0
            Algorithm: 1

            Segment Routing Range TLV: Length: 12
            Range Size: 65535

                SID sub-TLV: Length 3
                Label: 16000

            Node MSD TLV: Length: 2
                Type: 1, Value 10

            Segment Routing Local Block TLV: Length: 12
            Range Size: 1000

                SID sub-TLV: Length 3
                Label: 15000

        LS age: 65
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.49.0.1
        Opaque Type: 7
        Opaque ID: 1
        Advertising Router: 10.154.219.84
        LS Seq Number: 800009be
        Checksum: 0xf6d0
        Length: 48

            Extended Prefix Range TLV: Length: 24
            AF        : 0
            Prefix    : 10.246.254.0/32
            Range Size: 256
            Flags     : 0x0

            SID sub-TLV: Length: 8
                Flags     : 0x60
                MTID      : 0
                Algo      : 0
                SID Index : 1028

        LS age: 1057
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.64.0.78
        Opaque Type: 8
        Opaque ID: 78
        Advertising Router: 10.154.219.85
        LS Seq Number: 800004bf
        Checksum: 0x9a5b
        Length: 100

          Extended Link TLV: Length: 76
            Link-type : 1
            Link ID   : 10.154.219.57
            Link Data : 172.16.0.91

            Adj sub-TLV: Length: 7
                Flags     : 0x60
                MTID      : 0
                Weight    : 0
                Label     : 100479

            Local-ID Remote-ID sub-TLV: Length: 8
                Local Interface ID: 78
                Remote Interface ID: 76

            Remote If Address sub-TLV: Length: 4
                Neighbor Address: 172.16.0.90

            Link MSD sub-TLV: Length: 2
                Type: 1, Value 10

        LS age: 586
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.1.0.3
        Opaque Type: 1
        Opaque ID: 3
        Advertising Router: 10.154.219.51
        LS Seq Number: 80004036
        Checksum: 0xe06c
        Length: 136

            Link connected to Point-to-Point network
            Link ID : 10.154.219.106
            (all bandwidths in bytes/sec)
            Interface Address : 172.16.1.153
            Neighbor Address : 172.16.1.152
            Admin Metric : 10000
            Maximum bandwidth : 750000000
            Maximum reservable bandwidth global: 750000000
            Number of Priority : 8
            Priority 0 :            750000000  Priority 1 :            750000000
            Priority 2 :            750000000  Priority 3 :            750000000
            Priority 4 :            750000000  Priority 5 :            750000000
            Priority 6 :            750000000  Priority 7 :            750000000
            Link Identifiers:
                Local (Out) Id: 486  Remote (In) Id: 0
            Affinity Bit : 0

            Number of Links : 1

        LS age: 1057
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.1.17.240
        Opaque Type: 1
        Opaque ID: 4592
        Advertising Router: 10.154.219.85
        LS Seq Number: 800004c1
        Checksum: 0x827c
        Length: 80

            Link connected to Point-to-Point network
            Link ID : 10.154.219.58
            (all bandwidths in bytes/sec)
            Interface Address : 172.16.0.99
            Neighbor Address : 172.16.0.98
            Admin Metric : 1000
            Maximum bandwidth : 1250000000
            IGP Metric : 1000

            Number of Links : 1
    """
    }

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowOspfVrfAllInclusiveDatabaseOpaqueArea(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    golden_parsed_output3 = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "instance": {
                            "64577": {
                                "areas": {
                                    "0.0.0.0": {
                                        "database": {
                                            "lsa_types": {
                                                10: {
                                                    "lsa_type": 10,
                                                    "lsas": {
                                                        "10.16.0.0 10.154.219.84": {
                                                            "adv_router": "10.154.219.84",
                                                            "lsa_id": "10.16.0.0",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 65,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.16.0.0",
                                                                    "adv_router": "10.154.219.84",
                                                                    "opaque_type": 4,
                                                                    "opaque_id": 0,
                                                                    "seq_num": "80004c15",
                                                                    "checksum": "0xadfd",
                                                                    "length": 76,
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "router_capabilities_tlv": {
                                                                            1: {
                                                                                "length": 4,
                                                                                "information_capabilities": {
                                                                                    "graceful_restart_helper": True,
                                                                                    "stub_router": True,
                                                                                    "capability_bits": "0x60000000",
                                                                                },
                                                                            },
                                                                        },
                                                                        "sr_algorithm_tlv": {
                                                                            1: {
                                                                                "length": 2,
                                                                                "algorithm": {
                                                                                    "0": True,
                                                                                    "1": True,
                                                                                },
                                                                            },
                                                                        },
                                                                        "sid_range_tlvs": {
                                                                            1: {
                                                                                "length": 12,
                                                                                "tlv_type": "Segment Routing Range",
                                                                                "range_size": 65535,
                                                                                "sub_tlvs": {
                                                                                    1: {
                                                                                        "length": 3,
                                                                                        "type": "SID",
                                                                                        "label": 16000,
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                        "node_msd_tlvs": {
                                                                            1: {
                                                                                "length": 2,
                                                                                "node_type": 1,
                                                                                "value": 10,
                                                                            },
                                                                        },
                                                                        "local_block_tlvs": {
                                                                            1: {
                                                                                "length": 12,
                                                                                "range_size": 1000,
                                                                                "sub_tlvs": {
                                                                                    1: {
                                                                                        "length": 3,
                                                                                        "type": "SID",
                                                                                        "label": 15000,
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        "10.49.0.1 10.154.219.84": {
                                                            "adv_router": "10.154.219.84",
                                                            "lsa_id": "10.49.0.1",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 65,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.49.0.1",
                                                                    "adv_router": "10.154.219.84",
                                                                    "opaque_type": 7,
                                                                    "opaque_id": 1,
                                                                    "seq_num": "800009be",
                                                                    "checksum": "0xf6d0",
                                                                    "length": 48,
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "extended_prefix_tlvs": {
                                                                            1: {
                                                                                "length": 24,
                                                                                "af": 0,
                                                                                "prefix": "10.246.254.0/32",
                                                                                "range_size": 256,
                                                                                "flags": "0x0",
                                                                                "sub_tlvs": {
                                                                                    1: {
                                                                                        "length": 8,
                                                                                        "type": "SID",
                                                                                        "flags": "0x60",
                                                                                        "mt_id": "0",
                                                                                        "algo": 0,
                                                                                        "sid": 1028,
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        "10.64.0.78 10.154.219.85": {
                                                            "adv_router": "10.154.219.85",
                                                            "lsa_id": "10.64.0.78",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 1057,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.64.0.78",
                                                                    "adv_router": "10.154.219.85",
                                                                    "opaque_type": 8,
                                                                    "opaque_id": 78,
                                                                    "seq_num": "800004bf",
                                                                    "checksum": "0x9a5b",
                                                                    "length": 100,
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "extended_link_tlvs": {
                                                                            1: {
                                                                                "length": 76,
                                                                                "link_type": 1,
                                                                                "link_id": "10.154.219.57",
                                                                                "link_data": "172.16.0.91",
                                                                                "sub_tlvs": {
                                                                                    1: {
                                                                                        "length": 7,
                                                                                        "type": "Adj",
                                                                                        "flags": "0x60",
                                                                                        "mt_id": "0",
                                                                                        "weight": 0,
                                                                                        "label": 100479,
                                                                                    },
                                                                                    2: {
                                                                                        "length": 8,
                                                                                        "type": "Local-ID Remote-ID",
                                                                                        "local_interface_id": 78,
                                                                                        "remote_interface_id": 76,
                                                                                    },
                                                                                    3: {
                                                                                        "length": 4,
                                                                                        "type": "Remote If Address",
                                                                                        "neighbor_address": "172.16.0.90",
                                                                                    },
                                                                                    4: {
                                                                                        "length": 2,
                                                                                        "type": "Link MSD",
                                                                                        "node_type": 1,
                                                                                        "value": 10,
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        "10.1.0.3 10.154.219.51": {
                                                            "adv_router": "10.154.219.51",
                                                            "lsa_id": "10.1.0.3",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 586,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.0.3",
                                                                    "adv_router": "10.154.219.51",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 3,
                                                                    "seq_num": "80004036",
                                                                    "checksum": "0xe06c",
                                                                    "length": 136,
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "link_tlvs": {
                                                                            1: {
                                                                                "link_type": 1,
                                                                                "link_name": "point-to-point network",
                                                                                "link_id": "10.154.219.106",
                                                                                "local_if_ipv4_addrs": {
                                                                                    "172.16.1.153": {},
                                                                                },
                                                                                "neighbor_address": "172.16.1.152",
                                                                                "te_metric": 10000,
                                                                                "max_bandwidth": 750000000,
                                                                                "max_reservable_bandwidth": 750000000,
                                                                                "total_priority": 8,
                                                                                "unreserved_bandwidths": {
                                                                                    "0 750000000": {
                                                                                        "priority": 0,
                                                                                        "unreserved_bandwidth": 750000000,
                                                                                    },
                                                                                    "1 750000000": {
                                                                                        "priority": 1,
                                                                                        "unreserved_bandwidth": 750000000,
                                                                                    },
                                                                                    "2 750000000": {
                                                                                        "priority": 2,
                                                                                        "unreserved_bandwidth": 750000000,
                                                                                    },
                                                                                    "3 750000000": {
                                                                                        "priority": 3,
                                                                                        "unreserved_bandwidth": 750000000,
                                                                                    },
                                                                                    "4 750000000": {
                                                                                        "priority": 4,
                                                                                        "unreserved_bandwidth": 750000000,
                                                                                    },
                                                                                    "5 750000000": {
                                                                                        "priority": 5,
                                                                                        "unreserved_bandwidth": 750000000,
                                                                                    },
                                                                                    "6 750000000": {
                                                                                        "priority": 6,
                                                                                        "unreserved_bandwidth": 750000000,
                                                                                    },
                                                                                    "7 750000000": {
                                                                                        "priority": 7,
                                                                                        "unreserved_bandwidth": 750000000,
                                                                                    },
                                                                                },
                                                                                "admin_group": "0",
                                                                            },
                                                                        },
                                                                        "num_of_links": 1,
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        "10.1.17.240 10.154.219.85": {
                                                            "adv_router": "10.154.219.85",
                                                            "lsa_id": "10.1.17.240",
                                                            "ospfv2": {
                                                                "header": {
                                                                    "age": 1057,
                                                                    "option": "None",
                                                                    "option_desc": "No TOS-capability, DC",
                                                                    "type": 10,
                                                                    "lsa_id": "10.1.17.240",
                                                                    "adv_router": "10.154.219.85",
                                                                    "opaque_type": 1,
                                                                    "opaque_id": 4592,
                                                                    "seq_num": "800004c1",
                                                                    "checksum": "0x827c",
                                                                    "length": 80,
                                                                },
                                                                "body": {
                                                                    "opaque": {
                                                                        "link_tlvs": {
                                                                            1: {
                                                                                "link_type": 1,
                                                                                "link_name": "point-to-point network",
                                                                                "link_id": "10.154.219.58",
                                                                                "local_if_ipv4_addrs": {
                                                                                    "172.16.0.99": {},
                                                                                },
                                                                                "neighbor_address": "172.16.0.98",
                                                                                "te_metric": 1000,
                                                                                "max_bandwidth": 1250000000,
                                                                                "igp_metric": 1000,
                                                                            },
                                                                        },
                                                                        "num_of_links": 1,
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output3 = {
        "execute.return_value": """
        show ospf vrf all-inclusive database opaque-area

        Wed Oct  9 14:37:02.679 EDT

                OSPF Router with ID (10.154.219.84) (Process ID 64577)

        Type-10 Opaque Link Area Link States (Area 0)

        LS age: 65
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.16.0.0
        Opaque Type: 4
        Opaque ID: 0
        Advertising Router: 10.154.219.84
        LS Seq Number: 80004c15
        Checksum: 0xadfd
        Length: 76

            Router Information TLV: Length: 4
            Capabilities:
            Graceful Restart Helper Capable
            Stub Router Capable
            All capability bits: 0x60000000

            Segment Routing Algorithm TLV: Length: 2
            Algorithm: 0
            Algorithm: 1

            Segment Routing Range TLV: Length: 12
            Range Size: 65535

                SID sub-TLV: Length 3
                Label: 16000

            Node MSD TLV: Length: 2
                Type: 1, Value 10

            Segment Routing Local Block TLV: Length: 12
            Range Size: 1000

                SID sub-TLV: Length 3
                Label: 15000

        LS age: 65
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.49.0.1
        Opaque Type: 7
        Opaque ID: 1
        Advertising Router: 10.154.219.84
        LS Seq Number: 800009be
        Checksum: 0xf6d0
        Length: 48

            Extended Prefix TLV: Length: 24
            AF        : 0
            Prefix    : 10.246.254.0/32
            Range Size: 256
            Flags     : 0x0

            SID sub-TLV: Length: 8
                Flags     : 0x60
                MTID      : 0
                Algo      : 0
                SID Index : 1028

        LS age: 1057
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.64.0.78
        Opaque Type: 8
        Opaque ID: 78
        Advertising Router: 10.154.219.85
        LS Seq Number: 800004bf
        Checksum: 0x9a5b
        Length: 100

          Extended Link TLV: Length: 76
            Link-type : 1
            Link ID   : 10.154.219.57
            Link Data : 172.16.0.91

            Adj sub-TLV: Length: 7
                Flags     : 0x60
                MTID      : 0
                Weight    : 0
                Label     : 100479

            Local-ID Remote-ID sub-TLV: Length: 8
                Local Interface ID: 78
                Remote Interface ID: 76

            Remote If Address sub-TLV: Length: 4
                Neighbor Address: 172.16.0.90

            Link MSD sub-TLV: Length: 2
                Type: 1, Value 10

        LS age: 586
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.1.0.3
        Opaque Type: 1
        Opaque ID: 3
        Advertising Router: 10.154.219.51
        LS Seq Number: 80004036
        Checksum: 0xe06c
        Length: 136

            Link connected to Point-to-Point network
            Link ID : 10.154.219.106
            (all bandwidths in bytes/sec)
            Interface Address : 172.16.1.153
            Neighbor Address : 172.16.1.152
            Admin Metric : 10000
            Maximum bandwidth : 750000000
            Maximum reservable bandwidth global: 750000000
            Number of Priority : 8
            Priority 0 :            750000000  Priority 1 :            750000000
            Priority 2 :            750000000  Priority 3 :            750000000
            Priority 4 :            750000000  Priority 5 :            750000000
            Priority 6 :            750000000  Priority 7 :            750000000
            Link Identifiers:
                Local (Out) Id: 486  Remote (In) Id: 0
            Affinity Bit : 0

            Number of Links : 1

        LS age: 1057
        Options: (No TOS-capability, DC)
        LS Type: Opaque Area Link
        Link State ID: 10.1.17.240
        Opaque Type: 1
        Opaque ID: 4592
        Advertising Router: 10.154.219.85
        LS Seq Number: 800004c1
        Checksum: 0x827c
        Length: 80

            Link connected to Point-to-Point network
            Link ID : 10.154.219.58
            (all bandwidths in bytes/sec)
            Interface Address : 172.16.0.99
            Neighbor Address : 172.16.0.98
            Admin Metric : 1000
            Maximum bandwidth : 1250000000
            IGP Metric : 1000

            Number of Links : 1
    """
    }

    def test_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowOspfVrfAllInclusiveDatabaseOpaqueArea(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)

if __name__ == "__main__":
    unittest.main()
