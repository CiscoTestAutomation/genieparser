--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPolicyMapTypeQueueingInterfaceOutput parser
        * show call policy-map type queuing
    * Added ShowPppoeSession
        * for 'show pppoe session'
    * Added ShowPppoeSummary
        * for 'show pppoe summary'
    * Added ShowPlatformHardwareFedActiveTcamUtilization under new directory c9606r
        * show platform hardware fed active fwd-asic resource tcam utilization
    * Added 'ShowCryptoIkev2Proposal' schema and parser
        * show crypto ikev2 proposal
    * Added 'ShowCryptoIkev2Policy' schema and parser
        * show crypto ikev2 policy
    * Added 'ShowCryptoIpsecProfile' schema and parser
        * show crypto ipsec profile
    * Added ShowFlowMonitor parser for 9400 platform
        * Parser for show flow monitor cli
    * Added "flow_monitor_output" field in ShowRunInterface parser
        * To match "ip flow monitor monitor_ipv4_out output" config
    * Added ShowIpBgpMdtVrf parser
        * show ip bgp {address_family} mdt vrf {vrf}
    * Added ShowPlatformHardwareFedActiveQosSchedule parser
        * show platform software fed active qos schedule
    * Added ShowSdwanAppfwdCflowdStatistics
        * for 'show sdwan app-fwd cflowd statistics'
    * Added ShowSdwanAppfwdCflowdFlowCount
        * for 'show sdwan app-fwd cflowd flow-count'
    * Added ShowVrrpDetail
        * for 'show vrrp detail'
    * Added ShowVrrpVpn
        * for 'show vrrp vpn <vpn_ID>'
    * Added ShowLispRemoteLocatorSet
        * 'show lisp remote-locator-set {remote_locator_type}'
        * 'show lisp remote-locator-set name {remote_locator_name}'
        * 'show lisp {lisp_id} remote-locator-set {remote_locator_type}'
        * 'show lisp {lisp_id} remote-locator-set name {remote_locator_name}'
    * Added ShowPlatformHardwareFedActiveVlanIngress parser
        * show platform hardware fed active vlan <num> ingress
    * Added ShowIpArpInspectionVlan parser
        * show ip arp inspection vlan <num>
    * Added ShowControllers
        * for 'show controllers'
    * Added ShowSdwanSdwaAppFwdDpiSummary
        * for 'show sdwan app-fwd dpi summary'
    * Added ShowControlConnectionHistory
        * for 'show sdwan control connection-history'
    * Added ShowCryptoSockets
        * Parser for show crypto sockets
    * Added ShowCryptoMibIpsecFlowmibGlobal
        * Parser for show crypto mib ipsec flowmib global
    * Added ShowCryptoIpsecInternalDual
        * Parser for show crypto ipsec internal dual
    * Added ShowEndpointTrackerRecords
        * for 'show endpoint-tracker records'
    * Added ShowEndpointTrackerStaticRoute
        * for 'show endpoint-tracker static-route'
    * Added ShowEndpointTrackerTrackerGroup
        * for 'show endpoint-tracker tracker-group'
    * Added 'ShowGroupPolicyTrafficSteeringPolicy' schema and parser
        * show group-policy traffic-steering policy sgt
    * Added 'ShowGroupPolicyTrafficSteeringEntries' schema and parser
        * show group-policy traffic-steering entries
    * Added 'ShowGroupPolicyTrafficSteeringCounters' schema and parser
        * show group-policy traffic-steering counters
    * Added 'ShowGroupPolicyTrafficSteeringPermissions' schema and parser
        * show group-policy traffic-steering permissions
    * Added ShowHardwareLed
        * show hardware led
    * Added ShowHardwareLedPort
        * show hardware led port {port}
    * Added ShowIpSlaResponder
        * show ip sla responder
    * Updated ShowIpSlaResponder
        * Added option parameters for show ip sla responder schema
    * Added ShowIpv6DhcpBinding
        * Parser for 'show ipv6 dhcp binding'
    * Added ShowIpv6DhcpStatistics
        * Parser for 'show ipv6 dhcp statistics'
    * ShowIsisDatabase
        * show isis database
        * show isis database verbose
    * Added 'ShowL2tpTunnel' schema and parser
        * show l2tp tunnel
    * Added show_platform_ifm_mapping
        * show platform software fed {switch} {state} ifm mappings
        * show platform software fed active ifm mappings
    * Added 'ShowLldpTrafficInterface' schema and parser
        * show lldp traffic interface {id}
    * Added 'ShowCryptoIkev2StatsExchange' schema and parser
        * show crypto ikev2 stats exchange
    * Added ShowPlatformPktTraceStats
        * show packet-trace statistics
    * Added ShowPlatformPktTraceSummary
        * show platform packet-trace summary
    * Added ShowPlatformPacketTracePacket
        * show platform packet-trace packet all
    * Modified ShowIsisRib
        * Added the "from_srapp" feature to the schema
    * Added ShowIsisNodeLevel
        * show isis node {level}
    * Added ShowStackwiseVirtualDualActiveDetectionPagp
        * show stackwise-virtual dual-active-detection Pagp
    * Added 'ShowMdnsSdCacheInvalid' Parser
        * Parser for show mDNS(Multicasr Domain name services)sd cache invalid
    * Added ShowPppStatistics
        * parser for show ppp statistics
    * Added ShowFipsAuthorizationKey
        * Added 'show fips authorization-key'
    * Below are the new parsers added for Hawkeye feature
        * Added show platform software steering-policy forwarding-manager {switch} R0 permissions ipV4 {sgt} {dgt}
        * Added show platform software steering-policy forwarding-manager switch {switch} F0 policy-summary
        * Added show platform software steering-policy forwarding-manager F0 policy-summary
        * Added show platform software steering-policy forwarding-manager switch {switch} F0 cell-info
        * Added show platform software steering-policy forwarding-manager F0 cell-info
        * Added show platform software steering-policy forwarding-manager switch {switch} F0 service-all
        * Added show platform software steering-policy forwarding-manager F0 service-all
        * Added show platform software steering-policy forwarding-manager switch {switch} r0 service-id {service_id}
        * Added show platform software steering-policy forwarding-manager r0 service-id {service_id}
        * Added show platform software fed {switch} active security-fed sis-redirect firewall all
        * Added show platform software fed active security-fed sis-redirect firewall all
        * Added show platform software fed {switch} active security-fed sis-redirect firewall service-id {service_id} detail
        * Added show platform software fed active security-fed sis-redirect firewall service-id {service_id} detail
        * Added show platform software fed {switch} active security-fed sis-redirect acl all
        * Added show platform software fed active security-fed sis-redirect acl all
    * Added 'ShowCryptoIkev2Sa' schema and parser
        * show crypto ikev2 sa
    * Added ShowCryptoIpsecSaDetail
        * show crypto ipsec sa detail
    * Added ShowCryptoIpsecSa
        * show crypto ipsec sa
    * Added ShowCryptoIpsecSaPeerDetail
        * show crypto ipsec sa peer {} detail
    * Added ShowCryptoIpsecSaPeer
        * show crypto ipsec sa peer {}
    * Added ShowRunningConfigNve
        * show running-config nve
    * Added ShowRunningConfigNve
        * show running-config nve
    * Added ShowIpDhcpBinding parser:
        * show ip dhcp binding
    * Added ShowIpDhcpServerStatistics parser:
        * show ip dhcp server statistics
    * Added ShowFipsStatus
        * Added 'show fips status'


