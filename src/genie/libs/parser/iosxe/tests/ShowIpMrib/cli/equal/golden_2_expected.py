expected_output={
    "vrf": {
        "red": {
            "address_family": {
                "ipv4": {
                    "multicast_group": {
                        "224.0.1.40": {
                            "source_address": {
                                "*": {
                                    "rpf_nbr": "0.0.0.0",
                                    "flags": " C",
                                    "egress_interface_list": {
                                        "Vlan100": {"egress_flags": "F IC NS"}
                                    },
                                }
                            }
                        },
                        "232.1.1.2": {
                            "source_address": {
                                "20.0.0.2": {
                                    "rpf_nbr": "2.2.2.2",
                                    "flags": "",
                                    "incoming_interface_list": {
                                        "Vlan500": {"ingress_flags": "A "}
                                    },
                                    "egress_interface_list": {
                                        "Vlan100": {"egress_flags": "F NS"}
                                    },
                                },
                                "20.0.0.4": {
                                    "rpf_nbr": "0.0.0.0",
                                    "flags": "",
                                    "egress_interface_list": {
                                        "Vlan100": {"egress_flags": "F NS"}
                                    },
                                },
                                "20.0.0.5": {
                                    "rpf_nbr": "0.0.0.0",
                                    "flags": "",
                                    "egress_interface_list": {
                                        "Vlan100": {"egress_flags": "F NS"}
                                    },
                                },
                            }
                        },
                        "232.1.1.1": {
                            "source_address": {
                                "30.0.0.2": {
                                    "rpf_nbr": "0.0.0.0",
                                    "flags": "",
                                    "egress_interface_list": {
                                        "Vlan500-(239.1.1.0, 1.4.0.0)": {
                                            "egress_flags": "F ",
                                            "egress_next_hop": "(239.1.1.0, 1.4.0.0)",
                                        }
                                    },
                                    "incoming_interface_list": {
                                        "Vlan100": {"ingress_flags": "A"}
                                    },
                                }
                            }
                        },
                    }
                }
            }
        }
    }
}

