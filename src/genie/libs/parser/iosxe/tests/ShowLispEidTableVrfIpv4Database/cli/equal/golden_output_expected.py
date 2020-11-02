expected_output = {
    "vrf": {
        "User": {
            "iid": 4100,
            "lsb": "0x3",
            "total_entries": 3,
            "no_route": 0,
            "inactive": 0,
            "eid": {
                "10.16.0.0/19": {
                    "locator_set": [
                        "rloc_5823c743-d29b-40d4-a063-8a29881a59b2",
                        "auto-discover-rlocs",
                        "proxy"
                    ],
                    "rlocs": {
                        "10.8.190.11": {
                            "priority": 10,
                            "weight": 10,
                            "source": "cfg-intf",
                            "state": [
                                "site-self",
                                "reachable"
                            ]
                        },
                        "10.8.190.17": {
                            "priority": 10,
                            "weight": 10,
                            "source": "auto-disc",
                            "state": [
                                "site-other",
                                "report-reachable"
                            ]
                        }
                    }
                },
                "10.16.32.0/20": {
                    "locator_set": [
                        "rloc_5823c743-d29b-40d4-a063-8a29881a59b2",
                        "auto-discover-rlocs",
                        "proxy"
                    ],
                    "rlocs": {
                        "10.8.190.11": {
                            "priority": 10,
                            "weight": 10,
                            "source": "cfg-intf",
                            "state": [
                                "site-self",
                                "reachable"
                            ]
                        },
                        "10.8.190.17": {
                            "priority": 10,
                            "weight": 10,
                            "source": "auto-disc",
                            "state": [
                                "site-other",
                                "report-reachable"
                            ]
                        }
                    }
                },
                "10.16.48.0/24": {
                    "locator_set": [
                        "rloc_5823c743-d29b-40d4-a063-8a29881a59b2",
                        "auto-discover-rlocs",
                        "proxy"
                    ],
                    "rlocs": {
                        "10.8.190.11": {
                            "priority": 10,
                            "weight": 10,
                            "source": "cfg-intf",
                            "state": [
                                "site-self",
                                "reachable"
                            ]
                        },
                        "10.8.190.17": {
                            "priority": 10,
                            "weight": 10,
                            "source": "auto-disc",
                            "state": [
                                "site-other",
                                "report-reachable"
                            ]
                        }
                    }
                }
            }
        }
    }
}