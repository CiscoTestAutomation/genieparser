expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "10.55.50.1/32": {
                            "epoch": 0,
                            "feature_space": {
                                "broker": {"distribution_priority": 3},
                                "iprm": "0x00018000",
                                "lfd": {"10.55.50.1/32": {"local_labels": 0}},
                            },
                            "flags": ["rlbls"],
                            "output_chain": {
                                "label": ["262", "implicit-null"],
                                "tag_midchain": {
                                    "Tunnel65537": {
                                        "frr": {
                                            "primary": {
                                                "info": "0x80007F4F894B79F0",
                                                "primary": {
                                                    "tag_adj": {
                                                        "GigabitEthernet0/1/6": {
                                                            "addr": "10.169.196.213",
                                                            "addr_info": "7F4F881C1898",
                                                        }
                                                    }
                                                },
                                                "repair": {
                                                    "label": ["16061"],
                                                    "tag_adj": {
                                                        "GigabitEthernet0/1/7": {
                                                            "addr": "10.169.196.217",
                                                            "addr_info": "7F4F881C1CF8",
                                                        }
                                                    },
                                                },
                                            }
                                        },
                                        "label": [
                                            "[16073|16073]",
                                            "[90|90]",
                                            "[95|95]",
                                            "[90|90]",
                                        ],
                                        "tag_midchain_info": "7F4F881C0718",
                                    }
                                },
                            },
                            "path_list": {
                                "7F4F8A142848": {
                                    "flags": "0x249 [shble, rif, hwcn, bgp]",
                                    "locks": 3,
                                    "path": {
                                        "7F4F89512770": {
                                            "flags": "[must-be-lbld]",
                                            "for": "IPv4",
                                            "share": "1/1",
                                            "type": "recursive",
                                        }
                                    },
                                    "sharing": "per-destination",
                                },
                                "7F4F8A1428E8": {
                                    "flags": "0x249 [shble, rif, hwcn, bgp]",
                                    "locks": 3,
                                    "path": {
                                        "7F4F89512430": {
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
