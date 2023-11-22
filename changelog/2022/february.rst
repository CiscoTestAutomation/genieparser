--------------------------------------------------------------------------------
                                     Added                                      
--------------------------------------------------------------------------------

* iosxe
    * Added ShowLispInstanceIdServiceStatistics
        * show lisp instance-id {instance_id} {service} statistics
        * show lisp {lisp_id} {instance_id} {service} statistics
        * show lisp locator-table {locator_table} instance-id {instance_id} {service} statisticsNo backward compatibility


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowFirmwareVersionAll
        * show firmware version all
    * Added ShowIpv6RouteSummary parser
        * Parser for 'show ipv6 route summary' and 'show ipv6 route vrf {vrf} summary'
    * Modified ShowIpRouteSummary parser
        * Modified parser to grep v6 protocols
    * Added ShowLispInstanceIdIpv4MapCache
        * show lisp instance-id {instance_id} ipv4 map-cache
        * show lisp {lisp_id} instance-id {instance_id} ipv4 map-cache
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 map-cache
        * show lisp eid-table vrf {vrf} ipv4 map-cache
        * show lisp eid-table {eid_table} ipv4 map-caches
    * Added ShowLispInstanceIdIpv6MapCache
        * show lisp instance-id {instance_id} ipv6 map-cache
        * show lisp {lisp_id} instance-id {instance_id} ipv6 map-cache
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 map-cache
        * show lisp eid-table vrf {vrf} ipv6 map-cache
        * show lisp eid-table {eid_table} ipv6 map-caches
    * Deleted ShowLispEidTableVrfUserIpv4MapCache existing class because this command is covered by new parser (ShowLispInstanceIdIpv4MapCache). Modified Schema and updated code.No backward compatibility
    * Added ShowLisp
        * 'show lisp'
        * 'show lisp {lisp_id}'
    * Added ShowLoggingOnboardRpActiveTemperatureDetail
        * show logging onboard rp active temperature detail
        * show logging onboard rp active voltage detail
        * show logging onboard rp standby temperature detail
        * show logging onboard rp standby voltage detail
    * Added ShowPlatformSoftwareFedSwitchActiveQosPolicyTarget parser
        * show platform software fed switch active qos policy target brief
    * Added ShowPlatformSoftwareObjectManagerFpActiveStatistics parser
        * show platform software object-manager FP active statistics
    * Added ShowPolicyMapTypeQueueingSuperParser
    * Added ShowPolicyMapTypeQueueingInterfaceOutput
        * show policy-map type queueing interface {interface} output class {class_name}
        * show policy-map type queueing interface {interface} output
    * Added ShowRunningConfigFlowRecord
        * show running-config flow record
    * Added ShowTelemetryIETFSubscriptionSummary
        * show telemetry ietf subscription summary
    * Added ShowLispInstanceIdService
        * 'show lisp instance-id {instance_id} {service}',
        * 'show lisp {lisp_id} instance-id {instance_id} {service}',
        * 'show lisp locator-table {locator_table} instance-id {instance_id} {service}
    * Added ShowLispSiteSummary
        * 'show lisp site summary',
        * 'show lisp {lisp_id} site summary',
        * 'show lisp site summary instance-id {instance_id}',
        * 'show lisp site summary eid-table vrf {vrf}',
        * 'show lisp site summary eid-table {eid_table}'
    * Added ShowInstallState parser
        * show install <state>
    * Added ShowParserStatistics parser
        * show parser statistics
    * Added ShowVersionRunning parser
        * show version running
    * Added ShowStackwiseLink parser
        * show stackwise-virtual switch <number> link
    * Added ShowInstallRollback parser
        * show install rollback
    * Added ShowInstallRollbackId parser
        * show install rollback id <rollback_id>
    * Added ShowPlatformSoftwareInstallManagerSwitchActiveR0OperationHistorySummary parser
        * show platform software install-manager switch active r0 operation history summary
    * Added ShowPlatformSoftwareInstallManagerRpActiveOperationHistorySummary parser
        * show platform software install-manager RP active operation history summary
    * Added show install package SMU parser
        * show install package SMU
    * c9400
        * Added ShowBoot parser
            * show boot
    * Added ShowIpv6DhcpPool
        * Parser for show ipv6 dhcp pool
    * Added ShowIpv6OspfNeighbor
        * Parser for show ipv6 ospf neighbor
    * Added ShowPlatformSoftwareFedActiveAclInfoSummary
        * Parser for Show Platform Software Fed Active Acl Info Summary
    * Added ShowPlatformFedActiveIfmMapping
        * Parser for show platform software fed active ifm mappings
    * Added ShowPlatformFedActiveTcamUtilization
        * Parser for show platform hardware fed active fwd-asic resource tcam utilization
    * Added ShowLispInstanceIdIpv4Server
        * show lisp instance-id {instance_id} ipv4 server
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server
        * show lisp eid-table vrf {vrf} ipv4 server
        * show lisp eid-table {eid_table} ipv4 server
    * Added ShowLispInstanceIdIpv6Server
        * show lisp instance-id {instance_id} ipv6 server
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server
        * show lisp eid-table vrf {vrf} ipv6 server
        * show lisp eid-table {eid_table} ipv6 server
    * Added ShowCryptoIkev2Session
        * show crypto ikev2 session
    * Added ShowCryptoIkev2SessionDetail
        * show crypto ikev2 session detail
    * Added ShowCryptoIsakmpSa
        * show crypto isakmp sa
    * Added ShowCryptoIsakmpSaDetail
        * show crypto isakmp sa detail
    * Added ShowCryptoMibIpsecFlowmibEndpoint
        * Parser for show crypto mib ipsec flowmib endpoint
    * Added ShowCryptoMibIpsecFlowmibTunnel
        * Parser for show crypto mib ipsec flowmib tunnel
    * Added ShowCryptoSessionLocalDetail
        * Parser for show crypto session local {ip_address} detail
    * Added ShowCryptoSessionLocal
        * Parser for show crypto session local {ip_address}
    * Added ShowCryptoIpsecSaCount
        * Parser for show crypto ipsec sa count
    * Added ShowCryptoIkev2SaDetail
        * Parser for show crypto ikev2 sa detail
    * Added ShowCryptoIkev2SaLocalDetail
        * Parser for show crypto ikev2 sa local {ip_address} detail
    * Added ShowCryptoIkev2SaLocal
        * Parser for show crypto ikev2 sa local {ip_address}
    * Added ShowIpMrib
        * show ip mrib route
        * show ip mrib route {group}
        * show ip mrib route {group} {source}
        * show ip mrib vrf {vrf} route
        * show ip mrib vrf {vrf} route {group}
        * show ip mrib vrf {vrf} route {group} {source}
    * Added ShowIpMrib
        * added the new parser for cli "show ip mrib route"
        * show ip mrib route
        * show ip mrib route {group}
        * show ip mrib route {group} {source}
        * show ip mrib vrf {vrf} route
        * show ip mrib vrf {vrf} route {group}
        * show ip mrib vrf {vrf} route {group} {source}
    * Added ShowIpMroute
        * added the new argument verbose and supported additonal
        * combinations in parser for cli "show ip mroute" and "show ipv6 mroute"
        * show ip mroute verbose
        * show ip mroute {group} verbose
        * show ip mroute {group} {source} verbose
        * show ip mroute vrf {vrf}
        * show ip mroute vrf {vrf} {group}
        * show ip mroute vrf {vrf} {group} {source}
        * show ip mroute vrf {vrf} verbose
        * show ip mroute vrf {vrf} {group} verbose
        * show ip mroute vrf {vrf} {group} {source} verbose
        * show ipv6 mroute {group}
        * show ipv6 mroute {group} {source}
        * show ipv6 mroute verbose
        * show ipv6 mroute {group} verbose
        * show ipv6 mroute {group} {source} verbose
        * show ipv6 mroute vrf {vrf} {group}
        * show ipv6 mroute vrf {vrf} {group} {source}
        * show ipv6 mroute vrf {vrf} verbose
        * show ipv6 mroute vrf {vrf} {group} verbose
        * show ipv6 mroute vrf {vrf} {group} {source} verbose
    * Modified class ShowLispSite
        * show lisp site
        * show lisp {lisp_id} site
        * show lisp site instance-id {instance_id}
        * show lisp {lisp_id} site instance-id {instance_id}
        * show lisp site eid-table {eid_table}
        * show lisp {lisp_id} site eid-table {eid_table}
        * show lisp site eid-table vrf {vrf}
        * show lisp {lisp_id} site eid-table vrf {vrf}
    * Modified ShowLispInstanceIdEthernetServer
        * show lisp instance-id {instance_id} ethernet server
        * show lisp {lisp_id} instance-id {instance_id} ethernet server
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server
        * show lisp eid-table vlan {vlan} ethernet server
    * Added ShowLispIpv4ServerExtranetPolicy
        * show lisp instance-id {instance_id} ipv4 server extranet-policy
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server extranet-policy
        * show lisp eid-table {eid_table} ipv4 server extranet-policy
        * show lisp eid-table vrf {vrf} ipv4 server extranet-policy
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server extranet-policy
    * Added ShowLispIpv6ServerExtranetPolicy
        * show lisp instance-id {instance_id} ipv6 server extranet-policy
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server extranet-policy
        * show lisp eid-table {eid_table} ipv6 server extranet-policy
        * show lisp eid-table vrf {vrf} ipv6 server extranet-policy
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server extranet-policy
    * Added ShowCallAdmissionStatistics parser
        * show call admission statistics
    * Added ShowCallAdmissionStatisticsDetailed parser
        * show call admission statistics detailed
    * Added ShowPlatformSoftwareFedSwitchActivePuntCpuq
        * show platform software fed switch active punt cpuq {cpu_q_id}
    * Added ShowPlatformTcamPbr
        * show platform hardware fed switch active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}
    * Added ShowPlatformNatTranslationsStatistics
        * show platform nat translations active statistics
    * Added ShowPlatformNatTranslations
        * show platform nat translations active
    * Added ShowPlatformTcamAcl
        * show platform hardware fed switch active fwd-asic resource tcam table acl | begin {INPUT_NAT}
    * Added ShowStackwiseVirtualLink
        * show stackwise-virtual link
    * Added ShowPlatSwObjectManagerF0Statistics
        * show platform software object-manager {switch} {switch_type} F0 statistics
    * Added ShowPlatSwObjectManagerF0ErrorObject
        * show platform software object-manager {switch} {switch_type} F0 error-object
    * Added ShowAAAMethodList
        * Added the parser for cli 'show aaa method-list {type}'
    * Added ShowRunningConfigAAA
        * Added the parser for cli 'show running-config aaa'
    * Modified class ShowLispServiceDatabase
        * The existing schema does not properly represent the output of the show command So fixed all the schema so that it represents the output properly and updated code accordingly
    * Modified class ShowLispEidTableServiceDatabase
        * The existing schema does not properly represent the output of the show command So fixed all the schema so that it represents the output properly and updated code accordingly
    * Modified class ShowLispEthernetDatabase
        * The existing schema does not properly represent the output of the show command So fixed all the schema so that it represents the output properly and updated code accordingly
    * Below are the new parsers added for pdm
        * Added show pdm steering policy
        * Added show pdm steering policy {steering_policy} detail
        * Added show pdm steering service
        * Added show pdm steering service {steering_service} detail
        * Added show pdm steering policy | count {service}
    * Added ShowRepTopologySegment
        * 'show rep topology segment {no}'
    * Added ShowPlatformSoftwareFedSwitchSecurityfedDhcpsnoopVlanVlanid
        * 'show platform software fed switch {switch_no} security-fed dhcp-snoop vlan vlan-id {vlan_id}'
    * Added ShowInterfacesEtherchannelCounters
        * show interfaces {interface} counter etherchannel
    * Modified ShowIpMroute
        * show ip mroute vrf {vrf} {grpip} {sourceip}
        * show ip mroute vrf {vrf} {grpip}
        * Added Optional schema keys <upstream_interface>, <rpf_nbr>, and <state>
    * Modified ShowBgpAllDetail
        * show bgp {address_family} {route}
    * Added ShowIpMrib command with options
    * Added ShowIpSlaStatistics
        * 'show ip sla statistics'
        * 'show ip sla statistics {probe_id}'
    * Added ShowIpSlaStatisticsDetails
        * 'show ip sla statistics details'
        * 'show ip sla statistics {probe_id} details'
    * Added ShowIpSlaStatisticsAggregated
        * 'show ip sla statistics aggregated'
        * 'show ip sla statistics aggregated {probe_id}'

