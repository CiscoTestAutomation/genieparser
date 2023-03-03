expected_output = {
    "interfaces": {
        "GigabitEthernet1/0/21": {
            "mac_address": {
                "0800.37ff.f585": {
                    "iif_id": "0x105B0C0000005F5",
                    "ipv6_address": "Unknown",
                    "ipv4_address": "10.4.1.1",
                    "user_name": "genie123",
                    "status": "Authorized",
                    "domain": "DATA",
                    "current_policy": "Test_DOT1X-DEFAULT_V1",
                    "oper_host_mode": "multi-auth",
                    "oper_control_dir": "both",
                    "session_timeout": {"type": "N/A"},
                    "common_session_id": "0A7820020000413CCCE37640",
                    "acct_session_id": "0x00007EAF",
                    "handle": "0x7100056D",
                    "server_policies": {
                        1: {
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-Test_ACL_XeroxPrinters_v1-597a95c4",
                        }
                    },
                    "method_status": {
                        "dot1x": {"method": "dot1x", "state": "Stopped"},
                        "mab": {"method": "mab", "state": "Authc Success"},
                    },
                }
            }
        }
    }
}
