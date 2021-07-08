expected_output = {
    "GigabitEthernet1/0/1": {
        "address_family": {
            "ipv4": {
                "version": {
                    2: {
                        "groups": {
                            0: {
                                "active_router": "local",
                                "authentication": "5",
                                "authentication_type": "MD5",
                                "default_priority": 100,
                                "group_number": 0,
                                "hsrp_router_state": "active",
                                "last_state_change": "1w0d",
                                "local_virtual_mac_address": "0000.0cff.909f",
                                "local_virtual_mac_address_conf": "v2 default",
                                "preempt": True,
                                "preempt_min_delay": 5,
                                "preempt_reload_delay": 10,
                                "preempt_sync_delay": 20,
                                "primary_ipv4_address": {"address": "192.168.1.254"},
                                "priority": 100,
                                "session_name": "hsrp-Gi1/0/1-0",
                                "standby_ip_address": "192.168.1.2",
                                "standby_router": "192.168.1.2",
                                "standby_priority": 100,
                                "standby_expires_in": 10.624,
                                "statistics": {"num_state_changes": 8},
                                "timers": {
                                    "hello_msec_flag": False,
                                    "hello_sec": 5,
                                    "hold_msec_flag": False,
                                    "hold_sec": 20,
                                    "next_hello_sent": 2.848,
                                },
                                "tracked_objects": {
                                    1: {
                                        "object_name": 1
                                    }
                                },
                                "virtual_mac_address": "0000.0cff.909f",
                                "virtual_mac_address_mac_in_use": True,
                            }
                        }
                    }
                }
            }
        },
        "interface": "GigabitEthernet1/0/1",
        "redirects_disable": False,
        "use_bia": False,
    },
    "GigabitEthernet1/0/2": {
        "address_family": {
            "ipv4": {
                "version": {
                    1: {
                        "groups": {
                            10: {
                                "active_router": "unknown",
                                "authentication": "cisco123",
                                "authentication_type": "MD5",
                                "configured_priority": 110,
                                "group_number": 10,
                                "hsrp_router_state": "disabled",
                                "local_virtual_mac_address": "0000.0cff.b311",
                                "local_virtual_mac_address_conf": "v1 default",
                                "preempt": True,
                                "primary_ipv4_address": {"address": "unknown"},
                                "priority": 110,
                                "session_name": "hsrp-Gi1/0/2-10",
                                "standby_ip_address": "unknown",
                                "standby_router": "unknown",
                                "timers": {
                                    "hello_msec_flag": False,
                                    "hello_sec": 3,
                                    "hold_msec_flag": False,
                                    "hold_sec": 10,
                                },
                                "virtual_mac_address": "unknown",
                                "virtual_mac_address_mac_in_use": False,
                            }
                        }
                    }
                }
            }
        },
        "interface": "GigabitEthernet1/0/2",
        "redirects_disable": False,
        "use_bia": False,
    },
    "GigabitEthernet3": {
        "address_family": {
            "ipv4": {
                "version": {
                    1: {
                        "groups": {
                            10: {
                                "active_expires_in": 0.816,
                                "active_ip_address": "10.1.2.1",
                                "active_router": "10.1.2.1",
                                "active_router_priority": 120,
                                "configured_priority": 110,
                                "group_number": 10,
                                "hsrp_router_state": "standby",
                                "local_virtual_mac_address": "0000.0cff.b311",
                                "local_virtual_mac_address_conf": "v1 default",
                                "preempt": True,
                                "primary_ipv4_address": {"address": "10.1.2.254"},
                                "priority": 110,
                                "session_name": "hsrp-Gi3-10",
                                "standby_router": "local",
                                "timers": {
                                    "hello_msec_flag": False,
                                    "hello_sec": 3,
                                    "hold_msec_flag": False,
                                    "hold_sec": 10,
                                    "next_hello_sent": 2.096,
                                },
                                "virtual_mac_address": "0050.56ff.c8ce",
                                "virtual_mac_address_mac_in_use": False,
                            }
                        }
                    }
                }
            }
        },
        "interface": "GigabitEthernet3",
        "redirects_disable": False,
        "use_bia": False,
    },
}
