expected_output = {
    "interfaces": {
        "GigabitEthernet0/1/0": {
            "mac_address": {
                "0030.0000.0001": {
                    "acct_session_id": "0x0000024f",
                    "common_session_id": "1CB1A8C000000168BBA5232B",
                    "current_policy": "dot1x_dvlan_reauth_af",
                    "domain": "UNKNOWN",
                    "handle": "0x3400011e",
                    "iif_id": "0x09CB0212",
                    "ipv4_address": "Unknown",
                    "ipv6_address": "Unknown",
                    "local_policies": {
                        "template": {"AUTHFAIL_VLAN": {"priority": 150}},
                        "vlan_group": {"vlan": 110},
                    },
                    "method_status": {
                        "dot1x": {
                            "method": "dot1x",
                            "state": "Authc Failed",
                        }
                    },
                    "oper_control_dir": "both",
                    "oper_host_mode": "multi-domain",
                    "session_timeout": {
                        "remaining": "12s",
                        "timeout": "100s",
                        "type": "local",
                    },
                    "status": "Authorized",
                    "timeout_action": "Reauthenticate",
                    "user_name": "auto601",
                }
            }
        }
    }
}
