expected_output = {
    "bridge_group": {
        "GTT_DIP": {
            "bridge_domain": {
                "EXXON903DIP": {
                    "id": 244,
                    "state": "up",
                    "shg_id": 0,
                    "mst_i": 0,
                    "mac_aging_time": 300,
                    "mac_limit": 4000,
                    "mac_limit_action": "none",
                    "mac_limit_notification": "syslog",
                    "filter_mac_address": 0,
                    "ac": {
                        "num_ac": 1,
                        "num_ac_up": 1,
                        "interfaces": {
                            "GigabitEthernet0/0/1/10.903": {
                                "state": "up",
                                "static_mac_address": 0,
                            }
                        },
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "EXXON902DIP-04": {
                            "state": "up",
                            "neighbor": {
                                "172.16.75.4": {
                                    "pw_id": {
                                        903: {"state": "down", "static_mac_address": 0}
                                    }
                                }
                            },
                        },
                    },
                    "pw": {"num_pw": 1, "num_pw_up": 0},
                    "pbb": {"num_pbb": 0, "num_pbb_up": 0},
                    "vni": {"num_vni": 0, "num_vni_up": 0},
                },
                "EXXON904DIP": {
                    "id": 243,
                    "state": "up",
                    "shg_id": 0,
                    "mst_i": 0,
                    "mac_aging_time": 300,
                    "mac_limit": 4000,
                    "mac_limit_action": "none",
                    "mac_limit_notification": "syslog",
                    "filter_mac_address": 0,
                    "ac": {
                        "num_ac": 1,
                        "num_ac_up": 1,
                        "interfaces": {
                            "GigabitEthernet0/0/1/10.904": {
                                "state": "up",
                                "static_mac_address": 0,
                            }
                        },
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "EXXON899DIP-04": {
                            "state": "up",
                            "neighbor": {
                                "172.16.75.8": {
                                    "pw_id": {
                                        904: {"state": "up", "static_mac_address": 0}
                                    }
                                }
                            },
                        },
                    },
                    "pw": {"num_pw": 1, "num_pw_up": 1},
                    "pbb": {"num_pbb": 0, "num_pbb_up": 0},
                    "vni": {"num_vni": 0, "num_vni_up": 0},
                },
                "Gafoors-DIP": {
                    "id": 40,
                    "state": "up",
                    "shg_id": 0,
                    "mst_i": 0,
                    "mac_aging_time": 300,
                    "mac_limit": 4000,
                    "mac_limit_action": "none",
                    "mac_limit_notification": "syslog",
                    "filter_mac_address": 0,
                    "ac": {
                        "num_ac": 1,
                        "num_ac_up": 1,
                        "interfaces": {
                            "Bundle-Ether47.744": {
                                "state": "up",
                                "static_mac_address": 0,
                            }
                        },
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "Gafoors-DIP-VFI01": {
                            "state": "up",
                            "neighbor": {
                                "172.16.74.1": {
                                    "pw_id": {
                                        744: {"state": "down", "static_mac_address": 0}
                                    }
                                },
                                "172.16.70.4": {
                                    "pw_id": {
                                        744: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.70.7": {
                                    "pw_id": {
                                        744: {"state": "down", "static_mac_address": 0}
                                    }
                                },
                                "172.16.70.8": {
                                    "pw_id": {
                                        744: {"state": "down", "static_mac_address": 0}
                                    }
                                },
                                "172.16.71.16": {
                                    "pw_id": {
                                        744: {"state": "down", "static_mac_address": 0}
                                    }
                                },
                            },
                        },
                    },
                    "pw": {"num_pw": 5, "num_pw_up": 1},
                    "pbb": {"num_pbb": 0, "num_pbb_up": 0},
                    "vni": {"num_vni": 0, "num_vni_up": 0},
                },
                "CAMEX-DIP-BD": {
                    "id": 42,
                    "state": "up",
                    "shg_id": 0,
                    "mst_i": 0,
                    "mac_aging_time": 300,
                    "mac_limit": 4000,
                    "mac_limit_action": "none",
                    "mac_limit_notification": "syslog",
                    "filter_mac_address": 0,
                    "ac": {
                        "num_ac": 4,
                        "num_ac_up": 3,
                        "interfaces": {
                            "Bundle-Ether44.742": {
                                "state": "down",
                                "static_mac_address": 0,
                            },
                            "Bundle-Ether45.742": {
                                "state": "up",
                                "static_mac_address": 0,
                            },
                            "GigabitEthernet0/0/1/10.742": {
                                "state": "up",
                                "static_mac_address": 0,
                            },
                            "TenGigabitEthernet0/2/0/3.742": {
                                "state": "up",
                                "static_mac_address": 0,
                            },
                        },
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "VRF1": {
                            "state": "up",
                            "neighbor": {
                                "172.16.70.6": {
                                    "pw_id": {
                                        742: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.70.7": {
                                    "pw_id": {
                                        742: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.70.12": {
                                    "pw_id": {
                                        742: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.71.16": {
                                    "pw_id": {
                                        742: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.70.160": {
                                    "pw_id": {
                                        742: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                            },
                        },
                    },
                    "pw": {"num_pw": 5, "num_pw_up": 5},
                    "pbb": {"num_pbb": 0, "num_pbb_up": 0},
                    "vni": {"num_vni": 0, "num_vni_up": 0},
                },
                "CEVONS-L2VPN": {
                    "id": 264,
                    "state": "up",
                    "shg_id": 0,
                    "mst_i": 0,
                    "mac_aging_time": 300,
                    "mac_limit": 4000,
                    "mac_limit_action": "none",
                    "mac_limit_notification": "syslog",
                    "filter_mac_address": 0,
                    "ac": {
                        "num_ac": 1,
                        "num_ac_up": 1,
                        "interfaces": {
                            "Bundle-Ether53.752": {
                                "state": "up",
                                "static_mac_address": 0,
                            }
                        },
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "CEVONS-L2VPN-VFI01": {
                            "state": "up",
                            "neighbor": {
                                "172.16.77.1": {
                                    "pw_id": {
                                        752: {"state": "up", "static_mac_address": 0}
                                    }
                                }
                            },
                        },
                    },
                    "pw": {"num_pw": 1, "num_pw_up": 1},
                    "pbb": {"num_pbb": 0, "num_pbb_up": 0},
                    "vni": {"num_vni": 0, "num_vni_up": 0},
                },
                "EBD-MXK-MGMT": {
                    "id": 43,
                    "state": "up",
                    "shg_id": 0,
                    "mst_i": 0,
                    "mac_aging_time": 300,
                    "mac_limit": 4000,
                    "mac_limit_action": "none",
                    "mac_limit_notification": "syslog",
                    "filter_mac_address": 0,
                    "ac": {
                        "num_ac": 1,
                        "num_ac_up": 1,
                        "interfaces": {"BV990": {"state": "up", "bvi_mac_address": 1}},
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "EBD-MXK-MGMT": {
                            "state": "up",
                            "neighbor": {
                                "172.16.74.6": {
                                    "pw_id": {
                                        990: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.74.7": {
                                    "pw_id": {
                                        990: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                            },
                        },
                    },
                    "pw": {"num_pw": 2, "num_pw_up": 2},
                    "pbb": {"num_pbb": 0, "num_pbb_up": 0},
                    "vni": {"num_vni": 0, "num_vni_up": 0},
                },
            }
        }
    }
}


