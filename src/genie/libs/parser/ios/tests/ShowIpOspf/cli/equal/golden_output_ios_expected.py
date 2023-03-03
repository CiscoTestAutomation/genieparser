expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "1": {
                            "start_time": "00:00:20.892",
                            "enable": True,
                            "interface_flood_pacing_timer": 33,
                            "areas": {
                                "0.0.0.1": {
                                    "ranges": {},
                                    "area_id": "0.0.0.1",
                                    "area_type": "normal",
                                    "statistics": {
                                        "flood_list_length": 0,
                                        "dcbitless_lsa_count": 1,
                                        "area_scope_lsa_cksum_sum": "0x0D8C1F",
                                        "area_scope_opaque_lsa_count": 0,
                                        "area_scope_opaque_lsa_cksum_sum": "0x000000",
                                        "spf_runs_count": 3,
                                        "indication_lsa_count": 1,
                                        "area_scope_lsa_count": 28,
                                        "donotage_lsa_count": 0,
                                        "spf_last_executed": "6d06h",
                                        "interfaces_count": 1,
                                    },
                                },
                                "0.0.0.0": {
                                    "ranges": {},
                                    "area_id": "0.0.0.0",
                                    "area_type": "normal",
                                    "statistics": {
                                        "area_scope_lsa_cksum_sum": "0x0848BC",
                                        "dcbitless_lsa_count": 11,
                                        "indication_lsa_count": 0,
                                        "area_scope_opaque_lsa_count": 0,
                                        "area_scope_lsa_count": 14,
                                        "flood_list_length": 0,
                                        "loopback_count": 1,
                                        "spf_runs_count": 8,
                                        "interfaces_count": 3,
                                        "donotage_lsa_count": 0,
                                        "spf_last_executed": "6d06h",
                                        "area_scope_opaque_lsa_cksum_sum": "0x000000",
                                    },
                                },
                            },
                            "event_log": {
                                "mode": "cyclic",
                                "max_events": 1000,
                                "enable": True,
                            },
                            "redistribution": {
                                "static": {"subnets": "subnets", "enabled": True},
                                "max_prefix": {
                                    "num_of_prefix": 5000,
                                    "prefix_thld": 90,
                                    "warn_only": True,
                                    },
                                "connected": {"subnets": "subnets", "enabled": True},
                            },
                            "nssa": True,
                            "total_areas_transit_capable": 0,
                            "bfd": {"enable": False},
                            "total_areas": 2,
                            "lls": True,
                            "graceful_restart": {
                                "ietf": {
                                    "helper_enable": True,
                                    "type": "ietf",
                                    "enable": False,
                                },
                                "cisco": {
                                    "helper_enable": True,
                                    "type": "cisco",
                                    "enable": False,
                                },
                            },
                            "external_flood_list_length": 0,
                            "nsr": {"enable": False},
                            "retransmission_pacing_timer": 66,
                            "db_exchange_summary_list_optimization": True,
                            "lsa_group_pacing_timer": 240,
                            "total_nssa_areas": 0,
                            "router_id": "10.1.1.1",
                            "total_stub_areas": 0,
                            "area_transit": True,
                            "stub_router": {
                                "always": {
                                    "external_lsa": False,
                                    "always": False,
                                    "include_stub": False,
                                    "summary_lsa": False,
                                }
                            },
                            "auto_cost": {
                                "enable": False,
                                "reference_bandwidth": 100,
                                "bandwidth_unit": "mbps",
                            },
                            "adjacency_stagger": {
                                "initial_number": 300,
                                "maximum_number": 300,
                            },
                            "database_control": {
                                "max_lsa_current": 0,
                                "max_lsa": 123,
                                "max_lsa_ignore_time": 300,
                                "max_lsa_reset_time": 600,
                                "max_lsa_ignore_count": 5,
                                "max_lsa_warning_only": False,
                                "max_lsa_current_count": 0,
                                "max_lsa_limit": 5000,
                                "max_lsa_threshold_value": 75,
                            },
                            "spf_control": {
                                "incremental_spf": False,
                                "throttle": {
                                    "lsa": {"arrival": 1000},
                                    "spf": {
                                        "maximum": 10000,
                                        "start": 5000,
                                        "hold": 10000,
                                    },
                                },
                            },
                            "elapsed_time": "6d06h",
                            "opqaue_lsa": True,
                            "total_normal_areas": 2,
                            "numbers": {
                                "dc_bitless": 0,
                                "opaque_as_lsa_checksum": "0x000000",
                                "external_lsa": 0,
                                "opaque_as_lsa": 0,
                                "do_not_age": 0,
                                "external_lsa_checksum": "0x000000",
                            },
                            "flags": {"abr": True},
                        }
                    }
                }
            }
        }
    }
}
