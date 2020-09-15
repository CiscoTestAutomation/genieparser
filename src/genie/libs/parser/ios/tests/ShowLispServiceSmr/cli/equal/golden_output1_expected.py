expected_output = {
    "lisp_router_instances": {
        0: {
            "lisp_router_instance_id": 0,
            "service": {
                "ipv4": {
                    "instance_id": {
                        "101": {
                            "smr": {
                                "entries": 1,
                                "prefixes": {
                                    "192.168.0.0/24": {"producer": "local EID"}
                                },
                                "vrf": "red",
                            }
                        }
                    }
                }
            },
        }
    }
}
