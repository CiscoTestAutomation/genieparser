expected_output = {
    "VRF1": {
        "address_family": {
            "ipv4 unicast": {
                "flags": "0x0",
                "route_targets": {
                    "100:1": {"route_target": "100:1", "rt_type": "both"}
                },
                "table_id": "0x1",
                "vrf_label": {"allocation_mode": "per-prefix"},
            },
            "ipv6 unicast": {
                "flags": "0x0",
                "route_targets": {
                    "100:1": {"route_target": "100:1", "rt_type": "both"}
                },
                "table_id": "0x1E000001",
                "vrf_label": {"allocation_mode": "per-prefix"},
            },
        },
        "cli_format": "New",
        "flags": "0x180C",
        "interfaces": ["Loopback1", "GigabitEthernet0/4.200"],
        "interface": {
            "Loopback1": {"vrf": "VRF1"},
            "GigabitEthernet0/4.200": {"vrf": "VRF1"},
        },
        "route_distinguisher": "100:1",
        "support_af": "multiple address-families",
        "vrf_id": 1,
    },
    "VRF2": {
        "address_family": {
            "ipv4 unicast": {
                "flags": "0x0",
                "table_id": "0x2",
                "vrf_label": {"allocation_mode": "per-prefix"},
            },
            "ipv6 unicast": {
                "flags": "0x0",
                "table_id": "0x1E000002",
                "vrf_label": {"allocation_mode": "per-prefix"},
            },
        },
        "cli_format": "New",
        "flags": "0x1808",
        "support_af": "multiple address-families",
        "vrf_id": 2,
    },
}
