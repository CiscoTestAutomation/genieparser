--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* Check Point Gaia OS
    * New platform added called 'gaia'
        * Note: This name aligns with with netmiko driver name ('gaia') and is similar to the napalm driver ('gaiaos')
    * Included parsers:
        * show interface
        * show users
        * show ntp
        * show arp
        * show version
    * Parsers are for clish commands only. Expert mode commands are not currently supported.
    * Tested under Check Point Gaia R80.40
    * All parsers include tests, and all module tests passing.
    