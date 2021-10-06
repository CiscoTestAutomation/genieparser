# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {"evi": {
                        1: {
                            "producer": {
                                "BGP": {
                                    "origin_router_ip": {
                                        "1.1.1.3": {
                                            "eth_tag": {
                                                0 : {
                                                    "router_eth_tag": 0,
                                                    'tunnel_id': {
                                                        "1.1.1.1": {
                                                            'tunnel_flags': 0,
                                                            'tunnel_type': "Ingress Replication",
                                                            'tunnel_labels': 17,
                                                        }
                                                    },
                                                    "multi_proxy": "No",
                                                    "next_hops": [
                                                        "L:0 1.1.1.1"
                                                    ]
                                                }
                                            }
                                        },
                                        "2.2.2.3": {
                                            "eth_tag": {
                                                0 : {
                                                    "router_eth_tag": 0,
                                                    'tunnel_id': {
                                                        "2.2.2.1": {
                                                            'tunnel_flags': 0,
                                                            'tunnel_type': "Ingress Replication",
                                                            'tunnel_labels': 18,
                                                        }
                                                    },
                                                    "multi_proxy": "No",
                                                    "next_hops": [
                                                        "L:0 2.2.2.1"
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
