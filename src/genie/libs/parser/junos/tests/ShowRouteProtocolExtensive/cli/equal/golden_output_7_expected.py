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
                        "rt-destination": "10.66.12.12/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "9"},
                            "announce-bits": "3",
                            "announce-tasks": "0-KRT 5-BGP_RT_Background 6-Resolve tree 1",
                            "as-path": "AS path: I  (Originator)",
                            "bgp-path-attributes": {
                                "attr-as-path-effective": {
                                    "aspath-effective-string": "AS path:",
                                    "attr-value": "I  (Originator)",
                                }
                            },
                            "cluster-list": "0.0.0.4",
                            "gateway": "10.64.4.4",
                            "local-as": "3",
                            "metric2": "2",
                            "nh": [
                                {
                                    "nh-string": "Next hop",
                                    "session": "1304",
                                    "to": "10.205.0.2",
                                    "via": "ge-0/0/1.0",
                                }
                            ],
                            "nh-address": "0xbb7fff4",
                            "nh-index": "614",
                            "nh-reference-count": "3",
                            "nh-type": "Router",
                            "peer-as": "3",
                            "peer-id": "10.64.4.4",
                            "preference": "170",
                            "preference2": "101",
                            "protocol-name": "BGP",
                            "protocol-nh": [
                                {
                                    "indirect-nh": "0xc296984 1048578 INH Session ID: 0x130c",
                                    "to": "10.16.2.2",
                                },
                                {
                                    "forwarding-nh-count": "1",
                                    "indirect-nh": "0xc296984 1048578 INH Session ID: 0x130c",
                                    "metric": "2",
                                    "nh": [
                                        {
                                            "nh-string": "Next hop",
                                            "session": "1304",
                                            "to": "10.205.0.2",
                                            "via": "ge-0/0/1.0",
                                        }
                                    ],
                                    "output": "10.16.2.2/32 Originating RIB: inet.0\nForwarding nexthops: 1\nNexthop: 10.205.0.2 via ge-0/0/1.0\n",
                                    "to": "10.16.2.2",
                                },
                            ],
                            "rt-entry-state": "Active Int Ext",
                            "task-name": "BGP_10.169.64.4.4",
                            "validation-state": "unverified",
                        },
                        "rt-entry-count": {"#text": "1", "@junos:format": "1 entry"},
                        "tsi": {
                            "#text": "KRT in-kernel 10.66.12.12/32 -> {indirect(1048578)}\nPage 0 idx 1, (group ibgp-DUT type Internal) Type 1 val 0x134b0034 (adv_entry)\nAdvertised metrics:\nNexthop: 10.16.2.2\nLocalpref: 100\nAS path: [3] I (Originator)\nCommunities:\nPath 10.66.12.12\nfrom 10.64.4.4\nVector len 4.  Val: 1\nLocalpref: 100"
                        },
                    }
                ],
                "table-name": "inet.0",
                "total-route-count": "16",
            }
        ]
    }
}
