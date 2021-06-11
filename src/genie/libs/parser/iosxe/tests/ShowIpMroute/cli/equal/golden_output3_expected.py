expected_output =  {
    "vrf": {
        "DEVICE_VN": {
            "address_family": {
                "ipv4": {
                    "multicast_group": {
                        "239.1.1.1": {
                            "source_address": {
                                "*": {
                                    "uptime": "00:05:14",
                                    "expire": "stopped",
                                    "flags": "SPF",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "192.168.19.1",
                                    "rpf_nbr": "172.24.0.1",
                                    "incoming_interface_list": {"LISP0.4100": {"rpf_nbr": "172.24.0.1"}},
                                },
                                "192.168.11.11": {
                                    "uptime": "00:00:52",
                                    "expire": "00:02:07",
                                    "flags": "FT",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "0.0.0.0",
                                    "rpf_info": "registering",
                                    "incoming_interface_list": {"Vlan1022": {"rpf_nbr": "0.0.0.0", "rpf_info": "registering"}},
                                    "outgoing_interface_list": {
                                        "LISP0.4100": {
                                            "uptime": "00:00:52",
                                            "expire": "stopped",
                                            "state_mode": "forward/sparse",
                                            "lisp_mcast_source": "172.24.0.3",
                                            "lisp_mcast_group": "232.0.0.199",
                                        }
                                    },
                                },
                            }
                        },
                        "224.0.1.40": {
                            "source_address": {
                                "*": {
                                    "uptime": "00:08:58",
                                    "expire": "00:02:05",
                                    "flags": "SJCL",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "192.168.19.1",
                                    "rpf_nbr": "172.24.0.1",
                                    "incoming_interface_list": {"LISP0.4100": {"rpf_nbr": "172.24.0.1"}},
                                    "outgoing_interface_list": {
                                        "Loopback4100": {"uptime": "00:08:57", "expire": "00:02:05", "state_mode": "forward/sparse"}
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
