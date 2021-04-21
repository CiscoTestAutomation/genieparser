expected_output = {
    "vrf": {
        "process1": {
            "address_family": {
                "ipv6": {
                    "distance": 120,
                    "interfaces": {"Gigabitethernet0/0/0": {}},
                    "maximum_paths": 1,
                    "multicast_group": "FF02::9",
                    "originate_default_route": {"enabled": True},
                    "pid": 62,
                    "poison_reverse": False,
                    "port": 521,
                    "redistribute": {"bgp": {65001: {"route_policy": "bgp-to-rip"}}},
                    "split_horizon": True,
                    "statistics": {"periodic_updates": 223, "trigger_updates": 1},
                    "timers": {
                        "expire_time": 15,
                        "flush_interval": 30,
                        "holddown_interval": 10,
                        "update_interval": 5,
                    },
                }
            }
        }
    }
}
