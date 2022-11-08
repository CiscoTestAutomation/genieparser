--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOS
    * Modified ShowPlatform for platform cat6k:
        * Changed some keys to Optional
            cpu->[implementation, rev, l2_cache]
            memory->[packet_buffer, flash_internal_SIMM]
            last->reload_reason
        * Updated regex patterns: p11, p14, p31_1 to accommodate output from new device as used in test files
        * Added regex patterns: p13_1, p13_2 to accommodate output from new device as used in test files
        * Added new test files: golden_output_c7600_1_*

