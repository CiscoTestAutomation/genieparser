expected_output = {
    "tag": {
        "1": {
            "level": {
                2: {
                    "R1.00-00": {
                        "area_address": "49.1234",
                        "attach_bit": 0,
                        "d_flag": False,
                        "extended_is_neighbor": {
                            "R3.00": [
                                {
                                    "neighbor_id": "R3.00",
                                    "metric": 10,
                                    "admin_weight": 50,
                                    "asla": {
                                        "l_flag": False,
                                        "sa_length": 1,
                                        "uda_length": 0,
                                    },
                                    "standard_application": {
                                        "FLEX-ALGO": {
                                            "bit_mask": "0x10",
                                            "appl_spec_te_metric": 50,
                                        }
                                    },
                                }
                            ],
                        },
                        "hostname": "R1",
                        "local_router": True,
                        "lsp_checksum": "0x5CB6",
                        "lsp_holdtime": "554",
                        "lsp_rcvd": "*",
                        "lsp_sequence_num": "0x000000EE",
                        "nlpid": "0xCC 0x8E",
                        "node_msd": 16,
                        "overload_bit": 0,
                        "p_bit": 0,
                        "router_cap": "1.1.1.1",
                        "s_flag": False,
                        "segment_routing": {
                            "algorithms": [128],
                            "i_flag": True,
                            "spf": True,
                            "srgb_base": 16000,
                            "srgb_range": 13001,
                            "srlb_base": 15000,
                            "srlb_range": 1000,
                            "strict_spf": True,
                            "v_flag": False,
                        },
                        "topology": {
                            "ipv4": {
                                "code": "0x0",
                            },
                            "ipv6": {
                                "code": "0x2",
                            },
                        },
                    },
                },
            },
        },
    },
}
