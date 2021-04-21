expected_output = {
    
   "syslog_logging":{
      "enabled":{
         "counters":{
            "messages_dropped": 0,
            "messages_rate_limited": 149,
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
         "messages_logged": 0,
         "xml": "disabled",
         "filtering": "disabled"
      },
      "buffer":{
         "status": "enabled",
         "level": "debugging",
         "messages_logged": 481,
         "xml": "disabled",
         "filtering": "disabled"
      },
      "exception":{
         "size_bytes": 4096
      },
      "count_and_time_stamp_logging_messages": "disabled",
      "persistent":{
         "status": "disabled"
      },
      "trap":{
         "level": "informational",
         "message_lines_logged": 478
      }
   },
   "log_buffer_bytes": 4096,
   "logs":[
      "Jun  5 05:09:30.838 EST: %IP-4-DUPADDR: Duplicate address 172.16.1.216 on GigabitEthernet1, sourced by 5e00.80ff.0606",
      "Jun  5 05:10:36.839 EST: %IP-4-DUPADDR: Duplicate address 172.16.1.216 on GigabitEthernet1, sourced by 5e00.80ff.0606",
      "Jun  5 05:10:59.519 EST: %SYS-5-CONFIG_I: Configured from console by cisco on console",
      "Jun  5 05:11:04.626 EST: Rollback:Acquired Configuration lock.",
      "Jun  5 05:11:04.626 EST: %SYS-5-CONFIG_R: Config Replace is Done",
      "Jun  5 05:11:14.115 EST: Rollback:Acquired Configuration lock.",
      "Jun  5 05:11:14.115 EST: %SYS-5-CONFIG_R: Config Replace is Done"
   ]

}
