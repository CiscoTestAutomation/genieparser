expected_output = {
    "ospf-database-information": {
        "ospf-area-header": {"ospf-area": "192.168.76.0"},
        "ospf-database": {
            "@heading": "Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len",
            "advertising-router": "192.168.219.235",
            "age": "1730",
            "checksum": "0x1b56",
            "lsa-id": "10.69.197.1",
            "lsa-length": "36",
            "lsa-type": "Network",
            "options": "0x22",
            "ospf-network-lsa": {
                "address-mask": "255.255.255.128",
                "attached-router": [
                    "192.168.219.235",
                    "10.69.198.249",
                    "192.168.219.236",
                ],
                "ospf-lsa-topology": {
                    "ospf-lsa-topology-link": [
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
                    ],
                    "ospf-topology-id": "default",
                    "ospf-topology-name": "default",
                },
            },
            "our-entry": True,
            "sequence-number": "0x80000026",
        },
    }
}
