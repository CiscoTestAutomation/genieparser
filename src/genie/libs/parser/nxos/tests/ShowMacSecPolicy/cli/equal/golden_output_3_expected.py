expected_output = {
    "macsec_policy": {
        "MP1": {
            "cipher_suite": "GCM-AES-XPN-256",
            "icv_indicator": "FALSE",
            "include_sci": "TRUE",
            "offset": 0,
            "ppk_crypto_policy_name": "PPK1",
            "priority": 10,
            "sak_rekey_time": "pn-rollover",
            "security": "must-secure",
            "window": 148809600
        },
        "MP2": {
            "cipher_suite": "GCM-AES-XPN-256",
            "icv_indicator": "FALSE",
            "include_sci": "TRUE",
            "offset": 0,
            "ppk_crypto_policy_name": "PPK1",
            "priority": 10,
            "sak_rekey_time": "pn-rollover",
            "security": "must-secure",
            "window": 148809600
        },
        "Test": {
            "cipher_suite": "Enforce-Peer",
            "enforce_peer_cipher_suite": "GCM-AES-256",
            "icv_indicator": "FALSE",
            "include_sci": "TRUE",
            "offset": 0,
            "priority": 16,
            "sak_rekey_time": "pn-rollover",
            "security": "should-secure",
            "window": 148809600,
        },
        "system-default-macsec-policy": {
            "cipher_suite": "GCM-AES-XPN-256",
            "icv_indicator": "FALSE",
            "include_sci": "TRUE",
            "offset": 0,
            "priority": 16,
            "sak_rekey_time": "pn-rollover",
            "security": "should-secure",
            "window": 148809600
        }
    }
}