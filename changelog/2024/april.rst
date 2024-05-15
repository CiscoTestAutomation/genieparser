--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowSmartPowerChildren
    * Added ShowSmartPowerUsage
    * Modified ShowStackPowerDetail Parser
    * New ShowPowerInlineMeter
        * Parser for 'show power inline meter'
    * Added New Parser ShowSmartPowerCategories
    * Added ShowControllerEthernetControllerLinkstatus
        * Added schema and parser for 'show controllers ethernet-controller {interface} link-status'
    * Added value for line key
    * Added ShowLoggingOnboardRpStandbyUptimeDetail Parser
        * Added cli for show logging onboard rp standby uptime detail in the parser.
    * Added ShowPlatformHardwareChassisFantrayDetail
        * Added 'show platform hardware chassis fantray detail parser'
    * Added ShowSmartPowerLevelCurrentChildren
    * Added ShowMacsecPost
        * parser for 'show macsec post'
    * Added ShowMacsecStatisticsInterface
        * parser for 'show macsec statistics interface {interface}'
    * Added TestPlatformSoftwareDatabasePlatformComponent
        * Added schema and parser for 'test platform software database get-n all ios_oper/platform_component'
    * Added ShowPlatformHardwareChassisFantrayDetailSwitch
        * show platform hardware chassis fantray detail switch {mode}
    * Added ShowSdwanServiceChainDatabaseSummary parser
        * Parser for "show platform software sdwan service-chain database summary"
    * Added ShowSdwanServiceChainStatsDetail parser
        * Parser for "show platform software sdwan service-chain stats detail"
    * Added ShowSdwanQfpActiveDatapathStats parsser
        * Parser for "show platform hardware qfp active feature sdwan datapath statistics"
    * Added ShowPlatformHardwareFedActiveFwdasicdrops
        * Added schema and parser for 'show platform hardware fed {switch} {switch_var} fwd-asic drops asic {asic_id} slice {slice_id}'
        * Added schema and parser for 'show platform hardware fed {switch_var} fwd-asic drops asic {asic_id} slice {slice_id}'
    * Added ShowPlatformHardwareFedActiveFwdAsicTrapsNputraps
        * parser for ShowPlatformHardwareFedActiveFwdAsicTrapsNputraps
    * Added ShowPlatformHardwareFedActiveFwdAsicTrapsTMtraps
        * parser for ShowPlatformHardwareFedActiveFwdAsicTrapsTMtraps
    * Added ShowPlatformSoftwareFedActiveDropPacketCaptureInterfacesStats
        * parser for ShowPlatformSoftwareFedActiveDropPacketCaptureInterfacesStats
    * Added ShowPlatformSoftwareFedActiveDropPacketCaptureStatistics
        * parser for ShowPlatformSoftwareFedActiveDropPacketCaptureStatistics
    * Added ShowIsisIpv6Tilfa
        * show isis ipv6 fast-reroute ti-lfa fwd-ids
        * show isis ipv6 fast-reroute ti-lfa fwd-ids {fwd_id}
    * Added ShowPlatformSoftwareCpmSwitchActiveB0CountersInterfaceLacp
        * Added parser for "show platform software cpm switch active B0 counters interface lacp" and schema
    * Added ShowPlatformFedSwitchActiveFnfRecordCountAsicNum
        * parser for 'show platform software fed switch <state> fnf record-count asic <asic num>'
        * parser for 'show platform software fed <state> fnf record-count asic <asic num>'
    * Added ShowIpDhcpSnoopingStatistics
        * parser for 'show ip dhcp snooping statistics'
    * Added ShowPlatformFedSwitchActiveWiredClientR0IdIifid
        * parser for 'show platform software wired-client switch <state> r0 id <iif_id>'
        * parser for 'show platform software wired-client <state> r0 id <iif_id>'
    * Added ShowPlatformHardwareFedQosSchedulerSdkInterface
        * parser for 'show platform hardware fed {mode} qos scheduler sdk interface {interface}'
    * Added ShowInterfaceHumanReadable parser
        * Parser for "show interface <interface> human-readable"
    * Added ShowEndpointTracker parser
        * Parser for "show endpoint-tracker"
    * Added ShowTrackDynamic parser
        * Parser for "show track dynamic"
    * Added ShowIpIgmpSsm
        * Added 'show ip igmp ssm-mapping' command and schema for the command.
    * Added ShowIpv6MldSsm
        * Added 'show ipv6 mld ssm-map' command and schema for the command.

* iosxr
    * Added support for ShowDiagDetails
    * Added support for ShowIpv4VirtualAddressStatus
    * Added new cli support for ShowRouteIpv4
        * show route ipv4 next-hop {next_hop}
    * Added parser for 'show line'
    * Modified ShowOspfNeighborInterfaceDetail Parser
        * parser for 'show ospf neighbor {interface} detail'
    * Added ShowIsisDatabaseVerboseNeighbor
        * Added schema and parser for show isis instance {instance_name} database verbose {neighbor_device}
    * Added ShowSegmentRoutingTrafficEngPolicyColorEndpoint
        * added new parser for cli 'show segment-routing traffic-eng policy color {color_code} endpoint ipv4 {endpoint_ip}'
    * Added ShowDhcpVrfIpStatistics
        * Added schema and parser for show dhcp vrf {vrf_name} {ip_type} {user_command} statistics
    * Added ShowDhcpIpInterface
        * Added schema and parser for cli 'show dhcp {ip_type} {user_command} interface {interface_name}'
    * Added show bgp dampened-paths
        * parser for 'show bgp dampened-paths'

