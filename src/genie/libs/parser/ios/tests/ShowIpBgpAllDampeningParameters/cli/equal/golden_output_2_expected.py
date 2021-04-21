expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4 unicast": {
                    "dampening": True,
                    "dampening_decay_time": 2320,
                    "dampening_half_life_time": 900,
                    "dampening_reuse_time": 750,
                    "dampening_max_suppress_time": 3600,
                    "dampening_suppress_time": 2000,
                    "dampening_max_suppress_penalty": 12000,
                },
                "vpnv4 unicast": {
                    "dampening": True,
                    "dampening_decay_time": 2320,
                    "dampening_half_life_time": 900,
                    "dampening_reuse_time": 750,
                    "dampening_max_suppress_time": 3600,
                    "dampening_suppress_time": 2000,
                    "dampening_max_suppress_penalty": 12000,
                },
            }
        },
        "VRF1": {
            "address_family": {
                "vpnv4 unicast": {
                    "dampening": True,
                    "dampening_decay_time": 2320,
                    "dampening_half_life_time": 900,
                    "dampening_reuse_time": 750,
                    "dampening_max_suppress_time": 3600,
                    "dampening_suppress_time": 2000,
                    "dampening_max_suppress_penalty": 12000,
                }
            }
        },
    }
}
