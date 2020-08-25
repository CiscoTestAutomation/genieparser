| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |    20.8       |

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
    * Added ShowLdpSessionIpaddressDetail
        * Show Ldp Session Ipaddress Detail

* IOSXE
    * Added ShowApphostingList
        * show app-hosting list
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
    * Added showSdwanRebootHistory
        * show sdwan reboot history
    * Added ShowSdwanSystemStatus
        * show sdwan system status
    * Added ShowSdwanVersion
        * show sdwan version
    * Added ShowPlatformHardwareQfpActiveDatapathUtilSum
        * show platform hardware qfp active datapath utilization summarys
    * Added ShowSdwanOmpSummary:
        * show sdwan omp summary
    * Added ShowSdwanIpsecInboundConnections for:
        * show sdwan ipsec inbound-connections
    * Added ShowSdwanIpsecOutboundConnections for:
        * show sdwan ipsec outbound-connections
    * Added ShowSdwanIpsecLocalsa for:
        * show sdwan ipsec local-sa {WORD}
    * Added ShowSslProxyStatisticsSchema
        * show sslproxy statistics
    * Added ShowTcpproxyStatusSchema For:
        * show tcpproxy status
    * Added ShowTcpProxyStatisticsSchema For:
        * show tcpproxy statistics

* IOSXR
    * Added ShowIgmpGroupsSummary:
        * show igmp groups summary
        * show igmp vrf {vrf} groups summary
* NXOS
    * Added ShowProcessesCpu:
        * show processes cpu
        * show processes cpu | include {include}
    * Added ShowProcessesMemory:
        * show processes memory
        * show processes memory | include {include}
    * Added ShowCores
        * show cores

* VIPTELA
    * Added ShowRebootHistory
        * show reboot history
    * Added ShowSystemStatus
        * show system status
    * Added ShowVersion
        * show version
    * Added ShowOmpSummary:
        * show omp summary
    * Added ShowSoftwareTab
        * show software | tab

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------

