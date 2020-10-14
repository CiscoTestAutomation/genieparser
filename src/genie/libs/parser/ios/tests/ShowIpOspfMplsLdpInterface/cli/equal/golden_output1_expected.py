expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "2": {
                            "areas": {
                                "0.0.0.1": {
                                    "interfaces": {
                                        "GigabitEthernet3": {
                                            "mpls": {
                                                "ldp": {
                                                    "autoconfig": False,
                                                    "autoconfig_area_id": "0.0.0.1",
                                                    "holddown_timer": False,
                                                    "igp_sync": False,
                                                    "state": "down",
                                                    "state_info": "pending LDP",
                                                }
                                            }
                                        },
                                        "OSPF_SL1": {
                                            "mpls": {
                                                "ldp": {
                                                    "autoconfig": False,
                                                    "autoconfig_area_id": "0.0.0.1",
                                                    "holddown_timer": False,
                                                    "igp_sync": False,
                                                    "state": "up",
                                                }
                                            }
                                        },
                                    }
                                }
                            },
                            "mpls": {
                                "ldp": {
                                    "autoconfig": False,
                                    "autoconfig_area_id": "0.0.0.1",
                                }
                            },
                        }
                    }
                }
            }
        },
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "1": {
                            "areas": {
                                "0.0.0.0": {
                                    "interfaces": {
                                        "GigabitEthernet1": {
                                            "mpls": {
                                                "ldp": {
                                                    "autoconfig": False,
                                                    "autoconfig_area_id": "0.0.0.0",
                                                    "holddown_timer": False,
                                                    "igp_sync": False,
                                                    "state": "up",
                                                }
                                            }
                                        },
                                        "GigabitEthernet2": {
                                            "mpls": {
                                                "ldp": {
                                                    "autoconfig": False,
                                                    "autoconfig_area_id": "0.0.0.0",
                                                    "holddown_timer": False,
                                                    "igp_sync": False,
                                                    "state": "up",
                                                }
                                            }
                                        },
                                        "TenGigabitEthernet3/0/1": {
                                            "mpls": {
                                                "ldp": {
                                                    "autoconfig": False,
                                                    "autoconfig_area_id": "0.0.0.0",
                                                    "holddown_timer": False,
                                                    "igp_sync": False,
                                                    "state": "down",
                                                }
                                            }
                                        },
                                        "Loopback1": {
                                            "mpls": {
                                                "ldp": {
                                                    "autoconfig": False,
                                                    "autoconfig_area_id": "0.0.0.0",
                                                    "holddown_timer": False,
                                                    "igp_sync": False,
                                                    "state": "up",
                                                }
                                            }
                                        },
                                    }
                                }
                            },
                            "mpls": {
                                "ldp": {
                                    "autoconfig": False,
                                    "autoconfig_area_id": "0.0.0.0",
                                }
                            },
                        }
                    }
                }
            }
        },
    }
}
