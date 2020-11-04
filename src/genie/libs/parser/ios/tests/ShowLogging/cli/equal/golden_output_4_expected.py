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
    "console": { "status": "disabled" },
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
      "messages_logged": 2213,
      "xml": "disabled",
      "filtering": "disabled"
    },
    "exception": { "size_bytes": 4096 },
    "count_and_time_stamp_logging_messages": "disabled",
    "persistent": { "status": "disabled" },
    "trap": { "level": "informational", "message_lines_logged": 2207 }
  },
  "log_buffer_bytes": 4096,
  "logs": [
    "User 'developer' authenticated successfully from 172.16.196.146:0 and was authorized for rest over http. External groups: PRIV15"
  ]
}

