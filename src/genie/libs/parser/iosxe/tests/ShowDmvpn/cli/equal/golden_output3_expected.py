expected_output = {
    "interfaces": {
        "Tunnel1": {
            "type": "Hub",
            "nhrp_peers": 2,
            "ent": {
                1: {
                    "peers": {
                        "2001:DB8:1201::122": {
                            "tunnel_addr": {
                                "192.2.1.122": {
                                    "attrb": {
                                        "D": {
                                            "time": "00:02:19",
                                            "state": "UP"
                                        }
                                    }
                                }
                            }
                        },
                        "2001:DB8:1202::123": {
                            "tunnel_addr": {
                                "192.3.1.123": {
                                    "attrb": {
                                        "D": {
                                            "time": "00:02:08",
                                            "state": "UP"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}