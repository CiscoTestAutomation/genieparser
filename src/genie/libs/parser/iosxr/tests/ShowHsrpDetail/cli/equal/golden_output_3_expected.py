expected_output = {
    "Bundle-Ether4.1296": {
        "address_family": {
            "ipv4": {
                "version": {
                    2: {
                        "groups": {
                            1296: {
                                "active_ip_address": "local",
                                "active_priority": 110,
                                "active_router": "local",
                                "group_number": 1296,
                                "hsrp_router_state": "active",
                                "preempt": True,
                                "primary_ipv4_address": {
                                    "address": "10.229.254.158"
                                },
                                "priority": 110,
                                "standby_ip_address": "unknown",
                                "standby_router": "unknown",
                                "standby_state": "active",
                                "statistics": {
                                    "last_coup_received": "Never",
                                    "last_coup_sent": "Never",
                                    "last_resign_received": "Never",
                                    "last_resign_sent": "Never",
                                    "last_state_change": "10w4d",
                                    "num_state_changes": 4
                                },
                                "timers": {
                                    "hello_msec": 3000,
                                    "hello_msec_flag": True,
                                    "hold_msec": 10000,
                                    "hold_msec_flag": True
                                },
                                "virtual_mac_address": "0000.0c9f.f510"
                            }
                        }
                    }
                }
            }
        },
        "delay": {
            "minimum_delay": 30,
            "reload_delay": 60
        },
        "interface": "Bundle-Ether4.1296",
        "redirects_disable": False,
        "use_bia": False
    }
}