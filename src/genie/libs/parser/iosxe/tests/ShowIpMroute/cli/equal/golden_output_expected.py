expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "multicast_group": {
                        "239.1.1.1": {
                            "source_address": {
                                "*": {
                                    "expire": "stopped",
                                    "rp": "10.4.1.1",
                                    "flags": "SPF",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "uptime": "00:00:03",
                                    "rpf_nbr": "0.0.0.0",
                                },
                                "10.4.1.1": {
                                    "expire": "00:02:57",
                                    "flags": "PFT",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "uptime": "00:00:03",
                                    "rpf_info": "registering",
                                    "rpf_nbr": "0.0.0.0",
                                    "incoming_interface_list": {
                                        "Loopback0": {
                                            "rpf_info": "registering",
                                            "rpf_nbr": "0.0.0.0",
                                        }
                                    },
                                },
                                "10.1.3.1": {
                                    "expire": "00:02:57",
                                    "flags": "PFT",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "uptime": "00:00:03",
                                    "rpf_info": "registering",
                                    "rpf_nbr": "0.0.0.0",
                                    "incoming_interface_list": {
                                        "GigabitEthernet2": {
                                            "rpf_info": "registering",
                                            "rpf_nbr": "0.0.0.0",
                                        }
                                    },
                                },
                            }
                        },
                        "224.0.1.40": {
                            "source_address": {
                                "*": {
                                    "expire": "00:02:56",
                                    "outgoing_interface_list": {
                                        "Loopback0": {
                                            "expire": "00:02:56",
                                            "uptime": "2d09h",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                    "flags": "SCL",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "10.16.2.2",
                                    "uptime": "2d09h",
                                    "rpf_nbr": "0.0.0.0",
                                }
                            }
                        },
                        "224.1.1.1": {
                            "source_address": {
                                "*": {
                                    "expire": "00:02:54",
                                    "outgoing_interface_list": {
                                        "ATM0/0": {
                                            "expire": "00:02:53",
                                            "uptime": "00:03:57",
                                            "vcd": "14",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                    "flags": "SJ",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "172.16.0.0",
                                    "uptime": "00:03:57",
                                    "rpf_nbr": "224.0.0.0224.0.0.0",
                                }
                            }
                        },
                    }
                }
            }
        }
    }
}
