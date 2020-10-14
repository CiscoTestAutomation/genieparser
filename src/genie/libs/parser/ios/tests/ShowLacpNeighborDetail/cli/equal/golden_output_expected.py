expected_output = {
    "interfaces": {
        "Port-channel1": {
            "name": "Port-channel1",
            "protocol": "lacp",
            "members": {
                "GigabitEthernet0/0/1": {
                    "activity": "Active",
                    "age": 18,
                    "aggregatable": True,
                    "collecting": True,
                    "defaulted": False,
                    "distributing": True,
                    "expired": False,
                    "flags": "FA",
                    "interface": "GigabitEthernet0/0/1",
                    "lacp_port_priority": 100,
                    "oper_key": 1,
                    "port_num": 2,
                    "port_state": 63,
                    "synchronization": True,
                    "system_id": "00127,6487.88ff.68ef",
                    "timeout": "Short",
                },
                "GigabitEthernet0/0/7": {
                    "activity": "Active",
                    "age": 0,
                    "aggregatable": True,
                    "collecting": False,
                    "defaulted": False,
                    "distributing": False,
                    "expired": False,
                    "flags": "FA",
                    "interface": "GigabitEthernet0/0/7",
                    "lacp_port_priority": 200,
                    "oper_key": 1,
                    "port_num": 1,
                    "port_state": 15,
                    "synchronization": True,
                    "system_id": "00127,6487.88ff.68ef",
                    "timeout": "Short",
                },
            },
        }
    }
}
