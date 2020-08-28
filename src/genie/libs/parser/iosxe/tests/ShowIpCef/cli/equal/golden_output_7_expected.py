expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "0.0.0.0/0": {
                            "epoch": 3,
                            "flags": ["default route handler", "default route"],
                            "nexthop": {"no route": {}},
                        }
                    }
                }
            }
        }
    }
}
