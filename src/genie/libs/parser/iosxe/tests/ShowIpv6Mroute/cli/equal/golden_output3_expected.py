expected_output = {
    "vrf": {
        "red": {
            "address_family": {
                "ipv6": {
                    "multicast_group": {
                        "FF45::1": {
                            "source_address": {
                                "192:168:3::1": {
                                    "outgoing_interface_list": {
                                        "Ethernet0/0": {
                                            "state_mode": "forward",
                                            "uptime": "00:08:00",
                                            "expire": "00:02:37",
                                        },
                                        "LISP0.101": {
                                            "state_mode": "forward",
                                            "uptime": "01:38:26",
                                            "expire": "00:03:08",
                                            "lisp_mcast_source": "100:44:44::44",
                                        },
                                        "LISP0.101-1": {
                                            "state_mode": "forward",
                                            "uptime": "01:38:26",
                                            "expire": "00:03:10",
                                            "lisp_mcast_source": "100:55:55::55",
                                        },

                                    },
                                    "incoming_interface_list": {
                                        "LISP0.101": {"rpf_nbr": "100:11:11::11"}
                                    },
                                    "rp_bit": False,
                                    "rpf_nbr": "100:11:11::11",
                                    "uptime": "00:08:00",
                                    "flags": "ST",
                                    "msdp_learned": False,
                                    "expire": "00:02:37",
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
