expected_output = {
    "tag": {
        "test": {
            "system_id": {
                "R2_xr": {
                    "type": {
                        "L1L2": {
                            "holdtime": 26,
                            "state": "up",
                            "snpa": "fa16.3eff.9418",
                            "protocol": "M-ISIS",
                            "interface": "GigabitEthernet2.115",
                            "area_address": ["49.0001"],
                            "ip_address": ["10.12.115.2*"],
                            "ipv6_address": ["FE80::F816:3EFF:FEFF:9418"],
                            "uptime": "3d21h",
                            "nsf": "capable",
                            "topology": ["ipv4", "ipv6"],
                        }
                    }
                },
                "R3_nx": {
                    "type": {
                        "L1L2": {
                            "holdtime": 29,
                            "state": "up",
                            "snpa": "5e00.80ff.0209",
                            "protocol": "M-ISIS",
                            "interface": "GigabitEthernet3.115",
                            "area_address": ["49.0001"],
                            "ip_address": ["10.13.115.3*"],
                            "ipv6_address": ["FE80::5C00:80FF:FEFF:209"],
                            "uptime": "3d21h",
                            "nsf": "capable",
                            "topology": ["ipv4", "ipv6"],
                        }
                    }
                },
            }
        },
        "test1": {
            "system_id": {
                "2222.22ff.4444": {
                    "type": {
                        "L1L2": {
                            "holdtime": 29,
                            "state": "init",
                            "snpa": "fa16.3eff.9418",
                            "protocol": "M-ISIS",
                            "interface": "GigabitEthernet2.415",
                            "area_address": ["49.0001"],
                            "ip_address": ["10.12.115.2*"],
                            "ipv6_address": ["FE80::F816:3EFF:FEFF:9418"],
                            "uptime": "3d21h",
                            "nsf": "capable",
                            "topology": ["ipv4", "ipv6"],
                        }
                    }
                },
                "R3_nx": {
                    "type": {
                        "L1L2": {
                            "holdtime": 29,
                            "state": "up",
                            "snpa": "5e00.80ff.0209",
                            "protocol": "M-ISIS",
                            "interface": "GigabitEthernet3.415",
                            "area_address": ["49.0001"],
                            "ip_address": ["10.13.115.3*"],
                            "ipv6_address": ["FE80::5C00:80FF:FEFF:209"],
                            "uptime": "3d21h",
                            "nsf": "capable",
                            "topology": ["ipv4", "ipv6"],
                        }
                    }
                },
            }
        },
    }
}
