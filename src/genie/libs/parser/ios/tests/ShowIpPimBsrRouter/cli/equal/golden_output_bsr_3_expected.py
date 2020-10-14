expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "rp": {
                        "bsr": {
                            "Loopback0": {
                                "interface": "Loopback0",
                                "address": "10.16.2.2",
                                "holdtime": 150,
                                "next_advertisment": "00:00:26",
                                "priority": 10,
                                "interval": 60,
                            },
                            "bsr": {
                                "address": "10.64.4.4",
                                "hash_mask_length": 0,
                                "priority": 0,
                                "address_host": "?",
                                "up_time": "3d07h",
                            },
                            "bsr_next_bootstrap": "00:00:06",
                        }
                    }
                }
            }
        }
    }
}
