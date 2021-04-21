expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "rp": {
                        "bsr": {
                            "rp_candidate_next_advertisement": "00:00:33",
                            "2001:db8:100::1:1:3": {
                                "holdtime": 150,
                                "priority": 192,
                                "interval": 60,
                                "scope": "All Learnt Scoped Zones",
                                "address": "2001:db8:100::1:1:3",
                            },
                        }
                    }
                }
            }
        }
    }
}
