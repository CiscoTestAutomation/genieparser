expected_output = {
    "vrf": {
        "VRF1": {
            "interfaces": {
                "GigabitEthernet3": {
                    "address_family": {
                        "ipv4": {
                            "dr_priority": 1,
                            "hello_interval": 30,
                            "neighbor_count": 1,
                            "version": 2,
                            "mode": "dense-mode",
                            "dr_address": "10.1.5.5",
                            "address": ["10.1.5.1"],
                        }
                    }
                }
            }
        }
    }
}
