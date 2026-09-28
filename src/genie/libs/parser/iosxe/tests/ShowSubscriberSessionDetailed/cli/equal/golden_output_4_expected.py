expected_output = {
    "total_sessions": 1,
    "sessions": {
        "12": {
            "type": "IPv6",
            "uid": 12,
            "state": "authen",
            "identity": "client1",
            "ipv6_address": "5001::",
            "session_up_time": "00:00:28",
            "last_changed": "00:00:11",
            "switch_id": 4141,
            "policy_information": {
                "context": "789750921F48",
                "handle": "6600000C",
                "aaa_id": "0000001D",
                "flow_handle": 0,
                "authentication_status": "authen",
                "downloaded_user_profile": {
                    "excluding_services": {
                        "service_type": {
                            "value1": 0,
                            "value2": 2,
                            "description": "Framed"
                        }
                    },
                    "including_services": {
                        "service_type": {
                            "value1": 0,
                            "value2": 2,
                            "description": "Framed"
                        }
                    }
                },
                "config_history": {
                    "access_type": "Web-user-logon",
                    "client": "Account Command-Handler",
                    "policy_event": "Got More Keys",
                    "profile_name": "client1",
                    "references": 2,
                    "profile_attributes": {
                        "service_type": {
                            "value1": 0,
                            "value2": 2,
                            "description": "Framed"
                        }
                    }
                },
                "rules_actions_conditions_executed": {
                    "subscriber_rule_map": "ACCT_LOGON",
                    "conditions": [
                        {
                            "condition": "always",
                            "event": "session-start",
                            "actions": [
                                {
                                    "sequence": 5,
                                    "command": "service local"
                                }
                            ]
                        },
                        {
                            "condition": "always",
                            "event": "account-logon",
                            "actions": [
                                {
                                    "sequence": 15,
                                    "command": "authenticate aaa list AUTHEN_LIST"
                                }
                            ]
                        }
                    ]
                }
            },
            "classifiers": {
                0: {
                    "direction": "In",
                    "packets": 8,
                    "bytes": 828,
                    "priority": 0,
                    "definition": "Match Any"
                },
                1: {
                    "direction": "Out",
                    "packets": 4,
                    "bytes": 456,
                    "priority": 0,
                    "definition": "Match Any"
                }
            },
            "template_id": 1,
            "configuration_sources": {
                "USR": {
                    "active_time": "00:00:11",
                    "aaa_service_id": "-",
                    "name": "Peruser"
                },
                "INT": {
                    "active_time": "00:00:28",
                    "aaa_service_id": "-",
                    "name": "GigabitEthernet0/0/3"
                }
            }
        }
    }
}