expected_output = {
    "interfaces": {
        "GigabitEthernet1/0/12": {
            "mac_address": {
                "0010.00ff.1011": {
                    "acct_session_id": "Unknown",
                    "common_session_id": "AC14FC0A0000101200E28D62",
                    "current_policy": "dot1x_dvlan_reauth_hm",
                    "domain": "DATA",
                    "handle": "0xDB003227",
                    "iif_id": "0x1055240000001F6",
                    "ipv4_address": "192.0.2.1",
                    "ipv6_address": "Unknown",
                    "local_policies": {
                        "template": {"CRITICAL_VLAN": {"priority": 170}},
                        "vlan_group": {"vlan": 100},
                    },
                    "method_status": {"mab": {"method": "mab", "state": "Running"}},
                    "oper_control_dir": "both",
                    "oper_host_mode": "single-host",
                    "session_timeout": {"type": "N/A"},
                    "status": "Authorized",
                    "user_name": "genie123",
                }
            }
        }
    }
}
