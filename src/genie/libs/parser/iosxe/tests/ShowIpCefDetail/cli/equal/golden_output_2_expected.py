expected_output = {
    "vrf": {
        "red": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "0.0.0.0/0": {
                            "epoch": 0,
                            "flags": ['cover dependents', 'subtree context', 'check lisp eligibility', 'default route'],
                            "lisp": {
                                "remote_eid": {
                                    "packet_count": 1,
                                    "byte_count": 100,
                                    "fwd_action": "signal-fwd"
                                },
                                "src_paths": {
                                    "100.88.88.88": {
                                        "outgoing_interface": "LISP0.4100"
                                    },
                                    "100.99.99.99": {
                                        "outgoing_interface": "LISP0.4100"
                                    }
                                }
                            },
                            "nexthop": {
                                "100.88.88.88": {
                                    "outgoing_interface": {
                                        "LISP0.4100": {}
                                    }
                                },
                                "100.99.99.99": {
                                    "outgoing_interface": {
                                        "LISP0.4100": {}
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
