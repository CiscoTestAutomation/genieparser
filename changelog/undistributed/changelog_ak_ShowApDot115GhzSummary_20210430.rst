--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowApDot115GhzSummary:
        * Update schema to accept optional mode field
		* Update logic to include mode field when it exist in the cli output
		* Update regex p1 to include tx_pwr field with or without star
        * Add folder based unittests