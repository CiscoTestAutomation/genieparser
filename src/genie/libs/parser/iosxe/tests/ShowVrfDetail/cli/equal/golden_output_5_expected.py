expected_output = {
    "TEST4": {
        "address_family": {
            "ipv4 unicast": {
                "import_route_map": "import-test-map",
                "export_route_map": "export-test-map",
                "flags": "0x0",
                "route_targets": {
                    "9999:1390": {
                        "route_target": "9999:1390",
                        "rt_type": "import"
                    },
                    "9999:1391": {
                        "route_target": "9999:1391",
                        "rt_type": "export"
                    },
                    "9999:200": {
                        "route_target": "9999:200",
                        "rt_type": "import"
                    },
                    "9999:4120": {
                        "route_target": "9999:4120",
                        "rt_type": "both"
                    }
                },
                "table_id": "0x13",
                "vrf_label": {
                    "allocation_mode": "per-prefix"
                }
            }
        },
        "cli_format": "Old",
        "flags": "0xC",
        "interface": {
            "Loopback239": {
                "vrf": "TEST4"
            }
        },
        "interfaces": [
            "Loopback239"
        ],
        "route_distinguisher": "9999:4120",
        "support_af": "IPv4 only",
        "vrf_id": 19
    }
}