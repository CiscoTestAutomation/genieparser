expected_output = {
    "route-information": {
        "route-table": {
            "active-route-count": "1200008",
            "destination-count": "1200008",
            "hidden-route-count": "0",
            "holddown-route-count": "0",
            "rt": [
                {
                    "rt-destination": "10.81.123.0/32",
                    "rt-entry": {
                        "active-tag": "*",
                        "as-path": "67890 [1] I",
                        "bgp-metric-flags": "Nexthop Change",
                        "nh": {"to": "Self"},
                        "protocol-name": "BGP",
                    },
                }
            ],
            "table-name": "inet.0",
            "total-route-count": "1200008",
        }
    }
}
