expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "51": {
                            "interfaces": {
                                "Bundle-Ether63001": {
                                    "name": "Bundle-Ether63001",
                                    "demand_circuit": False,
                                    "enable": True,
                                    "line_protocol": True,
                                    "bfd": {
                                        "enable": False
                                    },
                                    "ip_address": "172.25.12.129/31",
                                    "area": "0",
                                    "sid": "0",
                                    "strict_spf_sid": "0",
                                    "label_stack": {
                                        "primary_label": "1",
                                        "backup_label": "3",
                                        "srte_label": "10"
                                    },
                                    "process_id": "51",
                                    "router_id": "172.25.12.4",
                                    "interface_type": "POINT_TO_POINT",
                                    "cost": 10,
                                    "ldp_status": {
                                        "ldp_sync": "Enabled",
                                        "sync_status": "Achieved"
                                    },
                                    "transmit_delay": 1,
                                    "state": "POINT_TO_POINT",
                                    "mtu": 9164,
                                    "max_pkt_sz": 9000,
                                    "forward_reference": "No",
                                    "unnumbered": False,
                                    "bandwidth": 10000000,
                                    "hello_interval": 10,
                                    "dead_interval": 40,
                                    "wait_interval": 40,
                                    "retransmit_interval": 5,
                                    "hello_timer": "00:00:04:871",
                                    "index": "2/2",
                                    "flood_queue_length": 0,
                                    "next": "0(0)/0(0)",
                                    "last_flood_scan_length": 8,
                                    "max_flood_scan_length": 8,
                                    "last_flood_scan_time_msec": 0,
                                    "max_flood_scan_time_msec": 0,
                                    "ls_ack_list": "current",
                                    "ls_ack_list_length": 0,
                                    "high_water_mark": 44,
                                    "statistics": {
                                        "nbr_count": 1,
                                        "adj_nbr_count": 1,
                                        "num_nbrs_suppress_hello": 0,
                                        "multi_area_intf_count": 0
                                    },
                                    "neighbors": {
                                        "172.25.12.2": {
                                            "router_id": "172.25.12.2"
                                        }
                                    },
                                    "authentication": {
                                        "auth_trailer_key": {
                                            "crypto_algorithm": "md5",
                                            "youngest_key_id": 1
                                        }
                                    }
                                },
                                "Bundle-Ether63002": {
                                    "name": "Bundle-Ether63002",
                                    "demand_circuit": False,
                                    "enable": True,
                                    "line_protocol": True,
                                    "bfd": {
                                        "enable": False
                                    },
                                    "ip_address": "172.25.12.131/31",
                                    "area": "0",
                                    "sid": "0",
                                    "strict_spf_sid": "0",
                                    "label_stack": {
                                        "primary_label": "1",
                                        "backup_label": "3",
                                        "srte_label": "10"
                                    },
                                    "process_id": "51",
                                    "router_id": "172.25.12.4",
                                    "interface_type": "POINT_TO_POINT",
                                    "cost": 10,
                                    "ldp_status": {
                                        "ldp_sync": "Enabled",
                                        "sync_status": "Achieved"
                                    },
                                    "transmit_delay": 1,
                                    "state": "POINT_TO_POINT",
                                    "mtu": 9164,
                                    "max_pkt_sz": 9000,
                                    "forward_reference": "No",
                                    "unnumbered": False,
                                    "bandwidth": 10000000,
                                    "hello_interval": 10,
                                    "dead_interval": 40,
                                    "wait_interval": 40,
                                    "retransmit_interval": 5,
                                    "hello_timer": "00:00:02:836",
                                    "index": "3/3",
                                    "flood_queue_length": 0,
                                    "next": "0(0)/0(0)",
                                    "last_flood_scan_length": 2,
                                    "max_flood_scan_length": 6,
                                    "last_flood_scan_time_msec": 0,
                                    "max_flood_scan_time_msec": 0,
                                    "ls_ack_list": "current",
                                    "ls_ack_list_length": 0,
                                    "high_water_mark": 43,
                                    "statistics": {
                                        "nbr_count": 1,
                                        "adj_nbr_count": 1,
                                        "num_nbrs_suppress_hello": 0,
                                        "multi_area_intf_count": 0
                                    },
                                    "neighbors": {
                                        "172.25.12.3": {
                                            "router_id": "172.25.12.3"
                                        }
                                    },
                                    "authentication": {
                                        "auth_trailer_key": {
                                            "crypto_algorithm": "md5",
                                            "youngest_key_id": 1
                                        }
                                    }
                                },
                                "Loopback0": {
                                    "name": "Loopback0",
                                    "demand_circuit": False,
                                    "enable": True,
                                    "line_protocol": True,
                                    "bfd": {
                                        "enable": False
                                    },
                                    "ip_address": "172.25.12.4/32",
                                    "area": "0",
                                    "sid": "0",
                                    "strict_spf_sid": "0",
                                    "label_stack": {
                                        "primary_label": "0",
                                        "backup_label": "0",
                                        "srte_label": "0"
                                    },
                                    "process_id": "51",
                                    "router_id": "172.25.12.4",
                                    "interface_type": "LOOPBACK",
                                    "cost": 1,
                                    "treated_as_stub_host": True
                                },
                                "tunnel-te10100": {
                                    "name": "tunnel-te10100",
                                    "demand_circuit": False,
                                    "enable": True,
                                    "line_protocol": True,
                                    "bfd": {
                                        "enable": False
                                    },
                                    "ip_address": "0.0.0.0/0",
                                    "area": "0",
                                    "sid": "0",
                                    "strict_spf_sid": "0",
                                    "label_stack": {
                                        "primary_label": "0",
                                        "backup_label": "0",
                                        "srte_label": "0"
                                    },
                                    "process_id": "51",
                                    "router_id": "172.25.12.4",
                                    "interface_type": "POINT_TO_POINT",
                                    "transmit_delay": 1,
                                    "state": "POINT_TO_POINT",
                                    "mtu": 0,
                                    "max_pkt_sz": 576,
                                    "forward_reference": "No",
                                    "unnumbered": False,
                                    "bandwidth": 100000,
                                    "hello_interval": 10,
                                    "dead_interval": 40,
                                    "wait_interval": 0,
                                    "retransmit_interval": 5,
                                    "passive": True,
                                    "index": "0/0",
                                    "flood_queue_length": 0,
                                    "next": "0(0)/0(0)",
                                    "last_flood_scan_length": 0,
                                    "max_flood_scan_length": 0,
                                    "last_flood_scan_time_msec": 0,
                                    "max_flood_scan_time_msec": 0,
                                    "ls_ack_list": "current",
                                    "ls_ack_list_length": 0,
                                    "high_water_mark": 0,
                                    "statistics": {
                                        "nbr_count": 0,
                                        "adj_nbr_count": 0,
                                        "num_nbrs_suppress_hello": 0,
                                        "multi_area_intf_count": 0
                                    },
                                    "neighbors": {},
                                    "authentication": {
                                        "auth_trailer_key": {
                                            "crypto_algorithm": "md5",
                                            "youngest_key_id": 1
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