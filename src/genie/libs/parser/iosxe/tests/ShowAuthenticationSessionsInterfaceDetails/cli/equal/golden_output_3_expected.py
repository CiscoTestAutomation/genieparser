expected_output = {
    "interfaces": {
        "GigabitEthernet3/0/2": {
            "mac_address": {
                "0010.00ff.1011": {
                    "iif_id": "0x1055240000001F6",
                    "ipv6_address": "Unknown",
                    "ipv4_address": "192.0.2.1",
                    "user_name": "genie123",
                    "status": "Authorized",
                    "domain": "DATA",
                    "current_policy": "dot1x_dvlan_reauth_hm",
                    "oper_host_mode": "single-host",
                    "oper_control_dir": "both",
                    "session_timeout": {"type": "N/A"},
                    "common_session_id": "AC14FC0A0000101200E28D62",
                    "acct_session_id": "Unknown",
                    "handle": "0xDB003227",
                    "local_policies": {
                        "template": {"CRITICAL_VLAN": {"priority": 150}},
                        "vlan_group": {"vlan": 130},
                    },
                    "method_status": {
                        "dot1x": {"method": "dot1x", "state": "Authc Failed"}
                    },
                }
            }
        }
    }
}
