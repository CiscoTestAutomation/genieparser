expected_output = {
    "vrf": {
        "red": {
            "address_family": {
                "ipv4": {
                    "multicast_group": {
                        "232.1.1.1": {
                            "source_address": {
                                "30.0.0.2": {
                                    "uptime": "1d05h",
                                    "expire": "stopped",
                                    "flags": "sTyGx",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "0.0.0.0",
                                    "incoming_interface_list": {
                                        "Vlan100": {"rpf_nbr": "0.0.0.0"}
                                    },
                                    "outgoing_interface_list": {
                                        "Vlan500": {
                                            "uptime": "1d05h",
                                            "expire": "stopped",
                                            "state_mode": "forward/sparse",
                                            "vxlan_version": "v4",
                                            "vxlan_vni": "50000",
                                            "vxlan_nxthop": "239.1.1.0",
                                        }
                                    },
                                }
                            }
                        },
                        "232.1.1.2": {
                            "source_address": {
                                "20.0.0.5": {
                                    "uptime": "1d05h",
                                    "expire": "00:02:42",
                                    "flags": "sTI",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "0.0.0.0",
                                    "outgoing_interface_list": {
                                        "Vlan100": {
                                            "uptime": "1d05h",
                                            "expire": "00:02:42",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                },
                                "20.0.0.4": {
                                    "uptime": "1d05h",
                                    "expire": "00:02:42",
                                    "flags": "sTI",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "0.0.0.0",
                                    "outgoing_interface_list": {
                                        "Vlan100": {
                                            "uptime": "1d05h",
                                            "expire": "00:02:42",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                },
                                "20.0.0.2": {
                                    "uptime": "1d05h",
                                    "expire": "00:02:42",
                                    "flags": "sTIYg",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "2.2.2.2",
                                    "incoming_interface_list": {
                                        "Vlan500": {"rpf_nbr": "2.2.2.2"}
                                    },
                                    "outgoing_interface_list": {
                                        "Vlan100": {
                                            "uptime": "1d05h",
                                            "expire": "00:02:42",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                },
                            }
                        },
                        "224.0.1.40": {
                            "source_address": {
                                "*": {
                                    "uptime": "1d05h",
                                    "expire": "00:02:40",
                                    "flags": "SJCL",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "10.10.10.10",
                                    "rpf_nbr": "0.0.0.0",
                                    "outgoing_interface_list": {
                                        "Vlan100": {
                                            "uptime": "1d05h",
                                            "expire": "00:02:40",
                                            "state_mode": "forward/sparse",
                                        }
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
