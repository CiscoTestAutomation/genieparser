expected_output = {
    "vrf": {
        "default": {
            "interface": {
                "Vlan210": {
                    "group": {
                        "224.0.1.39": {
                            "expire": "00:01:29",
                            "up_time": "1w0d",
                            "group_mode": "exclude",
                            "last_reporter": "192.168.135.2",
                        },
                        "227.1.1.1": {
                            "expire": "00:02:25",
                            "up_time": "1w0d",
                            "group_mode": "exclude",
                            "last_reporter": "192.168.135.4",
                        },
                        "225.1.1.1": {
                            "expire": "00:02:26",
                            "up_time": "1w0d",
                            "group_mode": "exclude",
                            "last_reporter": "192.168.135.4",
                        },
                        "226.1.1.1": {
                            "expire": "00:02:22",
                            "up_time": "1w0d",
                            "group_mode": "exclude",
                            "last_reporter": "192.168.135.4",
                        },
                    }
                },
                "Loopback10": {
                    "join_group": {
                        "224.0.1.40 *": {
                            "expire": "00:02:08",
                            "source": "*",
                            "group": "224.0.1.40",
                            "flags": "L U",
                            "up_time": "1w0d",
                            "last_reporter": "192.168.151.1",
                        }
                    },
                    "group": {
                        "224.0.1.40": {
                            "expire": "00:02:08",
                            "last_reporter": "192.168.151.1",
                            "up_time": "1w0d",
                            "group_mode": "exclude",
                            "flags": "L U",
                        }
                    },
                },
                "Vlan211": {
                    "static_group": {
                        "239.1.1.1 *": {
                            "expire": "00:02:29",
                            "source": "*",
                            "group": "239.1.1.1",
                            "flags": "L U SG",
                            "up_time": "4d11h",
                            "last_reporter": "192.168.76.1",
                        }
                    },
                    "join_group": {
                        "239.1.1.1 *": {
                            "expire": "00:02:29",
                            "source": "*",
                            "group": "239.1.1.1",
                            "flags": "L U SG",
                            "up_time": "4d11h",
                            "last_reporter": "192.168.76.1",
                        }
                    },
                    "group": {
                        "224.0.1.39": {
                            "expire": "00:02:30",
                            "up_time": "1w0d",
                            "group_mode": "exclude",
                            "last_reporter": "192.168.76.2",
                        },
                        "232.1.1.1": {
                            "last_reporter": "192.168.76.4",
                            "up_time": "1w0d",
                            "group_mode": "include",
                            "flags": "SSM",
                        },
                        "239.1.1.1": {
                            "expire": "00:02:29",
                            "last_reporter": "192.168.76.1",
                            "up_time": "4d11h",
                            "group_mode": "exclude",
                            "flags": "L U SG",
                        },
                    },
                },
            }
        }
    }
}
