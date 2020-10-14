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
                                            "hold": 11,
                                            "last_seq_number": 2,
                                            "nbr_sw_ver": {
                                                "os_majorver": 23,
                                                "os_minorver": 0,
                                                "tlv_majorrev": 2,
                                                "tlv_minorrev": 0,
                                            },
                                            "peer_handle": 0,
                                            "prefixes": 0,
                                            "q_cnt": 0,
                                            "retransmit_count": 0,
                                            "retry_count": 0,
                                            "rto": 100,
                                            "srtt": 2.0,
                                            "topology_ids_from_peer": 0,
                                            "topology_advert_to_peer": "base",
                                            "uptime": "00:01:03",
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
