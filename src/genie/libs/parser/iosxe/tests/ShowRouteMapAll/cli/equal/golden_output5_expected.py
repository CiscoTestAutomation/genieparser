expected_output = {
    "rm1": {
        "statements": {
            "1": {
                "actions": {
                    "route_disposition": "permit",
                    "set_next_hop_self": False,
                    "set_ip_tos": 7,
                },
                "conditions": {
                    "match_prefix_list": "pl1",
                },
                "policy_routing_matches": {
                    "bytes": 0,
                    "packets": 0,
                },
            },
        },
    },
}
