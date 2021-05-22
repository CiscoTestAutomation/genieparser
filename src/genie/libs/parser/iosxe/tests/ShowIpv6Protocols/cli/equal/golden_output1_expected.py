expected_output = {
    "protocols": {
        "bgp": {
            "instance": {
                "default": {
                    "bgp_id": 65003,
                    "vrf": {
                        "default": {
                            "address_family": {
                                "ipv6": {
                                    "igp_sync": False,
                                    "neighbors": {
                                        "1.1.1.1": {},
                                        "2001:DB8:20:10::10": {},
                                    },
                                    "redistribute": {
                                        "connected": {"include_connected": False},
                                        "eigrp": {
                                            "10": {
                                                "include_connected": True,
                                                "route_policy": "test",
                                            }
                                        },
                                        "ospf": {
                                            "1": {
                                                "include_connected": True,
                                                "route_policy": "test",
                                            }
                                        },
                                        "rip": {
                                            "worldskills": {
                                                "include_connected": True,
                                                "route_policy": "test",
                                            }
                                        },
                                        "static": {
                                            "include_connected": False,
                                            "route_policy": "test",
                                        },
                                    },
                                }
                            }
                        }
                    },
                }
            }
        },
        "eigrp": {
            "vrf": {
                "default": {
                    "address_family": {
                        "ipv6": {
                            "eigrp_instance": {
                                "10": {
                                    "configured_interfaces": [
                                        "Loopback3",
                                        "GigabitEthernet0/1",
                                        "GigabitEthernet0/0",
                                    ],
                                    "eigrp_id": 10,
                                    "metric_weight": {
                                        "k1": 1,
                                        "k2": 0,
                                        "k3": 1,
                                        "k4": 0,
                                        "k5": 0,
                                    },
                                    "named_mode": False,
                                    "passive_interfaces": ["GigabitEthernet0/0"],
                                    "redistribute": {},
                                    "router_id": "4.4.4.4",
                                    "topology": {
                                        "0": {
                                            "active_timer": 3,
                                            "distance_external": 170,
                                            "distance_internal": 90,
                                            "max_hopcount": 100,
                                            "max_path": 16,
                                            "max_variance": 1,
                                        }
                                    },
                                },
                                "cisco": {
                                    "configured_interfaces": [
                                        "GigabitEthernet0/0",
                                        "GigabitEthernet0/1",
                                        "Loopback0",
                                        "Loopback1",
                                        "Loopback2",
                                        "Loopback3",
                                    ],
                                    "eigrp_id": 20,
                                    "metric_weight": {
                                        "k1": 1,
                                        "k2": 0,
                                        "k3": 1,
                                        "k4": 0,
                                        "k5": 0,
                                        "k6": 0,
                                    },
                                    "name": "cisco",
                                    "named_mode": True,
                                    "redistribute": {},
                                    "router_id": "4.4.4.4",
                                    "topology": {
                                        "0": {
                                            "active_timer": 3,
                                            "distance_external": 170,
                                            "distance_internal": 90,
                                            "max_hopcount": 100,
                                            "max_path": 16,
                                            "max_variance": 1,
                                        }
                                    },
                                },
                            }
                        }
                    }
                }
            }
        },
        "ospf": {
            "vrf": {
                "default": {
                    "address_family": {
                        "ipv6": {
                            "instance": {
                                "1": {
                                    "areas": {
                                        0: {
                                            "configured_interfaces": [
                                                "Loopback0",
                                                "Loopback1",
                                                "GigabitEthernet0/0",
                                            ]
                                        }
                                    },
                                    "redistribute": {
                                        "bgp": {"65003": {"include_connected": False}},
                                        "rip": {
                                            "worldskills": {"include_connected": True}
                                        },
                                    },
                                    "router_id": "4.4.4.4",
                                    "total_normal_area": 1,
                                    "total_nssa_area": 0,
                                    "total_stub_area": 0,
                                }
                            }
                        }
                    }
                }
            }
        },
        "rip": {
            "vrf": {
                "default": {
                    "address_family": {
                        "ipv6": {
                            "instance": {
                                "worldskills": {
                                    "configured_interfaces": ["Loopback2"],
                                    "redistribute": {
                                        "bgp": {
                                            "65003": {
                                                "include_connected": False,
                                                "metric": 4,
                                                "route_policy": "test",
                                            }
                                        },
                                        "eigrp": {
                                            "10": {
                                                "include_connected": True,
                                                "metric": 4,
                                            }
                                        },
                                        "ospf": {
                                            "1": {
                                                "include_connected": True,
                                                "metric": 5,
                                            }
                                        },
                                    },
                                }
                            }
                        }
                    }
                }
            }
        },
    }
}


