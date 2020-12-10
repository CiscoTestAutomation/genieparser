expected_output = {
    "route-information": {
        "route-table": [
            {
                "active-route-count": "1",
                "destination-count": "1",
                "hidden-route-count": "0",
                "holddown-route-count": "0",
                "rt-entry": {
                    "active-tag": "*",
                    "as-path": "[1] I",
                    "bgp-group": {
                        "bgp-group-name": "eBGP_SUT-2",
                        "bgp-group-type": "External",
                    },
                    "flags": "Nexthop Change",
                    "med": "1",
                    "nh": {"to": "Self"},
                    "route-label": "17",
                    "rt-announced-count": "1",
                    "rt-destination": "10.36.3.3",
                    "rt-entry-count": "1",
                    "rt-prefix-length": "32",
                },
                "table-name": "inet.3",
                "total-route-count": "1",
            }
        ]
    }
}
