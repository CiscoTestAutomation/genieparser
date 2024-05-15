expected_output = {
    "RM-T2-POLICY-OUT": {
        "statements": {
            "15": {
                "actions": {
                    "set_next_hop_self": False,
                    "route_disposition": "permit",
                    "set_community": "1441794"
                },
                "conditions": {
                    "match_prefix_list": "PL-MGMT-LOCAL"
                },
                "policy_routing_matches": {
                    "packets": 0,
                    "bytes": 0
                }
            },
            "25": {
                "actions": {
                    "set_next_hop_self": False,
                    "route_disposition": "permit",
                    "set_community": "1441994"
                },
                "conditions": {
                    "match_prefix_list": "PL-CP-UNICAST-LOCAL"
                },
                "policy_routing_matches": {
                    "packets": 0,
                    "bytes": 0
                }
            },
            "35": {
                "actions": {
                    "set_next_hop_self": False,
                    "route_disposition": "permit",
                    "set_community": "1442092"
                },
                "conditions": {
                    "match_prefix_list": "PL-MSMR-ANYCAST"
                },
                "policy_routing_matches": {
                    "packets": 0,
                    "bytes": 0
                }
            },
            "45": {
                "actions": {
                    "set_next_hop_self": False,
                    "route_disposition": "permit",
                    "set_community": "1442122"
                },
                "conditions": {
                    "match_prefix_list": "PL-MSDP-ANYCAST"
                },
                "policy_routing_matches": {
                    "packets": 0,
                    "bytes": 0
                }
            },
            "1005": {
                "actions": {
                    "set_next_hop_self": False,
                    "route_disposition": "permit"
                },
                "conditions": {},
                "policy_routing_matches": {
                    "packets": 0,
                    "bytes": 0
                }
            }
        }
    },
    "RM-T1-POLICY-MAINT-OUT": {
        "statements": {
            "10": {
                "actions": {
                    "set_next_hop_self": False,
                    "route_disposition": "permit",
                    "set_as_path_prepend": "1.1",
                    "set_as_path_prepend_repeat_n": 2,
                    "set_as_path_group": [
                        "1.1",
                        "1.1"
                    ],
                    "set_community": "720897"
                },
                "conditions": {
                    "match_prefix_list": "PL-MGMT-LOCAL"
                },
                "policy_routing_matches": {
                    "packets": 0,
                    "bytes": 0
                }
            },
            "20": {
                "actions": {
                    "set_next_hop_self": False,
                    "route_disposition": "permit",
                    "set_as_path_prepend": "1.1",
                    "set_as_path_prepend_repeat_n": 2,
                    "set_as_path_group": [
                        "1.1",
                        "1.1"
                    ],
                    "set_community": "720997"
                },
                "conditions": {
                    "match_prefix_list": "PL-CP-UNICAST-LOCAL"
                },
                "policy_routing_matches": {
                    "packets": 0,
                    "bytes": 0
                }
            },
            "30": {
                "actions": {
                    "set_next_hop_self": False,
                    "route_disposition": "permit",
                    "set_as_path_prepend": "1.1",
                    "set_as_path_prepend_repeat_n": 2,
                    "set_as_path_group": [
                        "1.1",
                        "1.1"
                    ],
                    "set_community": "721096"
                },
                "conditions": {
                    "match_prefix_list": "PL-MSMR-ANYCAST"
                },
                "policy_routing_matches": {
                    "packets": 0,
                    "bytes": 0
                }
            },
            "40": {
                "actions": {
                    "set_next_hop_self": False,
                    "route_disposition": "permit",
                    "set_as_path_prepend": "1.1",
                    "set_as_path_prepend_repeat_n": 2,
                    "set_as_path_group": [
                        "1.1",
                        "1.1"
                    ],
                    "set_community": "721116"
                },
                "conditions": {
                    "match_prefix_list": "PL-MSDP-ANYCAST"
                },
                "policy_routing_matches": {
                    "packets": 0,
                    "bytes": 0
                }
            },
            "50": {
                "actions": {
                    "set_next_hop_self": False,
                    "route_disposition": "permit",
                    "set_as_path_prepend": "10",
                    "set_as_path_prepend_repeat_n": 3,
                    "set_as_path_group": [
                        "10",
                        "10",
                        "10"
                    ]
                },
                "conditions": {},
                "policy_routing_matches": {
                    "packets": 0,
                    "bytes": 0
                }
            },
            "1000": {
                "actions": {
                    "set_next_hop_self": False,
                    "route_disposition": "permit",
                    "set_as_path_prepend": "1.1",
                    "set_as_path_prepend_repeat_n": 2,
                    "set_as_path_group": [
                        "1.1",
                        "1.1"
                    ]
                },
                "conditions": {},
                "policy_routing_matches": {
                    "packets": 0,
                    "bytes": 0
                }
            }
        }
    },
    "RM-T2-POLICY-IN": {
        "statements": {
            "15": {
                "actions": {
                    "set_next_hop_self": False,
                    "route_disposition": "permit"
                },
                "conditions": {
                    "match_community_list": "2"
                },
                "policy_routing_matches": {
                    "packets": 0,
                    "bytes": 0
                }
            },
            "25": {
                "actions": {
                    "set_next_hop_self": False,
                    "route_disposition": "deny"
                },
                "conditions": {
                    "match_as_path_list": "2"
                },
                "policy_routing_matches": {
                    "packets": 0,
                    "bytes": 0
                }
            },
            "1005": {
                "actions": {
                    "set_next_hop_self": False,
                    "route_disposition": "permit"
                },
                "conditions": {},
                "policy_routing_matches": {
                    "packets": 0,
                    "bytes": 0
                }
            }
        }
    }
}
