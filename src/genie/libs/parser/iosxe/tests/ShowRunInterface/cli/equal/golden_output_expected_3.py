expected_output = {
    "interfaces": {
        "GigabitEthernet0/0/3": {
            "ip_ospf": {"2": {"area": "0",},},
            "ipv4": {"ip": "99.99.110.1", "netmask": "255.255.255.0",},
            "ipv6": ["2003::1/112"],
            "ipv6_ospf": {"1": {"area": "0",},},
            "negotiation_auto": True,
        },
    },
}
