expected_output = {
    "local_router_id": "3.3.3.3",
    "local_as": "64666",
    "vrf": {
        "default": {
            "address_family": {
                "ipv4 unicast": {
                    "peer": {
                        "10.10.10:10": {
                            "remote_as": "65000",
                            "total_messages": {
                                "received": 0,
                                "sent": 0
                            },
                            "out_queue": 0,
                            "up_down_time": "1272h18m",
                            "state": "Connect",
                            "prefixes_counters": {
                                "received": 0,
                                "advertised": 0
                            }
                        },
                        "20.20.20.20": {
                            "remote_as": "65000",
                            "total_messages": {
                                "received": 232782,
                                "sent": 279631
                            },
                            "out_queue": 0,
                            "up_down_time": "0646h36m",
                            "state": "Established",
                            "prefixes_counters": {
                                "received": 1,
                                "advertised": 7
                            }
                        },
                        "30.30.30.30": {
                            "remote_as": "64666",
                            "total_messages": {
                                "received": 6677,
                                "sent": 6724
                            },
                            "out_queue": 0,
                            "up_down_time": "15:23:48",
                            "state": "Established",
                            "prefixes_counters": {
                                "received": 1,
                                "advertised": 41
                            }
                        },
                        "40.40.40.40": {
                            "remote_as": "64666",
                            "total_messages": {
                                "received": 6583,
                                "sent": 6562
                            },
                            "out_queue": 0,
                            "up_down_time": "15:05:29",
                            "state": "Established",
                            "prefixes_counters": {
                                "received": 15,
                                "advertised": 41
                            }
                        }
                    }
                },
                "vpnv4 all": {
                    "peer": {
                        "50.50.50.50": {
                            "remote_as": "65000",
                            "total_messages": {
                                "received": 0,
                                "sent": 0
                            },
                            "out_queue": 0,
                            "up_down_time": "16:22:55",
                            "state": "Idle(Admin)",
                            "prefixes_counters": {
                                "received": 0,
                                "advertised": 0
                            }
                        },
                        "60.60.60.60": {
                            "remote_as": "65000",
                            "total_messages": {
                                "received": 245080,
                                "sent": 279587
                            },
                            "out_queue": 0,
                            "up_down_time": "0646h36m",
                            "state": "Established",
                            "prefixes_counters": {
                                "received": 40,
                                "advertised": 16
                            }
                        },
                        "70.70.70.70": {
                            "remote_as": "65000",
                            "total_messages": {
                                "received": 245082,
                                "sent": 279595
                            },
                            "out_queue": 0,
                            "up_down_time": "0646h36m",
                            "state": "Established",
                            "prefixes_counters": {
                                "received": 40,
                                "advertised": 16
                            }
                        }
                    }
                }
            }
        },
        "mobile": {
            "address_family": {
                "ipv4 unicast": {
                    "peer": {
                        "192.168.1.1": {
                            "remote_as": "64535",
                            "total_messages": {
                                "received": 0,
                                "sent": 0
                            },
                            "out_queue": 0,
                            "up_down_time": "1272h18m",
                            "state": "Idle",
                            "prefixes_counters": {
                                "received": 0,
                                "advertised": 0
                            }
                        },
                        "192.168.2.1": {
                            "remote_as": "64535",
                            "total_messages": {
                                "received": 55487,
                                "sent": 57371
                            },
                            "out_queue": 0,
                            "up_down_time": "0832h15m",
                            "state": "Established",
                            "prefixes_counters": {
                                "received": 5,
                                "advertised": 1
                            }
                        },
                        "192.168.3.1": {
                            "remote_as": "64535",
                            "total_messages": {
                                "received": 0,
                                "sent": 0
                            },
                            "out_queue": 0,
                            "up_down_time": "0138h25m",
                            "state": "Idle",
                            "prefixes_counters": {
                                "received": 0,
                                "advertised": 0
                            }
                        },
                        "192.168.4.1": {
                            "remote_as": "64535",
                            "total_messages": {
                                "received": 17621,
                                "sent": 17659
                            },
                            "out_queue": 0,
                            "up_down_time": "0256h06m",
                            "state": "Established",
                            "prefixes_counters": {
                                "received": 12,
                                "advertised": 1
                            }
                        }
                    }
                },
                "vpnv6 all": {
                    "peer": {
                        "50.50.50.50": {
                            "remote_as": "65000",
                            "total_messages": {
                                "received": 0,
                                "sent": 0
                            },
                            "out_queue": 0,
                            "up_down_time": "16:22:55",
                            "state": "Idle(Admin)",
                            "prefixes_counters": {
                                "received": 0,
                                "advertised": 0
                            }
                        }
                    }
                }
            }
        }
    }
}
