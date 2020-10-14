expected_output = {
    "eigrp_instance": {
        "100": {
            "vrf": {
                "VRF1": {
                    "address_family": {
                        "ipv4": {
                            "name": "test",
                            "named_mode": True,
                            "eigrp_interface": {
                                "GigabitEthernet2.390": {
                                    "eigrp_nbr": {
                                        "10.12.90.2": {
                                            "peer_handle": 1,
                                            "hold": 13,
                                            "uptime": "2d10h",
                                            "srtt": 0.024,
                                            "rto": 144,
                                            "q_cnt": 0,
                                            "last_seq_number": 8,
                                        }
                                    }
                                },
                                "GigabitEthernet3.390": {
                                    "eigrp_nbr": {
                                        "10.13.90.3": {
                                            "peer_handle": 0,
                                            "hold": 10,
                                            "uptime": "2d10h",
                                            "srtt": 0.005,
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
