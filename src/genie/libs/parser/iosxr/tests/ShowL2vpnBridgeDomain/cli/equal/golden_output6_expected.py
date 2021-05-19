expected_output = {
    "bridge_group": {
        "GTT_DIP": {
            "bridge_domain": {
                "GPF-CID-2723": {
                    "id": 45,
                    "state": "up",
                    "shg_id": 0,
                    "mst_i": 0,
                    "mac_aging_time": 300,
                    "mac_limit": 4000,
                    "mac_limit_action": "none",
                    "mac_limit_notification": "syslog",
                    "filter_mac_address": 0,
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "Bundle-Ether53.2723": {
                                "state": "up",
                                "static_mac_address": 0,
                            },
                            "TenGigabitEthernet0/2/0/3.2723": {
                                "state": "up",
                                "static_mac_address": 0,
                            },
                        },
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "GPF-CID01": {
                            "state": "up",
                            "neighbor": {
                                "172.16.74.2": {
                                    "pw_id": {
                                        2723: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.70.3": {
                                    "pw_id": {
                                        2723: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.70.6": {
                                    "pw_id": {
                                        2723: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.70.7": {
                                    "pw_id": {
                                        2723: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.70.8": {
                                    "pw_id": {
                                        2723: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.70.12": {
                                    "pw_id": {
                                        2723: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.71.14": {
                                    "pw_id": {
                                        2723: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.74.15": {
                                    "pw_id": {
                                        2723: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.70.17": {
                                    "pw_id": {
                                        2723: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.74.20": {
                                    "pw_id": {
                                        2723: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.71.26": {
                                    "pw_id": {
                                        2723: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.74.26": {
                                    "pw_id": {
                                        2723: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.70.160": {
                                    "pw_id": {
                                        2723: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                                "172.16.70.165": {
                                    "pw_id": {
                                        2723: {"state": "up", "static_mac_address": 0}
                                    }
                                },
                            },
                        },
                    },
                    "pw": {"num_pw": 14, "num_pw_up": 14},
                    "pbb": {"num_pbb": 0, "num_pbb_up": 0},
                    "vni": {"num_vni": 0, "num_vni_up": 0},
                },
                "BPI-DIP196-BD": {
                    "id": 46,
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
                            "Bundle-Ether53.196": {
                                "state": "up",
                                "static_mac_address": 0,
                            }
                        },
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "BPI196-VFI01": {
                            "state": "up",
                            "neighbor": {
                                "172.16.70.160": {
                                    "pw_id": {
                                        196: {"state": "up", "static_mac_address": 0}
                                    }
                                }
                            },
                        },
                    },
                    "pw": {"num_pw": 1, "num_pw_up": 1},
                    "pbb": {"num_pbb": 0, "num_pbb_up": 0},
                    "vni": {"num_vni": 0, "num_vni_up": 0},
                },
            }
        }
    }
}
