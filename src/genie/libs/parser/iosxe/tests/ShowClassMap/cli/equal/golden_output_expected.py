expected_output = {
    "class_maps": {
        "AutoConf-4.0-Output-Trans-Data-Queue": {
            "match_criteria": "match-any",
            "cm_id": 6,
            "index": {
                1: {
                    "match": {
                        "dscp": [
                            "af21",
                            "af22",
                            "af23"
                        ]
                    }
                },
                2: {
                    "match": {
                        "cos": [
                            "2"
                        ]
                    }
                }
            }
        }
    }
}
