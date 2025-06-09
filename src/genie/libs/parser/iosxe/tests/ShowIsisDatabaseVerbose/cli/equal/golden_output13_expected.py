expected_output = {
    "tag": {
        "1": {
            "level": {
                  2: {
                    "R1.00-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x000000EE",
                        "lsp_checksum": "0x5CB6",
                        "lsp_holdtime": "554",
                        "lsp_rcvd": "*",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "area_address": "49.1234",
                        "nlpid": "0xCC 0x8E",
                        "topology": {
                            "ipv4": {
                                "code": "0x0"
                            },
                            "ipv6": {
                                "code": "0x2"
                            }
                        },
                        "router_cap": "1.1.1.1",
                        "d_flag": False,
                        "s_flag": False,
                        "segment_routing": {
                            "i_flag": True,
                            "v_flag": False,
                            "srgb_base": 16000,
                            "srgb_range": 13001,
                            "srlb_base": 15000,
                            "srlb_range": 1000
                        },
                        "node_msd": 16,
                        "hostname": "R1",
                        "extended_is_neighbor": {
                            "R3.00": [
                                {
                                    "neighbor_id": "R3.00",
                                    "metric": 10,
                                    "admin_weight": 50,
                                    "asla": {
                                        "l_flag": False,
                                        "sa_length": 1,
                                        "uda_length": 0
                                    },
                                    "standard_application": {
                                        "FLEX-ALGO": {
                                            "bit_mask": "0x10",
                                            "appl_spec_te_metric": 50
                                        }
                                    }
                                }
                            ]
                        }
                    }
                }
            }
        }
    }
}
