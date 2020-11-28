expected_output = {
    "route-information": {
        "route-table": [
            {
                "table-name": "inet.0",
                "destination-count": "62",
                "total-route-count": "67",
                "active-route-count": "62",
                "holddown-route-count": "0",
                "hidden-route-count": "0",
                "rt-entry": {
                    "active-tag": "*",
                    "rt-destination": "10.36.255.252",
                    "rt-prefix-length": "32",
                    "rt-entry-count": "1",
                    "rt-announced-count": "1",
                    "bgp-group": {
                        "bgp-group-name": "sjkGDS221-EC11",
                        "bgp-group-type": "External",
                    },
                    "nh": {"to": "Self"},
                    "med": "16011",
                    "local-preference": "4294967285",
                    "as-path": "[65161] I",
                    "communities": "65151:65109",
                    "flags": "Nexthop Change",
                },
            },
            {
                "table-name": "inet.3",
                "destination-count": "27",
                "total-route-count": "27",
                "active-route-count": "27",
                "holddown-route-count": "0",
                "hidden-route-count": "0",
                "rt-entry": {
                    "active-tag": "*",
                    "rt-destination": "10.36.255.252",
                    "rt-prefix-length": "32",
                    "rt-entry-count": "1",
                    "rt-announced-count": "1",
                    "route-label": "118420",
                    "bgp-group": {
                        "bgp-group-name": "sjkGDS221-EC11",
                        "bgp-group-type": "External",
                    },
                    "nh": {"to": "Self"},
                    "med": "16011",
                    "local-preference": "100",
                    "as-path": "[65161] I",
                    "communities": "65151:65109",
                    "flags": "Nexthop Change",
                },
            },
        ]
    }
}
