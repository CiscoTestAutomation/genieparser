expected_output = {
    "vrf": {
        "default": {
            "index": {
                1: {
                    "inside_global": "192.168.1.1:514",
                    "inside_local": "192.168.2.3:53",
                    "outside_global": "192.168.2.22:256",
                    "outside_local": "192.168.2.22:256",
                    "protocol": "tcp",
                },
                2: {
                    "inside_global": "192.168.1.1:513",
                    "inside_local": "192.168.2.2:53",
                    "outside_global": "192.168.2.22:256",
                    "outside_local": "192.168.2.22:256",
                    "protocol": "tcp",
                },
                3: {
                    "inside_global": "192.168.1.1:512",
                    "inside_local": "192.168.2.4:53",
                    "outside_global": "192.168.2.22:256",
                    "outside_local": "192.168.2.22:256",
                    "protocol": "tcp",
                },
            }
        },
        "number_of_translations": 3,
    }
}
