expected_output = {
    "ospf3-database-information": {
        "ospf3-area-header": {"ospf-area": "0.0.0.0"},
        "ospf3-database": [
            {
                "lsa-type": "Router",
                "lsa-id": "0.0.0.0",
                "advertising-router": "10.16.2.2",
                "sequence-number": "0x80000002",
                "age": "491",
                "checksum": "0x549c",
                "lsa-length": "40",
                "ospf3-router-lsa": {
                    "bits": "0x0",
                    "ospf3-options": "0x33",
                    "ospf3-link": [
                        {
                            "link-type-name": "PointToPoint",
                            "link-type-value": "1",
                            "link-metric": "1",
                            "link-intf-id": "1",
                            "nbr-intf-id": "1",
                            "nbr-rtr-id": "10.4.1.1",
                        }
                    ],
                    "ospf3-lsa-topology": {
                        "ospf-topology-id": "0",
                        "ospf-topology-name": "default",
                        "ospf3-lsa-topology-link": [
                            {
                                "link-type-name": "PointToPoint",
                                "ospf-lsa-topology-link-node-id": "10.4.1.1",
                                "ospf-lsa-topology-link-metric": "1",
                                "ospf-lsa-topology-link-state": "Bidirectional",
                            }
                        ],
                    },
                },
                "ospf-database-extensive": {
                    "aging-timer": {"#text": "00:51:48"},
                    "expiration-time": {"#text": "00:51:49"},
                    "installation-time": {"#text": "00:08:08"},
                    "send-time": {"#text": "00:08:06"},
                    "lsa-changed-time": {"#text": "00:08:37"},
                    "lsa-change-count": "1",
                },
            },
            {
                "lsa-type": "IntraArPfx",
                "lsa-id": "0.0.0.1",
                "advertising-router": "10.16.2.2",
                "sequence-number": "0x80000003",
                "age": "491",
                "checksum": "0x991d",
                "lsa-length": "64",
                "ospf3-intra-area-prefix-lsa": {
                    "reference-lsa-type": "Router",
                    "reference-lsa-id": "0.0.0.0",
                    "reference-lsa-router-id": "10.16.2.2",
                    "prefix-count": "2",
                    "ospf3-prefix": ["2001:20::/64", "2001::2/128"],
                    "ospf3-prefix-options": ["0x0", "0x2"],
                    "ospf3-prefix-metric": ["1", "0"],
                },
                "ospf-database-extensive": {
                    "aging-timer": {"#text": "00:51:48"},
                    "expiration-time": {"#text": "00:51:49"},
                    "installation-time": {"#text": "00:08:08"},
                    "send-time": {"#text": "00:08:06"},
                    "lsa-changed-time": {"#text": "00:08:39"},
                    "lsa-change-count": "1",
                },
            },
            {
                "lsa-type": "Link",
                "lsa-id": "0.0.0.1",
                "advertising-router": "10.16.2.2",
                "sequence-number": "0x80000001",
                "age": "520",
                "checksum": "0x7045",
                "lsa-length": "56",
                "ospf3-link-lsa": {
                    "linklocal-address": "fe80::250:56ff:fe8d:3f55",
                    "ospf3-options": "0x33",
                    "router-priority": "128",
                    "prefix-count": "1",
                    "ospf3-prefix": "2001:20::/64",
                    "ospf3-prefix-options": "0x0",
                },
                "ospf-database-extensive": {
                    "aging-timer": {"#text": "00:51:19"},
                    "expiration-time": {"#text": "00:51:20"},
                    "installation-time": {"#text": "00:08:37"},
                    "lsa-changed-time": {"#text": "00:08:37"},
                    "lsa-change-count": "1",
                },
            },
        ],
        "ospf3-intf-header": [{"ospf-intf": "ge-0/0/0.0", "ospf-area": "0.0.0.0"}],
    }
}
