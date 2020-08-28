expected_output = {
    "eigrp_instance": {
        "100": {
            "vrf": {
                "default": {
                    "address_family": {
                        "ipv4": {
                            "name": "test",
                            "named_mode": True,
                            "eigrp_interface": {
                                "GigabitEthernet2.90": {
                                    "eigrp_nbr": {
                                        "10.12.90.2": {
                                            "peer_handle": 1,
                                            "hold": 13,
                                            "uptime": "2d10h",
                                            "srtt": 1.283,
                                            "rto": 5000,
                                            "q_cnt": 0,
                                            "last_seq_number": 5,
                                        }
                                    }
                                },
                                "GigabitEthernet3.90": {
                                    "eigrp_nbr": {
                                        "10.13.90.3": {
                                            "peer_handle": 0,
                                            "hold": 11,
                                            "uptime": "2d10h",
                                            "srtt": 0.006,
                                            "rto": 100,
                                            "q_cnt": 0,
                                            "last_seq_number": 9,
                                        }
                                    }
                                },
                            },
                        }
                    }
                }
            }
        }
    }
}
