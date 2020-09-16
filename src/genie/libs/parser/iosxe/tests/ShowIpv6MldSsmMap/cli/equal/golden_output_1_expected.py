expected_output = {
    "vrf": {
        "VRF1": {
            "ssm_map": {
                "2001:DB8:1:1::1 FF35:1::1": {
                    "source_addr": "2001:DB8:1:1::1",
                    "group_address": "FF35:1::1",
                    "database": "static",
                    "group_mode_ssm": False,
                },
                "2001:DB8::3 FF35:1::1": {
                    "source_addr": "2001:DB8::3",
                    "group_address": "FF35:1::1",
                    "database": "static",
                    "group_mode_ssm": False,
                },
            }
        }
    }
}
