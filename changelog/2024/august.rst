--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowSwitchStackRingSpeed
        * parser for 'show switch stack-ring speed'
    * Modified ShowLispEthernetPublisher
        * Modified the ShowLispEthernetPublisher parsers to facilitate new options.
    * Modified ShowEnvironmentStack
        * Fixed regular expressions p2 and p3 to match the correct values
    * Modified ShowXfsuEligibility
        * Added optional argument 'xfsu_platform_stauts' and made 'reload_fast_platform_stauts' as optional
    * Fixed ShowPlatformSoftwareFedIgmpSnooping
        * Fixed 'show platform software fed {switch_var} {state} ip igmp snooping vlan {vlan}' command and schema for the command.
    * Fixed ShowPlatformSoftwareFedActiveIpv6MldSnoopingVlan
        * Fixed 'show platform software fed {switch_var} {state} ipv6 igmp snooping vlan {vlan}' command and schema for the command.
    * Modified fix for ShowLispRegistrationHistory
        * Modified the command to use the ShowLispRegistrationHistory parser for a more exact match and to fix the fuzzy search issue
    * Modified ShowBgpAllNeighbors
        * Mode peer_group as optional in schema and added p73 regex to match peer-group from user's output.
    * Modified fix for ShowCdpEntry
        * Made 'peer_mac' as optional in the schema
    * Modified parser ShowIpv6MldSnoopingVlan
        * Modified 'host_tracking' as optional argument, fix regex p2 and added unit tests
    * Modified parser ShowEnvironmentSuperParser
        * Added PS_MAPPING keyvalue for C and added unit test files
    * Modified ShowLicenseTechSupport Parser
        * Added optional agruments 'trust_point', 'ip_mode', 'trustpointenrollmentonboot', 'smartagentpurgeallreports'
        * 'smartagentslpenhanced', 'smartagentmaxermnotifylistsize'
    * Modified ShowEtherChannelDetail Parser
        * Made 'fast_switchover' and 'dampening' as optional agruments and added unit tests for the same
    * Modified fix for ShowPlatformFedSwitchActiveFnfRecordCountAsicNum
        * Modified the name of the command in the parser comment section in ShowPlatformFedSwitchActiveFnfRecordCountAsicNum
    * Added ShowPlatformFedActiveFnfRecordCountAsicNum
        * Added schema and parser for show platform software fed active fnf record-count asic <asic num>
    * Modified ShowPlatformSoftwareFedSwitchActiveAclUsage
        * Added switch_num to show command.
    * Modified ShowPlatformSoftwareFedSwitchActivEAclUsage
        * Added switch_num to show command.
        * Renamed class name ShowPlatformSoftwareFedSwitchActivEAclUsage to ShowPlatformSoftwareFedSwitchActiveAclUsage
    * Deleted ShowPlatformSoftwareFedSwitchStandbyAclUsage
        * Removed duplicate class.
    * Modified fix for ShowPlatformSoftwareFedSwitchActiveAclUsage
        * Modified the Regex pattern p<2> to accommodate various outputs
    * Modified fix for ShowVersion
        * Modified the schema, Added regex pattern <p33> and added the corresponding code to get SMUs data in the output.
    * Modified ShowPlatform
        * update lines to match the output of the IE model into genie parser show platform i.e IE- , ESS- keywords that will ensure IE family supports.
    * Modified fix for ShowPlatformSoftwareFedSwitchActiveIpRouteDetail
        * Updated regex pattern and added keys in schema for show platform software fed {switch} {mode} ip route {ip_add} {detail}
        * Updated regex pattern and added keys in schema for show platform software fed {switch} {mode} ip route {ip_add}
    * Modified ShowMonitorEventTraceDmvpnAll
        * Fixed incorrect regex for events NHRP-CTRL-PLANE-RETRANS and NHRP-TUNNEL-ENDPOINT-ADD
    * Modified ShowMonitorEventTraceDmvpnAll
        * Fixed incorrect regex for events NHRP-CTRL-PLANE-RETRANS
    * Added missing empty_output_arguments.json files.
    * Removed unused golden output tests
    * Modified ShowPlatformSoftwareIgmpSnoopingGroupsCount
        * Added regex pattern <p2> and <p3> to accommodate various outputs.
    * Modified ShowPlatformSoftwareFedSwitchActiveIpRoute
        * Updated parameters default value
    * Added ShowPlatformSoftwareFedIpMfibCount/ShowPlatformSoftwareFedIpMfibSummary
        * Added missing ShowPlatformSoftwareFedSwitchActiveIpRoute
    * Removed ShowPlatformSoftwareFedIgmpSnoopingGroupsCount
        * Because we have ShowPlatformSoftwareIgmpSnoopingGroupsCount parser for same commands
    * Modified ShowInterfaces
        * Added <in_drops>, <out_drops>, <peer_ip> and <vc_id> into schema as Optional.
        * Renamed regex pattern <p_cd>, <p_cd_2> to <p54>, <p55> respectively and updated the code accordingly.
        * Added regex pattern <p1_2>, <p6_1>, <p56>, <p57> and <p58> to accommodate various outputs.
    * Modified ShowModule
        * Changed <mac_address>, <hw>, <fw>, <sw> and <status> from schema to Optional.
    * Modified ShowCtsInterface
        * Added Vlan Sgt-Map tabulated data to the schema.
        * Added regex p27 to parse the Vlan Sgt-Map tabulated data.
    * Modified fix for ShowLogging
        * Removed the variable that initializes a dictionary for the key log_buffer_bytes

