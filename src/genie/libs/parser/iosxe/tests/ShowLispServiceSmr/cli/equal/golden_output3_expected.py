expected_output = {
    "lisp_router_instances": {
        0: {
            "lisp_router_instance_id": 0,
            "service": {
                "ipv6": {
                    "instance_id": {
                        "101": {
                            "smr": {
                                "entries": 1,
                                "prefixes": {
                                    "A1:192:168::/64": {"producer": "local EID"}
                                },
                                "vrf": "red"
                            }
                        }
                    }
                }
            }
        }
    }
}
