expected_output = {
    "interface": {
        "TenGigabitEthernet5/0/23": {
            "pvlan_mode": "none",
            "stp_state": "disabled",
            "vtp_pruned": "No",
            "untagged": "Yes",
            "gid": 123011
        },
        "TenGigabitEthernet5/0/1": {
            "pvlan_mode": "none",
            "stp_state": "forwarding",
            "vtp_pruned": "No",
            "untagged": "Yes",
            "gid": 123012
        },
        "GigabitEthernet1/0/1": {
            "pvlan_mode": "none",
            "stp_state": "blocking",
            "vtp_pruned": "No",
            "untagged": "Yes",
            "gid": 123009
        }
    },
    "hw_flood_list": [
        "TenGigabitEthernet1/0/37",
        "TenGigabitEthernet5/0/23",
        "GigabitEthernet1/0/1",
        "TenGigabitEthernet5/0/1"
    ]
}