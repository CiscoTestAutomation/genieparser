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
                                                    "enable": "up",
                                                    "line_protocol": "up",
                                                    "link_local_address": "fe80:100:10::1",
                                                    "interface_id": 7,
                                                    "router_id": "10.94.1.1",
                                                    "network_type": "POINT_TO_POINT",
                                                    "cost": 1,
                                                    "bfd": {
                                                        "bfd_status": "enabled",
                                                        "interval": 150,
                                                        "multiplier": 3,
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
                                                        "num_nbrs_suppress_hello": 0,
                                                        "refrence_count": 6,
                                                    },
                                                    "adjacent_neighbors": {
                                                        "nbr_count": 1,
                                                        "adj_nbr_count": 1,
                                                        "neighbor": "10.220.100.100",
                                                    },
                                                },
                                                "Loopback0": {
                                                    "enable": "up",
                                                    "line_protocol": "up",
                                                    "link_local_address": "fe80::8849:faff:fe9c:f9b6",
                                                    "interface_id": 6,
                                                    "router_id": "10.94.1.1",
                                                    "network_type": "LOOPBACK",
                                                    "cost": 0,
                                                    "loopback_txt": "Loopback interface is treated as a stub Host",
                                                },
                                                "GigabitEthernet0/0/0/1": {
                                                    "enable": "up",
                                                    "line_protocol": "up",
                                                    "link_local_address": "fe80:100:20::1",
                                                    "interface_id": 8,
                                                    "router_id": "10.94.1.1",
                                                    "network_type": "POINT_TO_POINT",
                                                    "cost": 1,
                                                    "bfd": {
                                                        "bfd_status": "enabled",
                                                        "interval": 150,
                                                        "multiplier": 3,
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
                                                        "num_nbrs_suppress_hello": 0,
                                                        "refrence_count": 6,
                                                    },
                                                    "adjacent_neighbors": {
                                                        "nbr_count": 1,
                                                        "adj_nbr_count": 1,
                                                        "neighbor": "10.145.95.95",
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
        }
    }
}
