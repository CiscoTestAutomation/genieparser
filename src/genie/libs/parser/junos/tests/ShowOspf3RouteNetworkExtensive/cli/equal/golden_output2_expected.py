expected_output = {
    "ospf3-route-information": {
        "ospf-topology-route-table": {
            "ospf3-route": [
                {
                    "ospf3-route-entry": {
                        "address-prefix": "2001::1/128",
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
                    "ospf3-route-entry": {
                        "address-prefix": "2001::4/128",
                        "interface-cost": "1",
                        "next-hop-type": "IP",
                        "ospf-area": "0.0.0.0",
                        "route-origin": "10.64.4.4",
                        "route-path-type": "Intra",
                        "route-priority": "medium",
                        "route-type": "Network",
                    }
                },
                {
                    "ospf3-route-entry": {
                        "address-prefix": "2001:30::/64",
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
                    "ospf3-route-entry": {
                        "address-prefix": "2001:40::/64",
                        "interface-cost": "1",
                        "next-hop-type": "IP",
                        "ospf-area": "0.0.0.0",
                        "ospf-next-hop": {
                            "next-hop-name": {"interface-name": "ge-0/0/0.0"}
                        },
                        "route-origin": "10.64.4.4",
                        "route-path-type": "Intra",
                        "route-priority": "low",
                        "route-type": "Network",
                    }
                },
                {
                    "ospf3-route-entry": {
                        "address-prefix": "2001:50::/64",
                        "interface-cost": "2",
                        "next-hop-type": "IP",
                        "ospf-area": "0.0.0.0",
                        "route-origin": "10.64.4.4",
                        "route-path-type": "Intra",
                        "route-priority": "medium",
                        "route-type": "Network",
                    }
                },
            ]
        }
    }
}
