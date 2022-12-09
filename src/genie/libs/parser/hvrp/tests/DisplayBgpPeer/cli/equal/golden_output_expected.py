
expected_output = {
    "local_router_id": "1.1.1.1",
    "local_as": "64666",
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "peer": {
                        "5.5.5.5": {
                            "remote_as": "64666",
                            "bgp_version": 4,
                            "total_messages": {
                                "received": 0,
                                "sent": 0
                            },
                            "out_queue": 0,
                            "up_down_time": "00:08:50",
                            "state": "Connect",
                            "prefixes_counters": {
                                "received": 0
                            }
                        },
                        "5.5.5.6": {
                            "remote_as": "64666",
                            "bgp_version": 4,
                            "total_messages": {
                                "received": 0,
                                "sent": 0
                            },
                            "out_queue": 0,
                            "up_down_time": "00:08:50",
                            "state": "Connect",
                            "prefixes_counters": {
                                "received": 0
                            }
                        },
                        "5.55.66.5": {
                            "remote_as": "65000",
                            "bgp_version": 4,
                            "total_messages": {
                                "received": 0,
                                "sent": 0
                            },
                            "out_queue": 0,
                            "up_down_time": "00:08:50",
                            "state": "Connect",
                            "prefixes_counters": {
                                "received": 0
                            }
                        },
                        "172.16.20.20": {
                            "remote_as": "65000",
                            "bgp_version": 4,
                            "total_messages": {
                                "received": 46,
                                "sent": 60
                            },
                            "out_queue": 0,
                            "up_down_time": "00:07:09",
                            "state": "Established",
                            "prefixes_counters": {
                                "received": 1
                            }
                        },
                        "192.168.2.1": {
                            "remote_as": "64666",
                            "bgp_version": 4,
                            "total_messages": {
                                "received": 56,
                                "sent": 103
                            },
                            "out_queue": 0,
                            "up_down_time": "00:06:53",
                            "state": "Established",
                            "prefixes_counters": {
                                "received": 1
                            }
                        },
                        "192.168.3.1": {
                            "remote_as": "64666",
                            "bgp_version": 4,
                            "total_messages": {
                                "received": 98,
                                "sent": 104
                            },
                            "out_queue": 0,
                            "up_down_time": "00:06:52",
                            "state": "Established",
                            "prefixes_counters": {
                                "received": 15
                            }
                        }
                    }
                }
            }
        }
    }
}