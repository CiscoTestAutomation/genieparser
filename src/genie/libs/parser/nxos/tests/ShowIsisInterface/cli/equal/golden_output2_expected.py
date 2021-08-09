expected_output = {
    "instance": {
        "1": {
            "vrf": {
                "default": {
                    "interfaces": {
                        "Ethernet1/1": {
                            "authentication": {
                                "level_1": {
                                    "auth_check": "set"
                                },
                                "level_2": {
                                    "auth_check": "set"
                                }
                            },
                            "bfd_ipv4": "locally disabled",
                            "bfd_ipv6": "locally disabled",
                            "circuit_type": "L1-2",
                            "index": "0x0001",
                            "ipv6": {
                                "2001:db8:1:1::1/64": {
                                    "state": "VALID"
                                }
                            },
                            "ipv6_link_local_address": "fe80::50fc:beff:fe6c:1b08",
                            "ipv6_subnet": "2001:db8:1:1::/64",
                            "levels": {
                                "1": {
                                    "csnp": "10",
                                    "designated_is": "uut1",
                                    "hello": "3",
                                    "metric_0": "40",
                                    "metric_2": "40",
                                    "multi": "3",
                                    "next_csnp": "00:00:04",
                                    "next_iih": "00:00:03"
                                },
                                "2": {
                                    "csnp": "10",
                                    "designated_is": "uut1",
                                    "hello": "3",
                                    "metric_0": "40",
                                    "metric_2": "40",
                                    "multi": "3",
                                    "next_csnp": "00:00:05",
                                    "next_iih": "00:00:02"
                                }
                            },
                            "local_circuit_id": "0x01",
                            "lsp_interval_ms": 33,
                            "mtr": "enabled",
                            "mtu": 1500,
                            "name": "Ethernet1/1",
                            "status": "protocol-up/link-up/admin-up",
                            "topologies": {
                                "0": {
                                    "level": {
                                        "1": {
                                            "fwdng": "DN",
                                            "ipv4_cfg": "no",
                                            "ipv4_mt": "DN",
                                            "ipv6_cfg": "no",
                                            "ipv6_mt": "DN",
                                            "metric": "40",
                                            "metric_cfg": "no"
                                        },
                                        "2": {
                                            "fwdng": "DN",
                                            "ipv4_cfg": "no",
                                            "ipv4_mt": "DN",
                                            "ipv6_cfg": "no",
                                            "ipv6_mt": "DN",
                                            "metric": "40",
                                            "metric_cfg": "no"
                                        }
                                    }
                                },
                                "2": {
                                    "level": {
                                        "1": {
                                            "fwdng": "UP",
                                            "ipv4_cfg": "no",
                                            "ipv4_mt": "DN",
                                            "ipv6_cfg": "yes",
                                            "ipv6_mt": "UP",
                                            "metric": "40",
                                            "metric_cfg": "no"
                                        },
                                        "2": {
                                            "fwdng": "UP",
                                            "ipv4_cfg": "no",
                                            "ipv4_mt": "DN",
                                            "ipv6_cfg": "yes",
                                            "ipv6_mt": "UP",
                                            "metric": "40",
                                            "metric_cfg": "no"
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
