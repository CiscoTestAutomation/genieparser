expected_output = {
    "cpp": {
        "0": {
            "subdev": {
                "0": {
                    "input": {
                        "priority": {
                            "pps": {
                                "5_secs": 0,
                                "1_min": 0,
                                "5_min": 0,
                                "60_min": 0
                            },
                            "bps": {
                                "5_secs": 0,
                                "1_min": 0,
                                "5_min": 0,
                                "60_min": 0
                            }
                        },
                        "non_priority": {
                            "pps": {
                                "5_secs": 2,
                                "1_min": 3,
                                "5_min": 3,
                                "60_min": 1
                            },
                            "bps": {
                                "5_secs": 1040,
                                "1_min": 1552,
                                "5_min": 1552,
                                "60_min": 752
                            }
                        },
                        "total": {
                            "pps": {
                                "5_secs": 2,
                                "1_min": 3,
                                "5_min": 3,
                                "60_min": 1
                            },
                            "bps": {
                                "5_secs": 1040,
                                "1_min": 1552,
                                "5_min": 1552,
                                "60_min": 752
                            }
                        }
                    },
                    "output": {
                        "priority": {
                            "pps": {
                                "5_secs": 0,
                                "1_min": 0,
                                "5_min": 0,
                                "60_min": 0
                            },
                            "bps": {
                                "5_secs": 0,
                                "1_min": 0,
                                "5_min": 0,
                                "60_min": 0
                            }
                        },
                        "non_priority": {
                            "pps": {
                                "5_secs": 1,
                                "1_min": 2,
                                "5_min": 2,
                                "60_min": 1
                            },
                            "bps": {
                                "5_secs": 4864,
                                "1_min": 17624,
                                "5_min": 17632,
                                "60_min": 8360
                            }
                        },
                        "total": {
                            "pps": {
                                "5_secs": 1,
                                "1_min": 2,
                                "5_min": 2,
                                "60_min": 1
                            },
                            "bps": {
                                "5_secs": 4864,
                                "1_min": 17624,
                                "5_min": 17632,
                                "60_min": 8360
                            }
                        }
                    },
                    "processing": {
                        "load_pct": {
                            "5_secs": 1,
                            "1_min": 1,
                            "5_min": 1,
                            "60_min": 1
                        }
                    },
                    "crypto_io": {
                        "crypto": {
                            "load_pct": {
                                "5_secs": 0,
                                "1_min": 0,
                                "5_min": 0,
                                "60_min": 0
                            }
                        },
                        "rx": {
                            "load_pct": {
                                "5_secs": 0,
                                "1_min": 0,
                                "5_min": 0,
                                "60_min": 0
                            }
                        },
                        "tx": {
                            "load_pct": {
                                "5_secs": 1,
                                "1_min": 1,
                                "5_min": 1,
                                "60_min": 6
                            },
                            "idle_pct": {
                                "5_secs": 98,
                                "1_min": 98,
                                "5_min": 98,
                                "60_min": 93
                            }
                        }
                    }
                }
            }
        }
    }
}