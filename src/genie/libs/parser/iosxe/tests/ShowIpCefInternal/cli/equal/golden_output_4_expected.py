expected_output = {
    "vrf": {
        "MG501": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "192.168.1.0/24": {
                            "epoch": 1,
                            "feature_space": {
                                "broker": {"distribution_priority": 3},
                                "iprm": "0x00018000",
                                "lfd": {"192.168.1.0/24": {"local_labels": 0}},
                            },
                            "flags": ["rlbls"],
                            "output_chain": {
                                "label": ["362", "implicit-null"],
                                "tag_midchain": {
                                    "Tunnel65536": {
                                        "label": [
                                            "16063",
                                            "16051",
                                            "16052",
                                            "16051",
                                            "16052",
                                            "16051",
                                            "16052",
                                            "16051",
                                            "16052",
                                            "16051",
                                            "16052",
                                            "16051",
                                        ],
                                        "tag_midchain_info": "7F9C9D301840",
                                    }
                                },
                                "tag_adj": {
                                    "GigabitEthernet0/1/7": {
                                        "addr": "10.19.198.29",
                                        "addr_info": "7F9C9D304A90",
                                    }
                                },
                            },
                            "path_list": {
                                "7F9C9E8D7A30": {
                                    "flags": "0x249 [shble, rif, hwcn, bgp]",
                                    "locks": 3,
                                    "path": {
                                        "7F9C9E900AC8": {
                                            "flags": "[must-be-lbld]",
                                            "for": "IPv4",
                                            "share": "1/1",
                                            "type": "recursive",
                                        }
                                    },
                                    "sharing": "per-destination",
                                },
                                "7F9C9E8D7C10": {
                                    "flags": "0x249 [shble, rif, hwcn, bgp]",
                                    "locks": 3,
                                    "path": {
                                        "7F9C9E9009F8": {
                                            "for": "Binding-Sid Label",
                                            "share": "1/1",
                                            "type": "attached prefix",
                                        }
                                    },
                                    "sharing": "per-destination",
                                },
                            },
                            "refcnt": 6,
                            "rib": "[B]",
                            "sharing": "per-destination",
                            "sources": ["RIB"],
                        }
                    }
                }
            }
        }
    }
}
