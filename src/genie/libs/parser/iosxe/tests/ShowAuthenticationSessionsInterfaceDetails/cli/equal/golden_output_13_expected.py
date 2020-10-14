expected_output = {
    "interfaces": {
        "GigabitEthernet1/0/17": {
            "mac_address": {
                "00e1.6dff.a99e": {
                    "acct_session_id": "0x00000028",
                    "common_session_id": "0A8628020000003463B40D0F",
                    "current_policy": "Test_DOT1X-DEFAULT_V1",
                    "domain": "VOICE",
                    "handle": "0x3000002a",
                    "iif_id": "0x11910563",
                    "ipv4_address": "Unknown",
                    "ipv6_address": "Unknown",
                    "user_name": "00-E1-6D-FF-A9-9E",
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
                            "policies": "xACSACLx-IP-Test_ACL_CiscoPhones-583e3751",
                        }
                    },
                }
            }
        }
    }
}
