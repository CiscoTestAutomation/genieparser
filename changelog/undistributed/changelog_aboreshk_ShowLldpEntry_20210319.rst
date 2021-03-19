--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXR
    * Modified ShowLldpEntry:
        * Update regex p2 to handle spaces in chassis_id for 'show lldp neighbors detail' command.
        * Add folder based unittests.

* NXOS
    * Modified ShowLldpNeighborsDetail:
        * Update regex p5 and p6 to handle spaces in system_name and system_description for 'show lldp neighbors detail' command.
        * Converted unittestss to new folder based unittests and add new unittests.
