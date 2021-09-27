# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {"evi": {
                        1: {
                            "producer": {
                                "BGP": {
                                    "origin_router_ip": {
                                        "2.2.2.2": {
                                            "eth_tag": {
                                                0 : {
                                                    "router_eth_tag": 0,
                                                    'tunnel_id': {
                                                        "2.2.2.2": {
                                                            'tunnel_flags': 0,
                                                            'tunnel_type': "Ingress Replication",
                                                            'tunnel_labels': 20011,
                                                        }
                                                    },
                                                    "multi_proxy": "IGMP, MLD",
                                                    "next_hops": [
                                                         "V:20011 2.2.2.2"
                                                    ]
                                                }
                                            }
                                        },
                                        "3.3.3.2": {
                                            "eth_tag": {
                                                0 : {
                                                    "router_eth_tag": 0,
                                                    'tunnel_id': {
                                                        "3.3.3.2": {
                                                            'tunnel_flags': 0,
                                                            'tunnel_type': "Ingress Replication",
                                                            'tunnel_labels': 20011,
                                                        }
                                                    },
                                                    "multi_proxy": "IGMP",
                                                    "next_hops": [
                                                        "V:20011 3.3.3.2"
                                                    ]
                                                }
                                            }
                                        }
                                    }
                                },
                                "L2VPN": {
                                    "origin_router_ip": {
                                        "1.1.1.2": {
                                            "eth_tag": {
                                                0 : {
                                                    "router_eth_tag": 0,
                                                    'tunnel_id': {
                                                        "1.1.1.2": {
                                                            'tunnel_flags': 0,
                                                            'tunnel_type': "Ingress Replication",
                                                            'tunnel_labels': 20011,
                                                        }
                                                    },
                                                    "multi_proxy": "IGMP",
                                                    "next_hops": [
                                                        "N/A"
                                                    ]
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        2: {
                            "producer": {
                                "BGP": {
                                    "origin_router_ip": {
                                        "2.2.2.2": {
                                            "eth_tag": {
                                                0 : {
                                                    "router_eth_tag": 0,
                                                    'tunnel_id': {
                                                        "2.2.2.2": {
                                                            'tunnel_flags': 0,
                                                            'tunnel_type': "Ingress Replication",
                                                            'tunnel_labels': 20012,
                                                        }
                                                    },
                                                    "multi_proxy": "IGMP",
                                                    "next_hops": [
                                                        "V:20012 2.2.2.2"
                                                    ]
                                                }
                                            }
                                        },
                                        "3.3.3.2": {
                                            "eth_tag": {
                                                0 : {
                                                    "router_eth_tag": 0,
                                                    'tunnel_id': {
                                                        "3.3.3.2": {
                                                            'tunnel_flags': 0,
                                                            'tunnel_type': "Ingress Replication",
                                                            'tunnel_labels': 20012,
                                                        }
                                                    },
                                                    "multi_proxy": "IGMP",
                                                    "next_hops": [
                                                        "V:20012 3.3.3.2"
                                                    ]
                                                }
                                            }
                                        }
                                    }
                                },
                                "L2VPN": {
                                    "origin_router_ip": {
                                        "1.1.1.2": {
                                            "eth_tag": {
                                                0 : {
                                                    "router_eth_tag": 0,
                                                    'tunnel_id': {
                                                        "1.1.1.2": {
                                                            'tunnel_flags': 0,
                                                            'tunnel_type': "Ingress Replication",
                                                            'tunnel_labels': 20012,
                                                        }
                                                    },
                                                    "multi_proxy": "IGMP",
                                                    "next_hops": [
                                                        "N/A"
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
