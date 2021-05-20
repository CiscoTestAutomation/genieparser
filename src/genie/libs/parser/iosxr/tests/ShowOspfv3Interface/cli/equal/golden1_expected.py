expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "instance": {
                        "mpls1": {
                            "instance_id": {
                                0: {
                                    "areas": {
                                        0: {
                                            "interfaces": {
                                                "GigabitEthernet0/0/0/0": {
                                                    "enable": True,
                                                    "line_protocol": True,
                                                    "link_local_address": "fe80:100:10::1",
                                                    "interface_id": 7,
                                                    "router_id": "25.97.1.1",
                                                    "interface_type": "POINT_TO_POINT",
                                                    "cost": 1,
                                                    "bfd": {
                                                        "bfd_status": "enabled",
                                                        "interval": 150,
                                                        "multi": 3,
                                                        "mode": "Default",
                                                    },
                                                    "transmit_delay": 1,
                                                    "state": "POINT_TO_POINT",
                                                    "hello_interval": 10,
                                                    "dead_interval": 40,
                                                    "wait_interval": 40,
                                                    "retransmit_interval": 5,
                                                    "hello_timer": "00:00:08",
                                                    "index": "1/1/1",
                                                    "flood_queue_length": 0,
                                                    "next": "0(0)/0(0)/0(0)",
                                                    "last_flood_scan_length": 1,
                                                    "max_flood_scan_length": 4,
                                                    "last_flood_scan_time_msec": 0,
                                                    "max_flood_scan_time_msec": 0,
                                                    "statistics": {
                                                        "nbr_count": 1,
                                                        "adj_nbr_count": 1,
                                                        "neighbor": "95.95.95.95",
                                                        "num_nbrs_suppress_hello": 0,
                                                        "refrence_count": 6,
                                                    },
                                                    "neighbors": {
                                                        "100.100.100.100": {
                                                            "nbr_count": 1,
                                                            "adj_nbr_count": 1,
                                                        },
                                                        "95.95.95.95": {
                                                            "nbr_count": 1,
                                                            "adj_nbr_count": 1,
                                                        },
                                                    },
                                                },
                                                "GigabitEthernet0/0/0/1": {
                                                    "interface": "GigabitEthernet0/0/0/1",
                                                    "enable": True,
                                                    "line_protocol": True,
                                                    "link_local_address": "fe80:100:20::1",
                                                    "interface_id": 8,
                                                    "router_id": "25.97.1.1",
                                                    "interface_type": "POINT_TO_POINT",
                                                    "cost": 1,
                                                    "bfd": {
                                                        "bfd_status": "enabled",
                                                        "interval": 150,
                                                        "multi": 3,
                                                        "mode": "Default",
                                                    },
                                                    "transmit_delay": 1,
                                                    "state": "POINT_TO_POINT",
                                                    "hello_interval": 10,
                                                    "dead_interval": 40,
                                                    "wait_interval": 40,
                                                    "retransmit_interval": 5,
                                                    "hello_timer": "00:00:08",
                                                    "index": "1/2/2",
                                                    "flood_queue_length": 0,
                                                    "next": "0(0)/0(0)/0(0)",
                                                    "last_flood_scan_length": 1,
                                                    "max_flood_scan_length": 4,
                                                    "last_flood_scan_time_msec": 0,
                                                    "max_flood_scan_time_msec": 0,
                                                    "statistics": {
                                                        "nbr_count": 1,
                                                        "adj_nbr_count": 1,
                                                        "neighbor": "95.95.95.95",
                                                        "num_nbrs_suppress_hello": 0,
                                                        "refrence_count": 6,
                                                    },
                                                    "neighbors": {
                                                        "100.100.100.100": {
                                                            "nbr_count": 1,
                                                            "adj_nbr_count": 1,
                                                        },
                                                        "95.95.95.95": {
                                                            "nbr_count": 1,
                                                            "adj_nbr_count": 1,
                                                        },
                                                    },
                                                },
                                                "Loopback0": {},
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
