expected_output = {
    "eigrp_instance": {
        "100": {
            "vrf": {
                "default": {
                    "address_family": {
                        "ipv6": {
                            "name": "test",
                            "named_mode": True,
                            "eigrp_interface": {
                                "GigabitEthernet3.90": {
                                    "eigrp_nbr": {
                                        "FE80::5C00:FF:FE02:7": {
                                            "peer_handle": 1,
                                            "hold": 11,
                                            "uptime": "01:29:00",
                                            "srtt": 0.01,
                                            "rto": 100,
                                            "q_cnt": 0,
                                            "last_seq_number": 29,
                                        }
                                    }
                                },
                                "GigabitEthernet2.90": {
                                    "eigrp_nbr": {
                                        "FE80::F816:3EFF:FE3D:AC68": {
                                            "peer_handle": 0,
                                            "hold": 14,
                                            "uptime": "02:23:03",
                                            "srtt": 0.01,
                                            "rto": 100,
                                            "q_cnt": 0,
                                            "last_seq_number": 29,
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
