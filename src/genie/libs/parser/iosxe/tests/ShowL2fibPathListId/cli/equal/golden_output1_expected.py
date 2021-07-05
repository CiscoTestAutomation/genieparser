# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {"path_ids": {
                                "12": {
                                    "eth_seg": "03AA.BB00.0000.0200.0001",
                                    "path_cnt": 2,
                                    "path_list": [
                                        "[MAC]17@3.3.3.1",
                                        "[EVI]17@4.4.4.1"
                                    ],
                                    "type": "MPLS_UC"
                                },
                                "2": {
                                    "eth_seg": "0000.0000.0000.0000.0000",
                                    "path_cnt": 1,
                                    "path_list": [
                                        "[IR]16@3.3.3.1"
                                    ],
                                    "type": "MPLS_IR"
                                },
                                "3": {
                                    "eth_seg": "0000.0000.0000.0000.0000",
                                    "path_cnt": 1,
                                    "path_list": [
                                        "[MAC]16@2.2.2.1"
                                    ],
                                    "type": "MPLS_UC"
                                },
                                "4": {
                                    "eth_seg": "0000.0000.0000.0000.0000",
                                    "path_cnt": 1,
                                    "path_list": [
                                        "[IR]17@2.2.2.1"
                                    ],
                                    "type": "MPLS_IR"
                                },
                                "5": {
                                    "eth_seg": "03AA.BB00.0000.0200.0001",
                                    "path_cnt": 2,
                                    "path_list": [
                                        "[None]16@3.3.3.1",
                                        "[None]16@4.4.4.1"
                                    ],
                                    "type": "EAD_ES"
                                },
                                "6": {
                                    "eth_seg": "0000.0000.0000.0000.0000",
                                    "path_cnt": 1,
                                    "path_list": [
                                        "[IR]16@4.4.4.1"
                                    ],
                                    "type": "MPLS_IR"
                                }
                            }
                    }