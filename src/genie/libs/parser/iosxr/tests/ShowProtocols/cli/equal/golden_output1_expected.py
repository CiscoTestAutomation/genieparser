expected_output = {
    "protocols": {
        "bgp": {
            "bgp_pid": 100,
            "nsr": {
                "enabled": True,
                "current_state": "tcp initial sync"
            },
            "address_family": {
                "VPNv4 Unicast": {
                    "distance": {
                        "external": 20,
                        "internal": 200,
                        "local": 200
                    }
                },
                "VPNv6 Unicast": {
                    "distance": {
                        "external": 20,
                        "internal": 200,
                        "local": 200
                    }
                }
            }
        }
    }
}