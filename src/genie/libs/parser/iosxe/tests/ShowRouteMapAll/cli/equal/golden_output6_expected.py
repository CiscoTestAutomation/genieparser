expected_output = {
    "rm1": {
        "statements": {
            "1": {
                "actions": {
                    "route_disposition": "permit",
                    "set_next_hop_self": False,
                    "set_ipv6_precedence": 7,
                },
                "conditions": {
                    "match_prefix_list_v6": "pl1",
                },
                "policy_routing_matches": {
                    "bytes": 0,
                    "packets": 0,
                },
            },
        },
    },
}
