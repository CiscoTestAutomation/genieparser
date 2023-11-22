expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "1": {
                            "interfaces": {
                                "GigabitEthernet0/2/0/1": {
                                    "name": "GigabitEthernet0/2/0/1",
                                    "demand_circuit": False,
                                    "enable": True,
                                    "line_protocol": True,
                                    "bfd": {
                                        "enable": False
                                    },
                                    "ip_address": "121.10.10.2/24",
                                    "area": "2",
                                    "process_id": "1",
                                    "router_id": "200.2.2.2",
                                    "interface_type": "POINT_TO_POINT",
                                    "cost": 1,
                                    "transmit_delay": 1,
                                    "state": "POINT_TO_POINT",
                                    "hello_interval": 10,
                                    "dead_interval": 40,
                                    "wait_interval": 40,
                                    "retransmit_interval": 5,
                                    "hello_timer": "00:00:04",
                                    "index": "1/3",
                                    "flood_queue_length": 0,
                                    "next": "0(0)/0(0)",
                                    "last_flood_scan_length": 3,
                                    "max_flood_scan_length": 10,
                                    "last_flood_scan_time_msec": 0,
                                    "max_flood_scan_time_msec": 0,
                                    "statistics": {
                                        "nbr_count": 1,
                                        "adj_nbr_count": 1,
                                        "num_nbrs_suppress_hello": 0,
                                        "multi_area_intf_count": 1,
                                    },
                                    "neighbors": {
                                        "101.3.3.3": {"router_id": "101.3.3.3"}
                                    },
                                },
                                "GigabitEthernet0/3/0/0": {
                                    "name": "GigabitEthernet0/3/0/0",
                                    "demand_circuit": False,
                                    "enable": True,
                                    "line_protocol": True,
                                    "bfd": {
                                        "enable": True,
                                        "interval": 15,
                                        "multiplier": 3,
                                    },
                                    "ip_address": "145.10.10.2/16",
                                    "area": "3",
                                    "process_id": "1",
                                    "router_id": "200.2.2.2",
                                    "interface_type": "POINT_TO_POINT",
                                    "cost": 1,
                                    "transmit_delay": 1,
                                    "state": "POINT_TO_POINT",
                                    "hello_interval": 10,
                                    "dead_interval": 40,
                                    "wait_interval": 40,
                                    "retransmit_interval": 5,
                                    "index": "1/5",
                                    "flood_queue_length": 0,
                                    "next": "0(0)/0(0)",
                                    "last_flood_scan_length": 3,
                                    "max_flood_scan_length": 11,
                                    "last_flood_scan_time_msec": 0,
                                    "max_flood_scan_time_msec": 1,
                                    "statistics": {
                                        "nbr_count": 1,
                                        "adj_nbr_count": 1,
                                        "num_nbrs_suppress_hello": 0,
                                        "multi_area_intf_count": 0,
                                    },
                                    "neighbors": {
                                        "101.3.3.3": {"router_id": "101.3.3.3"}
                                    },
                                    "authentication": {
                                        "auth_trailer_key": {
                                            "crypto_algorithm": "md5",
                                            "youngest_key_id": 1,
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
