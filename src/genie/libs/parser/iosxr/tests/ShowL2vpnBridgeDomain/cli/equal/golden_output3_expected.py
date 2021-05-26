expected_output = {
    "bridge_group": {
        "SBC-service": {
            "bridge_domain": {
                "bd100": {
                    "id": 0,
                    "state": "up",
                    "shg_id": 0,
                    "mst_i": 0,
                    "mac_aging_time": 300,
                    "mac_limit": 4000,
                    "mac_limit_action": "none",
                    "mac_limit_notification": "syslog",
                    "filter_mac_address": 0,
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "BV100": {"state": "up", "bvi_mac_address": 2},
                            "GigabitEthernet0/4/0/1.100": {
                                "state": "up",
                                "static_mac_address": 0,
                            },
                        },
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "vfi100": {
                            "state": "up",
                            "neighbor": {
                                "10.229.11.11": {
                                    "pw_id": {
                                        100100: {"state": "up", "static_mac_address": 0}
                                    }
                                }
                            },
                        },
                    },
                    "pw": {"num_pw": 1, "num_pw_up": 1},
                    "pbb": {"num_pbb": 0, "num_pbb_up": 0},
                    "vni": {"num_vni": 0, "num_vni_up": 0},
                }
            }
        },
        "evpn_access": {
            "bridge_domain": {
                "100_evpn_access": {
                    "id": 1,
                    "state": "up",
                    "shg_id": 0,
                    "mst_i": 0,
                    "mac_aging_time": 300,
                    "mac_limit": 100,
                    "mac_limit_action": "limit, no-flood",
                    "mac_limit_notification": "syslog, trap",
                    "filter_mac_address": 0,
                    "ac": {
                        "num_ac": 1,
                        "num_ac_up": 1,
                        "interfaces": {
                            "GigabitEthernet0/4/0/6.100": {
                                "state": "up",
                                "static_mac_address": 0,
                                "mst_i": 5,
                            }
                        },
                    },
                    "vfi": {"num_vfi": 0},
                    "pw": {"num_pw": 0, "num_pw_up": 0},
                    "pbb": {"num_pbb": 0, "num_pbb_up": 0},
                    "vni": {"num_vni": 0, "num_vni_up": 0},
                    "evpn": {"EVPN": {"state": "up"}},
                }
            }
        },
    }
}
