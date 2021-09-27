
expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "1": {
                            "areas": {
                                "0.0.0.0": {
                                    "mpls": {
                                        "te": {
                                            "area_instance": 2,
                                            "enable": True,
                                            "link_fragments": {
                                                1: {
                                                    "affinity_bit": "0",
                                                    "extended_admin_groups": {
                                                        0: {"value": 0},
                                                        1: {"value": 0},
                                                        2: {"value": 0},
                                                        3: {"value": 0},
                                                        4: {"value": 0},
                                                        5: {"value": 0},
                                                        6: {"value": 0},
                                                        7: {"value": 0},
                                                    },
                                                    "interface_address": "10.3.4.3",
                                                    "link_id": "10.3.4.4",
                                                    "link_instance": 2,
                                                    "maximum_bandwidth": 125000000,
                                                    "maximum_reservable_bandwidth": 93750000,
                                                    "network_type": "broadcast",
                                                    "out_interface_id": 4,
                                                    "te_admin_metric": 1,
                                                    "total_extended_admin_group": 8,
                                                    "total_priority": 8,
                                                    "unreserved_bandwidths": {
                                                        "0 93750000": {
                                                            "priority": 0,
                                                            "unreserved_bandwidth": 93750000,
                                                        },
                                                        "1 93750000": {
                                                            "priority": 1,
                                                            "unreserved_bandwidth": 93750000,
                                                        },
                                                        "2 93750000": {
                                                            "priority": 2,
                                                            "unreserved_bandwidth": 93750000,
                                                        },
                                                        "3 93750000": {
                                                            "priority": 3,
                                                            "unreserved_bandwidth": 93750000,
                                                        },
                                                        "4 93750000": {
                                                            "priority": 4,
                                                            "unreserved_bandwidth": 93750000,
                                                        },
                                                        "5 93750000": {
                                                            "priority": 5,
                                                            "unreserved_bandwidth": 93750000,
                                                        },
                                                        "6 93750000": {
                                                            "priority": 6,
                                                            "unreserved_bandwidth": 93750000,
                                                        },
                                                        "7 93750000": {
                                                            "priority": 7,
                                                            "unreserved_bandwidth": 93750000,
                                                        },
                                                    },
                                                },
                                                2: {
                                                    "affinity_bit": "0",
                                                    "extended_admin_groups": {
                                                        0: {"value": 0},
                                                        1: {"value": 0},
                                                        2: {"value": 0},
                                                        3: {"value": 0},
                                                        4: {"value": 0},
                                                        5: {"value": 0},
                                                        6: {"value": 0},
                                                        7: {"value": 0},
                                                    },
                                                    "interface_address": "10.2.3.3",
                                                    "link_id": "10.2.3.3",
                                                    "link_instance": 2,
                                                    "maximum_bandwidth": 125000000,
                                                    "maximum_reservable_bandwidth": 93750000,
                                                    "network_type": "broadcast",
                                                    "out_interface_id": 6,
                                                    "te_admin_metric": 1,
                                                    "total_extended_admin_group": 8,
                                                    "total_priority": 8,
                                                    "unreserved_bandwidths": {
                                                        "0 93750000": {
                                                            "priority": 0,
                                                            "unreserved_bandwidth": 93750000,
                                                        },
                                                        "1 93750000": {
                                                            "priority": 1,
                                                            "unreserved_bandwidth": 93750000,
                                                        },
                                                        "2 93750000": {
                                                            "priority": 2,
                                                            "unreserved_bandwidth": 93750000,
                                                        },
                                                        "3 93750000": {
                                                            "priority": 3,
                                                            "unreserved_bandwidth": 93750000,
                                                        },
                                                        "4 93750000": {
                                                            "priority": 4,
                                                            "unreserved_bandwidth": 93750000,
                                                        },
                                                        "5 93750000": {
                                                            "priority": 5,
                                                            "unreserved_bandwidth": 93750000,
                                                        },
                                                        "6 93750000": {
                                                            "priority": 6,
                                                            "unreserved_bandwidth": 93750000,
                                                        },
                                                        "7 93750000": {
                                                            "priority": 7,
                                                            "unreserved_bandwidth": 93750000,
                                                        },
                                                    },
                                                },
                                            },
                                            "total_links": 2,
                                        }
                                    }
                                },
                                "0.0.0.1": {"mpls": {"te": {"enable": False}}},
                            },
                            "mpls": {"te": {"router_id": "10.36.3.3"}},
                        }
                    }
                }
            }
        }
    }
}

