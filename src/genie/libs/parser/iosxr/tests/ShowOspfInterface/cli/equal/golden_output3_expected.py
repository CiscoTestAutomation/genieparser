expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "4": {
                            "interfaces": {
                                "TenGigE0/7/0/1": {
                                    "name": "TenGigE0/7/0/1",
                                    "demand_circuit": False,
                                    "enable": True,
                                    "line_protocol": True,
                                    "bfd": {
                                        "enable": False
                                    },
                                    "ip_address": "172.30.138.1/30",
                                    "area": "0",
                                    "label_stack": {
                                        "primary_label": "1",
                                        "backup_label": "3",
                                        "srte_label": "10",
                                    },
                                    'ldp_status': {
                                        'ldp_sync': 'Enabled',
                                        'sync_status': 'Achieved'
                                    },
                                    "process_id": "4",
                                    "router_id": "221.132.195.51",
                                    "interface_type": "POINT_TO_POINT",
                                    "cost": 10,
                                    "transmit_delay": 1,
                                    "state": "POINT_TO_POINT",
                                    "mtu": 9000,
                                    "max_pkt_sz": 9000,
                                    "forward_reference": "No",
                                    "unnumbered": False,
                                    "bandwidth": 10000000,
                                    "hello_interval": 10,
                                    "dead_interval": 40,
                                    "wait_interval": 40,
                                    "retransmit_interval": 5,
                                    "nsf_enabled": True,
                                    "hello_timer": "00:00:00:676",
                                    "index": "4/4",
                                    "flood_queue_length": 0,
                                    "next": "0(0)/0(0)",
                                    "last_flood_scan_length": 1,
                                    "max_flood_scan_length": 4,
                                    "last_flood_scan_time_msec": 0,
                                    "max_flood_scan_time_msec": 0,
                                    "ls_ack_list": "current",
                                    "ls_ack_list_length": 0,
                                    "high_water_mark": 5,
                                    "statistics": {
                                        "nbr_count": 1,
                                        "adj_nbr_count": 1,
                                        "num_nbrs_suppress_hello": 0,
                                        "multi_area_intf_count": 0,
                                    },
                                    "neighbors": {
                                        "221.132.195.58": {
                                            "router_id": "221.132.195.58"
                                        }
                                    },
                                    "authentication": {
                                        "auth_trailer_key": {
                                            "crypto_algorithm": "md5",
                                            "youngest_key_id": 1,
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
