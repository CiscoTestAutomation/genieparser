expected_output = {
    "tag": {
        "1": {
            "topo_type": "unicast",
            "topo_name": "base",
            "tid": 0,
            "topo_id": "0x0",
            "flex_algo": {
                128: {
                    "prefix": {
                        "2.2.2.2": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "subnet": "32",
                            "source_router_id": "2.2.2.2",
                            "algo": {
                                0: {
                                    "sid_index": 202,
                                    "bound": True
                                },
                                1: {}
                            },
                            "via_interface": {
                                "GigabitEthernet0/3/0.1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "2.2.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 10,
                                                    "via_ip": "12.12.1.2",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "host": "asr1k-23.00-00",
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 202,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "implicit-null"
                                                        },
                                                        1: {}
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
    }
}
