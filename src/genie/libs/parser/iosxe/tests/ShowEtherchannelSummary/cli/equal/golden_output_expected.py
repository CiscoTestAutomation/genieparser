expected_output = {
    "number_of_lag_in_use": 2,
    "number_of_aggregators": 2,
    "interfaces": {
        "Port-channel1": {
            "name": "Port-channel1",
            "bundle_id": 1,
            "protocol": "lacp",
            "flags": "RU",
            "oper_status": "up",
            "members": {
                "GigabitEthernet2": {
                    "interface": "GigabitEthernet2",
                    "flags": "bndl",
                    "bundled": True,
                    "port_channel": {
                        "port_channel_member": True,
                        "port_channel_int": "Port-channel1",
                    },
                },
                "GigabitEthernet3": {
                    "interface": "GigabitEthernet3",
                    "flags": "bndl",
                    "bundled": True,
                    "port_channel": {
                        "port_channel_member": True,
                        "port_channel_int": "Port-channel1",
                    },
                },
            },
            "port_channel": {
                "port_channel_member": True,
                "port_channel_member_intfs": ["GigabitEthernet2", "GigabitEthernet3"],
            },
        },
        "Port-channel2": {
            "name": "Port-channel2",
            "bundle_id": 2,
            "protocol": "lacp",
            "flags": "RU",
            "oper_status": "up",
            "members": {
                "GigabitEthernet4": {
                    "interface": "GigabitEthernet4",
                    "flags": "bndl",
                    "bundled": True,
                    "port_channel": {
                        "port_channel_member": True,
                        "port_channel_int": "Port-channel2",
                    },
                },
                "GigabitEthernet5": {
                    "interface": "GigabitEthernet5",
                    "flags": "hot-sby",
                    "bundled": False,
                    "port_channel": {
                        "port_channel_member": True,
                        "port_channel_int": "Port-channel2",
                    },
                },
                "GigabitEthernet6": {
                    "interface": "GigabitEthernet6",
                    "flags": "bndl",
                    "bundled": True,
                    "port_channel": {
                        "port_channel_member": True,
                        "port_channel_int": "Port-channel2",
                    },
                },
            },
            "port_channel": {
                "port_channel_member": True,
                "port_channel_member_intfs": [
                    "GigabitEthernet4",
                    "GigabitEthernet5",
                    "GigabitEthernet6",
                ],
            },
        },
    },
}
