* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------

* JUNOS
    * ShowRouteTable
        * Added aditional testcase
    * Added ShowRouteAdvertisingProtocolDetail
        * show route advertising-protocol {protocol} {ip_address} {route} detail

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------

* IOSXE
    * Updated ShowIsisDatabaseDetail for code issue:
        * show isis database detail
* NXOS 
    * Updated ShowMacAddressTableBase:
        * Modified the regex patterns to support various outputs.
    * Updated ShowIpArpDetailVrfAll:
        * Modified the regex patterns to support various outputs.
* IOSXR
    * Updated ShowVrfAllDetail:
        * Modified the regex patterns to support various outputs.
* JUNOS
    * Upated ShowRoute
        * Modified cli method to accept only ip_address as input
    * Updated ShowRouteTable
        * Modified cli method to take an additional parameter
    * Updated ShowRouteAdvertisingProtocol
        * Added {route} parameter option
    * Added MonitorInterfaceTraffic for:
        * monitor interface traffic
