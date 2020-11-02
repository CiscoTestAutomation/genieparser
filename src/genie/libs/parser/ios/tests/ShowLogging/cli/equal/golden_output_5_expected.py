expected_output = {
  "log_buffer_bytes": 512000,
  "logging": {
    "buffer": {
      "filtering": "disabled",
      "level": "debugging",
      "messages_logged": 9789,
      "status": "enabled",
      "xml": "disabled"
    },
    "console": {
      "filtering": "disabled",
      "level": "debugging",
      "messages_logged": 9789,
      "status": "enabled",
      "xml": "disabled"
    },
    "count_and_time_stamp_logging_messages": "disabled",
    "exception": {
      "size_bytes": 4096
    },
    "monitor": {
      "filtering": "disabled",
      "level": "debugging",
      "messages_logged": 0,
      "status": "enabled",
      "xml": "disabled"
    },
    "persistent": {
      "batch_size_bytes": 4096,
      "disk_space_bytes": 104857600,
      "file_size_bytes": 10485760,
      "status": "enabled",
      "url": "bootflash:/syslog"
    },
    "trap": {
      "level": "informational",
      "message_lines_logged": 9780
    }
  },
  "logs": [
    "*Oct 15 09:12:40.734: %SYS-6-LOGOUT: User admin has exited tty session 866(192.168.1.31)",
    "*Oct 15 09:13:24.005: %SELINUX-3-MISMATCH: R0/0: audispd: type=AVC msg=audit(1602753204.003:5355): avc:  denied  { mounton } for  pid=11284 comm=\"DNS\" path=\"/sys\" dev=\"overlay\" ino=27798 scontext=system_u:system_r:polaris_vdaemon_t:s0 tcontext=system_u:object_r:tmp_t:s0 tclass=dir permissive=1"
  ],
  "syslog_logging": {
    "enabled": {
      "counters": {
        "filtering": "disabled",
        "flushes": 0,
        "messages_dropped": 0,
        "messages_rate_limited": 3,
        "overruns": 0,
        "xml": "disabled"
      }
    }
  }
}

