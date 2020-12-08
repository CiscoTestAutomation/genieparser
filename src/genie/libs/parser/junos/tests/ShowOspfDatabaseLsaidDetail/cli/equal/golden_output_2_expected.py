expected_output = {
    "ospf-database-information": {
        "ospf-database": [
            {
                "advertising-router": "10.169.14.240",
                "age": "1075",
                "checksum": "0xd7f4",
                "lsa-id": "10.34.2.250",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "ospf-external-lsa": {
                    "address-mask": "255.255.255.255",
                    "ospf-external-lsa-topology": {
                        "forward-address": "0.0.0.0",
                        "ospf-topology-id": "0",
                        "ospf-topology-metric": "50",
                        "ospf-topology-name": "default",
                        "tag": "10.166.34.12",
                        "type-value": "1",
                    },
                },
                "sequence-number": "0x80000043",
            },
            {
                "advertising-router": "10.169.14.241",
                "age": "670",
                "checksum": "0xcffa",
                "lsa-id": "10.34.2.250",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "ospf-external-lsa": {
                    "address-mask": "255.255.255.255",
                    "ospf-external-lsa-topology": {
                        "forward-address": "0.0.0.0",
                        "ospf-topology-id": "0",
                        "ospf-topology-metric": "50",
                        "ospf-topology-name": "default",
                        "tag": "10.166.34.12",
                        "type-value": "1",
                    },
                },
                "our-entry": True,
                "sequence-number": "0x80000044",
            },
        ]
    }
}
