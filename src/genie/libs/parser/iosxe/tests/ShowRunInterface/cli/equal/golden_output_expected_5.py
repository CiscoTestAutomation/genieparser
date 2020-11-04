expected_output = {
    "interfaces": {
        "Loopback1": {
            "ipv4": {"ip": "192.168.111.2", "netmask": "255.255.255.0",},
            "ipv6": ["2001:db8:4:1::1/64", "2001:db8:400:1::2/112"],
            "vrf": "VRF1",
        },
    },
}
