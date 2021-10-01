expected_output = {
    "sessions": {
        "IPv4-LSP": {
            "address": {
                "109.109.109.109": {
                    "tun_id": {
                        "50000": {
                            "ext_id": {
                                "17.17.17.17": {
                                    "psbs": 1,
                                    "rsbs": 1,
                                    "requests": 0,
                                    "lsp_id": 15,
                                    "tunnel_name": {
                                        "50000_F17-ASR9922_F109-ASR9001": {
                                            "rsvp_path_info": {
                                                "inlabel": {
                                                    "interface": "No intf",
                                                    "label": "No label",
                                                },
                                                "incoming_address": "Unknown",
                                                "explicit_route": {
                                                    0: {
                                                        "path_status": "Strict",
                                                        "route_address": "20.50.0.1/32",
                                                    },
                                                    1: {
                                                        "path_status": "Strict",
                                                        "route_address": "21.50.0.2/32",
                                                    },
                                                    2: {
                                                        "path_status": "Strict",
                                                        "route_address": "109.109.109.109/32",
                                                    },
                                                },
                                                "record_route_state": "None",
                                                "tspec": {
                                                    "avg_rate": 0,
                                                    "burst": 1,
                                                    "burst_unit": "K",
                                                    "peak_rate": 0,
                                                },
                                            },
                                            "rsvp_resv_info": {
                                                "outlabel": {
                                                    "interface": "HundredGigE0/0/0/0",
                                                    "label": "24023",
                                                },
                                                "frr_outlabel": {
                                                    "interface": "Tunnel-te53300",
                                                    "label": "3",
                                                },
                                                "record_route": {
                                                    0: {
                                                        "address": "141.141.141.141",
                                                        "address_flag": "0x21",
                                                    },
                                                    1: {
                                                        "label": "24023",
                                                        "label_flag": "0x1",
                                                    },
                                                    2: {
                                                        "address": "20.50.0.1",
                                                        "address_flag": "0x1",
                                                    },
                                                    3: {
                                                        "label": "24023",
                                                        "label_flag": "0x1",
                                                    },
                                                    4: {
                                                        "address": "109.109.109.109",
                                                        "address_flag": "0x20",
                                                    },
                                                    5: {
                                                        "label": "3",
                                                        "label_flag": "0x1",
                                                    },
                                                    6: {
                                                        "address": "21.50.0.2",
                                                        "address_flag": "0x0",
                                                    },
                                                    7: {
                                                        "label": "3",
                                                        "label_flag": "0x1",
                                                    },
                                                },
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
                        }
                    }
                }
            }
        }
    }
}
