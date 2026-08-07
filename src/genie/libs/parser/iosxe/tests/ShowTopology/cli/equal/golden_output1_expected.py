expected_output = {
    "topologies": {
        "base": {
            "address_families": {
                "ipv4": {
                    "vrfs": {
                        "default": {
                            "state": "UP"
                        },
                        "__Platform_iVRF:_ID00_": {
                            "state": "UP"
                        }
                    }
                },
                "ipv6": {
                    "vrfs": {
                        "default": {
                            "state": "UP"
                        },
                        "foo": {
                            "state": "UP"
                        }
                    }
                },
                "ipv4 multicast": {
                    "vrfs": {
                        "default": {
                            "state": "DOWN"
                        }
                    }
                },
                "ipv6 multicast": {
                    "vrfs": {
                        "default": {
                            "state": "DOWN"
                        },
                        "foo": {
                            "state": "DOWN"
                        }
                    }
                }
            }
        },
        "t1": {
            "address_families": {
                "ipv4": {
                    "vrfs": {
                        "default": {
                            "state": "UP"
                        }
                    }
                }
            }
        }
    }
}
