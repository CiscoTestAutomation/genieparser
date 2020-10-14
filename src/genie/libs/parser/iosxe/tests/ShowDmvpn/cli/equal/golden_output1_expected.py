expected_output = {
    "interfaces": {
        "Tunnel84": {
            "ent": {
                1: {
                    "peers": {
                        "172.30.84.1": {
                            "tunnel_addr": {
                                "172.29.0.1": {
                                    "attrb": {"SC": {"state": "NHRP", "time": "never"}}
                                }
                            }
                        }
                    }
                }
            },
            "nhrp_peers": 1,
            "type": "Spoke",
        },
        "Tunnel90": {
            "ent": {
                1: {
                    "peers": {
                        "172.29.0.1": {
                            "tunnel_addr": {
                                "172.30.90.1": {
                                    "attrb": {"S": {"state": "IKE", "time": "3w5d"}}
                                }
                            }
                        }
                    }
                },
                2: {
                    "peers": {
                        "172.29.0.2": {
                            "tunnel_addr": {
                                "172.30.90.2": {
                                    "attrb": {"S": {"state": "UP", "time": "6d12h"}}
                                },
                                "172.30.90.25": {
                                    "attrb": {"S": {"state": "UP", "time": "6d12h"}}
                                },
                            }
                        },
                        "172.29.134.1": {
                            "tunnel_addr": {
                                "172.30.72.72": {
                                    "attrb": {
                                        "DT1": {"state": "UP", "time": "00:29:40"},
                                        "DT2": {"state": "UP", "time": "00:29:40"},
                                    }
                                }
                            }
                        },
                    }
                },
            },
            "nhrp_peers": 3,
            "type": "Spoke",
        },
    }
}
