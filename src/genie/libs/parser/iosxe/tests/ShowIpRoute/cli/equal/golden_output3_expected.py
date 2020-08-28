expected_output = {
    "vrf": {
        "OOB_Mgmt": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "0.0.0.0/0": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {"index": 1, "next_hop": "10.50.15.1"}
                                }
                            },
                            "route": "0.0.0.0/0",
                            "route_preference": 1,
                            "source_protocol": "static",
                            "source_protocol_codes": "S*",
                        },
                        "10.50.15.0/25": {
                            "active": True,
                            "next_hop": {
                                "outgoing_interface": {
                                    "FastEthernet0/0": {
                                        "outgoing_interface": "FastEthernet0/0"
                                    }
                                }
                            },
                            "route": "10.50.15.0/25",
                            "source_protocol": "connected",
                            "source_protocol_codes": "C",
                        },
                        "10.50.15.12/32": {
                            "active": True,
                            "next_hop": {
                                "outgoing_interface": {
                                    "FastEthernet0/0": {
                                        "outgoing_interface": "FastEthernet0/0"
                                    }
                                }
                            },
                            "route": "10.50.15.12/32",
                            "source_protocol": "local",
                            "source_protocol_codes": "L",
                        },
                    }
                }
            }
        }
    }
}
