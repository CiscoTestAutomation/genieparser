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
                                "Ethernet1/0": {
                                    "eigrp_nbr": {
                                        "10.1.2.1": {
                                            "hold": 11,
                                            "last_seq_number": 6,
                                            "nbr_sw_ver": {
                                                "os_majorver": 5,
                                                "os_minorver": 1,
                                                "tlv_majorrev": 3,
                                                "tlv_minorrev": 0,
                                            },
                                            "peer_handle": 0,
                                            "prefixes": 1,
                                            "q_cnt": 0,
                                            "retransmit_count": 2,
                                            "retry_count": 0,
                                            "rto": 200,
                                            "srtt": 12.0,
                                            "topology_ids_from_peer": 0,
                                            "uptime": "00:02:31",
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
