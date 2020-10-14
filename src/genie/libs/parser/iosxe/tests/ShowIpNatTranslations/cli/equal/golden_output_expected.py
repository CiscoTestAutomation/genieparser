expected_output = {
    "vrf": {
        "default": {
            "index": {
                1: {
                    "inside_global": "10.5.5.1:1025",
                    "inside_local": "192.0.2.1:4000",
                    "outside_global": "---",
                    "outside_local": "---",
                    "protocol": "udp",
                },
                2: {
                    "inside_global": "10.5.5.1:1024",
                    "inside_local": "192.0.2.3:4000",
                    "outside_global": "---",
                    "outside_local": "---",
                    "protocol": "udp",
                },
                3: {
                    "inside_global": "10.5.5.1:1026",
                    "inside_local": "192.0.2.2:4000",
                    "outside_global": "---",
                    "outside_local": "---",
                    "protocol": "udp",
                },
            }
        },
        "number_of_translations": 3,
    }
}
