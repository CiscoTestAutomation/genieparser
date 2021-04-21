expected_output = {
    "ospf3-route-information": {
        "ospf-topology-route-table": {
            "ospf3-route": [
                {
                    "ospf3-route-entry": {
                        "address-prefix": "2001::4/128",
                        "interface-cost": "0",
                        "next-hop-type": "IP",
                        "ospf-area": "0.0.0.0",
                        "ospf-next-hop": {"next-hop-name": {"interface-name": "lo0.0"}},
                        "route-origin": "10.64.4.4",
                        "route-path-type": "Intra",
                        "route-priority": "low",
                        "route-type": "Network",
                    }
                }
            ]
        }
    }
}
