expected_output = {
    "BDI3147": {
        "interface": "BDI3147",
        "redirects_disable": False,
        "address_family": {
            "ipv4": {
                "version": {
                    1: {
                        "groups": {
                            31: {
                                "group_number": 31,
                                "hsrp_router_state": "active",
                                "statistics": {
                                    "num_state_changes": 17
                                },
                                "last_state_change": "12w6d",
                                "primary_ipv4_address": {
                                    "address": "10.190.99.49"
                                },
                                "virtual_mac_address": "0000.0c07.ac1f",
                                "virtual_mac_address_mac_in_use": True,
                                "local_virtual_mac_address": "0000.0c07.ac1f",
                                "local_virtual_mac_address_conf": "v1 default",
                                "timers": {
                                    "hello_msec_flag": False,
                                    "hello_sec": 3,
                                    "hold_msec_flag": False,
                                    "hold_sec": 10,
                                    "next_hello_sent": 1.856
                                },
                                "active_router": "local",
                                "standby_priority": 90,
                                "standby_expires_in": 11.504,
                                "standby_router": "10.190.99.51",
                                "standby_ip_address": "10.190.99.51",
                                "priority": 110,
                                "configured_priority": 110,
                                "session_name": "hsrp-BD3147-31"
                            },
                            32: {
                                "group_number": 32,
                                "hsrp_router_state": "active",
                                "statistics": {
                                    "num_state_changes": 17
                                },
                                "last_state_change": "12w6d",
                                "primary_ipv4_address": {
                                    "address": "10.188.109.1"
                                },
                                "virtual_mac_address": "0000.0c07.ac20",
                                "virtual_mac_address_mac_in_use": True,
                                "local_virtual_mac_address": "0000.0c07.ac20",
                                "local_virtual_mac_address_conf": "v1 default",
                                "timers": {
                                    "hello_msec_flag": False,
                                    "hello_sec": 3,
                                    "hold_msec_flag": False,
                                    "hold_sec": 10,
                                    "next_hello_sent": 2.496
                                },
                                "active_router": "local",
                                "standby_priority": 90,
                                "standby_expires_in": 10.576,
                                "standby_router": "10.188.109.3",
                                "standby_ip_address": "10.188.109.3",
                                "priority": 110,
                                "configured_priority": 110,
                                "session_name": "hsrp-BD3147-32"
                            }
                        }
                    }
                }
            }
        },
        "use_bia": False
    }
}
