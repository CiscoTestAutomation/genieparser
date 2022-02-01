expected_output = {
    "tag": {
        "1": {
            "topo_type": {
                "unicast": {
                    "topo_name": "base topology",
                    "mtid": "0",
                    "topo_id": "0x0",
                    "level": {
                        "1": {
                            "prefix": {
                                "12.1.0.0": {
                                    "mask_len": 24,
                                    "route_type": "connected",
                                    "metric": 10,
                                    "external": False,
                                    "interarea": False,
                                    "isis": False
                                },
                                "22.22.22.22": {
                                    "mask_len": 32,
                                    "route_type": "connected",
                                    "metric": 10,
                                    "external": False,
                                    "interarea": False,
                                    "isis": False,
                                    "algo": {
                                        0: {
                                            "index": 22,
                                            "p_flag": False,
                                            "r_flag": False,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True
                                        },
                                        1: {
                                            "index": 202,
                                            "p_flag": False,
                                            "r_flag": False,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True
                                        },
                                        129: {
                                            "index": 122,
                                            "p_flag": False,
                                            "r_flag": False,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True,
                                            "map_type": "0x1",
                                            "pfx_metric": 0,
                                            "advertise": False
                                        },
                                        150: {
                                            "index": 222,
                                            "p_flag": False,
                                            "r_flag": False,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True,
                                            "map_type": "0x1",
                                            "pfx_metric": 0,
                                            "advertise": False
                                        },
                                        190: {
                                            "index": 290,
                                            "p_flag": False,
                                            "r_flag": False,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True,
                                            "map_type": "0x1",
                                            "pfx_metric": 0,
                                            "advertise": False
                                        },
                                        200: {
                                            "index": 322,
                                            "p_flag": False,
                                            "r_flag": False,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True,
                                            "map_type": "0x1",
                                            "pfx_metric": 0,
                                            "advertise": False
                                        }
                                    },
                                    "x_flag": False,
                                    "r_flag": False,
                                    "n_flag": True,
                                    "src_rtr_id": "22.22.22.22"
                                },
                                "24.1.0.0": {
                                    "mask_len": 24,
                                    "route_type": "connected",
                                    "metric": 10,
                                    "external": False,
                                    "interarea": False,
                                    "isis": False
                                }
                            }
                        },
                        "2": {
                            "prefix": {
                                "1.1.1.1": {
                                    "mask_len": 32,
                                    "route_type": "isis",
                                    "metric": 20,
                                    "external": False,
                                    "interarea": False,
                                    "isis": True,
                                    "algo": {
                                        0: {
                                            "index": 11,
                                            "p_flag": True,
                                            "r_flag": True,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True
                                        },
                                        1: {
                                            "index": 101,
                                            "p_flag": True,
                                            "r_flag": True,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True
                                        },
                                        129: {
                                            "index": 111,
                                            "p_flag": False,
                                            "r_flag": False,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True,
                                            "map_type": "0x0",
                                            "pfx_metric": 20,
                                            "advertise": False
                                        },
                                        150: {
                                            "index": 211,
                                            "p_flag": False,
                                            "r_flag": False,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True,
                                            "map_type": "0x0",
                                            "pfx_metric": 20,
                                            "advertise": False
                                        },
                                        200: {
                                            "index": 201,
                                            "p_flag": False,
                                            "r_flag": False,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True,
                                            "map_type": "0x0",
                                            "pfx_metric": 20,
                                            "advertise": False
                                        }
                                    },
                                    "x_flag": False,
                                    "r_flag": True,
                                    "n_flag": True,
                                    "src_rtr_id": "1.1.1.1"
                                },
                                "12.1.0.0": {
                                    "mask_len": 24,
                                    "route_type": "connected",
                                    "metric": 10,
                                    "external": False,
                                    "interarea": False,
                                    "isis": False
                                },
                                "12.3.0.0": {
                                    "mask_len": 24,
                                    "route_type": "isis",
                                    "metric": 20,
                                    "external": False,
                                    "interarea": False,
                                    "isis": False,
                                    "x_flag": False,
                                    "r_flag": True,
                                    "n_flag": False
                                },
                                "13.1.0.0": {
                                    "mask_len": 24,
                                    "route_type": "isis",
                                    "metric": 20,
                                    "external": False,
                                    "interarea": False,
                                    "isis": False,
                                    "x_flag": False,
                                    "r_flag": True,
                                    "n_flag": False
                                },
                                "22.22.22.22": {
                                    "mask_len": 32,
                                    "route_type": "connected",
                                    "metric": 10,
                                    "external": False,
                                    "interarea": False,
                                    "isis": False,
                                    "algo": {
                                        0: {
                                            "index": 22,
                                            "p_flag": False,
                                            "r_flag": False,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True
                                        },
                                        1: {
                                            "index": 202,
                                            "p_flag": False,
                                            "r_flag": False,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True
                                        },
                                        129: {
                                            "index": 122,
                                            "p_flag": False,
                                            "r_flag": False,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True,
                                            "map_type": "0x1",
                                            "pfx_metric": 0,
                                            "advertise": False
                                        },
                                        150: {
                                            "index": 222,
                                            "p_flag": False,
                                            "r_flag": False,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True,
                                            "map_type": "0x1",
                                            "pfx_metric": 0,
                                            "advertise": False
                                        },
                                        190: {
                                            "index": 290,
                                            "p_flag": False,
                                            "r_flag": False,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True,
                                            "map_type": "0x1",
                                            "pfx_metric": 0,
                                            "advertise": False
                                        },
                                        200: {
                                            "index": 322,
                                            "p_flag": False,
                                            "r_flag": False,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True,
                                            "map_type": "0x1",
                                            "pfx_metric": 0,
                                            "advertise": False
                                        }
                                    },
                                    "x_flag": False,
                                    "r_flag": False,
                                    "n_flag": True,
                                    "src_rtr_id": "22.22.22.22"
                                },
                                "24.1.0.0": {
                                    "mask_len": 24,
                                    "route_type": "connected",
                                    "metric": 10,
                                    "external": False,
                                    "interarea": False,
                                    "isis": False
                                },
                                "24.2.0.0": {
                                    "mask_len": 24,
                                    "route_type": "connected",
                                    "metric": 0,
                                    "external": True,
                                    "interarea": False,
                                    "isis": False
                                },
                                "44.44.44.44": {
                                    "mask_len": 32,
                                    "route_type": "isis",
                                    "metric": 0,
                                    "external": True,
                                    "interarea": False,
                                    "isis": False,
                                    "algo": {
                                        0: {
                                            "index": 44,
                                            "p_flag": True,
                                            "r_flag": True,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": False
                                        },
                                        1: {
                                            "index": 404,
                                            "p_flag": True,
                                            "r_flag": True,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": False
                                        },
                                        200: {
                                            "index": 204,
                                            "p_flag": True,
                                            "r_flag": True,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": False,
                                            "map_type": "0x0",
                                            "pfx_metric": 20,
                                            "advertise": False
                                        }
                                    },
                                    "x_flag": True,
                                    "r_flag": False,
                                    "n_flag": False
                                },
                                "45.2.0.0": {
                                    "mask_len": 24,
                                    "route_type": "isis",
                                    "metric": 0,
                                    "external": True,
                                    "interarea": False,
                                    "isis": False,
                                    "x_flag": True,
                                    "r_flag": False,
                                    "n_flag": False
                                }
                            }
                        }
                    }
                }
            }
        },
        "2": {
            "topo_type": {
                "unicast": {
                    "topo_name": "base topology",
                    "mtid": "0",
                    "topo_id": "0x0",
                    "level": {
                        "1": {
                            "prefix": {
                                "12.2.0.0": {
                                    "mask_len": 24,
                                    "route_type": "connected",
                                    "metric": 10,
                                    "external": False,
                                    "interarea": False,
                                    "isis": False
                                },
                                "24.2.0.0": {
                                    "mask_len": 24,
                                    "route_type": "connected",
                                    "metric": 10,
                                    "external": False,
                                    "interarea": False,
                                    "isis": False
                                }
                            }
                        },
                        "2": {
                            "prefix": {
                                "12.2.0.0": {
                                    "mask_len": 24,
                                    "route_type": "connected",
                                    "metric": 10,
                                    "external": False,
                                    "interarea": False,
                                    "isis": False
                                },
                                "24.2.0.0": {
                                    "mask_len": 24,
                                    "route_type": "connected",
                                    "metric": 10,
                                    "external": False,
                                    "interarea": False,
                                    "isis": False
                                },
                                "44.44.44.44": {
                                    "mask_len": 32,
                                    "route_type": "isis",
                                    "metric": 20,
                                    "external": False,
                                    "interarea": False,
                                    "isis": True,
                                    "algo": {
                                        0: {
                                            "index": 44,
                                            "p_flag": True,
                                            "r_flag": True,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True
                                        },
                                        1: {
                                            "index": 404,
                                            "p_flag": True,
                                            "r_flag": True,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True
                                        },
                                        160: {
                                            "index": 344,
                                            "p_flag": False,
                                            "r_flag": False,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True,
                                            "map_type": "0x0",
                                            "pfx_metric": 20,
                                            "advertise": False
                                        },
                                        200: {
                                            "index": 204,
                                            "p_flag": False,
                                            "r_flag": False,
                                            "v_flag": False,
                                            "e_flag": False,
                                            "l_flag": False,
                                            "n_flag": True,
                                            "map_type": "0x0",
                                            "pfx_metric": 20,
                                            "advertise": False
                                        }
                                    },
                                    "x_flag": False,
                                    "r_flag": True,
                                    "n_flag": True
                                },
                                "45.2.0.0": {
                                    "mask_len": 24,
                                    "route_type": "isis",
                                    "metric": 20,
                                    "external": False,
                                    "interarea": False,
                                    "isis": False,
                                    "x_flag": False,
                                    "r_flag": True,
                                    "n_flag": False
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

