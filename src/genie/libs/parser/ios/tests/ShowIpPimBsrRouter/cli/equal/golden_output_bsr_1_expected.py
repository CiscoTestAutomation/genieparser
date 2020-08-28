expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv4": {
                    "rp": {
                        "bsr": {
                            "GigabitEthernet3": {
                                "interface": "GigabitEthernet3",
                                "address": "10.1.5.1",
                                "holdtime": 150,
                                "next_advertisment": "00:00:27",
                                "priority": 5,
                                "interval": 60,
                            },
                            "bsr": {
                                "address": "10.1.5.5",
                                "hash_mask_length": 0,
                                "priority": 0,
                                "address_host": "?",
                                "up_time": "00:00:26",
                                "expires": "00:01:45",
                            },
                        }
                    }
                }
            }
        }
    }
}
