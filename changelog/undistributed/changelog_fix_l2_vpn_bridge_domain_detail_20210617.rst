--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXR
    * Modified ShowL2vpnBridgeDomainDetail:
       * Fixed variable referenced before assignment error
       * Added support for outputs where MPLS data wants to be inside the LSP dict
       * Added support for more keys in the schema to match sample output