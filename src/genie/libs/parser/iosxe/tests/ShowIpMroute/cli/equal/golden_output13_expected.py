expected_output = {
    "vrf": {
        "vrf1": {
            "address_family": {
                "ipv4": {
                    "multicast_group": {
                        "225.1.1.1": {
                            "source_address": {
                                "*": {
                                    "uptime": "00:19:29",
                                    "expire": "00:02:48",
                                    "flags": "S",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "11.11.11.11",
                                    "rpf_nbr": "0.0.0.0",
                                    "outgoing_interface_list": {
                                        "Tunnel2": {
                                            "uptime": "00:01:16",
                                            "expire": "00:02:48",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                },
                                "192.168.1.2": {
                                    "uptime": "00:19:29",
                                    "expire": "00:02:15",
                                    "flags": "T",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "192.168.10.2",
                                    "incoming_interface_list": {
                                        "Port-channel10": {"rpf_nbr": "192.168.10.2"}
                                    },
                                    "outgoing_interface_list": {
                                        "Tunnel2": {
                                            "uptime": "00:01:16",
                                            "expire": "00:03:12",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                },
                            }
                        },
                        "225.1.1.3": {
                            "source_address": {
                                "*": {
                                    "uptime": "00:19:29",
                                    "expire": "00:02:47",
                                    "flags": "S",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "11.11.11.11",
                                    "rpf_nbr": "0.0.0.0",
                                    "outgoing_interface_list": {
                                        "Tunnel2": {
                                            "uptime": "00:01:16",
                                            "expire": "00:02:47",
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
