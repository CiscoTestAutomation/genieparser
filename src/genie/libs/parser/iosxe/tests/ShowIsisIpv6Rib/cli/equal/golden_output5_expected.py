expected_output = {
    "tag": {
        "": {
            "rib_root": "local RIB",
            "flex_algo": {
                "None": {
                    "prefix": {
                        "FCCC:CCC1:AA33::/48": {
                            "prefix_attr": {
                                "x_flag": True,
                                "r_flag": True,
                                "n_flag": True
                            },
                            "local_router": True,
                            "via": {
                                "FE80::A8BB:CCFF:FE00:6500": {
                                    "type": {
                                        "L2": {
                                            "metric": 20,
                                            "tag": "0",
                                            "interface": "Ethernet0/0",
                                            "filtered_out": False,
                                            "repair_path": {
                                                "attributes": {
                                                    "DS": True,
                                                    "LC": True,
                                                    "NP": True,
                                                    "PP": False,
                                                    "SR": True
                                                },
                                                "nh_addr": "FE80::A8BB:CCFF:FE00:6902",
                                                "interface": "Ethernet2/0",
                                                "metric": 110,
                                                "lfa_type": "TI-LFA node-protecting",
                                                "srv6_fwid": 25165856,
                                                "nodes": {
                                                    "R7": {
                                                        "pq_node": "Q",
                                                        "sid": "FCCC:CCC1:AA66:E000::"
                                                    }
                                                },
                                                "repair_source": "R3",
                                                "metric_to_prefix": 130
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
    }
}
