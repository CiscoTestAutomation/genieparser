expected_output = {
    "ospf3-database-information": {
        "ospf3-area-header": {"ospf-area": "0.0.0.0"},
        "ospf3-database": [
            {
                "advertising-router": "192.168.219.235",
                "age": "892",
                "checksum": "0xf99f",
                "lsa-id": "0.0.0.9",
                "lsa-length": "36",
                "lsa-type": "Network",
                "ospf3-network-lsa": {
                    "attached-router": [
                        "192.168.219.235",
                        "10.69.198.249",
                        "192.168.219.236",
                    ],
                    "ospf3-lsa-topology": {
                        "ospf3-lsa-topology-link": [
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "0",
                                "ospf-lsa-topology-link-node-id": "192.168.219.236",
                                "ospf-lsa-topology-link-state": "Bidirectional",
                            },
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "0",
                                "ospf-lsa-topology-link-node-id": "10.69.198.249",
                                "ospf-lsa-topology-link-state": "Bidirectional",
                            },
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "0",
                                "ospf-lsa-topology-link-node-id": "192.168.219.235",
                                "ospf-lsa-topology-link-state": "Bidirectional",
                            },
                        ]
                    },
                    "ospf3-options": "0x33",
                },
                "our-entry": True,
                "sequence-number": "0x8000001d",
            },
            {
                "advertising-router": "192.168.219.236",
                "age": "2142",
                "checksum": "0x1983",
                "lsa-id": "0.0.0.3",
                "lsa-length": "36",
                "lsa-type": "Network",
                "ospf3-network-lsa": {
                    "attached-router": [
                        "192.168.219.236",
                        "10.69.198.249",
                        "192.168.219.235",
                    ],
                    "ospf3-lsa-topology": {
                        "ospf3-lsa-topology-link": [
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "0",
                                "ospf-lsa-topology-link-node-id": "192.168.219.235",
                                "ospf-lsa-topology-link-state": "Bidirectional",
                            },
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "0",
                                "ospf-lsa-topology-link-node-id": "10.69.198.249",
                                "ospf-lsa-topology-link-state": "Bidirectional",
                            },
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "0",
                                "ospf-lsa-topology-link-node-id": "192.168.219.236",
                                "ospf-lsa-topology-link-state": "Bidirectional",
                            },
                        ]
                    },
                    "ospf3-options": "0x33",
                },
                "sequence-number": "0x80000b14",
            },
            {
                "advertising-router": "192.168.219.236",
                "age": "1092",
                "checksum": "0xa3d1",
                "lsa-id": "0.0.0.4",
                "lsa-length": "32",
                "lsa-type": "Network",
                "ospf3-network-lsa": {
                    "attached-router": ["192.168.219.236", "192.168.219.235"],
                    "ospf3-lsa-topology": {
                        "ospf3-lsa-topology-link": [
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "0",
                                "ospf-lsa-topology-link-node-id": "192.168.219.235",
                                "ospf-lsa-topology-link-state": "Bidirectional",
                            },
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "0",
                                "ospf-lsa-topology-link-node-id": "192.168.219.236",
                                "ospf-lsa-topology-link-state": "Bidirectional",
                            },
                        ]
                    },
                    "ospf3-options": "0x33",
                },
                "sequence-number": "0x80000b11",
            },
            {
                "advertising-router": "192.168.219.236",
                "age": "1692",
                "checksum": "0x8fe3",
                "lsa-id": "0.0.0.6",
                "lsa-length": "32",
                "lsa-type": "Network",
                "ospf3-network-lsa": {
                    "attached-router": ["192.168.219.236", "192.168.219.235"],
                    "ospf3-lsa-topology": {
                        "ospf3-lsa-topology-link": [
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "0",
                                "ospf-lsa-topology-link-node-id": "192.168.219.235",
                                "ospf-lsa-topology-link-state": "Bidirectional",
                            },
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "0",
                                "ospf-lsa-topology-link-node-id": "192.168.219.236",
                                "ospf-lsa-topology-link-state": "Bidirectional",
                            },
                        ]
                    },
                    "ospf3-options": "0x33",
                },
                "sequence-number": "0x80000b11",
            },
        ],
    }
}
