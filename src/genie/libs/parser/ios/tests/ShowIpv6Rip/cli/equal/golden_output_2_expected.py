expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv6": {
                    "port": 521,
                    "multicast_group": "FF02::9",
                    "pid": 635,
                    "distance": 120,
                    "maximum_paths": 16,
                    "split_horizon": True,
                    "poison_reverse": False,
                    "originate_default_route": {"enabled": True},
                    "timers": {
                        "flush_interval": 120,
                        "holddown_interval": 0,
                        "update_interval": 30,
                        "expire_time": 180,
                    },
                    "redistribute": {
                        "static": {"route_policy": "static-to-rip"},
                        "connected": {},
                    },
                    "interfaces": {
                        "GigabitEthernet3.200": {},
                        "GigabitEthernet2.200": {},
                    },
                    "statistics": {
                        "periodic_updates": 390,
                        "delayed_events": 0,
                        "trigger_updates": 3,
                        "full_advertisement": 0,
                    },
                }
            }
        }
    }
}
