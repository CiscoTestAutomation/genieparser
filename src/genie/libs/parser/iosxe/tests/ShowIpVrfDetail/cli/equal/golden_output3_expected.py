expected_output = {
    "Mgmt-intf": {
        "vrf_id": 1,
        "cli_format": "New",
        "support_af": "multiple address-families",
        "flags": "0x1808",
        "interfaces": ["GigabitEthernet0"],
        "interface": {"GigabitEthernet0": {"vrf": "Mgmt-intf"}},
        "address_family": {
            "none": {
                "table_id": "1",
                "flags": "0x0",
                "vrf_label": {"allocation_mode": "per-prefix"},
            }
        },
    }
}
