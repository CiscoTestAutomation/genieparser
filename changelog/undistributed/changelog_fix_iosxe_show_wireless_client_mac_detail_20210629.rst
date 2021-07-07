--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowWirelessClientMacDetail:
        * rewrote parser for better stability
        * added missing argument to cli command
        * added new optional keys, made several keys in schema optional
        * some schema entries are now int or string
        * added new test to cover schema changes