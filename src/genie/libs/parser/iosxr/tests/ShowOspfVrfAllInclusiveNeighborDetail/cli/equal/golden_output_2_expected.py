

expected_output = {
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
