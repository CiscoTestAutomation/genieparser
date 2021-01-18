expected_output = {
    "ospf3-route-information": {
        "ospf-topology-route-table": {
            "ospf3-route": {
                "ospf3-route-entry": {
                    "address-prefix": "2001:30::/64",
                    "interface-cost": "2",
                    "next-hop-type": "IP",
                    "ospf-next-hop": [
                        {
                            "next-hop-address": {
                                "interface-address": "fe80::250:5600:b8d:c798"
                            },
                            "next-hop-name": {
                                "interface-name": "ge-0/0/0.11"
                            }
                        },
                        {
                            "next-hop-address": {
                                "interface-address": "fe80::250:56ff:fe8d:6d7e"
                            },
                            "next-hop-name": {
                                "interface-name": "ge-0/0/4.0"
                            }
                        }
                    ],
                    "route-path-type": "Intra",
                    "route-type": "Network"
                }
            }
        }
    }
}