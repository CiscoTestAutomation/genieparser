--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowBgpDetailSuperParser:
        * modified p10 to cover scenario where EVPN ESI is in output, but not paired with gateway address or local_vtep information
        * added test (golden_output10) to cover scenario and modified golden_output1 that reflects new field in output