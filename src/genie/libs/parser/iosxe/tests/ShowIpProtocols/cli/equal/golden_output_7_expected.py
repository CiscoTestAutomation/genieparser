expected_output = {
    "protocols": {
        "application": {
            "update_frequency": 0,
            "invalid": 0,
            "holddown": 0,
            "flushed": 0,
            "outgoing_filter_list": "not set",
            "incoming_filter_list": "not set",
            "maximum_path": 32,
            "preference": {"single_value": {"all": 4}},
        },
        "ospf": {
            "vrf": {
                "default": {
                    "address_family": {
                        "ipv4": {
                            "instance": {
                                "1": {
                                    "outgoing_filter_list": "not set",
                                    "incoming_filter_list": "not set",
                                    "router_id": "192.168.1.179",
                                    "total_areas": 2,
                                    "total_normal_area": 1,
                                    "total_stub_area": 0,
                                    "total_nssa_area": 1,
                                    "spf_control": {"paths": 4},
                                    "network": {
                                        "192.168.1.0": {
                                            "netmask": "0.0.0.255",
                                            "area": "0.0.0.0",
                                        },
                                        "192.168.100.164": {
                                            "netmask": "0.0.0.3",
                                            "area": "0.0.0.0",
                                        },
                                        "192.168.100.192": {
                                            "netmask": "0.0.0.3",
                                            "area": "0.0.0.0",
                                        },
                                    },
                                    "areas": {
                                        "0.0.0.0": {
                                            "configured_interfaces": [
                                                "GigabitEthernet5"
                                            ]
                                        },
                                        "0.0.0.4": {
                                            "configured_interfaces": [
                                                "GigabitEthernet7"
                                            ]
                                        },
                                    },
                                    "passive_interfaces": [
                                        "GigabitEthernet3",
                                        "GigabitEthernet4",
                                        "GigabitEthernet8",
                                        "Loopback0",
                                        "VoIP-Null0",
                                    ],
                                    "routing_information_sources": {
                                        "gateway": {
                                            "192.168.1.177": {
                                                "distance": 110,
                                                "last_update": "21:33:11",
                                            },
                                            "192.168.1.176": {
                                                "distance": 110,
                                                "last_update": "21:32:48",
                                            },
                                            "192.168.1.178": {
                                                "distance": 110,
                                                "last_update": "21:36:07",
                                            },
                                        }
                                    },
                                    "preference": {"single_value": {"all": 110}},
                                }
                            }
                        }
                    }
                }
            }
        },
        "bgp": {
            "instance": {
                "default": {
                    "bgp_id": 202926,
                    "vrf": {
                        "default": {
                            "address_family": {
                                "ipv4": {
                                    "outgoing_filter_list": "not set",
                                    "incoming_filter_list": "not set",
                                    "igp_sync": False,
                                    "automatic_route_summarization": False,
                                    "neighbors": {
                                        "10.0.1.211": {},
                                        "10.0.1.221": {},
                                        "10.0.2.212": {},
                                        "10.0.2.222": {},
                                        "10.205.188.34": {},
                                        "10.205.37.149": {},
                                        "172.16.121.101": {
                                            "route_map": "ACCEPT_SCI_RICHEMONT"
                                        },
                                        "192.168.1.176": {
                                            "route_map": "INTERNET_EDGE_IN"
                                        },
                                        "192.168.1.177": {
                                            "route_map": "INTERNET_EDGE_IN"
                                        },
                                        "192.168.1.178": {},
                                    },
                                    "maximum_path": 2,
                                    "routing_information_sources": {
                                        "192.168.1.177": {
                                            "neighbor_id": "192.168.1.177",
                                            "distance": 200,
                                            "last_update": "21:33:06",
                                        },
                                        "192.168.1.176": {
                                            "neighbor_id": "192.168.1.176",
                                            "distance": 200,
                                            "last_update": "21:32:43",
                                        },
                                        "10.0.2.212": {
                                            "neighbor_id": "10.0.2.212",
                                            "distance": 20,
                                            "last_update": "21:35:39",
                                        },
                                    },
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
    }
}