* nxos
    * Revised ShowNveEthernetSegment
        * removed keys 'cc_failed_vlans', 'cc_timer_left' and 'ead_evi_rt_timer_age' keys
        * added keys 'df_bd_list', 'df_vni_list', 'esi_type' and 'esi_df_election_mode'
        * made changes to regular expressions to accomodate the parent interface as port-channel
    * Fixed parser show access-lists summary
        * Updated the attachment_points as optional so that it should not throw errors if no attached interfaces are present
    * Modified ShowNtpPeerStatus
        * Updated regex pattern <p2_1> to parse valid IP adddress.
        * Updated code to fix wrong clock_state value.

* added showplatformsoftwarefedigmpsnoopingvlandetail
    * Added 'show platform software fed {switch_var} {state} ip igmp snooping vlan {vlan} detail' command and schema for the command.

* added showplatformsoftwarefedactiveipv6mldsnoopingvlandetail
    * Added 'show platform software fed {switch_var} {state} ipv6 igmp snooping vlan {vlan} detail' command and schema for the command.

* iosxr
    * Modified fix for ShowMplsLdpParameters
        * Modified schema, updated regex pattern <p21>, added patterns <p32> and <p33>, and added the corresponding code to get IGP sync delay data.
    * Modified MonitorInterface
        * Added missing empty_output_arguments.json files
    * Modified MonitorInterfaceInterface class
        * Renamed class to MonitorInterface
        * Added support for the following CLI commands
            * monitor interface
            * monitor interface full-name
            * monitor interface filter physical
            * monitor interface {interface} full-name
            * monitor interface {interface} full-name wide
            * monitor interface {interface} wide full-name
    * Added Revision 1 of MonitorInterface
        * Changed convert_intf_name to use iosxr specific mapping
    * Modified ShowSegmentRoutingSrv6LocatorSid
        * Updated code to fix folder_parsing job for empty test

* common
    * Modified get_parser function to pass the formatted command as `command` variable
    * User can now use the following syntax for parser `cli` method
        * ``def cli(self, command, output=None, **kwargs)``

* utils
    * Updated unittest code to run empty tests successfully

