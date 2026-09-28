expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "prefix": {
                        "2001:10:10:1::/64": {
                            "epoch": 8,
                            "rib": "[B]",
                            "refcnt": 5,
                            "sharing": "per-destination",
                            "sources": ["RIB"],
                            "feature_space": {
                                "iprm": "0x00018000",
                                "broker": {"distribution_priority": 4},
                            },
                            "ifnums": {
                                "Vlan200": {
                                    "ifnum": 1305,
                                    "address": "172.16.254.1",
                                }
                            },
                            "path_list": {
                                "763A0B850A68": {
                                    "locks": 5,
                                    "sharing": "per-destination",
                                    "flags": "0x249 [shble, rif, hwcn, bgp]",
                                    "path": {
                                        "763A042BA6E8": {
                                            "share": "1/1",
                                            "type": "attached nexthop",
                                            "for": "IPv6",
                                            "nexthop": {
                                                "172.16.254.1": {
                                                    "outgoing_interface": {
                                                        "Vlan200": {
                                                            "ip_adj": {
                                                                "Vlan200": {
                                                                    "addr": "172.16.254.1",
                                                                    "addr_info": "763A0B04D0B0",
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            },
                                        }
                                    },
                                }
                            },
                            "output_chain": {
                                "lookup": {
                                    "address_family": "IPv6",
                                    "table": "green",
                                }
                            },
                        }
                    }
                }
            }
        }
    }
}
