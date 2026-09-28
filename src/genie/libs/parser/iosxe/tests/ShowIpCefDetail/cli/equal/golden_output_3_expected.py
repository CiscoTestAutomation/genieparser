expected_output = {
    "vrf": {
        "red": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "128.0.0.0/2": {
                            "epoch": 0,
                            "flags": ['subtree context', 'check lisp eligibility'],
                            "lisp": {
                                "remote_eid": {
                                    "packet_count": 0,
                                    "byte_count": 0,
                                    "fwd_action": "encap"
                                },
                                "src_paths": {
                                    "100.88.88.88": {
                                        "outgoing_interface": "LISP0.4100"
                                    }
                                }
                            },
                            "nexthop": {
                                "100.88.88.88": {
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
