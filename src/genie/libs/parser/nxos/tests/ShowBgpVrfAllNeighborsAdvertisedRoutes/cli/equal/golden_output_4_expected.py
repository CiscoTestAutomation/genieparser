expected_output = {
    "vrf": {
        "default": {
            "neighbor": {
                "10.2.56.11": {
                    "address_family": {
                        "ipv4 unicast": {
                            "advertised": {
                                "10.10.0.1/32": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "path_type": "l",
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "i",
                                            "weight": 32768,
                                            "locprf": 100
                                        }
                                    }
                                },
                                "10.10.0.2/32": {
                                    "index": {
                                        1: {
                                            "next_hop": "10.10.1.1",
                                            "origin_codes": "i",
                                            "status_codes": "x ",
                                            "path_type": "e",
                                            "weight": 0,
                                            "path": "64101 64002"
                                        },
                                        2: {
                                            "status_codes": "x ",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102 64002"
                                        }
                                    }
                                },
                                "10.10.0.101/32": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "next_hop": "10.10.1.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64101"
                                        }
                                    }
                                },
                                "10.10.0.102/32": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102"
                                        }
                                    }
                                },
                                "10.10.0.201/32": {
                                    "index": {
                                        1: {
                                            "next_hop": "10.10.1.1",
                                            "origin_codes": "i",
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "weight": 0,
                                            "path": "64101 64201"
                                        },
                                        2: {
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102 64201"
                                        }
                                    }
                                },
                                "10.10.0.202/32": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102 64202"
                                        }
                                    }
                                },
                                "10.10.1.0/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "path_type": "l",
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "i",
                                            "weight": 32768,
                                            "locprf": 100
                                        },
                                        2: {
                                            "next_hop": "10.10.1.1",
                                            "origin_codes": "i",
                                            "status_codes": "*>",
                                            "path_type": "l",
                                            "weight": 0,
                                            "path": "64101"
                                        }
                                    }
                                },
                                "10.10.1.4/30": {
                                    "index": {
                                        1: {
                                            "next_hop": "10.10.1.1",
                                            "origin_codes": "i",
                                            "status_codes": "x ",
                                            "path_type": "e",
                                            "weight": 0,
                                            "path": "64101"
                                        },
                                        2: {
                                            "status_codes": "x ",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102 64002"
                                        }
                                    }
                                },
                                "10.10.2.0/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "path_type": "l",
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "i",
                                            "weight": 32768,
                                            "locprf": 100
                                        },
                                        2: {
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "status_codes": "*>",
                                            "path_type": "l",
                                            "weight": 0,
                                            "path": "64102"
                                        }
                                    }
                                },
                                "10.10.2.4/30": {
                                    "index": {
                                        1: {
                                            "next_hop": "10.10.1.1",
                                            "origin_codes": "i",
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "weight": 0,
                                            "path": "64101 64002"
                                        },
                                        2: {
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102"
                                        }
                                    }
                                },
                                "10.10.101.0/30": {
                                    "index": {
                                        1: {
                                            "next_hop": "10.10.1.1",
                                            "origin_codes": "i",
                                            "status_codes": "* ",
                                            "path_type": "e",
                                            "weight": 0,
                                            "path": "64101"
                                        },
                                        2: {
                                            "status_codes": "* ",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102 64201"
                                        }
                                    }
                                },
                                "10.10.101.4/30": {
                                    "index": {
                                        1: {
                                            "next_hop": "10.10.1.1",
                                            "origin_codes": "i",
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "weight": 0,
                                            "path": "64101 64201"
                                        },
                                        2: {
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102"
                                        }
                                    }
                                },
                                "10.10.102.0/30": {
                                    "index": {
                                        1: {
                                            "next_hop": "10.10.1.1",
                                            "origin_codes": "i",
                                            "status_codes": "* ",
                                            "path_type": "e",
                                            "weight": 0,
                                            "path": "64101"
                                        },
                                        2: {
                                            "status_codes": "* ",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102 64202"
                                        }
                                    }
                                },
                                "10.10.102.4/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102"
                                        }
                                    }
                                },
                                "10.10.150.0/24": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "path_type": "l",
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "i",
                                            "weight": 32768,
                                            "locprf": 100
                                        }
                                    }
                                },
                                "10.10.151.0/24": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "path_type": "l",
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "i",
                                            "weight": 32768,
                                            "locprf": 100
                                        }
                                    }
                                },
                                "10.10.152.0/24": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "path_type": "l",
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "i",
                                            "weight": 32768,
                                            "locprf": 100
                                        }
                                    }
                                },
                                "10.10.160.0/24": {
                                    "index": {
                                        1: {
                                            "next_hop": "10.10.1.1",
                                            "origin_codes": "i",
                                            "status_codes": "x ",
                                            "path_type": "e",
                                            "weight": 0,
                                            "path": "64101 64002"
                                        },
                                        2: {
                                            "status_codes": "x ",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102 64002"
                                        }
                                    }
                                },
                                "10.10.161.0/24": {
                                    "index": {
                                        1: {
                                            "next_hop": "10.10.1.1",
                                            "origin_codes": "i",
                                            "status_codes": "x ",
                                            "path_type": "e",
                                            "weight": 0,
                                            "path": "64101 64002"
                                        },
                                        2: {
                                            "status_codes": "x ",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102 64002"
                                        }
                                    }
                                },
                                "10.10.162.0/24": {
                                    "index": {
                                        1: {
                                            "next_hop": "10.10.1.1",
                                            "origin_codes": "i",
                                            "status_codes": "x ",
                                            "path_type": "e",
                                            "weight": 0,
                                            "path": "64101 64002"
                                        },
                                        2: {
                                            "status_codes": "x ",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102 64002"
                                        }
                                    }
                                },
                                "10.10.201.0/30": {
                                    "index": {
                                        1: {
                                            "next_hop": "10.10.1.1",
                                            "origin_codes": "i",
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "weight": 0,
                                            "path": "64101 64201"
                                        },
                                        2: {
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102 64201"
                                        }
                                    }
                                },
                                "10.10.202.0/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102 64202"
                                        }
                                    }
                                },
                                "100.100.100.100/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "path_type": "l",
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "i",
                                            "weight": 32768,
                                            "locprf": 100
                                        }
                                    }
                                },
                                "100.100.100.104/30": {
                                    "index": {
                                        1: {
                                            "next_hop": "10.10.1.1",
                                            "origin_codes": "i",
                                            "status_codes": "x ",
                                            "path_type": "e",
                                            "weight": 0,
                                            "path": "64101 64002"
                                        },
                                        2: {
                                            "status_codes": "x ",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102 64002"
                                        }
                                    }
                                },
                                "100.100.100.108/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102 {64201 64202}"
                                        }
                                    }
                                },
                                "100.100.100.112/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102 {64201 64202} 64203"
                                        }
                                    }
                                },
                                "100.100.100.114/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102 {64201 64202} 64203 64500.2345"
                                        }
                                    }
                                },
                                "100.100.100.116/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "{64102 64201 64202} 64203 64500.2345"
                                        }
                                    }
                                },
                                "100.100.100.118/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "64102.444 {64201 64202} 64203 64500.2345"
                                        }
                                    }
                                },
                                "100.100.100.120/30": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "path_type": "e",
                                            "next_hop": "10.10.2.1",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "{64102.333 64201 64202} 64203 64500.2345"
                                        }
                                    }
                                }
                            },
                            "bgp_table_version": 325050,
                            "local_router_id": "10.2.12.2"
                        }
                    }
                }
            }
        }
    }
}