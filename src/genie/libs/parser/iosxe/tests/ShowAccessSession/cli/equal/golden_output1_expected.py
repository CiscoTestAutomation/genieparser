expected_output = {
    "session_count": 2,
    "interfaces": {
        "GigabitEthernet1/0/1": {
            "interface": "GigabitEthernet1/0/1",
            "client": {
                "f4cf.beff.9cb1": {
                    "client": "f4cf.beff.9cb1",
                    "method": "dot1x",
                    "domain": "DATA",
                    "status": "Auth",
                    "session": {
                        "000000000000000BB6FC9EAF": {
                            "session_id": "000000000000000BB6FC9EAF"
                        }
                    }
                }
            }
        },
        "GigabitEthernet1/0/2": {
            "interface": "GigabitEthernet1/0/2",
            "client": {
                "aabb.cc11.2233": {
                    "client": "aabb.cc11.2233",
                    "method": "dot1x",
                    "domain": "VOICE",
                    "status": "Unauth",
                    "session": {
                        "000000000000000A1B2C3D4E": {
                            "session_id": "000000000000000A1B2C3D4E"
                        }
                    }
                }
            }
        }
    }
}
