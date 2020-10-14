expected_output = {
    "interfaces": {
        "GigabitEthernet0/0": {
            "status": "up",
            "protocol": "up",
            "description": "OOB Management",
        },
        "GigabitEthernet0/1": {
            "status": "admin down",
            "protocol": "down",
            "description": "to router2",
        },
        "Loopback0": {"status": "up", "protocol": "up", "description": "Loopback"},
    }
}
