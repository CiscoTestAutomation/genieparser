expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv6": {
                    "rp": {
                        "bsr": {
                            "2001:DB8:1:5::1": {
                                "address": "2001:DB8:1:5::1",
                                "priority": 192,
                                "mode": "SM",
                                "holdtime": 150,
                                "interval": 60,
                            },
                            "rp_candidate_next_advertisement": "00:00:50",
                        }
                    }
                }
            }
        }
    }
}
