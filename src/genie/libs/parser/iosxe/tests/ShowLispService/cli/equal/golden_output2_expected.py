expected_output = {
    "lisp_router_instances": {
        0: {
            "lisp_router_id": {
                "site_id": "unspecified",
                "xtr_id": "0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7",
            },
            "lisp_router_instance_id": 0,
            "service": {
                "ipv6": {
                    "delegated_database_tree": False,
                    "etr": {
                        "accept_mapping_data": "disabled, verify disabled",
                        "enabled": True,
                        "encapsulation": "lisp",
                        "map_cache_ttl": "1d00h",
                        "use_petrs": {"10.10.10.10": {"use_petr": "10.10.10.10"}},
                        "mapping_servers": {
                            "10.166.13.13": {
                                "ms_address": "10.166.13.13",
                                "uptime": "00:00:35",
                            },
                            "10.64.4.4": {
                                "ms_address": "10.64.4.4",
                                "uptime": "17:49:58",
                            },
                        },
                        "proxy_etr_router": False,
                    },
                    "instance_id": {
                        "101": {
                            "database": {
                                "dynamic_database_limit": 65535,
                                "dynamic_database_size": 0,
                                "inactive_deconfig_away_size": 0,
                                "route_import_database_limit": 1000,
                                "route_import_database_size": 0,
                                "static_database_limit": 65535,
                                "static_database_size": 1,
                                "total_database_mapping_size": 1,
                            },
                            "eid_table": "vrf red",
                            "itr": {
                                "local_rloc_last_resort": "10.16.2.2",
                                "use_proxy_etr_rloc": "10.10.10.10",
                            },
                            "map_cache": {
                                "imported_route_count": 0,
                                "imported_route_limit": 1000,
                                "map_cache_size": 2,
                                "persistent_map_cache": False,
                                "static_mappings_configured": 0,
                            },
                            "map_request_source": "derived from EID destination",
                            "mapping_servers": {
                                "10.166.13.13": {
                                    "ms_address": "10.166.13.13",
                                    "uptime": "00:00:35",
                                },
                                "10.64.4.4": {
                                    "ms_address": "10.64.4.4",
                                    "uptime": "17:49:58",
                                },
                            },
                            "site_registration_limit": 0,
                        }
                    },
                    "itr": {
                        "enabled": True,
                        "map_resolvers": {
                            "10.166.13.13": {"map_resolver": "10.166.13.13"},
                            "10.64.4.4": {"map_resolver": "10.64.4.4"},
                        },
                        "max_smr_per_map_cache_entry": "8 more specifics",
                        "multiple_smr_suppression_time": 20,
                        "proxy_itr_router": False,
                        "solicit_map_request": "accept and process",
                    },
                    "locator_status_algorithms": {
                        "ipv4_rloc_min_mask_len": 0,
                        "ipv6_rloc_min_mask_len": 0,
                        "lsb_reports": "process",
                        "rloc_probe_algorithm": False,
                        "rloc_probe_on_member_change": False,
                        "rloc_probe_on_route_change": "N/A (periodic probing disabled)",
                    },
                    "locator_table": "default",
                    "map_cache": {
                        "map_cache_activity_check_period": 60,
                        "map_cache_fib_updates": "established",
                        "map_cache_limit": 1000,
                    },
                    "map_resolver": {"enabled": False},
                    "map_server": {"enabled": False},
                    "mobility_first_hop_router": False,
                    "nat_traversal_router": False,
                    "service": "ipv6",
                }
            },
        }
    }
}
