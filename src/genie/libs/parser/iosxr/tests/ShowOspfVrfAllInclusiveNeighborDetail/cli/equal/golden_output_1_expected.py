
expected_output = {
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
