expected_output = {
    "Mgmt-vrf": {
        "vrf_id": 1,
        "interfaces": ["GigabitEthernet0/0"],
        "interface": {"GigabitEthernet0/0": {"vrf": "Mgmt-vrf"}},
        "address_family": {
            "ipv4 unicast": {
                "table_id": "0x1",
                "flags": "0x0",
                "vrf_label": {"allocation_mode": "per-prefix"},
            },
            "ipv6 unicast": {
                "table_id": "0x1E000001",
                "flags": "0x0",
                "vrf_label": {"allocation_mode": "per-prefix"},
            },
        },
        "flags": "0x1808",
        "cli_format": "New",
        "support_af": "multiple address-families",
    },
    "VRF1": {
        "interfaces": ["GigabitEthernet0/0"],
        "interface": {"GigabitEthernet0/0": {"vrf": "VRF1"}},
        "address_family": {
            "ipv4 unicast": {
                "export_to_global": {
                    "export_to_global_map": "export_to_global_map",
                    "prefix_limit": 1000,
                },
                "import_from_global": {
                    "prefix_limit": 1000,
                    "import_from_global_map": "import_from_global_map",
                },
                "table_id": "0x1",
                "routing_table_limit": {
                    "routing_table_limit_action": {
                        "enable_alert_limit_number": {"alert_limit_number": 10000}
                    }
                },
                "route_targets": {
                    "200:1": {"rt_type": "both", "route_target": "200:1"},
                    "100:1": {"rt_type": "both", "route_target": "100:1"},
                },
                "flags": "0x2100",
                "vrf_label": {"allocation_mode": "per-prefix"},
            },
            "ipv6 unicast": {
                "export_to_global": {
                    "export_to_global_map": "export_to_global_map",
                    "prefix_limit": 1000,
                },
                "table_id": "0x1E000001",
                "routing_table_limit": {
                    "routing_table_limit_action": {
                        "enable_alert_percent": {"alert_percent_value": 70},
                        "enable_alert_limit_number": {"alert_limit_number": 7000},
                    },
                    "routing_table_limit_number": 10000,
                },
                "route_targets": {
                    "200:1": {"rt_type": "import", "route_target": "200:1"},
                    "400:1": {"rt_type": "import", "route_target": "400:1"},
                    "300:1": {"rt_type": "export", "route_target": "300:1"},
                    "100:1": {"rt_type": "export", "route_target": "100:1"},
                },
                "flags": "0x100",
                "vrf_label": {"allocation_mode": "per-prefix"},
            },
        },
        "flags": "0x180C",
        "cli_format": "New",
        "support_af": "multiple address-families",
        "route_distinguisher": "100:1",
        "vrf_id": 1,
    },
}
