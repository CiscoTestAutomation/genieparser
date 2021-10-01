

expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "64577": {
                            "areas": {
                                "0.0.0.0": {
                                    "mpls": {
                                        "te": {
                                            "area_instance": 13,
                                            "enable": True,
                                            "link_fragments": {
                                                1: {
                                                    "affinity_bit": "0x100000",
                                                    "extended_admin_groups": {
                                                        1: {"value": 0,},
                                                        2: {"value": 0,},
                                                        3: {"value": 0,},
                                                        4: {"value": 0,},
                                                        5: {"value": 0,},
                                                        6: {"value": 0,},
                                                        7: {"value": 0,},
                                                    },
                                                    "interface_address": "172.16.1.216",
                                                    "link_id": "10.154.219.75",
                                                    "link_instance": 13,
                                                    "maximum_bandwidth": 1250000000,
                                                    "maximum_reservable_bandwidth": 2985974784,
                                                    "network_type": "point-to-point",
                                                    "out_interface_id": 40,
                                                    "te_admin_metric": 65535,
                                                    "total_extended_admin_group": 8,
                                                    "total_priority": 8,
                                                    "unreserved_bandwidths": {
                                                        "0 1492987392": {
                                                            "priority": 0,
                                                            "unreserved_bandwidth": 1492987392,
                                                        },
                                                        "0 2985974784": {
                                                            "priority": 0,
                                                            "unreserved_bandwidth": 2985974784,
                                                        },
                                                        "1 1492987392": {
                                                            "priority": 1,
                                                            "unreserved_bandwidth": 1492987392,
                                                        },
                                                        "1 2985974784": {
                                                            "priority": 1,
                                                            "unreserved_bandwidth": 2985974784,
                                                        },
                                                        "2 1492987392": {
                                                            "priority": 2,
                                                            "unreserved_bandwidth": 1492987392,
                                                        },
                                                        "2 2985974784": {
                                                            "priority": 2,
                                                            "unreserved_bandwidth": 2985974784,
                                                        },
                                                        "3 1492987392": {
                                                            "priority": 3,
                                                            "unreserved_bandwidth": 1492987392,
                                                        },
                                                        "3 2985974784": {
                                                            "priority": 3,
                                                            "unreserved_bandwidth": 2985974784,
                                                        },
                                                        "4 1492987392": {
                                                            "priority": 4,
                                                            "unreserved_bandwidth": 1492987392,
                                                        },
                                                        "4 2985974784": {
                                                            "priority": 4,
                                                            "unreserved_bandwidth": 2985974784,
                                                        },
                                                        "5 1492987392": {
                                                            "priority": 5,
                                                            "unreserved_bandwidth": 1492987392,
                                                        },
                                                        "5 2985974784": {
                                                            "priority": 5,
                                                            "unreserved_bandwidth": 2985974784,
                                                        },
                                                        "6 1492987392": {
                                                            "priority": 6,
                                                            "unreserved_bandwidth": 1492987392,
                                                        },
                                                        "6 2985974784": {
                                                            "priority": 6,
                                                            "unreserved_bandwidth": 2985974784,
                                                        },
                                                        "7 1492987392": {
                                                            "priority": 7,
                                                            "unreserved_bandwidth": 1492987392,
                                                        },
                                                        "7 2985974784": {
                                                            "priority": 7,
                                                            "unreserved_bandwidth": 2985974784,
                                                        },
                                                    },
                                                },
                                            },
                                            "total_links": 9,
                                        },
                                    },
                                },
                            },
                            "mpls": {"te": {"router_id": "10.154.219.96",},},
                        },
                    },
                },
            },
        },
    },
}
