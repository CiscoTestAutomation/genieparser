

expected_output = {
    "isis": {
        "test": {
            "psnp_cache": {
                "hits": 21,
                "tries": 118},
            "csnp_cache": {
                "hits": 1398,
                "tries": 1501,
                "updates": 204},
            "lsp": {
                "checksum_errors_received": 0,
                "dropped": 0},
            "snp": {
                "dropped": 0},
            "upd": {
                "max_queue_size": 3,
                "queue_size": 0},
            "transmit_time": {
                "hello": {
                    "average_transmit_time_sec": 0,
                    "average_transmit_time_nsec": 66473,
                    "rate_per_sec": 15,
                },
                "csnp": {
                    "average_transmit_time_sec": 0,
                    "average_transmit_time_nsec": 45979,
                    "rate_per_sec": 2,
                },
                "psnp": {
                    "average_transmit_time_sec": 0,
                    "average_transmit_time_nsec": 4113,
                    "rate_per_sec": 0,
                },
                "lsp": {
                    "average_transmit_time_sec": 0,
                    "average_transmit_time_nsec": 14392,
                    "rate_per_sec": 0,
                },
            },
            "process_time": {
                "hello": {
                    "average_process_time_sec": 0,
                    "average_process_time_nsec": 51163,
                    "rate_per_sec": 9,
                },
                "csnp": {
                    "average_process_time_sec": 0,
                    "average_process_time_nsec": 26914,
                    "rate_per_sec": 1,
                },
                "psnp": {
                    "average_process_time_sec": 0,
                    "average_process_time_nsec": 39758,
                    "rate_per_sec": 0,
                },
                "lsp": {
                    "average_process_time_sec": 0,
                    "average_process_time_nsec": 52706,
                    "rate_per_sec": 0,
                },
            },
            "level": {
                1: {
                    "lsp": {
                        "new": 11,
                        "refresh": 15},
                    "address_family": {
                        "IPv4 Unicast": {
                            "total_spf_calculation": 18,
                            "full_spf_calculation": 16,
                            "ispf_calculation": 0,
                            "next_hop_calculation": 0,
                            "partial_route_calculation": 2,
                            "periodic_spf_calculation": 3,
                        },
                        "IPv6 Unicast": {
                            "total_spf_calculation": 19,
                            "full_spf_calculation": 17,
                            "ispf_calculation": 0,
                            "next_hop_calculation": 0,
                            "partial_route_calculation": 2,
                            "periodic_spf_calculation": 3,
                        },
                    },
                },
                2: {
                    "lsp": {
                        "new": 13,
                        "refresh": 11},
                    "address_family": {
                        "IPv4 Unicast": {
                            "total_spf_calculation": 23,
                            "full_spf_calculation": 15,
                            "ispf_calculation": 0,
                            "next_hop_calculation": 0,
                            "partial_route_calculation": 8,
                            "periodic_spf_calculation": 4,
                        },
                        "IPv6 Unicast": {
                            "total_spf_calculation": 22,
                            "full_spf_calculation": 14,
                            "ispf_calculation": 0,
                            "next_hop_calculation": 0,
                            "partial_route_calculation": 8,
                            "periodic_spf_calculation": 4,
                        },
                    },
                },
            },
            "interface": {
                "Loopback0": {
                    "level": {
                        1: {
                            "lsps_sourced": {
                                "sent": 0,
                                "received": 0,
                                "flooding_duplicates": 51,
                                "arrival_time_throttled": 0,
                            },
                            "csnp": {
                                "sent": 0,
                                "received": 0},
                            "psnp": {
                                "sent": 0,
                                "received": 0},
                        },
                        2: {
                            "lsps_sourced": {
                                "sent": 0,
                                "received": 0,
                                "flooding_duplicates": 46,
                                "arrival_time_throttled": 0,
                            },
                            "csnp": {
                                "sent": 0,
                                "received": 0},
                            "psnp": {
                                "sent": 0,
                                "received": 0},
                        },
                    }
                },
                "GigabitEthernet0/0/0/0": {
                    "level": {
                        1: {
                            "hello": {
                                "received": 594,
                                "sent": 593},
                            "dr": {
                                "elections": 1},
                            "lsps_sourced": {
                                "sent": 0,
                                "received": 0,
                                "flooding_duplicates": 51,
                                "arrival_time_throttled": 0,
                            },
                            "csnp": {
                                "sent": 0,
                                "received": 0},
                            "psnp": {
                                "sent": 0,
                                "received": 0},
                        },
                        2: {
                            "hello": {
                                "received": 1779,
                                "sent": 594},
                            "dr": {
                                "elections": 1},
                            "lsps_sourced": {
                                "sent": 63,
                                "received": 7,
                                "flooding_duplicates": 0,
                                "arrival_time_throttled": 0,
                            },
                            "csnp": {
                                "sent": 595,
                                "received": 0},
                            "psnp": {
                                "sent": 0,
                                "received": 0},
                        },
                    }
                },
                "GigabitEthernet0/0/0/1": {
                    "level": {
                        1: {
                            "hello": {
                                "received": 1294,
                                "sent": 604},
                            "dr": {
                                "elections": 5},
                            "lsps_sourced": {
                                "sent": 47,
                                "received": 15,
                                "flooding_duplicates": 8,
                                "arrival_time_throttled": 0,
                            },
                            "csnp": {
                                "sent": 339,
                                "received": 0},
                            "psnp": {
                                "sent": 0,
                                "received": 1},
                        },
                        2: {
                            "hello": {
                                "received": 724,
                                "sent": 281},
                            "dr": {
                                "elections": 5},
                            "lsps_sourced": {
                                "sent": 0,
                                "received": 0,
                                "flooding_duplicates": 42,
                                "arrival_time_throttled": 0,
                            },
                            "csnp": {
                                "sent": 0,
                                "received": 0},
                            "psnp": {
                                "sent": 0,
                                "received": 0},
                        },
                    }
                },
                "GigabitEthernet0/0/0/2": {
                    "level": {
                        1: {
                            "hello": {
                                "received": 1739,
                                "sent": 572},
                            "dr": {
                                "elections": 3},
                            "lsps_sourced": {
                                "sent": 51,
                                "received": 31,
                                "flooding_duplicates": 0,
                                "arrival_time_throttled": 0,
                            },
                            "csnp": {
                                "sent": 567,
                                "received": 0},
                            "psnp": {
                                "sent": 0,
                                "received": 0},
                        },
                        2: {
                            "hello": {
                                "received": 597,
                                "sent": 0},
                            "dr": {
                                "elections": 1},
                            "lsps_sourced": {
                                "sent": 0,
                                "received": 0,
                                "flooding_duplicates": 46,
                                "arrival_time_throttled": 0,
                            },
                            "csnp": {
                                "sent": 0,
                                "received": 0},
                            "psnp": {
                                "sent": 0,
                                "received": 0},
                        },
                    }
                },
                "GigabitEthernet0/0/0/3": {
                    "level": {
                        1: {
                            "hello": {
                                "received": 598,
                                "sent": 1115},
                            "dr": {
                                "elections": 3},
                            "lsps_sourced": {
                                "sent": 38,
                                "received": 26,
                                "flooding_duplicates": 5,
                                "arrival_time_throttled": 0,
                            },
                            "csnp": {
                                "sent": 0,
                                "received": 370},
                            "psnp": {
                                "sent": 0,
                                "received": 0},
                        },
                        2: {
                            "hello": {
                                "received": 596,
                                "sent": 1113},
                            "dr": {
                                "elections": 3},
                            "lsps_sourced": {
                                "sent": 18,
                                "received": 39,
                                "flooding_duplicates": 3,
                                "arrival_time_throttled": 0,
                            },
                            "csnp": {
                                "sent": 0,
                                "received": 370},
                            "psnp": {
                                "sent": 0,
                                "received": 0},
                        },
                    }
                },
            },
        }
    }
}
