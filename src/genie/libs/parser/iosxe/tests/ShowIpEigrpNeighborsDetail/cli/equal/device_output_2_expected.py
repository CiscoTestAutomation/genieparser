expected_output = {
    "eigrp_instance": {
        "1": {
            "vrf": {
                "default": {
                    "address_family": {
                        "ipv4": {
                            "name": "foo",
                            "named_mode": True,
                            "eigrp_interface": {
                                "GigabitEthernet2/0": {
                                    "eigrp_nbr": {
                                        "192.168.10.1": {
                                            "peer_handle": 0,
                                            "hold": 12,
                                            "uptime": "00:00:21",
                                            "srtt": 1600.0,
                                            "rto": 5000,
                                            "q_cnt": 0,
                                            "last_seq_number": 3,
                                            "nbr_sw_ver": {
                                                "os_majorver": 8,
                                                "os_minorver": 0,
                                                "tlv_majorrev": 2,
                                                "tlv_minorrev": 0,
                                            },
                                            "retransmit_count": 0,
                                            "retry_count": 0,
                                            "prefixes": 1,
                                            "topology_ids_from_peer": 0,
                                            "topology_advert_to_peer": "",
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
