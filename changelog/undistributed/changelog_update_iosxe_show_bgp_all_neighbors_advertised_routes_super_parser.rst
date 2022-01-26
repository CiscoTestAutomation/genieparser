--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE
    * modified showbgpneighborsadvertisedroutessuperparser
        * added try/catch for unconditional command execution "show bgp all neighbors | i BGP neighbor"
