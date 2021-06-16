expected_output = {
    "bridge_group": {
        "EVPN-Mulicast": {
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
                        "num_ac": 3,
                        "num_ac_up": 2,
                        "interfaces": {
                            "BV100": {"state": "up", "bvi_mac_address": 1},
                            "Bundle-Ether3.100": {
                                "state": "down",
                                "static_mac_address": 0,
                                "mst_i": 5,
                            },
                            "Bundle-Ether4.100": {
                                "state": "up",
                                "static_mac_address": 0,
                                "mst_i": 5,
                            },
                        },
                    },
                    "vfi": {"num_vfi": 0},
                    "pw": {"num_pw": 0, "num_pw_up": 0},
                    "pbb": {"num_pbb": 0, "num_pbb_up": 0},
                    "vni": {"num_vni": 0, "num_vni_up": 0},
                    "evpn": {"EVPN": {"state": "up"}},
                }
            }
        }
    }
}
