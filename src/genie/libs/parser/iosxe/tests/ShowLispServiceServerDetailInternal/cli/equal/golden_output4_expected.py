expected_output = {
    "lisp_router_instances": {
        0: {
            "service": {
                "ipv4": {
                    "map_server": {
                        "sites": {
                            "xtr1": {
                                "allowed_configured_locators": "any",
                                "site_id": "xtr1",
                            },
                            "xtr2": {
                                "allowed_configured_locators": "any",
                                "site_id": "xtr2",
                            },
                        },
                        "virtual_network_ids": {
                            "101": {
                                "mappings": {
                                    "192.168.0.1/32": {
                                        "eid_id": "192.168.0.1/32",
                                        "first_registered": "01:12:41",
                                        "eid_address": {
                                            "address_type": "ipv4-afi",
                                            "ipv4": {"ipv4": "192.168.0.1/32"},
                                            "virtual_network_id": "101",
                                        },
                                        "last_registered": "01:12:41",
                                        "mapping_records": {
                                            "0x21EDD25F-0x7598784C-0x769C8E4E-0xC04926EC": {
                                                "eid": {
                                                    "address_type": "ipv4-afi",
                                                    "ipv4": {"ipv4": "192.168.0.1/32"},
                                                    "virtual_network_id": "101",
                                                },
                                                "etr": "10.16.2.2",
                                                "map_notify": True,
                                                "merge": False,
                                                "nonce": "0x70D18EF4-0x3A605D67",
                                                "proxy_reply": True,
                                                "security_capability": False,
                                                "sourced_by": "reliable transport",
                                                "state": "complete",
                                                "time_to_live": 86400,
                                                "ttl": "1d00h",
                                                "creation_time": "01:12:41",
                                                "hash_function": "sha1,",
                                                "locator": {
                                                    "10.16.2.2": {
                                                        "local": True,
                                                        "priority": 50,
                                                        "scope": "IPv4 none",
                                                        "state": "up",
                                                        "weight": 50,
                                                    }
                                                },
                                                "site_id": "unspecified",
                                                "xtr_id": "0x21EDD25F-0x7598784C-0x769C8E4E-0xC04926EC",
                                            }
                                        },
                                        "merge_active": False,
                                        "origin": "Dynamic",
                                        "proxy_reply": True,
                                        "registration_errors": {
                                            "allowed_locators_mismatch": 0,
                                            "authentication_failures": 0,
                                        },
                                        "routing_table_tag": 0,
                                        "site_id": "xtr1",
                                        "state": "complete",
                                        "ttl": "1d00h",
                                    },
                                    "192.168.9.0/24": {
                                        "eid_id": "192.168.9.0/24",
                                        "first_registered": "01:55:47",
                                        "eid_address": {
                                            "address_type": "ipv4-afi",
                                            "ipv4": {"ipv4": "192.168.9.0/24"},
                                            "virtual_network_id": "101",
                                        },
                                        "last_registered": "01:55:47",
                                        "mapping_records": {
                                            "0x77200484-0xD134DC48-0x0FBAD9DC-0x4A46CA5D": {
                                                "eid": {
                                                    "address_type": "ipv4-afi",
                                                    "ipv4": {"ipv4": "192.168.9.0/24"},
                                                    "virtual_network_id": "101",
                                                },
                                                "etr": "1000:1000:1000:1000::",
                                                "creation_time": "01:55:47",
                                                "hash_function": "sha1,",
                                                "map_notify": True,
                                                "merge": False,
                                                "nonce": "0xB06AE31D-0x6ADB0BA5",
                                                "proxy_reply": True,
                                                "security_capability": False,
                                                "sourced_by": "reliable transport",
                                                "state": "complete",
                                                "time_to_live": 86400,
                                                "ttl": "1d00h",
                                                "locator": {
                                                    "1000:1000:1000:1000::": {
                                                        "local": True,
                                                        "priority": 50,
                                                        "scope": "IPv4 none",
                                                        "state": "up",
                                                        "weight": 50,
                                                    }
                                                },
                                                "site_id": "unspecified",
                                                "xtr_id": "0x77200484-0xD134DC48-0x0FBAD9DC-0x4A46CA5D",
                                            }
                                        },
                                        "merge_active": False,
                                        "origin": "Configuration",
                                        "proxy_reply": True,
                                        "registration_errors": {
                                            "allowed_locators_mismatch": 0,
                                            "authentication_failures": 0,
                                        },
                                        "routing_table_tag": 0,
                                        "site_id": "xtr2",
                                        "state": "complete",
                                        "ttl": "1d00h",
                                    },
                                },
                                "vni": "101",
                            }
                        },
                    }
                }
            }
        }
    }
}
