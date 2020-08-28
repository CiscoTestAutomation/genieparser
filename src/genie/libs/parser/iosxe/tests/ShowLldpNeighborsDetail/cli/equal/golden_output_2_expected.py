expected_output = {
    "interfaces": {
        "GigabitEthernet0/1/7": {
            "if_name": "GigabitEthernet0/1/7",
            "port_id": {
                "C8F9F9D61BC2:P1": {
                    "neighbors": {
                        "SEPC8F9F9D61BC2": {
                            "auto_negotiation": "supported, enabled",
                            "capabilities": {
                                "mac_bridge": {
                                    "enabled": True,
                                    "name": "mac_bridge",
                                    "system": True,
                                },
                                "telephone": {
                                    "enabled": True,
                                    "name": "telephone",
                                    "system": True,
                                },
                            },
                            "chassis_id": "10.10.0.1",
                            "management_address": "10.10.0.1",
                            "neighbor_id": "SEPC8F9F9D61BC2",
                            "physical_media_capabilities": [
                                "1000baseT(HD)",
                                "1000baseX(FD)",
                                "Symm, Asym Pause(FD)",
                                "Symm Pause(FD)",
                            ],
                            "port_description": "SW PORT",
                            "port_id": "C8F9F9D61BC2:P1",
                            "system_description": "Cisco IP Phone 7962G,V12, SCCP42.9-3-1ES27S\n",
                            "system_name": "SEPC8F9F9D61BC2",
                            "time_remaining": 127,
                            "unit_type": 16,
                        }
                    }
                }
            },
        }
    },
    "med_information": {
        "capabilities": ["NP", "PD", "IN"],
        "device_type": "PD device",
        "f/w_revision": "tnp62.8-3-1-21a.bin",
        "s/w_revision": "SCCP42.9-3-1ES27S",
        "h/w_revision": "12",
        "location": "not advertised",
        "manufacturer": "Cisco Systems, Inc.",
        "model": "CP-7962G",
        "network_policy": {
            "voice": {"dscp": 46, "layer_2_priority": 5, "tagged": True, "vlan": 10},
            "voice_signal": {
                "dscp": 32,
                "layer_2_priority": 4,
                "tagged": True,
                "vlan": 10,
            },
        },
        "power_priority": "Unknown",
        "power_source": "Unknown",
        "serial_number": "FCH1610A5S5",
        "wattage": 6.3,
    },
    "total_entries": 1,
}
