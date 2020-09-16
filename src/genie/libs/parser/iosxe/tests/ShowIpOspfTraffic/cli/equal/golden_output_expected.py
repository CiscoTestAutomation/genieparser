expected_output = {
    "ospf_statistics": {
        "last_clear_traffic_counters": "never",
        "rcvd": {
            "total": 1082870,
            "checksum_errors": 0,
            "hello": 961667,
            "database_desc": 1688,
            "link_state_req": 32,
            "link_state_updates": 94694,
            "link_state_acks": 24370,
        },
        "sent": {
            "total": 1072239,
            "hello": 932534,
            "database_desc": 1251,
            "link_state_req": 170,
            "link_state_updates": 74590,
            "link_state_acks": 63700,
        },
    },
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "888": {
                            "router_id": "192.168.36.220",
                            "ospf_queue_statistics": {
                                "limit": {"inputq": 0, "updateq": 200, "outputq": 0},
                                "drops": {"inputq": 0, "updateq": 0, "outputq": 0},
                                "max_delay_msec": {
                                    "inputq": 344,
                                    "updateq": 269,
                                    "outputq": 12,
                                },
                                "max_size": {
                                    "total": {"inputq": 5, "updateq": 5, "outputq": 2},
                                    "invalid": {
                                        "inputq": 0,
                                        "updateq": 0,
                                        "outputq": 0,
                                    },
                                    "hello": {"inputq": 1, "updateq": 0, "outputq": 1},
                                    "db_des": {"inputq": 2, "updateq": 0, "outputq": 1},
                                    "ls_req": {"inputq": 0, "updateq": 0, "outputq": 0},
                                    "ls_upd": {"inputq": 2, "updateq": 5, "outputq": 0},
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
                                    "GigabitEthernet0/0/0": {
                                        "last_clear_traffic_counters": "never",
                                        "ospf_packets_received_sent": {
                                            "type": {
                                                "rx_invalid": {
                                                    "packets": 0,
                                                    "bytes": 0,
                                                },
                                                "rx_hello": {
                                                    "packets": 495694,
                                                    "bytes": 23793308,
                                                },
                                                "rx_db_des": {
                                                    "packets": 1676,
                                                    "bytes": 298812,
                                                },
                                                "rx_ls_req": {
                                                    "packets": 30,
                                                    "bytes": 1392,
                                                },
                                                "rx_ls_upd": {
                                                    "packets": 46764,
                                                    "bytes": 4399320,
                                                },
                                                "rx_ls_ack": {
                                                    "packets": 6580,
                                                    "bytes": 316460,
                                                },
                                                "rx_total": {
                                                    "packets": 550744,
                                                    "bytes": 28809292,
                                                },
                                                "tx_failed": {"packets": 0, "bytes": 0},
                                                "tx_hello": {
                                                    "packets": 466574,
                                                    "bytes": 37324132,
                                                },
                                                "tx_db_des": {
                                                    "packets": 1238,
                                                    "bytes": 326112,
                                                },
                                                "tx_ls_req": {
                                                    "packets": 169,
                                                    "bytes": 10388,
                                                },
                                                "tx_ls_upd": {
                                                    "packets": 47473,
                                                    "bytes": 4865652,
                                                },
                                                "tx_ls_ack": {
                                                    "packets": 36140,
                                                    "bytes": 2827140,
                                                },
                                                "tx_total": {
                                                    "packets": 551594,
                                                    "bytes": 45353424,
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
                                            "unknown_neighbor": 419,
                                            "authentication": 0,
                                            "ttl_check_fail": 0,
                                            "test_discard": 0,
                                        },
                                        "ospf_lsa_errors": {
                                            "type": 0,
                                            "length": 0,
                                            "data": 0,
                                            "checksum": 0,
                                        },
                                    },
                                    "TenGigabitEthernet0/2/0": {
                                        "last_clear_traffic_counters": "never",
                                        "ospf_packets_received_sent": {
                                            "type": {
                                                "rx_invalid": {
                                                    "packets": 0,
                                                    "bytes": 0,
                                                },
                                                "rx_hello": {
                                                    "packets": 465973,
                                                    "bytes": 22366692,
                                                },
                                                "rx_db_des": {
                                                    "packets": 12,
                                                    "bytes": 1764,
                                                },
                                                "rx_ls_req": {
                                                    "packets": 2,
                                                    "bytes": 312,
                                                },
                                                "rx_ls_upd": {
                                                    "packets": 47930,
                                                    "bytes": 4445532,
                                                },
                                                "rx_ls_ack": {
                                                    "packets": 17790,
                                                    "bytes": 971660,
                                                },
                                                "rx_total": {
                                                    "packets": 531707,
                                                    "bytes": 27785960,
                                                },
                                                "tx_failed": {"packets": 0, "bytes": 0},
                                                "tx_hello": {
                                                    "packets": 465960,
                                                    "bytes": 37276652,
                                                },
                                                "tx_db_des": {
                                                    "packets": 13,
                                                    "bytes": 2592,
                                                },
                                                "tx_ls_req": {
                                                    "packets": 1,
                                                    "bytes": 56,
                                                },
                                                "tx_ls_upd": {
                                                    "packets": 27117,
                                                    "bytes": 2661612,
                                                },
                                                "tx_ls_ack": {
                                                    "packets": 27560,
                                                    "bytes": 2130760,
                                                },
                                                "tx_total": {
                                                    "packets": 520651,
                                                    "bytes": 42071672,
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
                                            "packets": 961667,
                                            "bytes": 46160000,
                                        },
                                        "rx_db_des": {"packets": 1688, "bytes": 300576},
                                        "rx_ls_req": {"packets": 32, "bytes": 1704},
                                        "rx_ls_upd": {
                                            "packets": 94694,
                                            "bytes": 8844852,
                                        },
                                        "rx_ls_ack": {
                                            "packets": 24370,
                                            "bytes": 1288120,
                                        },
                                        "rx_total": {
                                            "packets": 1082451,
                                            "bytes": 56595252,
                                        },
                                        "tx_failed": {"packets": 0, "bytes": 0},
                                        "tx_hello": {
                                            "packets": 932534,
                                            "bytes": 74600784,
                                        },
                                        "tx_db_des": {"packets": 1251, "bytes": 328704},
                                        "tx_ls_req": {"packets": 170, "bytes": 10444},
                                        "tx_ls_upd": {
                                            "packets": 74590,
                                            "bytes": 7527264,
                                        },
                                        "tx_ls_ack": {
                                            "packets": 63700,
                                            "bytes": 4957900,
                                        },
                                        "tx_total": {
                                            "packets": 1072245,
                                            "bytes": 87425096,
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
                                    "unknown_neighbor": 419,
                                    "authentication": 0,
                                    "ttl_check_fail": 0,
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
                    }
                }
            }
        }
    },
}
