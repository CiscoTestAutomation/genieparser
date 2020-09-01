expected_output = {
    "interfaces": {
        "GigabitEthernet1/0/2": {
            "mac_address": {
                "b4a8.b9ff.5cc3": {
                    "acct_session_id": "0x00000004",
                    "common_session_id": "0A76060A0000000D5323681F",
                    "current_policy": "POLICY_Gi1/0/2",
                    "domain": "VOICE",
                    "handle": "0x90000003",
                    "iif_id": "0x17B5937E",
                    "ipv4_address": "10.4.1.1",
                    "ipv6_address": "Unknown",
                    "method_status": {
                        "dot1x": {"method": "dot1x", "state": "Stopped"},
                        "mab": {"method": "mab", "state": "Authc Success"},
                    },
                    "oper_control_dir": "both",
                    "oper_host_mode": "multi-auth",
                    "server_policies": {
                        1: {
                            "name": "ACS ACL",
                            "policies": "xGENIEx-Test_ACL_CiscoPhones-e23431ede2",
                        },
                        2: {
                            "name": "URL Redirect ACL",
                            "policies": "ACLSWITCH_Redirect_v1",
                        },
                        3: {
                            "name": "URL Redirect",
                            "policies": "https://cisco.test.com.us:8446/portal/gateway?_sessionId_=",
                        },
                        4: {
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-ACL_MABDefault_V3-5da428a4",
                        },
                    },
                    "session_timeout": {"type": "N/A"},
                    "status": "Authorized",
                    "user_name": "B4-A8-B9-FF-5C-C3",
                }
            }
        }
    }
}
