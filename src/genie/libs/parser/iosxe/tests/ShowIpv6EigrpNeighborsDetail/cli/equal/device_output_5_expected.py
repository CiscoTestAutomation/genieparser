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
                                            "uptime": "01:30:32",
                                            "srtt": 0.01,
                                            "rto": 100,
                                            "q_cnt": 0,
                                            "last_seq_number": 29,
                                            "nbr_sw_ver": {
                                                "os_majorver": 8,
                                                "os_minorver": 0,
                                                "tlv_majorrev": 1,
                                                "tlv_minorrev": 2,
                                            },
                                            "retransmit_count": 0,
                                            "retry_count": 0,
                                            "prefixes": 4,
                                            "topology_ids_from_peer": 0,
                                            "topology_advert_to_peer": "base",
                                        }
                                    }
                                },
                                "GigabitEthernet2.90": {
                                    "eigrp_nbr": {
                                        "FE80::F816:3EFF:FE3D:AC68": {
                                            "peer_handle": 0,
                                            "hold": 14,
                                            "uptime": "02:24:36",
                                            "srtt": 0.01,
                                            "rto": 100,
                                            "q_cnt": 0,
                                            "last_seq_number": 29,
                                            "nbr_sw_ver": {
                                                "os_majorver": 3,
                                                "os_minorver": 3,
                                                "tlv_majorrev": 2,
                                                "tlv_minorrev": 0,
                                            },
                                            "retransmit_count": 1,
                                            "retry_count": 0,
                                            "prefixes": 4,
                                            "topology_ids_from_peer": 0,
                                            "topology_advert_to_peer": "base",
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
