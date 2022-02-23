expected_output = {
    "vrf": {
        "default": {
            "neighbor": {
                "10.186.0.2": {
                    "address_family": {
                        "vpnv4 unicast": {
                            "bgp_table_version": 56,
                            "local_router_id": "10.64.4.4",
                            "routes": {},
                        },
                        "vpnv4 unicast RD 200:1": {
                            "bgp_table_version": 56,
                            "local_router_id": "10.64.4.4",
                            "route_distinguisher": "200:1",
                            "routes": {
                                "10.1.1.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "10.1.2.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "10.1.3.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "10.1.4.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "10.1.5.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                            },
                        },
                        "vpnv4 unicast RD 200:2": {
                            "bgp_table_version": 56,
                            "local_router_id": "10.64.4.4",
                            "route_distinguisher": "200:2",
                            "routes": {
                                "10.1.1.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "10.1.2.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "10.1.3.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "10.1.4.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "10.1.5.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                            },
                        },
                        "vpnv4 unicast RD 300:1": {
                            "bgp_table_version": 56,
                            "default_vrf": "VRF1",
                            "local_router_id": "10.64.4.4",
                            "route_distinguisher": "300:1",
                            "routes": {
                                "10.1.1.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                        2: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                    }
                                },
                                "10.1.2.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                        2: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                    }
                                },
                                "10.1.3.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                        2: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                    }
                                },
                                "10.1.4.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                        2: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                    }
                                },
                                "10.1.5.0/24": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                        2: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                    }
                                },
                            },
                        },
                        "vpnv6 unicast": {
                            "bgp_table_version": 66,
                            "local_router_id": "10.64.4.4",
                            "routes": {},
                        },
                        "vpnv6 unicast RD 200:1": {
                            "bgp_table_version": 66,
                            "local_router_id": "10.64.4.4",
                            "route_distinguisher": "200:1",
                            "routes": {
                                "2001:db8:cdc9:144::/64": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "2001:db8:cdc9:169::/64": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "2001:db8:cdc9:190::/64": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "2001:db8:cdc9:1b9::/64": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "2001:db8:cdc9:121::/64": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                            },
                        },
                        "vpnv6 unicast RD 200:2": {
                            "bgp_table_version": 66,
                            "local_router_id": "10.64.4.4",
                            "route_distinguisher": "200:2",
                            "routes": {
                                "2001:db8:cdc9:144::/64": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "2001:db8:cdc9:169::/64": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "2001:db8:cdc9:190::/64": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "2001:db8:cdc9:1b9::/64": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "2001:db8:cdc9:121::/64": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                            },
                        },
                        "vpnv6 unicast RD 300:1": {
                            "bgp_table_version": 66,
                            "default_vrf": "VRF1",
                            "local_router_id": "10.64.4.4",
                            "route_distinguisher": "300:1",
                            "routes": {
                                "2001:db8:cdc9:144::/64": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                        2: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                    }
                                },
                                "2001:db8:cdc9:169::/64": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                        2: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                    }
                                },
                                "2001:db8:cdc9:190::/64": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                        2: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                    }
                                },
                                "2001:db8:cdc9:1b9::/64": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                        2: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                    }
                                },
                                "2001:db8:cdc9:121::/64": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                        2: {
                                            "localprf": 100,
                                            "metric": 2219,
                                            "next_hop": "::FFFF:10.4.1.1",
                                            "origin_codes": "e",
                                            "path": "200 33299 51178 47751 {27016}",
                                            "path_type": "i",
                                            "status_codes": "*",
                                            "weight": 0,
                                        },
                                    }
                                },
                            },
                        },
                    }
                }
            }
        }
    },
    "total_num_of_prefixes": 40
}
