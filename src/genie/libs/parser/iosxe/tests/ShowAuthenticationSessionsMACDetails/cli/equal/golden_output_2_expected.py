expected_output = {
    "interfaces": {
        "GigabitEthernet3/0/27": {
            "mac_address": {
                "0057.0100.0001": {
                    "ipv6_address": "Unknown",
                    "iif_id": "0x1F2CB7AA",
                    "ipv4_address": "177.10.0.1",
                    "user_name": "user_dot1x_btemplate",
                    "status": "Authorized",
                    "domain": "DATA",
                    "oper_host_mode": "multi-auth",
                    "oper_control_dir": "both",
                    "session_timeout": {
                        "type": "server",
                        "timeout": "120s",
                        "remaining": "78s"
                    },
                    "timeout_action": "Reauthenticate",
                    "common_session_id": "EE01060A000000E3F9F77577",
                    "acct_session_id": "0x000000bf",
                    "handle": "0xed0000d9",
                    "current_policy": "POLICY_Gi3/0/24",
                    "local_policies": {
                        "template": {
                            "edge_dot1x_btemplate": {
                                "priority": 100
                            }
                        }
                    },
                    "server_policies": {
                        1: {
                            "name": "Session-Timeout",
                            "policies": "120 sec",
                            "vlan_group": {
                                "vlan": 177
                            }
                        },
                        2: {
                            "name": "ACS ACL",
                            "policies": (
                                'xACSACLx-IP-permit_edge_dot1x_btemplate-65774576'
                            )
                        }
                    },
                    "method_status": {
                        "dot1x": {
                            "method": "dot1x",
                            "state": "Authc Success"
                        }
                    }
                }
            }
        }
    }
}
