expected_output = {
    "vrf": {
        "VRF1": {
            "interface": {
                "GigabitEthernet2": {
                    "static_group": {
                        "239.5.5.5 *": {
                            "group": "239.5.5.5",
                            "source": "*",
                            "last_reporter": "0.0.0.0",
                            "up_time": "00:06:17",
                            "flags": "SG",
                        },
                        "239.6.6.6 *": {
                            "group": "239.6.6.6",
                            "source": "*",
                            "last_reporter": "0.0.0.0",
                            "up_time": "00:06:14",
                            "flags": "SG",
                        },
                    },
                    "join_group": {
                        "239.8.8.8 10.16.2.2": {
                            "group": "239.8.8.8",
                            "source": "10.16.2.2",
                            "last_reporter": "0.0.0.0",
                            "flags": "SS",
                            "forward": True,
                            "csr_exp": "stopped",
                            "up_time": "00:05:59",
                            "v3_exp": "stopped",
                        },
                        "239.3.3.3 10.4.1.1": {
                            "group": "239.3.3.3",
                            "source": "10.4.1.1",
                            "last_reporter": "10.186.2.1",
                            "flags": "L",
                            "forward": True,
                            "csr_exp": "stopped",
                            "up_time": "00:06:24",
                            "v3_exp": "stopped",
                        },
                        "239.1.1.1 *": {
                            "group": "239.1.1.1",
                            "source": "*",
                            "last_reporter": "10.186.2.1",
                            "up_time": "00:06:24",
                            "flags": "L U",
                            "expire": "never",
                        },
                        "239.4.4.4 10.4.1.2": {
                            "group": "239.4.4.4",
                            "source": "10.4.1.2",
                            "last_reporter": "10.186.2.1",
                            "flags": "L",
                            "forward": True,
                            "csr_exp": "stopped",
                            "up_time": "00:06:23",
                            "v3_exp": "stopped",
                        },
                        "239.7.7.7 10.16.2.1": {
                            "group": "239.7.7.7",
                            "source": "10.16.2.1",
                            "last_reporter": "0.0.0.0",
                            "flags": "SS",
                            "forward": True,
                            "csr_exp": "stopped",
                            "up_time": "00:06:06",
                            "v3_exp": "stopped",
                        },
                        "239.2.2.2 *": {
                            "group": "239.2.2.2",
                            "source": "*",
                            "last_reporter": "10.186.2.1",
                            "up_time": "00:06:24",
                            "flags": "L U",
                            "expire": "never",
                        },
                        "239.8.8.8 10.16.2.1": {
                            "group": "239.8.8.8",
                            "source": "10.16.2.1",
                            "last_reporter": "0.0.0.0",
                            "flags": "SS",
                            "forward": True,
                            "csr_exp": "stopped",
                            "up_time": "00:05:59",
                            "v3_exp": "stopped",
                        },
                        "224.0.1.40 *": {
                            "group": "224.0.1.40",
                            "source": "*",
                            "last_reporter": "10.186.2.1",
                            "up_time": "00:25:55",
                            "flags": "L U",
                        },
                    },
                    "group": {
                        "239.4.4.4": {
                            "group_mode": "include",
                            "last_reporter": "10.186.2.1",
                            "flags": "L",
                            "source": {
                                "10.4.1.2": {
                                    "forward": True,
                                    "flags": "L",
                                    "up_time": "00:06:23",
                                    "v3_exp": "stopped",
                                    "csr_exp": "stopped",
                                }
                            },
                            "up_time": "00:06:23",
                        },
                        "239.5.5.5": {
                            "group_mode": "include",
                            "last_reporter": "0.0.0.0",
                            "flags": "SG",
                            "up_time": "00:06:17",
                        },
                        "239.1.1.1": {
                            "group_mode": "exclude",
                            "last_reporter": "10.186.2.1",
                            "flags": "L U",
                            "up_time": "00:06:24",
                            "expire": "never",
                        },
                        "239.3.3.3": {
                            "group_mode": "include",
                            "last_reporter": "10.186.2.1",
                            "flags": "L",
                            "source": {
                                "10.4.1.1": {
                                    "forward": True,
                                    "flags": "L",
                                    "up_time": "00:06:24",
                                    "v3_exp": "stopped",
                                    "csr_exp": "stopped",
                                }
                            },
                            "up_time": "00:06:24",
                        },
                        "239.6.6.6": {
                            "group_mode": "include",
                            "last_reporter": "0.0.0.0",
                            "flags": "SG",
                            "up_time": "00:06:14",
                        },
                        "239.8.8.8": {
                            "group_mode": "include",
                            "last_reporter": "0.0.0.0",
                            "flags": "SS",
                            "source": {
                                "10.16.2.1": {
                                    "forward": True,
                                    "flags": "S",
                                    "up_time": "00:03:56",
                                    "v3_exp": "stopped",
                                    "csr_exp": "stopped",
                                },
                                "10.16.2.2": {
                                    "forward": True,
                                    "flags": "S",
                                    "up_time": "00:05:57",
                                    "v3_exp": "stopped",
                                    "csr_exp": "stopped",
                                },
                            },
                            "up_time": "00:05:59",
                        },
                        "224.0.1.40": {
                            "group_mode": "include",
                            "last_reporter": "10.186.2.1",
                            "flags": "L U",
                            "up_time": "00:25:55",
                        },
                        "239.7.7.7": {
                            "group_mode": "include",
                            "last_reporter": "0.0.0.0",
                            "flags": "SS",
                            "source": {
                                "10.16.2.1": {
                                    "forward": True,
                                    "flags": "S",
                                    "up_time": "00:06:06",
                                    "v3_exp": "stopped",
                                    "csr_exp": "stopped",
                                }
                            },
                            "up_time": "00:06:06",
                        },
                        "239.2.2.2": {
                            "group_mode": "exclude",
                            "last_reporter": "10.186.2.1",
                            "flags": "L U",
                            "up_time": "00:06:24",
                            "expire": "never",
                        },
                    },
                }
            }
        }
    }
}
