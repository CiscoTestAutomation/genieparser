expected_output = {
    
   "syslog_logging":{
      "enabled":{
         "counters":{
            "messages_dropped": 0,
            "messages_rate_limited": 0,
            "flushes": 0,
            "overruns": 0,
            "xml": "disabled",
            "filtering": "disabled"
         }
      }
   },
   "logging":{
      "console":{
         "status": "disabled"
      },
      "monitor":{
         "status": "enabled",
         "level": "debugging",
         "messages_logged": 13,
         "xml": "disabled",
         "filtering": "disabled"
      },
      "buffer":{
         "status": "enabled",
         "level": "debugging",
         "messages_logged": 1566,
         "xml": "disabled",
         "filtering": "disabled"
      },
      "exception":{
         "size_bytes": 4096
      },
      "count_and_time_stamp_logging_messages": "disabled",
      "file":{
         "status": "disabled"
      },
      "persistent":{
         "status": "disabled"
      },
      "trap":{
         "level": "informational",
         "message_lines_logged": 1570,
         "logging_source_interface": {
            "Vlan200": {}
         },
         "logging_to":{
            "192.168.1.3":{
               "protocol": "tcp",
               "port": 1514,
               "audit": "disabled",
               "link": "down",
               "message_lines_logged": 787,
               "message_lines_rate_limited": 0,
               "message_lines_dropped_by_md": 0,
               "xml": "disabled",
               "sequence_number": "disabled",
               "filtering": "disabled"
            },
            "10.19.33.4":{
               "protocol": "udp",
               "port": 888,
               "audit": "disabled",
               "link": "down",
               "message_lines_logged": 0,
               "message_lines_rate_limited": 0,
               "message_lines_dropped_by_md": 0,
               "xml": "disabled",
               "sequence_number": "disabled",
               "filtering": "disabled",
               "logging_source_interface":{
                  "logging_configuration": "Vlan200"
               }
            }
         }
      }
   },
   "log_buffer_bytes": 32000,
}