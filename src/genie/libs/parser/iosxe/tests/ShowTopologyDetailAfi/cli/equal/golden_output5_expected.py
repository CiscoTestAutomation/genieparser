expected_output = {
    "topologies": {
        "base": {
            "address_families": {
                "ipv4 multicast": {
                    "vrfs": {
                        "default": {
                            "state": "DOWN",
                            "cef_forwarding": "disabled",
                            "lock_count": 4,
                            "mcast_multitopology": True,
                            "use_topo_afi": "ipv4",
                            "use_topo_name": "t1",
                            "user_lock_count": 0
                        }
                    }
                }
            }
        },
        "bar": {
            "address_families": {
                "ipv4 multicast": {
                    "vrfs": {
                        "default": {
                            "state": "DOWN",
                            "cef_forwarding": "disabled",
                            "lock_count": 2,
                            "use_topo_afi": "ipv4",
                            "use_topo_name": "t1",
                            "user_lock_count": 0
                        }
                    }
                }
            }
        },
        "test": {
            "address_families": {
                "ipv4 multicast": {
                    "vrfs": {
                        "default": {
                            "state": "DOWN",
                            "cef_forwarding": "disabled",
                            "lock_count": 2,
                            "use_topo_afi": "ipv4",
                            "use_topo_name": "t1",
                            "user_lock_count": 0
                        }
                    }
                }
            }
        }
    }
}
