expected_output = {
    "isis": {
        "1": {
            "neighbors": {
                "iolR3": {
                    "type": {
                        "L1": {
                            "interfaces": {
                                "Ethernet1/2": {
                                    "ip_address": "13.1.1.2",
                                    "state": "UP",
                                    "holdtime": "24",
                                    "circuit_id": "07",
                                    "area_addresses": ["50.1234"],
                                    "snpa": "aabb.cc03.ea21",
                                    "ipv6_addresses": ["FE80::A8BB:CCFF:FE03:EA21"],
                                    "ipv6_global_address": "13:13::2",
                                    "state_changed": "03:19:05",
                                    "format": "Phase V",
                                    "remote_tids": ["0, 2"],
                                    "parallel_suppressed": False,
                                    "local_tids": ["0, 2"],
                                    "interface_name": "Ethernet1/2",
                                    "nbr_ckt_id": "7",
                                    "remote_psnp_intvl": 50,
                                    "nbr_tlv_rcvd": True,
                                    "mtid_nlpid": [{"mtid": "2", "nlpid": "IPV6"}],
                                    "bfd_mtid_afi": [
                                        {"bfd_mtid": "2", "bfd_afi": "ipv6"}
                                    ],
                                    "adj_sid": {
                                        "20": {
                                            "level": 1,
                                            "f_flag": False,
                                            "b_flag": False,
                                            "v_flag": True,
                                            "l_flag": True,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0,
                                        },
                                        "17": {
                                            "level": 1,
                                            "f_flag": False,
                                            "b_flag": False,
                                            "v_flag": True,
                                            "l_flag": True,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0,
                                        },
                                        "18": {
                                            "level": 1,
                                            "f_flag": False,
                                            "b_flag": False,
                                            "v_flag": True,
                                            "l_flag": True,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0,
                                        },
                                    },
                                    "srv6_endx_sid": {
                                        "FCCC:CCC1:A1:E000::/64": {
                                            "b_flag": False,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0,
                                            "algo": 0,
                                        }
                                    },
                                    "adj_sync": {"Full": {}},
                                }
                            }
                        }
                    }
                },
                "iolR2": {
                    "type": {
                        "L1": {
                            "interfaces": {
                                "Ethernet0/1": {
                                    "ip_address": "12.1.1.2",
                                    "state": "UP",
                                    "holdtime": "29",
                                    "circuit_id": "02",
                                    "area_addresses": ["50.1234"],
                                    "snpa": "aabb.cc02.8410",
                                    "ipv6_addresses": ["FE80::A8BB:CCFF:FE02:8410"],
                                    "ipv6_global_address": "12:12::2",
                                    "state_changed": "03:19:05",
                                    "format": "Phase V",
                                    "remote_tids": ["0, 2"],
                                    "parallel_suppressed": False,
                                    "local_tids": ["0, 2"],
                                    "interface_name": "Ethernet0/1",
                                    "nbr_ckt_id": "2",
                                    "remote_psnp_intvl": 50,
                                    "nbr_tlv_rcvd": True,
                                    "mtid_nlpid": [{"mtid": "2", "nlpid": "IPV6"}],
                                    "bfd_mtid_afi": [
                                        {"bfd_mtid": "2", "bfd_afi": "ipv6"}
                                    ],
                                    "adj_sid": {
                                        "20": {
                                            "level": 1,
                                            "f_flag": False,
                                            "b_flag": False,
                                            "v_flag": True,
                                            "l_flag": True,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0,
                                        },
                                        "17": {
                                            "level": 1,
                                            "f_flag": False,
                                            "b_flag": False,
                                            "v_flag": True,
                                            "l_flag": True,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0,
                                        },
                                        "18": {
                                            "level": 1,
                                            "f_flag": False,
                                            "b_flag": False,
                                            "v_flag": True,
                                            "l_flag": True,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0,
                                        },
                                    },
                                    "srv6_endx_sid": {
                                        "FCCC:CCC1:A1:E002::/64": {
                                            "b_flag": False,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0,
                                            "algo": 0,
                                        }
                                    },
                                    "adj_sync": {"Full": {}},
                                }
                            }
                        }
                    }
                },
                "iolR8": {
                    "type": {
                        "L1": {
                            "interfaces": {
                                "Ethernet0/0": {
                                    "ip_address": "18.1.1.2",
                                    "state": "UP",
                                    "holdtime": "22",
                                    "circuit_id": "02",
                                    "area_addresses": ["50.1234"],
                                    "snpa": "aabb.cc03.8c10",
                                    "ipv6_addresses": ["FE80::A8BB:CCFF:FE03:8C10"],
                                    "ipv6_global_address": "18:18::2",
                                    "state_changed": "03:19:05",
                                    "format": "Phase V",
                                    "remote_tids": ["0, 2"],
                                    "parallel_suppressed": False,
                                    "local_tids": ["0, 2"],
                                    "interface_name": "Ethernet0/0",
                                    "nbr_ckt_id": "2",
                                    "remote_psnp_intvl": 50,
                                    "nbr_tlv_rcvd": True,
                                    "mtid_nlpid": [{"mtid": "2", "nlpid": "IPV6"}],
                                    "bfd_mtid_afi": [
                                        {"bfd_mtid": "2", "bfd_afi": "ipv6"}
                                    ],
                                    "adj_sid": {
                                        "20": {
                                            "level": 1,
                                            "f_flag": False,
                                            "b_flag": False,
                                            "v_flag": True,
                                            "l_flag": True,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0,
                                        },
                                        "17": {
                                            "level": 1,
                                            "f_flag": False,
                                            "b_flag": False,
                                            "v_flag": True,
                                            "l_flag": True,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0,
                                        },
                                        "18": {
                                            "level": 1,
                                            "f_flag": False,
                                            "b_flag": False,
                                            "v_flag": True,
                                            "l_flag": True,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0,
                                        },
                                    },
                                    "srv6_endx_sid": {
                                        "FCCC:CCC1:A1:E004::/64": {
                                            "b_flag": False,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0,
                                            "algo": 0,
                                        }
                                    },
                                    "adj_sync": {"Full": {}},
                                }
                            }
                        }
                    }
                },
            }
        }
    }
}
