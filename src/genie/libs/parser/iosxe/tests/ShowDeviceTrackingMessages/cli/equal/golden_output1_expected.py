expected_output = {
        "entries": {
            1: {
                "timestamp": "Wed Jul 21 20:31:27.000",
                "vlan": 10,
                "interface": "Ethernet0/0",
                "mac": "aabb.cc00.0100",
                "protocol": "NDP::NA",
                "ip": "FE80::A8BB:CCFF:FE00:100",
                "ignored": False,
                "drop_reason": "Packet accepted but not forwarded",
            },
            2: {
                "timestamp": "Wed Jul 21 20:31:27.000",
                "vlan": 10,
                "interface": "Ethernet0/0",
                "mac": "aabb.cc00.0100",
                "protocol": "NDP::RA",
                "ip": "FE80::A8BB:CCFF:FE00:100",
                "ignored": False,
                "drop_reason": "Packet not authorized on port",
            },
            3: {
                "timestamp": "Wed Jul 21 20:31:28.000",
                "vlan": 10,
                "interface": "Ethernet0/0",
                "mac": "aabb.cc00.0100",
                "protocol": "NDP::NA",
                "ip": "A::1",
                "ignored": False,
                "drop_reason": "Packet accepted but not forwarded"
            }
        }
    }