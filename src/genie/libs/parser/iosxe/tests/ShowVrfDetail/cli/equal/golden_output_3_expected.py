expected_output = {
    "GENIE-BACKUP": {
        "address_family": {
            "ipv4 unicast": {
                "flags": "0x0",
                "route_targets": {
                    "50998:1": {"route_target": "50998:1", "rt_type": "export"},
                    "50998:106": {"route_target": "50998:106", "rt_type": "both"},
                    "50998:4094": {"route_target": "50998:4094", "rt_type": "import"},
                },
                "table_id": "0xC",
                "vrf_label": {"allocation_mode": "per-prefix"},
            }
        },
        "cli_format": "New",
        "description": "VPN for CHRH (Backup network)",
        "flags": "0x180C",
        "interface": {"BDI106": {"vrf": "GENIE-BACKUP"}},
        "interfaces": ["BDI106"],
        "route_distinguisher": "50998:106",
        "support_af": "multiple address-families",
        "vrf_id": 12,
    },
    "GENIE-LAB": {
        "address_family": {
            "ipv4 unicast": {
                "flags": "0x0",
                "route_targets": {
                    "50998:11": {"route_target": "50998:11", "rt_type": "both"}
                },
                "table_id": "0x4C",
                "vrf_label": {"allocation_mode": "per-prefix"},
            },
            "ipv6 unicast": {
                "flags": "0x0",
                "route_targets": {
                    "50998:11": {"route_target": "50998:11", "rt_type": "both"}
                },
                "table_id": "0x1E000003",
                "vrf_label": {"allocation_mode": "per-prefix"},
            },
        },
        "cli_format": "New",
        "description": "VPN for Internet Direct Link Out (Internal FW)",
        "flags": "0x180C",
        "interface": {
            "TenGigabitEthernet0/1/1.11": {"vrf": "GENIE-LAB"},
            "vasiright110": {"vrf": "GENIE-LAB"},
            "vasiright92": {"vrf": "GENIE-LAB"},
        },
        "interfaces": ["TenGigabitEthernet0/1/1.11", "vasiright92", "vasiright110"],
        "route_distinguisher": "50998:11",
        "support_af": "multiple address-families",
        "vrf_id": 76,
    },
    "GENIE-PROD": {
        "address_family": {
            "ipv4 unicast": {
                "flags": "0x0",
                "route_targets": {
                    "50998:1": {"route_target": "50998:1", "rt_type": "export"},
                    "50998:110": {"route_target": "50998:110", "rt_type": "both"},
                    "50998:4094": {"route_target": "50998:4094", "rt_type": "import"},
                },
                "table_id": "0x11",
                "vrf_label": {"allocation_mode": "per-prefix"},
            }
        },
        "cli_format": "New",
        "description": "VPN for Dame Blanche",
        "flags": "0x180C",
        "interface": {
            "GigabitEthernet0/0/0.110": {"vrf": "GENIE-PROD"},
            "TenGigabitEthernet0/1/2.1042": {"vrf": "GENIE-PROD"},
            "vasileft110": {"vrf": "GENIE-PROD"},
        },
        "interfaces": [
            "GigabitEthernet0/0/0.110",
            "TenGigabitEthernet0/1/2.1042",
            "vasileft110",
        ],
        "route_distinguisher": "50998:110",
        "support_af": "multiple address-families",
        "vrf_id": 17,
    },
}
