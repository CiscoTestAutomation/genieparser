expected_output = {
    "GENIE": {
        "address_family": {
            "ipv4 unicast": {
                "flags": "0x0",
                "route_targets": {
                    "65109:1": {"route_target": "65109:1", "rt_type": "export"},
                    "65109:110": {"route_target": "65109:110", "rt_type": "both"},
                    "65109:4094": {"route_target": "65109:4094", "rt_type": "import"},
                },
                "table_id": "0x11",
                "vrf_label": {"allocation_mode": "per-prefix"},
            }
        },
        "cli_format": "New",
        "description": "VPN for GENIE parser",
        "flags": "0x180C",
        "interface": {
            "GigabitEthernet0/0/0.110": {"vrf": "GENIE"},
            "TenGigabitEthernet0/1/2.1042": {"vrf": "GENIE"},
            "vasileft110": {"vrf": "GENIE"},
        },
        "interfaces": [
            "GigabitEthernet0/0/0.110",
            "TenGigabitEthernet0/1/2.1042",
            "vasileft110",
        ],
        "route_distinguisher": "65109:110",
        "support_af": "multiple address-families",
        "vrf_id": 17,
    }
}
