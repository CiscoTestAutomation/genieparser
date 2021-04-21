expected_output = {
    "interface": {
        "GigabitEthernet2": {
            "interface": "GigabitEthernet2",
            "neighbors": {
                "2001:db8:8548:1::2": {
                    "age": "0",
                    "ip": "2001:db8:8548:1::2",
                    "link_layer_address": "fa16.3eff.09c8",
                    "neighbor_state": "REACH",
                },
                "2001:db8:8548:1::11": {
                    "age": "-",
                    "ip": "2001:db8:8548:1::11",
                    "link_layer_address": "aaaa.beff.bcbc",
                    "neighbor_state": "REACH",
                },
                "FE80::F816:3EFF:FEFF:9C8": {
                    "age": "1",
                    "ip": "FE80::F816:3EFF:FEFF:9C8",
                    "link_layer_address": "fa16.3eff.09c8",
                    "neighbor_state": "STALE",
                },
            },
        },
        "GigabitEthernet4": {
            "interface": "GigabitEthernet4",
            "neighbors": {
                "2001:db8:c56d:1::3": {
                    "age": "0",
                    "ip": "2001:db8:c56d:1::3",
                    "link_layer_address": "5e01.c0ff.0209",
                    "neighbor_state": "STALE",
                },
                "FE80::5C01:C0FF:FEFF:209": {
                    "age": "2",
                    "ip": "FE80::5C01:C0FF:FEFF:209",
                    "link_layer_address": "5e01.c0ff.0209",
                    "neighbor_state": "STALE",
                },
            },
        },
    }
}
