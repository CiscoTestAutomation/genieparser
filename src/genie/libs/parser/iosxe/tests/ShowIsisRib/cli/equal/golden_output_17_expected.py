expected_output = {
    "tag": {
        "1": {
            "topo_type": "unicast",
            "topo_name": "base",
            "tid": 0,
            "topo_id": "0x0",
            "flex_algo": {
                "None": {
                    "prefix": {
                        "4.4.4.4": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "subnet": "32",
                            "source_router_id": "4.4.4.4",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "GigabitEthernet0/0/8": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "4.4.4.4": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 4,
                                                        "rtp_lsp_index": 7,
                                                        "rtp_lsp_version": 2651,
                                                        "tpl_lsp_version": 2651
                                                    },
                                                    "distance": 115,
                                                    "metric": 35,
                                                    "via_ip": "23.23.23.1",
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
                                                            "sid_index": 604,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "100604"
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