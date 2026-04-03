expected_output = {
    "TEST_1": {
        "address_family": {
            "ipv4 unicast": {
                "route_target": {
                    "1234:5678": {"route_target": "1234:5678", "rt_type": "import"},
                    "8765:4321": {"route_target": "8765:4321", "rt_type": "export"},
                }
            },
            "ipv6 unicast": {},
        },
        "description": "not set",
        "interfaces": [
            "GigabitEthernet0/0/0/0.2",
            "Gi0/0/0/0.1",
            "GigabitEthernet0/0/0/1",
            "Gi0/0/0/4",
            "TenGigE0/0/0/0.1",
            "TenGigabitEthernet0/0/0/0.2",
            "Te0/0/0/0.3",
        ],
        "route_distinguisher": "10.10.10.10:10",
        "vrf_mode": "regular",
    },
    "TEST_2": {
        "address_family": {
            "ipv4 unicast": {
                "route_target": {
                    "1111:2222": {"route_target": "1111:2222", "rt_type": "import"},
                    "2222:1111": {"route_target": "2222:1111", "rt_type": "export"},
                }
            },
            "ipv6 unicast": {},
        },
        "description": "not set",
        "interfaces": [
            "FortyGigE0/0/0/0.1",
            "FortyGigabitEthernet0/0/0/0.2",
            "Fo0/0/0/0.3",
            "FortyGigE0/0/0/1",
            "FortyGigabitEthernet0/0/0/2",
            "Fo0/0/0/3",
            "HundredGigE0/0/0/0.1",
            "HundredGigabitEthernet0/0/0/0.2",
            "Hu0/0/0/0.3",
            "HundredGigE0/0/0/1",
            "HundredGigabitEthernet0/0/0/2",
            "Hu0/0/0/3",
        ],
        "route_distinguisher": "1.2.3.4:5",
        "vrf_mode": "regular",
    },
    "TEST_3": {
        "address_family": {
            "ipv4 unicast": {
                "route_target": {
                    "13285:56891": {"route_target": "13285:56891", "rt_type": "export"},
                    "7984:4657": {"route_target": "7984:4657", "rt_type": "import"},
                }
            },
            "ipv6 unicast": {},
        },
        "description": "not set",
        "interfaces": [
            "Bundle-Ether0",
            "Bundle-Ethernet1",
            "BE2",
            "Loopback1",
            "Lo0",
            "Null0",
            "Nu1",
            "MgmtEth0/RP0/CPU0/0",
            "ManagementEthernet1/RP0/CPU0/0",
            "MgmtEth0/0/3",
        ],
        "route_distinguisher": "5.4.3.2:1",
        "vrf_mode": "regular",
    },
    "TEST_4": {
        "address_family": {
            "ipv4 unicast": {
                "route_target": {
                    "1111:1111": {"route_target": "1111:1111", "rt_type": "export"},
                    "7985:4654": {"route_target": "7985:4654", "rt_type": "import"},
                }
            },
            "ipv6 unicast": {},
        },
        "description": "not set",
        "interfaces": ["POS0/0/0/0", "PacketOverSonet0/0/0/1", "PoS0/0/0/2"],
        "route_distinguisher": "1.1.1.1:1",
        "vrf_mode": "regular",
    },
}