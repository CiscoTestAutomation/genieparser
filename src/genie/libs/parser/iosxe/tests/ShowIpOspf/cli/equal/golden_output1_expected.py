expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "1": {
                            "adjacency_stagger": {
                                "initial_number": 300,
                                "maximum_number": 300,
                            },
                            "area_transit": True,
                            "enable": True,
                            "areas": {
                                "0.0.0.0": {
                                    "area_id": "0.0.0.0",
                                    "area_type": "normal",
                                    "ranges": {
                                        "10.4.0.0/16": {
                                            "advertise": True,
                                            "cost": 10,
                                            "prefix": "10.4.0.0/16",
                                        }
                                    },
                                    "rrr_enabled": True,
                                    "statistics": {
                                        "area_scope_lsa_cksum_sum": "0x07CF20",
                                        "area_scope_lsa_count": 19,
                                        "area_scope_opaque_lsa_cksum_sum": "0x000000",
                                        "area_scope_opaque_lsa_count": 0,
                                        "dcbitless_lsa_count": 5,
                                        "donotage_lsa_count": 0,
                                        "flood_list_length": 0,
                                        "indication_lsa_count": 0,
                                        "interfaces_count": 3,
                                        "loopback_count": 1,
                                        "spf_last_executed": "00:19:54.849",
                                        "spf_runs_count": 41,
                                    },
                                }
                            },
                            "auto_cost": {
                                "bandwidth_unit": "mbps",
                                "enable": False,
                                "reference_bandwidth": 100,
                            },
                            "bfd": {"enable": True, "strict_mode": True},
                            "database_control": {"max_lsa": 123},
                            "db_exchange_summary_list_optimization": True,
                            "elapsed_time": "1d01h",
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
                            "lls": True,
                            "lsa_group_pacing_timer": 240,
                            "nsr": {"enable": False},
                            "nssa": True,
                            "numbers": {
                                "dc_bitless": 0,
                                "do_not_age": 0,
                                "external_lsa": 1,
                                "external_lsa_checksum": "0x007F60",
                                "opaque_as_lsa": 0,
                                "opaque_as_lsa_checksum": "0x000000",
                            },
                            "opqaue_lsa": True,
                            "interface_flood_pacing_timer": 33,
                            "retransmission_pacing_timer": 66,
                            "router_id": "10.4.1.1",
                            "spf_control": {
                                "incremental_spf": False,
                                "throttle": {
                                    "lsa": {
                                        "arrival": 100,
                                        "hold": 200,
                                        "maximum": 5000,
                                        "start": 50,
                                    },
                                    "spf": {"hold": 200, "maximum": 5000, "start": 50},
                                },
                            },
                            "start_time": "00:23:49.050",
                            "stub_router": {
                                "always": {
                                    "always": False,
                                    "external_lsa": False,
                                    "include_stub": False,
                                    "summary_lsa": False,
                                }
                            },
                            "total_areas": 1,
                            "total_areas_transit_capable": 0,
                            "total_normal_areas": 1,
                            "total_nssa_areas": 0,
                            "total_stub_areas": 0,
                        },
                        "2": {
                            "adjacency_stagger": {
                                "initial_number": 300,
                                "maximum_number": 300,
                            },
                            "area_transit": True,
                            "enable": False,
                            "areas": {
                                "0.0.0.1": {
                                    "area_id": "0.0.0.1",
                                    "area_type": "normal",
                                    "ranges": {
                                        "10.4.1.0/24": {
                                            "advertise": True,
                                            "prefix": "10.4.1.0/24",
                                        }
                                    },
                                    "statistics": {
                                        "area_scope_lsa_cksum_sum": "0x053FED",
                                        "area_scope_lsa_count": 11,
                                        "area_scope_opaque_lsa_cksum_sum": "0x000000",
                                        "area_scope_opaque_lsa_count": 0,
                                        "dcbitless_lsa_count": 1,
                                        "donotage_lsa_count": 0,
                                        "flood_list_length": 0,
                                        "indication_lsa_count": 0,
                                        "interfaces_count": 2,
                                        "spf_last_executed": "03:26:37.769",
                                        "spf_runs_count": 97,
                                    },
                                }
                            },
                            "auto_cost": {
                                "bandwidth_unit": "mbps",
                                "enable": False,
                                "reference_bandwidth": 100,
                            },
                            "bfd": {"enable": True},
                            "db_exchange_summary_list_optimization": True,
                            "domain_id_type": "0x0005",
                            "domain_id_value": "0.0.0.2",
                            "elapsed_time": "23:34:42.224",
                            "external_flood_list_length": 0,
                            "flags": {"abr": True, "asbr": True},
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
                            "lls": True,
                            "lsa_group_pacing_timer": 240,
                            "nsr": {"enable": True},
                            "nssa": True,
                            "numbers": {
                                "dc_bitless": 0,
                                "do_not_age": 0,
                                "external_lsa": 0,
                                "external_lsa_checksum": "0x000000",
                                "opaque_as_lsa": 0,
                                "opaque_as_lsa_checksum": "0x000000",
                            },
                            "opqaue_lsa": True,
                            "redistribution": {
                                "bgp": {"bgp_id": 100, "subnets": "subnets"}
                            },
                            "interface_flood_pacing_timer": 33,
                            "retransmission_pacing_timer": 66,
                            "router_id": "10.229.11.11",
                            "spf_control": {
                                "incremental_spf": False,
                                "throttle": {
                                    "lsa": {
                                        "arrival": 100,
                                        "hold": 200,
                                        "maximum": 5000,
                                        "start": 50,
                                    },
                                    "spf": {"hold": 200, "maximum": 5000, "start": 50},
                                },
                            },
                            "start_time": "02:17:25.010",
                            "stub_router": {
                                "always": {
                                    "always": False,
                                    "external_lsa": False,
                                    "include_stub": False,
                                    "summary_lsa": False,
                                }
                            },
                            "total_areas": 1,
                            "total_areas_transit_capable": 0,
                            "total_normal_areas": 1,
                            "total_nssa_areas": 0,
                            "total_stub_areas": 0,
                        },
                    }
                }
            }
        }
    }
}
