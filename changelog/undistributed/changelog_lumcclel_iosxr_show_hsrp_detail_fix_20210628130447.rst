--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXR
    * Modified ShowHsrpDetail:
        * Updated regex pattern <p1> to accommodate various outputs.
        * Moved regexes outside of loop
    * Modified ShowHsrpSummary:
        * Moved regexes outside of loop