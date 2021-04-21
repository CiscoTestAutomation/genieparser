expected_output = {
    "route-information": {
        "route-table": [
            {
                "active-route-count": "929",
                "destination-count": "929",
                "hidden-route-count": "0",
                "holddown-route-count": "0",
                "rt": [
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.169.196.241/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:23:01"},
                            "announce-bits": "2",
                            "announce-tasks": "0-KRT 7-Resolve tree 3",
                            "as-path": "AS path: I",
                            "bgp-path-attributes": {
                                "attr-as-path-effective": {
                                    "aspath-effective-string": "AS path:",
                                    "attr-value": "I",
                                }
                            },
                            "local-as": "65171",
                            "metric": "1201",
                            "nh": [
                                {
                                    "nh-string": "Next hop",
                                    "session": "141",
                                    "to": "10.169.14.121",
                                    "via": "ge-0/0/1.0",
                                    "weight": "0x1",
                                }
                            ],
                            "nh-address": "0xdfa7934",
                            "nh-index": "613",
                            "nh-reference-count": "458",
                            "nh-type": "Router",
                            "preference": "10",
                            "preference2": "10",
                            "protocol-name": "OSPF",
                            "rt-entry-state": "Active Int",
                            "rt-ospf-area": "0.0.0.8",
                            "task-name": "OSPF",
                            "validation-state": "unverified",
                        },
                        "rt-entry-count": {"#text": "1", "@junos:format": "1 entry"},
                        "rt-state": "FlashAll",
                        "tsi": {
                            "#text": "KRT in-kernel 10.169.196.241/32 -> {10.169.14.121}"
                        },
                    }
                ],
                "table-name": "inet.0",
                "total-route-count": "1615",
            }
        ]
    }
}
