expected_output = {
    "device": {
            1: {
                "dev_code": "S",
                "link_layer_address": "dead.beef.0001",
                "interface": "Twe1/0/41",
                "vlan_id": 38,
                "pref_level": "TRUSTED",
                "state": "MAC-STALE",
                "time_left": "93013 s",
                "policy": "47",
                "attached": {
                    1: {
                        "ip": "10.10.10.11",
                    },
                    2: {
                        "ip": "10.10.10.10"
                    }
                }
            },
            2: {
                "dev_code": "L",
                "link_layer_address": "c4b2.39ae.51df",
                "interface": "Vl1",
                "vlan_id": 1,
                "pref_level": "TRUSTED",
                "state": "MAC-DOWN",
                "policy": "default",
                "input_index": 60,
            }
        }
}