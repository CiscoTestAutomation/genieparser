expected_output = {
    "vfi": {
        "VPLS-2052": {
            "vpn_id": 2052,
            "rd": "65109:2052",
            "type": "multipoint",
            "bd_vfi_name": "VPLS-2052",
            "ve_range": 10,
            "signaling": "BGP",
            "bridge_domain": {
                "2052": {
                    "pseudo_port_interface": "pseudowire100002",
                    "attachment_circuits": {},
                    "vfi": {
                        "10.120.202.64": {
                            "pw_id": {
                                "pseudowire100203": {
                                    "local_label": 26,
                                    "remote_label": 327818,
                                    "ve_id": 1,
                                    "split_horizon": True,
                                }
                            }
                        }
                    },
                }
            },
            "ve_id": 2,
            "rt": ["65109:2052", "65109:2052"],
            "state": "up",
        },
        "VPLS-2055": {
            "vpn_id": 2055,
            "rd": "65109:2055",
            "type": "multipoint",
            "bd_vfi_name": "VPLS-2055",
            "ve_range": 10,
            "signaling": "BGP",
            "bridge_domain": {
                "2055": {
                    "pseudo_port_interface": "pseudowire100005",
                    "attachment_circuits": {},
                    "vfi": {
                        "10.120.202.64": {
                            "pw_id": {
                                "pseudowire100206": {
                                    "local_label": 56,
                                    "remote_label": 327842,
                                    "ve_id": 1,
                                    "split_horizon": True,
                                }
                            }
                        }
                    },
                }
            },
            "ve_id": 2,
            "rt": ["65109:2055", "65109:2055"],
            "state": "up",
        },
        "VPLS-2051": {
            "vpn_id": 2051,
            "rd": "65109:2051",
            "type": "multipoint",
            "bd_vfi_name": "VPLS-2051",
            "ve_range": 10,
            "signaling": "BGP",
            "bridge_domain": {
                "2051": {
                    "pseudo_port_interface": "pseudowire100001",
                    "attachment_circuits": {},
                    "vfi": {
                        "10.120.202.64": {
                            "pw_id": {
                                "pseudowire100202": {
                                    "local_label": 16,
                                    "remote_label": 327810,
                                    "ve_id": 1,
                                    "split_horizon": True,
                                }
                            }
                        }
                    },
                }
            },
            "ve_id": 2,
            "rt": ["65109:2051", "65109:2051"],
            "state": "up",
        },
        "VPLS-2053": {
            "vpn_id": 2053,
            "rd": "65109:2053",
            "type": "multipoint",
            "bd_vfi_name": "VPLS-2053",
            "ve_range": 10,
            "signaling": "BGP",
            "bridge_domain": {
                "2053": {
                    "pseudo_port_interface": "pseudowire100003",
                    "attachment_circuits": {},
                    "vfi": {
                        "10.120.202.64": {
                            "pw_id": {
                                "pseudowire100204": {
                                    "local_label": 36,
                                    "remote_label": 327826,
                                    "ve_id": 1,
                                    "split_horizon": True,
                                }
                            }
                        }
                    },
                }
            },
            "ve_id": 2,
            "rt": ["65109:2053", "65109:2053"],
            "state": "up",
        },
        "VPLS-2054": {
            "vpn_id": 2054,
            "rd": "65109:2054",
            "type": "multipoint",
            "bd_vfi_name": "VPLS-2054",
            "ve_range": 10,
            "signaling": "BGP",
            "bridge_domain": {
                "2054": {
                    "pseudo_port_interface": "pseudowire100004",
                    "attachment_circuits": {},
                    "vfi": {
                        "10.120.202.64": {
                            "pw_id": {
                                "pseudowire100205": {
                                    "local_label": 46,
                                    "remote_label": 327834,
                                    "ve_id": 1,
                                    "split_horizon": True,
                                }
                            }
                        }
                    },
                }
            },
            "ve_id": 2,
            "rt": ["65109:2054", "65109:2054"],
            "state": "up",
        },
    }
}
