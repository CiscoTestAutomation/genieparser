expected_output ={
    "DROP": {
        "statements": {
            10: {
                "actions": {
                    "actions": "drop"
                },
                "conditions": {}
            }
        }
    },
    "PASS": {
        "statements": {
            10: {
                "actions": {
                    "actions": "pass"
                },
                "conditions": {}
            }
        }
    },
    "show": {
        "statements": {
            10: {
                "actions": {},
                "conditions": {}
            }
        }
    },
    "RP-SID($SID)": {
        "statements": {
            10: {
                "actions": {},
                "conditions": {}
            }
        }
    },
    "RP-PASS": {
        "statements": {
            10: {
                "actions": {
                    "actions": "pass"
                },
                "conditions": {}
            }
        }
    },
    "ADD-PATH": {
        "statements": {
            10: {
                "actions": {},
                "conditions": {}
            }
        }
    },
    "EVPN-IN-RPL": {
        "statements": {
            10: {
                "actions": {
                    "actions": "pass"
                },
                "conditions": {
                    "match_as_path_list": "EVPN-AS-SET",
                    "match_level_eq": "5"
                }
            }
        }
    },
    "RP-BACKUP-PATH": {
        "statements": {
            10: {
                "actions": {},
                "conditions": {}
            }
        }
    },
    "VRF:205:201": {
        "statements": {
            10: {
                "actions": {},
                "conditions": {}
            }
        }
    },
    "BGP-HAB-00001-RPL": {
        "statements": {
            10: {
                "actions": {
                    "set_local_pref": 16000,
                    "set_med": 400
                },
                "conditions": {}
            }
        }
    },
    "RP-ALLOCATE-LABELS": {
        "statements": {
            10: {
                "actions": {
                    "actions": "pass"
                },
                "conditions": {
                    "match_prefix_list": "PS-MY-LOOPBACK"
                }
            }
        }
    },
    "RP-AS65455-CORE-IN": {
        "statements": {
            10: {
                "actions": {
                    "actions": "drop"
                },
                "conditions": {
                    "match_prefix_list": "PS-MY-LOOPBACK"
                }
            },
            20: {
                "actions": {
                    "actions": "pass"
                },
                "conditions": {
                    "match_prefix_list": "PS-HOST-ROUTE"
                }
            }
        }
    },
    "ADD-BACKUP-PATH-RPL": {
        "statements": {
            10: {
                "actions": {},
                "conditions": {}
            }
        }
    },
    "RP-AS65455-CORE-OUT": {
        "statements": {
            10: {
                "actions": {
                    "actions": "pass"
                },
                "conditions": {
                    "match_prefix_list": "PS-MY-LOOPBACK"
                }
            }
        }
    }
}