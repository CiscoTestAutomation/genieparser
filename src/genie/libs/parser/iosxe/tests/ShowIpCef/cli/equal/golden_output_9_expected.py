expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "192.168.100.252/32": {
                            "nexthop": {
                                "10.169.196.213": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/3/6": {
                                            "local_label": 16051,
                                            "outgoing_label": ["16051"],
                                            "sid": "453955",
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
