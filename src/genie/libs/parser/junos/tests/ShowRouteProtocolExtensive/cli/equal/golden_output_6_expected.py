expected_output = {
    "route-information": {
        "route-table": [
            {
                "active-route-count": "13",
                "destination-count": "13",
                "hidden-route-count": "0",
                "holddown-route-count": "0",
                "rt": [
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.55.0.1/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "13"},
                            "announce-bits": "2",
                            "announce-tasks": "0-KRT 5-Resolve tree 1",
                            "as-path": "AS path: I  (Originator)",
                            "bgp-path-attributes": {
                                "attr-as-path-effective": {
                                    "aspath-effective-string": "AS path:",
                                    "attr-value": "I  (Originator)",
                                }
                            },
                            "cluster-list": "10.16.2.2 10.64.4.4",
                            "gateway": "10.16.2.2",
                            "local-as": "2",
                            "metric2": "3",
                            "nh": [
                                {
                                    "nh-string": "Next hop",
                                    "session": "3bf",
                                    "to": "10.145.0.2",
                                    "via": "ge-0/0/0.0",
                                }
                            ],
                            "nh-address": "0xbb68bf4",
                            "nh-index": "595",
                            "nh-reference-count": "4",
                            "nh-type": "Router",
                            "peer-as": "2",
                            "peer-id": "10.16.2.2",
                            "preference": "170",
                            "preference2": "101",
                            "protocol-name": "BGP",
                            "protocol-nh": [
                                {
                                    "indirect-nh": "0xc298604 1048574 INH Session ID: 0x3c1",
                                    "to": "10.100.5.5",
                                },
                                {
                                    "forwarding-nh-count": "1",
                                    "indirect-nh": "0xc298604 1048574 INH Session ID: 0x3c1",
                                    "metric": "3",
                                    "nh": [
                                        {
                                            "nh-string": "Next hop",
                                            "session": "3bf",
                                            "to": "10.145.0.2",
                                            "via": "ge-0/0/0.0",
                                        }
                                    ],
                                    "output": "10.100.5.5/32 Originating RIB: inet.0\nForwarding nexthops: 1\nNexthop: 10.145.0.2 via ge-0/0/0.0\nSession Id: 3bf\n",
                                    "to": "10.100.5.5",
                                },
                            ],
                            "rt-entry-state": "Active Int Ext",
                            "task-name": "BGP_10.16.2.2.2",
                            "validation-state": "unverified",
                        },
                        "rt-entry-count": {"#text": "1", "@junos:format": "1 entry"},
                        "tsi": {
                            "#text": "KRT in-kernel 10.55.0.1/32 -> {indirect(1048574)}\nLocalpref: 100"
                        },
                    }
                ],
                "table-name": "inet.0",
                "total-route-count": "13",
            }
        ]
    }
}
