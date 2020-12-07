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
                        "rt-destination": "0.0.0.0/0",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w3d 3:19:36"},
                            "announce-bits": "3",
                            "announce-tasks": "0-KRT 5-LDP 7-Resolve tree 3",
                            "as-path": "AS path: I",
                            "bgp-path-attributes": {
                                "attr-as-path-effective": {
                                    "aspath-effective-string": "AS path:",
                                    "attr-value": "I",
                                }
                            },
                            "local-as": "65171",
                            "metric": "101",
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
                            "preference": "150",
                            "preference2": "10",
                            "protocol-name": "OSPF",
                            "rt-entry-state": "Active Int Ext",
                            "rt-tag": "0",
                            "task-name": "OSPF",
                            "validation-state": "unverified",
                        },
                        "rt-entry-count": {"#text": "1", "@junos:format": "1 entry"},
                        "rt-state": "FlashAll",
                        "tsi": {"#text": "KRT in-kernel 0.0.0.0/0 -> {10.169.14.121}"},
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.1.0.0/24",
                        "rt-entry": [
                            {
                                "active-tag": "*",
                                "age": {"#text": "29w6d 21:42:46"},
                                "announce-bits": "2",
                                "announce-tasks": "5-LDP 7-Resolve tree 3",
                                "as-path": "AS path: I",
                                "bgp-path-attributes": {
                                    "attr-as-path-effective": {
                                        "aspath-effective-string": "AS path:",
                                        "attr-value": "I",
                                    }
                                },
                                "local-as": "65171",
                                "nh": [{"nh-string": "Next hop", "via": "fxp0.0"}],
                                "nh-address": "0xbb69254",
                                "nh-index": "0",
                                "nh-reference-count": "1",
                                "nh-type": "Interface",
                                "preference": "0",
                                "protocol-name": "Direct",
                                "rt-entry-state": "Active Int",
                                "task-name": "IF",
                                "validation-state": "unverified",
                            },
                            {
                                "age": {"#text": "3w3d 3:19:36"},
                                "as-path": "AS path: I",
                                "bgp-path-attributes": {
                                    "attr-as-path-effective": {
                                        "aspath-effective-string": "AS path:",
                                        "attr-value": "I",
                                    }
                                },
                                "inactive-reason": "Route Preference",
                                "local-as": "65171",
                                "metric": "20",
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
                                "preference": "150",
                                "preference2": "10",
                                "protocol-name": "OSPF",
                                "rt-entry-state": "Int Ext",
                                "rt-tag": "0",
                                "task-name": "OSPF",
                                "validation-state": "unverified",
                            },
                        ],
                        "rt-entry-count": {"#text": "2", "@junos:format": "2 entries"},
                        "rt-state": "FlashAll",
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.1.0.101/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "29w6d 21:42:46"},
                            "announce-bits": "2",
                            "announce-tasks": "5-LDP 7-Resolve tree 3",
                            "as-path": "AS path: I",
                            "bgp-path-attributes": {
                                "attr-as-path-effective": {
                                    "aspath-effective-string": "AS path:",
                                    "attr-value": "I",
                                }
                            },
                            "local-as": "65171",
                            "nh-address": "0xbb66c14",
                            "nh-index": "0",
                            "nh-reference-count": "14",
                            "nh-type": "Local",
                            "preference": "0",
                            "protocol-name": "Local",
                            "rt-entry-state": "Active NoReadvrt Int",
                            "task-name": "IF",
                            "validation-state": "unverified",
                        },
                        "rt-entry-count": {"#text": "1", "@junos:format": "1 entry"},
                        "rt-state": "FlashAll",
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.36.3.3/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "1w0d 15:51:32"},
                            "announce-bits": "3",
                            "announce-tasks": "0-KRT 5-LDP 7-Resolve tree 3",
                            "as-path": "AS path: I",
                            "bgp-path-attributes": {
                                "attr-as-path-effective": {
                                    "aspath-effective-string": "AS path:",
                                    "attr-value": "I",
                                }
                            },
                            "local-as": "65171",
                            "metric": "1202",
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
                            "#text": "KRT in-kernel 10.36.3.3/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.16.0.0/30",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w0d 4:46:27"},
                            "announce-bits": "3",
                            "announce-tasks": "0-KRT 5-LDP 7-Resolve tree 3",
                            "as-path": "AS path: I",
                            "bgp-path-attributes": {
                                "attr-as-path-effective": {
                                    "aspath-effective-string": "AS path:",
                                    "attr-value": "I",
                                }
                            },
                            "local-as": "65171",
                            "metric": "1200",
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
                            "#text": "KRT in-kernel 10.16.0.0/30 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.100.5.5/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w0d 4:46:27"},
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
                            "#text": "KRT in-kernel 10.100.5.5/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.220.0.0/16",
                        "rt-entry": [
                            {
                                "active-tag": "*",
                                "announce-bits": "3",
                                "announce-tasks": "0-KRT 6-BGP_RT_Background 7-Resolve tree 3",
                                "as-path": "AS path: (65151 65000) I",
                                "bgp-path-attributes": {
                                    "attr-as-path-effective": {
                                        "aspath-effective-string": "AS path:",
                                        "attr-value": "(65151 65000) I",
                                    }
                                },
                                "gateway": "10.169.14.240",
                                "local-as": "65171",
                                "nh": [
                                    {
                                        "nh-string": "Next hop",
                                        "session": "141",
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0",
                                    }
                                ],
                                "nh-address": "0xdbc5974",
                                "nh-index": "613",
                                "nh-reference-count": "1366",
                                "nh-type": "Router",
                                "peer-as": "65151",
                                "peer-id": "10.169.14.240",
                                "preference": "170",
                                "preference2": "121",
                                "protocol-name": "BGP",
                                "protocol-nh": [
                                    {
                                        "indirect-nh": "0xc285884 1048574 INH Session ID: 0x1ac",
                                        "to": "10.169.14.240",
                                    },
                                    {
                                        "forwarding-nh-count": "1",
                                        "indirect-nh": "0xc285884 1048574 INH Session ID: 0x1ac",
                                        "nh": [
                                            {
                                                "nh-string": "Next hop",
                                                "session": "141",
                                                "to": "10.169.14.121",
                                                "via": "ge-0/0/1.0",
                                            }
                                        ],
                                        "output": "10.169.14.240/32 Originating RIB: inet.0\nNode path count: 1\nForwarding nexthops: 1\nNexthop: 10.169.14.121 via ge-0/0/1.0\n",
                                        "to": "10.169.14.240",
                                    },
                                ],
                                "rt-entry-state": "Active Int Ext",
                                "task-name": "BGP_65172.16.15.14.240",
                                "validation-state": "unverified",
                            },
                            {
                                "as-path": "AS path: (65151 65000) I",
                                "bgp-path-attributes": {
                                    "attr-as-path-effective": {
                                        "aspath-effective-string": "AS path:",
                                        "attr-value": "(65151 65000) I",
                                    }
                                },
                                "gateway": "10.189.5.253",
                                "inactive-reason": "IGP metric",
                                "local-as": "65171",
                                "nh": [
                                    {
                                        "label-element": "0xc5cda38",
                                        "label-element-childcount": "10",
                                        "label-element-lspid": "0",
                                        "label-element-parent": "0x0",
                                        "label-element-refcount": "14",
                                        "nh-string": "Next hop",
                                        "session": "0",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0",
                                        "weight": "0x1",
                                    }
                                ],
                                "nh-address": "0xdfae654",
                                "nh-index": "0",
                                "nh-reference-count": "682",
                                "nh-type": "Router",
                                "peer-as": "65171",
                                "peer-id": "10.189.5.253",
                                "preference": "170",
                                "preference2": "121",
                                "protocol-name": "BGP",
                                "protocol-nh": [
                                    {
                                        "indirect-nh": "0xc285e84 - INH Session ID: 0x0",
                                        "to": "10.189.5.253",
                                    },
                                    {
                                        "forwarding-nh-count": "1",
                                        "indirect-nh": "0xc285e84 - INH Session ID: 0x0",
                                        "metric": "5",
                                        "nh": [
                                            {
                                                "nh-string": "Next hop",
                                                "session": "0",
                                                "to": "10.189.5.94",
                                                "via": "ge-0/0/0.0",
                                                "weight": "0x1",
                                            }
                                        ],
                                        "output": "10.189.5.253/32 Originating RIB: inet.3\nForwarding nexthops: 1\nNexthop: 10.189.5.94 via ge-0/0/0.0\n",
                                        "to": "10.189.5.253",
                                    },
                                ],
                                "rt-entry-state": "Int Ext Changed",
                                "task-name": "BGP_65172.16.220.5.253",
                                "validation-state": "unverified",
                            },
                        ],
                        "rt-entry-count": {"#text": "2", "@junos:format": "2 entries"},
                        "tsi": {
                            "#text": "KRT in-kernel 10.220.0.0/16 -> {indirect(1048574)}\nPage 0 idx 1, (group hktGCS002 type Internal) Type 1 val 0x10c0b9b0 (adv_entry)\nAdvertised metrics:\nFlags: Nexthop Change\nNexthop: Self\nMED: 12003\nLocalpref: 120\nAS path: [65171] (65151 65000) I\nCommunities: 65001:10 65151:244\nPath 10.220.0.0\nfrom 10.169.14.240\nVector len 4.  Val: 1\nCommunities: 65001:10 65151:244\nLocalpref: 120\nCommunities: 65001:10 65151:244\nLocalpref: 120"
                        },
                    },
                ],
                "table-name": "inet.0",
                "total-route-count": "1615",
            }
        ]
    }
}
