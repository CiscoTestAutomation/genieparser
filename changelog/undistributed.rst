* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* JUNOS
    * Added ShowBgpNeighbor for:
        * show bgp neighbor
    * Added ShowLDPOverview
        * show ldp overview
    * Added ShowOspfDatabaseAdvertisingRouterExtensive for:
        * show ospf database advertising-router {ipaddress} extensive
* IOSXE
    * Added ShowRunInterface for:
        * show running-config interface {interface}
    * Added ShowInterfaceTransceiverDetail for:
        * show interface {interface} transceiver detail
* IOSXR
    * Added ShowIgmpGroupsSummary
        * show igmp groups summary
        * show igmp vrf {vrf} groups summary
--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* JUNOS
    * Fixed ShowBgpNeighbor:
        * Updated few keys into Optional.
    * Fixed ShowOspfDatabaseExtensive:
        * Adjusted code to not capture Null values.
    * Fixed ShowClassOfService:
        * Updated regex to support more varied output
    * Fixed ShowRouteAdvertisingProtocol and ShowRouteReceiveProtocol:
        * Changed few keys into Optional, and modified regex to support various outputs. 
    * Fixed ShowInterfaces:
        * Modified regex to support various outputs.
* IOS
    * Fixed ShowNtpConfig:
        * Added prefered key
* IOSXE
    * Fixed ShowNtpConfig:
        * Added prefered key
    * Added ShowSdwanOmpSummary
	* show sdwan omp summary

* VIPTELA
    * Added ShowOmpSummary
        * show omp summary

* IOSXR
    * Updated ShowOspfVrfAllInclusiveDatabaseOpaqueArea
        * Enhanced parser
    * Updated ShowIsisSpfLogDetail:
        * Added more regex patterns to support various outputs.
    * Updated ShowIsisInterface:
        * Modified to support default as instance name
