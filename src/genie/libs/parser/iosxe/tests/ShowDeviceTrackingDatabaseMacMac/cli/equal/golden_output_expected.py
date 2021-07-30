expected_output = {
    "macDB_count": 2,
    "vlan": 38,
    "dynamic_count": 0,
    "entries": {
        1: {
            "dev_code": "S",
            "network_layer_address": "10.10.10.11",
            "link_layer_address": "dead.beef.0001",
            "interface": "Twe1/0/41",
            "vlan_id": 38,
            "pref_level_code": 100,
            "age": "4s",
            "state": "REACHABLE",
            "time_left": "308 s",
        },
        2: {
            "dev_code": "S",
            "network_layer_address": "10.10.10.10",
            "link_layer_address": "dead.beef.0001",
            "interface": "Twe1/0/42",
            "vlan_id": 38,
            "pref_level_code": 100,
            "age": "4173mn",
            "state": "STALE",
        },
    }
}