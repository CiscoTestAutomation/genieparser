--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowStandbyAll
        * Refactor parser so that it commits data to standby_all_dict after parsing all lines
        * Fix group name regex so that it works with subinterfaces

