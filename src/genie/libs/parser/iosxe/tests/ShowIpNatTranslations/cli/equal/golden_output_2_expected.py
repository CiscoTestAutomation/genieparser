expected_output = {
    "vrf": {
        "default": {
            "index": {
                1: {
                    "inside_global": "10.1.7.2:1220",
                    "inside_local": "192.168.1.95:1220",
                    "outside_global": "10.100.20.100:53",
                    "outside_local": "10.100.20.100:53",
                    "protocol": "udp",
                },
                2: {
                    "inside_global": "10.1.7.2:11012",
                    "inside_local": "192.168.1.89:11012",
                    "outside_global": "10.26.102.100:23",
                    "outside_local": "10.26.102.100:23",
                    "protocol": "tcp",
                },
                3: {
                    "inside_global": "10.1.7.2:1067",
                    "inside_local": "192.168.1.95:1067",
                    "outside_global": "10.220.2.25:23",
                    "outside_local": "10.220.2.25:23",
                    "protocol": "tcp",
                },
            }
        },
        "number_of_translations": 3,
    }
}
