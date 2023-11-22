expected_output = {
    "number_of_aggregators": 1,
    "interfaces": {
        "Port-channel10": {
            "name": "Port-channel10",
            "protocol": "pagp",
            "members": {
                "GigabitEthernet1/0/16": {
                    "interface": "GigabitEthernet1/0/16",
                    "flags": "P",
                    "bundled": True,
                    "port_channel": {
                        "port_channel_int": "Port-channel10",
                        "port_channel_member": True,
                    },
                },
                "GigabitEthernet1/0/15": {
                    "interface": "GigabitEthernet1/0/15",
                    "flags": "P",
                    "bundled": True,
                    "port_channel": {
                        "port_channel_int": "Port-channel10",
                        "port_channel_member": True,
                    },
                },
                "GigabitEthernet1/0/17": {
                    "interface": "GigabitEthernet1/0/17",
                    "flags": "P",
                    "bundled": True,
                    "port_channel": {
                        "port_channel_int": "Port-channel10",
                        "port_channel_member": True,
                    },
                },
            },
            "oper_status": "up",
            "bundle_id": 10,
            "port_channel": {
                "port_channel_member_intfs": [
                    "GigabitEthernet1/0/15",
                    "GigabitEthernet1/0/16",
                    "GigabitEthernet1/0/17",
                ],
                "port_channel_member": True,
            },
            "flags": "SU",
        }
    },
    "number_of_lag_in_use": 1,
}
