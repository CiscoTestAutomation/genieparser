expected_output = {
    "sessions": {
        "IPv4-LSP": {
            "address": {
                "17.17.17.17": {
                    "tun_id": {
                        "15060": {
                            "ext_id": {
                                "141.141.141.141": {
                                    "psbs": 1,
                                    "rsbs": 1,
                                    "requests": 1,
                                    "lsp_id": 5,
                                    "tunnel_name": {
                                        "NHOP_15060_F141-ASR9912_Hu0000_F17-ASR922_Hu0000": {
                                            "rsvp_path_info": {
                                                "inlabel": {
                                                    "interface": "TenGigE0/2/0/0",
                                                    "label": "3",
                                                },
                                                "incoming_address": "99.33.0.1",
                                                "explicit_route": {
                                                    0: {
                                                        "path_status": "Strict",
                                                        "route_address": "99.33.0.1/32",
                                                    },
                                                    1: {
                                                        "path_status": "Strict",
                                                        "route_address": "17.17.17.17/32",
                                                    },
                                                },
                                                "record_route": {
                                                    0: {
                                                        "address": "99.33.0.2",
                                                        "address_flag": "0x0",
                                                    },
                                                    1: {
                                                        "address": "20.51.0.1",
                                                        "address_flag": "0x0",
                                                    },
                                                    2: {
                                                        "address": "27.90.132.57",
                                                        "address_flag": "0x0",
                                                    },
                                                },
                                                "tspec": {
                                                    "avg_rate": 0,
                                                    "burst": 1,
                                                    "burst_unit": "K",
                                                    "peak_rate": 0,
                                                },
                                            },
                                            "rsvp_resv_info": {
                                                "outlabel": {
                                                    "interface": "No intf",
                                                    "label": "No label",
                                                },
                                                "frr_outlabel": {
                                                    "interface": "No intf",
                                                    "label": "No label",
                                                },
                                                "record_route_state": "None",
                                                "fspec": {
                                                    "avg_rate": 0,
                                                    "burst": 1,
                                                    "burst_unit": "K",
                                                    "peak_rate": 0,
                                                },
                                            },
                                        }
                                    },
                                }
                            }
                        },
                        "16370": {
                            "ext_id": {
                                "107.107.107.107": {
                                    "psbs": 1,
                                    "rsbs": 1,
                                    "requests": 1,
                                    "lsp_id": 14,
                                    "tunnel_name": {
                                        "NNHOP_16370_F107-ASR9001_F141-ASR9912_F17-ASR9922": {
                                            "rsvp_path_info": {
                                                "inlabel": {
                                                    "interface": "TenGigE0/2/0/0",
                                                    "label": "3",
                                                },
                                                "incoming_address": "99.33.0.1",
                                                "explicit_route": {
                                                    0: {
                                                        "path_status": "Strict",
                                                        "route_address": "99.33.0.1/32",
                                                    },
                                                    1: {
                                                        "path_status": "Strict",
                                                        "route_address": "17.17.17.17/32",
                                                    },
                                                },
                                                "record_route": {
                                                    0: {
                                                        "address": "99.33.0.2",
                                                        "address_flag": "0x0",
                                                    },
                                                    1: {
                                                        "address": "20.51.0.1",
                                                        "address_flag": "0x0",
                                                    },
                                                },
                                                "tspec": {
                                                    "avg_rate": 0,
                                                    "burst": 1,
                                                    "burst_unit": "K",
                                                    "peak_rate": 0,
                                                },
                                            },
                                            "rsvp_resv_info": {
                                                "outlabel": {
                                                    "interface": "No intf",
                                                    "label": "No label",
                                                },
                                                "frr_outlabel": {
                                                    "interface": "No intf",
                                                    "label": "No label",
                                                },
                                                "record_route_state": "None",
                                                "fspec": {
                                                    "avg_rate": 0,
                                                    "burst": 1,
                                                    "burst_unit": "K",
                                                    "peak_rate": 0,
                                                },
                                            },
                                        }
                                    },
                                }
                            }
                        },
                        "16710": {
                            "ext_id": {
                                "107.107.107.107": {
                                    "psbs": 1,
                                    "rsbs": 1,
                                    "requests": 1,
                                    "lsp_id": 23,
                                    "tunnel_name": {
                                        "NNHOP_16710_F107-ASR9001_F106-ASR9001_F17-ASR9922": {
                                            "rsvp_path_info": {
                                                "inlabel": {
                                                    "interface": "HundredGigE0/0/0/0",
                                                    "label": "3",
                                                },
                                                "incoming_address": "20.50.0.2",
                                                "explicit_route": {
                                                    0: {
                                                        "path_status": "Strict",
                                                        "route_address": "20.50.0.2/32",
                                                    },
                                                    1: {
                                                        "path_status": "Strict",
                                                        "route_address": "17.17.17.17/32",
                                                    },
                                                },
                                                "record_route": {
                                                    0: {
                                                        "address": "20.50.0.1",
                                                        "address_flag": "0x0",
                                                    },
                                                    1: {
                                                        "address": "27.90.132.58",
                                                        "address_flag": "0x0",
                                                    },
                                                },
                                                "tspec": {
                                                    "avg_rate": 0,
                                                    "burst": 1,
                                                    "burst_unit": "K",
                                                    "peak_rate": 0,
                                                },
                                            },
                                            "rsvp_resv_info": {
                                                "outlabel": {
                                                    "interface": "No intf",
                                                    "label": "No label",
                                                },
                                                "frr_outlabel": {
                                                    "interface": "No intf",
                                                    "label": "No label",
                                                },
                                                "record_route_state": "None",
                                                "fspec": {
                                                    "avg_rate": 0,
                                                    "burst": 1,
                                                    "burst_unit": "K",
                                                    "peak_rate": 0,
                                                },
                                            },
                                        }
                                    },
                                }
                            }
                        },
                        "55000": {
                            "ext_id": {
                                "109.109.109.109": {
                                    "psbs": 1,
                                    "rsbs": 1,
                                    "requests": 1,
                                    "lsp_id": 22,
                                    "tunnel_name": {
                                        "55000_F109-ASR9001_F17-ASR9922": {
                                            "rsvp_path_info": {
                                                "inlabel": {
                                                    "interface": "HundredGigE0/0/0/0",
                                                    "label": "3",
                                                },
                                                "incoming_address": "20.50.0.2",
                                                "explicit_route": {
                                                    0: {
                                                        "path_status": "Strict",
                                                        "route_address": "20.50.0.2/32",
                                                    },
                                                    1: {
                                                        "path_status": "Strict",
                                                        "route_address": "17.17.17.17/32",
                                                    },
                                                },
                                                "record_route": {
                                                    0: {
                                                        "address": "20.50.0.1",
                                                        "address_flag": "0x0",
                                                    },
                                                    1: {
                                                        "address": "21.50.0.2",
                                                        "address_flag": "0x0",
                                                    },
                                                },
                                                "tspec": {
                                                    "avg_rate": 0,
                                                    "burst": 1,
                                                    "burst_unit": "K",
                                                    "peak_rate": 0,
                                                },
                                            },
                                            "rsvp_resv_info": {
                                                "outlabel": {
                                                    "interface": "No intf",
                                                    "label": "No label",
                                                },
                                                "frr_outlabel": {
                                                    "interface": "No intf",
                                                    "label": "No label",
                                                },
                                                "record_route_state": "None",
                                                "fspec": {
                                                    "avg_rate": 0,
                                                    "burst": 1,
                                                    "burst_unit": "K",
                                                    "peak_rate": 0,
                                                },
                                            },
                                        }
                                    },
                                }
                            }
                        },
                        "56000": {
                            "ext_id": {
                                "108.108.108.108": {
                                    "psbs": 1,
                                    "rsbs": 1,
                                    "requests": 1,
                                    "lsp_id": 13,
                                    "tunnel_name": {
                                        "56000_F108-ASR9001_F17-ASR9922": {
                                            "rsvp_path_info": {
                                                "inlabel": {
                                                    "interface": "HundredGigE0/0/0/0",
                                                    "label": "3",
                                                },
                                                "incoming_address": "20.50.0.2",
                                                "explicit_route": {
                                                    0: {
                                                        "path_status": "Strict",
                                                        "route_address": "20.50.0.2/32",
                                                    },
                                                    1: {
                                                        "path_status": "Strict",
                                                        "route_address": "17.17.17.17/32",
                                                    },
                                                },
                                                "record_route": {
                                                    0: {
                                                        "address": "20.50.0.1",
                                                        "address_flag": "0x0",
                                                    },
                                                    1: {
                                                        "address": "21.50.0.2",
                                                        "address_flag": "0x0",
                                                    },
                                                    2: {
                                                        "address": "37.25.0.2",
                                                        "address_flag": "0x0",
                                                    },
                                                },
                                                "tspec": {
                                                    "avg_rate": 0,
                                                    "burst": 1,
                                                    "burst_unit": "K",
                                                    "peak_rate": 0,
                                                },
                                            },
                                            "rsvp_resv_info": {
                                                "outlabel": {
                                                    "interface": "No intf",
                                                    "label": "No label",
                                                },
                                                "frr_outlabel": {
                                                    "interface": "No intf",
                                                    "label": "No label",
                                                },
                                                "record_route_state": "None",
                                                "fspec": {
                                                    "avg_rate": 0,
                                                    "burst": 1,
                                                    "burst_unit": "K",
                                                    "peak_rate": 0,
                                                },
                                            },
                                        }
                                    },
                                }
                            }
                        },
                    }
                }
            }
        }
    }
}