* iosxr
    * NCS5K
        * Added platform folder
    * Added ShowInterfaceSummary Parser
        * show interface summary


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowInventoryRaw
        * Updated regex <p1> and <p2> and modified code to not to add keywords with empty value
    * Modified ShowEnvironment
        * Updated regex pattern <P4> to accommodate various outputs
    * Modified ShowModule parser
        * Updated ShowModule parser to include missing keys
    * Added ShowVpdnSuperParser
        * show vpdn
        * show vpdn tunnel
    * Modified ShowVpdn
        * Moved logic into ShowVpdnSuperParser
    * Added ShowVpdnTunnel
        * show vpdn tunnel
    * Modified ShowIsisLspLog
        * Added an initial tag value "default"
    * Modified ShowRunInterface
        * Added stackwise_virtual_link and dual_active_detection as new Optional keys.
    * Modified ShowVersion
        * Added two new keys <copyright_years> and <location> to parser schema, updated regex <p3> and <p4>
    * Modified ShowModule
        * Updated regex <p3> and <p4> and modified code so it works with multiple modules
        * Changed keys <redundancy_role>, <operating_redundancy_mode>, and <configured_redundancy_mode> to optional
    * Modified ShowPlatformSoftwareYangManagementProcessState
        * Added missing process states (Init, Failed, Invalid)
    * Modified ShowVlan
        * Added regex <p0> for handling situations where line wrapping is causing breakages
    * Modified ShowPlatform
        * Fix incorrect logic for <p6> slot type. C83 now included in matches for types 'lc' and 'rp'. Fix is NOT BACKWARDS COMPATIBLE
    * Modified ShowBgpAllNeighborsRoutesSuperParser
        * Added p8 to parse the "Total number of prefixes" in the for "show bgp neighbor routes"
    * Modified ShowPlatformSoftwareFedactiveAclCountersHardwareSchema
        * Added Optional Schema keys <ingress_ipv4_ipclients_cpu>, <ingress_ipv6_ipclients_cpu>, <ingress_ipv4_ipclients_drop>, and <ingress_ipv6_ipclients_drop>
    * Modified ShowIpMrouteSchema
        * Changed schema key <rpf_nbr> to Optional
    * Modified ShowProcessCpuSorted
        * Added 'include'/'exclude' support
    * Modified ShowProcessesMemory
        * Added 'exclude'/'section' support
    * Modified ShowSslproxyStatusSchema
        * Added "Dual-Side Optimization" key support.
    * Modified ShowBgpNeighborsAdvertisedRoutesSuperParser
        * added try/catch for unconditional command execution "show bgp all neighbors | i BGP neighbor"

