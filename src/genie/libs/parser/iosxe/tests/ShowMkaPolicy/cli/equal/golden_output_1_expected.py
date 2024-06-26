expected_output = {
    "policy": {
        "MACSEC_POLICY_1": {
            "key_server_priority": 0,
            "delay_protect": "FALSE",
            "confidentiality_offset": 0,
            "sak_rey_key_on_live_peer_loss": "FALSE",
            "include_icv_indicator": "TRUE",
            "cipher": "GCM-AES-256",
            "interfaces": [
                "Te0/0/0",
                "Te0/0/1"
            ]
        }
    }
}
