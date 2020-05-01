* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------

* JUNOS
    * Added ShowOspfNeighborDetail for:
        * show ospf neighbor {neighbor} detail
    * Added ShowLogFilename for:
        * show log {filename}
    * Added ShowChassisFpc for:
        * show chassis fpc
    * Added ShowChassisRoutingEngine for:
        * show chassis routing-engine
    * Added ShowChassisRoutingEngineNoForwarding for:
        * show chassis routing-engine no-forwarding
    * Added ShowLacpInterfacesInterface for:
        * show lacp interfaces {interface}

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------

* IOSXE
    * Fixed ShowDmvpn not executing the command properly on device

* NXOS
    * Updated ShowIpStaticRouteMulticast:
        * Change key 'address_family' into Optional

* LINUX
    * Fixed Ifconfig parser issues.

* JUNOS
    * Updated ShowRoute:
        * Update regex to support various outputs.

