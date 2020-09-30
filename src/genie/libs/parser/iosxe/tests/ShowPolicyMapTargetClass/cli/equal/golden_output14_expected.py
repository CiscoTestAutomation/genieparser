expected_output = {
    "GigabitEthernet0/0/1": {
        "service_policy": {
            "input": {"policy_name": {"TEST": {}}},
            "output": {"policy_name": {"TEST2": {}}},
        }
    },
    "TenGigabitEthernet0/3/0.41": {
        "service_policy": {"output": {"policy_name": {"VLAN51_QoS": {}}}}
    },
}
