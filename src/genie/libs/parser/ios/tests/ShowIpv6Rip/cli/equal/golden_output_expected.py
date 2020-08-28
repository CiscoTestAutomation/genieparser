expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "port": 521,
                    "multicast_group": "FF02::9",
                    "pid": 635,
                    "distance": 120,
                    "maximum_paths": 16,
                    "split_horizon": True,
                    "poison_reverse": False,
                    "originate_default_route": {"enabled": False},
                    "timers": {
                        "flush_interval": 120,
                        "holddown_interval": 0,
                        "update_interval": 30,
                        "expire_time": 180,
                    },
                    "redistribute": {"static": {"metric": 3}},
                    "interfaces": {
                        "GigabitEthernet3.100": {},
                        "GigabitEthernet2.100": {},
                    },
                    "statistics": {
                        "periodic_updates": 399,
                        "delayed_events": 0,
                        "trigger_updates": 8,
                        "full_advertisement": 0,
                    },
                }
            }
        }
    }
}
