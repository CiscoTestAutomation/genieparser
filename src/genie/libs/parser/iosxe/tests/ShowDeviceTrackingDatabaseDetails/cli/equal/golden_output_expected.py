expected_output = {
    "binding_table_configuration": {
        "max/box": "no limit",
        "max/vlan": "no limit",
        "max/port": "no limit",
        "max/mac": "no limit"
    },
    "binding_table_count": {
        "dynamic": 1,
        "local": 1,
        "total": 4
    },
    "binding_table_state_count": {
        "reachable": 1,
        "stale": 2,
        "down": 1,
        "total": 4
    },
    "device": {
        1: {
            "dev_code": "ND",
            "network_layer_address": "100.100.100.1",
            "link_layer_address": "dead.beef.0001(S)",
            "interface": "Twe1/0/42",
            "mode": "access",
            "vlan_id": 39,
            "pref_level_code": 24,
            "age": "92mn",
            "state": "STALE",
            "time_left": "83192 s",
            "filter": "no",
            "in_crimson": "no",
            "client_id": "0000.0000.0000",
            "policy": "test (Device-tracking)"
        },
        2: {
            "dev_code": "L",
            "network_layer_address": "39.39.39.1",
            "link_layer_address": "5c5a.c791.d69f(R)",
            "interface": "Vl39",
            "mode": "svi",
            "vlan_id": 39,
            "pref_level_code": 100,
            "age": "11591mn",
            "state": "REACHABLE",
            "time_left": "",
            "filter": "no",
            "in_crimson": "yes",
            "client_id": "0000.0000.0000",
            "policy": ""
        },
        3: {
            "dev_code": "S",
            "network_layer_address": "10.10.10.10",
            "link_layer_address": "dead.beef.0001(S)",
            "interface": "Twe1/0/42",
            "mode": "access",
            "vlan_id": 39,
            "pref_level_code": 100,
            "age": "59mn",
            "state": "STALE",
            "time_left": "N/A",
            "filter": "no",
            "in_crimson": "yes",
            "client_id": "0000.0000.0000",
            "policy": ""
        },
        4: {
            "dev_code": "S",
            "network_layer_address": "1000::1",
            "link_layer_address": "000a.000b.000c(D)",
            "interface": "Twe1/0/1",
            "mode": "trunk",
            "vlan_id": 100,
            "pref_level_code": 100,
            "age": "30565mn",
            "state": "DOWN",
            "time_left": "N/A",
            "filter": "no",
            "in_crimson": "yes",
            "client_id": "0000.0000.0000",
            "policy": ""
        },
        5: {
            "dev_code": "DH4",
            "network_layer_address": "20.0.0.20",
            "link_layer_address": "000a.000b.000c(D)",
            "interface": "Twe1/0/1",
            "mode": "trunk",
            "vlan_id": 100,
            "pref_level_code": 100,
            "age": "30566mn",
            "state": "DOWN",
            "time_left": "100 s(200 s)",
            "filter": "no",
            "in_crimson": "yes",
            "client_id": "0000.0000.0000",
            "policy": ""
        }        
        
    }
}
