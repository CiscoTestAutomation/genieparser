expected_output = {
    "lisp_router_instances": {
        0: {
            "lisp_router_id": {
                "site_id": "unspecified",
                "xtr_id": "0xA5EABB49-0x6C6CE939-0x530E699E-0x09187DFC",
            },
            "lisp_router_instance_id": 0,
            "service": {
                "ethernet": {
                    "delegated_database_tree": False,
                    "etr": {
                        "accept_mapping_data": "disabled, verify disabled",
                        "enabled": True,
                        "encapsulation": "vxlan",
                        "map_cache_ttl": "1d00h",
                        "mapping_servers": {
                            "10.94.44.44": {
                                "ms_address": "10.94.44.44",
                                "uptime": "00:00:50",
                            },
                            "10.84.66.66": {
                                "ms_address": "10.84.66.66",
                                "uptime": "never",
                            },
                        },
                        "proxy_etr_router": False,
                    },
                    "instance_id": {
                        "1": {
                            "database": {
                                "dynamic_database_limit": 65535,
                                "dynamic_database_size": 2,
                                "import_site_db_limit": 65535,
                                "import_site_db_size": 0,
                                "inactive_deconfig_away_size": 0,
                                "proxy_db_size": 0,
                                "route_import_database_limit": 5000,
                                "route_import_database_size": 0,
                                "static_database_limit": 65535,
                                "static_database_size": 0,
                                "total_database_mapping_size": 2,
                            },
                            "eid_table": "Vlan 101",
                            "itr": {"local_rloc_last_resort": "10.229.11.1"},
                            "map_cache": {
                                "imported_route_count": 0,
                                "imported_route_limit": 5000,
                                "map_cache_size": 4,
                                "persistent_map_cache": False,
                                "static_mappings_configured": 0,
                            },
                            "map_request_source": "derived from EID destination",
                            "mapping_servers": {
                                "10.94.44.44": {
                                    "ms_address": "10.94.44.44",
                                    "uptime": "00:00:45",
                                },
                                "10.84.66.66": {
                                    "ms_address": "10.84.66.66",
                                    "uptime": "never",
                                },
                            },
                            "site_registration_limit": 0,
                        },
                        "2": {
                            "database": {
                                "dynamic_database_limit": 65535,
                                "dynamic_database_size": 2,
                                "import_site_db_limit": 65535,
                                "import_site_db_size": 0,
                                "inactive_deconfig_away_size": 0,
                                "proxy_db_size": 0,
                                "route_import_database_limit": 5000,
                                "route_import_database_size": 0,
                                "static_database_limit": 65535,
                                "static_database_size": 0,
                                "total_database_mapping_size": 2,
                            },
                            "eid_table": "Vlan 102",
                            "itr": {"local_rloc_last_resort": "10.229.11.1"},
                            "map_cache": {
                                "imported_route_count": 0,
                                "imported_route_limit": 5000,
                                "map_cache_size": 0,
                                "persistent_map_cache": False,
                                "static_mappings_configured": 0,
                            },
                            "map_request_source": "derived from EID destination",
                            "mapping_servers": {
                                "10.94.44.44": {
                                    "ms_address": "10.94.44.44",
                                    "uptime": "00:00:50",
                                },
                                "10.84.66.66": {
                                    "ms_address": "10.84.66.66",
                                    "uptime": "never",
                                },
                            },
                            "site_registration_limit": 0,
                        },
                    },
                    "itr": {
                        "enabled": True,
                        "map_resolvers": {
                            "10.94.44.44": {"map_resolver": "10.94.44.44"},
                            "10.84.66.66": {"map_resolver": "10.84.66.66"},
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
                        "map_cache_limit": 5120,
                    },
                    "map_resolver": {"enabled": False},
                    "map_server": {"enabled": False},
                    "mobility_first_hop_router": False,
                    "nat_traversal_router": False,
                    "service": "ethernet",
                    "source_locator_configuration": {
                        "vlans": {
                            "vlan100": {
                                "address": "10.229.11.1",
                                "interface": "Loopback0",
                            },
                            "vlan101": {
                                "address": "10.229.11.1",
                                "interface": "Loopback0",
                            },
                        }
                    },
                }
            },
        }
    }
}
