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
    * Added ShowConfigurationProtocolsMplsLabelSwitchedPath
        * show configuration protocols mpls label-switched-path {path}
    * Added ShowConfigurationProtocolsMplsPath
        * show configuration protocols mpls path {path}
* IOSXE
    * Added ShowRunInterface for:
        * show running-config interface {interface}
    * Added ShowInterfaceTransceiverDetail for:
        * show interface {interface} transceiver detail
    * Added ShowSslproxyStatus for:
        * show sslproxy status
* IOSXR
    * Added ShowIgmpGroupsSummary
        * show igmp groups summary
        * show igmp vrf {vrf} groups summary
* NXOS
    * Added ShowProcessesCpu
        * show processes cpu
        * show processes cpu | include <include>
    * Added ShowProcessesMemory
        * show processes memory
        * show processes memory | include <include>
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
        * Missing key added
    * Updated ShowOspf3Overview
        * Missing key added
    * Updated ShowSystemUptime
        * Fixed optional key error, improved regex, and fixed return results
    * Updated ShowRouteForwardingTableLabel
        * Fixed regex matching issue
        
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
    * Updated ShowOspfDatabaseExtensive
        * Now accounts for netsummary
    * Updated ShowInterfacesExtensive
        * Included extra output case
    * Fixed ShowRouteProtocolExtensive:
        * Updated few keys into Optional.
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
