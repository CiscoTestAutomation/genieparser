expected_output = {
    "vrf": {
        "default": {
            "neighbor": {
                "192.168.36.119": {
                    "address_family": {
                        "vpnv4 unicast": {
                            "advertised": {},
                            "bgp_table_version": 16933183,
                            "local_router_id": "10.169.197.254",
                        },
                        "vpnv4 unicast RD 5918:50": {
                            "advertised": {
                                "10.4.1.0/24": {
                                    "index": {
                                        1: {
                                            "metric": 0,
                                            "next_hop": "192.168.10.253",
                                            "origin_codes": "?",
                                            "path": "62000",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "10.44.105.0/24": {
                                    "index": {
                                        1: {
                                            "metric": 0,
                                            "next_hop": "192.168.10.253",
                                            "origin_codes": "?",
                                            "path": "62000",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "172.16.100.1/32": {
                                    "index": {
                                        1: {
                                            "metric": 0,
                                            "next_hop": "192.168.10.253",
                                            "origin_codes": "?",
                                            "path": "62000",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "172.16.100.100/32": {
                                    "index": {
                                        1: {
                                            "metric": 0,
                                            "next_hop": "192.168.10.253",
                                            "origin_codes": "?",
                                            "path": "62000",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "172.16.100.2/32": {
                                    "index": {
                                        1: {
                                            "metric": 0,
                                            "next_hop": "192.168.10.253",
                                            "origin_codes": "?",
                                            "path": "62000",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "172.16.100.3/32": {
                                    "index": {
                                        1: {
                                            "metric": 0,
                                            "next_hop": "192.168.10.253",
                                            "origin_codes": "?",
                                            "path": "62000",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "172.16.100.4/32": {
                                    "index": {
                                        1: {
                                            "metric": 0,
                                            "next_hop": "192.168.10.253",
                                            "origin_codes": "?",
                                            "path": "62000",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "172.16.100.5/32": {
                                    "index": {
                                        1: {
                                            "metric": 0,
                                            "next_hop": "192.168.10.253",
                                            "origin_codes": "?",
                                            "path": "62000",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "172.16.100.6/32": {
                                    "index": {
                                        1: {
                                            "metric": 0,
                                            "next_hop": "192.168.10.253",
                                            "origin_codes": "?",
                                            "path": "62000",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "192.168.10.0": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "?",
                                            "weight": 32768,
                                            "localprf": 0,
                                        }
                                    }
                                },
                            },
                            "bgp_table_version": 16933183,
                            "default_vrf": "L3VPN-0050",
                            "local_router_id": "10.169.197.254",
                            "route_distinguisher": "5918:50",
                        },
                        "vpnv4 unicast RD 5918:51": {
                            "advertised": {
                                "172.16.100.1/32": {
                                    "index": {
                                        1: {
                                            "next_hop": "192.168.10.253",
                                            "origin_codes": "i",
                                            "path": "65555",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "172.16.100.2/32": {
                                    "index": {
                                        1: {
                                            "next_hop": "192.168.10.253",
                                            "origin_codes": "i",
                                            "path": "65555",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "172.16.100.3/32": {
                                    "index": {
                                        1: {
                                            "next_hop": "192.168.10.253",
                                            "origin_codes": "i",
                                            "path": "65555",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "172.16.100.4/32": {
                                    "index": {
                                        1: {
                                            "next_hop": "192.168.10.253",
                                            "origin_codes": "i",
                                            "path": "65555",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "172.16.100.5/32": {
                                    "index": {
                                        1: {
                                            "next_hop": "192.168.10.253",
                                            "origin_codes": "i",
                                            "path": "65555",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "172.16.100.6/32": {
                                    "index": {
                                        1: {
                                            "next_hop": "192.168.10.253",
                                            "origin_codes": "i",
                                            "path": "65555",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                            },
                            "bgp_table_version": 16933183,
                            "default_vrf": "L3VPN-0051",
                            "local_router_id": "10.169.197.254",
                            "route_distinguisher": "5918:51",
                        },
                    }
                }
            }
        }
    }
}
