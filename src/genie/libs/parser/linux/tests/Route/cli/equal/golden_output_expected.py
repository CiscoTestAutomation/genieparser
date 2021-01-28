expected_output = {
    "routes": {
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
                            "metric": 600,
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
        "default": {
            "mask": {
                "0.0.0.0": {
                    "nexthop": {
                        1: {
                            "flags": "UG",
                            "gateway": "_gateway",
                            "interface": "wlo1",
                            "metric": 600,
                            "ref": 0,
                            "use": 0,
                        }
                    }
                }
            }
        },
    }
}
