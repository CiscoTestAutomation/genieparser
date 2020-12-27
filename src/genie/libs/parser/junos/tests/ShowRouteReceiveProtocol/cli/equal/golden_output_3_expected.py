expected_output = {
    "route-information": {
        "route-table": [
            {
                "active-route-count": "850018",
                "destination-count": "850018",
                "hidden-route-count": "0",
                "holddown-route-count": "0",
                "rt": [
                    {
                        "rt-destination": "192.168.225.0/24",
                        "rt-entry": {
                            "active-tag": "*",
                            "as-path": "4 5 6 I",
                            "local-preference": "200000",
                            "med": "100",
                            "nh": {"to": "10.64.4.4"},
                            "protocol-name": "BGP",
                        },
                    }
                ],
                "table-name": "inet.0",
                "total-route-count": "850021",
            }
        ]
    }
}
