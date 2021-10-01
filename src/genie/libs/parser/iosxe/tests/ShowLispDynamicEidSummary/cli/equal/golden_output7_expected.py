expected_output = {
    "lisp_id": {
        0: {
            "instance_id": {
                100: {},
                101: {
                    "dynamic_eids": {
                        "Auto-L2-group-101": {
                            "eids": {
                                "aabb.cc00.c901": {
                                    "interface": "N/A",
                                    "uptime": "1d22h",
                                    "last_packet": "never",
                                    "pending_ping_count": 0,
                                },
                                "aabb.cc80.ca00": {
                                    "interface": "N/A",
                                    "uptime": "1d22h",
                                    "last_packet": "never",
                                    "pending_ping_count": 0,
                                },
                            }
                        }
                    }
                },
                4100: {
                    "eid_table": "red",
                    "dynamic_eids": {
                        "192_168_1_0": {
                            "eids": {
                                "192.168.1.1": {
                                    "interface": "Vlan101",
                                    "uptime": "1d22h",
                                    "last_packet": "never",
                                    "pending_ping_count": 0,
                                },
                                "192.168.1.71": {
                                    "interface": "Vlan101",
                                    "uptime": "1d22h",
                                    "last_packet": "never",
                                    "pending_ping_count": 0,
                                },
                            }
                        },
                        "2001_192_168_1": {
                            "eids": {
                                "2001:192:168:1::1": {
                                    "interface": "Vlan101",
                                    "uptime": "1d22h",
                                    "last_packet": "never",
                                    "pending_ping_count": 0,
                                },
                                "2001:192:168:1::71": {
                                    "interface": "Vlan101",
                                    "uptime": "1d22h",
                                    "last_packet": "never",
                                    "pending_ping_count": 0,
                                },
                            }
                        },
                    },
                },
                4101: {"eid_table": "blue"},
            }
        }
    }
}
