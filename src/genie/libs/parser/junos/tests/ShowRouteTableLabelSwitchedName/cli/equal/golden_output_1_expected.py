expected_output = {
    "route-information": {
        "route-table": {
            "table-name": "mpls.0",
            "destination-count": "36",
            "total-route-count": "36",
            "active-route-count": "36",
            "holddown-route-count": "0",
            "hidden-route-count": "0",
            "rt": [
                {
                    "rt-destination": "46",
                    "rt-entry": [
                        {
                            "age": {"#text": "00:10:22"},
                            "active-tag": "*",
                            "protocol-name": "RSVP",
                            "preference": "7",
                            "preference2": "1",
                            "metric": "1",
                            "nh": [
                                {
                                    "selected-next-hop": True,
                                    "to": "192.168.145.218",
                                    "via": "ge-0/0/1.1",
                                    "lsp-name": "test_lsp_01",
                                }
                            ],
                        }
                    ],
                }
            ],
        }
    }
}
