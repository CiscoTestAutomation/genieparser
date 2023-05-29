--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowIpOspfInterface:
        * Optimized parser by having it call additional commands once rather than call them for every instance, interface, etc...