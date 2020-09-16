expected_output = {
    "vrf": {
        "default": {
            "interface": {
                "GigabitEthernet1": {
                    "group": {
                        "239.1.1.1": {
                            "group_mode": "include",
                            "up_time": "00:05:06",
                            "flags": "L U",
                            "last_reporter": "10.1.2.1",
                        },
                        "239.5.5.5": {
                            "group_mode": "include",
                            "up_time": "00:05:06",
                            "flags": "SG",
                            "last_reporter": "0.0.0.0",
                        },
                        "239.4.4.4": {
                            "group_mode": "include",
                            "up_time": "00:05:06",
                            "flags": "L",
                            "source": {
                                "10.4.1.2": {
                                    "up_time": "00:05:06",
                                    "flags": "L",
                                    "forward": True,
                                    "csr_exp": "stopped",
                                    "v3_exp": "stopped",
                                }
                            },
                            "last_reporter": "10.1.2.1",
                        },
                        "239.8.8.8": {
                            "group_mode": "include",
                            "up_time": "00:05:06",
                            "flags": "SS",
                            "source": {
                                "10.16.2.1": {
                                    "up_time": "00:05:06",
                                    "flags": "S",
                                    "forward": True,
                                    "csr_exp": "stopped",
                                    "v3_exp": "stopped",
                                },
                                "10.16.2.2": {
                                    "up_time": "00:05:06",
                                    "flags": "S",
                                    "forward": True,
                                    "csr_exp": "stopped",
                                    "v3_exp": "stopped",
                                },
                            },
                            "last_reporter": "0.0.0.0",
                        },
                        "239.6.6.6": {
                            "group_mode": "include",
                            "up_time": "00:05:06",
                            "flags": "SG",
                            "last_reporter": "0.0.0.0",
                        },
                        "239.7.7.7": {
                            "group_mode": "include",
                            "up_time": "00:05:06",
                            "flags": "SS",
                            "source": {
                                "10.16.2.1": {
                                    "up_time": "00:05:06",
                                    "flags": "S",
                                    "forward": True,
                                    "csr_exp": "stopped",
                                    "v3_exp": "stopped",
                                }
                            },
                            "last_reporter": "0.0.0.0",
                        },
                        "239.9.9.9": {
                            "group_mode": "exclude",
                            "up_time": "00:23:15",
                            "flags": "Ac",
                            "expire": "00:06:06",
                            "last_reporter": "10.1.2.2",
                        },
                        "239.2.2.2": {
                            "group_mode": "include",
                            "up_time": "00:05:06",
                            "flags": "L U",
                            "last_reporter": "10.1.2.1",
                        },
                        "224.0.1.40": {
                            "group_mode": "include",
                            "up_time": "00:25:33",
                            "flags": "L U",
                            "last_reporter": "10.1.2.1",
                        },
                        "239.3.3.3": {
                            "group_mode": "include",
                            "up_time": "00:05:06",
                            "flags": "L",
                            "source": {
                                "10.4.1.1": {
                                    "up_time": "00:05:06",
                                    "flags": "L",
                                    "forward": True,
                                    "csr_exp": "stopped",
                                    "v3_exp": "stopped",
                                }
                            },
                            "last_reporter": "10.1.2.1",
                        },
                    },
                    "static_group": {
                        "239.6.6.6 *": {
                            "group": "239.6.6.6",
                            "source": "*",
                            "up_time": "00:05:06",
                            "flags": "SG",
                            "last_reporter": "0.0.0.0",
                        },
                        "239.5.5.5 *": {
                            "group": "239.5.5.5",
                            "source": "*",
                            "up_time": "00:05:06",
                            "flags": "SG",
                            "last_reporter": "0.0.0.0",
                        },
                    },
                    "join_group": {
                        "239.8.8.8 10.16.2.2": {
                            "group": "239.8.8.8",
                            "source": "10.16.2.2",
                            "up_time": "00:05:06",
                            "forward": True,
                            "csr_exp": "stopped",
                            "v3_exp": "stopped",
                            "flags": "SS",
                            "last_reporter": "0.0.0.0",
                        },
                        "239.8.8.8 10.16.2.1": {
                            "group": "239.8.8.8",
                            "source": "10.16.2.1",
                            "up_time": "00:05:06",
                            "forward": True,
                            "csr_exp": "stopped",
                            "v3_exp": "stopped",
                            "flags": "SS",
                            "last_reporter": "0.0.0.0",
                        },
                        "239.4.4.4 10.4.1.2": {
                            "group": "239.4.4.4",
                            "source": "10.4.1.2",
                            "up_time": "00:05:06",
                            "forward": True,
                            "csr_exp": "stopped",
                            "v3_exp": "stopped",
                            "flags": "L",
                            "last_reporter": "10.1.2.1",
                        },
                        "239.9.9.9 *": {
                            "group": "239.9.9.9",
                            "source": "*",
                            "expire": "00:06:06",
                            "up_time": "00:23:15",
                            "flags": "Ac",
                            "last_reporter": "10.1.2.2",
                        },
                        "224.0.1.40 *": {
                            "group": "224.0.1.40",
                            "source": "*",
                            "up_time": "00:25:33",
                            "flags": "L U",
                            "last_reporter": "10.1.2.1",
                        },
                        "239.7.7.7 10.16.2.1": {
                            "group": "239.7.7.7",
                            "source": "10.16.2.1",
                            "up_time": "00:05:06",
                            "forward": True,
                            "csr_exp": "stopped",
                            "v3_exp": "stopped",
                            "flags": "SS",
                            "last_reporter": "0.0.0.0",
                        },
                        "239.3.3.3 10.4.1.1": {
                            "group": "239.3.3.3",
                            "source": "10.4.1.1",
                            "up_time": "00:05:06",
                            "forward": True,
                            "csr_exp": "stopped",
                            "v3_exp": "stopped",
                            "flags": "L",
                            "last_reporter": "10.1.2.1",
                        },
                        "239.2.2.2 *": {
                            "group": "239.2.2.2",
                            "source": "*",
                            "up_time": "00:05:06",
                            "flags": "L U",
                            "last_reporter": "10.1.2.1",
                        },
                        "239.1.1.1 *": {
                            "group": "239.1.1.1",
                            "source": "*",
                            "up_time": "00:05:06",
                            "flags": "L U",
                            "last_reporter": "10.1.2.1",
                        },
                    },
                }
            }
        }
    }
}
