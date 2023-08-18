expected_output = {
    "key_chains": {
        "KCP128": {
            "keys": {
                "0": {
                    "key_string": "cisco ",
                    "cryptographic_algo": "hmac-sha-1",
                    "accept_lifetime": {
                        "start": "always valid",
                        "end": "always valid",
                        "is_valid": True
                    },
                    "send_lifetime": {
                        "start": "always valid",
                        "end": "always valid",
                        "is_valid": True
                    }
                }
            }
        },
        "KCP256": {
            "is_macsec": True,
            "keys": {
                "AAAA": {
                    "key_string": "1111111122222222333333334444444455555555666666667777777799999999",
                    "cryptographic_algo": "aes-256-cmac",
                    "lifetime": {
                        "start": "12:40:00 UTC Jun 1 2023",
                        "end": "13:21:00 UTC Jun 1 2023",
                        "is_valid": False
                    }
                },
                "BBBB": {
                    "key_string": "1111111122222222333333334444444455555555666666667777777700000000",
                    "cryptographic_algo": "aes-256-cmac",
                    "lifetime": {
                        "start": "20:20:00 IST Jun 15 2023",
                        "end": "20:34:00 IST Jun 15 2023",
                        "is_valid": False
                    }
                }
            }
        },
        "et0297-cpe-macsec-keychain": {
            "is_macsec": True,
            "keys": {
                "0297": {
                    "key_string": "40e9caa8e2b89e799501fc404963f10541123d89d2162ea0ea09593b249937e4",
                    "cryptographic_algo": "aes-256-cmac",
                    "lifetime": {
                        "start": "always valid",
                        "end": "always valid",
                        "is_valid": True
                    }
                }
            }
        }
    }
}