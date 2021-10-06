

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
                                    "area_id": "0.0.0.1",
                                    "area_type": "normal",
                                    "statistics": {
                                        "area_scope_lsa_cksum_sum": "0x04b760",
                                        "area_scope_lsa_count": 9,
                                        "area_scope_opaque_lsa_cksum_sum": "00000000",
                                        "area_scope_opaque_lsa_count": 0,
                                        "dcbitless_lsa_count": 0,
                                        "donotage_lsa_count": 0,
                                        "flood_list_length": 0,
                                        "indication_lsa_count": 0,
                                        "interfaces_count": 2,
                                        "lfa_interface_count": 0,
                                        "lfa_per_prefix_interface_count": 0,
                                        "lfa_revision": 0,
                                        "nbrs_full": 1,
                                        "nbrs_staggered_mode": 0,
                                        "spf_runs_count": 3,
                                    },
                                }
                            },
                            "external_flood_list_length": 0,
                            "flags": {"abr": True, "asbr": True},
                            "flood_pacing_interval_msec": 33,
                            "graceful_restart": {
                                "ietf": {"enable": True, "type": "ietf"}
                            },
                            "lsd_revision": 1,
                            "lsd_state": "connected, registered, bound",
                            "maximum_interfaces": 1024,
                            "nsr": {"enable": True},
                            "numbers": {
                                "dc_bitless": 0,
                                "do_not_age": 0,
                                "external_lsa": 3,
                                "external_lsa_checksum": "0x01df46",
                                "opaque_as_lsa": 0,
                                "opaque_as_lsa_checksum": "00000000",
                            },
                            "redistribution": {
                                "bgp": {"bgp_id": 100, "metric": 111},
                                "connected": {"enabled": True, "metric": 10},
                                "isis": {"isis_pid": "10", "metric": 3333},
                                "max_prefix": {
                                    "num_of_prefix": 4000,
                                    "prefix_thld": 70,
                                    "warn_only": False,
                                },
                                "static": {"enabled": True},
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
                            "stub_router": {
                                "always": {
                                    "always": False,
                                    "external_lsa": False,
                                    "include_stub": False,
                                    "summary_lsa": False,
                                }
                            },
                            "total_areas": 1,
                            "total_normal_areas": 1,
                            "total_nssa_areas": 0,
                            "total_stub_areas": 0,
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
                                "nbrs_full": 1,
                            },
                            "areas": {
                                "0.0.0.0": {
                                    "area_id": "0.0.0.0",
                                    "area_type": "normal",
                                    "rrr_enabled": True,
                                    "statistics": {
                                        "area_scope_lsa_cksum_sum": "0x07a597",
                                        "area_scope_lsa_count": 14,
                                        "area_scope_opaque_lsa_cksum_sum": "00000000",
                                        "area_scope_opaque_lsa_count": 0,
                                        "dcbitless_lsa_count": 0,
                                        "donotage_lsa_count": 0,
                                        "flood_list_length": 0,
                                        "indication_lsa_count": 0,
                                        "interfaces_count": 5,
                                        "lfa_interface_count": 0,
                                        "lfa_per_prefix_interface_count": 0,
                                        "lfa_revision": 0,
                                        "nbrs_full": 1,
                                        "nbrs_staggered_mode": 0,
                                        "spf_runs_count": 12,
                                    },
                                    "topology_version": 7,
                                },
                                "0.0.0.1": {
                                    "area_id": "0.0.0.1",
                                    "area_type": "stub",
                                    "summary": True,
                                    "default_cost": 111,
                                    "ranges": {
                                        "10.4.0.0/16": {
                                            "advertise": True,
                                            "prefix": "10.4.0.0/16",
                                        }
                                    },
                                    "statistics": {
                                        "area_scope_lsa_cksum_sum": "0x05adf0",
                                        "area_scope_lsa_count": 13,
                                        "area_scope_opaque_lsa_cksum_sum": "00000000",
                                        "area_scope_opaque_lsa_count": 0,
                                        "dcbitless_lsa_count": 0,
                                        "donotage_lsa_count": 0,
                                        "flood_list_length": 0,
                                        "indication_lsa_count": 0,
                                        "interfaces_count": 1,
                                        "lfa_interface_count": 0,
                                        "lfa_per_prefix_interface_count": 0,
                                        "lfa_revision": 0,
                                        "nbrs_full": 0,
                                        "nbrs_staggered_mode": 0,
                                        "spf_runs_count": 8,
                                    },
                                },
                                "0.0.0.2": {
                                    "area_id": "0.0.0.2",
                                    "area_type": "stub",
                                    "summary": False,
                                    "default_cost": 222,
                                    "ranges": {
                                        "10.4.1.0/24": {
                                            "advertise": True,
                                            "prefix": "10.4.1.0/24",
                                        }
                                    },
                                    "statistics": {
                                        "area_scope_lsa_cksum_sum": "0x0076bf",
                                        "area_scope_lsa_count": 2,
                                        "area_scope_opaque_lsa_cksum_sum": "00000000",
                                        "area_scope_opaque_lsa_count": 0,
                                        "dcbitless_lsa_count": 0,
                                        "donotage_lsa_count": 0,
                                        "flood_list_length": 0,
                                        "indication_lsa_count": 0,
                                        "interfaces_count": 1,
                                        "lfa_interface_count": 0,
                                        "lfa_per_prefix_interface_count": 0,
                                        "lfa_revision": 0,
                                        "nbrs_full": 0,
                                        "nbrs_staggered_mode": 0,
                                        "spf_runs_count": 4,
                                    },
                                },
                                "0.0.0.3": {
                                    "area_id": "0.0.0.3",
                                    "area_type": "nssa",
                                    "lsa_translation": "type-7/type-5",
                                    "ranges": {
                                        "10.16.2.0/24": {
                                            "advertise": True,
                                            "prefix": "10.16.2.0/24",
                                        }
                                    },
                                    "statistics": {
                                        "area_scope_lsa_cksum_sum": "0x09166c",
                                        "area_scope_lsa_count": 14,
                                        "area_scope_opaque_lsa_cksum_sum": "00000000",
                                        "area_scope_opaque_lsa_count": 0,
                                        "dcbitless_lsa_count": 0,
                                        "donotage_lsa_count": 0,
                                        "flood_list_length": 0,
                                        "indication_lsa_count": 0,
                                        "interfaces_count": 1,
                                        "lfa_interface_count": 0,
                                        "lfa_per_prefix_interface_count": 0,
                                        "lfa_revision": 0,
                                        "nbrs_full": 0,
                                        "nbrs_staggered_mode": 0,
                                        "spf_runs_count": 4,
                                    },
                                },
                                "0.0.0.4": {
                                    "area_id": "0.0.0.4",
                                    "area_type": "nssa",
                                    "lsa_translation": "type-7/type-5",
                                    "statistics": {
                                        "area_scope_lsa_cksum_sum": "0x022418",
                                        "area_scope_lsa_count": 4,
                                        "area_scope_opaque_lsa_cksum_sum": "00000000",
                                        "area_scope_opaque_lsa_count": 0,
                                        "dcbitless_lsa_count": 0,
                                        "donotage_lsa_count": 0,
                                        "flood_list_length": 0,
                                        "indication_lsa_count": 0,
                                        "interfaces_count": 1,
                                        "lfa_interface_count": 0,
                                        "lfa_per_prefix_interface_count": 0,
                                        "lfa_revision": 0,
                                        "nbrs_full": 0,
                                        "nbrs_staggered_mode": 0,
                                        "spf_runs_count": 4,
                                    },
                                },
                            },
                            "external_flood_list_length": 0,
                            "flags": {"abr": True, "asbr": True},
                            "flood_pacing_interval_msec": 33,
                            "graceful_restart": {
                                "cisco": {"enable": True, "type": "cisco"}
                            },
                            "lsd_revision": 1,
                            "lsd_state": "connected, registered, bound",
                            "maximum_interfaces": 1024,
                            "nsr": {"enable": True},
                            "numbers": {
                                "dc_bitless": 0,
                                "do_not_age": 0,
                                "external_lsa": 3,
                                "external_lsa_checksum": "0x01b657",
                                "opaque_as_lsa": 0,
                                "opaque_as_lsa_checksum": "00000000",
                            },
                            "redistribution": {
                                "bgp": {"bgp_id": 100, "metric": 111},
                                "connected": {"enabled": True},
                                "isis": {"isis_pid": "10", "metric": 3333},
                                "max_prefix": {
                                    "num_of_prefix": 3000,
                                    "prefix_thld": 90,
                                    "warn_only": True,
                                },
                                "static": {"enabled": True, "metric": 10},
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
                            "stub_router": {
                                "always": {
                                    "always": False,
                                    "external_lsa": False,
                                    "include_stub": False,
                                    "summary_lsa": False,
                                }
                            },
                            "total_areas": 5,
                            "total_normal_areas": 1,
                            "total_nssa_areas": 2,
                            "total_stub_areas": 2,
                        }
                    }
                }
            }
        },
    }
}
