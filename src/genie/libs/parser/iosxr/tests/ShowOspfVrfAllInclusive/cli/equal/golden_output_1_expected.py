
expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "1": {
                            "adjacency_stagger": {
                                "disable": False,
                                "initial_number": 2,
                                "maximum_number": 64,
                                "nbrs_forming": 0,
                                "nbrs_full": 1,
                            },
                            "areas": {
                                "0.0.0.1": {
                                    "area_type": "normal",
                                    "area_id": "0.0.0.1",
                                    "statistics": {
                                        "area_scope_lsa_cksum_sum": "0x04f437",
                                        "area_scope_lsa_count": 11,
                                        "area_scope_opaque_lsa_cksum_sum": "00000000",
                                        "area_scope_opaque_lsa_count": 0,
                                        "dcbitless_lsa_count": 1,
                                        "donotage_lsa_count": 0,
                                        "flood_list_length": 0,
                                        "indication_lsa_count": 0,
                                        "interfaces_count": 2,
                                        "lfa_interface_count": 0,
                                        "lfa_per_prefix_interface_count": 0,
                                        "lfa_revision": 0,
                                        "nbrs_full": 1,
                                        "nbrs_staggered_mode": 0,
                                        "spf_runs_count": 79,
                                    },
                                }
                            },
                            "database_control": {"max_lsa": 123},
                            "external_flood_list_length": 0,
                            "flags": {"abr": True, "asbr": True},
                            "flood_pacing_interval_msec": 33,
                            "lsd_revision": 1,
                            "lsd_state": "connected, registered, bound",
                            "maximum_interfaces": 1024,
                            "nsr": {"enable": True},
                            "numbers": {
                                "dc_bitless": 0,
                                "do_not_age": 0,
                                "external_lsa": 0,
                                "external_lsa_checksum": "00000000",
                                "opaque_as_lsa": 0,
                                "opaque_as_lsa_checksum": "00000000",
                            },
                            "redistribution": {
                                "bgp": {"bgp_id": 100},
                                "max_prefix": {
                                    "num_of_prefix": 10240,
                                    "prefix_thld": 75,
                                    "warn_only": False,
                                },
                            },
                            "retransmission_pacing_interval": 66,
                            "role": "primary active",
                            "router_id": "10.36.3.3",
                            "segment_routing_global_block_default": "16000-23999",
                            "segment_routing_global_block_status": "not allocated",
                            "snmp_trap": False,
                            "spf_control": {
                                "throttle": {
                                    "lsa": {
                                        "arrival": 100,
                                        "hold": 200,
                                        "interval": 200,
                                        "maximum": 5000,
                                        "refresh_interval": 1800,
                                        "start": 50,
                                    },
                                    "spf": {
                                        "hold": 200,
                                        "maximum": 5000,
                                        "start": 50,
                                    },
                                }
                            },
                            "strict_spf": True,
                            "total_areas": 1,
                            "total_normal_areas": 1,
                            "total_nssa_areas": 0,
                            "total_stub_areas": 0,
                            "stub_router": {
                                "always": {
                                    "always": False,
                                    "external_lsa": False,
                                    "include_stub": False,
                                    "summary_lsa": False,
                                }
                            },
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
                            "adjacency_stagger": {
                                "disable": False,
                                "initial_number": 2,
                                "maximum_number": 64,
                                "nbrs_forming": 0,
                                "nbrs_full": 2,
                            },
                            "areas": {
                                "0.0.0.0": {
                                    "area_type": "normal",
                                    "area_id": "0.0.0.0",
                                    "rrr_enabled": True,
                                    "statistics": {
                                        "area_scope_lsa_cksum_sum": "0x0a2fb5",
                                        "area_scope_lsa_count": 19,
                                        "area_scope_opaque_lsa_cksum_sum": "00000000",
                                        "area_scope_opaque_lsa_count": 0,
                                        "dcbitless_lsa_count": 5,
                                        "donotage_lsa_count": 0,
                                        "flood_list_length": 0,
                                        "indication_lsa_count": 0,
                                        "interfaces_count": 3,
                                        "lfa_interface_count": 0,
                                        "lfa_per_prefix_interface_count": 0,
                                        "lfa_revision": 0,
                                        "nbrs_full": 2,
                                        "nbrs_staggered_mode": 0,
                                        "spf_runs_count": 26,
                                    },
                                    "topology_version": 15,
                                }
                            },
                            "external_flood_list_length": 0,
                            "flood_pacing_interval_msec": 33,
                            "lsd_revision": 1,
                            "lsd_state": "connected, registered, bound",
                            "maximum_interfaces": 1024,
                            "mpls": {
                                "ldp": {
                                    "ldp_igp_sync": True,
                                    "ldp_sync_status": "not achieved",
                                }
                            },
                            "nsr": {"enable": True},
                            "numbers": {
                                "dc_bitless": 0,
                                "do_not_age": 0,
                                "external_lsa": 1,
                                "external_lsa_checksum": "0x00607f",
                                "opaque_as_lsa": 0,
                                "opaque_as_lsa_checksum": "00000000",
                            },
                            "retransmission_pacing_interval": 66,
                            "role": "primary active",
                            "router_id": "10.36.3.3",
                            "segment_routing_global_block_default": "16000-23999",
                            "segment_routing_global_block_status": "not allocated",
                            "snmp_trap": True,
                            "spf_control": {
                                "throttle": {
                                    "lsa": {
                                        "arrival": 100,
                                        "hold": 200,
                                        "interval": 200,
                                        "maximum": 5000,
                                        "refresh_interval": 1800,
                                        "start": 50,
                                    },
                                    "spf": {
                                        "hold": 200,
                                        "maximum": 5000,
                                        "start": 50,
                                    },
                                }
                            },
                            "strict_spf": True,
                            "total_areas": 1,
                            "total_normal_areas": 1,
                            "total_nssa_areas": 0,
                            "total_stub_areas": 0,
                            "stub_router": {
                                "always": {
                                    "always": True,
                                    "external_lsa": True,
                                    "external_lsa_metric": 16711680,
                                    "include_stub": True,
                                    "state": "active",
                                    "summary_lsa": True,
                                    "summary_lsa_metric": 16711680,
                                },
                                "on_startup": {
                                    "on_startup": 5,
                                    "external_lsa": True,
                                    "external_lsa_metric": 16711680,
                                    "include_stub": True,
                                    "state": "inactive",
                                    "summary_lsa": True,
                                    "summary_lsa_metric": 16711680,
                                },
                                "on_switchover": {
                                    "on_switchover": 10,
                                    "external_lsa": True,
                                    "external_lsa_metric": 16711680,
                                    "include_stub": True,
                                    "state": "inactive",
                                    "summary_lsa": True,
                                    "summary_lsa_metric": 16711680,
                                },
                            },
                        }
                    }
                }
            }
        },
    }
}

