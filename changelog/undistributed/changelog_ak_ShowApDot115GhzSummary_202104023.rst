--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowApDot115GhzSummary:
        * Update regex ap_info_capture - to accept additional states  Mode for 'show ap dot11 5ghz summary' command
        * Add Optional("mode") to schema
        * Update logic to include mode if it exists
        * Add folder based unittests