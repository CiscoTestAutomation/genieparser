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
                        "rt-destination": "10.16.2.2/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "announce-bits": "2",
                            "announce-tasks": "0-KRT 1-Resolve tree 1",
                            "as-path": "AS path: I",
                            "bgp-path-attributes": {
                                "attr-as-path-effective": {
                                    "aspath-effective-string": "AS path:",
                                    "attr-value": "I",
                                }
                            },
                            "nh": [
                                {
                                    "nh-string": "Next hop",
                                    "to": "10.145.0.2",
                                    "via": "ge-0/0/1.0",
                                }
                            ],
                            "nh-address": "0x9348b50",
                            "nh-index": "590",
                            "nh-reference-count": "19",
                            "nh-type": "Router",
                            "preference": "5",
                            "protocol-name": "Static",
                            "rt-entry-state": "Active Int Ext",
                            "task-name": "RT",
                        },
                        "rt-entry-count": {"#text": "1", "@junos:format": "1 entry"},
                        "tsi": {"#text": "KRT in-kernel 10.16.2.2/32 -> {10.145.0.2}"},
                    }
                ],
                "table-name": "inet.0",
                "total-route-count": "16",
            }
        ]
    }
}
