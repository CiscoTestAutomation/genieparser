expected_output = {
    "lisp_router_instances": {
        0: {
            "service": {
                "ipv4": {
                    "map_server": {
                        "virtual_network_ids": {
                            "101": {
                                "extranets": {
                                    "ext1": {
                                        "extranet": "ext1",
                                        "home_instance_id": 103,
                                        "subscriber": {
                                            "192.168.0.0/24": {
                                                "bidirectional": True,
                                                "eid_record": "192.168.0.0/24",
                                            },
                                            "192.168.9.0/24": {
                                                "bidirectional": True,
                                                "eid_record": "192.168.9.0/24",
                                            },
                                        },
                                    }
                                },
                                "vni": "101",
                            },
                            "102": {
                                "extranets": {
                                    "ext1": {
                                        "extranet": "ext1",
                                        "home_instance_id": 103,
                                        "subscriber": {
                                            "172.16.1.0/24": {
                                                "bidirectional": True,
                                                "eid_record": "172.16.1.0/24",
                                            }
                                        },
                                    }
                                },
                                "vni": "102",
                            },
                            "103": {
                                "extranets": {
                                    "ext1": {
                                        "extranet": "ext1",
                                        "home_instance_id": 103,
                                        "provider": {
                                            "10.220.100.0/24": {
                                                "bidirectional": True,
                                                "eid_record": "10.220.100.0/24",
                                            },
                                            "192.168.195.0/24": {
                                                "bidirectional": True,
                                                "eid_record": "192.168.195.0/24",
                                            },
                                            "10.121.88.0/24": {
                                                "bidirectional": True,
                                                "eid_record": "10.121.88.0/24",
                                            },
                                        },
                                    }
                                },
                                "vni": "103",
                            },
                            "total_extranet_entries": 6,
                        }
                    }
                }
            }
        }
    }
}
