expected_output = {
    "lisp_router_instances": {
        0: {
            "lisp_router_instance_id": 0,
            "service": {
                "ipv6": {
                    "service": "ipv6",
                    "itr": {
                        "map_cache": {
                            "101": {
                                "vni": "101",
                                "entries": 2,
                                "mappings": {
                                    "172.16.10.0/24": {
                                        "eid": {
                                            "address_type": "ipv4-afi",
                                            "ipv4": {"ipv4": "172.16.10.0/24"},
                                            "vrf": "red",
                                        },
                                        "time_to_live": "23:59:59",
                                        "id": "172.16.10.0/24",
                                        "positive_mapping": {
                                            "rlocs": {
                                                1: {
                                                    "id": "1",
                                                    "priority": 1,
                                                    "state": "up",
                                                    "uptime": "00:00:00",
                                                    "weight": 50,
                                                    "locator_address": {
                                                        "address_type": "ipv4-afi",
                                                        "ipv4": {
                                                            "ipv4": "172.16.156.134"
                                                        },
                                                        "virtual_network_id": "101",
                                                    },
                                                },
                                                2: {
                                                    "id": "2",
                                                    "priority": 1,
                                                    "state": "up",
                                                    "uptime": "00:00:00",
                                                    "weight": 50,
                                                    "locator_address": {
                                                        "address_type": "ipv4-afi",
                                                        "ipv4": {
                                                            "ipv4": "192.168.65.94"
                                                        },
                                                        "virtual_network_id": "101",
                                                    },
                                                },
                                                3: {
                                                    "id": "3",
                                                    "priority": 2,
                                                    "state": "up",
                                                    "uptime": "00:00:00",
                                                    "weight": 100,
                                                    "locator_address": {
                                                        "address_type": "ipv6-afi",
                                                        "ipv6": {
                                                            "ipv6": "2001:DB8:BBED:2829::80DF:9C86"
                                                        },
                                                        "virtual_network_id": "101",
                                                    },
                                                },
                                            }
                                        },
                                        "creation_time": "00:00:00",
                                        "via": "map-reply, complete",
                                    },
                                    "2001:192:168:9::/64": {
                                        "eid": {
                                            "address_type": "ipv6-afi",
                                            "ipv6": {"ipv6": "2001:192:168:9::/64"},
                                            "vrf": "red",
                                        },
                                        "time_to_live": "23:53:08",
                                        "id": "2001:192:168:9::/64",
                                        "positive_mapping": {
                                            "rlocs": {
                                                1: {
                                                    "id": "1",
                                                    "encap_iid": "-",
                                                    "priority": 50,
                                                    "state": "up",
                                                    "uptime": "00:06:51",
                                                    "weight": 50,
                                                    "locator_address": {
                                                        "address_type": "ipv4-afi",
                                                        "ipv4": {"ipv4": "10.1.8.8"},
                                                        "virtual_network_id": "101",
                                                    },
                                                }
                                            }
                                        },
                                        "creation_time": "00:06:51",
                                        "via": "map-reply, complete",
                                    },
                                    "::/0": {
                                        "eid": {
                                            "address_type": "ipv6-afi",
                                            "ipv6": {"ipv6": "::/0"},
                                            "vrf": "red",
                                        },
                                        "time_to_live": "never",
                                        "id": "::/0",
                                        "negative_mapping": {
                                            "map_reply_action": "send-map-request"
                                        },
                                        "creation_time": "00:11:28",
                                        "via": "static-send-map-request",
                                    },
                                },
                            }
                        }
                    },
                }
            },
        }
    }
}
