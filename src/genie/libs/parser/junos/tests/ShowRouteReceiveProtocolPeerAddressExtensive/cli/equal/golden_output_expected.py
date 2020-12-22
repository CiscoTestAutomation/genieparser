expected_output = {
    "route-information": {
        "route-table": [
            {
                "active-route-count": "16",
                "destination-count": "16",
                "hidden-route-count": "0",
                "holddown-route-count": "0",
                "rt": [
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.1.0.0",
                        "rt-entry": {
                            "as-path": "AS path: I",
                            "bgp-path-attributes": {
                                "attr-as-path-effective": {
                                    "aspath-effective-string": "AS path:",
                                    "attr-value": "I",
                                }
                            },
                            "bgp-rt-flag": "Accepted",
                            "local-preference": "100",
                            "nh": {"to": "10.64.4.4"},
                        },
                        "rt-entry-count": {"#text": "2"},
                        "rt-prefix-length": "24",
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.64.4.4",
                        "rt-entry": {
                            "as-path": "AS path: I",
                            "bgp-path-attributes": {
                                "attr-as-path-effective": {
                                    "aspath-effective-string": "AS path:",
                                    "attr-value": "I",
                                }
                            },
                            "bgp-rt-flag": "Accepted",
                            "local-preference": "100",
                            "nh": {"to": "10.64.4.4"},
                        },
                        "rt-entry-count": {"#text": "2"},
                        "rt-prefix-length": "32",
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.145.0.0",
                        "rt-entry": {
                            "as-path": "AS path: I",
                            "bgp-path-attributes": {
                                "attr-as-path-effective": {
                                    "aspath-effective-string": "AS path:",
                                    "attr-value": "I",
                                }
                            },
                            "bgp-rt-flag": "Accepted",
                            "local-preference": "100",
                            "nh": {"to": "10.64.4.4"},
                        },
                        "rt-entry-count": {"#text": "2"},
                        "rt-prefix-length": "24",
                    },
                    {
                        "active-tag": "* ",
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.0",
                        "rt-entry": {
                            "as-path": "AS path: I",
                            "bgp-path-attributes": {
                                "attr-as-path-effective": {
                                    "aspath-effective-string": "AS path:",
                                    "attr-value": "I",
                                }
                            },
                            "bgp-rt-flag": "Accepted",
                            "local-preference": "100",
                            "nh": {"to": "10.64.4.4"},
                        },
                        "rt-entry-count": {"#text": "1"},
                        "rt-prefix-length": "24",
                    },
                    {
                        "active-tag": "* ",
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.240.0",
                        "rt-entry": {
                            "as-path": "AS path: 200000 4 5 6 I",
                            "bgp-path-attributes": {
                                "attr-as-path-effective": {
                                    "aspath-effective-string": "AS path:",
                                    "attr-value": "200000 4 5 6 I",
                                }
                            },
                            "bgp-rt-flag": "Accepted",
                            "local-preference": "100",
                            "nh": {"to": "10.64.4.4"},
                        },
                        "rt-entry-count": {"#text": "1"},
                        "rt-prefix-length": "24",
                    },
                    {
                        "active-tag": "* ",
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.205.0",
                        "rt-entry": {
                            "as-path": "AS path: 200000 4 7 8 I",
                            "bgp-path-attributes": {
                                "attr-as-path-effective": {
                                    "aspath-effective-string": "AS path:",
                                    "attr-value": "200000 4 7 8 I",
                                }
                            },
                            "bgp-rt-flag": "Accepted",
                            "local-preference": "100",
                            "nh": {"to": "10.64.4.4"},
                        },
                        "rt-entry-count": {"#text": "1"},
                        "rt-prefix-length": "24",
                    },
                    {
                        "active-tag": "* ",
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.115.0",
                        "rt-entry": {
                            "as-path": "AS path: 200000 4 100000 8 I",
                            "bgp-path-attributes": {
                                "attr-as-path-effective": {
                                    "aspath-effective-string": "AS path:",
                                    "attr-value": "200000 4 100000 8 I",
                                }
                            },
                            "bgp-rt-flag": "Accepted",
                            "local-preference": "100",
                            "nh": {"to": "10.64.4.4"},
                        },
                        "rt-entry-count": {"#text": "1"},
                        "rt-prefix-length": "24",
                    },
                ],
                "table-name": "inet.0",
                "total-route-count": "19",
            },
            {
                "active-route-count": "18",
                "destination-count": "18",
                "hidden-route-count": "0",
                "holddown-route-count": "0",
                "table-name": "inet6.0",
                "total-route-count": "20",
            },
        ]
    }
}
