--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* JUNOS
    * Added ShowBgpNeighbor:
        * show bgp neighbor
    * Added ShowLDPOverview:
        * show ldp overview
    * Added ShowOspfDatabaseAdvertisingRouterExtensive:
        * show ospf database advertising-router {ipaddress} extensive
    * Added ShowConfigurationProtocolsMplsLabelSwitchedPath:
        * show configuration protocols mpls label-switched-path {path}
    * Added ShowConfigurationProtocolsMplsPath:
        * show configuration protocols mpls path {path}
* IOSXE
    * Added ShowRunInterface:
        * show running-config interface {interface}
    * Added ShowInterfaceTransceiverDetail:
        * show interface {interface} transceiver detail
    * Added ShowPlatformHardwareQfpActiveDatapathUtilSum
        * show platform hardware qfp active datapath utilization summary
    * Added ShowSslproxyStatus:
        * show sslproxy status
    * Added ShowSdwanAppqoeTcpoptStatus:
        * show sdwan appqoe tcpopt status
    * Added ShowSdwanAppqoeNatStatistics:
        * show sdwan appqoe nat-statistics
    * Added ShowSdwanAppqoeRmResources:
        * show sdwan appqoe rm-resources
    * Added ShowSdwanRebootHistory
        * show sdwan reboot history
    * Added ShowSdwanSystemStatus
        * show sdwan system status
    * Added ShowSdwanVersion
        * show sdwan version
* IOSXR
    * Added ShowIgmpGroupsSummary:
        * show igmp groups summary
        * show igmp vrf {vrf} groups summary
* NXOS
    * Added ShowProcessesCpu:
        * show processes cpu
        * show processes cpu | include <include>
    * Added ShowProcessesMemory:
        * show processes memory
        * show processes memory | include <include>
* VIPTELA
    * Added ShowRebootHistory
        * show reboot history
    * Added ShowSystemStatus
        * show system status
    * Added ShowVersion
        * show version
--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* JUNOS
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
    * Updated ShowOspfDatabaseExtensive:
        * Now accounts for netsummary
    * Updated ShowInterfacesExtensive:
        * Included extra output case
    * Fixed ShowRouteProtocolExtensive:
        * Updated few keys into Optional
* IOS
    * Fixed ShowNtpConfig:
        * Added prefered key
* IOSXE
    * Fixed ShowNtpConfig:
        * Added prefered key
    * Added ShowSdwanOmpSummary:
        * show sdwan omp summary

* VIPTELA
    * Added ShowOmpSummary:
        * show omp summary

* IOSXR
    * Updated ShowOspfVrfAllInclusiveDatabaseOpaqueArea:
        * Enhanced parser
    * Updated ShowIsisSpfLogDetail:
        * Added more regex patterns to support various outputs
    * Updated ShowIsisInterface:
        * Modified to support default as instance name
