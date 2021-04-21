expected_output = {
    "vrf": {
        "default": {
            "neighbor": {
                "10.186.0.2": {
                    "address_family": {
                        "vpnv4 unicast": {
                            "advertised": {},
                            "bgp_table_version": 56,
                            "local_router_id": "10.64.4.4",
                        },
                        "vpnv4 unicast RD 300:1": {
                            "advertised": {
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
                            },
                            "bgp_table_version": 56,
                            "default_vrf": "VRF1",
                            "local_router_id": "10.64.4.4",
                            "route_distinguisher": "300:1",
                        },
                        "vpnv4 unicast RD 400:1": {
                            "advertised": {
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
                            },
                            "bgp_table_version": 56,
                            "default_vrf": "VRF2",
                            "local_router_id": "10.64.4.4",
                            "route_distinguisher": "400:1",
                        },
                        "vpnv6 unicast": {
                            "advertised": {},
                            "bgp_table_version": 66,
                            "local_router_id": "10.64.4.4",
                        },
                        "vpnv6 unicast RD 300:1": {
                            "advertised": {
                                "2001:db8:31b9:144::/64": {
                                    "index": {
                                        1: {
                                            "metric": 2219,
                                            "next_hop": "2001:DB8:4:6::6",
                                            "origin_codes": "e",
                                            "path": "300 33299 51178 47751 {27016}",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "2001:db8:31b9:169::/64": {
                                    "index": {
                                        1: {
                                            "metric": 2219,
                                            "next_hop": "2001:DB8:4:6::6",
                                            "origin_codes": "e",
                                            "path": "300 33299 51178 47751 {27016}",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "2001:db8:31b9:190::/64": {
                                    "index": {
                                        1: {
                                            "metric": 2219,
                                            "next_hop": "2001:DB8:4:6::6",
                                            "origin_codes": "e",
                                            "path": "300 33299 51178 47751 {27016}",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "2001:db8:31b9:1b9::/64": {
                                    "index": {
                                        1: {
                                            "metric": 2219,
                                            "next_hop": "2001:DB8:4:6::6",
                                            "origin_codes": "e",
                                            "path": "300 33299 51178 47751 {27016}",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "2001:db8:31b9:121::/64": {
                                    "index": {
                                        1: {
                                            "metric": 2219,
                                            "next_hop": "2001:DB8:4:6::6",
                                            "origin_codes": "e",
                                            "path": "300 33299 51178 47751 {27016}",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                            },
                            "bgp_table_version": 66,
                            "default_vrf": "VRF1",
                            "local_router_id": "10.64.4.4",
                            "route_distinguisher": "300:1",
                        },
                        "vpnv6 unicast RD 400:1": {
                            "advertised": {
                                "2001:db8:a69:4c9::/64": {
                                    "index": {
                                        1: {
                                            "metric": 2219,
                                            "next_hop": "2001:DB8:20:4:6::6",
                                            "origin_codes": "e",
                                            "path": "400 33299 51178 47751 {27016}",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "2001:db8:a69:510::/64": {
                                    "index": {
                                        1: {
                                            "metric": 2219,
                                            "next_hop": "2001:DB8:20:4:6::6",
                                            "origin_codes": "e",
                                            "path": "400 33299 51178 47751 {27016}",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "2001:db8:a69:559::/64": {
                                    "index": {
                                        1: {
                                            "metric": 2219,
                                            "next_hop": "2001:DB8:20:4:6::6",
                                            "origin_codes": "e",
                                            "path": "400 33299 51178 47751 {27016}",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "2001:db8:a69:5a4::/64": {
                                    "index": {
                                        1: {
                                            "metric": 2219,
                                            "next_hop": "2001:DB8:20:4:6::6",
                                            "origin_codes": "e",
                                            "path": "400 33299 51178 47751 {27016}",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "2001:db8:a69:484::/64": {
                                    "index": {
                                        1: {
                                            "metric": 2219,
                                            "next_hop": "2001:DB8:20:4:6::6",
                                            "origin_codes": "e",
                                            "path": "400 33299 51178 47751 {27016}",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                            },
                            "bgp_table_version": 66,
                            "default_vrf": "VRF2",
                            "local_router_id": "10.64.4.4",
                            "route_distinguisher": "400:1",
                        },
                    }
                }
            }
        }
    }
}
