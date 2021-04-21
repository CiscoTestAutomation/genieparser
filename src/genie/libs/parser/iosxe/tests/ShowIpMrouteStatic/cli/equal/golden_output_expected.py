expected_output = {
    "vrf": {
        "default": {
            "mroute": {
                "172.16.0.0/16": {
                    "path": {
                        "172.30.10.13 1": {
                            "neighbor_address": "172.30.10.13",
                            "admin_distance": "1",
                        }
                    }
                },
                "172.16.1.0/24": {
                    "path": {
                        "172.30.10.13 1": {
                            "neighbor_address": "172.30.10.13",
                            "admin_distance": "1",
                        }
                    }
                },
            }
        }
    }
}
