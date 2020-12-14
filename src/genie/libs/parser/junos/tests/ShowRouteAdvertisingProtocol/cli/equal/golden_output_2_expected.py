expected_output = {
    "route-information": {
        "route-table": {
            "active-route-count": "10",
            "destination-count": "10",
            "hidden-route-count": "0",
            "holddown-route-count": "0",
            "rt": [
                {
                    "rt-destination": "0.0.0.0/0",
                    "rt-entry": {
                        "active-tag": "*",
                        "as-path": "I",
                        "bgp-metric-flags": "Nexthop Change",
                        "nh": {"to": "Self"},
                        "protocol-name": "BGP",
                    },
                },
                {
                    "rt-destination": "10.4.1.1/32",
                    "rt-entry": {
                        "active-tag": "*",
                        "as-path": "I",
                        "bgp-metric-flags": "Nexthop Change",
                        "nh": {"to": "Self"},
                        "protocol-name": "BGP",
                    },
                },
                {
                    "rt-destination": "10.36.3.3/32",
                    "rt-entry": {
                        "active-tag": "*",
                        "as-path": "2 I",
                        "bgp-metric-flags": "Nexthop Change",
                        "nh": {"to": "Self"},
                        "protocol-name": "BGP",
                    },
                },
            ],
            "table-name": "inet.0",
            "total-route-count": "10",
        }
    }
}
