expected_output = {
    "syslog_logging": {
        "enabled": {
            "counters": {
                "messages_dropped": 0,
                "messages_rate_limited": 20,
                "flushes": 0,
                "overruns": 0,
                "xml": "disabled",
                "filtering": "disabled"
            }
        }
    },
    "logging": {
        "console": {
            "status": "disabled"
        },
        "monitor": {
            "status": "disabled"
        },
        "buffer": {
            "status": "disabled",
            "xml": "disabled",
            "filtering": "disabled"
        },
        "exception": {
            "status": "disabled",
        },
        "count_and_time_stamp_logging_messages": "disabled",
        "persistent": {
            "status": "enabled",
            "url": "bootflash:/",
            "file_size_bytes": 8192,
            "disk_space_bytes": 16384,
            "batch_size_bytes": 4096,
            "threshold_percent": 5,
            "threshold_alert": "enabled",
            "immediate_write": "enabled",
            "protected": "enabled",
            "notify": "enabled"
        },
        "trap": {
            "status": "disabled"
        }
    },
    "log_buffer_bytes": 214748364,
    "tls_profiles": {
        "LOG-TLS": {
            "ciphersuites": ["Default"],
            "trustpoint": "tls-trustpoint-name",
            "tls_version": "TLSv1.2"
        },
        "LOG-TLS-2": {
            "ciphersuites": [
                "ecdhe-rsa-aes-gcm-sha2",
                "ecdhe-ecdsa-aes-gcm-sha2"
            ],
            "trustpoint": "Default",
            "tls_version": "TLSv1.2"
        },
        "TLSPROFILE3": {
            "ciphersuites": ["Default"],
            "trustpoint": "Default",
            "tls_version": "Default"
        }
    },
    "logs": [
        "*Aug 23 14:04:05.376: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet1, changed state to up",
        "*Aug 23 14:04:05.377: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet2, changed state to up"
    ]
}