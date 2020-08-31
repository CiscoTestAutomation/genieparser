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
                                "GigabitEthernet0/2.390": {
                                    "eigrp_nbr": {
                                        "10.12.90.2": {
                                            "peer_handle": 1,
                                            "hold": 11,
                                            "uptime": "01:38:09",
                                            "srtt": 0.021,
                                            "rto": 126,
                                            "q_cnt": 0,
                                            "last_seq_number": 8,
                                        }
                                    }
                                },
                                "GigabitEthernet0/3.390": {
                                    "eigrp_nbr": {
                                        "10.13.90.3": {
                                            "peer_handle": 0,
                                            "hold": 12,
                                            "uptime": "01:41:03",
                                            "srtt": 0.99,
                                            "rto": 5000,
                                            "q_cnt": 0,
                                            "last_seq_number": 11,
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
