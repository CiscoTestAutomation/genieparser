expected_output = {
    "vrf": {
        "default": {
            "neighbor": {
                "192.168.2.65": {
                    "address_family": {
                        "ipv4 unicast": {
                            "advertised": {
                                "0.0.0.0": {
                                    "index": {
                                        1: {
                                            "status_codes": "r>i",
                                            "next_hop": "10.250.6.1",
                                            "origin_codes": "i",
                                            "metric": 0,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "65000"
                                        }
                                    }
                                },
                                "10.0.0.0": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.250.6.1",
                                            "origin_codes": "?",
                                            "metric": 768,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "65000"
                                        }
                                    }
                                },
                                "10.1.100.23/32": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.250.6.1",
                                            "origin_codes": "i",
                                            "metric": 0,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "65000 65000 65000 65005"
                                        }
                                    }
                                },
                                "10.1.138.0/24": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.250.6.1",
                                            "origin_codes": "?",
                                            "metric": 3328,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "65000"
                                        }
                                    }
                                },
                                "10.2.28.11/32": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.250.6.1",
                                            "origin_codes": "?",
                                            "metric": 51968,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "65000"
                                        }
                                    }
                                },
                                "10.21.198.0/24": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "192.168.198.14",
                                            "origin_codes": "?",
                                            "weight": 32768,
                                            "localprf": 51712
                                        }
                                    }
                                },
                                "10.100.248.128/26": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.250.6.1",
                                            "origin_codes": "?",
                                            "metric": 3328,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "65000"
                                        }
                                    }
                                },
                                "10.105.144.128/25": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.250.6.1",
                                            "origin_codes": "?",
                                            "metric": 3328,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "65000"
                                        }
                                    }
                                },
                                "10.105.145.0/25": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.250.6.1",
                                            "origin_codes": "?",
                                            "metric": 3328,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "65000"
                                        }
                                    }
                                },
                                "10.105.145.128/25": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.250.6.1",
                                            "origin_codes": "?",
                                            "metric": 3328,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "65000"
                                        }
                                    }
                                },
                                "10.105.146.0/25": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.250.6.1",
                                            "origin_codes": "?",
                                            "metric": 3328,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "65000"
                                        }
                                    }
                                },
                                "10.105.146.128/25": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>i",
                                            "next_hop": "10.250.6.1",
                                            "origin_codes": "?",
                                            "metric": 3328,
                                            "localprf": 300,
                                            "weight": 0,
                                            "path": "65000"
                                        }
                                    }
                                }
                            },
                            "bgp_table_version": 1186969,
                            "local_router_id": "10.250.6.2"
                        }
                    }
                }
            }
        }
    }
}