expected_output = {
    "policy_num":{
        1:{
            "class":"script",
            "type":"user",
            "event_type":"syslog            ",
            "trap":"Off",
            "time_registered":"Wed Sep 15 11:29:18 2021",
            "eemfile_name":"eem_cli_exec_file.tcl",
            "pattern_name":"pattern {EEM script test message 1}",
            "nice_value":0,
            "queue_priority":"normal",
            "maxrun":100.0,
            "scheduler":"rp_primary",
            "secu":"none",
            "persist_time":3600,
            "username":"lab"
        },
        2:{
            "class":"script",
            "type":"user",
            "event_type":"timer watchdog    ",
            "trap":"Off",
            "time_registered":"Fri Sep 17 08:04:28 2021",
            "eemfile_name":"tm_watchdog_cli.tcl",
            "pattern_name":"name {watchtimer} time 180.000",
            "nice_value":0,
            "queue_priority":"normal",
            "maxrun":20.0,
            "scheduler":"rp_primary",
            "secu":"none",
            "persist_time":3600,
            "username":"lab"
        },
        3:{
            "class":"script",
            "type":"user",
            "event_type":"timer cron        ",
            "trap":"Off",
            "time_registered":"Fri Sep 17 08:42:03 2021",
            "eemfile_name":"tm_cron.tcl",
            "pattern_name":"name {crontimer2} cron entry {0-59/2 0-23/1 * * 0-7}",
            "nice_value":0,
            "queue_priority":"normal",
            "maxrun":20.0,
            "scheduler":"rp_primary",
            "secu":"none",
            "persist_time":3600,
            "username":"lab"
        },
        4:{
            "class":"script",
            "type":"system",
            "event_type":"timer cron        ",
            "trap":"Off",
            "time_registered":"Tue Sep 21 07:00:11 2021",
            "eemfile_name":"tm_crash_hist.tcl",
            "pattern_name":"name {crontimer1} cron entry {0 0 * * 0-6}",
            "nice_value":0,
            "queue_priority":"normal",
            "maxrun":20.0,
            "scheduler":"rp_primary",
            "secu":"none",
            "persist_time":3600,
            "username":"lab"
        }
    }
}

