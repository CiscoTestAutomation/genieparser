--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* nxos
    * ShowL2vpnBridgeDomainDetail
        * Added missing UT for ShowL2vpnBridgeDomainDetail

* iosxe
    * Added show mrp ring parser
        * Parser to get values for show mrp ring
    * Added ShowPortSecurityAddress
        * parser for "show port-security address"
    * Added ShowPlatformSoftwareFedSwitchAclIfId
        * parser for 'show platform software fed switch {switch} {mode} if-id {if_id}'
    * Added affinity_id support
        * Added affinity_id support in show publication prefix schema, parser.
        * Added affinity_id support in show map-cache prefix schema, parser.
        * Added affinity_id support in show database schema, parser.
    * New Parser for TestVdslOption
        * Parser for 'test vdsl option option1 option2'
    * Added ShowPlatformHardwareFedSwitchQosQueueConfig
        * show platform hardware fed {switch_var} qos queue config interface {interface}
        * show platform hardware fed {switch} {switch_var} qos queue config interface {interface}
    * Added ShowNat66Statistics
        * show nat66 statistics
    * Added ShowNat66Prefix
        * show nat66 prefix
    * Added ShowNat66Nd
        * show nat66 nd
    * Added ShowPlatformHardwareQfpActiveFeatureNat66DatapathPrefix
        * show platform hardware qfp active feature nat66 datapath prefix
    * Added show mrp ports parser
        * Parser to get values for show mrp ports
    * Added ShowTechSupportIncludeShow
        * Added schema and parser for show tech-support | i show
    * Added ShowIpMfibCount
        * parser for show ip mfib | count {interface}
    * Added ShowInterfaceHumanReadableIncludeDrops
        * show interface {interface} human-readable | i drops
    * Added ShowIpIgmpSnoopingMrouterVlan Parser
        * Parser for show ip igmp snooping mrouter vlan {vlan}
    * Added ShowAvbDomain
        * parser for 'show avb domain'
    * Added ShowPlatformSoftwareAccessListSwitchActiveF0Summary
        * Added schema and parser for show platform software access-list switch active F0 summary
    * Added ShowIpIgmpSnoopingQuerierVlanDetail
        * added parser for "show ip igmp snooping querier vlan {vlan} detail"
    * Added ShowPlatformSoftwareFedSwitchActiveAclStatisticsEvents
        * parser for Show Platform Software Fed Switch Active Acl Statistics Events
    * Added ShowPlatformPmEtherchannelGroupMask
        * Parser for show platform pm etherchannel {ec_channel_group_id} group-mask
    * Added ShowPlatformSoftwareFedSwitchActiveStpVlan
        * Parser for show platform software fed switch active stp-vlan {vlan_id}

* iosxr
    * Added ShowL2vpnForwardingXconnectDetailLocation
        * parser for 'show l2vpn forwarding xconnect {xconnect_name} detail location {location_name}'
    * Added ShowOspfSummary
        * Added parser for cli 'show ospf {process_name} summary'
        * Added parser for cli 'show ospf {process_name} vrf {vrf_name} summary'
    * Added ShowBgpVrf
        * added new parser for cli 'show bgp vrf {vrf}'
        * added new parser for cli 'show bgp vrf {vrf} {summary}'
        * added new parser for cli 'show bgp vrf {vrf} {address_family} summary'
        * added new parser for cli 'show bgp vrf {vrf} {address_family} {value}'


