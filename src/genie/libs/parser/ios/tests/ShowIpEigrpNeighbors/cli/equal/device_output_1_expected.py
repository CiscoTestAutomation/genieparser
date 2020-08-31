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
                                "GigabitEthernet0/2.90": {
                                    "eigrp_nbr": {
                                        "10.12.90.2": {
                                            "peer_handle": 1,
                                            "hold": 12,
                                            "uptime": "01:34:23",
                                            "srtt": 0.029,
                                            "rto": 174,
                                            "q_cnt": 0,
                                            "last_seq_number": 5,
                                        }
                                    }
                                },
                                "GigabitEthernet0/3.90": {
                                    "eigrp_nbr": {
                                        "10.13.90.3": {
                                            "peer_handle": 0,
                                            "hold": 10,
                                            "uptime": "01:37:17",
                                            "srtt": 0.013,
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
