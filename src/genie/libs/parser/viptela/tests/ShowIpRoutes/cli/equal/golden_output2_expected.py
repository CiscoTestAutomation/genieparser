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
        }
    }
}