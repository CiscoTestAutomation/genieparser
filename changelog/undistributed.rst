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
<<<<<<< HEAD
    * Updated ShowOspfDatabaseAdvertisingRouterSelfDetail
        * Added more keys to the schema, in order to support output of ShowOspfDatabaseLsaidDetail
    * Updated ShowSystemUsers
        * Regex issues resolved
    * Updated ShowOspfOverview
        * Optional key issue resolved
    * Updated ShowInterfaceExtensive
        * No longer breaks on use and previously unused data is now used
    * Updated ShowOspfDatabaseExtensiveSchema
        * Optional key issue resolved
    * Updated ShowOspf3DatabaseExtensiveSchema
        * Optional key issue resolved
    * Updated ShowOspfVrfAllInclusive
        * key error resolved
    * Updated ShowOspfDatabaseLsaidDetail
        * Resolved issue where empty output would cause error
    * Updated ShowOspf3DatabaseExtensive
        * Missing key issue resolved
    * Updated ShowOspf3Database
        * List ospf-area
    * Updated ShowOspfDatabaseExtensiveSchema
        * Modified ShowOspfDatabaseExtensiveSchema to have optional keys
        * Missing key added
    * Updated ShowOspf3Overview
        * Missing key added
    * Updated ShowSystemUptime
        * Fixed optional key error, improved regex, and fixed return results
    * Updated ShowInterfaces
        * Optional key issue resolved
        * Regex modified to support more output
        * 'show interfaces extensive {interface}' changed to 'show interfaces {interface} extensive'
    * Updated ShowOspfDatabaseExtensive
        * Now accounts for netsummary
=======
    * Fixed ShowBgpNeighbor:
        * Updated few keys into Optional.
        * Updated regex to support various outputs.
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
>>>>>>> dev
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
