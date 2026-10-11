--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* iosxr
    * Modified ShowIsis:
        * Changed Instance from schema to Optional
        * Fixed uninitialized variable 'vrf_dict' in r5 when no informations about Instance ar given in Output

    * Modified ShowIsisStatistics:
        * Changed psnp_cache, csnp_cache, lsp, upd, snp, transmit_time, process_time, ispf_calculation, arrival_time_throttled, flooding_duplicates from schema to Optional
        * Updated regex pattern r1, r16, r18, r20, r23, r24, r25, r26, r27, r28 to accommodate various outputs.
