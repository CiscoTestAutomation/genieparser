expected_output = {
    "vrf": {
        "vrf1": {
            "address_family": {
                "ipv6": {
                    "multicast_group": {
                        "FF8E::": {
                            "source_address": {
                                "*": {
                                    "uptime": "00:06:39",
                                    "expire": "00:02:57",
                                    "flags": "S",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "FC00::1:1:1",
                                    "incoming_interface_list": {
                                        "Tunnel2": {"rpf_nbr": "::FFFF:2.2.2.2"}
                                    },
                                    "rpf_nbr": "::FFFF:2.2.2.2",
                                    "outgoing_interface_list": {
                                        "Port-channel40": {
                                            "uptime": "00:06:39",
                                            "expire": "00:02:57",
                                            "state_mode": "forward",
                                        }
                                    },
                                },
                                "2001::2": {
                                    "uptime": "00:06:39",
                                    "expire": "00:02:57",
                                    "flags": "STY",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "incoming_interface_list": {
                                        "Tunnel2": {
                                            "iif_mdt_ip": "239.192.20.41",
                                            "rpf_nbr": "::FFFF:2.2.2.2",
                                        }
                                    },
                                    "rpf_nbr": "::FFFF:2.2.2.2",
                                    "outgoing_interface_list": {
                                        "Port-channel40": {
                                            "uptime": "00:06:39",
                                            "expire": "00:02:57",
                                            "state_mode": "forward",
                                        }
                                    },
                                },
                            }
                        },
                        "FF8E::1": {
                            "source_address": {
                                "*": {
                                    "uptime": "00:06:39",
                                    "expire": "00:02:57",
                                    "flags": "S",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "FC00::1:1:1",
                                    "incoming_interface_list": {
                                        "Tunnel2": {"rpf_nbr": "::FFFF:2.2.2.2"}
                                    },
                                    "rpf_nbr": "::FFFF:2.2.2.2",
                                    "outgoing_interface_list": {
                                        "Port-channel40": {
                                            "uptime": "00:06:39",
                                            "expire": "00:02:57",
                                            "state_mode": "forward",
                                        }
                                    },
                                },
                                "2001::2": {
                                    "uptime": "00:06:39",
                                    "expire": "00:02:57",
                                    "flags": "STY",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "incoming_interface_list": {
                                        "Tunnel2": {
                                            "iif_mdt_ip": "239.192.20.40",
                                            "rpf_nbr": "::FFFF:2.2.2.2",
                                        }
                                    },
                                    "rpf_nbr": "::FFFF:2.2.2.2",
                                    "outgoing_interface_list": {
                                        "Port-channel40": {
                                            "uptime": "00:06:39",
                                            "expire": "00:02:57",
                                            "state_mode": "forward",
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
