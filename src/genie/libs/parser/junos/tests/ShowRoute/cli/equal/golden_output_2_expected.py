expected_output = {
    "route-information": {
        "route-table": [
            {
                "active-route-count": "23",
                "destination-count": "23",
                "hidden-route-count": "0",
                "holddown-route-count": "0",
                "rt": [
                    {
                        "rt-destination": "2001:db8:eb18:ca45::1/128",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w5d 18:30:36"},
                            "nh": [
                                {"to": "2001:db8:eb18:6337::1", "via": "ge-0/0/1.0"}
                            ],
                            "preference": "5",
                            "protocol-name": "Static",
                        },
                    }
                ],
                "table-name": "inet6.0",
                "total-route-count": "24",
            }
        ]
    }
}
