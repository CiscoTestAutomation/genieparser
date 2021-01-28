expected_output = {
    "routes": {
        "0.0.0.0": {
            "mask": {
                "0.0.0.0": {
                    "nexthop": {
                        1: {
                            "gateway": "192.168.1.1",
                            "interface": "enp7s0",
                            "metric": 100,
                        }
                    }
                }
            }
        },
        "169.254.0.0": {
            "mask": {
                "255.255.0.0": {
                    "nexthop": {
                        1: {"interface": "enp7s0", "scope": "link", "metric": 1000}
                    }
                }
            }
        },
        "172.17.0.0": {
            "mask": {
                "255.255.0.0": {
                    "nexthop": {
                        1: {
                            "interface": "docker0",
                            "scope": "link",
                            "proto": "kernel",
                            "src": "172.17.0.1",
                        }
                    }
                }
            }
        },
        "172.18.0.0": {
            "mask": {
                "255.255.0.0": {
                    "nexthop": {
                        1: {
                            "interface": "br-d19b23fac393",
                            "scope": "link",
                            "proto": "kernel",
                            "src": "172.18.0.1",
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
                            "interface": "enp7s0",
                            "scope": "link",
                            "proto": "kernel",
                            "src": "192.168.1.212",
                        }
                    }
                }
            }
        },
        "127.0.0.0": {
            "mask": {
                "255.255.255.255": {
                    "nexthop": {
                        1: {
                            "interface": "lo",
                            "scope": "link",
                            "proto": "kernel",
                            "src": "127.0.0.1",
                            "broadcast": True,
                            "table": "local",
                        }
                    }
                }
            }
        },
        "10.233.44.70": {
            "mask": {
                "255.255.255.255": {
                    "nexthop": {
                        1: {
                            "interface": "kube-ipvs0",
                            "scope": "host",
                            "proto": "kernel",
                            "src": "10.233.44.70",
                            "local": True,
                            "table": "local",
                        }
                    }
                }
            }
        },
        "192.168.1.255": {
            "mask": {
                "255.255.255.255": {
                    "nexthop": {
                        1: {
                            "interface": "enp7s0",
                            "scope": "link",
                            "proto": "kernel",
                            "src": "192.168.1.212",
                            "broadcast": True,
                            "table": "local",
                        }
                    }
                }
            }
        },
    }
}
