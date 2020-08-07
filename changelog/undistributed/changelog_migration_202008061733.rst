--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* JUNOS
    * Added ShowTedDatabaseIpAddress
        * show ted database {ipaddress}
    * Created ShowMPLSLSPNameDetail
        * show mpls lsp name {name} detail
    * Created ShowMPLSLSPNameExtensive
        * show mpls lsp name {name} extensive
    * Show Ospf3 Route Network Extensive
        * Created ShowOspf3RouteNetworkExtensive
    * Added ShowBFDSesssion
        * show bfd session
    * Added ShowBFDSesssionDetail
        * show bfd session {ipaddress} detail
    * Added ShowLDPSession
        * show ldp session
    * Added ShowClassOfService
        * show class-of-service interface {interface}
    * Added ShowRouteForwardingTableLabel
        * show route forwarding-table label {label}
    * Added ShowRSVPSession
        * show rsvp session
    * Added ShowRSVPNeighbor
        * show rsvp neighbor
    * Added ShowLdpDatabaseSessionIpaddress
        * show ldp database session ipaddress
    * Added ShowLdpNeighbor
        * show ldp neighbor
    * Added ShowRSVPNeighborDetail
        * show rsvp neighbor detail
    * Added ShowOspfDatabaseOpaqueArea
        * show ospf database opaque-area
    * Added ShowLDPInterface
        * show ldp interface {interface}
    * Added ShowLDPInterfaceDetail
        * show ldp interface {interface} detail
    * Added PingMplsRsvp
        * ping mpls rsvp {rspv}
    * Added TracerouteNoResolve
        * traceroute {ipaddress} no-resolve
    * Added Ping
        * ping {addr} ttl {ttl} count {count} wait {wait}
* IOSXE
    * Added ShowPlatformHardwareQfpActiveFeatureAppqoe
        * show platform hardware qfp active feature appqoe stats all
    * Added ShowSdwanSoftware
        * show sdwan software
    * Added ShowBgpNeighbor for:
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

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* JUNOS
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

    * Updated ShowCdpNeighbors
        * Modified regex to support different output
    * Updated ShowCdpNeighborsDetail
        * Modified regex to support different output
    * Updated ShowIpInterface
        * Enhanced parser and added optional values
    * Updated ShowSegmentRoutingTrafficEngPolicy
        * Enhanced the schema to support updated outputs
    * Updated ShowPlatformIntegrity
        * to pretty print the rpc reply for netconf
    * Updated ShowVersion
        * Enhanced parser
    * Updated ShowProcessesMemory
        * Modified schema to support different output
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
    * Updated ShowInterfaces:
        * Added more regex patterns to support various outputs.
* VIPTELA
    * Added ShowSoftwareTab
        * show software | tab
