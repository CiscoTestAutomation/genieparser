expected_output = {
    "logs": [
        "*Aug 19 15:23:24.798: %SYS-5-CONFIG_I: Configured from console by cisco on vty1 (10.10.20.50)"
    ],
    "syslog_logging": {
        "enabled": {
            "counters": {
                "messages_dropped": 0,
                "messages_rate_limited": 1,
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
            "level": "debugging",
            "messages_logged": 0,
            "xml": "disabled",
            "filtering": "disabled"
        },
        "buffer": {
            "status": "enabled",
            "level": "debugging",
            "messages_logged": 59,
            "xml": "disabled",
            "filtering": "disabled"
        },
        "exception": {
            "size_bytes": 8192
        },
        "count_and_time_stamp_logging_messages": "disabled",
        "persistent": {
            "status": "disabled"
        },
        "trap": {
            "level": "informational",
            "message_lines_logged": 62,
            "logging_source_interface": {
                "Loopback246": {},
                "GigabitEthernet1": {"vrf": "Mgmt-intf"},
                "Loopback1": {"vrf": "000000"},
                "Loopback2": {"vrf": "default"},
                "Loopback3": {"vrf": "global"}
            }
        }
    },
    "log_buffer_bytes": 8192
}