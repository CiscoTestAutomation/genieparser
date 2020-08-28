expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "65109": {
                            "adjacency_stagger": {
                                "initial_number": 300,
                                "maximum_number": 300,
                            },
                            "area_transit": True,
                            "areas": {
                                "0.0.0.8": {
                                    "area_id": "0.0.0.8",
                                    "area_type": "normal",
                                    "ranges": {},
                                    "statistics": {
                                        "area_scope_lsa_cksum_sum": "0x07FAE2",
                                        "area_scope_lsa_count": 21,
                                        "area_scope_opaque_lsa_cksum_sum": "0x000000",
                                        "area_scope_opaque_lsa_count": 0,
                                        "dcbitless_lsa_count": 0,
                                        "donotage_lsa_count": 0,
                                        "flood_list_length": 0,
                                        "indication_lsa_count": 0,
                                        "interfaces_count": 2,
                                        "loopback_count": 1,
                                        "spf_last_executed": "13:02:02.080",
                                        "spf_runs_count": 8,
                                    },
                                }
                            },
                            "auto_cost": {
                                "bandwidth_unit": "mbps",
                                "enable": True,
                                "reference_bandwidth": 2488,
                            },
                            "bfd": {"enable": False},
                            "db_exchange_summary_list_optimization": True,
                            "elapsed_time": "13:07:02.634",
                            "enable": True,
                            "event_log": {
                                "enable": True,
                                "max_events": 1000,
                                "mode": "cyclic",
                            },
                            "external_flood_list_length": 0,
                            "graceful_restart": {
                                "cisco": {
                                    "enable": False,
                                    "helper_enable": True,
                                    "type": "cisco",
                                },
                                "ietf": {
                                    "enable": False,
                                    "helper_enable": True,
                                    "type": "ietf",
                                },
                            },
                            "interface_flood_pacing_timer": 33,
                            "lls": True,
                            "lsa_group_pacing_timer": 240,
                            "nsr": {"enable": False},
                            "nssa": True,
                            "numbers": {
                                "dc_bitless": 0,
                                "do_not_age": 0,
                                "external_lsa": 2,
                                "external_lsa_checksum": "0x00F934",
                                "opaque_as_lsa": 0,
                                "opaque_as_lsa_checksum": "0x000000",
                            },
                            "opqaue_lsa": True,
                            "retransmission_pacing_timer": 66,
                            "router_id": "10.169.197.254",
                            "spf_control": {
                                "incremental_spf": False,
                                "throttle": {
                                    "lsa": {
                                        "arrival": 100,
                                        "hold": 200,
                                        "maximum": 5000,
                                        "start": 50,
                                    },
                                    "spf": {
                                        "hold": 3000,
                                        "maximum": 3000,
                                        "start": 500,
                                    },
                                },
                            },
                            "start_time": "00:02:39.151",
                            "stub_router": {
                                "on_startup": {
                                    "include_stub": True,
                                    "on_startup": 300,
                                    "state": "inactive",
                                }
                            },
                            "total_areas": 1,
                            "total_areas_transit_capable": 0,
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
