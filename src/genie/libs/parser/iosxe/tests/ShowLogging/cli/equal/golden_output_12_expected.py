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
    "log_buffer_bytes": 214748364
}