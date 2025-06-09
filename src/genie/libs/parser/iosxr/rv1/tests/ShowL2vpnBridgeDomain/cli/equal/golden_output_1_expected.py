expected_output = {
    "bridge_group": {
        "VPLS": {
            "bridge_domain": {
                "TEST": {
                    "id": 0,
                    "state": "up",
                    "shg_id": 0,
                    "mst_i": 0,
                    "mac_aging_time": 300,
                    "mac_limit": 64000,
                    "mac_limit_action": "none",
                    "mac_limit_notification": "syslog",
                    "filter_mac_address": 0,
                    "ac": {
                        "num_ac": 1,
                        "num_ac_up": 1,
                        "interfaces": {
                            "Bundle-Ether3": {
                                "state": "up",
                                "static_mac_address": 0
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "TEST": {
                            "state": "up",
                            "neighbor": {
                                "172.16.152.13": {
                                    "pw_id": {
                                        "20161:10090": {
                                            "state": "up",
                                            "static_mac_address": 0
                                        }
                                    }
                                },
                                "172.16.152.67": {
                                    "pw_id": {
                                        "20161:10090": {
                                            "state": "up",
                                            "static_mac_address": 0
                                        }
                                    }
                                },
                                "172.16.154.190": {
                                    "pw_id": {
                                        "20161:10090": {
                                            "state": "up",
                                            "static_mac_address": 0
                                        }
                                    }
                                },
                                "172.16.154.191": {
                                    "pw_id": {
                                        "20161:10090": {
                                            "state": "up",
                                            "static_mac_address": 0
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "pw": {
                        "num_pw": 6,
                        "num_pw_up": 4,
                        "neighbor": {
                            "172.16.154.59": {
                                "pw_id": {
                                    "5966": {
                                        "state": "down",
                                        "static_mac_address": 0
                                    }
                                }
                            },
                            "172.16.154.60": {
                                "pw_id": {
                                    "6066": {
                                        "state": "down",
                                        "static_mac_address": 0
                                    }
                                }
                            }
                        }
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    }
                }
            }
        }
    }
}
