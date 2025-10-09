expected_output = {
    "autoconfig_status": "Enable",
    "interfaces": {
        "ipv4": {
            "GigabitEthernet1/0/1": {
                "arp_fail": 0,
                "gw_probe": "40F88DE4",
                "ip_address": "20.20.20.33",
                "ping": "431EFB60",
                "ping_fail": 1,
                "rescore": 1,
                "score": 0,
                "state": 14,
                "subnet_mask": "255.255.255.0",
            },
            "GigabitEthernet1/0/2": {
                "arp_fail": 0,
                "gw_probe": "40F88DE4",
                "ip_address": "30.30.30.24",
                "ping": "40F7B4AC",
                "ping_fail": 0,
                "rescore": 0,
                "score": 3,
                "state": 9,
                "subnet_mask": "255.255.255.0",
            },
        },
        "ipv6": {
            "GigabitEthernet1/0/1": {
                "arp_fail": 0,
                "gw_probe": "40F88DE4",
                "ipv6_address": "2001:20::4664:3CFF:FEE7:A64",
                "ping": "431EFB60",
                "ping_fail": 1,
                "prefix": "64",
                "rescore": 0,
                "score": 3,
                "state": 9,
            }
        },
    },
    "ipv4_uplink": {
        "gw_arp_pass_count": 1,
        "interface": "GigabitEthernet1/0/1",
        "ping_pass_count": 0,
    },
    "ipv6_uplink": {
        "gw_arp_pass_count": 9,
        "interface": "GigabitEthernet1/0/1",
        "ping_pass_count": 303,
    },
}
