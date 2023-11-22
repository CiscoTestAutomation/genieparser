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
            },
            3: {
                "dev_code": "L2F",
                "link_layer_address": "0001.0002.0001",
                "interface": "Gi1/0/23",
                "vlan_id": 110,
                "pref_level": "NO TRUST",
                "state": "MAC-REACHABLE",
                "time_left": "231 s",
                "policy": "LISP-DT-GLEAN-VLAN-MULTI-IP",
                "input_index": 31,
            },      
            4: {
                "dev_code": "L",
                "link_layer_address": "ba25.cdf4.ad38",
                "interface": "Vl110",
                "vlan_id": 110,
                "pref_level": "TRUSTED",
                "state": "MAC-REACHABLE",
                "time_left": "N/A",
                "policy": "LISP-DT-GLEAN-VLAN-MULTI-IP",
                "input_index": 60,
            }              
        }
}