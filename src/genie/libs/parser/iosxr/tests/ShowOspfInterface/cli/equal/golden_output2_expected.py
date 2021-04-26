schema = {
        "vrf": {
            'default': {  # VRF information, if no, assign "default"
                "address_family": {
                    'ipv4': {  # IPv4 as initial value
                        "instance": {
                            'mpls1': {  # here is ospf name
                                "interfaces": {
                                    'Loopback0': {
                                        "name": 'Loopback0',
                                        "enable": True,
                                        "line_protocol": True,
                                        "ip_address": '25.97.1.1/32',
                                        "demand_circuit": False,
                                        "process_id": 'mpls1',
                                        "router_id": '25.97.1.1',
                                        "interface_type": 'LOOPBACK',
                                        "area": '0',
                                        "bfd": {
                                            "enable": False,
                                        },
                                        "label_stack": {
                                            "primary_label": '0',
                                            "backup_label": '0',
                                            "srte_label": '0',
                                        },
                                        "sid": '0',
                                        "strict_spf_sid": '0',
                                        "cost": 1,
                                        Optional("state"): str,
                                        Optional("priority"): int,
                                        Optional("mtu"): int,
                                        Optional("max_pkt_sz"): int,
                                        Optional("dr_router_id"): str,
                                        Optional("dr_ip_addr"): str,
                                        Optional("bdr_router_id"): str,
                                        Optional("bdr_ip_addr"): str,
                                        Optional("hello_interval"): int,
                                        Optional("dead_interval"): int,
                                        Optional("wait_interval"): int,
                                        Optional("retransmit_interval"): int,
                                        Optional("passive"): bool,
                                        Optional("hello_timer"): str,
                                        Optional("index"): str,
                                        Optional("flood_queue_length"): int,
                                        Optional("next"): str,
                                        Optional("last_flood_scan_length"): int,
                                        Optional("max_flood_scan_length"): int,
                                        Optional(
                                            "last_flood_scan_time_msec"
                                        ): int,
                                        Optional(
                                            "max_flood_scan_time_msec"
                                        ): int,
                                        Optional("ls_ack_list"): str,
                                        Optional("ls_ack_list_length"): int,
                                        Optional("high_water_mark"): int,
                                        Optional("total_dcbitless_lsa"): int,
                                        Optional("donotage_lsa"): bool,
                                        Optional("statistics"): {
                                            Optional("adj_nbr_count"): int,
                                            Optional("nbr_count"): int,
                                            Optional(
                                                "num_nbrs_suppress_hello"
                                            ): int,
                                            Optional(
                                                "multi_area_intf_count"
                                            ): int,
                                        },
                                        Optional("neighbors"): list
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }