expected_output = {
    "vrf": {
        "0": {
            "prefixes": {
                "0.0.0.0/0": {
                    "next_hop_list": {
                        1: {
                            "color": "-",
                            "encap": "-",
                            "index": 1,
                            "nh_addr": "19.75.2.192",
                            "nh_if_name": "ge2/3",
                            "nh_vpn": "-",
                            "status": ["F", "S"],
                            "tloc_ip": "-",
                        },
                        2: {
                            "color": "-",
                            "encap": "-",
                            "index": 2,
                            "nh_addr": "19.75.2.176",
                            "nh_if_name": "ge2/2",
                            "nh_vpn": "-",
                            "status": ["F", "S"],
                            "tloc_ip": "-",
                        },
                    },
                    "prefix": "0.0.0.0/0",
                    "protocol": "static",
                    "protocol_sub_type": "-",
                },
                "10.139.1.3/32": {
                    "next_hop_list": {
                        1: {
                            "color": "-",
                            "encap": "-",
                            "index": 1,
                            "nh_addr": "-",
                            "nh_if_name": "system",
                            "nh_vpn": "-",
                            "status": ["F", "S"],
                            "tloc_ip": "-",
                        }
                    },
                    "prefix": "10.139.1.3/32",
                    "protocol": "connected",
                    "protocol_sub_type": "-",
                },
                "19.75.2.176/31": {
                    "next_hop_list": {
                        1: {
                            "color": "-",
                            "encap": "-",
                            "index": 1,
                            "nh_addr": "-",
                            "nh_if_name": "ge2/2",
                            "nh_vpn": "-",
                            "status": ["F", "S"],
                            "tloc_ip": "-",
                        }
                    },
                    "prefix": "19.75.2.176/31",
                    "protocol": "connected",
                    "protocol_sub_type": "-",
                },
                "19.75.2.192/31": {
                    "next_hop_list": {
                        1: {
                            "color": "-",
                            "encap": "-",
                            "index": 1,
                            "nh_addr": "-",
                            "nh_if_name": "ge2/3",
                            "nh_vpn": "-",
                            "status": ["F", "S"],
                            "tloc_ip": "-",
                        }
                    },
                    "prefix": "19.75.2.192/31",
                    "protocol": "connected",
                    "protocol_sub_type": "-",
                },
            }
        },
        "111": {
            "prefixes": {
                "0.0.0.0/0": {
                    "next_hop_list": {
                        1: {
                            "color": "-",
                            "encap": "-",
                            "index": 1,
                            "nh_addr": "19.75.10.168",
                            "nh_if_name": "ge2/1.101",
                            "nh_vpn": "-",
                            "status": ["F", "S"],
                            "tloc_ip": "-",
                        }
                    },
                    "prefix": "0.0.0.0/0",
                    "protocol": "bgp",
                    "protocol_sub_type": "e",
                },
                "10.139.1.3/32": {
                    "next_hop_list": {
                        1: {
                            "color": "-",
                            "encap": "-",
                            "index": 1,
                            "nh_addr": "-",
                            "nh_if_name": "loopback0",
                            "nh_vpn": "-",
                            "status": ["F", "S"],
                            "tloc_ip": "-",
                        }
                    },
                    "prefix": "10.139.1.3/32",
                    "protocol": "connected",
                    "protocol_sub_type": "-",
                },
                "19.75.10.168/31": {
                    "next_hop_list": {
                        1: {
                            "color": "-",
                            "encap": "-",
                            "index": 1,
                            "nh_addr": "-",
                            "nh_if_name": "ge2/1.101",
                            "nh_vpn": "-",
                            "status": ["F", "S"],
                            "tloc_ip": "-",
                        }
                    },
                    "prefix": "19.75.10.168/31",
                    "protocol": "connected",
                    "protocol_sub_type": "-",
                },
                "19.75.2.253/32": {
                    "next_hop_list": {
                        1: {
                            "color": "-",
                            "encap": "-",
                            "index": 1,
                            "nh_addr": "19.75.10.168",
                            "nh_if_name": "ge2/1.101",
                            "nh_vpn": "-",
                            "status": ["F", "S"],
                            "tloc_ip": "-",
                        }
                    },
                    "prefix": "19.75.2.253/32",
                    "protocol": "bgp",
                    "protocol_sub_type": "e",
                },
            }
        },
        "512": {
            "prefixes": {
                "0.0.0.0/0": {
                    "next_hop_list": {
                        1: {
                            "color": "-",
                            "encap": "-",
                            "index": 1,
                            "nh_addr": "172.31.0.1",
                            "nh_if_name": "mgmt0",
                            "nh_vpn": "-",
                            "status": ["F", "S"],
                            "tloc_ip": "-",
                        }
                    },
                    "prefix": "0.0.0.0/0",
                    "protocol": "static",
                    "protocol_sub_type": "-",
                },
                "172.31.0.0/21": {
                    "next_hop_list": {
                        1: {
                            "color": "-",
                            "encap": "-",
                            "index": 1,
                            "nh_addr": "-",
                            "nh_if_name": "mgmt0",
                            "nh_vpn": "-",
                            "status": ["F", "S"],
                            "tloc_ip": "-",
                        }
                    },
                    "prefix": "172.31.0.0/21",
                    "protocol": "connected",
                    "protocol_sub_type": "-",
                },
            }
        },
    }
}