* utils
    * Updated code to generate `_actual.json` for UT
    * Added `blocked` in result colour


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowWirelessClientSummary and ShowWirelessFabricClientSummary
        * Added support for Method of 'None' and 'SAE'
    * Modified ShowPower
        * parser for 'show power detail'
    * Modified ShowPowerInlinePolice
        * parser for 'show power inline police module <mod no>'
    * Modified ShowIpv6Routers Parser
        * Added the condition vrf!="" because even though vrf not provided in script command directing to show ipv6 routers vrf
    * Modified ShowVersion
        * Updated regex to capture build_label for newer version strings
    * Modified TestPlatformSoftwareDatabasePlatformComponent to TestPlatformSoftwareDatabase
        * Modified schema and parser for 'test platform software database get-n all ios_oper/{component}'
    * Modified ShowLoggingOnboardRpActiveUptimeDetail Parser
        * Added switch_num to the parser to support stack/svl devices.
    * Modified ShowSdwanAppqoeDreoptStatus
        * Schema change to support timing based value updation, marked as Optional
    * Modified ShowSslProxyStatistics
        * Added new regex pattern to support new set of lines, with backword compatibity
    * Modified ShowSdwanAppqoeRmResources
        * Added new regex pattern to support new set of lines, with backword compatibity
    * Modified ShowServiceInsertionTypeAppqoeServiceNodeGroup
        * Added new regex pattern to support new set of lines, with backword compatibity
    * Modified ShowServiceInsertionTypeAppqoeClusterSummary
        * Added new regex pattern to support new set of lines, with backword compatibity
    * Modified ShowPlatformHardwareQfpActiveFeatureAppqoe
        * Added new regex pattern to support new set of lines, with backword compatibity
    * Modified ShowPlatform Parser
        * Fix p3 if condition
    * Modified ShowWlanAllSchema
        * Updated `radio_policy` from schema to Optional
    * Modified ShowWlanAll
        * Updated regex pattern `p_name_ssid` to support SSID with spaces
    * Modified ShowWlanSummary
        * Updated regex pattern `wlan_info_capture` to support SSID with spaces (2 spaces max between each word)
    * Modified ShowLispPublicationPrefixSuperParser
        * Updated regex to capture IPv6 Merged Locator addresses.
    * Modified ShowCdpNeighborsDetailSchema in show_cdp.py
        * Added keys <power_drawn>, <power_request_id>, <power_mgmt_id_1>, <power_req_level>, <power_available_id>, <power_mgmt_id_2>, <available_power>, <mgmt_power> into the schema.
    * Modified ShowCdpNeighborsDetail in show_cdp.py
        * Added parsing code for the keys <power_drawn>, <power_request_id>, <power_mgmt_id_1>, <power_req_level>, <power_available_id>, <power_mgmt_id_2>, <available_power>, <mgmt_power>.
    * Modified ShowPlatformHardwareFedActiveQosQueueStats
        * Modified to support current output of c9400 platform
        * Two keys (q_policer and q_policer_drop) are changed to optional
    * Modified ShowCapabilityFeatureMonitorErspanSourceDestination Parser
        * Fix p1_3 regular expression
    * Modified ShowDeviceTrackingDatabaseInterfaceCount
        * parser for ShowDeviceTrackingDatabaseInterfaceCount
    * Modified ShowEnvironmentStack
        * Removed trailing whitespace from empty_output_output.txt file
    * Modified ShowPlatformSoftwareFedIgmpSnooping
        * Removed trailing whitespace from empty_output_output.txt file
    * Modified ShowPlatformSoftwareFedActiveIpv6MldSnoopingVlan
        * Removed trailing whitespace from empty_output_output.txt file
    * Modified ShowIpDhcpBindingActiveCount
        * Removed invalid directory
    * Modified ShowMacsecSummary
        * Modified p1 regex to match subinterfaces and portchannnel interfaces
    * Modified ShowLicenseUdi
        * Updated to support stackable platforms with more than 4 switches (2 members) in the stack
    * Modified ShowLicenseAll
        * Updated to support stackable platforms with more than 4 switches (2 members) in the stack
    * Modified ShowLicenseTechSupport
        * Updated to support stackable platforms with more than 4 switches (2 members) in the stack
        * Fixed regexp p14_data1 to match "Trust Code Installed" in single switch
        * Added a new key other_info.smartagentmaxsinglereportsize
    * Added <ShowCryptoKeyMypubkeyRsaKeyName>, <ShowCryptoKeyMypubkeyEcKeyName>
        * Added support for <key_name> in <show crypto key mypubkey ec {key_name}> and <show crypto key mypubkey rsa {key_name}>
    * Modified ShowRouteMapAll
        * Fixed regex pattern p21 to support as-path prepend with '.'.
        * Added new golden output txt and expected.py with as-path prepend.
    * Modified ShowIsisIpv6RibParser
        * Output of parser changed, srv6 sid behavior details got added.

* iosxr
    * Modified fix for ShowInstallActiveSummary
        * Added schema and code for fix the new output

* nxos
    * Modified the show interface status pattern.
        * Modified the regexp p1 to match user data status "linkFlapE".


