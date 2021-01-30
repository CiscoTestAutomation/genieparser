expected_output = {
    "ospf3-database-information": {
        "ospf3-area-header": {"ospf-area": "0.0.0.0"},
        "ospf3-database": [
            {
                "lsa-type": "Router",
                "lsa-id": "0.0.0.0",
                "advertising-router": "10.16.2.2",
                "sequence-number": "0x80000002",
                "age": "823",
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
                    "aging-timer": {"#text": "00:46:16"},
                    "expiration-time": {"#text": "00:46:17"},
                    "installation-time": {"#text": "00:13:40"},
                    "send-time": {"#text": "00:13:38"},
                    "lsa-changed-time": {"#text": "00:14:09"},
                    "lsa-change-count": "1",
                },
            }
        ],
    }
}
