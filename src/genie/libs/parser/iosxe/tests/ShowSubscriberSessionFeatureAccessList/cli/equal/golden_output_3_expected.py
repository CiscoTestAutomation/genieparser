expected_output = {
    "sessions": {
        138: {
            "type": "DHCPv4",
            "uid": 138,
            "state": "authen",
            "identity": "aaaa.bbbb.1111",
            "ipv4_address": "11.11.11.4",
            "session_up_time": "00:00:12",
            "last_changed": "00:00:12",
            "switch_id": 5730,
            "features": {
                "per_user_acl": {
                    0: {
                        "direction": "In",
                        "protocol": "IP",
                        "acl_name": "subscriber_feature#285212685949",
                        "source": "Peruser",
                    },
                    1: {
                        "direction": "Out",
                        "protocol": "IP",
                        "acl_name": "subscriber_feature#285212685950",
                        "source": "Peruser",
                    },
                }
            },
        }
    }
}
