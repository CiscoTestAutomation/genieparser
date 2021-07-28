expected_output = {
    "vrf": {
        "DEVICE_VN": {
            "eid": {
                "192.168.11.11/32": {
                    "locator_set": [
                        "192_168_11_0-DEVICE_VN-IPV4",
                        "inherited from default locator-set rloc_aba7a76a-fadd-4f6e-a44e-ef4258a1c129"
                    ],
                    "rlocs": {
                        "172.24.0.3": {
                            "priority": 10,
                            "source": "cfg-intf",
                            "state": [
                                "site-self",
                                "reachable"
                            ],
                            "weight": 10
                        }
                    }
                }
            },
            "iid": 4100,
            "inactive": 0,
            "lsb": "0x1",
            "no_route": 0,
            "total_entries": 2
        }
    }
}