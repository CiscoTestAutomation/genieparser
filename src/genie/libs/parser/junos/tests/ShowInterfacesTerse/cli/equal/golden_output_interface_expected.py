expected_output = {
    "em1.0": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
        "protocol": {
            "inet": {
                "10.0.0.4/8": {"local": "10.0.0.4/8"},
                "172.16.64.1/2": {"local": "172.16.64.1/2"},
                "172.16.64.4/2": {"local": "172.16.64.4/2"},
            },
            "inet6": {
                "fe80::250:56ff:fe82:ba52/64": {"local": "fe80::250:56ff:fe82:ba52/64"},
                "2001:db8:8d82:0:a::4/64": {"local": "2001:db8:8d82:0:a::4/64"},
            },
            "tnp": {"0x4": {"local": "0x4"}},
        },
    }
}
