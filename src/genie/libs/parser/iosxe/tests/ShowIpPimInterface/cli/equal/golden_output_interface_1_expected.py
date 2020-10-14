expected_output = {
    "vrf": {
        "default": {
            "interfaces": {
                "GigabitEthernet1": {
                    "address_family": {
                        "ipv4": {
                            "dr_priority": 1,
                            "hello_interval": 30,
                            "neighbor_count": 1,
                            "version": 2,
                            "mode": "sparse-mode",
                            "dr_address": "10.1.2.2",
                            "address": ["10.1.2.1"],
                        }
                    }
                },
                "GigabitEthernet2": {
                    "address_family": {
                        "ipv4": {
                            "dr_priority": 1,
                            "hello_interval": 30,
                            "neighbor_count": 1,
                            "version": 2,
                            "mode": "sparse-mode",
                            "dr_address": "10.1.3.3",
                            "address": ["10.1.3.1"],
                        }
                    }
                },
                "Loopback0": {
                    "address_family": {
                        "ipv4": {
                            "dr_priority": 1,
                            "hello_interval": 30,
                            "neighbor_count": 0,
                            "version": 2,
                            "mode": "sparse-mode",
                            "dr_address": "10.4.1.1",
                            "address": ["10.4.1.1"],
                        }
                    }
                },
            }
        }
    }
}
