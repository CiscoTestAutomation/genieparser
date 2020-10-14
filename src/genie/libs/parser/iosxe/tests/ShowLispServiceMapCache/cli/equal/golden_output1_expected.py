expected_output = {
    "lisp_router_instances": {
        0: {
            "lisp_router_instance_id": 0,
            "service": {
                "ipv4": {
                    "service": "ipv4",
                    "itr": {
                        "map_cache": {
                            "101": {
                                "vni": "101",
                                "entries": 2,
                                "mappings": {
                                    "0.0.0.0/0": {
                                        "id": "0.0.0.0/0",
                                        "creation_time": "15:23:50",
                                        "time_to_live": "never",
                                        "via": "static-send-map-request",
                                        "eid": {
                                            "address_type": "ipv4-afi",
                                            "vrf": "red",
                                            "ipv4": {"ipv4": "0.0.0.0/0"},
                                        },
                                        "negative_mapping": {
                                            "map_reply_action": "send-map-request"
                                        },
                                    },
                                    "192.168.9.0/24": {
                                        "id": "192.168.9.0/24",
                                        "creation_time": "00:04:02",
                                        "time_to_live": "23:55:57",
                                        "via": "map-reply, complete",
                                        "eid": {
                                            "address_type": "ipv4-afi",
                                            "vrf": "red",
                                            "ipv4": {"ipv4": "192.168.9.0/24"},
                                        },
                                        "positive_mapping": {
                                            "rlocs": {
                                                1: {
                                                    "id": "1",
                                                    "encap_iid": "-",
                                                    "priority": 50,
                                                    "state": "up",
                                                    "uptime": "00:04:02",
                                                    "weight": 50,
                                                    "locator_address": {
                                                        "address_type": "ipv4-afi",
                                                        "virtual_network_id": "101",
                                                        "ipv4": {"ipv4": "10.1.8.8"},
                                                    },
                                                }
                                            }
                                        },
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
