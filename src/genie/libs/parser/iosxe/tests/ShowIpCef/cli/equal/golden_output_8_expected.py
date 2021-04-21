expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "10.169.196.241/32": {
                            "nexthop": {
                                "10.0.0.10": {
                                    "outgoing_interface": {
                                        "GigabitEthernet3": {
                                            "local_label": 16022,
                                            "outgoing_label": ["16022"],
                                            "outgoing_label_backup": "16002",
                                            "outgoing_label_info": "elc",
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
