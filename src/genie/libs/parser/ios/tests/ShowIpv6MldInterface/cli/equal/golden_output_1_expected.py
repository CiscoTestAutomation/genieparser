expected_output = {
    "vrf": {
        "VRF1": {
            "interface": {
                "GigabitEthernet2": {
                    "query_max_response_time": 16,
                    "enable": True,
                    "query_interval": 366,
                    "querier": "FE80::5054:FF:FEDD:BB49",
                    "interface_status": "up",
                    "query_this_system": True,
                    "version": 2,
                    "interface_adress": "FE80::5054:FF:FEDD:BB49/10",
                    "active_groups": 0,
                    "querier_timeout": 740,
                    "last_member_query_interval": 1,
                    "counters": {"joins": 9, "leaves": 0},
                    "oper_status": "up",
                    "max_groups": 6400,
                },
                "Tunnel1": {
                    "interface_status": "up",
                    "interface_adress": "FE80::21E:BDFF:FEBA:D000/10",
                    "oper_status": "up",
                    "enable": False,
                },
            },
            "max_groups": 64000,
            "active_groups": 0,
        }
    }
}
