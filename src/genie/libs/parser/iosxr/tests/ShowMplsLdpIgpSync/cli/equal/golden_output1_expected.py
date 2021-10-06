expected_output = {
    "vrf": {
        "default": {
            "interfaces": {
                "HundredGigE0/0/0/0": {
                    "sync": {
                        "delay": "Disabled",
                        "status": "Ready",
                        "peers": {
                            "63.63.63.63:0": {"graceful_restart": True},
                            "63.63.63.65:0": {"graceful_restart": True},
                        },
                    }
                },
                "TenGigE0/2/0/0": {
                    "sync": {
                        "delay": "Disabled",
                        "status": "Not ready (No hello adjacency)",
                    }
                },
                "TenGigE0/2/0/3": {
                    "sync": {
                        "delay": "Disabled",
                        "status": "Ready",
                        "peers": {"107.107.107.107:0": {"graceful_restart": True}},
                    }
                },
            },
            "vrf_index": "0x60000000",
        }
    }
}
