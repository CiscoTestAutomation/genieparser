expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "10.151.22.22/32": {
                            "epoch": 2,
                            "sr_local_label_info": "global/16022 [0x1B]",
                            "nexthop": {
                                "10.0.0.9": {
                                    "outgoing_interface": {
                                        "GigabitEthernet3": {
                                            "local_label": 16022,
                                            "outgoing_label": ["16022"],
                                            "outgoing_label_backup": "implicit-null",
                                            "repair": "attached-nexthop 10.0.0.13 GigabitEthernet4",
                                        }
                                    }
                                }
                            },
                        }
                    }
                }
            }
        }
    }
}
