expected_output = {
    "vrf": {
        "vrf1": {
            "address_family": {
                "ipv4": {
                    "multicast_group": {
                        "239.0.0.13": {
                            "source_address": {
                                "*": {
                                    "uptime": "00:01:12",
                                    "expire": "stopped",
                                    "flags": "DC",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "0.0.0.0",
                                    "rpf_nbr": "0.0.0.0",
                                    "outgoing_interface_list": {
                                        "Vlan10": {
                                            "uptime": "00:01:12",
                                            "expire": "stopped",
                                            "state_mode": "forward/sparse-dense"
                                        }
                                    }
                                },
                                "50.50.50.2": {
                                    "uptime": "00:00:39",
                                    "expire": "00:02:20",
                                    "flags": "",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "0.0.0.0",
                                    "outgoing_interface_list": {
                                        "Vlan10": {
                                            "uptime": "00:00:39",
                                            "expire": "stopped",
                                            "state_mode": "forward/sparse-dense"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
