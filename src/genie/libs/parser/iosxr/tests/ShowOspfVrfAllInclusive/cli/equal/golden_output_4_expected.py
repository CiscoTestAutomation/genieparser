expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "1": {
                            "router_id": "3.3.3.3",
                            "role": "primary active",
                            "nsr": {
                                "enable": True
                            },
                            "database_control": {
                                "max_lsa": 500000,
                                "current_lsa": 4,
                                "threshold": 75,
                                "ignore_time": 5,
                                "reset_time": 10,
                                "allowed_ignore_count": 5,
                                "current_ignore_count": 0
                            },
                            "suppress_neighbor": {
                                "max_external_prefix": 50000,
                                "warning_threshold": 75
                            },
                            "stub_router": {
                                "always": {
                                    "always": False,
                                    "include_stub": False,
                                    "summary_lsa": False,
                                    "external_lsa": False
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
                                        "interval": 200,
                                        "arrival": 100,
                                        "refresh_interval": 1800
                                    }
                                }
                            },
                            "flood_pacing_interval_msec": 33,
                            "retransmission_pacing_interval": 66,
                            "adjacency_stagger": {
                                "disable": False,
                                "initial_number": 2,
                                "maximum_number": 64,
                                "nbrs_forming": 0,
                                "nbrs_full": 1
                            },
                            "maximum_interfaces": 1024,
                            "numbers": {
                                "external_lsa": 0,
                                "external_lsa_checksum": "00000000",
                                "opaque_as_lsa": 0,
                                "opaque_as_lsa_checksum": "00000000",
                                "dc_bitless": 0,
                                "do_not_age": 0
                            },
                            "total_areas": 1,
                            "total_normal_areas": 1,
                            "total_stub_areas": 0,
                            "total_nssa_areas": 0,
                            "external_flood_list_length": 0,
                            "snmp_trap": True,
                            "lsd_state": "not connected",
                            "lsd_revision": 0,
                            "segment_routing_global_block_default": "16000-23999",
                            "segment_routing_global_block_status": "not allocated",
                            "strict_spf": True,
                            "areas": {
                                "0.0.0.0": {
                                    "area_id": "0.0.0.0",
                                    "area_type": "normal",
                                    "statistics": {
                                        "interfaces_count": 2,
                                        "spf_runs_count": 24,
                                        "area_scope_lsa_count": 5,
                                        "area_scope_lsa_cksum_sum": "0x028706",
                                        "area_scope_opaque_lsa_count": 0,
                                        "area_scope_opaque_lsa_cksum_sum": "00000000",
                                        "dcbitless_lsa_count": 0,
                                        "indication_lsa_count": 0,
                                        "donotage_lsa_count": 0,
                                        "flood_list_length": 0,
                                        "lfa_interface_count": 0,
                                        "lfa_revision": 0,
                                        "lfa_per_prefix_interface_count": 0,
                                        "nbrs_staggered_mode": 0,
                                        "nbrs_full": 1
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

