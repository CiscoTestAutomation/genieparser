# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {"evi": {
                        "2": {
                            "producer": {
                                "BGP": {
                                    "host_ips": {
                                        "192.168.12.254": {
                                            "esi": "0000.0000.0000.0000.0000",
                                            "eth_tag": "0",
                                            "label_2": "0",
                                            "mac_addr": "0012.0012.0012",
                                            "mac_rt_flags": "BInt(Brm)Dgr",
                                            "next_hops": [
                                                "L:16 2.2.2.1"
                                            ],
                                            "seq_number": "0"
                                        },
                                        "2001:12::254": {
                                            "esi": "0000.0000.0000.0000.0000",
                                            "eth_tag": "0",
                                            "label_2": "0",
                                            "mac_addr": "0012.0012.0012",
                                            "mac_rt_flags": "BInt(Brm)Dgr",
                                            "next_hops": [
                                                "L:16 2.2.2.1"
                                            ],
                                            "seq_number": "0"
                                        },
                                        "FE80::A8BB:CCFF:FE82:2800": {
                                            "esi": "03AA.BB00.0000.0200.0001",
                                            "eth_tag": "0",
                                            "label_2": "0",
                                            "mac_addr": "aabb.cc82.2800",
                                            "mac_rt_flags": "Int(Brm)",
                                            "next_hops": [
                                                "L:17 4.4.4.1(proxy)"
                                            ],
                                            "seq_number": "0"
                                        },
                                        "FE80::A8BB:FF:FE12:2": {
                                            "esi": "0000.0000.0000.0000.0000",
                                            "eth_tag": "0",
                                            "label_2": "0",
                                            "mac_addr": "aabb.0012.0002",
                                            "mac_rt_flags": "B()",
                                            "next_hops": [
                                                "L:16 2.2.2.1"
                                            ],
                                            "seq_number": "0"
                                        }
                                    }
                                },
                                "L2VPN": {
                                    "host_ips": {
                                        "192.168.12.254": {
                                            "esi": "0000.0000.0000.0000.0000",
                                            "eth_tag": "0",
                                            "label_2": "0",
                                            "mac_addr": "0012.0012.0012",
                                            "mac_rt_flags": "Int(Brm)Dgl",
                                            "next_hops": [
                                                "BD12:0",
                                                "L:17 4.4.4.1"
                                            ],
                                            "seq_number": "0"
                                        },
                                        "2001:12::254": {
                                            "esi": "0000.0000.0000.0000.0000",
                                            "eth_tag": "0",
                                            "label_2": "0",
                                            "mac_addr": "0012.0012.0012",
                                            "mac_rt_flags": "Int(Brm)Dgl",
                                            "next_hops": [
                                                "BD12:0"
                                            ],
                                            "seq_number": "0"
                                        },
                                        "FE80::A8BB:CCFF:FE82:2800": {
                                            "esi": "03AA.BB00.0000.0200.0001",
                                            "eth_tag": "0",
                                            "label_2": "0",
                                            "mac_addr": "aabb.cc82.2800",
                                            "mac_rt_flags": "B(Brm)",
                                            "next_hops": [
                                                "Et1/0:12"
                                            ],
                                            "seq_number": "0"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
