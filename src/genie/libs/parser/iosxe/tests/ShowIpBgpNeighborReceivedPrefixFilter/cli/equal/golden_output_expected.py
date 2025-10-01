expected_output = {
    "address_family": {
        "IPv4 Unicast": {
            "ip_prefix_list": {
                "3.3.3.3": {
                    "entries": 3,
                    "sequences": {
                        10: {
                            "action": "permit",
                            "prefix": "3.3.3.0/24"
                        },
                        20: {
                            "action": "permit",
                            "prefix": "33.33.33.11/32"
                        },
                        30: {
                            "action": "permit",
                            "prefix": "84.0.0.0/8"
                        }
                    }
                }
            }
        }
    }
}