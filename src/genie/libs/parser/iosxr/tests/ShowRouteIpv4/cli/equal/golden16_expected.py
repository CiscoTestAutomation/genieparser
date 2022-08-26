expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "116.119.10.251/32": {
                            "route": "116.119.10.251/32",
                            "ip": "116.119.10.251",
                            "mask": "32",
                            "active": True,
                            "installed": {
                                "date": "Aug 15 14:51:07.021",
                                "for": "47w0d",
                            },
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "outgoing_interface": "Bundle-Ether104",
                                        "from": "116.119.10.251",
                                        "next_hop": "100.72.21.206",
                                        "metric": 10,
                                    },
                                    2: {
                                        "index": 2,
                                        "outgoing_interface": "Bundle-Ether105",
                                        "from": "116.119.10.251",
                                        "next_hop": "100.72.21.209",
                                        "metric": 20,
                                    },
                                }
                            },
                        }
                    }
                }
            }
        }
    }
}