* iosxr
    * Added ShowEvpnEviInclusiveMulticast
        * 'show evpn evi inclusive-multicast'
        * 'show evpn evi vpn-id {vpn_id} inclusive-multicast'
    * Added ShowEvpnEviInclusiveMulticastDetail
        * 'show evpn evi inclusive-multicast detail'
        * 'show evpn evi vpn-id {vpn_id} inclusive-multicast detail'
    * Added showEvpnInternalId
        * 'show evpn internal-id'
        * 'show evpn internal-id vpn-id {vpn-id}'
    * Added showEvpnInternalIdDetail
        * 'show evpn internal-id detail'
        * 'show evpn internal-id vpn-id {vpn-id} detail'
    * Added ShowSegmentRoutingSrv6LocatorSid
        * show segment-routing srv6 sid
        * show segment-routing srv6 locator {locator} sid
    * Added ShowSnmp
        * show snmp
        * show snmp host

* nxos
    * Added "Show fabric multicast ipv4  mroute parser"
        * show fabric Multicast ipv4 vrf all
        * show fabric Multicast ipv4  vrf <vrf_name>

* viptela
    * Added ShowIpRoutes parser
        * show ip routes
        * show ip routes <prefix>
        * show ip routes vpn <vpn>
        * show ip routes vpn <vpn> <prefix>


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowRomvar
        * changed schema key <ps1> to Optional
        * added Optional schema key <abnormal_reset_count>
    * Modified ShowLispEidAway
        * Changed <eid_prefix> from schema to Optional
    * Modified ShowLispInstanceIdService
        * Changed <xtr_id> and <site_id> from schema to Optional
    * Modified ShowIpCefSchema
        * Changed <nexthop> from schema to Optional
    * Modified ShowIsisDatabaseDetail
        * Converted the base parser to a super parser
    * Modified ShowRunningConfigAAAUsername
        * To support more varied output
    * Modified Convert_intf_name
        * Modified Convert_intf_name function to expand Fou - FourHundredGigE.
    * Modified ShowLispServiceStatistics
        * The existing schema does not properly represent the output of the show command So fixed all the schema and updated code accordingly. Note This change is NOT backwards compatible.
    * Modified ShowIpMfib
        * merged the comments addressed / committed in ShowIpv6Mfib  to  ShowIpMfib
    * Modified ShowIpMrib
        * initialization of dictionary variable was moved before first match was executed
    * Modified ShowIsisRib
        * Added the functionality to parse a rib entry where the first line is only a single IP
    * Modified ShowMplsMldpRoot
        * Modified interface field regex to grep all kind of interfaces
    * Modified ShowMplsMldpNeighbors
        * Modified LDP GR regex to grep all kind of states
    * Modified ShowBgp
        * Modified prefix field in p3_1 regex to consider \*
    * Modified ShowSdwanOmpRoutes
        * Return the prefix and VPN to the upstream Viptela class parser.
    * Modified ShowPlatformTcamPbr Parser
        * Modified ShowPlatformTcamPbr schema to use Any() for output specific and also modified cli_command to run on  Standalone and HA setup.
    * Modified ShowPlatformSoftwareFedSwitchActivePuntCpuq
        * Modified ShowPlatformSoftwareFedSwitchActivePuntCpuq cli_command to run on Standalone and HA setup.
    * Modified ShowStackwiseVirtualDualActiveDetection
        * Covered parsing of entire output which was missing in existing Parser
    * Modified 'ShowMdnsSdQueryDb' Parser
        * Added new variables in schmea as optional for the latest release
    * Modified 'ShowMdnsSdSummary' Parser
        * Added new variables in schema as optional for the latest release
    * Modified show_run
        * changed regex pattern <p1_1> to match optional policy-map type queueing
    * Modified ShowVlanId
        * changed schema key <ports> to Optional
        * changed regexp pattern to match optional ports field
    * Modified ShowVrf
        * changed schema key <protocols> to Optional
        * changed regexp pattern to match optional protocol field
    * Modified ShowVersion
        * Added optional key <installation_mode> to schema
    * Modified ShowWirelessClientMacDetail
        * Added missing keys
        * Optionalized keys that aren't consistent
        * current_rate and vlan now record types correctly
    * Modified ShowIpMroute
        * Updated ShowIpMrouteSchema with optional keys <vxlan_version>,<vxlan_vni>,<vxlan_nxthop>
        * Updated regex pattern of outgoing interface list by including another line to accomodate vxlan
    * Modified ShowStackwiseVirtualLink
        * Updated schema to properly support device output. This is not backwards compatible.
    * Modified ShowPlatformSoftwareObjectManagerFpActiveStatistics parser
        * Added "show platform software object-manager switch {switchstate} {serviceprocessor} active statistics" cli
    * Modified ShowInterfaces{interface} parser
        * Added optional keys <tunnel_source_ip>, <tunnel_destnation_ip>, <tunnel_protocol>, <tunnel_ttl>, <tunnel_transport_mtu>, <tunnel_transmit_bandwidth>, <tunnel_receive_bandwidth> into the schema.
    * Modified ShowMacsecInterfaceSchema
        * Changed few values of macsec-data key as optional.
    * Modified ShowRunningConfigAAAUsername
        * To support more varied output
    * Modified ShowWirelessProfilePolicyDetailed
        * Added format for policy_name argument
    * Modified ShowStackwiseVirtualDualActiveDetection:
        * Modified to take the pre-passed output.
    * Modified ShowStackwiseVirtualDualActiveDetectionPagp:
        * Modified to take the pre-passed output & linestip assignment.
    * Modified ShowApDot115GhzChannel:
        * Added Optional keys <zero_wait>, <dca_aggressive>, <wlc_leader_ipv4>, and <wlc_leader_ipv6> to schema
    * Modified ShowInterfaces{interface} parser
        * Modified key name <tunnel_destination_ip> of the schema.
    * Modified ShowTelemetryIETFSubscriptionReceiver
        * Added "name" field to schema to account for named receivers
        * Added regex pattern <p9> for newly added "name" field
        * Updated regex pattern <p7> to accommodate for multi-word entries
    * Modified ShowTelemetryConnectionAll
        * Strip entry under 'VRF' from letter 'M' that might be present in output

