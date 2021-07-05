expected_output = {
    "sessions": {
        1: {
            "child_sa_count": 2,
            "ike_count": 1,
            "status": "UP-ACTIVE",
            "tunnels": {
                "2001:db8:2:1::1/500-2001:db8:2:1::2/500": {
                    "activetime_secs": 880,
                    "authentication_sign": "PSK",
                    "authentication_verify": "PSK",
                    "child_sa": {
                        0: {
                            "esp_in": "0xbe064bdc",
                            "esp_out": "0x5db6eff3",
                            "local_selector": "2001:db8:1:2::/0 "
                            "- "
                            "2001:db8:1:2:ffff:ffff:ffff:ffff/65535",
                            "remote_selector": "2001:db8:3:2::/0 "
                            "- "
                            "2001:db8:3:2:ffff:ffff:ffff:ffff/65535",
                        },
                        1: {
                            "esp_in": "0x69b865f8",
                            "esp_out": "0x978dbbe5",
                            "local_selector": "2001:db8:1:1::/0 "
                            "- "
                            "2001:db8:1:1:ffff:ffff:ffff:ffff/65535",
                            "remote_selector": "2001:db8:3:1::/0 "
                            "- "
                            "2001:db8:3:1:ffff:ffff:ffff:ffff/65535",
                        },
                    },
                    "dh_group": 2,
                    "encryption_algorithm": "3DES",
                    "hashing_algorithm": "SHA96",
                    "lifetime_secs": 43200,
                    "local": "2001:db8:2:1::1/500",
                    "remote": "2001:db8:2:1::2/500",
                    "role": "INITIATOR",
                    "status": "READY",
                    "tunnel_id": 3686011,
                }
            },
        }
    }
}

