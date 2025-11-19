expected_output = {
    "class_map": {
        "name": "FOO",
        "match_criteria": "match-all",
        "id": 1,
        "matches": {
            1: {
                "match_type": "protocol",
                "value": "icmp"
            },
            2: {
                "match_type": "access_group",
                "value": "ipv6ACL_for_drop_test"
            }
        }
    }
}