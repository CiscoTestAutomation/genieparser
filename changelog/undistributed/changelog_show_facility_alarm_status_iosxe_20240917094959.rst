--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowFacilityAlarmStatusSchema:
        * Update schema to include optional 'syslog_string'.
    * Modified ShowFacilityAlarmStatus:
        * Update 'show facility-alarm status', add two new patterns to match table format including "Syslog String".
