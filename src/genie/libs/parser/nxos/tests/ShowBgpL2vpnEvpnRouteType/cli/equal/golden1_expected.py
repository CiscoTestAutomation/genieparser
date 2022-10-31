expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "default": {
                    "address_family": {
                        "l2vpn evpn": {
                            "rd": {
                                "1004:4": {
                                    "rd": "1004:4",
                                    "rd_vrf": "l3",
                                    "rd_vniid": 501004,
                                    "prefix": {
                                        "[5]:[0]:[0]:[32]:[100.4.1.1]/224": {
                                            "nonipprefix": "[5]:[0]:[0]:[32]:[100.4.1.1]/224",
                                            "prefixversion": 349,
                                            "totalpaths": 1,
                                            "bestpathnr": 1,
                                            "on_xmitlist": True,
                                            "path": {
                                                1: {
                                                    "pathnr": 0,
                                                    "pathtype": "internal",
                                                    "pathvalid": True,
                                                    "pathbest": True,
                                                    "pathnolabeledrnh": True,
                                                    "imported_from": "99.99.99.99:10:[5]:[0]:[0]:[32]:[100.4.1.1]/224",
                                                    "gateway_ip": "0.0.0.0",
                                                    "as_path": "4 1 10 33299 51178 47751 {27016}",
                                                    "ipnexthop": "93.93.93.93",
                                                    "nexthopmetric": 5,
                                                    "neighbor": "99.99.99.99",
                                                    "neighborid": "99.99.99.99",
                                                    "origin": "egp",
                                                    "localpref": 100,
                                                    "weight": 0,
                                                    "inlabel": 501004,
                                                    "extcommunity": [
                                                        "RT:3:501004",
                                                        "ENCAP:8",
                                                        "Router",
                                                        "MAC:0200.5d5d.5d5d"
                                                    ]
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
    }
}
