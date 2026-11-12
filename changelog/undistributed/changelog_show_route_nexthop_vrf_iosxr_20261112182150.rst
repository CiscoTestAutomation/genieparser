--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXR
    * Modified ShowRouteIpv4:
        * Updated regex patterns p2 and p3 to accept next-hop VRF names with characters other than letters, digits and underscores, such as hyphens and dots.
    * Modified ShowRouteIpv6:
        * Updated regex pattern p3 to accept next-hop VRF names with hyphens and dots.
