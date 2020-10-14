expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "10.16.2.2/32": {
                            "epoch": 2,
                            "nexthop": {
                                "10.0.0.13": {
                                    "outgoing_interface": {
                                        "GigabitEthernet4": {
                                            "local_label": 16002,
                                            "outgoing_label": ["16002"],
                                            "outgoing_label_backup": "16002",
                                            "repair": "attached-nexthop 10.0.0.5 GigabitEthernet2",
                                        }
                                    }
                                },
                                "10.0.0.25": {
                                    "outgoing_interface": {
                                        "GigabitEthernet5": {
                                            "local_label": 16002,
                                            "outgoing_label": ["16002"],
                                            "outgoing_label_backup": "16002",
                                            "repair": "attached-nexthop 10.0.0.13 GigabitEthernet4",
                                        }
                                    }
                                },
                                "10.0.0.5": {
                                    "outgoing_interface": {
                                        "GigabitEthernet2": {
                                            "local_label": 16002,
                                            "outgoing_label": ["16002"],
                                            "outgoing_label_backup": "16002",
                                            "repair": "attached-nexthop 10.0.0.9 GigabitEthernet3",
                                        }
                                    }
                                },
                                "10.0.0.9": {
                                    "outgoing_interface": {
                                        "GigabitEthernet3": {
                                            "local_label": 16002,
                                            "outgoing_label": ["16002"],
                                            "outgoing_label_backup": "16002",
                                            "repair": "attached-nexthop 10.0.0.25 GigabitEthernet5",
                                        }
                                    }
                                },
                            },
                            "per_destination_sharing": True,
                            "sr_local_label_info": "global/16002 [0x1B]",
                        }
                    }
                }
            }
        }
    }
}
