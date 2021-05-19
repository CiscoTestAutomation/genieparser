expected_output = {
    "bridge_group": {
        "g1": {
            "bridge_domain": {
                "EVPN-Multicast-Genie": {
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
                        "num_ac": 1,
                        "num_ac_up": 1,
                        "interfaces": {
                            "GigabitEthernet0/1/0/0": {
                                "state": "up",
                                "static_mac_address": 2,
                                "mst_i": 0,
                                "mst_i_state": "unprotected",
                            }
                        },
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "1": {
                            "neighbor": {
                                "10.1.1.1": {
                                    "pw_id": {
                                        1: {"state": "up", "static_mac_address": 0}
                                    }
                                }
                            }
                        },
                    },
                    "pw": {"num_pw": 1, "num_pw_up": 1},
                }
            }
        }
    }
}