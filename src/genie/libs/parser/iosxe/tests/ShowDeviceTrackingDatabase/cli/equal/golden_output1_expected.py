expected_output = {
    "binding_table_count": 4,
    "dynamic_entry_count": 3,
    "binding_table_limit": 200000,
    "device": {
        1: {
            "dev_code": "S",
            "network_layer_address": "10.10.10.10",
            "link_layer_address": "7081.05ff.eb41",
            "interface": "E0/0",
            "vlan_id": 228,
            "pref_level_code": 100,
            "age": "10330mn",
            "state": "REACHABLE",
            "time_left": "N/A"
        },
        2: {
            "dev_code": "ND",
            "network_layer_address": "10.10.10.11",
            "link_layer_address": "7081.05ff.eb42",
            "interface": "E0/1",
            "vlan_id": 226,
            "pref_level_code": 5,
            "age": "235mn",
            "state": "STALE",
            "time_left": "try 0 73072 s"
        },
        3: {
            "dev_code": "ND",
            "network_layer_address": "10.10.10.12",
            "link_layer_address": "7081.05ff.eb43",
            "interface": "E0/2",
            "vlan_id": 224,
            "pref_level_code": 5,
            "age": "60s",
            "state": "REACHABLE",
            "time_left": "250 s"
        },
        4: {
            "dev_code": "ARP",
            "network_layer_address": "10.10.10.13",
            "link_layer_address": "7081.05ff.eb44",
            "interface": "E0/3",
            "vlan_id": 222,
            "pref_level_code": 5,
            "age": "3mn",
            "state": "REACHABLE",
            "time_left": "83 s try 0"
        }
    }
}
