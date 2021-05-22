expected_output = {
    "interfaces": {
        "GigabitEthernet0/0/0.101": {
            "encapsulation_dot1q": "101",
            "ipv4": {"ip": "192.168.111.1", "netmask": "255.255.255.0",},
            "ipv6": ["2001::1/112"],
            "ipv6_enable": True,
            "ipv6_ospfv3": {"1": {"area": "0",},},
            "vrf": "VRF1",
        },
    },
}
