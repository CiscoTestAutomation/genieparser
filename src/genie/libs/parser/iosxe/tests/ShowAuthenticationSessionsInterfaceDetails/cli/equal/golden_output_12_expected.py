expected_output = {
    "interfaces": {
        "GigabitEthernet1/0/48": {
            "mac_address": {
                "006b.f1ff.5b0c": {
                    "acct_session_id": "0x00004d7a",
                    "common_session_id": "0A788905000021FBF8593E6C",
                    "current_policy": "Test_DOT1X-DEFAULT_V1",
                    "domain": "DATA",
                    "handle": "0xa60001eb",
                    "iif_id": "0x1AE25879",
                    "ipv4_address": "Unknown",
                    "ipv6_address": "Unknown",
                    "user_name": "00-6B-F1-FF-5B-0C",
                    "status": "Authorized",
                    "oper_host_mode": "multi-auth",
                    "oper_control_dir": "both",
                    "session_timeout": {"type": "N/A"},
                    "method_status": {
                        "dot1x": {"method": "dot1x", "state": "Stopped"},
                        "mab": {"method": "mab", "state": "Authc Success"},
                    },
                    "server_policies": {
                        1: {
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-Test_ACL_WAPs-598d0d01",
                        }
                    },
                }
            }
        }
    }
}
