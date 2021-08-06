expected_output = {
    "interfaces": {
        "GigabitEthernet1/12": {
            "mac_address": {
                "6390.c2ff.5519": {
                    "acct_session_id": "Unknown",
                    "common_session_id": "0A805A0A000012C8FDF2EF40",
                    "current_policy": "POLICY_Gi1/12",
                    "domain": "DATA",
                    "handle": "0x3F000FC8",
                    "ipv4_address": "10.1.2.102",
                    "ipv6_address": "Unknown",
                    "local_policies": {
                        "security_policy": "Should Secure",
                        "security_status": "Link Unsecure",
                        "template": {
                            "DEFAULT_LINKSEC_POLICY_SHOULD_SECURE": {"priority": 150}
                        },
                    },
                    "method_status": {
                        "dot1x": {"method": "dot1x", "state": "Authc Success"},
                        "mab": {"method": "mab", "state": "Stopped"},
                    },
                    "oper_control_dir": "in",
                    "oper_host_mode": "single-host",
                    "periodic_acct_timeout": "N/A",
                    "session_timeout": {
                        "remaining": "31799s",
                        "timeout": "43200s",
                        "type": "local",
                    },
                    "session_uptime": "22444s",
                    "status": "Authorized",
                    "timeout_action": "Reauthenticate",
                    "user_name": "host/genie.cisco.corp",
                }
            }
        }
    }
}
