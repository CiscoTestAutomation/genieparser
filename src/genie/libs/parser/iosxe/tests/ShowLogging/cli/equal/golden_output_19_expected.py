expected_output = {
    "syslog_logging": {
        "enabled": {
            "counters": {
                "messages_dropped": 0,
                "messages_rate_limited": 916,
                "flushes": 0,
                "overruns": 0,
                "xml": "disabled",
                "filtering": "disabled"
            }
        }
    },
    "logging": {
        "console": {
            "status": "enabled",
            "level": "debugging",
            "messages_logged": 1229,
            "xml": "disabled",
            "filtering": "disabled"
        },
        "monitor": {
            "status": "enabled",
            "level": "debugging",
            "messages_logged": 2220,
            "xml": "disabled",
            "filtering": "disabled"
        },
        "buffer": {
            "status": "enabled",
            "level": "debugging",
            "messages_logged": 0,
            "xml": "disabled",
            "filtering": "enabled"
        },
        "exception": {
            "size_bytes": 4096
        },
        "count_and_time_stamp_logging_messages": "disabled",
        "persistent": {
            "status": "disabled"
        },
        "trap": {
            "logging_source_interface": {
                "show": {
                    "vrf": "logging"
                },
                "tls-profile:": {
                    "vrf": "syslog-tls-1"
                }
            },
            "level": "informational",
            "message_lines_logged": 2283,
            "logging_to": {
                "10.64.69.167": {
                    "protocol": "tls",
                    "port": 6514,
                    "audit": "disabled",
                    "link": "up",
                    "message_lines_logged": 39,
                    "message_lines_rate_limited": 0,
                    "message_lines_dropped_by_md": 0,
                    "xml": "disabled",
                    "sequence_number": "disabled",
                    "filtering": "disabled",
                    "logging_source_interface": {
                        "logging_configuration": "tls-profile::syslog-tls-1"
                    }
                }
            }
        }
    },
    "logs": [
        "Inactive Message Discriminator:",
        "test      mnemonics      drops    CONFIG_I",
        "dis1      msg-body       drops    \"Configured from console by cisco\"",
        "test2     msg-body       drops    Configured from console by cisco on vty0 (173.39.61.194)"
    ],
    "tls_profiles": {
        "{'syslog-tls-1'}": {
            "ciphersuites": [
                "Default"
            ],
            "trustpoint": "Default",
            "tls_version": "Default"
        },
        "syslog_tls_1": {
            "ciphersuites": [
                "aes-256-cbc-sha"
            ],
            "trustpoint": "tp1",
            "tls_version": "TLSv1.3"
        },
        "syslog_tls_2": {
            "ciphersuites": [
                "Default"
            ],
            "trustpoint": "tp1",
            "tls_version": "TLSv1.3"
        },
        "syslog-tls-1": {
            "ciphersuites": [
                "aes-128-cbc-sha",
                "ecdhe-rsa-aes-cbc-sha2",
                "tls13-chacha20-poly1305-sha256"
            ],
            "trustpoint": "tp1",
            "tls_version": "TLSv1.3"
        }
    }
}
