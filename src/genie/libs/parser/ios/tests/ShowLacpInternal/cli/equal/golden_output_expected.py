expected_output = {
    "interfaces": {
        "Port-channel1": {
            "name": "Port-channel1",
            "protocol": "lacp",
            "members": {
                "FastEthernet4/1": {
                    "interface": "FastEthernet4/1",
                    "activity": "auto",
                    "flags": "saC",
                    "state": "bndl",
                    "bundled": True,
                    "lacp_port_priority": 32768,
                    "admin_key": 100,
                    "oper_key": 100,
                    "port_num": 193,
                    "port_state": 117,
                    "lacp_interval": "30s",
                },
                "FastEthernet4/2": {
                    "interface": "FastEthernet4/2",
                    "activity": "auto",
                    "flags": "saC",
                    "state": "bndl",
                    "bundled": True,
                    "lacp_port_priority": 32768,
                    "admin_key": 100,
                    "oper_key": 100,
                    "port_num": 194,
                    "port_state": 117,
                    "lacp_interval": "30s",
                },
            },
        }
    }
}
