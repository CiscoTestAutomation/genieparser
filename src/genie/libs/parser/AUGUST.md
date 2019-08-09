| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 19.7.1b       |

--------------------------------------------------------------------------------
                                Interface
--------------------------------------------------------------------------------
* IOSXE
    * Fix ShowRedundancyStates
        changed 'maintenance_mode' key to optional to support more output

--------------------------------------------------------------------------------
                                Lag
--------------------------------------------------------------------------------
* IOSXR
    * Update ShowBundle
        to support 'show bundle {interface}'

--------------------------------------------------------------------------------
                                traceroute
--------------------------------------------------------------------------------
* IOSXE
    * Update TraceRoute
        schema changed for multi paths support

-----------------------------------------------------------------------------
                                Cdp
-----------------------------------------------------------------------------
* NXOS
    * Updated ShowCdpNeighborsDetail
        * Fixed regEx to avoid omitting after '/' in the 'port_id'
