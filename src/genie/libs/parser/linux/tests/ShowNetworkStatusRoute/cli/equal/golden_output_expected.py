expected_output = {
    "routes": {
        "0.0.0.0": {
            "mask": {
                "0.0.0.0": {
                    "nexthop": {
                        1: {
                            "flags": "UG",
                            "gateway": "192.168.1.1",
                            "interface": "wlo1",
                            "metric": 0,
                            "ref": 0,
                            "use": 0,
                        }
                    }
                }
            }
        },
        "10.10.0.0": {
            "mask": {
                "255.255.255.0": {
                    "nexthop": {
                        1: {
                            "flags": "U",
                            "gateway": "0.0.0.0",
                            "interface": "eth1-05",
                            "metric": 0,
                            "ref": 0,
                            "use": 0,
                        }
                    }
                }
            }
        },
        "172.17.0.0": {
            "mask": {
                "255.255.0.0": {
                    "nexthop": {
                        1: {
                            "flags": "U",
                            "gateway": "0.0.0.0",
                            "interface": "docker0",
                            "metric": 0,
                            "ref": 0,
                            "use": 0,
                        }
                    }
                }
            }
        },
        "192.168.1.0": {
            "mask": {
                "255.255.255.0": {
                    "nexthop": {
                        1: {
                            "flags": "U",
                            "gateway": "0.0.0.0",
                            "interface": "wlo1",
                            "metric": 0,
                            "ref": 0,
                            "use": 0,
                        }
                    }
                }
            }
        },
        "192.168.122.0": {
            "mask": {
                "255.255.255.0": {
                    "nexthop": {
                        1: {
                            "flags": "U",
                            "gateway": "0.0.0.0",
                            "interface": "virbr0",
                            "metric": 0,
                            "ref": 0,
                            "use": 0,
                        }
                    }
                }
            }
        },
    }
}
