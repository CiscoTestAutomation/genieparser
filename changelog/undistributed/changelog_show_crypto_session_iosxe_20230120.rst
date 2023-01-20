--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* iosxe
    * Modified ShowCryptoSessionSchema:
        * made keys peer, ipsec_flow, ike_sa Optional
        * change interface key to an index instead of non-unique name
        * added 'interface' to dictionary
    * Modified ShowCryptoSessionSchema:
        * adapted code to new number index for interface
        * moved several flag underneath interface match - 
                these flags must be reset when there is a new Interface  