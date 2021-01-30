expected_output = {
    "route-information": {
        "route-table": [
            {
                "active-route-count": "60",
                "destination-count": "60",
                "hidden-route-count": "0",
                "holddown-route-count": "1",
                "rt": [
                    {
                        "rt-destination": "10.36.255.252/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "4w5d 22:51:00"},
                            "metric": "1111",
                            "nh": [{"to": "10.169.14.158", "via": "ge-0/0/2.0"}],
                            "preference": "10",
                            "preference2": "10",
                            "protocol-name": "OSPF",
                        },
                    },
                    {
                        "rt-entry": {
                            "age": {"#text": "27w6d 12:53:14"},
                            "med": "16011",
                            "as-path": " (65161) I",
                            "learned-from": "10.34.2.250",
                            "local-preference": "4294967285",
                            "nh": [{"to": "10.169.14.158", "via": "ge-0/0/2.0"}],
                            "preference": "170",
                            "protocol-name": "BGP",
                            "validation-state": "unverified",
                        }
                    },
                ],
                "table-name": "inet.0",
                "total-route-count": "66",
            },
            {
                "active-route-count": "27",
                "destination-count": "27",
                "hidden-route-count": "0",
                "holddown-route-count": "0",
                "rt": [
                    {
                        "rt-destination": "10.36.255.252/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "4w5d 22:51:00"},
                            "med": "16011",
                            "as-path": " (65161) I",
                            "learned-from": "10.34.2.250",
                            "local-preference": "100",
                            "nh": [
                                {
                                    "to": "10.169.14.158",
                                    "via": "ge-0/0/2.0",
                                    "mpls-label": "Push 118420",
                                }
                            ],
                            "preference": "170",
                            "protocol-name": "BGP",
                            "validation-state": "unverified",
                        },
                    }
                ],
                "table-name": "inet.3",
                "total-route-count": "27",
            },
            {
                "active-route-count": "34",
                "destination-count": "34",
                "hidden-route-count": "0",
                "holddown-route-count": "0",
                "rt": [
                    {
                        "rt-destination": "10.36.255.252/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "4w5d 22:51:00"},
                            "metric": "0",
                            "nh": [{"to": "10.169.14.158", "via": "ge-0/0/2.0"}],
                            "preference": "10",
                            "preference2": "10",
                            "protocol-name": "OSPF",
                            "rt-tag": "65151500",
                        },
                    }
                ],
                "table-name": "GIPV.inet.0",
                "total-route-count": "34",
            },
        ]
    }
}
