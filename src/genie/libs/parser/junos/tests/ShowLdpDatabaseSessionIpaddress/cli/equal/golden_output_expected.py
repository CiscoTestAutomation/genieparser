expected_output = {
    "ldp-database-information": {
        "ldp-database": [
            {
                "ldp-binding": [
                    {"ldp-label": "3", "ldp-prefix": "10.34.2.250/32"},
                    {"ldp-label": "16", "ldp-prefix": "10.169.14.240/32"},
                ],
                "ldp-database-type": "Input label database",
                "ldp-label-received": "2",
                "ldp-session-id": "10.169.14.240:0--10.34.2.250:0",
            },
            {
                "ldp-binding": [
                    {"ldp-label": "16", "ldp-prefix": "10.34.2.250/32"},
                    {"ldp-label": "3", "ldp-prefix": "10.169.14.240/32"},
                ],
                "ldp-database-type": "Output label database",
                "ldp-label-advertised": "2",
                "ldp-session-id": "10.169.14.240:0--10.34.2.250:0",
            },
        ]
    }
}
