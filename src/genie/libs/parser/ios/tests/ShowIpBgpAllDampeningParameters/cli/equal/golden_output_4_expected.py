expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4 unicast": {
                    "dampening": True,
                    "dampening_decay_time": 4200,
                    "dampening_half_life_time": 2100,
                    "dampening_reuse_time": 200,
                    "dampening_max_suppress_time": 4200,
                    "dampening_suppress_time": 200,
                    "dampening_max_suppress_penalty": 800,
                }
            }
        },
        "VRF1": {
            "address_family": {
                "vpnv4 unicast": {
                    "dampening": True,
                    "dampening_decay_time": 4240,
                    "dampening_half_life_time": 2160,
                    "dampening_reuse_time": 2001,
                    "dampening_max_suppress_time": 4260,
                    "dampening_suppress_time": 2001,
                    "dampening_max_suppress_penalty": 7850,
                }
            }
        },
    }
}
