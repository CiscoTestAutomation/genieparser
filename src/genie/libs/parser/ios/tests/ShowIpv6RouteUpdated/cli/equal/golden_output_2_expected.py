expected_output = {
    "ipv6_unicast_routing_enabled": True,
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:db8:100::/64": {
                            "route": "2001:db8:100::/64",
                            "active": True,
                            "source_protocol_codes": "O",
                            "source_protocol": "ospf",
                            "route_preference": 110,
                            "metric": 1,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "FE80::211:1FF:FE00:1",
                                        "outgoing_interface": "GigabitEthernet0/0/2.100",
                                        "updated": "09:42:39 06 December 2017",
                                    }
                                }
                            },
                        },
                        "2001:db8:100:1::/64": {
                            "route": "2001:db8:100:1::/64",
                            "active": True,
                            "source_protocol_codes": "O",
                            "source_protocol": "ospf",
                            "route_preference": 110,
                            "metric": 1,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "FE80::211:1FF:FE00:1",
                                        "outgoing_interface": "GigabitEthernet0/0/2.100",
                                        "updated": "09:42:39 06 December 2017",
                                    }
                                }
                            },
                        },
                        "2001:db8:100:4::/64": {
                            "route": "2001:db8:100:4::/64",
                            "active": True,
                            "source_protocol_codes": "O",
                            "source_protocol": "ospf",
                            "route_preference": 110,
                            "metric": 1,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "FE80::211:1FF:FE00:1",
                                        "outgoing_interface": "GigabitEthernet0/0/2.100",
                                        "updated": "09:42:39 06 December 2017",
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
