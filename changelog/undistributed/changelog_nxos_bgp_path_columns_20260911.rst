--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------
* NXOS
    * Modified ShowBgpIpMvpnRouteType and its EVPN/MVPN subclasses:
        * Read Metric, LocPrf, Weight and Path using table header column boundaries.
        * Preserve AS paths when Metric or LocPrf is blank.
        * Made localpref optional when the displayed column is blank.
        * Retained the existing parsing path for outputs without a table header.
        * Added EVPN and MVPN fixtures and regression tests.
