expected_output = {
    "lisp_router_instances": {
        0: {
            "lisp_router_instance_id": 0,
            "service": {
                "ipv4": {
                    "instance_id": {
                        "101": {
                            "rloc": {
                                "distribution": False,
                                "total_entries": 2,
                                "valid_entries": 2,
                                "members": {
                                    "10.16.2.2": {
                                        "origin": "registration",
                                        "valid": "yes",
                                    },
                                    "10.1.8.8": {
                                        "origin": "registration",
                                        "valid": "yes",
                                    },
                                },
                            }
                        }
                    }
                }
            },
        }
    }
}
