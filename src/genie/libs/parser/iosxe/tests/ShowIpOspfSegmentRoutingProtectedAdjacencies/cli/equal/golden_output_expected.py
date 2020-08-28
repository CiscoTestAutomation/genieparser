expected_output = {
    "process_id": {
        65109: {
            "router_id": "10.4.1.1",
            "areas": {
                "0.0.0.8": {
                    "neighbors": {
                        "10.151.22.22": {
                            "interfaces": {
                                "GigabitEthernet5": {
                                    "address": "10.0.0.25",
                                    "adj_sid": 20,
                                    "backup_nexthop": "10.0.0.9",
                                    "backup_interface": "GigabitEthernet3",
                                },
                                "GigabitEthernet4": {
                                    "address": "10.0.0.13",
                                    "adj_sid": 21,
                                    "backup_nexthop": "10.0.0.9",
                                    "backup_interface": "GigabitEthernet3",
                                },
                            }
                        },
                        "10.229.11.11": {
                            "interfaces": {
                                "GigabitEthernet3": {
                                    "address": "10.0.0.9",
                                    "adj_sid": 22,
                                    "backup_nexthop": "10.0.0.13",
                                    "backup_interface": "GigabitEthernet4",
                                }
                            }
                        },
                    }
                }
            },
        }
    }
}
