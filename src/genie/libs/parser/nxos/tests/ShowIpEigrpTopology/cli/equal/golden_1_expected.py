expected_output = {
    "as": {
        1: {
            "routerid": "10.0.0.1",
            "vrf": {
                "default": {
                    "address_family": {
                        "ipv4": {
                            "route": {
                                "10.1.1.0/24": {
                                    "state": "P",
                                    "num_successors": 1,
                                    "fd": "2816",
                                    "nexthops": {
                                        0: {
                                            "nexthop": "Connected",
                                            "interface": "Ethernet1/2"
                                        }
                                    }
                                },
                                "10.121.0.0/24": {
                                    "state": "P",
                                    "num_successors": 1,
                                    "fd": "51200",
                                    "nexthops": {
                                        0: {
                                            "nexthop": "Rstatic",
                                            "fd": 51200,
                                            "rd": 0
                                        },
                                        1: {
                                            "nexthop": "10.1.1.2",
                                            "fd": 3072,
                                            "rd": 576,
                                            "interface": "Ethernet1/2"
                                        }
                                    }
                                },
                                "10.81.1.0/24": {
                                    "state": "P",
                                    "num_successors": 1,
                                    "fd": "51200",
                                    "nexthops": {
                                        0: {
                                            "nexthop": "Rstatic",
                                            "fd": 51200,
                                            "rd": 0
                                        },
                                        1: {
                                            "nexthop": "10.1.1.2",
                                            "fd": 3072,
                                            "rd": 576,
                                            "interface": "Ethernet1/2"
                                        }
                                    }
                                },
                                "10.121.2.0/24": {
                                    "state": "P",
                                    "num_successors": 1,
                                    "fd": "51200",
                                    "nexthops": {
                                        0: {
                                            "nexthop": "Rstatic",
                                            "fd": 51200,
                                            "rd": 0
                                        },
                                        1: {
                                            "nexthop": "10.1.1.2",
                                            "fd": 3072,
                                            "rd": 576,
                                            "interface": "Ethernet1/2"
                                        }
                                    }
                                },
                                "10.121.3.0/24": {
                                    "state": "P",
                                    "num_successors": 1,
                                    "fd": "51200",
                                    "nexthops": {
                                        0: {
                                            "nexthop": "Rstatic",
                                            "fd": 51200,
                                            "rd": 0
                                        },
                                        1: {
                                            "nexthop": "10.1.1.2",
                                            "fd": 3072,
                                            "rd": 576,
                                            "interface": "Ethernet1/2"
                                        }
                                    }
                                },
                                "10.121.4.0/24": {
                                    "state": "P",
                                    "num_successors": 1,
                                    "fd": "Inaccessible",
                                    "nexthops": {
                                        0: {
                                            "nexthop": "Rstatic",
                                            "fd": 51200,
                                            "rd": 0
                                        },
                                        1: {
                                            "nexthop": "10.1.1.2",
                                            "fd": 3072,
                                            "rd": 576,
                                            "interface": "Ethernet1/2"
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
}
