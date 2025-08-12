expected_output = {
    "zone_pair": {
        "in-out": {
            "source_zone": "inside",
            "source_interfaces": [
                "GigabitEthernet0/1/3"
            ],
            "destination_zone": "outside",
            "destination_interfaces": [
                "GigabitEthernet0/1/0"
            ],
            "service_policy": {
                "name": "pmap",
                "class_map": {
                    "nested_cmap": {
                        "match_type": "match-any",
                        "match_criteria": [
                            "match class-map cmap",
                            "match protocol tcp"
                        ],
                        "action": "inspect",
                        "parameter_map": "param"
                    },
                    "class-default": {
                        "match_type": "match-any",
                        "match_criteria": [
                            "match any"
                        ],
                        "action": "drop log",
                        "parameter_map": "Default"
                    }
                }
            }
        }
    }
}