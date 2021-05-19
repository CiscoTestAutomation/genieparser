--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXR
    * Modified ShowL2vpnBridgeDomainBrief:
        * Class now parses its own output instead of calling and returning another class' output verbatim.
        * This is helpful because the Brief version of the command outputs in a different format.

    * Added ShowL2vpnBridgeDomainSchema:
        * Schema needed to support modifications to ShowL2vpnBridgeDomainBrief
