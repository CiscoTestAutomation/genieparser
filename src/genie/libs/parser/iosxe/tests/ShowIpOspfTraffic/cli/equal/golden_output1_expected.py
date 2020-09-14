expected_output = {
    "ospf_statistics": {
        "last_clear_traffic_counters": "never",
        "rcvd": {
            "checksum_errors": 0,
            "database_desc": 938,
            "hello": 2024732,
            "link_state_acks": 75666,
            "link_state_req": 323,
            "link_state_updates": 11030,
            "total": 2112690,
        },
        "sent": {
            "database_desc": 1176,
            "hello": 2381794,
            "link_state_acks": 8893,
            "link_state_req": 43,
            "link_state_updates": 92224,
            "total": 2509472,
        },
    },
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "65109": {
                            "router_id": "10.169.197.252",
                            "ospf_queue_statistics": {
                                "limit": {"inputq": 0, "outputq": 0, "updateq": 200},
                                "drops": {"inputq": 0, "outputq": 0, "updateq": 0},
                                "max_delay_msec": {
                                    "inputq": 49,
                                    "outputq": 2,
                                    "updateq": 2,
                                },
                                "max_size": {
                                    "total": {
                                        "inputq": 14,
                                        "outputq": 6,
                                        "updateq": 14,
                                    },
                                    "invalid": {
                                        "inputq": 0,
                                        "outputq": 0,
                                        "updateq": 0,
                                    },
                                    "hello": {"inputq": 0, "outputq": 0, "updateq": 0},
                                    "db_des": {"inputq": 0, "outputq": 0, "updateq": 0},
                                    "ls_req": {"inputq": 0, "outputq": 0, "updateq": 0},
                                    "ls_upd": {"inputq": 0, "outputq": 0, "updateq": 0},
                                    "ls_ack": {
                                        "inputq": 14,
                                        "outputq": 6,
                                        "updateq": 14,
                                    },
                                },
                                "current_size": {
                                    "total": {"inputq": 0, "outputq": 0, "updateq": 0},
                                    "invalid": {
                                        "inputq": 0,
                                        "outputq": 0,
                                        "updateq": 0,
                                    },
                                    "hello": {"inputq": 0, "outputq": 0, "updateq": 0},
                                    "db_des": {"inputq": 0, "outputq": 0, "updateq": 0},
                                    "ls_req": {"inputq": 0, "outputq": 0, "updateq": 0},
                                    "ls_upd": {"inputq": 0, "outputq": 0, "updateq": 0},
                                    "ls_ack": {"inputq": 0, "outputq": 0, "updateq": 0},
                                },
                            },
                            "interface_statistics": {
                                "interfaces": {
                                    "GigabitEthernet0/0/0": {
                                        "last_clear_traffic_counters": "never",
                                        "ospf_header_errors": {
                                            "adjacency_throttle": 0,
                                            "area_mismatch": 0,
                                            "auth_type": 0,
                                            "authentication": 0,
                                            "bad_source": 0,
                                            "bfd": 0,
                                            "checksum": 0,
                                            "duplicate_id": 0,
                                            "hello": 0,
                                            "instance_id": 0,
                                            "length": 0,
                                            "lls": 0,
                                            "mtu_mismatch": 0,
                                            "nbr_ignored": 0,
                                            "no_sham_link": 0,
                                            "no_virtual_link": 0,
                                            "self_originated": 0,
                                            "test_discard": 0,
                                            "ttl_check_fail": 0,
                                            "unknown_neighbor": 1,
                                            "version": 0,
                                        },
                                        "ospf_lsa_errors": {
                                            "checksum": 0,
                                            "data": 0,
                                            "length": 0,
                                            "type": 0,
                                        },
                                        "ospf_packets_received_sent": {
                                            "type": {
                                                "rx_db_des": {
                                                    "bytes": 4980,
                                                    "packets": 145,
                                                },
                                                "rx_hello": {
                                                    "bytes": 18443216,
                                                    "packets": 384238,
                                                },
                                                "rx_invalid": {
                                                    "bytes": 0,
                                                    "packets": 0,
                                                },
                                                "rx_ls_ack": {
                                                    "bytes": 713980,
                                                    "packets": 11840,
                                                },
                                                "rx_ls_req": {
                                                    "bytes": 9180,
                                                    "packets": 57,
                                                },
                                                "rx_ls_upd": {
                                                    "bytes": 242036,
                                                    "packets": 2581,
                                                },
                                                "rx_total": {
                                                    "bytes": 19413392,
                                                    "packets": 398861,
                                                },
                                                "tx_db_des": {
                                                    "bytes": 50840,
                                                    "packets": 475,
                                                },
                                                "tx_failed": {"bytes": 0, "packets": 0},
                                                "tx_hello": {
                                                    "bytes": 30825036,
                                                    "packets": 385336,
                                                },
                                                "tx_ls_ack": {
                                                    "bytes": 187352,
                                                    "packets": 2473,
                                                },
                                                "tx_ls_req": {
                                                    "bytes": 404,
                                                    "packets": 7,
                                                },
                                                "tx_ls_upd": {
                                                    "bytes": 13558188,
                                                    "packets": 12658,
                                                },
                                                "tx_total": {
                                                    "bytes": 44621820,
                                                    "packets": 400949,
                                                },
                                            }
                                        },
                                    },
                                    "GigabitEthernet0/0/1": {
                                        "last_clear_traffic_counters": "never",
                                        "ospf_header_errors": {
                                            "adjacency_throttle": 0,
                                            "area_mismatch": 0,
                                            "auth_type": 0,
                                            "authentication": 0,
                                            "bad_source": 0,
                                            "bfd": 0,
                                            "checksum": 0,
                                            "duplicate_id": 0,
                                            "hello": 0,
                                            "instance_id": 0,
                                            "length": 0,
                                            "lls": 0,
                                            "mtu_mismatch": 0,
                                            "nbr_ignored": 0,
                                            "no_sham_link": 0,
                                            "no_virtual_link": 0,
                                            "self_originated": 0,
                                            "test_discard": 0,
                                            "ttl_check_fail": 0,
                                            "unknown_neighbor": 0,
                                            "version": 0,
                                        },
                                        "ospf_lsa_errors": {
                                            "checksum": 0,
                                            "data": 0,
                                            "length": 0,
                                            "type": 0,
                                        },
                                        "ospf_packets_received_sent": {
                                            "type": {
                                                "rx_db_des": {
                                                    "bytes": 11844,
                                                    "packets": 47,
                                                },
                                                "rx_hello": {
                                                    "bytes": 18812552,
                                                    "packets": 391929,
                                                },
                                                "rx_invalid": {
                                                    "bytes": 0,
                                                    "packets": 0,
                                                },
                                                "rx_ls_ack": {
                                                    "bytes": 18804556,
                                                    "packets": 19064,
                                                },
                                                "rx_ls_req": {
                                                    "bytes": 25212,
                                                    "packets": 22,
                                                },
                                                "rx_ls_upd": {
                                                    "bytes": 231124,
                                                    "packets": 1902,
                                                },
                                                "rx_total": {
                                                    "bytes": 37885288,
                                                    "packets": 412964,
                                                },
                                                "tx_db_des": {
                                                    "bytes": 54772,
                                                    "packets": 53,
                                                },
                                                "tx_failed": {"bytes": 0, "packets": 0},
                                                "tx_hello": {
                                                    "bytes": 31355000,
                                                    "packets": 391938,
                                                },
                                                "tx_ls_ack": {
                                                    "bytes": 167024,
                                                    "packets": 1871,
                                                },
                                                "tx_ls_req": {
                                                    "bytes": 6632,
                                                    "packets": 10,
                                                },
                                                "tx_ls_upd": {
                                                    "bytes": 26983772,
                                                    "packets": 26114,
                                                },
                                                "tx_total": {
                                                    "bytes": 58567200,
                                                    "packets": 419986,
                                                },
                                            }
                                        },
                                    },
                                    "GigabitEthernet0/0/3": {
                                        "last_clear_traffic_counters": "never",
                                        "ospf_header_errors": {
                                            "adjacency_throttle": 0,
                                            "area_mismatch": 0,
                                            "auth_type": 0,
                                            "authentication": 0,
                                            "bad_source": 0,
                                            "bfd": 0,
                                            "checksum": 0,
                                            "duplicate_id": 0,
                                            "hello": 0,
                                            "instance_id": 0,
                                            "length": 0,
                                            "lls": 0,
                                            "mtu_mismatch": 0,
                                            "nbr_ignored": 3,
                                            "no_sham_link": 0,
                                            "no_virtual_link": 0,
                                            "self_originated": 0,
                                            "test_discard": 0,
                                            "ttl_check_fail": 0,
                                            "unknown_neighbor": 0,
                                            "version": 0,
                                        },
                                        "ospf_lsa_errors": {
                                            "checksum": 0,
                                            "data": 0,
                                            "length": 0,
                                            "type": 0,
                                        },
                                        "ospf_packets_received_sent": {
                                            "type": {
                                                "rx_db_des": {
                                                    "bytes": 25932,
                                                    "packets": 636,
                                                },
                                                "rx_hello": {
                                                    "bytes": 20276152,
                                                    "packets": 422436,
                                                },
                                                "rx_invalid": {
                                                    "bytes": 0,
                                                    "packets": 0,
                                                },
                                                "rx_ls_ack": {
                                                    "bytes": 788256,
                                                    "packets": 12534,
                                                },
                                                "rx_ls_req": {
                                                    "bytes": 29088,
                                                    "packets": 191,
                                                },
                                                "rx_ls_upd": {
                                                    "bytes": 170236,
                                                    "packets": 1967,
                                                },
                                                "rx_total": {
                                                    "bytes": 21289664,
                                                    "packets": 437764,
                                                },
                                                "tx_db_des": {
                                                    "bytes": 73492,
                                                    "packets": 508,
                                                },
                                                "tx_failed": {"bytes": 0, "packets": 0},
                                                "tx_hello": {
                                                    "bytes": 31262032,
                                                    "packets": 390845,
                                                },
                                                "tx_ls_ack": {
                                                    "bytes": 127024,
                                                    "packets": 1956,
                                                },
                                                "tx_ls_req": {
                                                    "bytes": 644,
                                                    "packets": 10,
                                                },
                                                "tx_ls_upd": {
                                                    "bytes": 15890600,
                                                    "packets": 15015,
                                                },
                                                "tx_total": {
                                                    "bytes": 47353792,
                                                    "packets": 408334,
                                                },
                                            }
                                        },
                                    },
                                    "GigabitEthernet0/0/4": {
                                        "last_clear_traffic_counters": "never",
                                        "ospf_header_errors": {
                                            "adjacency_throttle": 0,
                                            "area_mismatch": 0,
                                            "auth_type": 0,
                                            "authentication": 0,
                                            "bad_source": 0,
                                            "bfd": 0,
                                            "checksum": 0,
                                            "duplicate_id": 0,
                                            "hello": 0,
                                            "instance_id": 0,
                                            "length": 0,
                                            "lls": 0,
                                            "mtu_mismatch": 0,
                                            "nbr_ignored": 0,
                                            "no_sham_link": 0,
                                            "no_virtual_link": 0,
                                            "self_originated": 0,
                                            "test_discard": 0,
                                            "ttl_check_fail": 0,
                                            "unknown_neighbor": 0,
                                            "version": 0,
                                        },
                                        "ospf_lsa_errors": {
                                            "checksum": 0,
                                            "data": 0,
                                            "length": 0,
                                            "type": 0,
                                        },
                                        "ospf_packets_received_sent": {
                                            "type": {
                                                "rx_db_des": {
                                                    "bytes": 524,
                                                    "packets": 12,
                                                },
                                                "rx_hello": {
                                                    "bytes": 14716084,
                                                    "packets": 306586,
                                                },
                                                "rx_invalid": {
                                                    "bytes": 0,
                                                    "packets": 0,
                                                },
                                                "rx_ls_ack": {
                                                    "bytes": 613440,
                                                    "packets": 10100,
                                                },
                                                "rx_ls_req": {
                                                    "bytes": 1032,
                                                    "packets": 6,
                                                },
                                                "rx_ls_upd": {
                                                    "bytes": 165556,
                                                    "packets": 1706,
                                                },
                                                "rx_total": {
                                                    "bytes": 15496636,
                                                    "packets": 318410,
                                                },
                                                "tx_db_des": {
                                                    "bytes": 2816,
                                                    "packets": 19,
                                                },
                                                "tx_failed": {"bytes": 0, "packets": 0},
                                                "tx_hello": {
                                                    "bytes": 24538936,
                                                    "packets": 306737,
                                                },
                                                "tx_ls_ack": {
                                                    "bytes": 132900,
                                                    "packets": 1690,
                                                },
                                                "tx_ls_req": {
                                                    "bytes": 336,
                                                    "packets": 6,
                                                },
                                                "tx_ls_upd": {
                                                    "bytes": 10449232,
                                                    "packets": 11120,
                                                },
                                                "tx_total": {
                                                    "bytes": 35124220,
                                                    "packets": 319572,
                                                },
                                            }
                                        },
                                    },
                                    "GigabitEthernet0/0/5": {
                                        "last_clear_traffic_counters": "never",
                                        "ospf_header_errors": {
                                            "adjacency_throttle": 0,
                                            "area_mismatch": 0,
                                            "auth_type": 0,
                                            "authentication": 0,
                                            "bad_source": 0,
                                            "bfd": 0,
                                            "checksum": 0,
                                            "duplicate_id": 0,
                                            "hello": 0,
                                            "instance_id": 0,
                                            "length": 0,
                                            "lls": 0,
                                            "mtu_mismatch": 0,
                                            "nbr_ignored": 0,
                                            "no_sham_link": 0,
                                            "no_virtual_link": 0,
                                            "self_originated": 0,
                                            "test_discard": 0,
                                            "ttl_check_fail": 0,
                                            "unknown_neighbor": 0,
                                            "version": 0,
                                        },
                                        "ospf_lsa_errors": {
                                            "checksum": 0,
                                            "data": 0,
                                            "length": 0,
                                            "type": 0,
                                        },
                                        "ospf_packets_received_sent": {
                                            "type": {
                                                "rx_db_des": {"bytes": 0, "packets": 0},
                                                "rx_hello": {"bytes": 0, "packets": 0},
                                                "rx_invalid": {
                                                    "bytes": 0,
                                                    "packets": 0,
                                                },
                                                "rx_ls_ack": {"bytes": 0, "packets": 0},
                                                "rx_ls_req": {"bytes": 0, "packets": 0},
                                                "rx_ls_upd": {"bytes": 0, "packets": 0},
                                                "rx_total": {"bytes": 0, "packets": 0},
                                                "tx_db_des": {"bytes": 0, "packets": 0},
                                                "tx_failed": {"bytes": 0, "packets": 0},
                                                "tx_hello": {
                                                    "bytes": 27731564,
                                                    "packets": 364889,
                                                },
                                                "tx_ls_ack": {"bytes": 0, "packets": 0},
                                                "tx_ls_req": {"bytes": 0, "packets": 0},
                                                "tx_ls_upd": {"bytes": 0, "packets": 0},
                                                "tx_total": {
                                                    "bytes": 27731564,
                                                    "packets": 364889,
                                                },
                                            }
                                        },
                                    },
                                    "GigabitEthernet0/0/6": {
                                        "last_clear_traffic_counters": "never",
                                        "ospf_header_errors": {
                                            "adjacency_throttle": 0,
                                            "area_mismatch": 0,
                                            "auth_type": 0,
                                            "authentication": 0,
                                            "bad_source": 0,
                                            "bfd": 0,
                                            "checksum": 0,
                                            "duplicate_id": 0,
                                            "hello": 0,
                                            "instance_id": 0,
                                            "length": 0,
                                            "lls": 0,
                                            "mtu_mismatch": 0,
                                            "nbr_ignored": 0,
                                            "no_sham_link": 0,
                                            "no_virtual_link": 0,
                                            "self_originated": 0,
                                            "test_discard": 0,
                                            "ttl_check_fail": 0,
                                            "unknown_neighbor": 0,
                                            "version": 0,
                                        },
                                        "ospf_lsa_errors": {
                                            "checksum": 0,
                                            "data": 0,
                                            "length": 0,
                                            "type": 0,
                                        },
                                        "ospf_packets_received_sent": {
                                            "type": {
                                                "rx_db_des": {
                                                    "bytes": 1232,
                                                    "packets": 36,
                                                },
                                                "rx_hello": {
                                                    "bytes": 8125472,
                                                    "packets": 169281,
                                                },
                                                "rx_invalid": {
                                                    "bytes": 0,
                                                    "packets": 0,
                                                },
                                                "rx_ls_ack": {
                                                    "bytes": 8733808,
                                                    "packets": 9327,
                                                },
                                                "rx_ls_req": {
                                                    "bytes": 25080,
                                                    "packets": 20,
                                                },
                                                "rx_ls_upd": {
                                                    "bytes": 76640,
                                                    "packets": 908,
                                                },
                                                "rx_total": {
                                                    "bytes": 16962232,
                                                    "packets": 179572,
                                                },
                                                "tx_db_des": {
                                                    "bytes": 43560,
                                                    "packets": 40,
                                                },
                                                "tx_failed": {"bytes": 0, "packets": 0},
                                                "tx_hello": {
                                                    "bytes": 13552440,
                                                    "packets": 169411,
                                                },
                                                "tx_ls_ack": {
                                                    "bytes": 63396,
                                                    "packets": 899,
                                                },
                                                "tx_ls_req": {
                                                    "bytes": 224,
                                                    "packets": 4,
                                                },
                                                "tx_ls_upd": {
                                                    "bytes": 12553264,
                                                    "packets": 12539,
                                                },
                                                "tx_total": {
                                                    "bytes": 26212884,
                                                    "packets": 182893,
                                                },
                                            }
                                        },
                                    },
                                    "GigabitEthernet0/0/7": {
                                        "last_clear_traffic_counters": "never",
                                        "ospf_header_errors": {
                                            "adjacency_throttle": 0,
                                            "area_mismatch": 0,
                                            "auth_type": 0,
                                            "authentication": 0,
                                            "bad_source": 0,
                                            "bfd": 0,
                                            "checksum": 0,
                                            "duplicate_id": 0,
                                            "hello": 0,
                                            "instance_id": 0,
                                            "length": 0,
                                            "lls": 0,
                                            "mtu_mismatch": 0,
                                            "nbr_ignored": 0,
                                            "no_sham_link": 0,
                                            "no_virtual_link": 0,
                                            "self_originated": 0,
                                            "test_discard": 0,
                                            "ttl_check_fail": 0,
                                            "unknown_neighbor": 0,
                                            "version": 0,
                                        },
                                        "ospf_lsa_errors": {
                                            "checksum": 0,
                                            "data": 0,
                                            "length": 0,
                                            "type": 0,
                                        },
                                        "ospf_packets_received_sent": {
                                            "type": {
                                                "rx_db_des": {
                                                    "bytes": 2524,
                                                    "packets": 62,
                                                },
                                                "rx_hello": {
                                                    "bytes": 16812472,
                                                    "packets": 350262,
                                                },
                                                "rx_invalid": {
                                                    "bytes": 0,
                                                    "packets": 0,
                                                },
                                                "rx_ls_ack": {
                                                    "bytes": 759424,
                                                    "packets": 12801,
                                                },
                                                "rx_ls_req": {
                                                    "bytes": 4452,
                                                    "packets": 27,
                                                },
                                                "rx_ls_upd": {
                                                    "bytes": 11921824,
                                                    "packets": 1966,
                                                },
                                                "rx_total": {
                                                    "bytes": 29500696,
                                                    "packets": 365118,
                                                },
                                                "tx_db_des": {
                                                    "bytes": 11964,
                                                    "packets": 81,
                                                },
                                                "tx_failed": {"bytes": 0, "packets": 0},
                                                "tx_hello": {
                                                    "bytes": 29795828,
                                                    "packets": 372638,
                                                },
                                                "tx_ls_ack": {
                                                    "bytes": 256,
                                                    "packets": 4,
                                                },
                                                "tx_ls_req": {
                                                    "bytes": 336,
                                                    "packets": 6,
                                                },
                                                "tx_ls_upd": {
                                                    "bytes": 13471532,
                                                    "packets": 14778,
                                                },
                                                "tx_total": {
                                                    "bytes": 43279916,
                                                    "packets": 387507,
                                                },
                                            }
                                        },
                                    },
                                }
                            },
                            "summary_traffic_statistics": {
                                "ospf_header_errors": {
                                    "adjacency_throttle": 0,
                                    "area_mismatch": 0,
                                    "auth_type": 0,
                                    "authentication": 0,
                                    "bad_source": 0,
                                    "bfd": 0,
                                    "checksum": 0,
                                    "duplicate_id": 0,
                                    "hello": 0,
                                    "instance_id": 0,
                                    "length": 0,
                                    "lls": 0,
                                    "mtu_mismatch": 0,
                                    "nbr_ignored": 3,
                                    "no_sham_link": 0,
                                    "no_virtual_link": 0,
                                    "self_originated": 0,
                                    "test_discard": 0,
                                    "ttl_check_fail": 0,
                                    "unknown_neighbor": 1,
                                    "version": 0,
                                },
                                "ospf_lsa_errors": {
                                    "checksum": 0,
                                    "data": 0,
                                    "length": 0,
                                    "type": 0,
                                },
                                "ospf_packets_received_sent": {
                                    "type": {
                                        "rx_db_des": {"bytes": 47036, "packets": 938},
                                        "rx_hello": {
                                            "bytes": 97185948,
                                            "packets": 2024732,
                                        },
                                        "rx_invalid": {"bytes": 0, "packets": 0},
                                        "rx_ls_ack": {
                                            "bytes": 30413464,
                                            "packets": 75666,
                                        },
                                        "rx_ls_req": {"bytes": 94044, "packets": 323},
                                        "rx_ls_upd": {
                                            "bytes": 12807416,
                                            "packets": 11030,
                                        },
                                        "rx_total": {
                                            "bytes": 140547908,
                                            "packets": 2112689,
                                        },
                                        "tx_db_des": {"bytes": 237444, "packets": 1176},
                                        "tx_failed": {"bytes": 0, "packets": 0},
                                        "tx_hello": {
                                            "bytes": 189060836,
                                            "packets": 2381794,
                                        },
                                        "tx_ls_ack": {"bytes": 677952, "packets": 8893},
                                        "tx_ls_req": {"bytes": 8576, "packets": 43},
                                        "tx_ls_upd": {
                                            "bytes": 92906588,
                                            "packets": 92224,
                                        },
                                        "tx_total": {
                                            "bytes": 282891396,
                                            "packets": 2484130,
                                        },
                                    }
                                },
                            },
                        }
                    }
                }
            }
        }
    },
}
