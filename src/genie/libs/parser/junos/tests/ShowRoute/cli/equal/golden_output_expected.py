expected_output = {
    "route-information": {
        "route-table": [
            {
                "active-route-count": "932",
                "destination-count": "932",
                "hidden-route-count": "0",
                "holddown-route-count": "0",
                "rt": [
                    {
                        "rt-destination": "10.169.14.240/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "5w2d 15:42:25"},
                            "nh": [{"to": "10.169.14.121", "via": "ge-0/0/1.0"}],
                            "preference": "5",
                            "protocol-name": "Static",
                        },
                    }
                ],
                "table-name": "inet.0",
                "total-route-count": "1618",
            },
            {
                "active-route-count": "12",
                "destination-count": "12",
                "hidden-route-count": "0",
                "holddown-route-count": "0",
                "table-name": "inet.3",
                "total-route-count": "12",
            },
        ]
    }
}
