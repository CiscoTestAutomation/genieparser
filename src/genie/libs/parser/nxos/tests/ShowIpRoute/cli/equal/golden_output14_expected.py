expected_output ={
    "vrf": {
        "tn-L2-PBR:vrf-L2-PBR": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "192.168.1.0/24": {
                            "route": "192.168.1.0/24",
                            "active": True,
                            "ubest": 1,
                            "mbest": 0,
                            "attached": True,
                            "direct": True,
                            "pervasive": True,
                            "metric": 0,
                            "route_preference": 1,
                            "tag": 4294967294,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.11.200.98",
                                        "source_protocol": "static",
                                        "best_ucast_nexthop": True,
                                        "updated": "02w00d",
                                        "next_hop_vrf": "overlay-1",
                                        "metric": 0,
                                        "route_preference": 1,
                                    }
                                }
                            },
                            "source_protocol": "static",
                        },
                        "192.168.1.1/32": {
                            "route": "192.168.1.1/32",
                            "active": True,
                            "ubest": 1,
                            "mbest": 0,
                            "attached": True,
                            "pervasive": True,
                            "metric": 0,
                            "route_preference": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "192.168.1.1",
                                        "source_protocol": "local",
                                        "source_protocol_status": "local",
                                        "best_ucast_nexthop": True,
                                        "updated": "02w00d",
                                        "outgoing_interface": "Vlan60",
                                        "metric": 0,
                                        "route_preference": 0,
                                    }
                                }
                            },
                            "source_protocol": "local",
                            "source_protocol_status": "local",
                        },
                        "192.168.100.0/24": {
                            "route": "192.168.100.0/24",
                            "active": True,
                            "ubest": 1,
                            "mbest": 0,
                            "attached": True,
                            "direct": True,
                            "pervasive": True,
                            "metric": 0,
                            "route_preference": 1,
                            "tag": 4294967294,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.11.200.98",
                                        "source_protocol": "static",
                                        "best_ucast_nexthop": True,
                                        "updated": "02w00d",
                                        "next_hop_vrf": "overlay-1",
                                        "metric": 0,
                                        "route_preference": 1,
                                    }
                                }
                            },
                            "source_protocol": "static",
                        },
                        "192.168.100.1/32": {
                            "route": "192.168.100.1/32",
                            "active": True,
                            "ubest": 1,
                            "mbest": 0,
                            "attached": True,
                            "pervasive": True,
                            "metric": 0,
                            "route_preference": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "192.168.100.1",
                                        "source_protocol": "local",
                                        "source_protocol_status": "local",
                                        "best_ucast_nexthop": True,
                                        "updated": "02w00d",
                                        "outgoing_interface": "Vlan14",
                                        "metric": 0,
                                        "route_preference": 0,
                                    }
                                }
                            },
                            "source_protocol": "local",
                            "source_protocol_status": "local",
                        },
                        "192.168.254.0/24": {
                            "route": "192.168.254.0/24",
                            "active": True,
                            "ubest": 1,
                            "mbest": 0,
                            "attached": True,
                            "direct": True,
                            "pervasive": True,
                            "metric": 0,
                            "route_preference": 1,
                            "tag": 4294967294,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.11.200.98",
                                        "source_protocol": "static",
                                        "best_ucast_nexthop": True,
                                        "updated": "02w00d",
                                        "next_hop_vrf": "overlay-1",
                                        "metric": 0,
                                        "route_preference": 1,
                                    }
                                }
                            },
                            "source_protocol": "static",
                        },
                        "192.168.254.1/32": {
                            "route": "192.168.254.1/32",
                            "active": True,
                            "ubest": 1,
                            "mbest": 0,
                            "attached": True,
                            "pervasive": True,
                            "metric": 0,
                            "route_preference": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "192.168.254.1",
                                        "source_protocol": "local",
                                        "source_protocol_status": "local",
                                        "best_ucast_nexthop": True,
                                        "updated": "02w00d",
                                        "outgoing_interface": "Vlan39",
                                        "metric": 0,
                                        "route_preference": 0,
                                    }
                                }
                            },
                            "source_protocol": "local",
                            "source_protocol_status": "local",
                        },
                    }
                }
            }
        }
    }
}
