expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "10.169.196.241/32": {
                            "nexthop": {
                                "10.19.198.25": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/1/6": {
                                            "local_label": 17063,
                                            "outgoing_label": ["16063"],
                                            "outgoing_label_info": "elc",
                                        }
                                    }
                                },
                                "10.19.198.26": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/1/7": {
                                            "local_label": 17063,
                                            "outgoing_label": ["16063"],
                                            "outgoing_label_backup": "16063",
                                            "repair": "attached-nexthop 10.19.198.29 GigabitEthernet0/1/8",
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
}
