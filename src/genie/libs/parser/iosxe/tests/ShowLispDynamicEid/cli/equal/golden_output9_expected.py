expected_output = {
    "lisp_id": {
        0: {
            "instance_id": {
                4100: {
                    "eid_table": "red",
                    "dynamic_eids": {
                        "2001_192_168_1": {
                            "database_mapping": {
                                "eid_prefix": "A1:192:168:1::/64",
                                "locator_set": "RLOC",
                            },
                            "map_servers": [],
                            "num_of_dynamic_eid": 2,
                            "last_dyn_eid_discovered": "A1:192:168:1::1",
                        },
                        "test": {
                            "database_mapping": {
                                "eid_prefix": "A1:1:1:0::/48",
                                "locator_set": "RLOC",
                            },
                            "map_servers": ["1:1:1:1::", "2:2:2:2::"],
                            "num_of_dynamic_eid": 0,
                        },
                    },
                }
            }
        }
    }
}
