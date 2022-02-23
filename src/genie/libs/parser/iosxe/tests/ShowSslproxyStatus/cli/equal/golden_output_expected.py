expected_output = {
    "configuration": {
        "ca_cert_bundle": "/bootflash/vmanage-admin/sslProxyDefaultCAbundle.pem",
        "ca_tp_label": "PROXY-SIGNING-CA",
        "cert_lifetime": 730,
        "ec_key_type": "P256",
        "rsa_key_modulus": 2048,
        "cert_revocation": "NONE",
        "expired_cert": "drop",
        "untrusted_cert": "drop",
        "unknown_status": "drop",
        "unsupported_protocol_ver": "drop",
        "unsupported_cipher_suites": "drop",
        "failure_mode_action": "close",
        "min_tls_ver": "TLS Version 1.1",
        "dual_side_optimization": "TRUE",
    },
    "status": {
        "ssl_proxy_operational_state": "RUNNING",
        "tcp_proxy_operational_state": "RUNNING",
        "clear_mode": "FALSE",
    },
}
