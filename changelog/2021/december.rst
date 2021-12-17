--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added class ShowLispEthernetDatabase
        * show lisp instance-id {instance_id} ethernet database
        * show lisp {lisp_id} instance-id {instance_id} ethernet database
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet database
        * show lisp eid-table vlan {vlan} ethernet database
    * Added ShowPolicyMapClass
        * show policy-map {policy_name} class {class_name}
    * Modified ShowPolicyMapInterfaceOutput
        * Added p38_1 regexp to match new priority output line
    * Added class ShowLispIpv4MapCachePrefix
        * show lisp instance-id {instance_id} ipv4 map-cache {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 map-cache {prefix}
        * show lisp eid-table vrf {eid_table} ipv4 map-cache {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 map-cache {prefix}
    * Added class ShowLispIpv6MapCachePrefix
        * show lisp instance-id {instance_id} ipv6 map-cache {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 map-cache {prefix}
        * show lisp eid-table vrf {eid_table} ipv6 map-cache {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 map-cache {prefix}
    * Added class ShowLispSessionRLOC
        * show lisp session {rloc}
        * show lisp {lisp_id} session {rloc}
        * show lisp locator-table {locator_table} session {rloc}
        * show lisp vrf {vrf} session {rloc}
    * Added AuthenticationDisplayConfigMode parser
        * authentication display config-mode
    * Modified ShowRunInterface parser
        * Added code to grep trust_device, ipv6_destination_guard_attach_policy and ipv6_source_guard_attach_policy
    * Added AuthenticationDisplayConfigMode
        * 'authentication display config-mode'
    * Added ShowIpMfibVrfSummay
        * show ip mfib vrf vrf summary
    * Added ShowIpMfibVrfActiveHwRate
        * show ip mfib vrf vrf active | c HW Rate
    * Added ShowIpMfibVrfActive
        * show ip mfib vrf vrf active
    * Added class ShowLispInstanceIdIpv4ForwardingEID
        * show lisp instance-id {instance_id} ipv4 forwarding eid remote
    * Added class ShowLispInstanceIdIpv6ForwardingEID
        * show lisp instance-id {instance_id} ipv6 forwarding eid remote
    * Added ShowAAACommonCriteraPolicy
        * Parser for show aaa common-criteria policy name {policy_name}
    * Added ShowFlowExporter parser
        * show flow exporter
    * Added ShowVlanSummary parser
        * show vlan summary
    * Added ShowFlowRecord parser
        * show flow record
    * Added ShowRunningConfigFlowExporter parser
        * show running-config flow exporter
    * Added ShowIpIgmpSnoopingGroupsCount parser
        * show ip igmp snooping groups count
    * Added ShowIpv6MldSnoopingAddressCount parser
        * show ipv6 mld snooping address count
    * Modified ShowBootSystem parser
        * Changed enable_break type and regexp according to stack output
    * Added  ShowIpPimTunnel parser
        * show ip pim tunnel
    * Fixed ShowStandbyBrief parser
        * Modified regexp to grep preempt state
    * Added ShowIpv6DhcpLdra
        * show ipv6 dhcp-ldra
    * Added ShowIpv6DhcpLdraStatistics
        * show ipv6 dhcp-ldra statistics
    * Added ShowLicenseAll
        * show license all
    * Added ShowLicenseEventlog2
        * show license eventlog 2
    * Added ShowLicenseRumIdDetail
        * show license rum id detail
    * Added ShowLicenseStatus
        * show license status
    * Added ShowLicenseUsage
        * show license usage
    * Added class ShowLispIAFServer
        * show lisp instance-id {instance_id} {address_family} server summary
        * show lisp {lisp_id} instance-id {instance_id} {address_family} server summary
        * show lisp locator-table {locator_table} instance-id {instance_id} {address_family} server summary
    * Added ShowLispEidWatch
        * for 'show lisp {lisp_id} instance-id {instance_id} {address_family} eid-watch'
        * for 'show lisp instance-id {instance_id} {address_family} eid-watch'
        * for 'show lisp locator-table {locator_table} instance-id {instance_id} {address_family} eid-watch'
        * for 'show lisp eid-table {eid_table} {address_family} eid-watch'
        * for 'show lisp eid-table vlan {vlan_id} ethernet eid-watch'
    * Added ShowLispEthernetMapCache
        * 'show lisp instance-id {instance_id} ethernet map-cache'
        * 'show lisp {lisp_id} instance-id {instance_id} ethernet map-cache'
        * 'show lisp eid-table vlan {vlan_id} ethernet map-cache'
        * 'show lisp locator-table {vrf} instance-id {instance_id} ethernet map-cache'
    * Added ShowLispInstanceIdForwardingState
        * 'show ip lisp instance-id {instance_id} forwarding state'
        * 'show ipv6 lisp instance-id {instance_id} forwarding state'
        * 'show lisp instance-id {instance_id} {service} forwarding state'
    * Added ShowLispInstanceIdDNStatistics
        * 'show lisp {lisp_id} instance-id 16777214 dn statistics'
        * 'show lisp instance-id 16777214 dn statistics'
    * Added ShowLispRedundancy
        * for 'show lisp {lisp_id} redundancy'
        * for 'show lisp redundancy'
        * for 'show lisp locator-table {locator_table} redundancy'
    * Added class ShowLispSessionCapabilityRLOC
        * show lisp vrf {vrf} session capability {rloc}
    * Added ShowLoggingOnboardRpActiveUptime
        * show logging onboard rp active uptime
    * Added ShowLoggingOnboardRpActiveStatus
        * show logging onboard rp active status
    * Added ShowLoggingOnboardRpActiveTemperatureContinuous
        * show logging onboard rp active temperature continuous
        * show logging onboard rp active voltage continuous
        * show logging onboard rp active message continuous
    * Added ShowMkaStatistics
        * show mka statistics
    * Added ShowPlatformSoftware
        * for 'show platform software fed {switchvirtualstate} mpls lspa all | c {mode}'
        * for 'show platform software fed {switchvirtualstate} mpls lspa all'
    * Added ShowPlatformHardware
        * for 'show platform hardware fed switch active fwd-asic drops exceptions'
    * Added ShowPowerInlineUpoePlusModule
        * show power inline upoe-plus module {mod_num}
    * Added ShowRunningConfigFlowMonitor
        * show running-config flow monitor
    * Added ShowFlowMonitorAll
        * show flow monitor all
    * Added ShowTelemetryReceiverName
        * show telemetry receiver name {name}
    * Added ShowTelemetryReceiverAll
        * show telemetry receiver all
    * Added ShowTelemetryInternalSensor
        * show telemetry internal sensor subscription {sub_id}
        * show telemetry internal sensor stream {stream_type}
    * Added ShowTelemetryInternalSubscriptionAllStats
        * show telemetry internal subscription all stats
    * Added ShowTelemetryConnectionDetail
        * show telemetry connection all
        * show telemetry connection {con_idx} detail
    * Updated ShowTelemetryIETFSubscription
        * show telemetry ietf subscription {sub_id}
        * show telemetry connection {con_idx} subscription
    * Added ShowVpdn
        * show vpdn
    * Modified ShowUsers
        * Added Optional schema keys <connection_details>, <intf>, <u_name>, <mode>, <idle_time>, and <peer_address>
    * Added ShowIpIgmpVrfGroups
        * show ip igmp vrf {vrf} groups
    * Added ShowPlatformMplsRlistSummary
        * show platform software fed switch {switch_type} mpls rlist summary
    * Added ShowPlatformSoftwareInterfaceSwitchF0Brief
        * show platform software interface switch {mode} F0 brief
    * Added ShowPlatformSoftwareFedSwitchPortSummary
        * show platform software fed switch {mode} port summary
    * Added ShowPower
        * show power {detail}
    * Added ShowIdprom
        * show idprom
    * ADDED ShowUmbrellaDeviced
        * 'show umbrella deviceid'
    * ADDED ShowUmbrellaConfig
        * 'show umbrella config'
    * ADDED ShowPlatformSoftwareDnsUmbrellaStatistics
        * 'show platform software dns-umbrella statistics'
    * Added ShowInterfaceSummaryVlan
        * show interface summary vlan
    * Added ShowMacAddressTableCountSummary
        * show mac address-table count summary
    * Added `show cef path sets summary`
    * Added `show cef uid`
    * Addded `show cef path set id <id> detail | in Relpicate oce`
    * Added `show mpls forwarding-table | sect gid`
    * Added ShowLispEthernetMapCachePrefix
        * show lisp instance-id {instance_id} ethernet map-cache {eid_prefix}
        * show lisp {lisp_id} instance-id {instance_id} ethernet map-cache {eid_prefix}
        * show lisp eid-table vlan {vlan} ethernet map-cache {eid_prefix}
        * show lisp locator-table {locator_table} ethernet map-cache {eid_prefix}
    * Added class ShowControllerVDSL
    * Added ShowAAACacheGroup
        * show aaa cache group {server_grp} all
        * show aaa cache group {server_grp} profile {profile}
    * Inherit schema and parser for show crypto pki certificates verbose commands
        * show crypto pki certificates verbose {trustpoint}
    * Inherit Ipv4 schema and parser for Show Lisp Ipv6 Route Import Map Cache commands
        * show lisp instance-id {instance_id} ipv6 route-import map-cache
        * show lisp instance-id {instance_id} ipv6 route-import map-cache {eid}
        * show lisp instance-id {instance_id} ipv6 route-import map-cache {eid_prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 route-import map-cache
        * show lisp {lisp_id} instance-id {instance_id} ipv6 route-import map-cache {eid}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 route-import map-cache {eid_prefix}
        * show lisp eid-table vrf {vrf} ipv6 route-import map-cache
        * show lisp eid-table vrf {vrf} ipv6 route-import map-cache {eid}
        * show lisp eid-table vrf {vrf} ipv6 route-import map-cache {eid_prefix}
        * show lisp eid-table {eid_table} ipv6 route-import map-cache
        * show lisp eid-table {eid_table} ipv6 route-import map-cache {eid}
        * show lisp eid-table {eid_table} ipv6 route-import map-cache {eid_prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 route-import map-cache
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 route-import map-cache {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 route-import map-cache {eid_prefix}
    * Added ShowLispIpv6Away
        * show lisp instance-id {instance_id} ipv6 away
        * show lisp instance-id {instance_id} ipv6 away {eid}
        * show lisp instance-id {instance_id} ipv6 away {eid_prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 away
        * show lisp {lisp_id} instance-id {instance_id} ipv6 away {eid}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 away {eid_prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away {eid_prefix}
        * show lisp eid-table {eid_table} ipv6 away
        * show lisp eid-table {eid_table} ipv6 away {eid}
        * show lisp eid-table {eid_table} ipv6 away {eid_prefix}
        * show lisp eid-table vrf {eid_table} ipv6 away
        * show lisp eid-table vrf {eid_table} ipv6 away {eid}
        * show lisp eid-table vrf {eid_table} ipv6 away {eid_prefix}
    * Added ShowInventoryOID
        * show inventory OID
    * Added  ShowInventoryRaw
        * show inventory raw
        * show inventory raw | include {include}
    * Added ShowNveInterfaceDetail
        * show nve interface nve {nve_num} detail
    * Added ShowNveVni
        * show nve vni
    * Modified ShowIpEigrpInterfaces
        * show ip eigrp vrf <vrf> interfaces
    * Added ShowControllers for Catalyst 9300 platform
        * show controllers ethernet-controller {interface} phy detail
    * Modified ShowRunInterface
        * Added parsing support (schema and parsers) for following output
            * spanning-tree portfast trunk

* nxos
    * Added ShowIncompatibilityNxos
        * show incompatibility nxos {image}
    * Added ShowBootMode
        * show boot mode
    * Added ShowInstallAllStatus
        * show install all status
    * Added ShowIpv6Neighbor
        * show ipv6 neighbor
        * show ipv6 neighbor vrf all
        * show ipv6 neighbor vrf <vrf>
    * Added ShowSpanningTreeIssuImpact
        * show spanning-tree issu-impact
    * Modified ShowInterfaceBrief
        * show interface brief fix to handle vlan bd down state
    * Added ShowIpv6Ospfv3NeighborsDetail
        * show ipv6 ospfv3 neighbors detail
        * show ipv6 ospfv3 neighbors <neighbor> detail
        * show ipv6 ospfv3 neighbors detail vrf <vrf>
        * show ipv6 ospfv3 neighbors <neighbor> detail vrf <vrf>

* generic
    * Added ShowVersion
        * show version
    * Added Inventory
        * show inventory
    * Added Uname
        * uname -a

* utils
    * Modified common.py
        * Added banner message to do 'make json' in case of JSON file issue
    * Modified unittests.py
        * To support excluding parser class via EXCLUDE_CLASSES

* iosxr
    * Added ShowIsisSegmentRoutingSrv6Locators
        * show isis segment-routing srv6 locators
        * show isis instance {instance} segment-routing srv6 locators


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowLispIpv4Publication
        * Updated regex patterns and logic to handle updated device output from show command
    * Modified ShowLispIpv6Publication
        * Updated regex patterns and logic to handle updated device output from show command
    * Modified ShowLispPublicationPrefixSuperParser
        * Updated regex pattern <p1> and logic to handle updated device output from show command
    * Modified ShowLicenseSummary
        * Modified show license summary parser in order to grep all information & also to support other platform devices
    * Modified ShowTelemetryConnectionAll
        * show telemetry connection all
    * Modified ShowIpMfibSchema
        * Added optional keyword for key 'incoming_interface_list'
    * Modified ShowBgpNeighborsAdvertisedRoutesSuperParser
        * To support more varied output in the 'show bgp all neighbor {neighbor} advertised-routes' command
    * Modified ShowInterfacesTransceiverDetail
        * Value key can be string or a float to cover cases where device outputs 'N/A'
    * Modified ShowLispInstanceIdDNStatistics
        * Fixed for generic instance id
    * Modified ShowInterfacesTransceiverDetail
        * Improved handling for larger outputs
    * Modified ShowIsisRib
        * Fixed a regex to cover another cli output variation
    * Modified ShowL2vpnEvpnPeersVxlanDetail
        * Added support for UP Time in 000000 format
    * Modified ShowStormControl
        * Added support for Filter State in Link Down
    * Modified Traceroute
        * Fixed regex matching order
        * Added support for address hostname
    * Modified ShowBgpDetailSuperParser
        * Changes made for ShowIpBgpDetail to handle ext_community lists that are multiple lines
    * Modified ShowUdldInterface
        * Fixed schema and output to parse all lines of command
    * Modified ShowDmvpn
        * Change to regex to capture UNKNOWN peer
    * Modified ShowIpInterface
        * Added if statements to broadcast address logic to check for existence
        * Allows unnumbered interfaces to pass since they report a broadcast
    * Modified ShowIpBgpL2vpnEvpn
        * Fixed regex for supporting both IPv4 and IPv6 address
    * Modified ShowL2vpnEvpnMacDetail
        * Fixed regex for supporting both IPv4 and IPv6 address
    * Modified ShowL2vpnEvpnMacIpDetail
        * Fixed regex for supporting both IPv4 and IPv6 address
    * Modified ShowBgpSummarySchema
        * Modified bgp_id and local_as keys to work as either int/str types. BGP AS Notation Dot does not work with strictly type int.
    * Modified ShowBgpSummarySuperParser
        * Modified p2 match line to get local_as variable working as int or str type.
    * Modified ShowBgpAllNeighborSchema
        * Modified remote_as and local_as keys to work as either int/str types. BGP AS Notation Dot does not work with strictly type int.
    * Modified ShowBgpNeighborSuperParser
        * Modified p2_1, p2_2, p2_3 match line to get local_as variable working as int or str type.
    * Modified ShowIpRoute
        * Modified p3 regex pattern to be able to handle patterns such i*L1 without any spaces.
        * Changed names of folder unit tests to be consistent format golden_output<#>
    * Modified ShowIpv6Route
        * Modified golden_output8_expected.py to be able to handle the parser modifications over the past months. Initial was incorrect.
    * Modified ShowIpBgpL2VPNEVPN
        * Changed CLI from show ip bgp l2vpn evpn evi {evi} to show ip bgp l2vpn evpn evi {evi} detail.
    * Added ShowApStatus to support
        * show ap status
    * Modified ShowApSummary
        * Separated 'country' from 'location' in parsed output
    * Modified ShowApConfigGeneral
        * Added optional argument for AP name
    * Added ShowCapwapClientRcb to support
        * show capwap client rcb
    * Modified ShowCryptoPkiCertificateVerbose
        * Modified schema to make certain key optional.
        * Corrected counters to give the exact order of numbering
    * Modified ShowCryptoPkiCertificateVerbose
        * Modified for key error.
    * Modified ShowRomVarSchema
        * Corrected the keyword from crash to crashinfo
    * Modified ShowLispServiceSummary
        * show lisp service {service} summary,
        * show lisp {lisp_id} service {service} summary,
        * show lisp locator-table {locator-table} service {service} summary,
        * show lisp locator-table vrf {vrf} service {service} summary
    * Modified ShowRunInterface
        * Added support for Nve interfaces
    * Modified ShowMacsecSummary
        * Added support for empty response
    * Modified ShowIpEigrpTopology
        * Modified regex to support parsing EIGRP in named mode.
    * Modified ShowInterfacesDescription
        * Added two tests to check Di, Vi, Vp, pw and Ce full interface name conversion
    * Modified ShowSnmpMibIfmibIfindex
        * Modify regex pattern p1 to correctly match interfaces of the type 'unrouted VLAN <ID>'
    * Modified ShowPowerInline
        * Re-named regex pattern p1 to p1a and changed the pattern for <power> & <max> to always include ´.´,
        * Added regex pattern p1b to cover 'show power inline' output from Cat45xxR.
    * Modified ShowRunInterface
        * Removed duplicate schema variables
            * Optional('snmp_trap_link_status') bool,
            * Optional('snmp_trap_mac_notification_change_added') bool,
            * Optional('snmp_trap_mac_notification_change_removed') bool,
            * Optional('spanning_tree_bpduguard') str,
            * Optional('spanning_tree_portfast') bool,
            * Optional('spanning_tree_bpdufilter') str,
            * Optional('switchport_access_vlan') str,
            * Optional('switchport_trunk_vlans') str,
            * Optional('switchport_mode') str,
            * Optional('switchport_nonegotiate') str,
            * Optional('vrf') str,
        * Added the following schema variable
            * Optional('spanning_tree_portfast_trunk') bool,
    * Modified ShowRunInterface schema and parser
        * Added regex to parse ACLs applied to an interface.

* nxos
    * Modified ShowNveInterfaceDetail
        * Fixed handling of interface discovery when given output
    * Modified ShowBgpSessions
        * Added two new regex patterns to accommodate link local ipv6 bgp peers.
        * Added a new test case for the testing of these new patterns.

* utils
    * Modified unittests.py
        * Modified unittests.py to be able to handle older legacy parsers with the parser_command variable instead of cli_command.
    * Modified Common
        * Added Di, Vi, Vp, pw and Ce to convert list of interfaces

* asa
    * Modified ShowRoute
        * Supports tunneled routes

* iosxr
    * Modified ShowL2vpnMacLearning
        * Changed cli_command from string to list



