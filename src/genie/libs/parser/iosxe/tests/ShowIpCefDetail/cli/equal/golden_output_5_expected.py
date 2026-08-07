expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "22.1.0.0/16": {
                            "epoch": 0,
                            "flags": ['default route handler', 'subtree context', 'check lisp eligibility', 'default route'],
                            "lisp": {
                                "remote_eid": {
                                    "packet_count": 9,
                                    "byte_count": 900,
                                    "fwd_action": "encap"
                                },
                                "src_paths": {
                                    "112.1.0.2": {
                                        "outgoing_interface": "LISP0"
                                    },
                                    "123.1.0.2": {
                                        "outgoing_interface": "LISP0"
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
