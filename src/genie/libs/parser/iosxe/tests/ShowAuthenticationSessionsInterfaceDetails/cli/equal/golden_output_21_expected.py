expected_output = {
    "interfaces": {
        "GigabitEthernet3/0/27": {
            "mac_address": {
                "0012.0100.0001": {
                    "ipv6_address": "Unknown",
                    "iif_id": "0x1AB852F4",
                    "ipv4_address": "106.10.0.9",
                    "user_name": "AAA_TC01",
                    "status": "Authorized",
                    "domain": "DATA",
                    "oper_host_mode": "multi-auth",
                    "oper_control_dir": "both",
                    "session_timeout": {
                        "type": "server",
                        "timeout": "60s",
                        "remaining": "40s"
                    },
                    "timeout_action": "Reauthenticate",
                    "common_session_id": "EE01060A00000051F9D34746",
                    "acct_session_id": "0x0000003a",
                    "handle": "0xf5000047",
                    "current_policy": "POLICY_Gi1/0/12",
                    "server_policies": {
                        1: {
                            "name": "Session-Timeout",
                            "policies": "60 sec",
                            "vlan_group": {
                                "vlan": 106
                            }
                        },
                        2: {
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-AAA_TC01_dvlan_permit-6564d970"
                        }
                    },
                    "method_status": {
                        "dot1x": {
                            "method": "dot1x",
                            "state": "Authc Success"
                        }
                    }
                },
                "0012.0100.0002": {
                    "ipv6_address": "Unknown",
                    "iif_id": "0x18173A4A",
                    "ipv4_address": "106.10.0.5",
                    "user_name": "AAA_TC02",
                    "status": "Authorized",
                    "domain": "DATA",
                    "oper_host_mode": "multi-auth",
                    "oper_control_dir": "both",
                    "session_timeout": {
                        "type": "server",
                        "timeout": "60s",
                        "remaining": "40s"
                    },
                    "timeout_action": "Reauthenticate",
                    "common_session_id": "EE01060A00000052F9D34747",
                    "acct_session_id": "0x00000035",
                    "handle": "0x82000048",
                    "current_policy": "POLICY_Gi1/0/12",
                    "server_policies": {
                        1: {
                            "name": "Session-Timeout",
                            "policies": "60 sec",
                            "vlan_group": {
                                "vlan": 106
                            }
                        },
                        2: {
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-AAA_TC01_dvlan_permit-6564d970"
                        }
                    },
                    "method_status": {
                        "dot1x": {
                            "method": "dot1x",
                            "state": "Authc Success"
                        }
                    }
                },
                "0012.0100.0003": {
                    "ipv6_address": "Unknown",
                    "iif_id": "0x1D88E420",
                    "ipv4_address": "106.10.0.8",
                    "user_name": "AAA_TC03",
                    "status": "Authorized",
                    "domain": "DATA",
                    "oper_host_mode": "multi-auth",
                    "oper_control_dir": "both",
                    "session_timeout": {
                        "type": "server",
                        "timeout": "60s",
                        "remaining": "40s"
                    },
                    "timeout_action": "Reauthenticate",
                    "common_session_id": "EE01060A00000053F9D34748",
                    "acct_session_id": "0x00000033",
                    "handle": "0xe2000049",
                    "current_policy": "POLICY_Gi1/0/12",
                    "server_policies": {
                        1: {
                            "name": "Session-Timeout",
                            "policies": "60 sec",
                            "vlan_group": {
                                "vlan": 106
                            }
                        },
                        2: {
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-AAA_TC01_dvlan_permit-6564d970"
                        }
                    },
                    "method_status": {
                        "dot1x": {
                            "method": "dot1x",
                            "state": "Authc Success"
                        }
                    }
                },
                "0012.0100.0004": {
                    "ipv6_address": "Unknown",
                    "iif_id": "0x1614C188",
                    "ipv4_address": "106.10.0.3",
                    "user_name": "AAA_TC04",
                    "status": "Authorized",
                    "domain": "DATA",
                    "oper_host_mode": "multi-auth",
                    "oper_control_dir": "both",
                    "session_timeout": {
                        "type": "server",
                        "timeout": "60s",
                        "remaining": "40s"
                    },
                    "timeout_action": "Reauthenticate",
                    "common_session_id": "EE01060A00000054F9D3474A",
                    "acct_session_id": "0x00000037",
                    "handle": "0xe300004a",
                    "current_policy": "POLICY_Gi1/0/12",
                    "server_policies": {
                        1: {
                            "name": "Session-Timeout",
                            "policies": "60 sec",
                            "vlan_group": {
                                "vlan": 106
                            }
                        },
                        2: {
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-AAA_TC01_dvlan_permit-6564d970"
                        }
                    },
                    "method_status": {
                        "dot1x": {
                            "method": "dot1x",
                            "state": "Authc Success"
                        }
                    }
                },
                "0012.0100.0005": {
                    "ipv6_address": "Unknown",
                    "iif_id": "0x16A5524F",
                    "ipv4_address": "106.10.0.7",
                    "user_name": "AAA_TC05",
                    "status": "Authorized",
                    "domain": "DATA",
                    "oper_host_mode": "multi-auth",
                    "oper_control_dir": "both",
                    "session_timeout": {
                        "type": "server",
                        "timeout": "60s",
                        "remaining": "40s"
                    },
                    "timeout_action": "Reauthenticate",
                    "common_session_id": "EE01060A00000055F9D3474B",
                    "acct_session_id": "0x00000039",
                    "handle": "0x8f00004b",
                    "current_policy": "POLICY_Gi1/0/12",
                    "server_policies": {
                        1: {
                            "name": "Session-Timeout",
                            "policies": "60 sec",
                            "vlan_group": {
                                "vlan": 106
                            }
                        },
                        2: {
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-AAA_TC01_dvlan_permit-6564d970"
                        }
                    },
                    "method_status": {
                        "dot1x": {
                            "method": "dot1x",
                            "state": "Authc Success"
                        }
                    }
                },
                "0012.0100.0006": {
                    "ipv6_address": "Unknown",
                    "iif_id": "0x19101752",
                    "ipv4_address": "Unknown",
                    "user_name": "AAA_TC06",
                    "status": "Authorized",
                    "domain": "DATA",
                    "oper_host_mode": "multi-auth",
                    "oper_control_dir": "both",
                    "session_timeout": {
                        "type": "server",
                        "timeout": "60s",
                        "remaining": "40s"
                    },
                    "timeout_action": "Reauthenticate",
                    "common_session_id": "EE01060A00000056F9D3474C",
                    "acct_session_id": "0x0000003b",
                    "handle": "0xe000004c",
                    "current_policy": "POLICY_Gi1/0/12",
                    "server_policies": {
                        1: {
                            "name": "Session-Timeout",
                            "policies": "60 sec",
                            "vlan_group": {
                                "vlan": 106
                            }
                        },
                        2: {
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-AAA_TC01_dvlan_permit-6564d970"
                        }
                    },
                    "method_status": {
                        "dot1x": {
                            "method": "dot1x",
                            "state": "Authc Success"
                        }
                    }
                },
                "0012.0100.0007": {
                    "ipv6_address": "Unknown",
                    "iif_id": "0x1B712597",
                    "ipv4_address": "106.10.0.10",
                    "user_name": "AAA_TC07",
                    "status": "Authorized",
                    "domain": "DATA",
                    "oper_host_mode": "multi-auth",
                    "oper_control_dir": "both",
                    "session_timeout": {
                        "type": "server",
                        "timeout": "60s",
                        "remaining": "40s"
                    },
                    "timeout_action": "Reauthenticate",
                    "common_session_id": "EE01060A00000057F9D3474F",
                    "acct_session_id": "0x0000003c",
                    "handle": "0x8400004d",
                    "current_policy": "POLICY_Gi1/0/12",
                    "server_policies": {
                        1: {
                            "name": "Session-Timeout",
                            "policies": "60 sec",
                            "vlan_group": {
                                "vlan": 106
                            }
                        },
                        2: {
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-AAA_TC01_dvlan_permit-6564d970"
                        }
                    },
                    "method_status": {
                        "dot1x": {
                            "method": "dot1x",
                            "state": "Authc Success"
                        }
                    }
                },
                "0012.0100.0008": {
                    "ipv6_address": "Unknown",
                    "iif_id": "0x1A1A3E45",
                    "ipv4_address": "106.10.0.6",
                    "user_name": "AAA_TC08",
                    "status": "Authorized",
                    "domain": "DATA",
                    "oper_host_mode": "multi-auth",
                    "oper_control_dir": "both",
                    "session_timeout": {
                        "type": "server",
                        "timeout": "60s",
                        "remaining": "40s"
                    },
                    "timeout_action": "Reauthenticate",
                    "common_session_id": "EE01060A00000058F9D3474F",
                    "acct_session_id": "0x00000036",
                    "handle": "0x5d00004e",
                    "current_policy": "POLICY_Gi1/0/12",
                    "server_policies": {
                        1: {
                            "name": "Session-Timeout",
                            "policies": "60 sec",
                            "vlan_group": {
                                "vlan": 106
                            }
                        },
                        2: {
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-AAA_TC01_dvlan_permit-6564d970"
                        }
                    },
                    "method_status": {
                        "dot1x": {
                            "method": "dot1x",
                            "state": "Authc Success"
                        }
                    }
                },
                "0012.0100.0009": {
                    "ipv6_address": "Unknown",
                    "iif_id": "0x1243E0DC",
                    "ipv4_address": "106.10.0.1",
                    "user_name": "AAA_TC09",
                    "status": "Authorized",
                    "domain": "DATA",
                    "oper_host_mode": "multi-auth",
                    "oper_control_dir": "both",
                    "session_timeout": {
                        "type": "server",
                        "timeout": "60s",
                        "remaining": "40s"
                    },
                    "timeout_action": "Reauthenticate",
                    "common_session_id": "EE01060A00000059F9D34751",
                    "acct_session_id": "0x00000034",
                    "handle": "0xae00004f",
                    "current_policy": "POLICY_Gi1/0/12",
                    "server_policies": {
                        1: {
                            "name": "Session-Timeout",
                            "policies": "60 sec",
                            "vlan_group": {
                                "vlan": 106
                            }
                        },
                        2: {
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-AAA_TC01_dvlan_permit-6564d970"
                        }
                    },
                    "method_status": {
                        "dot1x": {
                            "method": "dot1x",
                            "state": "Authc Success"
                        }
                    }
                },
                "0012.0100.000a": {
                    "ipv6_address": "Unknown",
                    "iif_id": "0x1AED585C",
                    "ipv4_address": "106.10.0.4",
                    "user_name": "AAA_TC010",
                    "status": "Authorized",
                    "domain": "DATA",
                    "oper_host_mode": "multi-auth",
                    "oper_control_dir": "both",
                    "session_timeout": {
                        "type": "server",
                        "timeout": "60s",
                        "remaining": "40s"
                    },
                    "timeout_action": "Reauthenticate",
                    "common_session_id": "EE01060A0000005AF9D34752",
                    "acct_session_id": "0x00000038",
                    "handle": "0x74000050",
                    "current_policy": "POLICY_Gi1/0/12",
                    "server_policies": {
                        1: {
                            "name": "Session-Timeout",
                            "policies": "60 sec",
                            "vlan_group": {
                                "vlan": 106
                            }
                        },
                        2: {
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-AAA_TC01_dvlan_permit-6564d970"
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
