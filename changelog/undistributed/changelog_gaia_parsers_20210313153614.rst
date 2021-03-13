--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* Check Point Gaia
    * New platform added called 'gaia'
        * Note: This name aligns with with netmiko driver name ('gaia') and is similar to the napalm driver ('gaiaos')
    * Included parsers:
        * show interface
        * show users
        * user ntp
        * show arp
        * show version
    * Parsers are for clish commands only. Expert mode commands are not currently supported.
    * All parsers include tests, and all module tests passing.