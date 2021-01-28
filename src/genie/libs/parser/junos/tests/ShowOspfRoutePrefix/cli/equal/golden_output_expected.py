expected_output = {
    "ospf-route-information": {
        "ospf-topology-route-table": {
            "ospf-route": {
                "ospf-route-entry": {
                    "address-prefix": "30.0.0.0/24",
                    "interface-cost": "2",
                    "next-hop-type": "IP",
                    "ospf-next-hop": [
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