* JUNOS
	* Modified ShowArpSchema
	* Modified ShowArpNoResolveSchema
	* Modified ShowBFDSessionSchema
	* Modified ShowBgpGroupBriefSchema
	* Modified ShowBgpSummarySchema
	* Modified ShowBgpNeighborSchema
	* Modified ShowChassisFpcDetailSchema
	* Modified ShowChassisHardwareSchema
	* Modified ShowChassisHardwareDetailSchema
    * Modified ShowChassisHardwareExtensiveSchema
    * Modified ShowChassisFpcSchema
	* Modified ShowConfigurationProtocolsMplsPathSchema
	* Modified ShowFirewallSchema
	* Modified ShowInterfacesDescriptionsSchema
	* Modified ShowInterfacesSchema
	* Modified ShowInterfacesStatisticsSchema
	* Modified ShowInterfacesPolicersInterfaceSchema
	* Modified ShowInterfacesQueueSchema
	* Modified ShowIpv6NeighborsSchema
	* Modified ShowKrtStateSchema
	* Modified ShowLacpInterfacesInterfaceSchema
	* Modified ShowLDPSessionSchema
	* Modified ShowLdpNeighborSchema
	* Modified ShowLdpDatabaseSessionIpaddressSchema
	* Modified ShowMPLSLSPNameDetailSchema
	* Modified ShowOspfInterfaceBriefSchema
	* Modified ShowOspfDatabaseSchema
	* Modified ShowOspfDatabaseSummarySchema
	* Modified ShowOspfDatabaseExternalExtensiveSchema
	* Modified ShowOspfDatabaseAdvertisingRouterSelfDetailSchema
	* Modified ShowOspfDatabaseExtensiveSchema
	* Modified ShowOspfNeighborExtensiveSchema
	* Modified ShowOspfInterfaceExtensiveSchema
	* Modified ShowOspfRouteBriefSchema
	* Modified ShowOspfDatabaseNetworkLsaidDetailSchema
	* Modified ShowOspfRouteNetworkExtensiveSchema
	* Modified ShowOspfDatabaseOpaqueAreaSchema
	* Modified ShowOspf3InterfaceBriefSchema
	* Modified ShowOspf3DatabaseSchema
	* Modified ShowOspf3DatabaseSummarySchema
	* Modified ShowOspf3DatabaseExternalExtensiveSchema
	* Modified ShowOspf3DatabaseAdvertisingRouterSelfDetailSchema
	* Modified ShowOspf3DatabaseExtensiveSchema
	* Modified ShowOspf3NeighborExtensiveSchema
	* Modified ShowOspf3InterfaceExtensiveSchema
	* Modified ShowOspf3RouteBriefSchema
	* Modified ShowOspf3DatabaseNetworkLsaidDetailSchema
	* Modified ShowOspf3RouteNetworkExtensiveSchema
	* Modified ShowOspf3DatabaseOpaqueAreaSchema
	* Modified ShowPfeRouteSummarySchema
	* Modified ShowVersionSchema
	* Modified FileListDetailSchema
	* Modified ShowRouteTableSchema
	* Modified ShowRouteProtocolExtensiveSchema
	* Modified ShowRouteForwardingTableSummarySchema
	* Modified ShowRouteReceiveProtocolSchema
	* Modified ShowRouteAdvertisingProtocolSchema
	* Modified ShowRouteSummarySchema
	* Modified ShowRouteInstanceDetailSchema
	* Modified ShowRouteAdvertisingProtocolDetailSchema
	* Modified ShowRouteForwardingTableLabelSchema
	* Modified ShowRSVPNeighborSchema
	* Modified ShowRSVPNeighborDetailSchema
	* Modified ShowRSVPSessionSchema
	* Modified ShowSnmpMibWalkSystemSchema
	* Modified ShowSystemUsersSchema
	* Modified ShowSystemCommitSchema
	* Modified ShowSystemQueuesSchema
	* Modified ShowSystemStorageSchema
	* Modified ShowSystemCoreDumpsSchema
	* Modified ShowSystemUptimeSchema
	* Modified ShowTedDatabaseExtensiveSchema
	* Modified ShowVersionDetailSchema
	* Modified ShowVersionInvokeOnAllRoutingEnginesSchema
	* Modified TracerouteNoResolveSchema
	* Modified ShowRouteTableLabelSwitchedNameSchema
		* Fixed SchemaTypeError exception
    * Modified ShowRouteAdvertisingProtocolDetail:
    	* Changed 'local-preference' and 'communities' to Optional.
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
    * Modified ShowRoute:
        * Updated regex pattern p4 to accommodate various outputs.
    * Updated ShowBgpNeighbor:
        * Added key (is-bgp-running) to handle output as BGP is not running
    * Modified ShowBgpNeighborSchema:
      * Changed the follow to Optional:
        * 'bgp-options2'
        * 'bgp-options-extended'
        * 'gshut-recv-local-preference'
        * 'peer-cfg-rti'
        * 'peer-fwd-rti'
        * 'peer-group'
    * Updated ShowRouteAdvertisingProtocolDetail
        * Added more regex patterns to support various outputs
    * Updated ShowRouteAdvertisingProtocolDetailSchema
        * med optional now
    * Modified ShowRouteProtocolExtensive:
        * Added key "metric2" into the schema.
    * Fixed ShowLDPOverviewSchema
        * Made several keys optional
    * Fixed ShowRouteTable
        * Fixed regex pattern for r3
    * Modified ShowSystemUptime:
        * Updated regex pattern p6 to accommodate various outputs.

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
    * Modified ShowSdwanIpsecLocal:
        * Fixed SyntaxWarning
    * Fixed ShowBgpAllNeighborsPolicy:
        * Updated Regex to support more various ouput
    * Fixed review comments for ShowTcpproxyStatusSchema:
        * show tcpproxy status
    * Fixed review comments for ShowTcpProxyStatisticsSchema:
        * show tcpproxy statistics
    * Updated ShowTcpProxyStatisticsSchema with new keys(
        syncache_not_added_flow_entry_null,syncache_not_added_flow_invalid,syncache_not_added_flow_is_in_use,
        total_flow_entries_pending_cleanup_0,total_flow_entries_pending_cleanup,syncache_flow_mismatch) and 
        old keys(syncache_not_added_nat_entry_null, syncache_not_added_mrkd_for_cleanup,
            failed_conn_already_accepted_conn) to optional:
        * show tcpproxy statistics
    * Updated key 'ca_cert_bundle' into Optional in schema ShowSslproxyStatusSchema:
        * show sslproxy status

* IOSXR
    * Updated ShowOspfVrfAllInclusiveDatabaseOpaqueArea:
        * Enhanced parser
    * Updated ShowIsisSpfLogDetail:
        * Added more regex patterns to support various outputs
    * Updated ShowIsisInterface:
        * Modified to support default as instance name
    * Updated ShowInterfaces:
        * Added more regex patterns to support various outputs.
    * Modified ShowLldpEntry:
        * Added key peer_mac to schema
        * Changed system_name, system_description, neighbor_id, and capabilities to Optional

* NXOS
    * Fixed ShowInterfaceBrief:
        * Updated Regex to support more various ouput
    * Modified ShowLldpTraffic:
        * Added optional key 'total_flap_count'