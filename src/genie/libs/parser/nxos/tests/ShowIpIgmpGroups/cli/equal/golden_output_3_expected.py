expected_output = {
    "vrfs": {
        "MCAST_VRF_A": {
            "total_entries": 4,
            "interface": {
                "Vlan20": {
                    "group": {
                        "230.11.1.1": {
                            "expire": "00:03:01",
                            "type": "D",
                            "up_time": "1d02h",
                            "last_reporter": "10.22.1.10"
                        },
                        "232.11.1.1": {
                            "source": {
                                "10.11.1.10": {
                                    "expire": "00:03:01",
                                    "type": "D",
                                    "up_time": "1d02h",
                                    "last_reporter": "10.22.1.20"
                                }
                            }
                        }
                    }
                },
                "Vlan2": {
                    "group": {
                        "230.11.1.1": {
                            "expire": "00:03:43",
                            "type": "D",
                            "up_time": "1d02h",
                            "last_reporter": "10.23.4.30"
                        },
                        "232.11.1.1": {
                            "source": {
                                "10.11.1.10": {
                                    "expire": "00:03:43",
                                    "type": "D",
                                    "up_time": "1d02h",
                                    "last_reporter": "10.23.4.40"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
