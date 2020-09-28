expected_output = {
    "vfi": {
        "serviceCore1": {
            "signaling": "LDP",
            "vpls_id": "9:10",
            "vpn_id": 100,
            "bd_vfi_name": "serviceCore1",
            "bridge_domain": {
                100: {
                    "pseudo_port_interface": "Virtual-Ethernet1000",
                    "vfi": {
                        "10.0.0.1": {
                            "pw_id": {
                                "Pw2000": {
                                    "discovered_router_id": "10.0.0.1",
                                    "vc_id": 10,
                                    "next_hop": "10.0.0.1",
                                }
                            }
                        },
                        "10.0.0.4": {
                            "pw_id": {
                                "Pw5": {
                                    "discovered_router_id": "-",
                                    "vc_id": 10,
                                    "next_hop": "10.0.0.4",
                                }
                            }
                        },
                        "10.0.0.3": {
                            "pw_id": {
                                "Pw2002": {
                                    "discovered_router_id": "10.1.1.3",
                                    "vc_id": 10,
                                    "next_hop": "10.0.0.3",
                                }
                            }
                        },
                        "10.0.0.2": {
                            "pw_id": {
                                "Pw2001": {
                                    "discovered_router_id": "10.1.1.2",
                                    "vc_id": 10,
                                    "next_hop": "10.0.0.2",
                                }
                            }
                        },
                    },
                }
            },
            "rt": ["10.10.10.10:150"],
            "state": "UP",
            "rd": "9:10",
        }
    }
}
