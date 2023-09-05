expected_output = {
    "syslog_logging": {
        "enabled": {
            "counters": {
                "messages_dropped": 0,
                "messages_rate_limited": 64,
                "flushes": 0,
                "overruns": 0,
                "xml": "disabled",
                "filtering": "disabled"
            }
        }
    },
    "logging": {
        "console": {
            "status": "enabled",
            "level": "debugging",
            "messages_logged": 734,
            "xml": "disabled",
            "filtering": "disabled"
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
            "messages_logged": 1230,
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
            "message_lines_logged": 1205
        }
    },
    "log_buffer_bytes": 5000,
    "logs": [
        "OIN_DISJOIN: Chassis 2 R0/0: wncd: AP Event: AP Name: L11_2003_AP2 Mac: ccdb.93df.bbe0 Session-IP: 9.2.91.59[5264] 9.2.89.30[5246] Disjoined Tag modified",
        "Aug 14 13:04:09.111: %SYS-5-CONFIG_I: Configured from console by giri on console",
        "Aug 14 13:04:16.789: %APMGR_TRACE_MESSAGE-2-WLC_APMGR_CRIT_MSG: Chassis 2 R0/0: wncd: CRITICAL, 0c75.bdb4.87e0 Configured policy-tag PT1 not defined, picking default-policy-tag.",
        "Aug 14 13:04:17.735: %CAPWAPAC_SMGR_TRACE_MESSAGE-5-AP_JOIN_DISJOIN: Chassis 2 R0/0: wncd: AP Event: AP Name: L11_2005_AP4 Mac: 0c75.bdb4.87e0 Session-IP: 9.2.91.63[5248] 9.2.89.30[5246] Ethernet MAC: 0c75.bdb6.09ec Joined",
        "Aug 14 13:04:18.074: %APMGR_TRACE_MESSAGE-3-WLC_GEN_ERR: Chassis 2 R0/0: wncd: Error in AP: 687d.b460.02a0: country code (IN) and regulatory domain (-B) mismatch for slot 1",
        "Aug 14 13:04:27.057: %APMGR_TRACE_MESSAGE-3-WLC_GEN_ERR: Chassis 2 R0/0: wncd: Error in AP: 00e5.6400.0200: country code (IN) and regulatory domain (-B) mismatch for slot 1",
        "Aug 14 13:04:27.591: %CAPWAPAC_SMGR_TRACE_MESSAGE-5-AP_JOIN_DISJOIN: Chassis 2 R0/0: wncd: AP Event: AP Name: WSIMAP-0002 Mac: 00e5.6400.0200 Session-IP: 9.2.91.145[5272] 9.2.89.30[5246] Ethernet MAC: 00e5.64f0.0002 Joined",
        "Aug 14 13:04:45.331: %CAPWAPAC_SMGR_TRACE_MESSAGE-5-AP_JOIN_DISJOIN: Chassis 2 R0/0: wncd: AP Event: AP Name: L11_2004_AP3 Mac: 687d.b477.5d00 Session-IP: 9.2.91.60[5275] 9.2.89.30[5246] Ethernet MAC: 687d.b402.eb70 Joined",
        "Aug 14 13:05:10.138: %APMGR_TRACE_MESSAGE-3-WLC_GEN_ERR: Chassis 2 R0/0: wncd: Error in AP: 00e5.6400.0100: country code (IN) and regulatory domain (-B) mismatch for slot 1",
        "Aug 14 13:05:10.422: %CAPWAPAC_SMGR_TRACE_MESSAGE-5-AP_JOIN_DISJOIN: Chassis 2 R0/0: wncd: AP Event: AP Name: WSIMAP-0001 Mac: 00e5.6400.0100 Session-IP: 9.2.91.144[5272] 9.2.89.30[5246] Ethernet MAC: 00e5.64f0.0001 Joined",
        "Aug 14 13:06:35.328: %AAA-6-METHOD_LIST_STATE: authen mlist  pvt_authen_0 of DOT1X service is marked for notifyingstate and its current state is : DEAD",
        "Aug 14 13:06:35.328: %AAA-6-METHOD_LIST_STATE: authen mlist  pvt_authen_0 of DOT1X service is marked for notifyingstate and its current state is : DEAD",
        "Aug 14 13:06:35.425: %AAA-6-METHOD_LIST_STATE: authen mlist  pvt_authen_0 of DOT1X service is marked for notifyingstate and its current state is : DEAD",
        "Aug 14 13:06:35.425: %AAA-6-METHOD_LIST_STATE: authen mlist  pvt_authen_0 of DOT1X service is marked for notifyingstate and its current state is : DEAD",
        "Aug 14 13:06:35.529: %AAA-6-METHOD_LIST_STATE: authen mlist  pvt_authen_0 of DOT1X service is marked for notifyingstate and its current state is : DEAD",
        "Aug 14 13:06:35.529: %AAA-6-METHOD_LIST_STATE: authen mlist  pvt_authen_0 of DOT1X service is marked for notifyingstate and its current state is : DEAD",
        "Aug 14 13:06:35.703: %AAA-6-METHOD_LIST_STATE: authen mlist  pvt_authen_0 of DOT1X service is marked for notifyingstate and its current state is : DEAD",
        "Aug 14 13:06:35.703: %AAA-6-METHOD_LIST_STATE: authen mlist  pvt_authen_0 of DOT1X service is marked for notifyingstate and its current state is : DEAD",
        "Aug 14 13:06:35.351: %AAA_AUDIT_MESSAGE-6-METHOD_LIST_STATE: Chassis 2 R0/0: wncd: mlist default of 8021X service is marked for notifying  state and its current state is : ALIVE",
        "Aug 14 13:06:35.351: %AAA_AUDIT_MESSAGE-6-METHOD_LIST_STATE: Chassis 2 R0/0: sessmgrd: mlist default of 8021X service is marked for notifying  state and its current state is : ALIVE",
        "Aug 14 13:06:35.807: %AAA-6-METHOD_LIST_STATE: authen mlist  pvt_authen_0 of DOT1X service is marked for notifyingstate and its current state is : DEAD",
        "Aug 14 13:06:35.807: %AAA-6-METHOD_LIST_STATE: authen mlist  pvt_authen_0 of DOT1X service is marked for notifyingstate and its current state is : DEAD",
        "Aug 14 13:06:36.623: %AAA-6-METHOD_LIST_STATE: authen mlist  pvt_authen_0 of DOT1X service is marked for notifyingstate and its current state is : DEAD",
        "Aug 14 13:06:36.623: %AAA-6-METHOD_LIST_STATE: authen mlist  pvt_authen_0 of DOT1X service is marked for notifyingstate and its current state is : DEAD",
        "Aug 14 13:06:36.732: %AAA-6-METHOD_LIST_STATE: authen mlist  pvt_authen_0 of DOT1X service is marked for notifyingstate and its current state is : DEAD",
        "Aug 14 13:06:36.732: %AAA-6-METHOD_LIST_STATE: authen mlist  pvt_authen_0 of DOT1X service is marked for notifyingstate and its current state is : DEAD",
        "Aug 14 13:06:38.852: %AAA-6-METHOD_LIST_STATE: authen mlist  pvt_authen_0 of DOT1X service is marked for notifyingstate and its current state is : DEAD",
        "Aug 14 13:06:38.852: %AAA-6-METHOD_LIST_STATE: authen mlist  pvt_authen_0 of DOT1X service is marked for notifyingstate and its current state is : DEAD",
        "Aug 14 13:06:39.105: %AAA-6-METHOD_LIST_STATE: authen mlist  pvt_authen_0 of DOT1X service is marked for notifyingstate and its current state is : DEAD",
        "Aug 14 13:06:39.106: %AAA-6-METHOD_LIST_STATE: authen mlist  pvt_authen_0 of DOT1X service is marked for notifyingstate and its current state is : DEAD",
        "Aug 14 13:06:40.399: %SYS-5-CONFIG_I: Configured from console by giri on console"
    ]
}