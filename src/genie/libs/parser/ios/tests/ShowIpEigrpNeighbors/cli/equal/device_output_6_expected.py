expected_output = {
    "eigrp_instance": {
        "": {
            "vrf": {
                "default": {
                    "address_family": {
                        "ipv4": {
                            "name": "",
                            "named_mode": False,
                            "eigrp_interface": {
                                "Ethernet0/0": {
                                    "eigrp_nbr": {
                                        "10.1.1.2": {
                                            "peer_handle": 0,
                                            "hold": 13,
                                            "uptime": "00:00:03",
                                            "srtt": 1.996,
                                            "rto": 5000,
                                            "q_cnt": 0,
                                            "last_seq_number": 5,
                                        },
                                        "10.1.1.9": {
                                            "peer_handle": 2,
                                            "hold": 14,
                                            "uptime": "00:02:24",
                                            "srtt": 0.206,
                                            "rto": 5000,
                                            "q_cnt": 0,
                                            "last_seq_number": 5,
                                        },
                                    }
                                },
                                "Ethernet0/1": {
                                    "eigrp_nbr": {
                                        "10.1.2.3": {
                                            "peer_handle": 1,
                                            "hold": 11,
                                            "uptime": "00:20:39",
                                            "srtt": 2.202,
                                            "rto": 5000,
                                            "q_cnt": 0,
                                            "last_seq_number": 5,
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
