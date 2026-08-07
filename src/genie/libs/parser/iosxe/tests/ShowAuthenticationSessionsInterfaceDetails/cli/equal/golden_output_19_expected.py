expected_output = {
    "interfaces": {
        "GigabitEthernet0/1/1": {
            "mac_address": {
                "0030.0000.0002": {
                    "acct_session_id": "0x00000252",
                    "common_session_id": "1CB1A8C000000168BBA5232C",
                    "current_policy": "dot1x_dvlan_reauth_af",
                    "domain": "DATA",
                    "handle": "0x3400011f",
                    "iif_id": "0x09CB0213",
                    "ipv4_address": "Unknown",
                    "ipv6_address": "Unknown",
                    "method_status": {
                        "dot1x": {
                            "method": "dot1x",
                            "state": "Authc Success",
                        }
                    },
                    "oper_control_dir": "both",
                    "oper_host_mode": "multi-domain",
                    "server_policies": {
                        1: {
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-Test_ACL-12345678",
                        },
                        2: {
                            "vlan_group": {
                                "vlan": 60
                            }
                        },
                    },
                    "session_timeout": {
                        "remaining": "91s",
                        "timeout": "100s",
                        "type": "local",
                    },
                    "status": "Authorized",
                    "timeout_action": "Reauthenticate",
                    "user_name": "auto602",
                }
            }
        }
    }
}
