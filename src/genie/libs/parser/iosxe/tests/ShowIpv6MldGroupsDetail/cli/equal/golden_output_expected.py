expected_output = {
    "vrf": {
        "default": {
            "interface": {
                "GigabitEthernet1": {
                    "group": {
                        "FF15:1::1": {
                            "up_time": "08:14:15",
                            "source": {
                                "2001:DB8:2:2::2": {
                                    "forward": True,
                                    "up_time": "08:13:22",
                                    "flags": "Remote Local 2D",
                                    "expire": "00:06:42",
                                }
                            },
                            "filter_mode": "include",
                            "host_mode": "include",
                            "last_reporter": "FE80::5054:FF:FE7C:DC70",
                        },
                        "FF25:2::1": {
                            "up_time": "08:14:01",
                            "filter_mode": "exclude",
                            "last_reporter": "FE80::5054:FF:FE7C:DC70",
                            "host_mode": "exclude",
                            "expire": "never",
                        },
                        "FF35:1::1": {
                            "up_time": "00:42:41",
                            "source": {
                                "2001:DB8:3:3::3": {
                                    "forward": True,
                                    "up_time": "00:42:41",
                                    "flags": "Remote Local E",
                                    "expire": "00:06:42",
                                }
                            },
                            "filter_mode": "include",
                            "host_mode": "include",
                            "last_reporter": "FE80::5054:FF:FE7C:DC70",
                        },
                        "FF45:1::1": {
                            "up_time": "00:42:32",
                            "filter_mode": "exclude",
                            "last_reporter": "FE80::5054:FF:FE7C:DC70",
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
