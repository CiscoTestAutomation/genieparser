

expected_output = {
    "vrf": {
        "default": {
            "interfaces": {
                "GigabitEthernet0/0/0/2": {
                    "group": {
                        "232.1.1.1": {
                            "host_mode": "include",
                            "last_reporter": "192.168.1.42",
                            "router_mode": "INCLUDE",
                            "router_mode_expires": "None",
                            "up_time": "00:04:55",
                            "source": {
                                "192.168.1.18": {
                                    "up_time": "00:04:55",
                                    "expire": "00:01:28",
                                    "forward": "Yes",
                                    "flags": "Remote"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
