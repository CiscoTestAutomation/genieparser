--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXR
    * Modified ShowBgpAddressFamily:
        * New Show Command - show bgp {address_family} community {community}
        * New Show Command - show bgp {address_family} community {community} {exact_match}
        * Updated regex for handling IPv6 adresses/prefixes  
        * Updated regex pattern for handling new lines in IPv6 address family output
