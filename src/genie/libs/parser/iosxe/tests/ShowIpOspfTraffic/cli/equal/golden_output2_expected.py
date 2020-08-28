expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "10000": {
                            "summary_traffic_statistics": {
                                "ospf_packets_received_sent": {
                                    "type": {
                                        "rx_invalid": {"packets": 0, "bytes": 0},
                                        "rx_hello": {"packets": 0, "bytes": 0},
                                        "rx_db_des": {"packets": 0, "bytes": 0},
                                        "rx_ls_req": {"packets": 0, "bytes": 0},
                                        "rx_ls_upd": {"packets": 0, "bytes": 0},
                                        "rx_ls_ack": {"packets": 0, "bytes": 0},
                                        "rx_total": {"packets": 0, "bytes": 0},
                                        "tx_failed": {"packets": 0, "bytes": 0},
                                        "tx_hello": {"packets": 0, "bytes": 0},
                                        "tx_db_des": {"packets": 0, "bytes": 0},
                                        "tx_ls_req": {"packets": 0, "bytes": 0},
                                        "tx_ls_upd": {"packets": 0, "bytes": 0},
                                        "tx_ls_ack": {"packets": 0, "bytes": 0},
                                        "tx_total": {"packets": 0, "bytes": 0},
                                    }
                                },
                                "ospf_header_errors": {
                                    "length": 0,
                                    "instance_id": 0,
                                    "checksum": 0,
                                    "auth_type": 0,
                                    "version": 0,
                                    "bad_source": 0,
                                    "no_virtual_link": 0,
                                    "area_mismatch": 0,
                                    "no_sham_link": 0,
                                    "self_originated": 0,
                                    "duplicate_id": 0,
                                    "hello": 0,
                                    "mtu_mismatch": 0,
                                    "nbr_ignored": 0,
                                    "lls": 0,
                                    "unknown_neighbor": 0,
                                    "authentication": 0,
                                    "ttl_check_fail": 0,
                                    "adjacency_throttle": 0,
                                    "bfd": 0,
                                    "test_discard": 0,
                                },
                                "ospf_lsa_errors": {
                                    "type": 0,
                                    "length": 0,
                                    "data": 0,
                                    "checksum": 0,
                                },
                            }
                        },
                        "888": {
                            "router_id": "10.19.13.14",
                            "ospf_queue_statistics": {
                                "limit": {"inputq": 0, "updateq": 200, "outputq": 0},
                                "drops": {"inputq": 0, "updateq": 0, "outputq": 0},
                                "max_delay_msec": {
                                    "inputq": 3,
                                    "updateq": 2,
                                    "outputq": 1,
                                },
                                "max_size": {
                                    "total": {"inputq": 4, "updateq": 3, "outputq": 2},
                                    "invalid": {
                                        "inputq": 0,
                                        "updateq": 0,
                                        "outputq": 0,
                                    },
                                    "hello": {"inputq": 4, "updateq": 0, "outputq": 1},
                                    "db_des": {"inputq": 0, "updateq": 0, "outputq": 1},
                                    "ls_req": {"inputq": 0, "updateq": 0, "outputq": 0},
                                    "ls_upd": {"inputq": 0, "updateq": 3, "outputq": 0},
                                    "ls_ack": {"inputq": 0, "updateq": 0, "outputq": 0},
                                },
                                "current_size": {
                                    "total": {"inputq": 0, "updateq": 0, "outputq": 0},
                                    "invalid": {
                                        "inputq": 0,
                                        "updateq": 0,
                                        "outputq": 0,
                                    },
                                    "hello": {"inputq": 0, "updateq": 0, "outputq": 0},
                                    "db_des": {"inputq": 0, "updateq": 0, "outputq": 0},
                                    "ls_req": {"inputq": 0, "updateq": 0, "outputq": 0},
                                    "ls_upd": {"inputq": 0, "updateq": 0, "outputq": 0},
                                    "ls_ack": {"inputq": 0, "updateq": 0, "outputq": 0},
                                },
                            },
                            "interface_statistics": {
                                "interfaces": {
                                    "Tunnel65541": {
                                        "last_clear_traffic_counters": "never",
                                        "ospf_packets_received_sent": {
                                            "type": {
                                                "rx_invalid": {
                                                    "packets": 0,
                                                    "bytes": 0,
                                                },
                                                "rx_hello": {"packets": 0, "bytes": 0},
                                                "rx_db_des": {"packets": 0, "bytes": 0},
                                                "rx_ls_req": {"packets": 0, "bytes": 0},
                                                "rx_ls_upd": {"packets": 0, "bytes": 0},
                                                "rx_ls_ack": {"packets": 0, "bytes": 0},
                                                "rx_total": {"packets": 0, "bytes": 0},
                                                "tx_failed": {"packets": 0, "bytes": 0},
                                                "tx_hello": {
                                                    "packets": 62301,
                                                    "bytes": 5980896,
                                                },
                                                "tx_db_des": {"packets": 0, "bytes": 0},
                                                "tx_ls_req": {"packets": 0, "bytes": 0},
                                                "tx_ls_upd": {"packets": 0, "bytes": 0},
                                                "tx_ls_ack": {"packets": 0, "bytes": 0},
                                                "tx_total": {
                                                    "packets": 62301,
                                                    "bytes": 5980896,
                                                },
                                            }
                                        },
                                        "ospf_header_errors": {
                                            "length": 0,
                                            "instance_id": 0,
                                            "checksum": 0,
                                            "auth_type": 0,
                                            "version": 0,
                                            "bad_source": 0,
                                            "no_virtual_link": 0,
                                            "area_mismatch": 0,
                                            "no_sham_link": 0,
                                            "self_originated": 0,
                                            "duplicate_id": 0,
                                            "hello": 0,
                                            "mtu_mismatch": 0,
                                            "nbr_ignored": 0,
                                            "lls": 0,
                                            "unknown_neighbor": 0,
                                            "authentication": 0,
                                            "ttl_check_fail": 0,
                                            "adjacency_throttle": 0,
                                            "bfd": 0,
                                            "test_discard": 0,
                                        },
                                        "ospf_lsa_errors": {
                                            "type": 0,
                                            "length": 0,
                                            "data": 0,
                                            "checksum": 0,
                                        },
                                    },
                                    "GigabitEthernet0/1/7": {
                                        "last_clear_traffic_counters": "never",
                                        "ospf_packets_received_sent": {
                                            "type": {
                                                "rx_invalid": {
                                                    "packets": 0,
                                                    "bytes": 0,
                                                },
                                                "rx_hello": {
                                                    "packets": 70493,
                                                    "bytes": 3383664,
                                                },
                                                "rx_db_des": {
                                                    "packets": 3,
                                                    "bytes": 1676,
                                                },
                                                "rx_ls_req": {
                                                    "packets": 1,
                                                    "bytes": 36,
                                                },
                                                "rx_ls_upd": {
                                                    "packets": 14963,
                                                    "bytes": 1870388,
                                                },
                                                "rx_ls_ack": {
                                                    "packets": 880,
                                                    "bytes": 76140,
                                                },
                                                "rx_total": {
                                                    "packets": 86340,
                                                    "bytes": 5331904,
                                                },
                                                "tx_failed": {"packets": 0, "bytes": 0},
                                                "tx_hello": {
                                                    "packets": 1,
                                                    "bytes": 100,
                                                },
                                                "tx_db_des": {
                                                    "packets": 4,
                                                    "bytes": 416,
                                                },
                                                "tx_ls_req": {
                                                    "packets": 1,
                                                    "bytes": 968,
                                                },
                                                "tx_ls_upd": {
                                                    "packets": 1,
                                                    "bytes": 108,
                                                },
                                                "tx_ls_ack": {
                                                    "packets": 134,
                                                    "bytes": 9456,
                                                },
                                                "tx_total": {
                                                    "packets": 141,
                                                    "bytes": 11048,
                                                },
                                            }
                                        },
                                        "ospf_header_errors": {
                                            "length": 0,
                                            "instance_id": 0,
                                            "checksum": 0,
                                            "auth_type": 0,
                                            "version": 0,
                                            "bad_source": 0,
                                            "no_virtual_link": 0,
                                            "area_mismatch": 0,
                                            "no_sham_link": 0,
                                            "self_originated": 0,
                                            "duplicate_id": 0,
                                            "hello": 0,
                                            "mtu_mismatch": 0,
                                            "nbr_ignored": 0,
                                            "lls": 0,
                                            "unknown_neighbor": 0,
                                            "authentication": 0,
                                            "ttl_check_fail": 0,
                                            "adjacency_throttle": 0,
                                            "bfd": 0,
                                            "test_discard": 0,
                                        },
                                        "ospf_lsa_errors": {
                                            "type": 0,
                                            "length": 0,
                                            "data": 0,
                                            "checksum": 0,
                                        },
                                    },
                                    "GigabitEthernet0/1/6": {
                                        "last_clear_traffic_counters": "never",
                                        "ospf_packets_received_sent": {
                                            "type": {
                                                "rx_invalid": {
                                                    "packets": 0,
                                                    "bytes": 0,
                                                },
                                                "rx_hello": {
                                                    "packets": 70504,
                                                    "bytes": 3384192,
                                                },
                                                "rx_db_des": {
                                                    "packets": 3,
                                                    "bytes": 1676,
                                                },
                                                "rx_ls_req": {
                                                    "packets": 1,
                                                    "bytes": 36,
                                                },
                                                "rx_ls_upd": {
                                                    "packets": 14809,
                                                    "bytes": 1866264,
                                                },
                                                "rx_ls_ack": {
                                                    "packets": 877,
                                                    "bytes": 76028,
                                                },
                                                "rx_total": {
                                                    "packets": 86194,
                                                    "bytes": 5328196,
                                                },
                                                "tx_failed": {"packets": 0, "bytes": 0},
                                                "tx_hello": {
                                                    "packets": 1,
                                                    "bytes": 100,
                                                },
                                                "tx_db_des": {
                                                    "packets": 4,
                                                    "bytes": 416,
                                                },
                                                "tx_ls_req": {
                                                    "packets": 1,
                                                    "bytes": 968,
                                                },
                                                "tx_ls_upd": {
                                                    "packets": 1,
                                                    "bytes": 108,
                                                },
                                                "tx_ls_ack": {
                                                    "packets": 117,
                                                    "bytes": 8668,
                                                },
                                                "tx_total": {
                                                    "packets": 124,
                                                    "bytes": 10260,
                                                },
                                            }
                                        },
                                        "ospf_header_errors": {
                                            "length": 0,
                                            "instance_id": 0,
                                            "checksum": 0,
                                            "auth_type": 0,
                                            "version": 0,
                                            "bad_source": 0,
                                            "no_virtual_link": 0,
                                            "area_mismatch": 0,
                                            "no_sham_link": 0,
                                            "self_originated": 0,
                                            "duplicate_id": 0,
                                            "hello": 0,
                                            "mtu_mismatch": 0,
                                            "nbr_ignored": 0,
                                            "lls": 0,
                                            "unknown_neighbor": 0,
                                            "authentication": 0,
                                            "ttl_check_fail": 0,
                                            "adjacency_throttle": 0,
                                            "bfd": 0,
                                            "test_discard": 0,
                                        },
                                        "ospf_lsa_errors": {
                                            "type": 0,
                                            "length": 0,
                                            "data": 0,
                                            "checksum": 0,
                                        },
                                    },
                                }
                            },
                            "summary_traffic_statistics": {
                                "ospf_packets_received_sent": {
                                    "type": {
                                        "rx_invalid": {"packets": 0, "bytes": 0},
                                        "rx_hello": {
                                            "packets": 159187,
                                            "bytes": 7640968,
                                        },
                                        "rx_db_des": {
                                            "packets": 10240,
                                            "bytes": 337720,
                                        },
                                        "rx_ls_req": {"packets": 5, "bytes": 216},
                                        "rx_ls_upd": {
                                            "packets": 31899,
                                            "bytes": 4010656,
                                        },
                                        "rx_ls_ack": {"packets": 2511, "bytes": 201204},
                                        "rx_total": {
                                            "packets": 203842,
                                            "bytes": 12190764,
                                        },
                                        "tx_failed": {"packets": 0, "bytes": 0},
                                        "tx_hello": {
                                            "packets": 208493,
                                            "bytes": 20592264,
                                        },
                                        "tx_db_des": {
                                            "packets": 10540,
                                            "bytes": 15808320,
                                        },
                                        "tx_ls_req": {"packets": 5, "bytes": 3112},
                                        "tx_ls_upd": {
                                            "packets": 33998,
                                            "bytes": 5309252,
                                        },
                                        "tx_ls_ack": {
                                            "packets": 17571,
                                            "bytes": 1220144,
                                        },
                                        "tx_total": {
                                            "packets": 270607,
                                            "bytes": 42933092,
                                        },
                                    }
                                },
                                "ospf_header_errors": {
                                    "length": 0,
                                    "instance_id": 0,
                                    "checksum": 0,
                                    "auth_type": 0,
                                    "version": 0,
                                    "bad_source": 0,
                                    "no_virtual_link": 0,
                                    "area_mismatch": 0,
                                    "no_sham_link": 0,
                                    "self_originated": 0,
                                    "duplicate_id": 0,
                                    "hello": 0,
                                    "mtu_mismatch": 0,
                                    "nbr_ignored": 2682,
                                    "lls": 0,
                                    "unknown_neighbor": 0,
                                    "authentication": 0,
                                    "ttl_check_fail": 0,
                                    "adjacency_throttle": 0,
                                    "bfd": 0,
                                    "test_discard": 0,
                                },
                                "ospf_lsa_errors": {
                                    "type": 0,
                                    "length": 0,
                                    "data": 0,
                                    "checksum": 0,
                                },
                            },
                        },
                    }
                }
            }
        }
    },
    "ospf_statistics": {
        "last_clear_traffic_counters": "never",
        "rcvd": {
            "total": 204136,
            "checksum_errors": 0,
            "hello": 159184,
            "database_desc": 10240,
            "link_state_req": 5,
            "link_state_updates": 31899,
            "link_state_acks": 2511,
        },
        "sent": {
            "total": 281838,
            "hello": 219736,
            "database_desc": 10540,
            "link_state_req": 5,
            "link_state_updates": 33998,
            "link_state_acks": 17571,
        },
    },
}
