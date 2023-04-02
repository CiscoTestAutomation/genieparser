expected_output = {
    "tag": {
        "1": {
            "topology_id": "0x0",
            "type": "SRTE",
            "enabled": True,
            "router_id": "1.1.1.1",
            "interface": {
                "GigabitEthernet0/0/7": {
                    "hdl": "0xF",
                    "affinity": {
                        "set": 0,
                        "affinity_bits": 0
                    },
                    "te_metrics": {
                        "set": 0,
                        "te_metric": 4294967295
                    },
                    "extended_affinity": {
                        "set": 0,
                        "length": 0
                    }
                }
            },
            "te_attr_pm_info": {
                "Gi0/0/7": {
                    "idb_num": 15,
                    "min": 30,
                    "max": 30,
                    "avg": 30,
                    "var": 0
                },
                "Gi0/3/0": {
                    "idb_num": 16,
                    "min": 30,
                    "max": 30,
                    "avg": 30,
                    "var": 0
                }
            }
        },
        "2": {
            "topology_id": "0x2",
            "type": "SRTE",
            "enabled": False,
            "router_id": "2.2.2.2",
            "interface": {
                "Tunnel65537": {
                    "hdl": "0xF",
                    "affinity": {
                        "set": 0,
                        "affinity_bits": 0
                    },
                    "te_metrics": {
                        "set": 0,
                        "te_metric": 4294967295
                    },
                    "extended_affinity": {
                        "set": 0,
                        "length": 0
                    }
                }
            },
            "te_attr_pm_info": {
                "Tunnel65537": {
                    "idb_num": 15,
                    "min": 30,
                    "max": 30,
                    "avg": 30,
                    "var": 0
                }
            }
        }
    }
}
