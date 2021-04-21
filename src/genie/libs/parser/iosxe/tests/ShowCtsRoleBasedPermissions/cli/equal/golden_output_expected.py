expected_output = {
    "indexes": {
        1: {
            "policy_name": "default",
            "action_policy": "Permit",
            "action_policy_group": "IP-00"
        },
        2: {
            "src_grp_id": 42,
            "src_grp_name": "Untrusted",
            "unknown_group": "Unknown",
            "action_policy": "Deny",
            "action_policy_group": "IP-00"
        },
        3: {
            "src_grp_id": 199,
            "src_grp_name": "FAILED_AUTH",
            "unknown_group": "Unknown",
            "action_policy": "Deny",
            "action_policy_group": "IP-00"
        },
        4: {
            "src_grp_id": 22,
            "src_grp_name": "Untrusted",
            "dst_group_id": 22,
            "dst_group_name": "Untrusted",
            "action_policy": "Deny",
            "action_policy_group": "IP-00"
        },
        5: {
            "src_grp_id": 100,
            "src_grp_name": "Tech",
            "dst_group_id": 6,
            "dst_group_name": "Trusted",
            "policy_groups": ["NFS-08", "ACCESS-01"],
            "action_policy": "Deny",
            "action_policy_group": "IP-00"
        },
        6: {
            "src_grp_id": 101,
            "src_grp_name": "Mars",
            "dst_group_id": 5,
            "dst_group_name": "Trusted",
            "action_policy": "Deny",
            "action_policy_group": "IP-00"
        },
        7: {
            "src_grp_id": 111,
            "src_grp_name": "Technicolor",
            "dst_group_id": 9,
            "dst_group_name": "Printers",
            "policy_groups": ["PRINTING-10", "GENERIC-14"],
            "action_policy": "Deny",
            "action_policy_group": "IP-00"
        },
        8: {
            "src_grp_id": 102,
            "src_grp_name": "Moon",
            "dst_group_id": 6,
            "dst_group_name": "Printers",
            "policy_groups": ["ICMP-01", "PRINTING-10"],
            "action_policy": "Deny",
            "action_policy_group": "IP-00"
        },
        9: {
            "src_grp_id": 199,
            "src_grp_name": "FAILED_AUTH",
            "dst_group_id": 9999,
            "dst_group_name": "QUARANTINE_REDIRECT_PORTAL",
            "action_policy": "Deny",
            "action_policy_group": "IP-00"
        },
        "monitor_dynamic": False,
        "monitor_configured": False
    }
}
