expected_output = {
    "vrf": {
        "1018": {
            "neighbor": {
                "100.103.0.5": {
                    "address_family": {
                        "vpnv4 unicast": {
                            "advertised": {},
                            "bgp_table_version": 58974,
                            "local_router_id": "ROUTER-ID"
                        },
                        "vpnv4 unicast RD AS:RD": {
                            "bgp_table_version": 58974,
                            "local_router_id": "ROUTER-ID",
                            "route_distinguisher": "AS:RD",
                            "default_vrf": "VRF",
                            "advertised": {
                                "0.0.0.0": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "i",
                                            "weight": 32768,
                                            "localprf": 0
                                        }
                                    }
                                },
                                "3.3.3.0/28": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "NEIGHBOR",
                                            "origin_codes": "?"
                                        }
                                    }
                                },
                                "3.3.3.12/32": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "NEIGHBOR",
                                            "origin_codes": "?"
                                        }
                                    }
                                },
                                "4.78.52.234/32": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "NEIGHBOR",
                                            "origin_codes": "?"
                                        }
                                    }
                                },
                                "10.0.0.0": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "NEIGHBOR",
                                            "origin_codes": "i"
                                        },
                                        2: {
                                            "next_hop": "10.0.0.0",
                                            "origin_codes": "i",
                                            "status_codes": "*>"
                                        }
                                    }
                                },
                                "10.0.5.0/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "NEIGHBOR",
                                            "origin_codes": "i"
                                        }
                                    }
                                },
                                "10.0.5.4/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "NEIGHBOR",
                                            "origin_codes": "i"
                                        }
                                    }
                                },
                                "10.0.5.20/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "NEIGHBOR",
                                            "origin_codes": "?"
                                        }
                                    }
                                },
                                "10.0.5.24/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "NEIGHBOR",
                                            "origin_codes": "?"
                                        }
                                    }
                                },
                                "10.0.5.32/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "NEIGHBOR",
                                            "origin_codes": "?"
                                        }
                                    }
                                },
                                "10.0.5.36/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "NEIGHBOR",
                                            "origin_codes": "?"
                                        }
                                    }
                                },
                                "10.0.5.40/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "NEIGHBOR",
                                            "origin_codes": "?"
                                        }
                                    }
                                },
                                "10.0.5.48/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "NEIGHBOR",
                                            "origin_codes": "i"
                                        }
                                    }
                                },
                                "10.0.5.52/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "NEIGHBOR",
                                            "origin_codes": "?"
                                        }
                                    }
                                },
                                "10.0.5.60/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "NEIGHBOR",
                                            "origin_codes": "i"
                                        }
                                    }
                                },
                                "10.0.5.64/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "NEIGHBOR",
                                            "origin_codes": "?"
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

