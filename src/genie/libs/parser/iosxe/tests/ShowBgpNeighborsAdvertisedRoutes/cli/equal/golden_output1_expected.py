expected_output = {
    "vrf": {
        "default": {
            "neighbor": {
                "192.168.120.13": {
                    "address_family": {
                        "": {
                            "advertised": {
                                "0.0.0.0": {
                                    "index": {
                                        1: {
                                            "status_codes": "r>i",
                                            "next_hop": "10.121.1.2",
                                            "origin_codes": "?",
                                            "metric": 0,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "209 64520"
                                        }
                                    }
                                },
                                "10.120.0.0/16": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.121.1.2",
                                            "origin_codes": "i",
                                            "metric": 0,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "209 64520"
                                        }
                                    }
                                },
                                "10.121.0.0/16": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "i"
                                        }
                                    }
                                },
                                "10.122.0.0/16": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.121.1.2",
                                            "origin_codes": "i",
                                            "metric": 0,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "209 64522"
                                        }
                                    }
                                },
                                "10.123.0.0/16": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.121.1.2",
                                            "origin_codes": "i",
                                            "metric": 0,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "209 64523"
                                        }
                                    }
                                },
                                "10.250.54.0/24": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.121.1.2",
                                            "origin_codes": "?",
                                            "metric": 0,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "209 64520"
                                        }
                                    }
                                },
                                "159.140.61.0/24": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.121.1.2",
                                            "origin_codes": "?",
                                            "metric": 0,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "209 64522 64522 64522"
                                        }
                                    }
                                },
                                "159.140.67.0/24": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.121.1.2",
                                            "origin_codes": "?",
                                            "metric": 0,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "209 64522 64522 64522"
                                        }
                                    }
                                },
                                "162.135.0.0": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.121.1.2",
                                            "origin_codes": "?",
                                            "metric": 0,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "209 64522 64522 64522"
                                        }
                                    }
                                },
                                "192.168.120.0/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.121.1.2",
                                            "origin_codes": "i",
                                            "metric": 0,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "209"
                                        }
                                    }
                                },
                                "192.168.120.8/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.121.1.2",
                                            "origin_codes": "i",
                                            "metric": 0,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "209"
                                        }
                                    }
                                },
                                "192.168.120.16/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.121.1.2",
                                            "origin_codes": "i",
                                            "metric": 0,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "209"
                                        }
                                    }
                                },
                                "192.168.120.24/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.121.1.2",
                                            "origin_codes": "i",
                                            "metric": 0,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "209"
                                        }
                                    }
                                }
                            },
                            "bgp_table_version": 407,
                            "local_router_id": "10.121.1.1"
                        }
                    }
                }
            }
        }
    }
}