

expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "10": {
                            "ipfrr_per_prefix_tiebreakers": {
                                "post_convergence_path": "0",
                                "srlg_disjoint": "0",
                                "downstream": "0",
                                "line_card_disjoint": "30",
                                "lowest_metric": "20",
                                "name": "Index",
                                "no_tunnel": "255",
                                "node_protection": "40",
                                "primary_path": "10",
                                "secondary_path": "0",
                            },
                            "adjacency_stagger": {
                                "disable": False,
                                "initial_number": 2,
                                "maximum_number": 64,
                                "nbrs_forming": 0,
                                "nbrs_full": 2,
                            },
                            "areas": {
                                "0.0.0.0": {
                                    "area_id": "0.0.0.0",
                                    "area_type": "normal",
                                    "rrr_enabled": True,
                                    "statistics": {
                                        "area_scope_lsa_cksum_sum": "0x1849b5b",
                                        "area_scope_lsa_count": 786,
                                        "area_scope_opaque_lsa_cksum_sum": "00000000",
                                        "area_scope_opaque_lsa_count": 0,
                                        "dcbitless_lsa_count": 166,
                                        "donotage_lsa_count": 0,
                                        "flood_list_length": 0,
                                        "indication_lsa_count": 0,
                                        "interfaces_count": 6,
                                        "lfa_interface_count": 2,
                                        "lfa_per_prefix_interface_count": 0,
                                        "lfa_revision": 366718,
                                        "nbrs_full": 2,
                                        "nbrs_staggered_mode": 0,
                                        "spf_runs_count": 366720,
                                    },
                                    "topology_version": 390659,
                                }
                            },
                            "external_flood_list_length": 0,
                            "flood_pacing_interval_msec": 33,
                            "lsd_revision": 1,
                            "lsd_state": "connected, " "registered, " "bound",
                            "maximum_interfaces": 1024,
                            "nsr": {"enable": True},
                            "numbers": {
                                "dc_bitless": 0,
                                "do_not_age": 0,
                                "external_lsa": 145,
                                "external_lsa_checksum": "0x40c673",
                                "opaque_as_lsa": 0,
                                "opaque_as_lsa_checksum": "00000000",
                            },
                            "retransmission_pacing_interval": 66,
                            "role": "primary " "active",
                            "router_id": "10.0.12.56",
                            "segment_routing_global_block_default": "16000-23999",
                            "segment_routing_global_block_status": "not "
                            "allocated",
                            "snmp_trap": True,
                            "spf_control": {
                                "throttle": {
                                    "lsa": {
                                        "arrival": 0,
                                        "hold": 25,
                                        "interval": 25,
                                        "maximum": 10000,
                                        "refresh_interval": 1800,
                                        "start": 0,
                                    },
                                    "spf": {
                                        "hold": 500,
                                        "maximum": 10000,
                                        "start": 100,
                                    },
                                }
                            },
                            "stub_router": {"always": {"include_stub": True}},
                            "total_areas": 1,
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
