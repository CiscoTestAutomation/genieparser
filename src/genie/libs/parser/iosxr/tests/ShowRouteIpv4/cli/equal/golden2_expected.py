expected_output = {
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "routes": {
                            "10.4.1.32/32": {
                                "route": "10.4.1.32/32",
                                "active": True,
                                "metric": 100020,
                                "route_preference": 115,
                                "source_protocol_codes": "i L2 (!)",
                                "source_protocol": "isis",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.16.2.3",
                                            "updated": "1d06h",
                                            "outgoing_interface": "HundredGigE0/0/1/1"
                                        },
                                        2: {
                                            "index": 2,
                                            "next_hop": "10.16.2.1",
                                            "updated": "1d06h",
                                            "outgoing_interface": "Bundle-Ether1"
                                        }
                                    }
                                }
                            },
                            "10.4.1.33/32": {
                                "route": "10.4.1.33/32",
                                "active": True,
                                "metric": 100020,
                                "route_preference": 115,
                                "source_protocol_codes": "i L2 (!)",
                                "source_protocol": "isis",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.16.2.3",
                                            "updated": "1d06h",
                                            "outgoing_interface": "HundredGigE0/0/1/1"
                                        },
                                        2: {
                                            "index": 2,
                                            "next_hop": "10.16.2.1",
                                            "updated": "1d06h",
                                            "outgoing_interface": "Bundle-Ether1"
                                        }
                                    }
                                }
                            },
                            "10.4.1.34/32": {
                                "route": "10.4.1.34/32",
                                "active": True,
                                "metric": 100020,
                                "route_preference": 115,
                                "source_protocol_codes": "i L2 (!)",
                                "source_protocol": "isis",
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.16.2.3",
                                            "updated": "1d06h",
                                            "outgoing_interface": "HundredGigE0/0/1/1"
                                        },
                                        2: {
                                            "index": 2,
                                            "next_hop": "10.16.2.1",
                                            "updated": "1d06h",
                                            "outgoing_interface": "Bundle-Ether1"
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                'last_resort': {
                    'gateway': 'not set'
                },
            }
        }
    }
