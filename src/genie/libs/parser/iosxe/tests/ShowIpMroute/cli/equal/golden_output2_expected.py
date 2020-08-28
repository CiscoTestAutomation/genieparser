expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv4": {
                    "multicast_group": {
                        "239.1.1.1": {
                            "source_address": {
                                "10.229.11.11": {
                                    "expire": "00:02:55",
                                    "uptime": "00:00:04",
                                    "flags": "PFT",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_info": "registering",
                                    "rpf_nbr": "0.0.0.0",
                                    "incoming_interface_list": {
                                        "Loopback1": {
                                            "rpf_info": "registering",
                                            "rpf_nbr": "0.0.0.0",
                                        }
                                    },
                                },
                                "*": {
                                    "expire": "stopped",
                                    "uptime": "00:00:04",
                                    "flags": "SPF",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "10.229.11.11",
                                    "rpf_nbr": "0.0.0.0",
                                },
                            }
                        },
                        "224.0.1.40": {
                            "source_address": {
                                "*": {
                                    "expire": "00:02:52",
                                    "uptime": "00:08:58",
                                    "rpf_nbr": "0.0.0.0",
                                    "outgoing_interface_list": {
                                        "Loopback1": {
                                            "state_mode": "forward/sparse",
                                            "uptime": "00:08:58",
                                            "expire": "00:02:52",
                                        }
                                    },
                                    "flags": "SJCL",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "10.229.11.11",
                                }
                            }
                        },
                    }
                }
            }
        }
    }
}
