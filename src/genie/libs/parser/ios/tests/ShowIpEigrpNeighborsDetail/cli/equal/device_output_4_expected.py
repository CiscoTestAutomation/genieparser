expected_output = {
    "eigrp_instance": {
        "1": {
            "vrf": {
                "VRF1": {
                    "address_family": {
                        "ipv4": {
                            "name": "foo",
                            "named_mode": True,
                            "eigrp_interface": {
                                "GigabitEthernet3": {
                                    "eigrp_nbr": {
                                        "10.1.2.2": {
                                            "peer_handle": 0,
                                            "hold": 11,
                                            "uptime": "00:01:03",
                                            "srtt": 2.0,
                                            "rto": 100,
                                            "q_cnt": 0,
                                            "last_seq_number": 2,
                                            "nbr_sw_ver": {
                                                "os_majorver": 23,
                                                "os_minorver": 0,
                                                "tlv_majorrev": 2,
                                                "tlv_minorrev": 0,
                                            },
                                            "retransmit_count": 0,
                                            "retry_count": 0,
                                            "prefixes": 0,
                                            "topology_ids_from_peer": 0,
                                            "topology_advert_to_peer": "base",
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
