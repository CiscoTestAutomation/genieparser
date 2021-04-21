expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "rp": {
                        "bsr": {
                            "bsr_candidate": {
                                "address": "2001:1:1:1::1",
                                "priority": 0,
                                "hash_mask_length": 126,
                            },
                            "bsr": {
                                "address": "2001:1:1:1::1",
                                "hash_mask_length": 126,
                                "priority": 0,
                                "up_time": "00:00:07",
                                "scope_range_list": "ff00::/8",
                                "rpf_address": "FE80::21E:F6FF:FE2D:3600",
                                "rpf_interface": "Loopback0",
                                "expires": "00:00:52",
                            },
                        }
                    }
                }
            }
        }
    }
}
