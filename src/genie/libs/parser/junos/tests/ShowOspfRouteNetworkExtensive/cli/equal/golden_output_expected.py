expected_output = {
    "ospf-route-information": {
        "ospf-topology-route-table": {
            "ospf-route": [
                {
                    "ospf-route-entry": {
                        "address-prefix": "10.1.0.0/24",
                        "interface-cost": "0",
                        "next-hop-type": "IP",
                        "ospf-area": "0.0.0.0",
                        "ospf-next-hop": {
                            "next-hop-address": {"interface-address": "10.70.0.4"},
                            "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                        },
                        "route-origin": "10.36.3.3",
                        "route-path-type": "Ext2",
                        "route-priority": "medium",
                        "route-type": "Network",
                    }
                },
                {
                    "ospf-route-entry": {
                        "address-prefix": "10.4.1.1/32",
                        "interface-cost": "0",
                        "next-hop-type": "IP",
                        "ospf-area": "0.0.0.0",
                        "ospf-next-hop": {"next-hop-name": {"interface-name": "lo0.0"}},
                        "route-origin": "10.4.1.1",
                        "route-path-type": "Intra",
                        "route-priority": "low",
                        "route-type": "Network",
                    }
                },
                {
                    "ospf-route-entry": {
                        "address-prefix": "10.16.2.2/32",
                        "interface-cost": "1",
                        "next-hop-type": "IP",
                        "ospf-area": "0.0.0.0",
                        "ospf-next-hop": {
                            "next-hop-address": {"interface-address": "10.135.0.2"},
                            "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                        },
                        "route-origin": "10.16.2.2",
                        "route-path-type": "Intra",
                        "route-priority": "medium",
                        "route-type": "Network",
                    }
                },
                {
                    "ospf-route-entry": {
                        "address-prefix": "10.36.3.3/32",
                        "interface-cost": "2",
                        "next-hop-type": "IP",
                        "ospf-area": "0.0.0.0",
                        "ospf-next-hop": {
                            "next-hop-address": {"interface-address": "10.70.0.4"},
                            "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                        },
                        "route-origin": "10.36.3.3",
                        "route-path-type": "Intra",
                        "route-priority": "medium",
                        "route-type": "Network",
                    }
                },
                {
                    "ospf-route-entry": {
                        "address-prefix": "10.64.4.4/32",
                        "interface-cost": "1",
                        "next-hop-type": "IP",
                        "ospf-area": "0.0.0.0",
                        "ospf-next-hop": {
                            "next-hop-address": {"interface-address": "10.70.0.4"},
                            "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                        },
                        "route-origin": "10.64.4.4",
                        "route-path-type": "Intra",
                        "route-priority": "medium",
                        "route-type": "Network",
                    }
                },
                {
                    "ospf-route-entry": {
                        "address-prefix": "10.145.0.0/24",
                        "interface-cost": "0",
                        "next-hop-type": "IP",
                        "ospf-area": "0.0.0.0",
                        "ospf-next-hop": {
                            "next-hop-address": {"interface-address": "10.70.0.4"},
                            "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                        },
                        "route-origin": "10.36.3.3",
                        "route-path-type": "Ext2",
                        "route-priority": "medium",
                        "route-type": "Network",
                    }
                },
                {
                    "ospf-route-entry": {
                        "address-prefix": "10.135.0.0/24",
                        "interface-cost": "1",
                        "next-hop-type": "IP",
                        "ospf-area": "0.0.0.0",
                        "ospf-next-hop": {
                            "next-hop-name": {"interface-name": "ge-0/0/1.0"}
                        },
                        "route-origin": "10.4.1.1",
                        "route-path-type": "Intra",
                        "route-priority": "low",
                        "route-type": "Network",
                    }
                },
                {
                    "ospf-route-entry": {
                        "address-prefix": "10.70.0.0/24",
                        "interface-cost": "1",
                        "next-hop-type": "IP",
                        "ospf-area": "0.0.0.0",
                        "ospf-next-hop": {
                            "next-hop-name": {"interface-name": "ge-0/0/0.0"}
                        },
                        "route-origin": "10.4.1.1",
                        "route-path-type": "Intra",
                        "route-priority": "low",
                        "route-type": "Network",
                    }
                },
                {
                    "ospf-route-entry": {
                        "address-prefix": "10.205.0.0/24",
                        "interface-cost": "2",
                        "next-hop-type": "IP",
                        "ospf-area": "0.0.0.0",
                        "ospf-next-hop": {
                            "next-hop-address": {"interface-address": "10.70.0.4"},
                            "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                        },
                        "route-origin": "10.64.4.4",
                        "route-path-type": "Intra",
                        "route-priority": "medium",
                        "route-type": "Network",
                    }
                },
            ],
            "ospf-topology-name": "default",
        }
    }
}
