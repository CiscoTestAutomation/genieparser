--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXR
    * Modified ShowBgpInstancesSchema:
        * Switched key from int to Or(int, str)
    * Modified ShowBgpInstances
        Fixed regex
        Allowed pattern to try int, on failing that default to str
    * Modified ShowBgpInstanceSummarySchema:
        * Switched keys from int to Or(int, str)
    * Modified ShowBgpInstanceSummary:
        Fixed regex
        Allowed pattern to try int, on failing that default to str