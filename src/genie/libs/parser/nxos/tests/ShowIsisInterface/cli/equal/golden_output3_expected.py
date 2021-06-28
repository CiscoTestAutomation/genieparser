expected_output = {
    "instance": {
        "1": {
            "vrf": {
                "default": {
                    "interfaces": {
                        "Ethernet1/1": {
                            "authentication": {
                                "level_1": {},
                                "level_2": {}
                            },
                            "bfd_ipv4": "locally disabled",
                            "bfd_ipv6": "locally disabled",
                            "circuit_type": "L1-2",
                            "index": "0x0001",
                            "ipv4": "9.9.9.1",
                            "ipv4_subnet": "9.9.9.0/24",
                            "levels": {
                                "1": {
                                    "designated_is": "uut1"
                                },
                                "2": {
                                    "designated_is": "uut1"
                                }
                            },
                            "local_circuit_id": "0x01",
                            "lsp_interval_ms": 33,
                            "mtr": "disabled",
                            "mtu": 1500,
                            "name": "Ethernet1/1",
                            "status": "protocol-up/link-up/admin-up",
                            "topologies": {
                                "0": {
                                    "level": {
                                        "1": {
                                            "fwdng": "UP",
                                            "ipv4_cfg": "yes",
                                            "ipv4_mt": "UP",
                                            "ipv6_cfg": "no",
                                            "ipv6_mt": "DN",
                                            "metric": "40",
                                            "metric_cfg": "no"
                                        },
                                        "2": {
                                            "fwdng": "UP",
                                            "ipv4_cfg": "yes",
                                            "ipv4_mt": "UP",
                                            "ipv6_cfg": "no",
                                            "ipv6_mt": "DN",
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