--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowInventory:
        * Add regex p1_8 to accept additional NAMES for 'show inventory' command
        * Update logic to include missing NAMES if they exists
        * Add folder based unittests
        