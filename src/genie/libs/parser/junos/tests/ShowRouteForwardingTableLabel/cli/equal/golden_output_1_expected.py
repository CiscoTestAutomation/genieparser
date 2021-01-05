expected_output = {
    "forwarding-table-information": {
        "route-table": [
            {
                "address-family": "MPLS",
                "rt-entry": [
                    {
                        "destination-type": "user",
                        "nh": {
                            "nh-index": "578",
                            "nh-reference-count": "2",
                            "nh-type": "Pop",
                            "to": "10.169.14.158",
                            "via": "ge-0/0/0.0",
                        },
                        "route-reference-count": "0",
                        "rt-destination": "16",
                    },
                    {
                        "destination-type": "user",
                        "nh": {
                            "nh-index": "579",
                            "nh-reference-count": "2",
                            "nh-type": "Pop",
                            "to": "10.169.14.158",
                            "via": "ge-0/0/0.0",
                        },
                        "route-reference-count": "0",
                        "rt-destination": "16(S=0)",
                    },
                ],
                "table-name": "default.mpls",
            },
            {
                "address-family": "MPLS",
                "enabled-protocols": "Bridging, Single VLAN, Dual VLAN,",
                "rt-entry": [
                    {
                        "destination-type": "perm",
                        "nh": {
                            "nh-index": "535",
                            "nh-reference-count": "1",
                            "nh-type": "dscd",
                        },
                        "route-reference-count": "0",
                        "rt-destination": "default",
                    }
                ],
                "table-name": "__mpls-oam__.mpls",
            },
        ]
    }
}
