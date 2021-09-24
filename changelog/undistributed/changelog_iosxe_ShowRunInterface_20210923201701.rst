--------------------------------------------------------------------------------
                            New
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowRunInterface:
        * Added parsing support (schema and parsers) for following output
            * spanning-tree portfast trunk

--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowRunInterface:
        * Removed duplicate schema variables
                * Optional('spanning_tree_bpduguard'): str,
                * Optional('spanning_tree_portfast'): bool,