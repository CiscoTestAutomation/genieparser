--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowBgpNeighborsAdvertisedRoutesSuperParser
        * Added try/catch for unconditional command execution `show bgp all neighbors | i BGP neighbor`
