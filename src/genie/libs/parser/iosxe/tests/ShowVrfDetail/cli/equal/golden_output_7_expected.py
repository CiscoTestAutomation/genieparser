expected_output = {
    "TESTINGVNI": {
        "vrf_id": 4,
        "cli_format": "New",
        "support_af": "multiple address-families",
        "vnid": "30022",
        "vni": "4096",
        "core_vlan": "300",
        "flags": "0x1808",
        "interfaces": [
            "Vlan300",
            "Address",
            "family",
            "Ipv4",
            "unicast",
            "not",
            "active",
            "Address",
            "family",
            "Ipv6",
            "unicast",
            "not",
            "active",
            "Address",
            "family",
            "Ipv4",
            "multicast",
            "not",
            "active",
            "Address",
            "family",
            "Ipv6",
            "multicast",
            "not",
            "active"
        ],
        "interface": {
            "Vlan300": {
                "vrf": "TESTINGVNI"
            },
            "Address": {
                "vrf": "TESTINGVNI"
            },
            "family": {
                "vrf": "TESTINGVNI"
            },
            "Ipv4": {
                "vrf": "TESTINGVNI"
            },
            "unicast": {
                "vrf": "TESTINGVNI"
            },
            "not": {
                "vrf": "TESTINGVNI"
            },
            "active": {
                "vrf": "TESTINGVNI"
            },
            "Ipv6": {
                "vrf": "TESTINGVNI"
            },
            "multicast": {
                "vrf": "TESTINGVNI"
            }
        }
    }
}
