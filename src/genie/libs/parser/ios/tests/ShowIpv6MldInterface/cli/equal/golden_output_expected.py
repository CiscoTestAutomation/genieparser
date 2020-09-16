expected_output = {
    "vrf": {
        "default": {
            "interface": {
                "Tunnel0": {
                    "oper_status": "up",
                    "interface_adress": "FE80::21E:BDFF:FEBA:D000/10",
                    "enable": False,
                    "interface_status": "up",
                },
                "VoIP-Null0": {
                    "oper_status": "up",
                    "interface_adress": "::/0",
                    "enable": False,
                    "interface_status": "up",
                },
                "LIIN0": {
                    "oper_status": "up",
                    "interface_adress": "::/0",
                    "enable": False,
                    "interface_status": "up",
                },
                "GigabitEthernet1": {
                    "oper_status": "up",
                    "querier_timeout": 740,
                    "active_groups": 0,
                    "group_policy": "test",
                    "query_interval": 366,
                    "version": 2,
                    "query_this_system": True,
                    "querier": "FE80::5054:FF:FE7C:DC70",
                    "interface_status": "up",
                    "last_member_query_interval": 1,
                    "counters": {"leaves": 2, "joins": 11},
                    "max_groups": 6400,
                    "query_max_response_time": 16,
                    "enable": True,
                    "interface_adress": "FE80::5054:FF:FE7C:DC70/10",
                },
                "GigabitEthernet3": {
                    "oper_status": "down",
                    "interface_adress": "::/0",
                    "enable": False,
                    "interface_status": "administratively down",
                },
                "Null0": {
                    "oper_status": "up",
                    "interface_adress": "FE80::1/10",
                    "enable": False,
                    "interface_status": "up",
                },
            },
            "max_groups": 64000,
            "active_groups": 0,
        }
    }
}
