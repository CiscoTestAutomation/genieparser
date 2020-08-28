expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv6": {
                    "multicast_group": {
                        "FF07::1": {
                            "source_address": {
                                "2001:DB8:999::99": {
                                    "outgoing_interface_list": {
                                        "POS4/0": {
                                            "state_mode": "forward",
                                            "uptime": "00:02:06",
                                            "expire": "00:03:27",
                                        }
                                    },
                                    "incoming_interface_list": {
                                        "POS1/0": {"rpf_nbr": "2001:DB8:999::99"}
                                    },
                                    "uptime": "00:02:06",
                                    "flags": "SFT",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "2001:DB8:999::99",
                                    "expire": "00:01:23",
                                },
                                "*": {
                                    "outgoing_interface_list": {
                                        "POS4/0": {
                                            "state_mode": "forward",
                                            "uptime": "00:04:45",
                                            "expire": "00:02:47",
                                        }
                                    },
                                    "incoming_interface_list": {
                                        "Tunnel5": {"rpf_nbr": "2001:db8:90:24::6"}
                                    },
                                    "uptime": "00:04:45",
                                    "rp": "2001:DB8:6::6",
                                    "flags": "S",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "2001:db8:90:24::6",
                                    "expire": "00:02:47",
                                },
                            }
                        }
                    }
                }
            }
        }
    }
}
