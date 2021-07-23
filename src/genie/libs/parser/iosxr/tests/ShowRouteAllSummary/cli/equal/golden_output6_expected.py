expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "IPv4 Unicast": {
                    "route_source": {
                        "connected": {
                            "routes": 7,
                            "backup": 1,
                            "deleted": 0,
                            "memory_bytes": 1984
                        },
                        "local": {
                            "routes": 8,
                            "backup": 0,
                            "deleted": 0,
                            "memory_bytes": 1984
                        },
                        "static": {
                            "routes": 0,
                            "backup": 0,
                            "deleted": 0,
                            "memory_bytes": 0
                        },
                        "ospf": {
                            "65000": {
                                "routes": 5,
                                "backup": 0,
                                "deleted": 0,
                                "memory_bytes": 1352
                            }
                        },
                        "bgp": {
                            "65000.65000": {
                                "routes": 6174,
                                "backup": 5,
                                "deleted": 0,
                                "memory_bytes": 1532392
                            }
                        },
                        "dagr": {
                            "routes": 0,
                            "backup": 0,
                            "deleted": 0,
                            "memory_bytes": 0
                        }
                    },
                    "total_route_source": {
                        "routes": 6194,
                        "backup": 6,
                        "deleted": 0,
                        "memory_bytes": 1537712
                    }
                },
                "IPv4 Multicast": {
                    "route_source": {
                        "local": {
                            "routes": 0,
                            "backup": 0,
                            "deleted": 0,
                            "memory_bytes": 0
                        },
                        "connected": {
                            "routes": 0,
                            "backup": 0,
                            "deleted": 0,
                            "memory_bytes": 0
                        }
                    },
                    "total_route_source": {
                        "routes": 0,
                        "backup": 0,
                        "deleted": 0,
                        "memory_bytes": 0
                    }
                },
                "IPv6 Unicast": {
                    "route_source": {
                        "connected": {
                            "routes": 7,
                            "backup": 1,
                            "deleted": 0,
                            "memory_bytes": 2176,
                            "l2tpv3_xconnect": {
                                "routes": 0,
                                "backup": 0,
                                "deleted": 0,
                                "memory_bytes": 0
                            }
                        },
                        "local": {
                            "routes": 8,
                            "backup": 0,
                            "deleted": 0,
                            "memory_bytes": 2176
                        },
                        "static": {
                            "routes": 2,
                            "backup": 0,
                            "deleted": 0,
                            "memory_bytes": 544
                        },
                        "ospf": {
                            "65000": {
                                "routes": 7,
                                "backup": 0,
                                "deleted": 0,
                                "memory_bytes": 2176
                            }
                        },
                        "bgp": {
                            "65000.65000": {
                                "routes": 36,
                                "backup": 5,
                                "deleted": 1,
                                "memory_bytes": 11288
                            }
                        },
                        "local-srv6": {
                            "bgp-65000.65000": {
                                "routes": 0,
                                "backup": 0,
                                "deleted": 0,
                                "memory_bytes": 0
                            }
                        }
                    },
                    "total_route_source": {
                        "routes": 60,
                        "backup": 6,
                        "deleted": 1,
                        "memory_bytes": 18360
                    }
                },
                "IPv6 Multicast": {
                    "route_source": {
                        "connected": {
                            "routes": 0,
                            "backup": 0,
                            "deleted": 0,
                            "memory_bytes": 0
                        },
                        "local": {
                            "routes": 0,
                            "backup": 0,
                            "deleted": 0,
                            "memory_bytes": 0
                        }
                    },
                    "total_route_source": {
                        "routes": 0,
                        "backup": 0,
                        "deleted": 0,
                        "memory_bytes": 0
                    }
                }
            }
        }
    }
}
