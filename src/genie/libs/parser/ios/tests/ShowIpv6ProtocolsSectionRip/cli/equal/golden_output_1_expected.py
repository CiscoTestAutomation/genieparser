expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "instance": {
                        "rip ripng": {
                            "redistribute": {"static": {"metric": 3}},
                            "interfaces": {
                                "GigabitEthernet3.100": {},
                                "GigabitEthernet2.100": {},
                            },
                        }
                    }
                }
            }
        }
    }
}
