expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv6": {
                    "instance": {
                        "rip ripng": {
                            "redistribute": {
                                "static": {"route_policy": "static-to-rip"},
                                "connected": {},
                            },
                            "interfaces": {
                                "GigabitEthernet3.200": {},
                                "GigabitEthernet2.200": {},
                            },
                        }
                    }
                }
            }
        }
    }
}
