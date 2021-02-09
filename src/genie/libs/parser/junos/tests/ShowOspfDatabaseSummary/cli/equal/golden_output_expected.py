expected_output = {
    "ospf-database-information": {
        "ospf-database-summary": [
            {
                "ospf-area": "0.0.0.8",
                "ospf-lsa-count": ["12", "2", "79"],
                "ospf-lsa-type": ["Router", "Network", "OpaqArea"],
            },
            {
                "@external-heading": "Externals",
                "ospf-lsa-count": "19",
                "ospf-lsa-type": "Extern",
            },
            {
                "ospf-area": ["0.0.0.8", "0.0.0.8", "0.0.0.8", "0.0.0.8", "0.0.0.8"],
                "ospf-intf": [
                    "ge-0/0/0.0",
                    "ge-0/0/1.0",
                    "ge-0/0/2.0",
                    "ge-0/0/3.0",
                    "lo0.0",
                ],
            },
        ]
    }
}
