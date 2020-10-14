expected_output = {
    "Mgmt-intf": {
        "address_family": {
            "ipv4 unicast": {
                "flags": "0x0",
                "table_id": "0x1",
                "vrf_label": {"allocation_mode": "per-prefix"},
            }
        },
        "cli_format": "New",
        "flags": "0x1808",
        "interface": {"GigabitEthernet1": {"vrf": "Mgmt-intf"}},
        "interfaces": ["GigabitEthernet1"],
        "support_af": "multiple address-families",
        "vrf_id": 1,
    }
}
