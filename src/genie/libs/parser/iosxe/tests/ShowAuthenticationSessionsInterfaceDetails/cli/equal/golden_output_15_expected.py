expected_output = {
    "interfaces": {
        "GigabitEthernet4/0/18": {
            "mac_address": {
                "0800.273f.f427": {
                    "ipv6_address": "fe80::7635:22a5:7597:2429",
                    "iif_id": "0x2B5A8BE5",
                    "ipv4_address": "10.15.1.233",
                    "user_name": "08-00-27-3F-F4-27",
                    "status": "Authorized",
                    "domain": "DATA",
                    "oper_host_mode": "multi-auth",
                    "oper_control_dir": "in",
                    "session_timeout": {
                        "type": "N/A"
                    },
                    "common_session_id": "86010F8900002F29A505F344",
                    "acct_session_id": "0x00003487",
                    "handle": "0x73000fc1",
                    "current_policy": "C3PL_ISE_210",
                    "local_policies": {
                        "template": {
                            "DEFAULT_LINKSEC_POLICY_SHOULD_SECURE": {
                                "priority": 150
                            }
                        },
                        "security_policy": "Should Secure"
                    },
                    "server_policies": {
                        1: {
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-PERMIT_ALL_IPV4_TRAFFIC-57f6b0d3",
                            "security_policy": "Should Secure"
                        }
                    },
                    "method_status": {
                        "dot1x": {
                            "method": "dot1x",
                            "state": "Stopped"
                        },
                        "mab": {
                            "method": "mab",
                            "state": "Authc Success"
                        }
                    }
                },
                "1062.e519.072e": {
                    "ipv6_address": "Unknown",
                    "iif_id": "0x273804C8",
                    "ipv4_address": "10.15.1.176",
                    "user_name": "J2XD0170154",
                    "status": "Authorized",
                    "domain": "DATA",
                    "oper_host_mode": "multi-auth",
                    "oper_control_dir": "in",
                    "session_timeout": {
                        "type": "server",
                        "timeout": "64800s",
                        "remaining": "24177s"
                    },
                    "timeout_action": "Reauthenticate",
                    "common_session_id": "86010F8900002F28A5016B11",
                    "acct_session_id": "0x00003951",
                    "handle": "0x21000fc0",
                    "current_policy": "C3PL_ISE_210",
                    "local_policies": {
                        "template": {
                            "DEFAULT_LINKSEC_POLICY_SHOULD_SECURE": {
                                "priority": 150
                            }
                        }
                    },
                    "server_policies": {
                        1: {
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-PERMIT_ALL_IPV4_TRAFFIC-57f6b0d3"
                        },
                        2: {
                            "name": "Session-Timeout",
                            "policies": "64800 sec"
                        }
                    },
                    "method_status": {
                        "dot1x": {
                            "method": "dot1x",
                            "state": "Authc Success"
                        },
                        "mab": {
                            "method": "mab",
                            "state": "Stopped"
                        }
                    }
                }
            }
        }
    }
}
