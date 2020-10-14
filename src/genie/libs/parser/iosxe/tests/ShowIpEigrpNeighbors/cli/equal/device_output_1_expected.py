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
                                "GigabitEthernet0/0": {
                                    "eigrp_nbr": {
                                        "10.1.1.2": {
                                            "peer_handle": 0,
                                            "hold": 13,
                                            "uptime": "00:00:03",
                                            "srtt": 1.996,
                                            "rto": 5000,
                                            "q_cnt": 0,
                                            "last_seq_number": 5,
                                        }
                                    }
                                }
                            },
                        }
                    }
                }
            }
        }
    }
}
