expected_output = {
    "interfaces": {
        "GigabitEthernet2/0/47": {
            "mac_address": {
                "0001.10ff.1111": {
                    "acct_session_id": "0x00000002",
                    "authorized_by": "Guest Vlan",
                    "common_session_id": "0A3462C8000000000002763C",
                    "domain": "DATA",
                    "handle": "0x25000000",
                    "idle_timeout": "N/A",
                    "ipv4_address": "10.1.2.3",
                    "method_status": {
                        "dot1x": {"method": "dot1x", "state": "Failed over"},
                        "mab": {"method": "mab", "state": "Failed over"},
                    },
                    "oper_control_dir": "both",
                    "oper_host_mode": "multi-host",
                    "session_timeout": {"type": "N/A"},
                    "status": "Authz Success",
                    "vlan_policy": "20",
                },
                "0005.5eff.5781": {
                    "acct_session_id": "0x00000003",
                    "authorized_by": "Authentication Server",
                    "common_session_id": "0A3462C8000000010002A238",
                    "domain": "VOICE",
                    "handle": "0x91000001",
                    "idle_timeout": "N/A",
                    "ipv4_address": "10.1.3.5",
                    "method_status": {
                        "dot1x": {"method": "dot1x", "state": "Not run"},
                        "mab": {"method": "mab", "state": "Authc Success"},
                    },
                    "oper_control_dir": "both",
                    "oper_host_mode": "multi-domain",
                    "session_timeout": {"type": "N/A"},
                    "status": "Authz Success",
                    "user_name": "00055eff5781",
                },
            }
        }
    }
}
