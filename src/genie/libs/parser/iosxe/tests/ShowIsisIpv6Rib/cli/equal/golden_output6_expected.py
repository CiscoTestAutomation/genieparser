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
                                                    "R6": {
                                                        "pq_node": "P",
                                                        "sid": "FCCC:CCC1:F1::",
                                                        "srv6_sid_behavior": "uN (PSP/USD)"
                                                    },
                                                    "r604": {
                                                        "pq_node": "Q",
                                                        "sid": "CAFE:0:603:E001::",
                                                        "srv6_sid_behavior": "uA (PSP/USD)"
                                                    },
                                                    "R7": {
                                                        "pq_node": "Q",
                                                        "sid": "CAFE:0:603:E011::",
                                                        "srv6_sid_behavior": "reserved behavior: 0"
                                                    }
                                                },
                                                "repair_source": "R3",
                                                "metric_to_prefix": 130
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "666::666/128": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "local_router": True,
                            "source_router_id": "666::666",
                            "via_uloop": {
                                "srv6_fwid": {
                                    "25165865": {
                                        "type": "L1",
                                        "metric": 65,
                                        "tag": "0",
                                        "nodes": {
                                            "R4": {
                                                "pq_node": "P",
                                                "sid": "FCCC:CCC1:D1::",
                                                "srv6_sid_behavior": "uN (PSP/USD)"
                                            }
                                        },
                                        "installed": True,
                                        "alt": True
                                    }
                                }
                            },
                            "via": {
                                "FE80::A8BB:CCFF:FE00:9C10": {
                                    "type": {
                                        "L1": {
                                            "metric": 65,
                                            "tag": "0",
                                            "interface": "Ethernet0/1",
                                            "filtered_out": False
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

