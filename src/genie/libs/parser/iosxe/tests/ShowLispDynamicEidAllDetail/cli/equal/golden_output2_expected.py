expected_output = {
    "lisp_id": {
        0: {
            "instance_id": {
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
                            "eid_entries": {
                                "192.168.1.1": {
                                    "interface": "Vlan101",
                                    "uptime": "02:47:09",
                                    "last_activity": "never",
                                    "discovered_by": "Device-tracking",
                                },
                                "192.168.1.71": {
                                    "interface": "Vlan101",
                                    "uptime": "02:47:24",
                                    "last_activity": "never",
                                    "discovered_by": "Device-trackin",
                                },
                            },
                        },
                        "2001_192_168_1": {
                            "database_mapping": {
                                "eid_prefix": "2001:192:168:1::/64",
                                "locator_set": "RLOC",
                            },
                            "map_servers": [],
                            "num_of_dynamic_eid": 2,
                            "last_dyn_eid_discovered": "2001:192:168:1::1",
                            "eid_entries": {
                                "2001:192:168:1::1": {
                                    "interface": "Vlan101",
                                    "uptime": "02:47:06",
                                    "last_activity": "never",
                                    "discovered_by": "Device-tracking",
                                },
                                "2001:192:168:1::71": {
                                    "interface": "Vlan101",
                                    "uptime": "02:47:19",
                                    "last_activity": "never",
                                    "discovered_by": "Device-trackin",
                                },
                            },
                        },
                    },
                }
            }
        }
    }
}
