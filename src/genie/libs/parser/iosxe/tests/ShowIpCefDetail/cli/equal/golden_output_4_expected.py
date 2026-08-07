expected_output = {
    "vrf": {
        "blue": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "0.0.0.0/0": {
                            "epoch": 0,
                            "flags": ['default route handler', 'cover dependents', 'subtree context', 'check lisp eligibility', 'default route'],
                            "lisp": {
                                "remote_eid": {
                                    "packet_count": 0,
                                    "byte_count": 0,
                                    "fwd_action": "signal-fwd"
                                },
                                "src_paths": {
                                    "10.255.1.31": {
                                        "outgoing_interface": "LISP0.101"
                                    }
                                }
                            },
                            "nexthop": {
                                "no route": {}
                            }
                        }
                    }
                }
            }
        }
    }
}
