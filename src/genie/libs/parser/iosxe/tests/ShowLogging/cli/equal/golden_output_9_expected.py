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
            "size_bytes": 4096
        },
        "count_and_time_stamp_logging_messages": "disabled",
        "persistent": {
            "status": "disabled"
        },
        "trap": {
            "level": "informational",
            "message_lines_logged": 1190,
            "logging_source_interface": {
                "Loopback246": {},
                "GigabitEthernet1": {"vrf": "Mgmt-intf"},
                "Loopback1": {"vrf": "000000"},
                "Loopback2": {"vrf": "default"},
                "Loopback3": {"vrf": "global"}
            },
            "logging_to": {
                "55.55.55.70": {
                    "protocol": "udp",
                    "port": 514,
                    "audit": "disabled",
                    "vrf": "Mgmt-vrf",
                    "link": "up",
                    "message_lines_logged": 1189,
                    "message_lines_rate_limited": 0,
                    "message_lines_dropped_by_md": 0,
                    "xml": "disabled",
                    "sequence_number": "disabled",
                    "filtering": "disabled"
                },
                "11.11.11.1": {
                    "protocol": "udp",
                    "port": 514,
                    "audit": "disabled",
                    "link": "up",
                    "message_lines_logged": 1190,
                    "message_lines_rate_limited": 0,
                    "message_lines_dropped_by_md": 0,
                    "xml": "disabled",
                    "sequence_number": "disabled",
                    "filtering": "disabled"
                },
                "10.10.0.104": {
                    "protocol": "udp",
                    "port": 514,
                    "audit": "disabled",
                    "link": "up",
                    "message_lines_logged": 1190,
                    "message_lines_rate_limited": 0,
                    "message_lines_dropped_by_md": 0,
                    "xml": "disabled",
                    "sequence_number": "disabled",
                    "filtering": "disabled"
                },
                "10.10.0.251": {
                    "protocol": "udp",
                    "port": 514,
                    "audit": "disabled",
                    "link": "up",
                    "message_lines_logged": 1190,
                    "message_lines_rate_limited": 0,
                    "message_lines_dropped_by_md": 0,
                    "xml": "disabled",
                    "sequence_number": "disabled",
                    "filtering": "disabled"
                },
                "10.10.0.160": {
                    "protocol": "udp",
                    "port": 514,
                    "audit": "disabled",
                    "link": "up",
                    "message_lines_logged": 1190,
                    "message_lines_rate_limited": 0,
                    "message_lines_dropped_by_md": 0,
                    "xml": "disabled",
                    "sequence_number": "disabled",
                    "filtering": "disabled"
                },
                "10.10.0.117": {
                    "protocol": "udp",
                    "port": 514,
                    "audit": "disabled",
                    "link": "up",
                    "message_lines_logged": 1190,
                    "message_lines_rate_limited": 0,
                    "message_lines_dropped_by_md": 0,
                    "xml": "disabled",
                    "sequence_number": "disabled",
                    "filtering": "disabled",
                    "logging_source_interface": {
                        "logging_configuration": "Loopback3:global"
                    }
                }
            }
        }
    },
    "log_buffer_bytes": 214748364
}