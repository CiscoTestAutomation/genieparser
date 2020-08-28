expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv4": {
                    "rp": {
                        "bsr": {
                            "GigabitEthernet0/2": {
                                "interface": "GigabitEthernet0/2",
                                "address": "10.4.6.4",
                                "holdtime": 150,
                                "next_advertisment": "00:00:00",
                                "priority": 5,
                                "interval": 60,
                            },
                            "bsr": {
                                "address": "10.4.6.6",
                                "hash_mask_length": 0,
                                "priority": 0,
                                "address_host": "?",
                                "up_time": "4d03h",
                                "expires": "00:02:00",
                            },
                        }
                    }
                }
            }
        }
    }
}
