expected_output = {
    "Mgmt-intf": {
        "vrf_id": 1,
        "flags": "0x1808",
        "cli_format": "New",
        "support_af": "multiple address-families",
        "interface": {"GigabitEthernet1": {"vrf": "Mgmt-intf"}},
        "interfaces": ["GigabitEthernet1"],
        "address_family": {
            "ipv4 unicast": {
                "flags": "0x0",
                "table_id": "0x1",
                "vrf_label": {"allocation_mode": "per-prefix"},
            }
        },
    }
}
