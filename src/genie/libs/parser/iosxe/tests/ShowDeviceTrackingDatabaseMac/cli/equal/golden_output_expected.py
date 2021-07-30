expected_output = {
    "device": {
        1: {
            "link_layer_address": "dead.beef.0001",
            "interface": "Twe1/0/42",
            "vlan_id": 39,
            "pref_level_code": "NO TRUST",
            "state": "MAC-STALE",
            "policy": "49",
        },
        2: {
           "link_layer_address": "5c5a.c791.d69f",
            "interface": "Vl39",
            "vlan_id": 39,
            "pref_level_code": "TRUSTED",
            "state": "MAC-REACHABLE",
            "policy": "dna_policy",
            "input_index": 108,
        },
        3: {
           "link_layer_address": "0050.56b0.babc",
            "interface": "Twe1/0/42",
            "vlan_id": 39,
            "pref_level_code": "NO TRUST",
            "state": "MAC-REACHABLE",
            "time_left": "41 s",
            "policy": "test1",
            "input_index": 49,
        },
        4: {
           "link_layer_address": "0050.56b0.afed",
            "interface": "Twe1/0/42",
            "vlan_id": 39,
            "pref_level_code": "NO TRUST",
            "state": "MAC-REACHABLE",
            "time_left": "21 s",
            "policy": "test1",
            "input_index": 49,
        },
        5: {
           "link_layer_address": "000a.000b.000c",
            "interface": "Twe1/0/1",
            "vlan_id": 100,
            "pref_level_code": "NO TRUST",
            "state": "MAC-DOWN",
            "policy": "8",
        },
    }
}