expected_output = {
    "vrf": {
        "BT-RBG-LAB": {
            "interfaces": ["GigabitEthernet0/0/0"],
            "protocols": ["ipv4"],
            "route_distinguisher": "10.116.83.34:99",
        },
        "Mgmt-intf": {
            "interfaces": ["GigabitEthernet0"],
            "protocols": ["ipv4", "ipv6"],
            "route_distinguisher": "<not set>",
        },
        "rb-bcn-lab": {
            "interfaces": ["Loopback9", "TenGigabitEthernet0/0/1"],
            "protocols": ["ipv4", "ipv6"],
            "route_distinguisher": "10.116.83.34:1",
        },
        "test": {
            "interfaces": ["Loopback100"],
            "protocols": ["ipv4", "ipv6"],
            "route_distinguisher": "10.116.83.34:100",
        },
    }
}
