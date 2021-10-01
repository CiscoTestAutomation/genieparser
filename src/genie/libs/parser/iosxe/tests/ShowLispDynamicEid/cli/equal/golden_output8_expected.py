expected_output = {
    "lisp_id": {
        0: {
            "instance_id": {
                100: {
                    "dynamic_eids": {
                        "Auto-L2-group-100": {
                            "database_mapping": {
                                "eid_prefix": "any-mac",
                                "locator_set": "RLOC",
                            },
                            "map_servers": [],
                            "num_of_dynamic_eid": 0,
                        }
                    }
                },
                101: {
                    "dynamic_eids": {
                        "Auto-L2-group-101": {
                            "database_mapping": {
                                "eid_prefix": "any-mac",
                                "locator_set": "RLOC",
                            },
                            "map_servers": [],
                            "num_of_dynamic_eid": 2,
                            "last_dyn_eid_discovered": "aabb.cc80.ca00",
                        }
                    }
                },
                4100: {
                    "eid_table": "red",
                    "dynamic_eids": {
                        "192_168_1_0": {
                            "database_mapping": {
                                "eid_prefix": "192.168.1.0/24",
                                "locator_set": "RLOC",
                            },
                            "map_servers": [],
                            "num_of_dynamic_eid": 2,
                            "last_dyn_eid_discovered": "192.168.1.1",
                        },
                        "2001_192_168_1": {
                            "database_mapping": {
                                "eid_prefix": "2001:192:168:1::/64",
                                "locator_set": "RLOC",
                            },
                            "map_servers": [],
                            "num_of_dynamic_eid": 2,
                            "last_dyn_eid_discovered": "2001:192:168:1::1",
                        },
                    },
                },
                4101: {
                    "eid_table": "blue",
                    "dynamic_eids": {
                        "193_168_1_0": {
                            "database_mapping": {
                                "eid_prefix": "193.168.1.0/24",
                                "locator_set": "RLOC",
                            },
                            "map_servers": [],
                            "num_of_dynamic_eid": 0,
                        },
                        "2001_193_168_1": {
                            "database_mapping": {
                                "eid_prefix": "2001:193:168:1::/64",
                                "locator_set": "RLOC",
                            },
                            "map_servers": [],
                            "num_of_dynamic_eid": 0,
                        },
                    },
                },
            }
        }
    }
}
