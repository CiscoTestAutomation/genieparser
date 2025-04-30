expected_output = {
  "profiles": {
    "DefaultProfile": {
      "protocol": "TLSv1.2",
      "cipher_suite": "AES256-SHA",
      "authentication": "Certificate",
      "session_timeout_in_seconds": 3600,
      "renegotiation": "Enabled",
      "keepalive_interval_in_seconds": 60
    },
    "CustomProfile": {
      "protocol": "TLSv1.3",
      "cipher_suite": "AES128-GCM-SHA256",
      "authentication": "Pre-Shared Key",
      "session_timeout_in_seconds": 1800,
      "renegotiation": "Disabled",
      "keepalive_interval_in_seconds": 120
    }
  }
}
