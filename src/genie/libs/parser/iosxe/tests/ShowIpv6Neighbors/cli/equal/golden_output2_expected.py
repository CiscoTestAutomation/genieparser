expected_output = {
    "interface": {
        "GigabitEthernet3": {
            "interface": "GigabitEthernet3",
            "neighbors": {
                "2001:db8:888c:1::2": {
                    "age": "0",
                    "ip": "2001:db8:888c:1::2",
                    "link_layer_address": "fa16.3eff.1b7b",
                    "neighbor_state": "REACH",
                },
                "2001:db8:c8d1:1::11": {
                    "age": "-",
                    "ip": "2001:db8:c8d1:1::11",
                    "link_layer_address": "bbbb.beff.bcbc",
                    "neighbor_state": "REACH",
                },
                "FE80::F816:3EFF:FEFF:1B7B": {
                    "age": "0",
                    "ip": "FE80::F816:3EFF:FEFF:1B7B",
                    "link_layer_address": "fa16.3eff.1b7b",
                    "neighbor_state": "REACH",
                },
            },
        },
        "GigabitEthernet5": {
            "interface": "GigabitEthernet5",
            "neighbors": {
                "2001:db8:c8d1:1::3": {
                    "age": "0",
                    "ip": "2001:db8:c8d1:1::3",
                    "link_layer_address": "5e01.c0ff.0209",
                    "neighbor_state": "REACH",
                },
                "FE80::5C01:C0FF:FEFF:209": {
                    "age": "1",
                    "ip": "FE80::5C01:C0FF:FEFF:209",
                    "link_layer_address": "5e01.c0ff.0209",
                    "neighbor_state": "STALE",
                },
            },
        },
    }
}
