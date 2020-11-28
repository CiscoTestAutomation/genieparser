expected_output = {
    "route-information": {
        "route-table": [
            {
                "table-name": "inet.0",
                "destination-count": "60",
                "total-route-count": "66",
                "active-route-count": "60",
                "holddown-route-count": "1",
                "hidden-route-count": "0",
                "rt-entry": {
                    "rt-destination": "10.169.196.254",
                    "rt-prefix-length": "32",
                    "rt-entry-count": "2",
                    "rt-announced-count": "2",
                    "bgp-group": {
                        "bgp-group-name": "lacGCS001",
                        "bgp-group-type": "External",
                    },
                    "nh": {"to": "10.189.5.252"},
                    "med": "29012",
                    "local-preference": "4294967285",
                    "as-path": "[65151] (65171) I",
                    "communities": "65151:65109",
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
                    "rt-destination": "10.169.196.254",
                    "rt-prefix-length": "32",
                    "rt-entry-count": "1",
                    "rt-announced-count": "1",
                    "route-label": "118071",
                    "bgp-group": {
                        "bgp-group-name": "lacGCS001",
                        "bgp-group-type": "External",
                    },
                    "nh": {"to": "10.189.5.252"},
                    "med": "29012",
                    "local-preference": "100",
                    "as-path": "[65151] (65171) I",
                    "communities": "65151:65109",
                },
            },
        ]
    }
}