* ios
    * Modified ShowCdpNeighborsDetail
        * Changed port_id from schema to Optional.
        * Rearranged software version and advertisement version patterns to accommodate various outputs.

* iosxr
    * Modified ShowPolicyMapInterface
        * Updated regex patterns <p2> and <p4> to accommodate various outputs
        * Added optional schema keys <queue_conform_packets>, <queue_conform_bytes>, <queue_conform_rate>, <red_random_drops_packets>, and <red_random_drops_bytes>
    * Modified ShowBgpInstanceNeighborsAdvertisedRoutes
        * Added new pattern and logic to handle when device output was split into multiple lines

* generic
    * Modified ShowVersion
        * Adjusted iosxe/ios logic to ignore platforms that contain "x86_64_linux"

* nxos
    * Modified ShowInterface
        * Updated regex pattern <p1> to accommodate various outputs.
    * Modified ShowEigrpTopology
        * Removed cli_commands, af and vrf
    * Added ShowIpEigrpTopology
        * show ip eigrp topology
        * show ip eigrp topology vrf {vrf}
    * Added ShowIpv6EigrpTopology
        * show ipv6 eigrp topology
        * show ipv6 eigrp topology vrf {vrf}


--------------------------------------------------------------------------------
                                     Update                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowMkaSessions Parser
        * changed the 'ckn' variable to match decimal/hexa decimal


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowLispService
        * Modified Schema and updated code.No backward compatibility


