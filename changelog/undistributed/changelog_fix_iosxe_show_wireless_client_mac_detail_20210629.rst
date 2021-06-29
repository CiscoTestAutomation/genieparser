--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowWirelessClientMacDetail:
        * added missing argument to cli command
        * added new optional keys
        * made several keys in schema optional
        * current_rate can now be a float or string if the value is the encoding scheme