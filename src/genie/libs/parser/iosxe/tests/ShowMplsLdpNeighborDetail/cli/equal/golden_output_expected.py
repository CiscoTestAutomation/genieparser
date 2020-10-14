expected_output = {
    "vrf": {
        "default": {
            "peers": {
                "10.169.197.252": {
                    "label_space_id": {
                        0: {
                            "local_ldp_ident": "10.169.197.254:0",
                            "tcp_connection": "10.169.197.252.646 - 10.169.197.254.44315",
                            "password": "not required, none, in use",
                            "state": "oper",
                            "msg_sent": 9981,
                            "msg_rcvd": 10004,
                            "downstream": True,
                            "last_tib_rev_sent": 4103,
                            "uptime": "3d21h",
                            "ldp_discovery_sources": {
                                "interface": {
                                    "GigabitEthernet0/0/0": {
                                        "ip_address": {
                                            "10.169.197.93": {
                                                "holdtime_ms": 15000,
                                                "hello_interval_ms": 5000,
                                            }
                                        }
                                    }
                                }
                            },
                            "address_bound": [
                                "10.169.197.252",
                                "192.168.36.49",
                                "10.120.202.49",
                                "192.168.36.57",
                                "10.169.197.101",
                                "10.169.197.93",
                                "10.69.111.2",
                                "10.16.190.254",
                            ],
                            "peer_holdtime_ms": 180000,
                            "ka_interval_ms": 60000,
                            "peer_state": "estab",
                            "nsr": "Not Ready",
                            "capabilities": {
                                "sent": {
                                    "ICCP": {
                                        "type": "0x0405",
                                        "maj_ver": 1,
                                        "min_ver": 0,
                                    },
                                    "dynamic_anouncement": "0x0506",
                                    "mldp_point_to_multipoint": "0x0508",
                                    "mldp_multipoint_to_multipoint": "0x0509",
                                    "typed_wildcard": "0x050B",
                                },
                                "received": {
                                    "ICCP": {
                                        "type": "0x0405",
                                        "maj_ver": 1,
                                        "min_ver": 0,
                                    },
                                    "dynamic_anouncement": "0x0506",
                                    "mldp_point_to_multipoint": "0x0508",
                                    "mldp_multipoint_to_multipoint": "0x0509",
                                    "typed_wildcard": "0x050B",
                                },
                            },
                        }
                    }
                },
                "10.169.197.253": {
                    "label_space_id": {
                        0: {
                            "local_ldp_ident": "10.169.197.254:0",
                            "tcp_connection": "10.169.197.253.646 - 10.169.197.254.34904",
                            "password": "not required, none, in use",
                            "state": "oper",
                            "msg_sent": 9966,
                            "msg_rcvd": 9153,
                            "downstream": True,
                            "last_tib_rev_sent": 4103,
                            "uptime": "3d21h",
                            "ldp_discovery_sources": {
                                "interface": {
                                    "GigabitEthernet0/0/2": {
                                        "ip_address": {
                                            "10.169.197.97": {
                                                "holdtime_ms": 15000,
                                                "hello_interval_ms": 5000,
                                            }
                                        }
                                    }
                                }
                            },
                            "address_bound": ["10.120.202.57", "10.169.197.97"],
                            "peer_holdtime_ms": 180000,
                            "ka_interval_ms": 60000,
                            "peer_state": "estab",
                            "nsr": "Not Ready",
                            "capabilities": {
                                "sent": {
                                    "ICCP": {
                                        "type": "0x0405",
                                        "maj_ver": 1,
                                        "min_ver": 0,
                                    },
                                    "dynamic_anouncement": "0x0506",
                                    "mldp_point_to_multipoint": "0x0508",
                                    "mldp_multipoint_to_multipoint": "0x0509",
                                    "typed_wildcard": "0x050B",
                                }
                            },
                        }
                    }
                },
            }
        }
    }
}
