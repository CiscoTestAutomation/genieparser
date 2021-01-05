expected_output = {
    "ospf-database-information": {
        "ospf-area-header": {"ospf-area": "0.0.0.1"},
        "ospf-database": [
            {
                "lsa-type": "Summary",
                "lsa-id": "10.9.0.0",
                "advertising-router": "10.4.1.1",
                "sequence-number": "0x80000005",
                "age": "2388",
                "options": "0x22",
                "checksum": "0x48e8",
                "lsa-length": "28",
                "our-entry": True,
                "ospf-summary-lsa": {
                    "address-mask": "255.255.255.0",
                    "ospf-summary-lsa-topology": {
                        "ospf-topology-name": "default",
                        "ospf-topology-id": "0",
                        "ospf-topology-metric": "1",
                    },
                },
                "ospf-database-extensive": {
                    "generation-timer": {"#text": "00:10:10"},
                    "aging-timer": {"#text": "00:20:12"},
                    "installation-time": {"#text": "00:39:48"},
                    "expiration-time": {"#text": "00:20:12"},
                },
            },
            {
                "lsa-type": "Summary",
                "lsa-id": "10.16.2.2",
                "advertising-router": "10.4.1.1",
                "sequence-number": "0x80000003",
                "age": "1890",
                "options": "0x22",
                "checksum": "0x1519",
                "lsa-length": "28",
                "our-entry": True,
                "ospf-summary-lsa": {
                    "address-mask": "255.255.255.255",
                    "ospf-summary-lsa-topology": {
                        "ospf-topology-name": "default",
                        "ospf-topology-id": "0",
                        "ospf-topology-metric": "1",
                    },
                },
                "ospf-database-extensive": {
                    "generation-timer": {"#text": "00:18:30"},
                    "aging-timer": {"#text": "00:28:30"},
                    "installation-time": {"#text": "00:31:30"},
                    "expiration-time": {"#text": "00:28:30"},
                },
            },
            {
                "lsa-type": "Summary",
                "lsa-id": "10.4.1.1",
                "advertising-router": "10.4.1.1",
                "sequence-number": "0x80000005",
                "age": "1389",
                "options": "0x22",
                "checksum": "0x35fb",
                "lsa-length": "28",
                "our-entry": True,
                "ospf-summary-lsa": {
                    "address-mask": "255.255.255.255",
                    "ospf-summary-lsa-topology": {
                        "ospf-topology-name": "default",
                        "ospf-topology-id": "0",
                        "ospf-topology-metric": "0",
                    },
                },
                "ospf-database-extensive": {
                    "generation-timer": {"#text": "00:26:50"},
                    "aging-timer": {"#text": "00:36:50"},
                    "expiration-time": {"#text": "00:36:51"},
                    "installation-time": {"#text": "00:23:09"},
                    "send-time": {"#text": "00:23:07"},
                },
            },
            {
                "lsa-type": "Summary",
                "lsa-id": "10.229.11.11",
                "advertising-router": "10.4.1.1",
                "sequence-number": "0x80000005",
                "age": "890",
                "options": "0x22",
                "checksum": "0x67a1",
                "lsa-length": "28",
                "our-entry": True,
                "ospf-summary-lsa": {
                    "address-mask": "255.255.255.255",
                    "ospf-summary-lsa-topology": {
                        "ospf-topology-name": "default",
                        "ospf-topology-id": "0",
                        "ospf-topology-metric": "0",
                    },
                },
                "ospf-database-extensive": {
                    "generation-timer": {"#text": "00:35:10"},
                    "aging-timer": {"#text": "00:45:10"},
                    "expiration-time": {"#text": "00:45:10"},
                    "installation-time": {"#text": "00:14:50"},
                    "send-time": {"#text": "00:14:47"},
                },
            },
        ],
    }
}
