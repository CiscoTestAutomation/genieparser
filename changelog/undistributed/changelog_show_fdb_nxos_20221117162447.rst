--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* NX-OS
    * Modified ShowMacAddressTableBase in show_fdb.py:
        * Updated regex patterns: p1 to accommodate output from new device as used in test files
        * Added new test files for nxos, ShowMacAddressTable: golden_output_4_*