* nxos
    * Fixed Show Fabic Multicast ipv4  sa-ad route parser
        * Fixed the regular expression while parsing the output

* asa
    * Modified ShowInterfacesSummary
        * Updated regex pattern p1 to accommodate various outputs.
    * Modified ShowVersion
        * Made certain keys optional
        * Added optional key for SSP Slot Number
    * Modified ShowInventory
        * Updated regex patterns p1 and p2 to accommodate various outputs.
        * Added another file for unit testing

* iosxr
    * Modified ShowLldpEntry
        * Added the "age" feature to the schema
    * Modified ShowLldpTraffic
        * Added the "tlv_accepted" feature to the schema
        * Added the "last_clear" feature to the schema
    * Modified ShowPolicyMapInterface Parser, update pattern p2 input direction
    * Updated showEvpnInternalId
        * Updated p1 pattern to include hex value for esi in 'show evpn internal-id'

* viptela
    * Modified ShowOmpRoutes
        * Added "route_info" variable to correctly populate the parsed_dict dictionary.
        * Added vpn/vrf variable to dynamically populate the correct VPN used.

* cheetah
    * Modified ShowCapwapClientRcb
        * Made "mwar_name" as optional string
    * Modified ShowCapwapClientRcb
        * Made "ap_tcp_mss_size" as optional string
        * Added "flex_group_name" as new key,value pair

* dnac
    * Updated Interface
        * Added additional keys
