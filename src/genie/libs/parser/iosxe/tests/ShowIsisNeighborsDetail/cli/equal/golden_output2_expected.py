expected_output = {
    "isis": {
        "1": {
            "neighbors": {
                "R3": {
                    "type": {
                        "L1": {
                            "interfaces": {
                                "Ethernet0/2": {
                                    "ip_address": "13.1.1.2",
                                    "state": "UP",
                                    "holdtime": "23",
                                    "circuit_id": "Circuit3.01",
                                    "area_addresses": [
                                        "47"
                                    ],
                                    "snpa": "aabb.cc01.f404",
                                    "state_changed": "00:02:07",
                                    "format": "Phase V",
                                    "remote_tids": [
                                        "0, 2"
                                    ],
                                    "parallel_suppressed": False,
                                    "local_tids": [
                                        "0"
                                    ],
                                    "interface_name": "Ethernet4/0",
                                    "nbr_ckt_id": "17",
                                    "adj_sid": {
                                        "16": {
                                            "level": 1,
                                            "f_flag": False,
                                            "b_flag": False,
                                            "v_flag": True,
                                            "l_flag": True,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0
                                        }
                                    },
                                    "adj_sync": {
                                        "Full": {}
                                    }
                                }
                            }
                        }
                    }
                },
                "7600": {
                    "type": {
                        "L1": {
                            "interfaces": {
                                "Ethernet0/1": {
                                    "state": "UP",
                                    "holdtime": "24",
                                    "circuit_id": "rudy.105",
                                    "area_addresses": [
                                        "50.1234",
                                        "49.1234"
                                    ],
                                    "snpa": "aabb.cc00.9d20",
                                    "state_changed": "00:02:07",
                                    "format": "Phase IV",
                                    "remote_tids": [
                                        "0"
                                    ],
                                    "parallel_suppressed": True,
                                    "local_tids": [
                                        "0"
                                    ],
                                    "interface_name": "Ethernet4/0",
                                    "nbr_ckt_id": "17",
                                    "nbr_tlv_rcvd": False,
                                    "mtid_nlpid": [
                                        {
                                            "mtid": "0",
                                            "nlpid": "IPV4"
                                        },
                                        {
                                            "mtid": "0",
                                            "nlpid": "IPV4"
                                        }
                                    ],
                                    "bfd_mtid_afi": [
                                        {
                                            "bfd_mtid": "2",
                                            "bfd_afi": "ipv6"
                                        },
                                        {
                                            "bfd_mtid": "2",
                                            "bfd_afi": "ipv6"
                                        }
                                    ]
                                }
                            }
                        }
                    }
                },
                "ott-lisp-c9k-127": {
                    "type": {
                        "L1L2": {
                            "interfaces": {
                                "TwentyFiveGigE1/0/2": {
                                    "ip_address": "20.20.22.2",
                                    "state": "DOWN",
                                    "holdtime": "24",
                                    "circuit_id": "0B",
                                    "area_addresses": [
                                        "50.1234"
                                    ],
                                    "snpa": "aabb.cc00.9d20",
                                    "ipv4_addresses": [
                                        "1.1.1.1",
                                        "2.2.2.2"
                                    ],
                                    "ipv6_addresses": [
                                        "FE80::A8BB:CCFF:FE00:9D20",
                                        "FE80::A8BB:CCFF:FE00:9D21"
                                    ],
                                    "ipv6_global_address": "13:13::2",
                                    "state_changed": "00:00:38",
                                    "lan_priority": 64,
                                    "format": "Phase V",
                                    "remote_tids": [
                                        "0, 2"
                                    ],
                                    "parallel_suppressed": False,
                                    "local_tids": [
                                        "0, 2"
                                    ],
                                    "interface_name": "Ethernet0/2",
                                    "nbr_ckt_id": "3",
                                    "remote_psnp_intvl": 50,
                                    "adj_down_reason": "Waiting For BFD Session",
                                    "nbr_tlv_rcvd": True,
                                    "mtid_nlpid": [
                                        {
                                            "mtid": "2",
                                            "nlpid": "IPV6"
                                        },
                                        {
                                            "mtid": "2",
                                            "nlpid": "IPV6"
                                        }
                                    ],
                                    "bfd_mtid_afi": [
                                        {
                                            "bfd_mtid": "2",
                                            "bfd_afi": "ipv6"
                                        },
                                        {
                                            "bfd_mtid": "2",
                                            "bfd_afi": "ipv6"
                                        }
                                    ],
                                    "auth_type": "MD5",
                                    "adj_sid": {
                                        "16": {
                                            "level": 1,
                                            "f_flag": False,
                                            "b_flag": False,
                                            "v_flag": True,
                                            "l_flag": True,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0
                                        }
                                    },
                                    "srv6_endx_sid": {
                                        "FCCC:CCC1:A1:E001::/64": {
                                            "b_flag": False,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0
                                        },
                                        "FCCC:CCC1:F1:E002::/64": {
                                            "b_flag": True,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0
                                        }
                                    },
                                    "adj_sync": {
                                        "Syncing": {
                                            "csnp_rcvd": "no",
                                            "init_flood": "yes",
                                            "requests": "0"
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "2222": {
                    "type": {
                        "L2": {
                            "interfaces": {
                                "FastEthernet0/0": {
                                    "ip_address": "10.1.1.2",
                                    "state": "UP",
                                    "holdtime": "7",
                                    "circuit_id": "01",
                                    "area_addresses": [
                                        "49.0001"
                                    ],
                                    "snpa": "cc02.1538.0000",
                                    "state_changed": "01:05:28",
                                    "lan_priority": 64,
                                    "format": "Phase V",
                                    "interface_name": "FastEthernet0/0",
                                    "auth_type": "Generic Cryptographic",
                                    "key_id": 100
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
