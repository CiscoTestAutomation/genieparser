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
                            "age": {"#text": "3w2d 4:46:58"},
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
                        "rt-entry": {
                            "age": {"#text": "3w2d 4:46:58"},
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
                        "rt-entry-count": {"#text": "2", "@junos:format": "2 entries"},
                        "rt-state": "FlashAll",
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.36.3.3/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "age": {"#text": "2w6d 6:13:49"},
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
                            "age": {"#text": "2w6d 6:13:49"},
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
                        "rt-destination": "10.19.198.28/30",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w0d 18:25:19"},
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
                            "metric": "1005",
                            "nh": [
                                {
                                    "nh-string": "Next hop",
                                    "session": "140",
                                    "to": "10.189.5.94",
                                    "via": "ge-0/0/0.0",
                                    "weight": "0x1",
                                }
                            ],
                            "nh-address": "0xdbe48d4",
                            "nh-index": "614",
                            "nh-reference-count": "6",
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
                            "#text": "KRT in-kernel 10.19.198.28/30 -> {10.189.5.94}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.19.198.239/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "1w5d 22:14:58"},
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
                            "metric": "1001",
                            "nh": [
                                {
                                    "nh-string": "Next hop",
                                    "session": "1ae",
                                    "to": "10.19.198.26",
                                    "via": "ge-0/0/2.0",
                                    "weight": "0x1",
                                }
                            ],
                            "nh-address": "0xdbc0d54",
                            "nh-index": "605",
                            "nh-reference-count": "4",
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
                            "#text": "KRT in-kernel 10.19.198.239/32 -> {10.19.198.26}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.174.132.237/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w2d 4:46:58"},
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
                            "metric": "150",
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
                        "tsi": {
                            "#text": "KRT in-kernel 10.174.132.237/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.34.2.200/30",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "2w6d 6:13:49"},
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
                            "metric": "205",
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
                            "#text": "KRT in-kernel 10.34.2.200/30 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.34.2.250/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "2w6d 6:13:49"},
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
                            "metric": "200",
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
                            "#text": "KRT in-kernel 10.34.2.250/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.34.2.251/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "2w6d 6:13:49"},
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
                            "metric": "205",
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
                            "#text": "KRT in-kernel 10.34.2.251/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.15.0.0/30",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "1w5d 22:14:58"},
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
                            "metric": "1001",
                            "nh": [
                                {
                                    "nh-string": "Next hop",
                                    "session": "1ae",
                                    "to": "10.19.198.26",
                                    "via": "ge-0/0/2.0",
                                    "weight": "0x1",
                                }
                            ],
                            "nh-address": "0xdbc0d54",
                            "nh-index": "605",
                            "nh-reference-count": "4",
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
                            "#text": "KRT in-kernel 10.15.0.0/30 -> {10.19.198.26}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.64.0.0/30",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 10.64.0.0/30 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.169.196.212/30",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "2w6d 6:13:49"},
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
                            "#text": "KRT in-kernel 10.169.196.212/30 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.169.196.216/30",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "2w6d 6:13:49"},
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
                            "metric": "1205",
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
                            "#text": "KRT in-kernel 10.169.196.216/30 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.169.196.241/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.169.14.16/30",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w2d 4:46:58"},
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
                            "metric": "105",
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
                            "#text": "KRT in-kernel 10.169.14.16/30 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.169.14.32/30",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "2w6d 5:33:46"},
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
                            "metric": "225",
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
                            "#text": "KRT in-kernel 10.169.14.32/30 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.169.14.128/30",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w0d 18:25:19"},
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
                            "metric": "125",
                            "nh": [
                                {
                                    "nh-string": "Next hop",
                                    "session": "140",
                                    "to": "10.189.5.94",
                                    "via": "ge-0/0/0.0",
                                    "weight": "0x1",
                                }
                            ],
                            "nh-address": "0xdbe48d4",
                            "nh-index": "614",
                            "nh-reference-count": "6",
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
                            "#text": "KRT in-kernel 10.169.14.128/30 -> {10.189.5.94}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.169.14.156/30",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "2w6d 6:13:51"},
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
                            "metric": "200",
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
                            "#text": "KRT in-kernel 10.169.14.156/30 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.169.14.240/32",
                        "rt-entry": {
                            "age": {"#text": "3w2d 4:46:58"},
                            "as-path": "AS path: I",
                            "bgp-path-attributes": {
                                "attr-as-path-effective": {
                                    "aspath-effective-string": "AS path:",
                                    "attr-value": "I",
                                }
                            },
                            "inactive-reason": "Route Preference",
                            "local-as": "65171",
                            "metric": "100",
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
                            "rt-entry-state": "Int",
                            "rt-ospf-area": "0.0.0.8",
                            "task-name": "OSPF",
                            "validation-state": "unverified",
                        },
                        "rt-entry-count": {"#text": "2", "@junos:format": "2 entries"},
                        "rt-state": "FlashAll",
                        "tsi": {
                            "#text": "KRT in-kernel 10.169.14.240/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.169.14.241/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w2d 4:46:58"},
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
                            "metric": "105",
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
                            "#text": "KRT in-kernel 10.169.14.241/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.169.14.242/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w2d 4:46:58"},
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
                            "metric": "100",
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
                            "#text": "KRT in-kernel 10.169.14.242/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.169.14.243/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w2d 4:46:58"},
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
                            "metric": "105",
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
                            "#text": "KRT in-kernel 10.169.14.243/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "10.189.5.253/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w0d 18:25:19"},
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
                            "metric": "5",
                            "nh": [
                                {
                                    "nh-string": "Next hop",
                                    "session": "140",
                                    "to": "10.189.5.94",
                                    "via": "ge-0/0/0.0",
                                    "weight": "0x1",
                                }
                            ],
                            "nh-address": "0xdbe48d4",
                            "nh-index": "614",
                            "nh-reference-count": "6",
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
                            "#text": "KRT in-kernel 10.189.5.253/32 -> {10.189.5.94}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.0/30",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "2w6d 6:13:49"},
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
                            "#text": "KRT in-kernel 192.168.220.0/30 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.0/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.0/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.1/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.1/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.2/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.2/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.3/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.3/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.4/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.4/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.5/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.5/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.6/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.6/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.7/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.7/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.8/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.8/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.9/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.9/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.10/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.10/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.11/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.11/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.12/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.12/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.13/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.13/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.14/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.14/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.15/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.15/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.16/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.16/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.17/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.17/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.18/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.18/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.19/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.19/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.20/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.20/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.21/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.21/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.22/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.22/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.23/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.23/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.24/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.24/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.25/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.25/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.26/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.26/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.27/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.27/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.28/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.28/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.29/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.29/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.30/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.30/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.31/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.31/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.32/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.32/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.33/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.33/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.34/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.34/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.35/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.35/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.36/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.36/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.37/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.37/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.38/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.38/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.39/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.39/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.40/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.40/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.41/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.41/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.42/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.42/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.43/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.43/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.44/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.44/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.45/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.45/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.46/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.46/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.47/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.47/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.48/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.48/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.49/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.49/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.50/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.50/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.51/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.51/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.52/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.52/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.53/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.53/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.54/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.54/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.55/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.55/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.56/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.56/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.57/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.57/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.58/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.58/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.59/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.59/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.60/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.60/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.61/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.61/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.62/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.62/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.63/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.63/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.64/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.64/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.65/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.65/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.66/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.66/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.67/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.67/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.68/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.68/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.69/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.69/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.70/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.70/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.71/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.71/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.72/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.72/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.73/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.73/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.74/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.74/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.75/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.75/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.76/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.76/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.77/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.77/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.78/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.78/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.79/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.79/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.80/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.80/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.81/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.81/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.82/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.82/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.83/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.83/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.84/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.84/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.85/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.85/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.86/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.86/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.87/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.87/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.88/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.88/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.89/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.89/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.90/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.90/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.91/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.91/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.92/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.92/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.93/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.93/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.94/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.94/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.95/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.95/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.96/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.96/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.97/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.97/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.98/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.98/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.99/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.99/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.100/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.100/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.101/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.101/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.102/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.102/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.103/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.103/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.104/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.104/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.105/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.105/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.106/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.106/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.107/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.107/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.108/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.108/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.109/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.109/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.110/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.110/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.111/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.111/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.112/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.112/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.113/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.113/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.114/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.114/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.115/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.115/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.116/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.116/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.117/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.117/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.118/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.118/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.119/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.119/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.120/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.120/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.121/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.121/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.122/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.122/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.123/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.123/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.124/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.124/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.125/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.125/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.126/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.126/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.127/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.127/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.128/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.128/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.129/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.129/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.130/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.130/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.131/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.131/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.132/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.132/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.133/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.133/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.134/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.134/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.135/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.135/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.136/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.136/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.137/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.137/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.138/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.138/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.139/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.139/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.140/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.140/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.141/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.141/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.142/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.142/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.143/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.143/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.144/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.144/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.145/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.145/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.146/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.146/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.147/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.147/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.148/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.148/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.149/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.149/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.150/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.150/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.151/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.151/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.152/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.152/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.153/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.153/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.154/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.154/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.155/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.155/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.156/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.156/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.157/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.157/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.158/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.158/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.159/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.159/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.160/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.160/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.161/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.161/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.162/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.162/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.163/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.163/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.164/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.164/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.165/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.165/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.166/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.166/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.167/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.167/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.168/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.168/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.169/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.169/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.170/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.170/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.171/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.171/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.172/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.172/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.173/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.173/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.174/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.174/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.175/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.175/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.176/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.176/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.177/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.177/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.178/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.178/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.179/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.179/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.180/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.180/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.181/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.181/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.182/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.182/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.183/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.183/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.184/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.184/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.185/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.185/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.186/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.186/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.187/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.187/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.188/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.188/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.189/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.189/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.190/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.190/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.191/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.191/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.192/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.192/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.193/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.193/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.194/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.194/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.195/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.195/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.196/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.196/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.197/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.197/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.198/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.198/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.199/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.199/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.220.200/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.220.200/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.111.0/30",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:54"},
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
                            "#text": "KRT in-kernel 192.168.111.0/30 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.4.0/30",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "6d 17:18:29"},
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
                            "#text": "KRT in-kernel 192.168.4.0/30 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.100.0/25",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "2w5d 16:22:08"},
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
                            "metric": "32000",
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
                            "rt-tag": "65000500",
                            "task-name": "OSPF",
                            "validation-state": "unverified",
                        },
                        "rt-entry-count": {"#text": "2", "@junos:format": "2 entries"},
                        "tsi": {
                            "#text": "KRT in-kernel 192.168.100.0/25 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.100.252/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "2w5d 16:22:08"},
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
                            "metric": "32000",
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
                            "rt-tag": "65000500",
                            "task-name": "OSPF",
                            "validation-state": "unverified",
                        },
                        "rt-entry-count": {"#text": "2", "@junos:format": "2 entries"},
                        "tsi": {
                            "#text": "KRT in-kernel 192.168.100.252/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.36.48/30",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w2d 4:46:58"},
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
                            "metric": "10100",
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
                            "#text": "KRT in-kernel 192.168.36.48/30 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.36.56/30",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w2d 4:46:58"},
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
                            "metric": "10100",
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
                            "#text": "KRT in-kernel 192.168.36.56/30 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.36.119/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w2d 4:46:58"},
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
                            "metric": "10101",
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
                            "#text": "KRT in-kernel 192.168.36.119/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "192.168.36.120/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w2d 4:46:58"},
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
                            "metric": "10101",
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
                            "#text": "KRT in-kernel 192.168.36.120/32 -> {10.169.14.121}"
                        },
                    },
                    {
                        "rt-announced-count": "1",
                        "rt-destination": "224.0.0.5/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "29w5d 23:10:09"},
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
                            "metric": "1",
                            "nh-address": "0xbb66cd4",
                            "nh-index": "0",
                            "nh-reference-count": "9",
                            "nh-type": "MultiRecv",
                            "preference": "10",
                            "protocol-name": "OSPF",
                            "rt-entry-state": "Active NoReadvrt Int",
                            "task-name": "OSPF I/O./var/run/ppmd_control",
                            "validation-state": "unverified",
                        },
                        "rt-entry-count": {"#text": "1", "@junos:format": "1 entry"},
                        "rt-state": "FlashAll",
                        "tsi": {"#text": "KRT in-kernel 224.0.0.5/32 -> {}"},
                    },
                ],
                "table-name": "inet.0",
                "total-route-count": "1615",
            }
        ]
    }
}
