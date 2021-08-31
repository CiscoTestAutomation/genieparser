expected_output = {
    "binding_table_configuration": {
        "max/box": "no limit",
        "max/port": "no limit",
        "max/vlan": "no limit",
        "max/mac": "no limit",
    },
    "binding_table_count": {
        "dynamic": 0,
        "local": 0,
        "total": 2,
    },
    "binding_table_state_count": {
        "reachable": 2,
        "total": 2,
    },
    "entry_count": 2,
    "vlan_id": 38,
    "dynamic_count": 0,
    "entries":{
        1: {
            "dev_code": "S",
            "network_layer_address": "10.10.10.11",
            "link_layer_address": "dead.beef.0001(R)",
            "interface": "Twe1/0/41",
            "mode": "trunk",
            "vlan_id": 38,
            "pref_level_code": 100,
            "age": "63s",
            "state": "REACHABLE",
            "time_left": "249 s",
            "filter": "no",
            "in_crimson": "yes",
            "client_id": "0000.0000.0000",
        },
        2: {
            "dev_code": "S",
            "network_layer_address": "10.10.10.10",
            "link_layer_address": "dead.beef.0001(R)",
            "interface": "Twe1/0/41",
            "mode": "trunk",
            "vlan_id": 38,
            "pref_level_code": 100,
            "age": "136s",
            "state": "REACHABLE",
            "time_left": "167 s",
            "filter": "no",
            "in_crimson": "yes",
            "client_id": "0000.0000.0000",
        }
    }
}