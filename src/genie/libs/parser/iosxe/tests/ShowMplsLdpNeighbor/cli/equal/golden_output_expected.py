expected_output = {
    "vrf": {
        "default": {
            "peers": {
                "10.169.197.252": {
                    "label_space_id": {
                        0: {
                            "address_bound": [
                                "10.169.197.252",
                                "10.120.202.49",
                                "10.169.197.101",
                                "10.16.190.254",
                                "10.169.197.93",
                            ],
                            "downstream": True,
                            "ldp_discovery_sources": {
                                "interface": {
                                    "GigabitEthernet0/0/0": {
                                        "ip_address": {"10.169.197.93": {}}
                                    }
                                }
                            },
                            "local_ldp_ident": "10.169.197.254:0",
                            "msg_rcvd": 852,
                            "msg_sent": 851,
                            "state": "oper",
                            "tcp_connection": "10.169.197.252.646 - 10.169.197.254.20170",
                            "uptime": "04:50:30",
                        }
                    }
                },
                "10.169.197.253": {
                    "label_space_id": {
                        0: {
                            "address_bound": [
                                "10.186.1.2",
                                "10.120.202.57",
                                "10.169.197.97",
                            ],
                            "downstream": True,
                            "ldp_discovery_sources": {
                                "interface": {
                                    "GigabitEthernet0/0/2": {
                                        "ip_address": {"10.169.197.97": {}}
                                    }
                                }
                            },
                            "local_ldp_ident": "10.169.197.254:0",
                            "msg_rcvd": 306,
                            "msg_sent": 858,
                            "state": "oper",
                            "tcp_connection": "10.169.197.253.646 - 10.169.197.254.42450",
                            "uptime": "04:50:30",
                        }
                    }
                },
            }
        }
    }
}
