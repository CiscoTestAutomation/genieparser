expected_output = {
    "sessions": {
        61: {
            "type": "DHCPv4",
            "uid": 61,
            "state": "authen",
            "identity": "aaaa.bbbb.1111",
            "ipv4_address": "11.11.11.4",
            "session_up_time": "00:00:05",
            "last_changed": "00:00:07",
            "switch_id": 4328,
            "features": {
                "per_user_acl": {
                    0: {
                        "direction": "In",
                        "protocol": "IP",
                        "acl_name": "ACL_IN_INTERNET11",
                        "source": "Peruser",
                    },
                    1: {
                        "direction": "Out",
                        "protocol": "IP",
                        "acl_name": "ACL_OUT_INTERNET11",
                        "source": "Peruser",
                    },
                }
            },
        }
    }
}
