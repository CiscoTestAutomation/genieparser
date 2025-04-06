--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* <IOSXE>
    * Modified ShowObjectGroupName:
        * Updated regex pattern p3 to accomodate ipv4 as well as ipv6 addresses.
        * Added regex pattern p4 to accomodate ipv4 network addresses.
        * Added regex pattern p5 to accomodate ipv4 address ranges.
        * Addedd network_address and range to the schema as Optional.