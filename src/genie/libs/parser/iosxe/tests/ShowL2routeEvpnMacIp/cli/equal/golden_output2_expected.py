# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {"evi": {
                        1: {
                            "producer": {
                                "BGP": {
                                    "host_ip": {
                                        "192.168.11.254": {
                                            "eth_tag": {
                                                0 : {
                                                    "mac_addr": {
                                                        "0011.0011.0011" : {
                                                            "next_hops": [
                                                                "L:16 1.1.1.1"
                                                            ]
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "L2VPN": {
                                    "host_ip": {
                                        "192.168.11.254": {
                                            "eth_tag": {
                                                0 : {
                                                    "mac_addr" : {
                                                        "0011.0011.0011" : {
                                                            "next_hops": [
                                                                "BD11:0"
                                                            ]
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