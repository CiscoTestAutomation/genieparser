expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "10.2.3.0/24": {
                            "nexthop": {
                                "10.1.2.2": {
                                    "outgoing_interface": {"GigabitEthernet2.100": {}}
                                },
                                "10.1.3.3": {
                                    "outgoing_interface": {"GigabitEthernet3.100": {}}
                                },
                            }
                        }
                    }
                }
            }
        }
    }
}
