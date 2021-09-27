--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowIpv6Route:
        * Fixed p6 match logic to allow % in case of leaked route in current vrf table.
    * Modified ShowIpRoute:
        * Fixed p3 match logic for Ipv6 and Ipv6 to properly parse code 1 (in cases such as replicated routes or additional codes). Ipv6 routes now properly parsed as well
