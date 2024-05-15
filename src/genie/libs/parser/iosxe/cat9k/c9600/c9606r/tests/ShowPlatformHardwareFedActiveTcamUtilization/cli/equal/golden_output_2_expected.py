expected_output = {
    "asic": {
        "0": {
            "table": {
                "mac_address_table": {
                    "subtype": {
                        "em": {
                            "dir": {
                                "i": {
                                    "max": 32768,
                                    "used": 31,
                                    "used_percent": "0.09%",
                                    "v4": 0,
                                    "v6": 0,
                                    "mpls": 0,
                                    "other": 31
                                }
                            }
                        },
                        "tcam": {
                            "dir": {
                                "i": {
                                    "max": 768,
                                    "used": 22,
                                    "used_percent": "2.86%",
                                    "v4": 0,
                                    "v6": 0,
                                    "mpls": 0,
                                    "other": 22
                                }
                            }
                        }
                    }
                },
                "l3_multicast": {
                    "subtype": {
                        "em": {
                            "dir": {
                                "i": {
                                    "max": 32768,
                                    "used": 0,
                                    "used_percent": "0.00%",
                                    "v4": 0,
                                    "v6": 0,
                                    "mpls": 0,
                                    "other": 0
                                }
                            }
                        },
                        "tcam": {
                            "dir": {
                                "i": {
                                    "max": 768,
                                    "used": 6,
                                    "used_percent": "0.78%",
                                    "v4": 3,
                                    "v6": 3,
                                    "mpls": 0,
                                    "other": 0
                                }
                            }
                        }
                    }
                },
                "l2_multicast": {
                    "subtype": {
                        "tcam": {
                            "dir": {
                                "i": {
                                    "max": 2304,
                                    "used": 7,
                                    "used_percent": "0.30%",
                                    "v4": 3,
                                    "v6": 4,
                                    "mpls": 0,
                                    "other": 0
                                }
                            }
                        }
                    }
                },
                "ip_route_table": {
                    "subtype": {
                        "em_lpm": {
                            "dir": {
                                "i": {
                                    "max": 212992,
                                    "used": 13,
                                    "used_percent": "0.01%",
                                    "v4": 13,
                                    "v6": 0,
                                    "mpls": 0,
                                    "other": 0
                                }
                            }
                        },
                        "tcam": {
                            "dir": {
                                "i": {
                                    "max": 1536,
                                    "used": 20,
                                    "used_percent": "1.30%",
                                    "v4": 14,
                                    "v6": 3,
                                    "mpls": 3,
                                    "other": 0
                                }
                            }
                        }
                    }
                },
                "qos_acl_ipv4": {
                    "subtype": {
                        "tcam": {
                            "dir": {
                                "i": {
                                    "max": 5632,
                                    "used": 15,
                                    "used_percent": "0.27%",
                                    "v4": 15,
                                    "v6": 0,
                                    "mpls": 0,
                                    "other": 0
                                },
                                "o": {
                                    "max": 6144,
                                    "used": 13,
                                    "used_percent": "0.21%",
                                    "v4": 13,
                                    "v6": 0,
                                    "mpls": 0,
                                    "other": 0
                                }
                            }
                        }
                    }
                },
                "qos_acl_non_ipv4": {
                    "subtype": {
                        "tcam": {
                            "dir": {
                                "i": {
                                    "max": 2560,
                                    "used": 30,
                                    "used_percent": "1.17%",
                                    "v4": 0,
                                    "v6": 20,
                                    "mpls": 0,
                                    "other": 10
                                },
                                "o": {
                                    "max": 2048,
                                    "used": 27,
                                    "used_percent": "1.32%",
                                    "v4": 0,
                                    "v6": 18,
                                    "mpls": 0,
                                    "other": 9
                                }
                            }
                        }
                    }
                },
                "security_acl_ipv4": {
                    "subtype": {
                        "tcam": {
                            "dir": {
                                "i": {
                                    "max": 7168,
                                    "used": 12,
                                    "used_percent": "0.17%",
                                    "v4": 12,
                                    "v6": 0,
                                    "mpls": 0,
                                    "other": 0
                                },
                                "o": {
                                    "max": 7168,
                                    "used": 14,
                                    "used_percent": "0.20%",
                                    "v4": 14,
                                    "v6": 0,
                                    "mpls": 0,
                                    "other": 0
                                }
                            }
                        }
                    }
                },
                "security_acl_non_ipv4": {
                    "subtype": {
                        "tcam": {
                            "dir": {
                                "i": {
                                    "max": 5120,
                                    "used": 76,
                                    "used_percent": "1.48%",
                                    "v4": 0,
                                    "v6": 36,
                                    "mpls": 0,
                                    "other": 40
                                },
                                "o": {
                                    "max": 8192,
                                    "used": 29,
                                    "used_percent": "0.35%",
                                    "v4": 0,
                                    "v6": 24,
                                    "mpls": 0,
                                    "other": 5
                                }
                            }
                        }
                    }
                },
                "netflow_acl": {
                    "subtype": {
                        "tcam": {
                            "dir": {
                                "i": {
                                    "max": 512,
                                    "used": 6,
                                    "used_percent": "1.17%",
                                    "v4": 2,
                                    "v6": 2,
                                    "mpls": 0,
                                    "other": 2
                                },
                                "o": {
                                    "max": 512,
                                    "used": 6,
                                    "used_percent": "1.17%",
                                    "v4": 2,
                                    "v6": 2,
                                    "mpls": 0,
                                    "other": 2
                                }
                            }
                        }
                    }
                },
                "pbr_acl": {
                    "subtype": {
                        "tcam": {
                            "dir": {
                                "i": {
                                    "max": 3072,
                                    "used": 54,
                                    "used_percent": "1.76%",
                                    "v4": 38,
                                    "v6": 16,
                                    "mpls": 0,
                                    "other": 0
                                }
                            }
                        }
                    }
                },
                "flow_span_acl": {
                    "subtype": {
                        "tcam": {
                            "dir": {
                                "i": {
                                    "max": 512,
                                    "used": 4,
                                    "used_percent": "0.78%",
                                    "v4": 1,
                                    "v6": 2,
                                    "mpls": 0,
                                    "other": 1
                                },
                                "o": {
                                    "max": 512,
                                    "used": 4,
                                    "used_percent": "0.78%",
                                    "v4": 1,
                                    "v6": 2,
                                    "mpls": 0,
                                    "other": 1
                                }
                            }
                        }
                    }
                },
                "control_plane": {
                    "subtype": {
                        "tcam": {
                            "dir": {
                                "i": {
                                    "max": 512,
                                    "used": 283,
                                    "used_percent": "55.27%",
                                    "v4": 130,
                                    "v6": 106,
                                    "mpls": 0,
                                    "other": 47
                                }
                            }
                        }
                    }
                },
                "tunnel_termination": {
                    "subtype": {
                        "tcam": {
                            "dir": {
                                "i": {
                                    "max": 2816,
                                    "used": 33,
                                    "used_percent": "1.17%",
                                    "v4": 12,
                                    "v6": 20,
                                    "mpls": 0,
                                    "other": 1
                                }
                            }
                        }
                    }
                },
                "lisp_inst_mapping": {
                    "subtype": {
                        "tcam": {
                            "dir": {
                                "i": {
                                    "max": 2048,
                                    "used": 1,
                                    "used_percent": "0.05%",
                                    "v4": 0,
                                    "v6": 0,
                                    "mpls": 0,
                                    "other": 1
                                }
                            }
                        }
                    }
                },
                "security_association": {
                    "subtype": {
                        "tcam": {
                            "dir": {
                                "i": {
                                    "max": 512,
                                    "used": 4,
                                    "used_percent": "0.78%",
                                    "v4": 2,
                                    "v6": 2,
                                    "mpls": 0,
                                    "other": 0
                                }
                            }
                        }
                    }
                },
                "cts_cell_matrix_vpn_label": {
                    "subtype": {
                        "em": {
                            "dir": {
                                "o": {
                                    "max": 32768,
                                    "used": 0,
                                    "used_percent": "0.00%",
                                    "v4": 0,
                                    "v6": 0,
                                    "mpls": 0,
                                    "other": 0
                                }
                            }
                        },
                        "tcam": {
                            "dir": {
                                "o": {
                                    "max": 768,
                                    "used": 1,
                                    "used_percent": "0.13%",
                                    "v4": 0,
                                    "v6": 0,
                                    "mpls": 0,
                                    "other": 1
                                }
                            }
                        }
                    }
                },
                "client_table": {
                    "subtype": {
                        "em": {
                            "dir": {
                                "i": {
                                    "max": 8192,
                                    "used": 0,
                                    "used_percent": "0.00%",
                                    "v4": 0,
                                    "v6": 0,
                                    "mpls": 0,
                                    "other": 0
                                }
                            }
                        },
                        "tcam": {
                            "dir": {
                                "i": {
                                    "max": 512,
                                    "used": 0,
                                    "used_percent": "0.00%",
                                    "v4": 0,
                                    "v6": 0,
                                    "mpls": 0,
                                    "other": 0
                                }
                            }
                        }
                    }
                },
                "input_group_le": {
                    "subtype": {
                        "tcam": {
                            "dir": {
                                "i": {
                                    "max": 1024,
                                    "used": 0,
                                    "used_percent": "0.00%",
                                    "v4": 0,
                                    "v6": 0,
                                    "mpls": 0,
                                    "other": 0
                                }
                            }
                        }
                    }
                },
                "output_group_le": {
                    "subtype": {
                        "tcam": {
                            "dir": {
                                "o": {
                                    "max": 1024,
                                    "used": 0,
                                    "used_percent": "0.00%",
                                    "v4": 0,
                                    "v6": 0,
                                    "mpls": 0,
                                    "other": 0
                                }
                            }
                        }
                    }
                },
                "macsec_spd": {
                    "subtype": {
                        "tcam": {
                            "dir": {
                                "i": {
                                    "max": 256,
                                    "used": 2,
                                    "used_percent": "0.78%",
                                    "v4": 0,
                                    "v6": 0,
                                    "mpls": 0,
                                    "other": 2
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
