--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* NXOS
    * Modified ShowRunningConfigVrf:
        * Updated regex pattern <p5> to include : match for route-target
        * Updated so 'both' is used when route-target is imported and exported. (Already done the same way for IOS XE 'show vrf detail')