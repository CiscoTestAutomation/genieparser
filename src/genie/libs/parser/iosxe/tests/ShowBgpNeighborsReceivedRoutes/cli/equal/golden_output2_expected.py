expected_output = {
    "vrf": {
        "default": {
            "neighbor": {
                "10.106.101.1": {
                    "address_family": {
                        "ipv4 multicast": {
                            "bgp_table_version": 175,
                            "local_router_id": "10.145.0.6",
                            "received_routes": {
                                "10.9.1.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "next_hop": "10.106.101.1",
                                            "origin_codes": "i",
                                            "path": "2 3 4",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "10.9.2.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "next_hop": "10.106.101.1",
                                            "origin_codes": "i",
                                            "path": "2 3 4",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                            },
                        },
                        "ipv4 unicast": {
                            "bgp_table_version": 174,
                            "local_router_id": "10.145.0.6",
                            "received_routes": {
                                "10.4.1.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2222,
                                            "next_hop": "10.106.101.1",
                                            "origin_codes": "i",
                                            "path": "1 2 3 65000 23",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "10.4.2.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2222,
                                            "next_hop": "10.106.101.1",
                                            "origin_codes": "i",
                                            "path": "1 2 3 65000 23",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "10.49.0.0/16": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "next_hop": "10.106.101.1",
                                            "origin_codes": "i",
                                            "path": "10 20 30 40 50 60 70 80 90",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                            },
                        },
                        "ipv6 multicast": {
                            "bgp_table_version": 6,
                            "local_router_id": "10.145.0.6",
                            "received_routes": {},
                        },
                        "ipv6 unicast": {
                            "bgp_table_version": 173,
                            "local_router_id": "10.145.0.6",
                            "received_routes": {},
                        },
                        "link-state": {
                            "bgp_table_version": 173,
                            "local_router_id": "10.145.0.6",
                            "received_routes": {
                                "[2]:[77][7,0][10.69.9.9,1,151587081][10.135.1.1,22][10.106.101.1,10.76.1.30]/616": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 4444,
                                            "next_hop": "10.106.101.1",
                                            "origin_codes": "i",
                                            "path": "3 10 20 30 40 50 60 70 80 90",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "[2]:[77][7,0][10.69.9.9,2,151587081][10.135.1.1,22][10.106.101.1,10.76.1.31]/616": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 4444,
                                            "next_hop": "10.106.101.1",
                                            "origin_codes": "i",
                                            "path": "3 10 20 30 40 50 60 70 80 90",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                            },
                        },
                        "vpnv4 unicast": {
                            "bgp_table_version": 183,
                            "local_router_id": "10.145.0.6",
                            "received_routes": {},
                        },
                        "vpnv4 unicast RD 0:0": {
                            "bgp_table_version": 183,
                            "local_router_id": "10.145.0.6",
                            "route_distinguisher": "0:0",
                            "received_routes": {},
                        },
                        "vpnv4 unicast RD 101:100": {
                            "bgp_table_version": 183,
                            "local_router_id": "10.145.0.6",
                            "route_distinguisher": "101:100",
                            "received_routes": {
                                "10.16.1.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 4444,
                                            "next_hop": "10.106.101.1",
                                            "origin_codes": "i",
                                            "path": "3 10 20 4 5 6 3 10 20 4 5 6",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "10.16.2.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 4444,
                                            "next_hop": "10.106.101.1",
                                            "origin_codes": "i",
                                            "path": "3 10 20 4 5 6 3 10 20 4 5 6",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        }
                                    }
                                },
                            },
                        },
                        "vpnv4 unicast RD 102:100": {
                            "bgp_table_version": 183,
                            "local_router_id": "10.145.0.6",
                            "route_distinguisher": "102:100",
                            "received_routes": {},
                        },
                        "vpnv6 unicast": {
                            "bgp_table_version": 13,
                            "local_router_id": "10.145.0.6",
                            "received_routes": {},
                        },
                        "vpnv6 unicast RD 0xbb00010000000000": {
                            "bgp_table_version": 13,
                            "local_router_id": "10.145.0.6",
                            "route_distinguisher": "0xbb00010000000000",
                            "received_routes": {},
                        },
                        "vpnv6 unicast RD 100:200": {
                            "bgp_table_version": 13,
                            "local_router_id": "10.145.0.6",
                            "route_distinguisher": "100:200",
                            "received_routes": {
                                "2001:db8:aaaa:1::/113": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "next_hop": "4444",
                                            "origin_codes": "i",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "2001:db8:2001:db8:aaaa:1::8000/113": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "next_hop": "4444",
                                            "origin_codes": "i",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                            },
                        },
                    }
                }
            }
        }
    }
}
