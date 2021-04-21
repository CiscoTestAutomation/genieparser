expected_output = {
    "vrf": {
        "VRF1": {
            "interface": {
                "GigabitEthernet2": {
                    "group": {
                        "FF15:1::1": {
                            "up_time": "08:14:20",
                            "source": {
                                "2001:DB8:2:2::2": {
                                    "forward": True,
                                    "up_time": "08:13:56",
                                    "flags": "Remote Local 2D",
                                    "expire": "00:12:23",
                                }
                            },
                            "filter_mode": "include",
                            "host_mode": "include",
                            "last_reporter": "FE80::5054:FF:FEDD:BB49",
                        },
                        "FF25:2::1": {
                            "up_time": "08:14:18",
                            "filter_mode": "exclude",
                            "last_reporter": "FE80::5054:FF:FEDD:BB49",
                            "host_mode": "exclude",
                            "expire": "never",
                        },
                        "FF35:1::1": {
                            "up_time": "00:42:30",
                            "source": {
                                "2001:DB8:3:3::3": {
                                    "forward": True,
                                    "up_time": "00:42:30",
                                    "flags": "Remote Local E",
                                    "expire": "00:12:23",
                                }
                            },
                            "filter_mode": "include",
                            "host_mode": "include",
                            "last_reporter": "FE80::5054:FF:FEDD:BB49",
                        },
                        "FF45:1::1": {
                            "up_time": "00:42:30",
                            "filter_mode": "exclude",
                            "last_reporter": "FE80::5054:FF:FEDD:BB49",
                            "host_mode": "exclude",
                            "expire": "never",
                        },
                    },
                    "join_group": {
                        "FF15:1::1 2001:DB8:2:2::2": {
                            "group": "FF15:1::1",
                            "source": "2001:DB8:2:2::2",
                        }
                    },
                    "static_group": {
                        "FF35:1::1 2001:DB8:3:3::3": {
                            "group": "FF35:1::1",
                            "source": "2001:DB8:3:3::3",
                        }
                    },
                }
            }
        }
    }
}
