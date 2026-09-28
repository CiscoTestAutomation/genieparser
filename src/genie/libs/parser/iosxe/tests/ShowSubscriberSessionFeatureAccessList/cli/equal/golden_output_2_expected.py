expected_output = {
    "sessions": {
        156: {
            "type": "DHCPv4",
            "uid": 156,
            "state": "authen",
            "identity": "aaaa.bbbb.1111",
            "ipv4_address": "11.11.11.4",
            "session_up_time": "00:00:05",
            "last_changed": "00:00:07",
            "switch_id": 4737,
            "features": {
                "per_user_acl": {
                    0: {
                        "direction": "In",
                        "protocol": "IP",
                        "acl_name": "subscriber_feature#280179522749",
                        "source": "Peruser",
                    },
                    1: {
                        "direction": "Out",
                        "protocol": "IP",
                        "acl_name": "subscriber_feature#280179522750",
                        "source": "Peruser",
                    },
                }
            },
        }
    }
}
