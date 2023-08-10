--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowPlatformSoftwareFedMatmMactableVlan
        * Moved the parser under c9300 folder due to verify_matm_mactable API failure
    * Modified ShowPlatformSoftwareFedQosInterfaceSuperParser
        * modified meter_type regular expression and unit test added
    * Modified ShowHardwareLed
        * Added stack and switch_num options
    * Modified ShowLispEthernetDatabase
        * Added support for parsing IPv6 RLOC addresses
    * Modified ShowStackPowerLoadShedding
        * Fixed parser by adding line.strip()
    * Modified ShowLispDynamicEidDetail
        * Added support for parsing IPv6 map server, map-nofify group and EID addresses
    * Modified ShowLispServiceServerDetailInternal
        * Added support for SGT
    * Modified ShowLispServiceSmr
        * Added support for parsing IPv6 EID addresses
    * Modified ShowLispEthernetMapCachePrefix
        * Added support for parsing IPv6 RLOC addresses
    * Modified ShowLispDatabaseConfigPropSuperParser
        * Added support for parsing IPv6 RLOC addresses
    * Modified ShowLine
        * Added `line` key to the schema
        * Update regex pattern to support output with and witout line
        * Added logic to handle output that has tty line names cut short
    * Modified ShowInventory
        * Enhanced the parser to get the details of interface type 'FiftyGigE' in the output
    * Enhanced ShowDeviceTrackingDatabaseDetails
        * Updated an optional key 'incomplete' in schema
        * Enhanced regexp to match 'time_left' with form "34 s try 0(6741 s)"
    * Modified ShowLispSessionSuperParser
        * Added support for parsing IPv6 session addresses
    * Modified ShowIpArpInspectionLog
        * Made 'interfaces' key as Optional and added unit test.
    * Modified ShowPlatformSoftwareFedQosInterfaceSuperParser
        * Couple of Bind Information parameters are kept as optional and unit test added
    * Modified ShowRunningConfigNve
        * Updated regex pattern <p4_8> to include MVPN address families
    * Updated ShowVtemplate parser
        * Updated parser for "show vtemplate"
    * Modified ShowLispSessionCapability
        * Added support for parsing IPv6 peer addresses
    * Added
        * show platform software fed active vt hardware if-id {ifid}
        * show platform software fed switch {switch_var} vt hardware if-id {ifid}
    * Modified ShowLispSiteDetailSuperParser
        * Added support for SGT
        * Added support for parsing IPv6 registering ETR in merged locators
        * Fixed a parsing issue when short RLOC addresses are used
        * Made instance_id optional in schema
    * Modified ShowPtpPortInterface
        * Added ptp destination mac regex
    * Modified ShowNveInterfaceDetail
        * Add parsing for command 'show nve interface nve1 detail', before only 'show nve interface nve 1 detail' was supported
        * Add key 'mcast_encap' (Optional for backwards compatibility with older IOSXE version show outputs)
        * Add key 'secondary_ip' which applies in dual-stack EVPN underlay
    * Modified ShowLispServiceRlocMembers
        * Added support for parsing IPv6 RLOC member addresses
    * Added ShowIpOspfDatabaseDatabaseSummary
        * Parser for 'show ip ospf database database-summary'
    * Modified ShowLispDatabaseSuperParser
        * Added support for parsing IPv6 RLOC addresses
        * Fixed the ordering of parsing auto-discover-rloc and NO ROUTE TO EID PREFIX
    * Modified ShowPlatformHardwareQfpStatisticsDrop
        * Add logic when there is no global drop stats
    * Modified ShowLispIpMapCachePrefixSuperParser
        * Added support for parsing IPv6 ITR RLOC addresses
    * Modified ShowVrf
        * Fixed to capture route distinguisher status
    * Modified ShowBgpSummarySuperParser
        * Updated regex to capture variation of outputs
    * Modified ShowRedundancyStates
        * Changed `unit` in schema as optional
    * Modified ShowIpRoute
        * Updated regex to capture variation of outputs
    * Modified ShowIpCefInternal
        * Updated some keys in schema as optional
    * Modified ShowLispEthernetPublication
        * Added support for parsing IPv6 publisher addresses
    * Modified ShowLispSessionRLOC
        * Added support for parsing IPv6 peer and local addresses
    * Modified ShowLispDatabaseEid
        * Made map_servers and locators optional in schema
    * Modified ShowRunningConfigNve
        * Added regex <p3_3_1> to get vxlan encapsulation info
        * Updated regex pattern <p3_4> to accommodate IPv6 mcast group
        * Updated regex pattern <p4_11>, <p4_12>, <p4_13>, <p4_14> to accommodate IPv6 neighbors
    * Modified ShowLispEthernetMapCache
        * Added support for parsing IPv6 RLOC addresses
    * Modified ShowLispInstanceIdServiceStatistics
        * Added support for parsing IPv6 ITR and ETR map resolver addresses
    * Modified ShowLispARDetailParser
        * Added support for parsing IPv6 ETR addresses
    * Fixed ShowPolicyMapTypeQueueingInterfaceOutput
        * Fixed queue status variables queue_limit_bytes, total_drops, bytes_output
    * Modified ShowLispEthernetPublicationPrefix
        * Added support for parsing IPv6 publisher and RLOC addresses
        * Added support for new display format of publisher addresses
    * Modified ShowLispSessionCapabilityRLOC
        * Added support for parsing IPv6 peer and local addresses
    * Added
        * show processes pid
    * Modified ShowPlatformSoftwareWiredClientSwitchActiveFo
        * Modified show platform software wired-client switch active F0
    * Modified ShowLispRemoteLocatorSet
        * Added support for parsing IPv6 RLOC addresses
    * Modified ShowLispPublicationConfigPropSuperParser
        * Added support for parsing IPv6 publisher addresses
    * Modified ShowLispIpv4Publication
        * Added support for parsing IPv6 publisher addresses
    * Modified ShowLispDynamicEidSuperParser
        * Added support for parsing IPv6 map server addresses


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowPolicyMapTypeSuperParser
        * Added 'burst_bytes' and 'rate_bps' keys support to super parser
    * Modified ShowVlanPrivateVlan
        * Modified ports key as optional
    * Modified ShowCryptoEntropyStatus
        * Modified regular expression to support "CPU jitter". new change in above 17.10 release.
    * Added ShowCapabilityFeatureMonitorErspanSourceDestination
        * "show capability feature monitor erspan-source"
        * "show capability feature monitor erspan-destination"
    * Added TracerouteIpv6 Parser
        * Parser for "traceroute ipv6 address"
    * Added ShowSdwanAppqoeStatus parser
        * Parser for "show sdwan appqoe status"
    * Added ShowSdwanAppqoeServiceChainStatus parser
        * Parser for "show sdwan appqoe service-chain status"
    * Added ShowSdwanAppqoeDreoptStatus parser
        * Parser for "show sdwan appqoe dreopt status"
    * Added ShowSwitchStackPorts parser
        * Parser for "sh switch stack-ports"
    * Added ShowIsisSrv6LocatorsDetail
        * added parser for show isis srv6 locator details
    * Added ShowPlatformSoftwareTdlContentBpConfig Parser
        * Parser for "show platform software tdl-database content bp config {mode}"
    * Added ShowCableModem
        * show cable modem
        * show cable modem {cm_ipv4_or_ipv6_or_mac}
        * show cable modem rpd {rpd_ipv4_or_ipv6_or_mac}
        * show cable modem rpd id {rpd_mac}
        * show cable modem rpd name {rpd_name}
        * show cable modem cable {cable_interface}
    * Modified ShowPlatformHardwareQfpStatisticsDrop
        * add a new command show platform hardware qfp active statistics drop
    * Added ShowPlatformSoftwareFedMatmMactableVlan
        * parser for 'show platform software fed active matm macTable vlan {vlan}'
        * parser for 'show platform software fed switch {mode} matm macTable vlan {vlan}'
    * Added ShowPlatformSoftwareFedSwitchQosInterfaceIngressNpd Parser
        * Parser for "show platform software fed {switch} {mode} qos interface {interface} ingress npd"
        * "show platform software fed {mode} qos interface {interface} ingress npd"
    * Added ShowPlatformSoftwareFedQosInterfaceIngressNpdDetailed Parser
        * Parser for "show platform software fed {switch} {mode} qos interface {interface} ingress npd detailed"
        * "show platform software fed {mode} qos interface {interface} ingress npd detailed"
    * Added ShowPlatformSoftwareFedQosInterfaceEgressSdkDetailed Parser
        * Parser for "show platform software fed {switch} {mode} qos interface {interface} egress sdk detailed"
        * "show platform software fed {mode} qos interface {interface} egress sdk detailed"
    * Added ShowPlatformSoftwareFedQosInterfaceIngressSdk Parser
        * Parser for "show platform software fed {switch} {mode} qos interface {interface} ingress sdk"
        * "show platform software fed {mode} qos interface {interface} ingress sdk"
    * Added ShowPlatformSoftwareFedQosInterfaceIngressSdkDetailed Parser
        * Parser for "show platform software fed {switch} {mode} qos interface {interface} ingress sdk detailed"
        * "show platform software fed {mode} qos interface {interface} ingress sdk detailed"
    * Added ShowLldpCustomInformation
        * show lldp custom-information
    * Modified ShowClnsProtocol
        * Added `lsp_mtu` in schema
    * Modified ShowInterfaces
        * Added `out_broadcast_pkts` to exclude
    * Modified ShowIsisTopology
        * Added `show isis {address_family} topology` to cli_command
    * Modified ShowIpRouteDistributor
        * added `updated` to exclude
    * Modified ShowIpv6RouteDistributor
        * Added `updated` to exclude
    * Modified ShowRunInterface
        * Updated schema to capture ISIS level
    * Added ShowRunInterfaceAllSectionInterface
        * New parser `show running-config all | section ^interface`
    * Added ShowRunSectionVrfDefinition
        * New parser `show running-config | section vrf definition`
    * Added ShowMplsTrafficEngAutoroute Parser
        * Parser for "show mpls traffic-eng autoroute"
    * Added ShowMplsForwardingTableSummary Parser
        * Parser for "show mpls forwarding-table summary"
    * Added ShowDeviceClassifierAttachedDetail Parser
        * Parser for show device classifier attached detail
    * Modified ShowDeviceClassifierAttachedInterfaceDetail Parser
        * Modified to cater super parser
    * Added ShowInterfaceEtherchannel
        * show interface {interface_id} etherchannel
    * Added ShowInterfacesPrivateVlanMapping Parser
        * Parser for show interfaces private-vlan mapping
    * Added ShowSwitchStackPortsDetail
        * Parser for cli 'show switch stack-ports detail'
    * Added ShowDlepCounters
        * Added new parser for show dlep counters
    * Added ShowDlepConfigInterface
        * show dlep config {interface}
    * Added ShowXfsuEligibility
        * show xfsu eligibility
    * Added ShowBannerMotd Parser
        * Parser for show banner motd
    * Added ShowPlatformHardwareFedSwitchQosQueueStatsInterface Parser
        * Parser for 'show platform hardware fed {switch} {switch_var} qos queue stats interface {interface}'
        * 'show platform hardware fed {switch_var} qos queue stats interface {interface}'
    * Added ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear Parser
        * Parser for 'show platform hardware fed {switch} {switch_var} qos queue stats interface {interface} clear'
        * 'show platform hardware fed {switch_var} qos queue stats interface {interface} clear'
    * Added ShowL2protocolTunnelInterface
        * parser for show l2protocol-tunnel interface <>
    * Added ShowL2protocolTunnelSummary
        * parser for show l2protocol-tunnel summary under c9300
        * parser for show l2protocol-tunnel summary under c9500
    * Added ShowTableMap Parser
        * Parser for "show table-map {map}"
    * Added ShowIpIgmpGroups
        * parser for 'show ip igmp groups'
    * Added ShowCtsInterfaceSummary
        * show cts interface summary
    * Added ShowIpv6MldGroups
        * parser for to verify the mld groups
    * Added ShowIpv6MfibSummary
        * parser for toverify the ipv6 mfib summary
    * Added ShowMplsTrafficEngLinkManagementAdvertisements
        * Parser for show mpls traffic-eng link-management advertisement


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowL2vpnEvpnMcastLocal
        * show l2vpn evpn multicast local
    * Added ShowL2vpnEvpnMcastRemote
        * show l2vpn evpn multicast remote
    * Added ShowL2vpnEvpnCap
        * show l2vpn evpn capabilities
    * Added ShowRunSectionL2vpnEvpn
        * show running-config | section l2vpn evpn
    * Added ShowL2vpnEvpnVpwsVc
        * show l2vpn evpn vpws vc id detail
        * show l2vpn evpn vpws vc id <vc_id> detail
    * Added ShowL2vpnEvpnVpwsVcPreferredPath
        * show l2vpn evpn vpws vc preferred-path


