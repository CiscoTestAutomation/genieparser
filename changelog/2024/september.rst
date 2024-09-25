--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowBgpNeighborsReceivedRoutesSuperParser
        * Make optional to handle regex without CICD
    * Modified ShowInterfaces
        * Added <in_drops>, <out_drops>, <peer_ip> and <vc_id> into schema as Optional.
        * Renamed regex pattern <p_cd>, <p_cd_2> to <p54>, <p55> respectively and updated the code accordingly.
        * Added regex pattern <p1_2>, <p6_1>, <p56>, <p57> and <p58> to accommodate various outputs.
    * Modified ShowIpRouteWord
        * Updated regex pattern <p2> to accommodate various outputs.
    * Modified ShowSdwanOmpSummary
        * Added the new fields in schema to match the output
    * Modified ShowPlatformSoftwareFedSwitchActiveVtAll
        * Added CLI without Switch keyword too in the CLI list.
    * Modified ShowInterfacesTransceiver
        * parser for 'show interfaces transceiver'
    * Modified fix for auto off addition
        * Replaced ecomode with auto-off due to new cli
    * Modified ShowIPVerifySource
        * Fixed regular expressions p1 to match filter_type which is 'ip'
    * Added ShowRepTopologyDetail
        * show rep topology detail
    * Modified ShowMeraki
        * Updated the P2 regex based on the latest output at line number 70.
    * Modified ShowSpanningTreeSummaryTotals
        * Made "portfast_bpdu_guard" and "portfast_bpdu_filter" optional and
    * Modified ShowVersion
        * c9500 Added schema key 'bootldr' to match the schema of the iosxe parser.
    * Modified ShowRedundancyStates
        * Made rf_debug_mask variable as optional and unit test added
    * Modified fix for ShowEthernetTags
        * Updated the interface variable, now uses the correct OS-specific format.when converting the interface name.
    * Modified ShowPolicyMapControlPlaneClassMap parser.
        * added extra regx. for burst_pkt pattern.
    * Modified ShowLispIpMapCachePrefixSuperParser
        * Changed <locators> key from schema to Optional.
    * Modified ShowPlatformSoftwareFedActiveAclInfoDbDetail
        * Added commands 'show platform software fed {mode} acl info db detail' and 'show platform software fed {switch} {mode} acl info db detail {acl_name}' under iosxe
    * Modified ShowPlatformSoftwareFedActiveAclInfoDbDetail
        * Added commands 'show platform software fed {mode} acl info db detail' and 'show platform software fed {switch} {mode} acl info db detail {acl_name}' under c9350
        * fixed reg ex p1 for 'show platform software fed {mode} acl info db detail' under c9350
    * Modified ShowMonitor
        * Removed un-necessary cli command from ShowMonitor parser.
    * Modified fix for ShowLispRegistrationHistory
        * Reverted the changes due to the CLI index issue
    * Modified fix for ShowPlatformHardwareFedQosSchedulerSdkInterface
        * Modified 'rate' as string from 'int' under 'svcse_scheduler' and added unit test to support the same.
    * Modified ShowAPSummary
        * Updated regex pattern <ap_ip_address> to accommodate IPv6 address.
    * Modified ShowAPDot115ghzChannel
        * Updated regex pattern <lead_auto_chan_assn_capture> to accommodate Local or Leader words based on release.
        * Made last_run_seconds as Optional key.
    * Modified fix for ShowPowerDetail
        * Replaced ecomode with auto off to accomodate CLI change
    * Added support for Stack total input power variable
        * Added 'stack_total_input_power' in the schema
    * Modified ShowPlatformSoftwareFedSwitchActiveAclStatisticsEvents
        * Made switch and mode optional variables.
    * Modified ShowPlatformSoftwareFedSwitchActiveAclInfoDbSummary
        * Made switch and mode optional variables.
    * Modified ShowCtsRoleBasedSgtMapAll
        * Added optional argument total_cached
    * Modified fix for ShowLispInstanceIdService
        * database value is present in Publication_entries_exported and Publication (Type - Config Propagation)
        * database value was overriden by the second occurence hence added a flag to avoid the overriding issue
    * Modified ShowProcessesMemorySorted
        * Made "reserve_p_pool" as optional field.

* iosxr
    * Modified fix for ShowRplRoutePolicy
        * Modified the 'as-path in' block in p19.match to correctly capture the 'as-path in' data
    * Modified MonitorInterface
        * Added missing empty_output_arguments.json files
    * Modified ShowBundle
        * Modified <wait_while_timer_ms> in schema to store either integer or string value.
        * Modified regex pattern <p9> to capture either integer or string value.
    * Modified ShowL2vpnXconnect
        * Updated regex pattern <p3> and <p6> to accommodate various outputs.

* viptela
    * Modified ShowOmpSummary
        * Added the new fields in schema to match the output

