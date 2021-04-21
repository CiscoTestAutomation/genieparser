expected_output = {
    "mac_table": {
        "vlans": {
            "2": {
                "mac_addresses": {
                    "701f.53ff.4de2": {
                        "interfaces": {
                            "Port-channel1": {
                                "entry_type": "dynamic",
                                "interface": "Port-channel1",
                                "protocols": ["ip"],
                            }
                        },
                        "mac_address": "701f.53ff.4de2",
                    },
                    "cc98.91ff.cbc2": {
                        "interfaces": {
                            "Port-channel1": {
                                "entry_type": "dynamic",
                                "interface": "Port-channel1",
                                "protocols": ["ip", "ipx"],
                            }
                        },
                        "mac_address": "cc98.91ff.cbc2",
                    },
                },
                "vlan": 2,
            }
        }
    }
}
