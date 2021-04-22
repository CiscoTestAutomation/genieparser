--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowInterfaces:
        * Update schema to include optional line protocol err-disabled state if it exists 
            for 'show interfaces' and 'show interfaces {interface} commands'
        * Update condition to display line protocol err-disabled state if it exists
        * Update 3 of the existing golden_output2_expected to accomodate schema changes
        * Add folder based unittests