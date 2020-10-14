expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "vpnv4 unicast RD 200:1": {
                    "bgp_table_version": 56,
                    "default_vrf": "default",
                    "route_distinguisher": "200:1",
                    "route_identifier": "10.64.4.4",
                    "routes": {
                        "10.1.1.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "* i",
                                    "weight": 0,
                                },
                                2: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "*>i",
                                    "weight": 0,
                                },
                            }
                        },
                        "10.1.2.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "* i",
                                    "weight": 0,
                                },
                                2: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "*>i",
                                    "weight": 0,
                                },
                            }
                        },
                    },
                },
                "vpnv4 unicast RD 200:2": {
                    "bgp_table_version": 56,
                    "default_vrf": "default",
                    "route_distinguisher": "200:2",
                    "route_identifier": "10.64.4.4",
                    "routes": {
                        "10.1.1.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "*>i",
                                    "weight": 0,
                                },
                                2: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "* i",
                                    "weight": 0,
                                },
                            }
                        },
                        "10.1.2.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "*>i",
                                    "weight": 0,
                                },
                                2: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "* i",
                                    "weight": 0,
                                },
                            }
                        },
                        "10.1.3.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "*>i",
                                    "weight": 0,
                                },
                                2: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "* i",
                                    "weight": 0,
                                },
                            }
                        },
                    },
                },
            }
        },
        "VRF1": {
            "address_family": {
                "vpnv4 unicast RD 300:1": {
                    "bgp_table_version": 56,
                    "default_vrf": "VRF1",
                    "route_distinguisher": "300:1",
                    "route_identifier": "10.64.4.4",
                    "vrf_route_identifier": "10.94.44.44",
                    "routes": {
                        "10.1.1.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "* i",
                                    "weight": 0,
                                },
                                2: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "*>i",
                                    "weight": 0,
                                },
                            }
                        },
                        "10.1.2.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "* i",
                                    "weight": 0,
                                },
                                2: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "*>i",
                                    "weight": 0,
                                },
                            }
                        },
                        "10.169.1.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.4.6.6",
                                    "origin_codes": "e",
                                    "path": "300 33299 51178 47751 {27016}",
                                    "status_codes": "*>",
                                    "weight": 0,
                                }
                            }
                        },
                        "10.169.2.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.4.6.6",
                                    "origin_codes": "e",
                                    "path": "300 33299 51178 47751 {27016}",
                                    "status_codes": "*>",
                                    "weight": 0,
                                }
                            }
                        },
                        "10.169.3.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.4.6.6",
                                    "origin_codes": "e",
                                    "path": "300 33299 51178 47751 {27016}",
                                    "status_codes": "*>",
                                    "weight": 0,
                                }
                            }
                        },
                        "10.169.4.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.4.6.6",
                                    "origin_codes": "e",
                                    "path": "300 33299 51178 47751 {27016}",
                                    "status_codes": "*>",
                                    "weight": 0,
                                }
                            }
                        },
                        "10.169.5.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.4.6.6",
                                    "origin_codes": "e",
                                    "path": "300 33299 51178 47751 {27016}",
                                    "status_codes": "*>",
                                    "weight": 0,
                                }
                            }
                        },
                        "10.9.2.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.66.6.6",
                                    "origin_codes": "e",
                                    "path": "400 33299 51178 47751 {27016}",
                                    "status_codes": "*>",
                                    "weight": 0,
                                }
                            }
                        },
                    },
                }
            }
        },
        "VRF2": {
            "address_family": {
                "vpnv4 unicast RD 400:1": {
                    "bgp_table_version": 56,
                    "default_vrf": "VRF2",
                    "route_distinguisher": "400:1",
                    "route_identifier": "10.64.4.4",
                    "vrf_route_identifier": "10.94.44.44",
                    "routes": {
                        "10.9.2.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.66.6.6",
                                    "origin_codes": "e",
                                    "path": "400 33299 51178 47751 {27016}",
                                    "status_codes": "*>",
                                    "weight": 0,
                                }
                            }
                        },
                        "10.9.3.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.66.6.6",
                                    "origin_codes": "e",
                                    "path": "400 33299 51178 47751 {27016}",
                                    "status_codes": "*>",
                                    "weight": 0,
                                }
                            }
                        },
                        "10.9.4.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.66.6.6",
                                    "origin_codes": "e",
                                    "path": "400 33299 51178 47751 {27016}",
                                    "status_codes": "*>",
                                    "weight": 0,
                                }
                            }
                        },
                        "10.9.5.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.66.6.6",
                                    "origin_codes": "e",
                                    "path": "400 33299 51178 47751 {27016}",
                                    "status_codes": "*>",
                                    "weight": 0,
                                }
                            }
                        },
                        "10.9.6.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.66.6.6",
                                    "origin_codes": "e",
                                    "path": "400 33299 51178 47751 {27016}",
                                    "status_codes": "*>",
                                    "weight": 0,
                                }
                            }
                        },
                        "2001:db8:cdc9:121::/64": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "localpref": 100,
                                    "next_hop": "::FFFF:10.4.1.1",
                                    "origin_codes": "e",
                                    "path": "400 33299 51178 47751 {27016}",
                                    "status_codes": "* i",
                                    "weight": 0,
                                },
                                2: {
                                    "metric": 2219,
                                    "localpref": 100,
                                    "next_hop": "::FFFF:10.4.1.1",
                                    "origin_codes": "e",
                                    "path": "400 33299 51178 47751 {27016}",
                                    "status_codes": "*>i",
                                    "weight": 0,
                                },
                            }
                        },
                        "2001:db8:cdc9:144::/64": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "localpref": 100,
                                    "next_hop": "::FFFF:10.4.1.1",
                                    "origin_codes": "e",
                                    "path": "400 33299 51178 47751 {27016}",
                                    "status_codes": "* i",
                                    "weight": 0,
                                },
                                2: {
                                    "metric": 2219,
                                    "localpref": 100,
                                    "next_hop": "::FFFF:10.4.1.1",
                                    "origin_codes": "e",
                                    "path": "400 33299 51178 47751 {27016}",
                                    "status_codes": "*>i",
                                    "weight": 0,
                                },
                            }
                        },
                    },
                }
            }
        },
    }
}
