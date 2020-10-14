expected_output = {
    "protocols": {
        "application": {
            "flushed": 0,
            "holddown": 0,
            "incoming_filter_list": "not set",
            "invalid": 0,
            "maximum_path": 32,
            "outgoing_filter_list": "not set",
            "preference": {"single_value": {"all": 4}},
            "update_frequency": 0,
        },
        "bgp": {
            "instance": {
                "default": {
                    "bgp_id": 9999,
                    "vrf": {
                        "default": {
                            "address_family": {
                                "ipv4": {
                                    "automatic_route_summarization": False,
                                    "igp_sync": False,
                                    "incoming_filter_list": "not set",
                                    "maximum_path": 1,
                                    "routing_information_sources": {
                                        "10.60.6.2": {
                                            "distance": 200,
                                            "last_update": "14w4d",
                                            "neighbor_id": "10.60.6.2",
                                        },
                                        "10.60.6.3": {
                                            "distance": 200,
                                            "last_update": "12w5d",
                                            "neighbor_id": "10.60.6.3",
                                        },
                                    },
                                    "outgoing_filter_list": "not set",
                                    "preference": {
                                        "multi_values": {
                                            "external": 20,
                                            "internal": 200,
                                            "local": 200,
                                        }
                                    },
                                }
                            }
                        }
                    },
                }
            }
        },
        "isis": {
            "vrf": {
                "default": {
                    "address_family": {
                        "ipv4": {
                            "instance": {
                                "banana": {
                                    "configured_interfaces": [
                                        "TenGigabitEthernet0/0/26",
                                        "TenGigabitEthernet0/0/27",
                                    ],
                                    "incoming_filter_list": "not set",
                                    "maximum_path": 4,
                                    "outgoing_filter_list": "not set",
                                    "passive_interfaces": ["Loopback0"],
                                    "preference": {"single_value": {"all": 115}},
                                    "redistributing": "isis banana",
                                    "routing_information_sources": {
                                        "gateway": {
                                            "10.60.6.2": {
                                                "distance": 115,
                                                "last_update": "05:56:34",
                                            },
                                            "10.60.6.3": {
                                                "distance": 115,
                                                "last_update": "05:56:34",
                                            },
                                            "10.60.6.4": {
                                                "distance": 115,
                                                "last_update": "05:56:34",
                                            },
                                            "10.60.6.9": {
                                                "distance": 115,
                                                "last_update": "05:56:34",
                                            },
                                        }
                                    },
                                }
                            }
                        }
                    }
                }
            }
        },
    }
}