* <nxos>
    * Modified ShowIpRoute
        * Updated regex pattern <p2> to accommodate new output line


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * New ShowSwitchStackBandwidth
        * Parser for 'show switch stack-bandwidth'
    * Added ShowPlatformSoftwareFedSwitchAclUsageIncludeAcl
        * Added show platform Software fed switch {switch_num} acl usage
        * Added show platform Software fed switch {switch_num} acl usage | include {acl_name}
    * Added ShowPlatformSoftwareFedSwitchActiveAclBindDbIfid parser.
        * Added parser for cli show platform software fed switch active acl bind db if-id {if_id} detail.
    * Added ShowPlatformSoftwareFedSwitchAclUsageIncludeAcl
        * Added show platform Software fed switch {switch_num} acl usage
        * Added show platform Software fed switch {switch_num} acl usage | include {acl_name}
    * Added ShowPlatformSoftwareFedSwitchActiveIfmInterfacesInternal parser.
        * Added parser for cli show platform software fed switch active ifm interfaces internal {interface}.
    * Fixed regex pattern for cli ShowPlatformSoftwareFedSwitchActiveIfmInterfacesLabel parser.
        * Fixed regex pattern for cli show platform software fed {switch} active ifm interfaces {label}.
    * Added ShowPlatformSoftwareFedSwitchActiveInjectBrief
        * Added show platform software fed {switch} {mode} inject ios-cause brief
        * Added show platform software fed active inject ios-cause brief
    * Added ShowPlatformSoftwareFedSwitchActiveSecurityFedArpIf parser.
        * Added parser for cli show platform software fed switch active security-fed arp if {if_id}.
    * Added ShowPlatformSoftwareFedSwitchActiveSecurityFedArpVlan parser.
        * Added parser for cli show platform software fed switch active security-fed arp vlan {vlan}.
    * Added ShowIdprom parser
        * Added show idprom all cli
    * Added ShowSpanningTreeSummaryTotals
        * Added show spanning-tree summary totals
    * Added ShowModule
        * Added schema and parser for 'show module' under c9610
    * Added ShowPlatformSoftwareFedIpv6MfibCount
        * Added 'show platform software fed {switch_var} {state} ipv6 mfib count' command and schema for the command.
    * Added ShowPlatformSoftwareFedIpv6MfibSummary
        * Added 'show platform software fed {switch_var} {state} ipv6 mfib summary' command and schema for the command.
    * Added ShowPlatformSoftwareFedIpv6MldSnoopingSummary
        * Added 'show platform software fed {switch_var} {state} ipv6 mld snooping summary' command and schema for the command.
    * Added ShowPlatformSoftwareFedSwitchActiveipecrexactroutesourceipdestinationip
        * show platform software fed switch {type} ip ecr exact-route {sourceip} {destinationip} {sourceport} {destinationport} {protocol}
            * show platform software fed switch {type} ip ecr exact-route {sourceip} {destinationip}
    * Added ShowPlatformHardwareFedPortPrbscmdSchema
        * Added parser for show platform hardware fed {switch} {mode} npu slot 1 port {port_num} prbs_cmd {num}
    * Added ShowPlatformHardwareFedPrbsPolynomialSchema
        * Added parser for show platform hardware fed switch {mode} npu slot 1 port {port_num} prbs_polynomial {num}
    * Added ShowPlatformHardwareFedloopbackSchema
        * Added parser for show platform hardware fed switch {mode} npu slot 1 port {port_num} loopback {num}
    * Added ShowPlatformHardwareFedeyescanSchema
        * Added parser for show platform hardware fed switch {mode} npu slot 1 port {port_num} eye_scan
    * Added ShowPlatformSoftwareFedSwitchActivePuntPacketCapturedisplayFiltericmpv6Brief
        * Added schema and parser for 'show platform software fed switch active punt packet-capture display-filter icmpv6 brief'
    * Added ShowPlatformHardwareFedSwitchActiveFwdasicdropsasic
        * show platform hardware fed switch {switch} fwd-asic drops asic {asic}

* nxos
    * Added ShowNveEthernetSegmentSummary
        * show nve ethernet-segment summary
        * show nve ethernet-segment summary esi {esi_id}
    * Added ShowNveEthernetSegment
        * show nve ethernet-segment esi {esi_id}


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowLispEthernetARSubscriber
        * Introduced the ShowLispEthernetARSubscriber parsers.
    * Added ShowLispEthernetARPublisher
        * Introduced ShowLispEthernetARPublisher parsers.
    * Added ShowLispEthernetMapCachePrefixAR
        * Introduce ShowLispEthernetMapCachePrefixAR parser.