--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowAccessSessionMacDetails parser.
        * Added Local policies New keys in Schema.
        * Added Server policies New key in Schema.
        * Modified user_name key as optional in Schema.
        * Added regex pattern for newly added keys
    * Modified ShowPlatformSoftwareMemoryCallsite
        * Updated regex pattern <p2> to accommodate hex callsites.
    * Modified ShowPlatformHardwareFedActiveTcamUtilization
        * added switch_type argument to execute show cli on standby
    * Modified ShowPlatformTcamPbrNat
        * added switch_type argument to execute show cli on standby
    * Modified ShowPlatformSoftwareFedSwitchActivePuntCpuq
        * added switch_type argument to execute show cli on standby
    * Modified ShowFirmwareVersionAll Parser
        * Added "switch" option to the firmware CLI
    * Fixed ShowControllerVDSLSchema parser
        * Parser for "show controller vdsl <slot no>"
    * Modified affinity_id support
        * Removed affinity_id support in show database prefix schema, parser under
        * Added affinity_id support in show database prefix schema, parser under
    * Fixed ShowIdpromInterface Parser
        * Added the key 'vendor_part_number' to schema.
    * Modified ShowIpMroute
        * Allow parsing IPv6 next hop for LISP outgoing interface.
        * Allow parsing Inherited outgoint interface list.
    * Modified ShowIpv6Mfib
        * Allow parsing blank Mfib flags.
        * Allow parsing IPv6 next hop for LISP outgoing interface.
    * Modified ShowRunInterface
        * Added 111 regex for pim outputs
    * Modified ShowModule Parser
        * Fixed parser for multiple switches
    * Enhanced BGP router ID extraction
        * Modified the regular expression pattern (p1) to support both interface name and IP address for BGP router ID.
    * Modified BGP router ID extraction from IP Address
        * Added new support for BGP router ID extraction from the provided IP address.
    * Modified ShowRomMonSwitchR0
        * parser for 'show rom-mon switch {switch_num} {process}'
    * Added ShowIpNatStatistics Parser
        * Added if condition for name_1 and name_2 key to match with all available output.
    * Modified ShowClnsNeighborsDetail
        * Updated the regex to support `-`
    * Removed duplicate class ShowLispEthernetDatabase
        * removed the duplicate class and add a optional key to ShowLispDatabaseSuperParser schema
    * Modified ShowIpIgmpSnoopingQuerier Parser
        * Fixed parser for all type of ports
    * Modified ShowBootvar
        * Updated regex pattern <p1> to parse the output which contains WHITESPACE in BOOT variable string.
    * Modified ShowStackPowerLoadShedding Parser
        * Fixed p2 and p3 regular expressions
    * Modified ShowPlatformSoftwareWiredClientFpActive Parser
        * Added line.strip()
    * Modified ShowPtpClock Parser
        * Made message_general_ip_dscp and message_event_ip_dscp as optional keys
    * Modified ShowPlatformSoftwareFedSwitchActivePtpDomain Parser
        * Made message_general_ip_dscp and message_event_ip_dscp as optional keys
    * Modified ShowIpv6MldGroups Parser
        * parser for 'show ipv6 mld groups'
    * Updated ShowBgpAllNeighbors parser
        * Added `ack_hold` and `fastretransmit` to exclude list
    * Modified ShowCdpNeighborsDetail
        * Changed software_version from schema to Optional.
    * Modified ShowEnvironmentSuperParser Parser
        * Fixed p1 and p1_1 regex
            * Added New regex p13,p14 and p15 for new log

* nxos
    * Fix for show bgp vrf all all summary parser
        * Added int and float pattern to match all possible values
    * Fix for show bgp vrf <vrf> all neighbors <neighbor> advertised-routes parser
        * Added p9_1 pattern to match all possible state values

* iosxr
    * Modified ShowL2vpnBridgeDomainDetail
        * Adding Optional evi in schema due to parser failed with schema key error
    * Modified ShowRouteIpv4
        * Modified 'outgoing_interface' keyname as optional parameter in schema
        * Added keys 'label', 'tunnel_id', 'binding_label', 'extended_communites_count', 'nhid', 'path_grouping_id', 'srv6_headend' and 'sid_list' as optional parameters in scehma
        * Fixed pattern <p11> as it should not match line 'NHID0x0(Ref0)'
        * Added pattern <p16> to support line 'Label None'
        * Added pattern <p17> to support line 'Tunnel ID None'
        * Added pattern <p18> to support line 'Binding Label None'
        * Added pattern <p19> to support line 'Extended communities count 0'
        * Added pattern <p20> to support line 'NHID0x0(Ref0)'
        * Added pattern <p21> to support line 'Path Grouping ID 100'
        * Added pattern <p22> to support line 'SRv6 Headend H.Encaps.Red [f3216], SID-list {fc00c0001002e002}'
    * Modified ShowRouteIpv6
        * Fixed pattern <p12> as it should not match line 'NHID0x0(Ref0)'
        * Added pattern <p15> to support line 'Label None'
        * Added pattern <p16> to support line 'Tunnel ID None'
        * Added pattern <p17> to support line 'Binding Label None'
        * Added pattern <p18> to support line 'Extended communities count 0'
        * Added pattern <p19> to support line 'NHID0x0(Ref0)'
        * Added pattern <p20> to support line 'Path Grouping ID 100'
        * Added pattern <p21> to support line 'SRv6 Headend H.Encaps.Red [f3216], SID-list {fc00c0001002e003}'

* <iosxe>
    * Added <ShowControlConnections>
        * Change the <p1> regex under if block for <peer_organization>

* iosxe/c9600
    * Modified ShowPlatformHardwareFedActiveTcamUtilization
        * Made mode dynamic in CLI command

* iosxe/c9600/c9606r
    * Modified ShowPlatformHardwareFedActiveTcamUtilization
        * Made mode dynamic in CLI command


--------------------------------------------------------------------------------
                                     Modify
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowLispInstanceidService
        * Added ethernet_fast_detection to schema and parser.
    * Modified ShowRomvar
        * Made boot key as optional.


--------------------------------------------------------------------------------
                                    Modified
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowPppoeSession parser
        * Parser for "show pppoe session"


