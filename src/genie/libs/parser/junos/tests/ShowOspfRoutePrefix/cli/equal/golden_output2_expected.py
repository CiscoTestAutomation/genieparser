expected_output = {
    "ospf-route-information": {
        "ospf-topology-route-table": {
            "ospf-route": {
                "ospf-route-entry": {
                    "address-prefix": "10.135.0.0/24",
                    "interface-cost": "2",
                    "next-hop-type": "IP",
                    "ospf-next-hop": [
                        {
                            "next-hop-address": {
                                "interface-address": "10.0.1.2"
                            },
                            "next-hop-name": {
                                "interface-name": "ge-0/0/0.11"
                            }
                        },
                        {
                            "next-hop-address": {
                                "interface-address": "10.0.0.2"
                            },
                            "next-hop-name": {
                                "interface-name": "ge-0/0/4.0"
                            }
                        }
                    ],
                    "route-path-type": "Intra",
                    "route-type": "Network"
                }
            },
            "ospf-topology-name": "default"
        }
    }
}