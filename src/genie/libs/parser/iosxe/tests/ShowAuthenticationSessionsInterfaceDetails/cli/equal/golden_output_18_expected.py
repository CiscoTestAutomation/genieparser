expected_output = {
    "interfaces": {
        "GigabitEthernet0/1/0": {
            "mac_address": {
                "0030.0000.0001": {
                    "acct_session_id": "0x00000250",
                    "common_session_id": "1CB1A8C000000168BBA5232B",
                    "current_policy": "dot1x_dvlan_reauth_af",
                    "domain": "DATA",
                    "handle": "0x3400011e",
                    "iif_id": "0x09CB0212",
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
                            "vlan_group": {
                                "vlan": 60
                            }
                        }
                    },
                    "session_timeout": {
                        "remaining": "91s",
                        "timeout": "100s",
                        "type": "local",
                    },
                    "status": "Authorized",
                    "timeout_action": "Reauthenticate",
                    "user_name": "auto601",
                },
                "0030.00a0.0022": {
                    "acct_session_id": "0x00000251",
                    "common_session_id": "1CB1A8C000000169BBA71DFF",
                    "current_policy": "dot1x_dvlan_reauth_af",
                    "domain": "VOICE",
                    "handle": "0xfc00011f",
                    "iif_id": "0x07FA353B",
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
                            "vlan_group": {
                                "vlan": 160
                            }
                        }
                    },
                    "session_timeout": {
                        "remaining": "91s",
                        "timeout": "100s",
                        "type": "local",
                    },
                    "status": "Authorized",
                    "timeout_action": "Reauthenticate",
                    "user_name": "auto1601",
                }
            }
        }
    }
}
