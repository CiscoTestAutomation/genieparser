expected_output = {
    "protocols": {
        "bgp": {
            "bgp_pid": 40,
            "address_family": {
                "IPv4 Unicast": {
                    "distance": {
                        "external": 20,
                        "internal": 200,
                        "local": 200
                    },
                    "sourced_networks": [
                        "10.100.0.0/16 backdoor",
                        "10.100.1.0/24",
                        "10.100.2.0/24"
                    ],
                    "neighbors": {
                        "10.5.0.2": {
                            "last_update": "Idle"
                        },
                        "10.9.0.3": {
                            "last_update": "Idle"
                        }
                    }
                }
            }
        }
    }
}