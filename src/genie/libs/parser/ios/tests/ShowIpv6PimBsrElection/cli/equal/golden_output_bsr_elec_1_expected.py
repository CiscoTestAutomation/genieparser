expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv6": {
                    "rp": {
                        "bsr": {
                            "bsr_candidate": {
                                "address": "2001:DB8:1:5::1",
                                "priority": 0,
                                "hash_mask_length": 126,
                            },
                            "bsr": {
                                "address": "2001:DB8:1:5::1",
                                "hash_mask_length": 126,
                                "priority": 0,
                                "up_time": "00:08:39",
                                "scope_range_list": "ff00::/8",
                                "rpf_address": "FE80::5054:FF:FEC3:D71C",
                                "rpf_interface": "GigabitEthernet3",
                                "expires": "00:00:22",
                            },
                        }
                    }
                }
            }
        }
    }
}
