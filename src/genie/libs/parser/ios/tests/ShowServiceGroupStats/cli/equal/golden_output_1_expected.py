expected_output = {
    "service_group_statistics": {
        "global": {"num_of_groups": 5, "num_of_members": 8005},
        "1": {
            "num_of_interfaces": 1,
            "num_of_members": {3000: {"service_instance": 3000}},
            "members_joined": 13000,
            "members_left": 10000,
        },
        "2": {
            "num_of_interfaces": 1,
            "num_of_members": {2000: {"service_instance": 2000}},
            "members_joined": 10000,
            "members_left": 8000,
        },
        "3": {
            "num_of_interfaces": 1,
            "num_of_members": {3000: {"service_instance": 3000}},
            "members_joined": 9000,
            "members_left": 6000,
        },
        "10": {
            "num_of_interfaces": 1,
            "num_of_members": {3: {"service_instance": 3}},
            "members_joined": 8003,
            "members_left": 8000,
        },
        "20": {
            "num_of_interfaces": 1,
            "num_of_members": {2: {"service_instance": 2}},
            "members_joined": 8002,
            "members_left": 8000,
        },
    }
}
