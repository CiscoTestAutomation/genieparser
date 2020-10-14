expected_output = {
    "eigrp_instance": {
        "1100": {
            "vrf": {
                "VRF1": {
                    "address_family": {
                        "ipv4": {
                            "name": "",
                            "named_mode": False,
                            "eigrp_interface": {
                                "GigabitEthernet3": {
                                    "eigrp_nbr": {
                                        "10.1.2.2": {
                                            "peer_handle": 0,
                                            "hold": 13,
                                            "uptime": "00:01:01",
                                            "srtt": 0.002,
                                            "rto": 100,
                                            "q_cnt": 0,
                                            "last_seq_number": 2,
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
