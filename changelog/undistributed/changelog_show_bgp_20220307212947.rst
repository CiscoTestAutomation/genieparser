--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowBgpNeighbor:
        * Updated parsing to support VRF in bgp neighbors cli command instead of always setting 'default' VRF (parser p2_3)
        * Added another files for unit testing (show ip bgp neighbors all, show bgp neighbors all)