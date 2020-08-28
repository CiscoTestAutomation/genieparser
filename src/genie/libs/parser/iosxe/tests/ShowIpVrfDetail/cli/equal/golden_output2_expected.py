expected_output = {
    "VRF1": {
        "address_family": {
            "ipv4 unicast": {
                "flags": "0x0",
                "table_id": "0x2",
                "vrf_label": {
                    "allocation_mode": "per-prefix",
                    "distribution_protocol": "LDP",
                },
            }
        },
        "cli_format": "New",
        "flags": "0x180C",
        "interface": {
            "GigabitEthernet2.390": {"vrf": "VRF1"},
            "GigabitEthernet2.410": {"vrf": "VRF1"},
            "GigabitEthernet2.415": {"vrf": "VRF1"},
            "GigabitEthernet2.420": {"vrf": "VRF1"},
            "GigabitEthernet3.390": {"vrf": "VRF1"},
            "GigabitEthernet3.410": {"vrf": "VRF1"},
            "GigabitEthernet3.415": {"vrf": "VRF1"},
            "GigabitEthernet3.420": {"vrf": "VRF1"},
            "Loopback300": {"vrf": "VRF1"},
            "Tunnel1": {"vrf": "VRF1"},
            "Tunnel3": {"vrf": "VRF1"},
            "Tunnel4": {"vrf": "VRF1"},
            "Tunnel6": {"vrf": "VRF1"},
            "Tunnel8": {"vrf": "VRF1"},
        },
        "interfaces": [
            "Tunnel1",
            "Loopback300",
            "GigabitEthernet2.390",
            "GigabitEthernet2.410",
            "GigabitEthernet2.415",
            "GigabitEthernet2.420",
            "GigabitEthernet3.390",
            "GigabitEthernet3.410",
            "GigabitEthernet3.415",
            "GigabitEthernet3.420",
            "Tunnel3",
            "Tunnel4",
            "Tunnel6",
            "Tunnel8",
        ],
        "route_distinguisher": "65000:1",
        "support_af": "multiple address-families",
        "vrf_id": 2,
    }
}
