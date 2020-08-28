expected_output = {
    "tag": {
        "core": {
            "system_id": {
                "Genie1A": {
                    "type": {
                        "L1": {
                            "area_address": ["01"],
                            "holdtime": 25,
                            "interface": "TenGigabitEthernet0/3/0",
                            "ip_address": ["10.94.51.9*"],
                            "nsf": "capable",
                            "protocol": "IS-IS //missing neighbor, instead RT2 shows in JSON.",
                            "snpa": "234f.23ff.feec",
                            "state": "up",
                            "uptime": "2w0d",
                        }
                    }
                },
                "Genie1": {
                    "type": {
                        "L1": {
                            "area_address": ["01"],
                            "holdtime": 28,
                            "interface": "GigabitEthernet0/0/7",
                            "ip_address": ["10.166.1.113*"],
                            "nsf": "capable",
                            "protocol": "IS-IS",
                            "snpa": "0230c.22ff.8953",
                            "state": "up",
                            "uptime": "2w0d",
                        }
                    }
                },
                "Genie2": {
                    "type": {
                        "L1": {
                            "area_address": ["01"],
                            "holdtime": 26,
                            "interface": "TenGigabitEthernet0/2/1",
                            "ip_address": ["10.21.1.12*"],
                            "nsf": "capable",
                            "protocol": "IS-IS",
                            "snpa": "34e4.fcff.557d",
                            "state": "up",
                            "uptime": "2w0d",
                        }
                    }
                },
                "Genie3": {
                    "type": {
                        "L1": {
                            "area_address": ["01"],
                            "holdtime": 28,
                            "interface": "TenGigabitEthernet0/2/0",
                            "ip_address": ["10.111.1.0*"],
                            "nsf": "capable",
                            "protocol": "IS-IS",
                            "snpa": "23f1.23ff.7273",
                            "state": "up",
                            "uptime": "1w6d",
                        }
                    }
                },
            }
        }
    }
}
