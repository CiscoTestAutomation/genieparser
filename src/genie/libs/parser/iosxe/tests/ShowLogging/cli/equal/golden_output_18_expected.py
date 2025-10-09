expected_output = {
    "syslog_logging": {
        "enabled": {
            "counters": {
                "messages_dropped": 0,
                "messages_rate_limited": 0,
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
            "messages_logged": 124,
            "xml": "disabled",
            "filtering": "disabled"
        },
        "monitor": {
            "status": "enabled",
            "level": "debugging",
            "messages_logged": 0,
            "xml": "disabled",
            "filtering": "disabled"
        },
        "buffer": {
            "status": "enabled",
            "level": "debugging",
            "messages_logged": 128,
            "xml": "disabled",
            "filtering": "disabled"
        },
        "exception": {
            "size_bytes": 4096
        },
        "count_and_time_stamp_logging_messages": "disabled",
        "file": {
            "status": "disabled"
        },
        "persistent": {
            "status": "disabled"
        },
        "trap": {
            "level": "notifications",
            "message_lines_logged": 68,
            "logging_to": {
                "192.0.2.10": {
                    "protocol": "udp",
                    "port": 514,
                    "audit": "disabled",
                    "link": "up",
                    "authentication": "disabled",
                    "encryption": "disabled",
                    "message_lines_logged": 68,
                    "message_lines_rate_limited": 0,
                    "message_lines_dropped_by_md": 0,
                    "xml": "disabled",
                    "sequence_number": "disabled",
                    "filtering": "disabled"
                },
                "192.0.2.11": {
                    "protocol": "udp",
                    "port": 514,
                    "audit": "disabled",
                    "vrf": "Mgmt-vrf",
                    "link": "down",
                    "authentication": "disabled",
                    "encryption": "disabled",
                    "message_lines_logged": 0,
                    "message_lines_rate_limited": 0,
                    "message_lines_dropped_by_md": 0,
                    "xml": "disabled",
                    "sequence_number": "disabled",
                    "filtering": "disabled"
                }
            }
        }
    },
    "log_buffer_bytes": 4096,
    "logs": [
        "{output removed here for brevity and privacy}"
    ]
}
