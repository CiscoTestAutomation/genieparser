expected_output = {
    "vrf": {
        "default": {
            "index": {
                1: {
                    "inside_global": "192.168.33.28:228",
                    "inside_local": "172.25.0.1:228",
                    "outside_global": "192.168.33.1:228",
                    "outside_local": "192.168.33.1:228",
                    "protocol": "icmp",
                },
                2: {
                    "inside_global": "192.168.33.28:229",
                    "inside_local": "172.25.0.1:229",
                    "outside_global": "192.168.33.28:229",
                    "outside_local": "192.168.33.28:229",
                    "protocol": "icmp",
                },
                3: {
                    "inside_global": "192.168.33.28:230",
                    "inside_local": "172.25.0.1:230",
                    "outside_global": "10.1.8.8:230",
                    "outside_local": "10.1.8.8:230",
                    "protocol": "icmp",
                },
                4: {
                    "inside_global": "192.168.33.28:231",
                    "inside_local": "172.25.0.1:231",
                    "outside_global": "192.168.219.1:231",
                    "outside_local": "192.168.219.1:231",
                    "protocol": "icmp",
                },
                5: {
                    "inside_global": "192.168.33.28:27432",
                    "inside_local": "172.25.0.2:27432",
                    "outside_global": "10.1.8.8:27432",
                    "outside_local": "10.1.8.8:27432",
                    "protocol": "icmp",
                },
            }
        }
    }
}
