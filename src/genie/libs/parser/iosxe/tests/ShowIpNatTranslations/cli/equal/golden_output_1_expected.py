expected_output = {
    "vrf": {
        "default": {
            "index": {
                1: {
                    "inside_global": "10.1.7.2",
                    "inside_local": "192.168.1.95",
                    "outside_global": "---",
                    "outside_local": "---",
                    "protocol": "---",
                },
                2: {
                    "inside_global": "10.1.7.200",
                    "inside_local": "192.168.1.89",
                    "outside_global": "--",
                    "outside_local": "---",
                    "protocol": "---",
                },
            }
        },
        "number_of_translations": 2,
    }
}
