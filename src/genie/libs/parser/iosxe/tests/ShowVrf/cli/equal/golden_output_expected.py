expected_output = {
    "vrf": {
        "Mgmt-intf": {
            "route_distinguisher": "<not set>",
            "protocols": ["ipv4", "ipv6"],
            "interfaces": ["GigabitEthernet1"],
        },
        "VRF1": {
            "route_distinguisher": "65000:1",
            "protocols": ["ipv4", "ipv6"],
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
                "Tunnel3",
                "Tunnel4",
                "Tunnel6",
                "Tunnel8",
                "GigabitEthernet3.420",
            ],
        },
    }
}
