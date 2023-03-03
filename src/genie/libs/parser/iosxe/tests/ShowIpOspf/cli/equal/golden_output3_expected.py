expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "1": {
                            "router_id": "2.2.2.2",
                            "enable": True,
                            "nsr": {"enable": False},
                            "bfd": {"enable": False},
                            "start_time": "00:07:57.265",
                            "elapsed_time": "8w5d",
                            "opqaue_lsa": True,
                            "lls": True,
                            "area_transit": True,
                            "nssa": True,
                            "db_exchange_summary_list_optimization": True,
                            "database_control": {
                                "max_lsa": 1000000,
                                "max_lsa_current": 9,
                                "max_lsa_threshold_value": 60,
                                "max_lsa_ignore_time": 600,
                                "max_lsa_reset_time": 2640,
                                "max_lsa_ignore_count": 22,
                                "max_lsa_current_count": 0,
                                "max_lsa_limit": 312321312,
                                "max_lsa_warning_only": False,
                            },
                            "event_log": {
                                "enable": True,
                                "max_events": 1000,
                                "mode": "cyclic",
                            },
                            "flags": {
                                "abr": True, 
                                "asbr": True
                                },
                            "redistribution": {
                                "connected": {
                                    "enabled": True, 
                                    "subnets": "subnets"
                                    },
                                "max_prefix": {
                                    "num_of_prefix": 312321312,
                                    "warn_only": True,
                                    "prefix_thld": 90,
                                },
                            },
                            "stub_router": {
                                "always": {
                                    "always": False,
                                    "include_stub": False,
                                    "summary_lsa": False,
                                    "external_lsa": False,
                                }
                            },
                            "spf_control": {
                                "throttle": {
                                    "spf": {
                                        "start": 50, 
                                        "hold": 200, 
                                        "maximum": 5000
                                        },
                                    "lsa": {
                                        "start": 50,
                                        "hold": 200,
                                        "maximum": 5000,
                                        "arrival": 100,
                                    },
                                },
                                "incremental_spf": False,
                            },
                            "lsa_group_pacing_timer": 240,
                            "interface_flood_pacing_timer": 33,
                            "retransmission_pacing_timer": 66,
                            "adjacency_stagger": {
                                "initial_number": 300,
                                "maximum_number": 300,
                            },
                            "numbers": {
                                "external_lsa": 7,
                                "external_lsa_checksum": "0x029C32",
                                "opaque_as_lsa": 0,
                                "opaque_as_lsa_checksum": "0x000000",
                                "dc_bitless": 0,
                                "do_not_age": 0,
                            },
                            "total_areas": 2,
                            "total_normal_areas": 2,
                            "total_stub_areas": 0,
                            "total_nssa_areas": 0,
                            "total_areas_transit_capable": 0,
                            "external_flood_list_length": 0,
                            "graceful_restart": {
                                "ietf": {
                                    "type": "ietf",
                                    "helper_enable": True,
                                    "enable": False,
                                },
                                "cisco": {
                                    "type": "cisco",
                                    "helper_enable": True,
                                    "enable": False,
                                },
                            },
                            "auto_cost": {
                                "reference_bandwidth": 100,
                                "bandwidth_unit": "mbps",
                                "enable": False,
                            },
                            "areas": {
                                "0.0.0.0": {
                                    "area_id": "0.0.0.0",
                                    "area_type": "normal",
                                    "statistics": {
                                        "interfaces_count": 1,
                                        "spf_last_executed": "3w3d",
                                        "spf_runs_count": 14,
                                        "area_scope_lsa_count": 7,
                                        "area_scope_lsa_cksum_sum": "0x03BF96",
                                        "area_scope_opaque_lsa_count": 0,
                                        "area_scope_opaque_lsa_cksum_sum": "0x000000",
                                        "dcbitless_lsa_count": 0,
                                        "indication_lsa_count": 0,
                                        "donotage_lsa_count": 0,
                                        "flood_list_length": 0,
                                    },
                                    "ranges": {},
                                },
                                "0.0.0.2": {
                                    "area_id": "0.0.0.2",
                                    "area_type": "normal",
                                    "statistics": {
                                        "interfaces_count": 1,
                                        "spf_last_executed": "3w3d",
                                        "spf_runs_count": 7,
                                        "area_scope_lsa_count": 7,
                                        "area_scope_lsa_cksum_sum": "0x041251",
                                        "area_scope_opaque_lsa_count": 0,
                                        "area_scope_opaque_lsa_cksum_sum": "0x000000",
                                        "dcbitless_lsa_count": 0,
                                        "indication_lsa_count": 0,
                                        "donotage_lsa_count": 0,
                                        "flood_list_length": 0,
                                    },
                                    "ranges": {},
                                },
                            },
                        }
                    }
                }
            }
        }
    }
}