expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "rp": {
                        "bsr": {
                            "2001:3:3:3::3": {
                                "address": "2001:3:3:3::3",
                                "priority": 5,
                                "mode": "SM",
                                "holdtime": 150,
                                "interval": 60,
                            },
                            "rp_candidate_next_advertisement": "00:00:48",
                        }
                    }
                }
            }
        }
    }
}
