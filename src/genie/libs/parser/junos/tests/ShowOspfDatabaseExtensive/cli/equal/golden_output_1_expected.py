expected_output = {
    "ospf-database-information": {
        "ospf-area-header": {"ospf-area": "0.0.0.8"},
        "ospf-database": [
            {
                "advertising-router": "10.34.2.250",
                "age": "1107",
                "checksum": "0x29f7",
                "lsa-id": "10.34.2.250",
                "lsa-length": "60",
                "lsa-type": "Router",
                "options": "0x22",
                "ospf-database-extensive": {
                    "aging-timer": {"#text": "00:41:32"},
                    "expiration-time": {"#text": "00:41:33"},
                    "installation-time": {"#text": "00:18:24"},
                    "lsa-change-count": "2",
                    "lsa-changed-time": {"#text": "00:18:53"},
                },
                "ospf-router-lsa": {
                    "bits": "0x0",
                    "link-count": "3",
                    "ospf-link": [
                        {
                            "link-data": "10.169.14.158",
                            "link-id": "10.169.14.240",
                            "link-type-name": "PointToPoint",
                            "link-type-value": "1",
                            "metric": "1",
                            "ospf-topology-count": "0",
                        },
                        {
                            "link-data": "10.169.14.158",
                            "link-id": "10.169.14.240",
                            "link-type-name": "PointToPoint",
                            "link-type-value": "1",
                            "metric": "1",
                            "ospf-topology-count": "0",
                        },
                        {
                            "link-data": "255.255.255.252",
                            "link-id": "10.169.14.156",
                            "link-type-name": "Stub",
                            "link-type-value": "3",
                            "metric": "1",
                            "ospf-topology-count": "0",
                        },
                        {
                            "link-data": "255.255.255.252",
                            "link-id": "10.169.14.156",
                            "link-type-name": "Stub",
                            "link-type-value": "3",
                            "metric": "1",
                            "ospf-topology-count": "0",
                        },
                        {
                            "link-data": "255.255.255.255",
                            "link-id": "10.34.2.250",
                            "link-type-name": "Stub",
                            "link-type-value": "3",
                            "metric": "0",
                            "ospf-topology-count": "0",
                        },
                        {
                            "link-data": "255.255.255.255",
                            "link-id": "10.34.2.250",
                            "link-type-name": "Stub",
                            "link-type-value": "3",
                            "metric": "0",
                            "ospf-topology-count": "0",
                        },
                    ],
                    "ospf-lsa-topology": {
                        "ospf-lsa-topology-link": [
                            {
                                "link-type-name": "PointToPoint",
                                "ospf-lsa-topology-link-metric": "1",
                                "ospf-lsa-topology-link-node-id": "10.169.14.240",
                                "ospf-lsa-topology-link-state": "Bidirectional",
                            }
                        ],
                        "ospf-topology-id": "0",
                        "ospf-topology-name": "default",
                    },
                },
                "sequence-number": "0x80000003",
            }
        ],
    }
}
