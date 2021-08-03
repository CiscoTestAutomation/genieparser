expected_output = {
    "interfaces": {
        "GigabitEthernet2/0/2": {
            "mac_address": {
                "00b7.71fa.f7d5": {
                    "acct_session_id": "Unknown",
                    "common_session_id": "000000000000000BFDC31297",
                    "current_policy": "SOM-DOT1X-AUTH-POLICY",
                    "domain": "DATA",
                    "handle": "0x04000001",
                    "iif_id": "0x3AC7969C",
                    "ipv4_address": "Unknown",
                    "ipv6_address": "Unknown",
                    "local_policies": {
                        "security_policy": "Should Secure",
                        "template": {
                            "DEFAULT_LINKSEC_POLICY_SHOULD_SECURE": {"priority": 150}
                        },
                    },
                    "method_status": {
                        "dot1x": {"method": "dot1x", "state": "Authc Success"},
                        "mab": {"method": "mab", "state": "Authc Failed"},
                    },
                    "oper_control_dir": "both",
                    "oper_host_mode": "multi-auth",
                    "restart_timeout": {
                        "remaining": 44,
                        "timeout": 60
                    },
                    "session_timeout": {"type": "N/A"},
                    "status": "Authorized",
                    "unauth_timeout": {"remaining": 5, "timeout": 10},
                    "user_name": "rreddyc",
                }
            }
        }
    }
}
