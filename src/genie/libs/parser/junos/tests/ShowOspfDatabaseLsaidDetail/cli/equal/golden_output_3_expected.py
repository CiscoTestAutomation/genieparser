expected_output = {
    "ospf-database-information": {
        "ospf-area-header": {"ospf-area": "0.0.0.0"},
        "ospf-database": [
            {
                "advertising-router": "10.36.3.3",
                "age": "64",
                "checksum": "0x9958",
                "lsa-id": "10.145.0.3",
                "lsa-length": "36",
                "lsa-type": "Network",
                "options": "0x22",
                "ospf-network-lsa": {
                    "address-mask": "255.255.255.0",
                    "attached-router": ["10.36.3.3", "10.64.4.4", "10.4.1.1"],
                    "ospf-lsa-topology": {
                        "ospf-lsa-topology-link": [
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "0",
                                "ospf-lsa-topology-link-node-id": "10.4.1.1",
                                "ospf-lsa-topology-link-state": "Bidirectional",
                            },
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "0",
                                "ospf-lsa-topology-link-node-id": "10.64.4.4",
                                "ospf-lsa-topology-link-state": "Bidirectional",
                            },
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "0",
                                "ospf-lsa-topology-link-node-id": "10.36.3.3",
                                "ospf-lsa-topology-link-state": "Bidirectional",
                            },
                        ],
                        "ospf-topology-id": "0",
                        "ospf-topology-name": "default",
                    },
                },
                "our-entry": True,
                "sequence-number": "0x80000002",
            }
        ],
    }
}
