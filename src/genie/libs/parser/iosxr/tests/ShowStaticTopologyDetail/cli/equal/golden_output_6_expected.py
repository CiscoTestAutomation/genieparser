expected_output  = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "safi": "unicast",
                    "table_id": "0xe0000000",
                    "routes": {
                        "10.248.4.16/32": {
                            "route": "10.248.4.16/32",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Bundle-Ether100": {
                                        "outgoing_interface": "Bundle-Ether100",
                                        "metrics": 1,
                                        "preference": 1,
                                        "local_label": "No label",
                                        "active": True,
                                        "path_event": "Path is installed into RIB at May  1 22:10:34.079",
                                        "path_version": 1,
                                        "path_status": "0x21",
                                        "tag": 0
                                    }
                                }
                            }
                        },
                        "10.248.4.18/32": {
                            "route": "10.248.4.18/32",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Bundle-Ether200": {
                                        "outgoing_interface": "Bundle-Ether200",
                                        "metrics": 1,
                                        "preference": 1,
                                        "local_label": "No label",
                                        "active": True,
                                        "path_event": "Path is installed into RIB at May  1 22:11:04.487",
                                        "path_version": 1,
                                        "path_status": "0x21",
                                        "tag": 0
                                    }
                                }
                            }
                        },
                        "10.252.252.31/32": {
                            "route": "10.252.252.31/32",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "1.1.1.1",
                                        "metrics": 1,
                                        "preference": 5,
                                        "local_label": "No label",
                                        "active": False,
                                        "path_event": "Path is configured at May  1 22:04:12.804",
                                        "path_version": 0,
                                        "path_status": "0x0"
                                    }
                                }
                            }
                        },
                        "10.255.255.224/32": {
                            "route": "10.255.255.224/32",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "1.3.2.1",
                                        "metrics": 1,
                                        "preference": 10,
                                        "local_label": "No label",
                                        "active": True,
                                        "path_event": "Path is installed into RIB at May  1 22:06:22.240",
                                        "path_version": 1,
                                        "path_status": "0x21",
                                        "tag": 0
                                    }
                                }
                            }
                        },
                        "10.255.255.253/32": {
                            "route": "10.255.255.253/32",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Bundle-Ether5.507": {
                                        "outgoing_interface": "Bundle-Ether5.507",
                                        "metrics": 1,
                                        "preference": 1,
                                        "local_label": "No label",
                                        "active": False,
                                        "path_event": "Path is configured at May  1 22:04:12.804",
                                        "path_version": 0,
                                        "path_status": "0x0"
                                    },
                                    "Bundle-Ether5.506": {
                                        "outgoing_interface": "Bundle-Ether5.506",
                                        "metrics": 1,
                                        "preference": 1,
                                        "local_label": "No label",
                                        "active": False,
                                        "path_event": "Path is configured at May  1 22:04:12.804",
                                        "path_version": 0,
                                        "path_status": "0x0"
                                    }
                                }
                            }
                        },
                        "10.255.255.240/28": {
                            "route": "10.255.255.240/28",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Bundle-Ether5.507": {
                                        "outgoing_interface": "Bundle-Ether5.507",
                                        "metrics": 1,
                                        "preference": 1,
                                        "local_label": "No label",
                                        "active": False,
                                        "path_event": "Path is configured at May  1 22:04:12.804",
                                        "path_version": 0,
                                        "path_status": "0x0"
                                    },
                                    "Bundle-Ether5.506": {
                                        "outgoing_interface": "Bundle-Ether5.506",
                                        "metrics": 1,
                                        "preference": 1,
                                        "local_label": "No label",
                                        "active": False,
                                        "path_event": "Path is configured at May  1 22:04:12.804",
                                        "path_version": 0,
                                        "path_status": "0x0"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}