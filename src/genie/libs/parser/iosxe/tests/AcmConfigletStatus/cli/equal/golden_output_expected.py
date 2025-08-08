expected_output = {
    "configlets": {
        "metatest": {
            "cli_count": 5,
            "configlet_data": [
                "crypto pki certificate pool",
                "ipv6 access-list unmanaged_isolation_v6",
                "sequence 10 deny ipv6 any 2620:10D:C011:3000::/52",
                "sequence 20 deny ipv6 any 2620:10D:C011:4000::/52",
                "sequence 30 permit ipv6 any any"
            ],
            "terminal": "TTY0"
        },
        "metatest2": {
            "cli_count": 4,
            "configlet_data": [
                "ipv6 access-list unmanaged_isolation_v6",
                "sequence 10 deny ipv6 any 2620:10D:C011:3000::/52",
                "sequence 20 deny ipv6 any 2620:10D:C011:4000::/52",
                "sequence 30 permit ipv6 any any"
            ],
            "terminal": "TTY0"
        },
        "mgmt-vrf": {
            "cli_count": 1,
            "configlet_data": [
                "vrf definition Mgmt-vrf"
            ],
            "terminal": "TTY0"
        },
        "s1": {
            "cli_count": 2,
            "configlet_data": [
                "vrf definition Mgmt-vrf",
                "vrf definition Mgmt-vrf"
            ],
            "terminal": "TTY0"
        },
        "s10": {
            "cli_count": 3,
            "configlet_data": [
                "vrf definition Mgmt-vrf",
                "vrf definition red",
                "ip vrf Red"
            ],
            "terminal": "TTY0"
        },
        "skm": {
            "cli_count": 1,
            "configlet_data": [
                "vrf definition Mgmt-vrf"
            ],
            "terminal": "TTY0"
        }
    }
}