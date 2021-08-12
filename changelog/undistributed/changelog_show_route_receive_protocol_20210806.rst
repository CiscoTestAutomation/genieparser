--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* JUNOS
    * Modified ShowRouteReceiveProtocol:
        * Correctly match IPv6 output on multiple lines.
        * Correctly match IPv6 routes and next-hops with a-f characters
        * Correctly match the presence or absence of either med or local-pref in output
