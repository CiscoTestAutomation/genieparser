expected_output = {
    "syslog_logging": {
        "enabled": {
            "counters": {
                "messages_dropped": 0,
                "messages_rate_limited": 27,
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
            "status": "enabled",
            "level": "informational",
            "messages_logged": 1297,
            "xml": "disabled",
            "filtering": "disabled"
        },
        "buffer": {
            "status": "enabled",
            "level": "informational",
            "messages_logged": 5501,
            "xml": "disabled",
            "filtering": "disabled"
        },
        "exception": {
            "size_bytes": 4096
        },
        "count_and_time_stamp_logging_messages": "disabled",
        "persistent": {
            "status": "disabled"
        },
        "trap": {
            "level": "informational",
            "message_lines_logged": 5509,
            "logging_to": {
                "2001:DB8::1": {
                    "protocol": "udp",
                    "port": 514,
                    "audit": "disabled",
                    "vrf": "MGMT",
                    "link": "up",
                    "message_lines_logged": 5508,
                    "message_lines_rate_limited": 0,
                    "message_lines_dropped_by_md": 0,
                    "xml": "disabled",
                    "sequence_number": "disabled",
                    "filtering": "disabled"
                },
                "2001:DB8::2": {
                    "protocol": "udp",
                    "port": 514,
                    "audit": "disabled",
                    "vrf": "MGMT",
                    "link": "up",
                    "message_lines_logged": 5509,
                    "message_lines_rate_limited": 0,
                    "message_lines_dropped_by_md": 0,
                    "xml": "disabled",
                    "sequence_number": "disabled",
                    "filtering": "disabled",
                    "logging_source_interface": {
                        "logging_configuration": "Loopback0:MGMT"
                    }
                }
            },
            "logging_source_interface": {
                "Loopback0": {
                    "vrf": "MGMT"
                }
            }
        }
    },
    "log_buffer_bytes": 10000000,
    "logs": [
        "Logging to: vty2(1297)"
    ]
}