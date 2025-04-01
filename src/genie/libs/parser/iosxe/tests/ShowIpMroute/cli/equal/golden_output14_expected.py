expected_output = {
    "vrf": {
        "vrf1": {
            "address_family": {
                "ipv4": {
                    "multicast_group": {
                        "225.1.1.1": {
                            "source_address": {
                                "*": {
                                    "uptime": "00:24:00",
                                    "expire": "00:02:59",
                                    "flags": "S",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "11.11.11.11",
                                    "rpf_nbr": "2.2.2.2",
                                    "incoming_interface_list": {
                                        "Tunnel0": {"rpf_nbr": "2.2.2.2"}
                                    },
                                    "outgoing_interface_list": {
                                        "Port-channel40": {
                                            "uptime": "00:06:55",
                                            "expire": "00:02:59",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                },
                                "192.168.1.2": {
                                    "uptime": "00:06:54",
                                    "expire": "00:02:23",
                                    "flags": "TY",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "2.2.2.2",
                                    "incoming_interface_list": {
                                        "Tunnel0": {
                                            "rpf_nbr": "2.2.2.2",
                                            "iif_mdt_ip": "239.192.20.41",
                                        }
                                    },
                                    "outgoing_interface_list": {
                                        "Port-channel40": {
                                            "uptime": "00:06:54",
                                            "expire": "00:03:27",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                },
                            }
                        },
                        "225.1.1.3": {
                            "source_address": {
                                "*": {
                                    "uptime": "00:24:00",
                                    "expire": "00:03:00",
                                    "flags": "S",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "11.11.11.11",
                                    "rpf_nbr": "2.2.2.2",
                                    "incoming_interface_list": {
                                        "Tunnel0": {"rpf_nbr": "2.2.2.2"}
                                    },
                                    "outgoing_interface_list": {
                                        "Port-channel40": {
                                            "uptime": "00:06:55",
                                            "expire": "00:03:00",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                },
                                "192.168.1.2": {
                                    "uptime": "00:06:54",
                                    "expire": "00:02:23",
                                    "flags": "TY",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "2.2.2.2",
                                    "incoming_interface_list": {
                                        "Tunnel0": {
                                            "rpf_nbr": "2.2.2.2",
                                            "iif_mdt_ip": "239.192.20.32",
                                        }
                                    },
                                    "outgoing_interface_list": {
                                        "Port-channel40": {
                                            "uptime": "00:06:54",
                                            "expire": "00:03:28",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                },
                            }
                        },
                    }
                }
            }
        }
    }
}
