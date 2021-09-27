--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* iosxr
    * Modified ShowControllersOptics:
        * Added Optional key <fec_state> to schema
        * Added regex pattern <p4_1> to accommodate new <fec_state> schema key
        * Updated regex pattern <p3> to accommodate various outputs.
        * Updated regex pattern <p4> to accommodate various outputs.
        * Updated regex pattern <p40> to accommodate various outputs.
