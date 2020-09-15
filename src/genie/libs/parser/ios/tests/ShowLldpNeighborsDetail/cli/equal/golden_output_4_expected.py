expected_output = {
    "interfaces": {
        "GigabitEthernet1/0/17": {
            "if_name": "GigabitEthernet1/0/17",
            "port_id": {
                "C81f.77ff.dddd": {
                    "neighbors": {
                        "TestName": {
                            "neighbor_id": "TestName",
                            "chassis_id": "127.0.0.2",
                            "port_id": "C81f.77ff.dddd",
                            "system_name": "TestName",
                            "time_remaining": 104,
                            "capabilities": {
                                "mac_bridge": {
                                    "name": "mac_bridge",
                                    "system": True,
                                    "enabled": True,
                                },
                                "telephone": {
                                    "name": "telephone",
                                    "system": True,
                                    "enabled": True,
                                },
                            },
                            "management_address": "127.0.0.2",
                            "auto_negotiation": "not supported",
                            "unit_type": 30,
                        }
                    }
                }
            },
        }
    },
    "med_information": {
        "h/w_revision": "9611GD02C",
        "s/w_revision": "6.6604",
        "serial_number": "12389WET87",
        "manufacturer": "Avaya",
        "model": "9611",
        "capabilities": ["NP", "PD", "IN"],
        "device_type": "Endpoint Class III",
        "network_policy": {
            "voice": {"tagged": True, "layer_2_priority": 5, "dscp": 46, "vlan": 66}
        },
        "location": "not advertised",
    },
    "total_entries": 1,
}
