expected_output = {
    "ipv6_unicast_routing_enabled": True,
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:1:1:1::1/128": {
                            "route": "2001:1:1:1::1/128",
                            "active": True,
                            "source_protocol_codes": "LC",
                            "source_protocol": "local",
                            "route_preference": 0,
                            "metric": 0,
                            "next_hop": {
                                "outgoing_interface": {
                                    "Loopback0": {
                                        "outgoing_interface": "Loopback0",
                                        "updated": "22:55:51 04 December 2017",
                                    }
                                }
                            },
                        },
                        "2001:2:2:2::2/128": {
                            "route": "2001:2:2:2::2/128",
                            "active": True,
                            "route_preference": 1,
                            "metric": 0,
                            "source_protocol_codes": "S",
                            "source_protocol": "static",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "2001:10:1:2::2",
                                        "outgoing_interface": "GigabitEthernet0/0",
                                        "updated": "22:57:07 04 December 2017",
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "2001:20:1:2::2",
                                        "outgoing_interface": "GigabitEthernet0/1",
                                        "updated": "22:57:23 04 December 2017",
                                    },
                                }
                            },
                        },
                        "2001:3:3:3::3/128": {
                            "route": "2001:3:3:3::3/128",
                            "active": True,
                            "route_preference": 1,
                            "metric": 0,
                            "source_protocol_codes": "S",
                            "source_protocol": "static",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/2": {
                                        "outgoing_interface": "GigabitEthernet0/2",
                                        "updated": "22:57:34 04 December 2017",
                                    },
                                    "GigabitEthernet0/3": {
                                        "outgoing_interface": "GigabitEthernet0/3",
                                        "updated": "22:57:43 04 December 2017",
                                    },
                                }
                            },
                        },
                        "2001:db8:400:1::/64": {
                            "route": "2001:db8:400:1::/64",
                            "active": True,
                            "route_preference": 200,
                            "metric": 1,
                            "source_protocol_codes": "B",
                            "source_protocol": "bgp",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "192.168.51.1",
                                        "updated": "09:43:27 06 December 2017",
                                    }
                                }
                            },
                        },
                    }
                }
            }
        }
    },
}
