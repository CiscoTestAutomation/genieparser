expected_output = {
    "ldra": {
        "client_facing_disable": {
            "targets": [
                "GigabitEthernet1/0/20"
                ]
            },
        "client_facing_trusted": {
            "targets": [
                "GigabitEthernet1/0/12",
                "Vlan2",
                "Vlan3",
                "Vlan10"
                ]
        },
        "client_facing_untrusted": {
            "targets": [
                "GigabitEthernet1/0/11",
                "Vlan4",
                "Vlan5",
                "Vlan11"
                ]
        },
        "server_facing": {
            "targets": [
                "GigabitEthernet1/0/6",
                "GigabitEthernet1/0/7",
                "GigabitEthernet1/0/8",
                "GigabitEthernet1/0/9",
                "GigabitEthernet1/0/10",
                "GigabitEthernet1/0/13",
                "GigabitEthernet1/0/14",
                "GigabitEthernet1/0/15",
                "GigabitEthernet1/0/16",
                "GigabitEthernet1/0/17",
                "GigabitEthernet1/0/18",
                "GigabitEthernet1/0/19"
            ]
        },
        "status": "Enabled",
    }
}
