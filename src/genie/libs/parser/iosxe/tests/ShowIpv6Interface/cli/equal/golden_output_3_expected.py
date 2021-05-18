expected_output={
    "Serial1/0/2:0": {
        "enabled": True,
        "oper_status": "up",
        "ipv6": {
            "FE80::250:56FF:FE8D:EF3D": {
                "ip": "FE80::250:56FF:FE8D:EF3D",
                "origin": "link_layer",
                "status": "valid",
            },
            "2001:111::1/64": {
                "ip": "2001:111::1",
                "prefix_length": "64",
                "status": "valid",
            },
            "enabled": True,
            "icmp": {
                "error_messages_limited": 100,
                "redirects": True,
                "unreachables": "sent",
            },
            "nd": {
                "suppress": False,
                "dad_enabled": True,
                "dad_attempts": 1,
                "reachable_time": 30000,
                "using_time": 30000,
                "ns_retransmit_interval": 1000,
            },
        },
        "joined_group_addresses": ["FF02::1", "FF02::1:FF00:1", "FF02::1:FF8D:EF3D"],
        "mtu": 1500,
    }
}
