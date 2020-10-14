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
                                "GigabitEthernet0/2.90": {
                                    "eigrp_nbr": {
                                        "FE80::F816:3EFF:FE39:94CB": {
                                            "peer_handle": 1,
                                            "hold": 14,
                                            "uptime": "01:37:31",
                                            "srtt": 0.739,
                                            "rto": 4434,
                                            "q_cnt": 0,
                                            "last_seq_number": 7,
                                        }
                                    }
                                },
                                "GigabitEthernet0/3.90": {
                                    "eigrp_nbr": {
                                        "FE80::5C00:80FF:FE01:7": {
                                            "peer_handle": 0,
                                            "hold": 12,
                                            "uptime": "01:40:24",
                                            "srtt": 0.993,
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
