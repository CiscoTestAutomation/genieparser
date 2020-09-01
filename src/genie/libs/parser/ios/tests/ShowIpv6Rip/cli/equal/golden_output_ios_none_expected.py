expected_output = {
    "vrf": {
        "one": {
            "address_family": {
                "ipv6": {
                    "distance": 25,
                    "interfaces": {"Ethernet2": {}},
                    "maximum_paths": 4,
                    "multicast_group": "FF02::9",
                    "originate_default_route": {"enabled": False},
                    "pid": 55,
                    "poison_reverse": False,
                    "port": 521,
                    "split_horizon": True,
                    "statistics": {"periodic_updates": 8883, "trigger_updates": 2},
                    "timers": {
                        "expire_time": 180,
                        "flush_interval": 120,
                        "holddown_interval": 0,
                        "update_interval": 30,
                    },
                }
            }
        },
        "two": {
            "address_family": {
                "ipv6": {
                    "distance": 120,
                    "maximum_paths": 4,
                    "multicast_group": "FF02::9",
                    "originate_default_route": {"enabled": False},
                    "pid": 61,
                    "poison_reverse": False,
                    "port": 521,
                    "split_horizon": True,
                    "statistics": {"periodic_updates": 8883, "trigger_updates": 0},
                    "timers": {
                        "expire_time": 180,
                        "flush_interval": 120,
                        "holddown_interval": 0,
                        "update_interval": 30,
                    },
                }
            }
        },
    }
}
