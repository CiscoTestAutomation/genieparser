expected_output = {
    "lisp_router_instances": {
        0: {
            "service": {
                "ipv6": {
                    "map_server": {
                        "sites": {
                            "provider": {
                                "allowed_configured_locators": "any",
                                "site_id": "provider",
                            },
                            "xtr1_1": {
                                "allowed_configured_locators": "any",
                                "site_id": "xtr1_1",
                            },
                            "xtr1_2": {
                                "allowed_configured_locators": "any",
                                "site_id": "xtr1_2",
                            },
                            "xtr2": {
                                "allowed_configured_locators": "any",
                                "site_id": "xtr2",
                            },
                        },
                        "virtual_network_ids": {
                            "101": {
                                "mappings": {
                                    "2001:192:168:9::/64": {
                                        "eid_id": "2001:192:168:9::/64",
                                        "first_registered": "00:13:19",
                                        "eid_address": {
                                            "address_type": "ipv6-afi",
                                            "ipv6": {"ipv6": "2001:192:168:9::/64"},
                                            "virtual_network_id": "101",
                                        },
                                        "last_registered": "00:13:19",
                                        "mapping_records": {
                                            "0x6BE732BF-0xD9530F52-0xF9162AA3-0x6283920A": {
                                                "eid": {
                                                    "address_type": "ipv6-afi",
                                                    "ipv6": {
                                                        "ipv6": "2001:192:168:9::/64"
                                                    },
                                                    "virtual_network_id": "101",
                                                },
                                                "etr": "10.1.8.8",
                                                "creation_time": "00:13:19",
                                                "hash_function": "sha1,",
                                                "map_notify": True,
                                                "merge": False,
                                                "nonce": "0x90004FBE-0x03D2420E",
                                                "proxy_reply": True,
                                                "security_capability": False,
                                                "sourced_by": "reliable transport",
                                                "state": "complete",
                                                "time_to_live": 86400,
                                                "ttl": "1d00h",
                                                "locator": {
                                                    "10.1.8.8": {
                                                        "local": True,
                                                        "priority": 50,
                                                        "scope": "IPv4 none",
                                                        "state": "up",
                                                        "weight": 50,
                                                    }
                                                },
                                                "site_id": "unspecified",
                                                "xtr_id": "0x6BE732BF-0xD9530F52-0xF9162AA3-0x6283920A",
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
                                    "2001:192:168::/64": {
                                        "eid_id": "2001:192:168::/64",
                                        "first_registered": "00:13:19",
                                        "eid_address": {
                                            "address_type": "ipv6-afi",
                                            "ipv6": {"ipv6": "2001:192:168::/64"},
                                            "virtual_network_id": "101",
                                        },
                                        "last_registered": "00:13:19",
                                        "mapping_records": {
                                            "0x5B6A0468-0x55E69768-0xD1AE2E61-0x4A082FD5": {
                                                "eid": {
                                                    "address_type": "ipv6-afi",
                                                    "ipv6": {
                                                        "ipv6": "2001:192:168::/64"
                                                    },
                                                    "virtual_network_id": "101",
                                                },
                                                "etr": "10.16.2.2",
                                                "creation_time": "00:13:19",
                                                "hash_function": "sha1,",
                                                "map_notify": True,
                                                "merge": False,
                                                "nonce": "0xF8845AAB-0x44B8B869",
                                                "proxy_reply": True,
                                                "security_capability": False,
                                                "sourced_by": "reliable transport",
                                                "state": "complete",
                                                "time_to_live": 86400,
                                                "ttl": "1d00h",
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
                                                "xtr_id": "0x5B6A0468-0x55E69768-0xD1AE2E61-0x4A082FD5",
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
                                        "site_id": "xtr1_1",
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
