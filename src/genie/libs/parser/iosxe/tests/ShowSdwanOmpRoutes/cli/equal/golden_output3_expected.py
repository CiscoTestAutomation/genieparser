expected_output = {
    "vrf": {
        "10": {
            "prefixes": {
                "0.0.0.0/0": {
                    "prefix": "0.0.0.0/0",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "453",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.131",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "549",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.131",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.0.0.0/8": {
                    "prefix": "10.0.0.0/8",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "1540",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "1541",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                3: {
                                    "index": 3,
                                    "path_id": "1588",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "1503",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "1504",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                3: {
                                    "index": 3,
                                    "path_id": "1607",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.9.0.0/16": {
                    "prefix": "10.9.0.0/16",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "553",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "554",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "569",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "570",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.10.10.0/24": {
                    "prefix": "10.10.10.0/24",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "1271",
                                    "label": "1002",
                                    "status": [
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.10",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "1272",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.10",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                3: {
                                    "index": 3,
                                    "path_id": "1449",
                                    "label": "1002",
                                    "status": [
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.11",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "516",
                                    "label": "1002",
                                    "status": [
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.10",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "517",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.10",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                3: {
                                    "index": 3,
                                    "path_id": "1209",
                                    "label": "1002",
                                    "status": [
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.11",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.16.23.56/29": {
                    "prefix": "10.16.23.56/29",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "411",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.86",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "321",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.86",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.30.0.0/30": {
                    "prefix": "10.30.0.0/30",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "207",
                                    "label": "1007",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.30",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "737",
                                    "label": "1007",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.30",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "359",
                                    "label": "1007",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.30",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "743",
                                    "label": "1007",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.30",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.30.0.12/30": {
                    "prefix": "10.30.0.12/30",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "279",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.31",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "353",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.31",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.30.10.0/24": {
                    "prefix": "10.30.10.0/24",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "280",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.31",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "353",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.31",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.31.23.56/29": {
                    "prefix": "10.31.23.56/29",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "5",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.88",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "5",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.88",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.40.0.0/30": {
                    "prefix": "10.40.0.0/30",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "1137",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.40",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "941",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.40",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.40.0.8/30": {
                    "prefix": "10.40.0.8/30",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "1476",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.40",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "1161",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.40",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.40.10.0/24": {
                    "prefix": "10.40.10.0/24",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "1492",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.40",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "1175",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.40",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.50.0.0/30": {
                    "prefix": "10.50.0.0/30",
                    "tenant": "0",
                    "from_peer": {
                        "0.0.0.0": {
                            "peer": "0.0.0.0",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "66",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "Red",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.50",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "68",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "Red",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.50",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.50.0.12/30": {
                    "prefix": "10.50.0.12/30",
                    "tenant": "0",
                    "from_peer": {
                        "0.0.0.0": {
                            "peer": "0.0.0.0",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "66",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "Red",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.50",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "68",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "Red",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.50",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "537",
                                    "label": "1002",
                                    "status": [
                                        "Inv",
                                        "U"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.51",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "267",
                                    "label": "1002",
                                    "status": [
                                        "Inv",
                                        "U"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.51",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.50.5.0/24": {
                    "prefix": "10.50.5.0/24",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "5",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.130",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "5",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.130",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.50.10.0/24": {
                    "prefix": "10.50.10.0/24",
                    "tenant": "0",
                    "from_peer": {
                        "0.0.0.0": {
                            "peer": "0.0.0.0",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "66",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "Red",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.50",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "68",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "Red",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.50",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "1265",
                                    "label": "1002",
                                    "status": [
                                        "Inv",
                                        "U"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.51",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "478",
                                    "label": "1002",
                                    "status": [
                                        "Inv",
                                        "U"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.51",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.100.10.0/24": {
                    "prefix": "10.100.10.0/24",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "1545",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "1546",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                3: {
                                    "index": 3,
                                    "path_id": "1593",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "1512",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "1513",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                3: {
                                    "index": 3,
                                    "path_id": "1616",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "172.16.253.0/24": {
                    "prefix": "172.16.253.0/24",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "678",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "775",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "172.16.253.20/30": {
                    "prefix": "172.16.253.20/30",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "677",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "777",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "172.16.253.24/30": {
                    "prefix": "172.16.253.24/30",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "676",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "777",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "172.16.253.28/30": {
                    "prefix": "172.16.253.28/30",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "553",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "554",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "568",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "569",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "172.16.253.32/30": {
                    "prefix": "172.16.253.32/30",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "555",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "556",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "568",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "569",
                                    "label": "1002",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "192.168.6.0/24": {
                    "prefix": "192.168.6.0/24",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "577",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.131",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "613",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.131",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "192.168.9.0/24": {
                    "prefix": "192.168.9.0/24",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "978",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.131",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "1035",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.131",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                }
            }
        },
        "30": {
            "prefixes": {
                "10.0.0.0/8": {
                    "prefix": "10.0.0.0/8",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "366",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "367",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                3: {
                                    "index": 3,
                                    "path_id": "398",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "375",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "376",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                3: {
                                    "index": 3,
                                    "path_id": "421",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.10.30.0/24": {
                    "prefix": "10.10.30.0/24",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "328",
                                    "label": "1003",
                                    "status": [
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.10",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "329",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.10",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                3: {
                                    "index": 3,
                                    "path_id": "378",
                                    "label": "1003",
                                    "status": [
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.11",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "127",
                                    "label": "1003",
                                    "status": [
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.10",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "128",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.10",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                3: {
                                    "index": 3,
                                    "path_id": "196",
                                    "label": "1003",
                                    "status": [
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.11",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.30.0.4/30": {
                    "prefix": "10.30.0.4/30",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "35",
                                    "label": "1009",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.30",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "127",
                                    "label": "1009",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.30",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "94",
                                    "label": "1009",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.30",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "128",
                                    "label": "1009",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.30",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.30.0.16/30": {
                    "prefix": "10.30.0.16/30",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "19",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.31",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "57",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.31",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.30.30.0/24": {
                    "prefix": "10.30.30.0/24",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "19",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.31",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "57",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.31",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.50.0.4/30": {
                    "prefix": "10.50.0.4/30",
                    "tenant": "0",
                    "from_peer": {
                        "0.0.0.0": {
                            "peer": "0.0.0.0",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "66",
                                    "label": "1005",
                                    "status": [
                                        "C",
                                        "Red",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.50",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "68",
                                    "label": "1005",
                                    "status": [
                                        "C",
                                        "Red",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.50",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.50.0.16/30": {
                    "prefix": "10.50.0.16/30",
                    "tenant": "0",
                    "from_peer": {
                        "0.0.0.0": {
                            "peer": "0.0.0.0",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "66",
                                    "label": "1005",
                                    "status": [
                                        "C",
                                        "Red",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.50",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "68",
                                    "label": "1005",
                                    "status": [
                                        "C",
                                        "Red",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.50",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "87",
                                    "label": "1003",
                                    "status": [
                                        "Inv",
                                        "U"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.51",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "61",
                                    "label": "1003",
                                    "status": [
                                        "Inv",
                                        "U"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.51",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.50.30.0/24": {
                    "prefix": "10.50.30.0/24",
                    "tenant": "0",
                    "from_peer": {
                        "0.0.0.0": {
                            "peer": "0.0.0.0",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "66",
                                    "label": "1005",
                                    "status": [
                                        "C",
                                        "Red",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.50",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "68",
                                    "label": "1005",
                                    "status": [
                                        "C",
                                        "Red",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.50",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "184",
                                    "label": "1003",
                                    "status": [
                                        "Inv",
                                        "U"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.51",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "116",
                                    "label": "1003",
                                    "status": [
                                        "Inv",
                                        "U"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.51",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.100.30.0/24": {
                    "prefix": "10.100.30.0/24",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "366",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "367",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                3: {
                                    "index": 3,
                                    "path_id": "398",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "375",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "376",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                3: {
                                    "index": 3,
                                    "path_id": "421",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "172.16.253.0/24": {
                    "prefix": "172.16.253.0/24",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "365",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "366",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                3: {
                                    "index": 3,
                                    "path_id": "397",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "375",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "376",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                3: {
                                    "index": 3,
                                    "path_id": "420",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "172.16.253.52/30": {
                    "prefix": "172.16.253.52/30",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "163",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "205",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "172.16.253.56/30": {
                    "prefix": "172.16.253.56/30",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "340",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "337",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.100",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "172.16.253.60/30": {
                    "prefix": "172.16.253.60/30",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "138",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "139",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "148",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "149",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "172.16.253.64/30": {
                    "prefix": "172.16.253.64/30",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "177",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "178",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "214",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "215",
                                    "label": "1003",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.101",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                }
            }
        },
        "40": {
            "prefixes": {
                "10.10.40.0/24": {
                    "prefix": "10.10.40.0/24",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "176",
                                    "label": "1004",
                                    "status": [
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.10",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "177",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.10",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                3: {
                                    "index": 3,
                                    "path_id": "190",
                                    "label": "1004",
                                    "status": [
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.11",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "63",
                                    "label": "1004",
                                    "status": [
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.10",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "64",
                                    "label": "1004",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.10",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                3: {
                                    "index": 3,
                                    "path_id": "84",
                                    "label": "1004",
                                    "status": [
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.11",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.30.0.8/30": {
                    "prefix": "10.30.0.8/30",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "17",
                                    "label": "1010",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.30",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "73",
                                    "label": "1010",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.30",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "50",
                                    "label": "1010",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.30",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "60",
                                    "label": "1010",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.30",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.30.0.20/30": {
                    "prefix": "10.30.0.20/30",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "9",
                                    "label": "1005",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.31",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "30",
                                    "label": "1005",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.31",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.30.40.0/24": {
                    "prefix": "10.30.40.0/24",
                    "tenant": "0",
                    "from_peer": {
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "9",
                                    "label": "1005",
                                    "status": [
                                        "C",
                                        "I",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.31",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "30",
                                    "label": "1005",
                                    "status": [
                                        "C",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.31",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.50.0.8/30": {
                    "prefix": "10.50.0.8/30",
                    "tenant": "0",
                    "from_peer": {
                        "0.0.0.0": {
                            "peer": "0.0.0.0",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "66",
                                    "label": "1006",
                                    "status": [
                                        "C",
                                        "Red",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.50",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "68",
                                    "label": "1006",
                                    "status": [
                                        "C",
                                        "Red",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.50",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.50.0.20/30": {
                    "prefix": "10.50.0.20/30",
                    "tenant": "0",
                    "from_peer": {
                        "0.0.0.0": {
                            "peer": "0.0.0.0",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "66",
                                    "label": "1006",
                                    "status": [
                                        "C",
                                        "Red",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.50",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "68",
                                    "label": "1006",
                                    "status": [
                                        "C",
                                        "Red",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.50",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "45",
                                    "label": "1004",
                                    "status": [
                                        "Inv",
                                        "U"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.51",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "34",
                                    "label": "1004",
                                    "status": [
                                        "Inv",
                                        "U"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.51",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                },
                "10.50.40.0/24": {
                    "prefix": "10.50.40.0/24",
                    "tenant": "0",
                    "from_peer": {
                        "0.0.0.0": {
                            "peer": "0.0.0.0",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "66",
                                    "label": "1006",
                                    "status": [
                                        "C",
                                        "Red",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.50",
                                    "color": "mpls",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                },
                                2: {
                                    "index": 2,
                                    "path_id": "68",
                                    "label": "1006",
                                    "status": [
                                        "C",
                                        "Red",
                                        "R"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.50",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.4": {
                            "peer": "1.1.1.4",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "99",
                                    "label": "1004",
                                    "status": [
                                        "Inv",
                                        "U"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.51",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        },
                        "1.1.1.5": {
                            "peer": "1.1.1.5",
                            "path_list": {
                                1: {
                                    "index": 1,
                                    "path_id": "63",
                                    "label": "1004",
                                    "status": [
                                        "Inv",
                                        "U"
                                    ],
                                    "attr_type": "installed",
                                    "tloc_ip": "10.255.255.51",
                                    "color": "biz-internet",
                                    "encap": "ipsec",
                                    "preference": "-",
                                    "affinity": "None",
                                    "region_id": "None",
                                    "region_path": "-"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}