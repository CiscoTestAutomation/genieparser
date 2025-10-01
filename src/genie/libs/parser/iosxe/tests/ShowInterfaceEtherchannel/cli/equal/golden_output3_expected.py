expected_output = {
    "all_idbs_list": {
        "total_configured_interfaces": 4,
        "interfaces": {
            "TenGigabitEthernet0/0/0": {
                "interface": "TenGigabitEthernet0/0/0",
                "index": 0
            },
            "TenGigabitEthernet0/0/1": {
                "interface": "TenGigabitEthernet0/0/1",
                "index": 1
            },
            "TenGigabitEthernet0/0/2": {
                "interface": "TenGigabitEthernet0/0/2",
                "index": 2
            },
            "TenGigabitEthernet0/0/3": {
                "interface": "TenGigabitEthernet0/0/3",
                "index": 3
            }
        }
    },
    "active_member_list": {
        "total_interfaces": 4,
        "interfaces": {
            "TenGigabitEthernet0/0/0": {
                "interface": "TenGigabitEthernet0/0/0",
                "lacp_mode": "Active"
            },
            "TenGigabitEthernet0/0/1": {
                "interface": "TenGigabitEthernet0/0/1",
                "lacp_mode": "Active"
            },
            "TenGigabitEthernet0/0/2": {
                "interface": "TenGigabitEthernet0/0/2",
                "lacp_mode": "Active"
            },
            "TenGigabitEthernet0/0/3": {
                "interface": "TenGigabitEthernet0/0/3",
                "lacp_mode": "Active"
            }
        }
    },
    "passive_member_list": {
        "total_interfaces": 0
    },
    "load_balancing_method": "flow-based",
    "bucket_information": {
        "TenGigabitEthernet0/0/0": {
            "interface": "TenGigabitEthernet0/0/0",
            "buckets": [0, 1, 2, 3]
        },
        "TenGigabitEthernet0/0/1": {
            "interface": "TenGigabitEthernet0/0/1",
            "buckets": [4, 5, 6, 7]
        },
        "TenGigabitEthernet0/0/2": {
            "interface": "TenGigabitEthernet0/0/2",
            "buckets": [8, 9, 10, 11]
        },
        "TenGigabitEthernet0/0/3": {
            "interface": "TenGigabitEthernet0/0/3",
            "buckets": [12, 13, 14, 15]
        }
    }
}