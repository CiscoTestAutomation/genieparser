expected_output = {
    "interfaces": {
        "GigabitEthernet1/0/17": {
            "mac_address": {
                "0024.9bff.0ac8": {
                    "acct_session_id": "0x0000008d",
                    "common_session_id": "0A8628020000007168945FE6",
                    "current_policy": "Test_DOT1X-DEFAULT_V1",
                    "domain": "DATA",
                    "handle": "0x86000067",
                    "iif_id": "0x1534B4E2",
                    "ipv4_address": "Unknown",
                    "ipv6_address": "Unknown",
                    "user_name": "host/Laptop123.test.com",
                    "status": "Authorized",
                    "oper_host_mode": "multi-auth",
                    "oper_control_dir": "both",
                    "session_timeout": {"type": "N/A"},
                    "server_policies": {
                        1: {
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-Test_ACL_PERMIT_ALL-565bad69",
                            "security_policy": "None",
                            "security_status": "Link Unsecured",
                        }
                    },
                    "method_status": {
                        "dot1x": {"method": "dot1x", "state": "Authc Success"},
                        "mab": {"method": "mab", "state": "Stopped"},
                    },
                }
            }
        }
    }
}
