expected_output = {
    "route-information": {
        "route-table": {
            "active-route-count": "1250009",
            "destination-count": "1250009",
            "hidden-route-count": "0",
            "holddown-route-count": "0",
            "rt": {
                "rt-announced-count": "1",
                "rt-destination": "10.55.0.0",
                "rt-entry": {
                    "active-tag": "*",
                    "age": {"#text": "4:32"},
                    "announce-bits": "2",
                    "announce-tasks": "0-KRT 1-BGP_RT_Background",
                    "as-path": "AS path:2 I",
                    "bgp-path-attributes": {
                        "attr-as-path-effective": {
                            "aspath-effective-string": "AS path:",
                            "attr-value": "2 I",
                        }
                    },
                    "bgp-rt-flag": "Accepted",
                    "gateway": "10.30.0.2",
                    "local-as": "1",
                    "local-preference": "100",
                    "nh": {
                        "nh-string": "Next hop",
                        "session": "0xf44",
                        "to": "10.30.0.2",
                        "via": "ge-0/0/2.0",
                    },
                    "nh-address": "0x17b226b4",
                    "nh-index": "605",
                    "nh-reference-count": "800002",
                    "nh-type": "Router",
                    "peer-as": "2",
                    "peer-id": "192.168.19.1",
                    "preference": "170",
                    "preference2": "101",
                    "protocol-name": "BGP",
                    "rt-entry-state": "Active Ext",
                    "task-name": "BGP_10.144.30.0.2",
                    "validation-state": "unverified",
                },
                "rt-entry-count": {"#text": "1"},
                "rt-prefix-length": "32",
                "tsi": {"#text": "KRT in-kernel 10.55.0.0/32 -> {10.30.0.2}"},
            },
            "table-name": "inet.0",
            "total-route-count": "1250009",
        }
    }
}
