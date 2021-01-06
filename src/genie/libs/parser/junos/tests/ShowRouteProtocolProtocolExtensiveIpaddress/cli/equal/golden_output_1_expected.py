expected_output = {
    "route-information": {
        "route-table": {
            "active-route-count": "8",
            "destination-count": "8",
            "hidden-route-count": "0",
            "holddown-route-count": "0",
            "rt": {
                "rt-announced-count": "1",
                "rt-destination": "10.16.2.2",
                "rt-entry": {
                    "active-tag": "*",
                    "age": {"#text": "7:14:16"},
                    "announce-bits": "1",
                    "announce-tasks": "0-KRT",
                    "as-path": "AS path:30000 I",
                    "bgp-path-attributes": {
                        "attr-as-path-effective": {
                            "aspath-effective-string": "AS path:",
                            "attr-value": "30000 I",
                        }
                    },
                    "bgp-rt-flag": "Accepted",
                    "gateway": "10.145.0.3",
                    "local-as": "1",
                    "local-preference": "100",
                    "nh": {
                        "nh-string": "Next hop",
                        "session": "0xe78",
                        "to": "10.145.0.3",
                        "via": "ge-0/0/0.0",
                    },
                    "nh-address": "0xf991014",
                    "nh-index": "604",
                    "nh-reference-count": "2",
                    "nh-type": "Router",
                    "peer-as": "30000",
                    "peer-id": "10.16.2.2",
                    "preference": "170",
                    "preference2": "101",
                    "protocol-name": "BGP",
                    "rt-entry-state": "Active Ext",
                    "task-name": "BGP_30000.10.145.0.3",
                    "validation-state": "unverified",
                },
                "rt-entry-count": {"#text": "1"},
                "rt-prefix-length": "32",
                "tsi": {"#text": "KRT in-kernel 10.16.2.2/32 -> {10.145.0.3}"},
            },
            "table-name": "inet.0",
            "total-route-count": "8",
        }
    }
}
