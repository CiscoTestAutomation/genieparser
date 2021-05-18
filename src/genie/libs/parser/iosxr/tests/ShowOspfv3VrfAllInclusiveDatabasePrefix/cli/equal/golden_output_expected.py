expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "instance": {
                        "mpls1": {
                            "areas": {
                                "0.0.0.0": {
                                    "database": {
                                        "lsa_types": {
                                            "9": {
                                                "lsa_type": 9,
                                                "lsas": {
                                                    "0 25.97.1.1": {
                                                        "adv_router": "25.97.1.1",
                                                        "lsa_id": "0",
                                                        "ospfv3": {
                                                            "body": {
                                                                "number_of_prefix": 3,
                                                                "prefixes": {
                                                                    "1": {
                                                                        "metric": 65535,
                                                                        "options": "None",
                                                                        "prefix_address": "2001:1100::1001",
                                                                        "prefix_length": 128,
                                                                        "priority": "Medium"
                                                                    },
                                                                    "2": {
                                                                        "metric": 65535,
                                                                        "options": "None",
                                                                        "prefix_address": "2001:100:20::",
                                                                        "prefix_length": 64,
                                                                        "priority": "Low"
                                                                    },
                                                                    "3": {
                                                                        "metric": 65535,
                                                                        "options": "None",
                                                                        "prefix_address": "2001:100:10::",
                                                                        "prefix_length": 64,
                                                                        "priority": "Low"
                                                                    }
                                                                 
                                                            },
                                                            "header": {
                                                                "adv_router": "25.97.1.1",
                                                                "age": 852,
                                                                "checksum": "0x66cb",
                                                                "length": 76,
                                                                "lsa_id": "0",
                                                                "ref_adv_router": "25.97.1.1",
                                                                "ref_lsa_id": "0",
                                                                "ref_lsa_type": "2001",
                                                                "routing_bit_enable": True,
                                                                "seq_num": "80000002",
                                                                "type": "Intra-Area-Prefix-LSA"
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
    }
}}
