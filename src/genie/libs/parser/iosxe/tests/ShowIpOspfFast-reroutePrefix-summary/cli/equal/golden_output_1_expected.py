expected_output = {
    "process_id": "100",
    "router_id": "40.0.0.1",
    "topology": {
        "mtid": "0",
        "areas": {
            "0": {
                "interfaces": {
                    "Gi0/0/6": {
                        "protected": True,
                        "primary_paths": {
                            "all": 2,
                            "high": 1,
                            "low": 1
                        },
                        "protected_paths": {
                            "all": 2,
                            "high": 1,
                            "low": 1
                        },
                        "percent_protected": {
                            "all": "100%",
                            "high": "100%",
                            "low": "100%"
                        }
                    },
                    "Gi0/0/7": {
                        "protected": True,
                        "primary_paths": {
                            "all": 2,
                            "high": 1,
                            "low": 1
                        },
                        "protected_paths": {
                            "all": 2,
                            "high": 1,
                            "low": 1
                        },
                        "percent_protected": {
                            "all": "100%",
                            "high": "100%",
                            "low": "100%"
                        }
                    }
                },
                "area_total": {
                    "primary_paths": {
                        "all": 4,
                        "high": 2,
                        "low": 2
                    },
                    "protected_paths": {
                        "all": 4,
                        "high": 2,
                        "low": 2
                    },
                    "percent_protected": {
                        "all": "100%",
                        "high": "100%",
                        "low": "100%"
                    }
                }
            }
        },
        "process_total": {
            "primary_paths": {
                "all": 4,
                "high": 2,
                "low": 2
            },
            "protected_paths": {
                "all": 4,
                "high": 2,
                "low": 2
            },
            "percent_protected": {
                "all": "100%",
                "high": "100%",
                "low": "100%"
            }
        }
    }
}