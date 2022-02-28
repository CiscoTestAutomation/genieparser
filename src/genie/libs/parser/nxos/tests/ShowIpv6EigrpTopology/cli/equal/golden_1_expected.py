expected_output = {
    "as": {
        1: {
            "routerid": "2001:10::1",
            "vrf": {
                "default": {
                    "address_family": {
                        "ipv6": {
                            "route": {
                                "2001:1::1:0/112": {
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
                                "2001:11::/112": {
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
                                            "nexthop": "2001:1::1:2",
                                            "fd": 3072,
                                            "rd": 576,
                                            "interface": "Ethernet1/2"
                                        }
                                    }
                                },
                                "2001:11::1:0/112": {
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
                                            "nexthop": "2001:1::1:2",
                                            "fd": 3072,
                                            "rd": 576,
                                            "interface": "Ethernet1/2"
                                        }
                                    }
                                },
                                "2001:11::2:0/112": {
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
                                            "nexthop": "2001:1::1:2",
                                            "fd": 3072,
                                            "rd": 576,
                                            "interface": "Ethernet1/2"
                                        }
                                    }
                                },
                                "2001:11::3:0/112": {
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
                                            "nexthop": "2001:1::1:2",
                                            "fd": 3072,
                                            "rd": 576,
                                            "interface": "Ethernet1/2"
                                        }
                                    }
                                },
                                "2001:11::4:0/112": {
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
                                            "nexthop": "2001:1::1:2",
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
