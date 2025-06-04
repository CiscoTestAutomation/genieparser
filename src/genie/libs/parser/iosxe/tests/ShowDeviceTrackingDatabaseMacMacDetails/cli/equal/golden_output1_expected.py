expected_output = {
    "binding_table_configuration": {
        "max/box": "no limit",
        "max/vlan": "no limit",
        "max/port": "no limit",
        "max/mac": "no limit"
    },
    "binding_table_count": {
        "dynamic": 5,
        "local": 13,
        "total": 18
    },
    "binding_table_state_count": {
        "reachable": 17,
        "unknown": 1,
        "total": 18
    },
    "entry_count": 2,
    "vlan_id": 2045,
    "dynamic_count": 2,
    "entries": {
        1: {
            "dev_code": "DH4",
            "network_layer_address": "172.19.5.10",
            "link_layer_address": "b811.4b0e.2630(R)",
            "interface": "Te1/0/14",
            "mode": "trunk",
            "vlan_id": 2045,
            "pref_level_code": 24,
            "age": "9s",
            "state": "REACHABLE",
            "filter": "no",
            "in_crimson": "yes",
            "client_id": "b811.4b0e.2630",
            "time_left": "233 s(691141 s)",
            "policy": "(unspecified)",
            "session_id": "LISP-DT-GUARD-VLAN (Device-tracking)"
        },
        2: {
            "dev_code": "ND",
            "network_layer_address": "FE80::A2BB:E8BC:FC85:EF11",
            "link_layer_address": "b811.4b0e.2630(R)",
            "interface": "Te1/0/14",
            "mode": "trunk",
            "vlan_id": 2045,
            "pref_level_code": 5,
            "age": "3s",
            "state": "REACHABLE",
            "filter": "no",
            "in_crimson": "yes",
            "client_id": "0000.0000.0000",
            "time_left": "240 s",
            "policy": "(unspecified)",
            "session_id": "LISP-DT-GUARD-VLAN (Device-tracking)"
        }
    }
}