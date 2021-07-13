--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* <OS>
    * Modified ShowBgpSummarySuperParser:
        * used if .get() to prevent error on missing 'vrf' key
        * added test to cover change
