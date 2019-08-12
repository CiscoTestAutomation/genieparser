* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                Interface
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowInterfaces for:
        'show interfaces'
        'show interfaces {interface}'

* IOSXE
    * Fix ShowRedundancyStates
        changed 'maintenance_mode' key to optional to support more output

--------------------------------------------------------------------------------
                                Lag
--------------------------------------------------------------------------------
* IOSXE
    * Fix ShowPagpNeighbor
        added 'show pagp neighbor' key to cli command for Ops
* IOSXR
    * Update ShowBundle
        to support 'show bundle {interface}'

--------------------------------------------------------------------------------
                                traceroute
--------------------------------------------------------------------------------
* IOSXE
    * Update TraceRoute
        schema changed for multi paths support

--------------------------------------------------------------------------------
                                Cdp
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowCdpNeighborsDetail
        * Fixed regEx to avoid omitting after '/' in the 'port_id'

--------------------------------------------------------------------------------
                                Platform
--------------------------------------------------------------------------------
* NXOS
    * Fix ShowVersion
        updated schema and regEx to support more outputs
* IOSXE
    * Update ShowPlatform
        to parse 'lc_type' more clearly and flexibly based on updated schema

--------------------------------------------------------------------------------
                                Lldp
--------------------------------------------------------------------------------
* IOSXR
    * Update ShowLldpEntry
        added a key 'show lldp entry' for Ops

--------------------------------------------------------------------------------
                                Routing
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpRouteWord
        * Added parsing ability for: 'SR Incoming Label', 'MPLS label', 'MPLS Flags', 'Repair Path'