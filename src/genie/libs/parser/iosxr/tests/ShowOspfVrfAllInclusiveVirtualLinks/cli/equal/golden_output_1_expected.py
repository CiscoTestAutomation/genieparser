

expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "1": {
                            "areas": {
                                "0.0.0.1": {
                                    "virtual_links": {
                                        "0.0.0.1 10.16.2.2": {
                                            "authentication": {
                                                "auth_trailer_key": {
                                                    "crypto_algorithm": "simple"
                                                }
                                            },
                                            "cost": 65535,
                                            "dcbitless_lsa_count": 1,
                                            "donotage_lsa": "not allowed",
                                            "dead_interval": 16,
                                            "demand_circuit": True,
                                            "hello_interval": 4,
                                            "hello_timer": "00:00:03:179",
                                            "interface": "GigabitEthernet0/0/0/3",
                                            "name": "VL0",
                                            "link_state": "up",
                                            "nsf": {
                                                "enable": True,
                                                "last_restart": "00:18:16",
                                            },
                                            "retransmit_interval": 44,
                                            "router_id": "10.16.2.2",
                                            "state": "point-to-point,",
                                            "transit_area_id": "0.0.0.1",
                                            "transmit_delay": 5,
                                            "wait_interval": 16,
                                        },
                                        "0.0.0.1 10.100.5.5": {
                                            "authentication": {
                                                "auth_trailer_key": {
                                                    "crypto_algorithm": "md5",
                                                    "youngest_key_id": 1,
                                                }
                                            },
                                            "cost": 65535,
                                            "dcbitless_lsa_count": 1,
                                            "donotage_lsa": "not allowed",
                                            "dead_interval": 16,
                                            "demand_circuit": True,
                                            "hello_interval": 4,
                                            "hello_timer": "00:00:03:179",
                                            "interface": "GigabitEthernet0/0/0/4",
                                            "name": "VL1",
                                            "link_state": "up",
                                            "nsf": {
                                                "enable": True,
                                                "last_restart": "00:18:16",
                                            },
                                            "retransmit_interval": 44,
                                            "router_id": "10.100.5.5",
                                            "state": "point-to-point,",
                                            "transit_area_id": "0.0.0.1",
                                            "transmit_delay": 5,
                                            "wait_interval": 16,
                                        },
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
