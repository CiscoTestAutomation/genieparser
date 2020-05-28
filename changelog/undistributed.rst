* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------

* JUNOS
    * Added ShowRouteAdvertisingProtocolDetail
        * show route advertising-protocol {protocol} {ip_address} {route} detail

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------

* IOSXE
    * Updated ShowIsisDatabaseDetail for code issue:
        * show isis database detail
* JUNOS
    * Updated ShowRouteAdvertisingProtocol
        * Added {route} parameter option
* IOS 
    * Updated ShowIpArp
        * Added argument 'output' into super().cli()
    * Updated ShowMacAddressTableBase:
        * Modified the regex patterns to support various outputs.
    * Updated ShowIpArpDetailVrfAll:
        * Modified the regex patterns to support various outputs.
* IOSXR
    * Updated ShowVrfAllDetail:
        * Modified the regex patterns to support various outputs.