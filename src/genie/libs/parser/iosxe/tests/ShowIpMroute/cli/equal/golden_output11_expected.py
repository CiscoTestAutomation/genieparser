expected_output = {
    "vrf": {
        "red": {
            "address_family": {
                "ipv4": {
                    "multicast_group": {
                        "226.1.1.1": {
                            "source_address": {
                                "*": {
                                    "uptime": "00:08:41",
                                    "expire": "stopped",
                                    "flags": "SPF",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "10.10.10.10",
                                    "rpf_nbr": "8888::8",
                                    "incoming_interface_list": {
                                        "Vlan500": {"rpf_nbr": "8888::8"}
                                    },
                                },
                                "30.0.0.2": {
                                    "uptime": "00:08:41",
                                    "expire": "00:02:18",
                                    "flags": "FTGqx",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "0.0.0.0",
                                    "incoming_interface_list": {
                                        "Vlan100": {"rpf_nbr": "0.0.0.0"}
                                    },
                                    "outgoing_interface_list": {
                                        "Vlan500": {
                                            "uptime": "00:08:41",
                                            "expire": "stopped",
                                            "state_mode": "forward/sparse",
                                            "vxlan_version": "v6",
                                            "vxlan_vni": "50000",
                                            "vxlan_nxthop": "FF13::1",
                                        }
                                    },
                                },
                            }
                        },
                        "224.0.1.40": {
                            "source_address": {
                                "*": {
                                    "uptime": "01:07:39",
                                    "expire": "00:02:27",
                                    "flags": "SJCLg",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "10.10.10.10",
                                    "rpf_nbr": "8888::8",
                                    "incoming_interface_list": {
                                        "Vlan500": {"rpf_nbr": "8888::8"}
                                    },
                                    "outgoing_interface_list": {
                                        "Loopback1": {
                                            "uptime": "01:07:39",
                                            "expire": "00:02:27",
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
