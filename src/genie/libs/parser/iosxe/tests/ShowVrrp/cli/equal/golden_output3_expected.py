expected_output = {
    "interface": {
        "Vlan33": {
            "group": {
                10: {
                    "description": 'WORKING-VRRP',
                    "state": "MASTER",
                    "state_duration": {"minutes": 8, "seconds": 40.214},
                    "virtual_ip_address": "17.0.0.154",
                    "virtual_mac_address": "0000.5E00.010A",
                    "advertise_interval_secs": 1.0,
                    "preemption": "enabled",
                    "priority": 150,
                    "track_object": {
                        1: {
                            "decrement": 70,
                            "state": "UP"
                        }
                    },
                    "master_router_ip": "17.0.0.1",
                    "master_router": "local",
                    "master_router_priority": 150,
                    "master_advertisement_interval_secs": 1.0,
                    "master_advertisement_expiration_secs": 0.046,
                    "master_down_interval_secs": "unknown",
                    "flags": "1/1",
                    "address_family": {
                        "ipv6": {
                            "description": 'WORKING-VRRP',
                            "state": "MASTER",
                            "state_duration": {"minutes": 8, "seconds": 40.213},
                            "virtual_ip_address": "FE80::1",
                            "virtual_secondary_addresses": ["17::154/64"],
                            "virtual_mac_address": "0000.5E00.020A",
                            "advertise_interval_secs": 1.0,
                            "preemption": "enabled",
                            "priority": 150,
                            "track_object": {
                                1: {
                                    "decrement": 70,
                                    "state": "UP"
                                }
                            },
                            "master_router_ip": "FE80::2A3:D1FF:FE45:BEC5",
                            "master_router": "local",
                            "master_router_priority": 150,
                            "master_advertisement_interval_secs": 1.0,
                            "master_advertisement_expiration_secs": 0.441,
                            "master_down_interval_secs": "unknown",
                            "flags": "1/1",
                        }
                    },
                }
            }
        }
    }
}