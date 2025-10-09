expected_output = {
    "eigrp_instance": {
        "100": {
            "vrf": {
                "default": {
                    "address_family": {
                        "ipv4": {
                            "name": "",
                            "named_mode": False,
                            "eigrp_interface": {
                                "TenGigabitEthernet0/0/4": {
                                    "eigrp_nbr": {
                                        "61.1.1.1": {
                                            "peer_handle": 0,
                                            "hold": 13,
                                            "uptime": "00:00:40",
                                            "srtt": 1.966,
                                            "rto": 100,
                                            "q_cnt": 0,
                                            "last_seq_number": 1882480,
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
