expected_output = {
    "syslog_logging": {
        "enabled": {
            "counters": {
                "messages_dropped": 0,
                "messages_rate_limited": 2,
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
            "logging_source_interface": {
                "show": {
                    "vrf": "logging"
                }
            },
            "level": "informational",
            "message_lines_logged": 258
        }
    }
}

