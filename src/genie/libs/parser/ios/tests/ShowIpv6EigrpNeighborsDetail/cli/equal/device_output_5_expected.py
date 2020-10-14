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
                                            "hold": 11,
                                            "uptime": "01:42:01",
                                            "srtt": 0.739,
                                            "rto": 4434,
                                            "q_cnt": 0,
                                            "last_seq_number": 7,
                                            "topology_advert_to_peer": "base",
                                            "nbr_sw_ver": {
                                                "os_majorver": 3,
                                                "os_minorver": 3,
                                                "tlv_majorrev": 2,
                                                "tlv_minorrev": 0,
                                            },
                                            "retransmit_count": 0,
                                            "retry_count": 0,
                                            "prefixes": 4,
                                            "topology_ids_from_peer": 0,
                                        }
                                    }
                                },
                                "GigabitEthernet0/3.90": {
                                    "eigrp_nbr": {
                                        "FE80::5C00:80FF:FE01:7": {
                                            "peer_handle": 0,
                                            "hold": 11,
                                            "uptime": "01:44:53",
                                            "srtt": 0.993,
                                            "rto": 5000,
                                            "q_cnt": 0,
                                            "last_seq_number": 11,
                                            "topology_advert_to_peer": "base",
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
