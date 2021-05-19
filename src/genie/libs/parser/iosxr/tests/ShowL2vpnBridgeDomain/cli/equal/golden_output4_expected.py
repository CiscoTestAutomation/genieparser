expected_output = {
    "bridge_group": {
        "GTT_DIP": {
            "bridge_domain": {
                "SOL-GUYANA-DIP168-BD": {
                    "id": 79,
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
                            "Bundle-Ether47.168": {
                                "state": "up",
                                "static_mac_address": 0,
                            }
                        },
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "SOL-GUYANA-VFI01": {
                            "state": "up",
                            "neighbor": {
                                "172.16.74.13": {
                                    "pw_id": {
                                        168: {"state": "up", "static_mac_address": 0}
                                    }
                                }
                            },
                        },
                    },
                    "pw": {"num_pw": 1, "num_pw_up": 1},
                    "pbb": {"num_pbb": 0, "num_pbb_up": 0},
                    "vni": {"num_vni": 0, "num_vni_up": 0},
                }
            }
        },
        "DSL_PUBLIC": {
            "bridge_domain": {
                "DSL_KWAKWANI": {
                    "id": 265,
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
                        "interfaces": {"BV24": {"state": "up", "bvi_mac_address": 1}},
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "DSL_KWAKNI": {
                            "state": "up",
                            "neighbor": {
                                "172.16.74.15": {
                                    "pw_id": {
                                        24: {"state": "up", "static_mac_address": 0}
                                    }
                                }
                            },
                        },
                    },
                    "pw": {"num_pw": 1, "num_pw_up": 1},
                    "pbb": {"num_pbb": 0, "num_pbb_up": 0},
                    "vni": {"num_vni": 0, "num_vni_up": 0},
                }
            }
        },
        "IPLC-MIAMI": {
            "bridge_domain": {
                "NEUTRONA1505": {
                    "id": 106,
                    "state": "up",
                    "shg_id": 0,
                    "mst_i": 0,
                    "mac_aging_time": 300,
                    "mac_limit": 4000,
                    "mac_limit_action": "none",
                    "mac_limit_notification": "syslog",
                    "filter_mac_address": 0,
                    "ac": {
                        "num_ac": 3,
                        "num_ac_up": 3,
                        "interfaces": {
                            "Bundle-Ether101.1505": {
                                "state": "up",
                                "static_mac_address": 0,
                            },
                            "Bundle-Ether15.1505": {
                                "state": "up",
                                "static_mac_address": 0,
                            },
                            "Bundle-Ether53.1505": {
                                "state": "up",
                                "static_mac_address": 0,
                            },
                        },
                    },
                    "vfi": {"num_vfi": 0},
                    "pw": {
                        "num_pw": 0,
                        "num_pw_up": 0,
                        "neighbor": {
                            "172.16.74.13": {
                                "pw_id": {168: {"state": "up", "static_mac_address": 0}}
                            }
                        },
                    },
                    "pbb": {"num_pbb": 0, "num_pbb_up": 0},
                    "vni": {"num_vni": 0, "num_vni_up": 0},
                }
            }
        },
    }
}
