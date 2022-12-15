--------------------------------------------------------------------------------
                            New
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowInterfacesCapabilities:
        * show interfaces {interface} capabilities
--------------------------------------------------------------------------------
                            New
--------------------------------------------------------------------------------
* IOS
    * Added ShowInterfacesCapabilities:
        * show interfaces {interface} capabilities

--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowSwitchStackPortsSummary:
        * Modified neighbor from support int OR str in order to support ports like 1 or 1/2
        * Updated regex patterns

--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowRunInterface:
        * Added parser for speed
        * Added parser for duplex
