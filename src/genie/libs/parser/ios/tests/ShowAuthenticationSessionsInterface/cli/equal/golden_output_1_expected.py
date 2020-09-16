expected_output = {
    "interfaces": {
        "GigabitEthernet2/0/47": {
            "mac_address": {
                "Unknown": {
                    "ipv4_address": "Unknown",
                    "status": "Authz Success",
                    "domain": "DATA",
                    "oper_host_mode": "multi-host",
                    "oper_control_dir": "both",
                    "authorized_by": "Guest Vlan",
                    "vlan_policy": "20",
                    "session_timeout": {"type": "N/A"},
                    "idle_timeout": "N/A",
                    "common_session_id": "0A3462C8000000000002763C",
                    "acct_session_id": "0x00000002",
                    "handle": "0x25000000",
                    "method_status": {
                        "mab": {"method": "mab", "state": "Failed over"},
                        "dot1x": {"method": "dot1x", "state": "Failed over"},
                    },
                }
            }
        }
    }
}