* nxos
    * Modified ShowVrfAllInterface
        * Updated regex pattern <p1> to accommodate various outputs which may contain underscore (_) as well.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareFedIpMfibVrfGroupDetail
        * Added schema and parser for 'show platform software fed switch active ip mfib vrf vrf_name group detail'
    * Added ShowL2vpnEvpnEsiMlagSummary
        * Introduced ShowL2vpnEvpnEsiMlagSummary parsers.
    * Added ShowL2vpnEvpnEsiMlagMacIP
        * Introduced ShowL2vpnEvpnEsiMlagMacIP parsers.
    * Added ShowL2vpnEvpnEsiMlagVlanBrief
        * Introduced ShowL2vpnEvpnEsiMlagVlanBrief parsers.
    * Added ShowPlatSoftFedSwAccessSecuritySecMacLrnTable parser.
        * Added parser for cli show plat soft fed sw {switch} access-security sec-mac-lrn-table summary.
        * Added parser for cli show plat soft fed sw {switch} access-security sec-mac-lrn-table mac {client_mac}.
        * Added parser for cli show plat soft fed sw {switch} access-security sec-mac-lrn-table interface if-id {if_id}.
    * Added ShowPlatformSoftwareFedSwitchNumberIfmMappingsLpn
        * Added schema and parser for 'Show Platform Software Fed Switch Number Ifm Mappings Lpn' under c9300
    * Added ShowHardwareLed
        * Added schema and parser for 'show hardware led' under c9610
    * Added ShowPlatformHardwareFedSwitchQosQueueConfigInterfaceQueueInclude
        * Added 'show platform hardware fed switch {sw_number} qos queue config interface {interface} queue {queue_id} | include {match}' command and schema for the command.
    * Added ShowPlatformSoftwareFedActiveAclInfoDbDetail
        * Added schema and parser for 'show platform software fed {mode} acl info db detail' under c9610
    * Added ShowPlatformSoftwareFedSwitchActiveAclinfoSdkDetail parser.
        * Added parser for cli 'show platform software fed switch {switch_var} acl info sdk detail'.
        * Added parser for cli 'show platform software fed switch {switch_var} acl info sdk feature {feature_name} detail'.
        * Added parser for cli 'show platform software fed switch {switch_var} acl info sdk feature {feature_name} dir {in_out} cgid {cg_id} detail'.
    * Added show interfaces | include {include}, show ip interface | include {include}, show ipv6 interface | include {include}
    * Added ShowSwitchStackPortSummary
        * Added schema and parser for 'show switch stack-ports summary' under c9350
    * Added ShowPlatformHardwareFedSwitchActiveStandbyFwdAsicInsightNplSummaryDiff
        * show platform hardware fed switch {type} fwd-asic insight npl_summary_diff({f1}, {f2}).
    * Added ShowDeviceTrackingCapturePolicy parser.
        * Added parser for cli show device-tracking capture-policy.
        * Added parser for cli show device-tracking capture-policy interface {interface_name}'.
        * Added parser for cli show device-tracking capture-policy vlan {vlan_id}.
    * Added ShowPlatformSoftwareFedIpMfibVrfCount
        * Added 'show platform software fed {switch_var} {state} ip mfib vrf {vrf_name} count' command and schema for the command.
    * Added ShowPlatformSoftwareFedIpIgmpSnoopingSummary
        * Added 'show platform software fed {switch_var} {state} ip igmp snooping summary' command and schema for the command.
    * Added ShowPlatformSoftwareFedMldSnoopingIpv6GroupsCount
        * Added 'show ipv6 mld snooping address vlan {vlan} {group} summary' command and schema for the command.
    * Added ShowPrpChannelDetails
        * Added schema and parser for show prp channel detail
    * Added ShowPlatformSoftwareInterfaceF0Name
        * Added 'show platform software interface f0 name {intf}' command and schema for the command.
    * Added ShowPlatformSoftwareObjectManagerF0ObjectDownlinks
        * Added 'show platform software object manager f0 object down links' command and schema for the command.
    * Added ShowPlatformSoftwareInfrastructureInject parser
        * Added parser for cli show platform software infrastructure Inject
    * Added ShowIpNbarProtocolPackActive
        * Added show show ip nbar protocol-pack active

* nxos
    * Modified ShowNveVni
        * show nve vni {vni}
    * Added show interface {interface} | include {include}, show interface | include {include} to show interface

* added showplatformhardwarefedswitchqosschedulerinterfaceinclude
    * Added schema and parser for 'show platform hardware fed switch {sw_number} qos scheduler interface {interface} | include {match}'

* added showplatformhardwarefedswitchqosinterfaceingressndpdetailedinclude
    * Added schema and parser for 'show platform software fed switch {sw_number} qos interface {interface} ingress npd detailed | include {match}'


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformFedActiveTcamUtilization
        * Added parser for show platform software fed switch active tcam utilization parser for c9610