expected_output = {
    "isis": {
        "64512": {
            "psnp_cache": {
                "hits": 91099,
                "tries": 146551
            },
            "csnp_cache": {
                "hits": 5,
                "tries": 30,
                "updates": 50
            },
            "lsp": {
                "checksum_errors_received": 0,
                "dropped": 0
            },
            "snp": {
                "dropped": 0
            },
            "upd": {
                "max_queue_size": 8,
                "queue_size": 0
            },
            "transmit_time": {
                "hello": {
                    "average_transmit_time_sec": 0,
                    "rate_per_sec": 2
                },
                "csnp": {
                    "average_transmit_time_sec": 0,
                    "rate_per_sec": 0
                },
                "psnp": {
                    "average_transmit_time_sec": 0,
                    "rate_per_sec": 0
                },
                "lsp": {
                    "average_transmit_time_sec": 0,
                    "rate_per_sec": 0
                }
            },
            "process_time": {
                "hello": {
                    "average_process_time_sec": 0,
                    "rate_per_sec": 2
                },
                "csnp": {
                    "average_process_time_sec": 0,
                    "rate_per_sec": 0
                },
                "psnp": {
                    "average_process_time_sec": 0,
                    "rate_per_sec": 0
                },
                "lsp": {
                    "average_process_time_sec": 0,
                    "rate_per_sec": 0
                }
            },
            "level": {
                2: {
                    "lsp": {
                        "new": 50,
                        "refresh": 16892
                    },
                    "address_family": {
                        "IPv4 Unicast": {
                            "total_spf_calculation": 7526,
                            "full_spf_calculation": 7508,
                            "ispf_calculation": 0,
                            "next_hop_calculation": 11,
                            "partial_route_calculation": 7,
                            "periodic_spf_calculation": 7382
                        }
                    }
                }
            },
            "interface": {
                "Loopback0": {},
                "TenGigE0/0/0/0.10": {
                    "level": {
                        2: {
                            "lsps_sourced": {
                                "sent": 49222,
                                "received": 53198,
                                "flooding_duplicates": 7,
                                "arrival_time_throttled": 0
                            },
                            "csnp": {
                                "sent": 1,
                                "received": 1
                            },
                            "psnp": {
                                "sent": 52991,
                                "received": 49049
                            }
                        }
                    }
                },
                "TenGigE0/0/0/0.20": {
                    "level": {
                        2: {
                            "lsps_sourced": {
                                "sent": 4,
                                "received": 12,
                                "flooding_duplicates": 22912,
                                "arrival_time_throttled": 0
                            },
                            "csnp": {
                                "sent": 1,
                                "received": 1
                            },
                            "psnp": {
                                "sent": 4,
                                "received": 3
                            }
                        }
                    }
                },
                "TenGigE0/0/0/1.10": {
                    "level": {
                        2: {
                            "lsps_sourced": {
                                "sent": 0,
                                "received": 0,
                                "flooding_duplicates": 22919,
                                "arrival_time_throttled": 0
                            },
                            "csnp": {
                                "sent": 1,
                                "received": 1
                            },
                            "psnp": {
                                "sent": 0,
                                "received": 0
                            }
                        }
                    }
                },
                "TenGigE0/0/0/1.20": {
                    "level": {
                        2: {
                            "lsps_sourced": {
                                "sent": 8,
                                "received": 0,
                                "flooding_duplicates": 22918,
                                "arrival_time_throttled": 0
                            },
                            "csnp": {
                                "sent": 1,
                                "received": 1
                            },
                            "psnp": {
                                "sent": 0,
                                "received": 1
                            }
                        }
                    }
                },
                "TenGigE0/0/0/2.10": {
                    "level": {
                        2: {
                            "lsps_sourced": {
                                "sent": 42506,
                                "received": 52552,
                                "flooding_duplicates": 63,
                                "arrival_time_throttled": 0
                            },
                            "csnp": {
                                "sent": 4,
                                "received": 4
                            },
                            "psnp": {
                                "sent": 52362,
                                "received": 42363
                            }
                        }
                    }
                },
                "TenGigE0/0/0/2.20": {
                    "level": {
                        2: {
                            "lsps_sourced": {
                                "sent": 13,
                                "received": 7,
                                "flooding_duplicates": 29708,
                                "arrival_time_throttled": 0
                            },
                            "csnp": {
                                "sent": 4,
                                "received": 4
                            },
                            "psnp": {
                                "sent": 6,
                                "received": 1
                            }
                        }
                    }
                },
                "TenGigE0/0/0/3.10": {
                    "level": {
                        2: {
                            "lsps_sourced": {
                                "sent": 14,
                                "received": 9,
                                "flooding_duplicates": 29701,
                                "arrival_time_throttled": 0
                            },
                            "csnp": {
                                "sent": 4,
                                "received": 4
                            },
                            "psnp": {
                                "sent": 5,
                                "received": 2
                            }
                        }
                    }
                },
                "TenGigE0/0/0/3.20": {
                    "level": {
                        2: {
                            "lsps_sourced": {
                                "sent": 22,
                                "received": 6,
                                "flooding_duplicates": 29696,
                                "arrival_time_throttled": 0
                            },
                            "csnp": {
                                "sent": 4,
                                "received": 4
                            },
                            "psnp": {
                                "sent": 5,
                                "received": 1
                            }
                        }
                    }
                },
                "TenGigE0/0/0/4.10": {
                    "level": {
                        2: {
                            "lsps_sourced": {
                                "sent": 37830,
                                "received": 10,
                                "flooding_duplicates": 3636,
                                "arrival_time_throttled": 0
                            },
                            "csnp": {
                                "sent": 5,
                                "received": 5
                            },
                            "psnp": {
                                "sent": 0,
                                "received": 37798
                            }
                        }
                    }
                },
                "TenGigE0/0/0/4.20": {
                    "level": {
                        2: {
                            "lsps_sourced": {
                                "sent": 11,
                                "received": 40757,
                                "flooding_duplicates": 710,
                                "arrival_time_throttled": 0
                            },
                            "csnp": {
                                "sent": 5,
                                "received": 5
                            },
                            "psnp": {
                                "sent": 40495,
                                "received": 3
                            }
                        }
                    }
                }
            }
        }
    }
}
