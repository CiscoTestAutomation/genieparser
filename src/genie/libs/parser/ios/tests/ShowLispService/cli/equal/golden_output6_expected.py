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
                        "map_cache_ttl": "1d00h",
                        "mapping_servers": {
                            "10.94.44.44": {"ms_address": "10.94.44.44"}
                        },
                        "proxy_etr_router": False,
                    },
                    "instance_id": {
                        "*": {
                            "database": {"dynamic_database_mapping_limit": 5120},
                            "itr": {"local_rloc_last_resort": "*** NOT FOUND ***"},
                            "map_cache": {"persistent_map_cache": False},
                            "mapping_servers": {
                                "10.94.44.44": {"ms_address": "10.94.44.44"}
                            },
                        }
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
