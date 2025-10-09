--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxr
    * Modified ShowProcesses
        * Added support for the option 'location'
    * Modified ShowL2vpnXconnectDetail
        * Added support for parsing the line "Flow Label flags configured (Tx=1,Rx=1), negotiated (Tx=1,Rx=1)"
    * Modified ShowIpSourceBinding
        * Modified regex pattern to support lease if infinite

* iosxe
    * Modified ShowLispInstanceIdService
        * Modified regex pattern to support a variant of the output
    * Fixed parser ShowIpv6PimBsrElection
        * Added support for parsing "This system is the Bootstrap Router (BSR)"
        * Updated schema to include 'bsr_system' under 'bsr' for Bootstrap Router detection
        * Enhanced parser to capture and store the 'bsr_system' information
    * Modified parser ShowIpMroute
        * Updated regex pattern p3_1 to accomodate various outputs
        * Added optional key 'iif_mdt_ip' to schema
    * Modified ShowDeviceTrackingDatabaseMacMacDetails parser
        * Modified entries regex pattern
    * Modified ShowDeviceTrackingDatabaseMac parser
        * Modified parser and schema to support device tracking database mac for different vlans
    * Fix parser ShowDeviceTrackingDatabaseMacDetails
        * New revision handles handles extracting primary vlan
    * Fixed ShowPlatformSoftwareFedSwitchActiveSecurityFedSisfStatistics parser
        * Added support command should work for all the platforms.
        * Added clear command support for 'show platform software fed switch {active} security-fed sisf statistics {clear}'.
    * Modified ShowPlatformSoftwareFedSwitchActiveIfmInterfacesLabel
        * Added new cli command 'show platform software fed switch active ifm interfaces virtualportgroup'
        * Added new cli command 'show platform software fed active ifm interfaces virtualportgroup'
        * Added new cli command 'show platform software fed switch {mode} ifm interfaces ethernet'
        * Added new cli command 'show platform software fed active ifm interfaces ethernet'
        * Added new cli command 'show platform software fed switch active ifm interfaces loopback'
        * Added new cli command 'show platform software fed active ifm interfaces loopback'
    * Modified ShowPlatformSoftwareFedSwitchActiveIFMMappingsEtherchannel
        * Added command parameter to support new way of assiging the variables to the command
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveIfmInterfacesLabel
        * show command "show platform software fed switch active ifm interfaces detail" was hitting this parser
    * Modified Parser ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfPorts
        * Supported CLIs
            * `show platform hardware fed {switch} {state} fwd-asic insight vrf_ports_detail`
            * `show platform hardware fed {switch} {state} fwd-asic insight vrf_ports`
        * Introduced `state` as a variable for flexibility.
    * Modified Parser ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfRouteTable
        * Supported CLI
            * `show platform hardware fed {switch} {state} fwd-asic insight vrf_route_table`
        * Introduced `state` as a variable for flexibility.
    * Modified ShowPowerInlineModule
        * Modified the regex pattern
    * Modified ShowLicenseAll
        * Enhanced the parser code to handle the trust_code_installed field more effectively
    * Modified ShowVersion
        * Added handling for merged boot line on c9500x
    * Fixed parser ShowLispMapCacheSuperParser
        * Added support for parsing more date and time formats
    * Modified ShowPolicyMapTypeInspectZonePair
    * Added show policy-map type inspect zone-pair in-self cli
    * Modified ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL2MirrorCommandErspan parser
        * Modified parser for CLI
            * 'show platform hardware fed switch {switch_type} fwd-asic insight l2_mirror_command_erspan({mirror_gid})',
            * 'show platform hardware fed {switch} {switch_type} fwd-asic insight l2_mirror_command_erspan({mirror_gid})'
    * Added  ShowPlatformHardwareQfpActiveFeatureBfdDatapathSession parser
        * Added schema and parser for 'show platform hardware qfp active feature bfd datapath session'
    * Fixed parser ShowPlatformSoftwareFedMatmMacTable parser
        * Modified the parser to handle the output of the command "show platform software fed switch {switch_var} mac address-table" correctly.
        * Modified schema and parser to handle the output of the command "show platform software fed switch {switch_var} mac address-table" correctly.
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveSecurityFedArpIf parser
        * Added schema and regex pattern p9 and p10 to match the output of the command.
    * Fixed parser ShowPlatformSoftwareFedSwitchStateIfmIfIdIf_id
        * Added "show platform software fed switch {switch_num} ifm if-id {if_id}" to the command
    * Fixed  ShowPlatformHardwareFedSwitchActiveFwdAsicInsightRoutes parser
        * Fixed parser to work on any switch id
    * Fixed  ShowPlatformSoftwareFedSwitchActiveOifsetUrid parser
        * made the switch_id optional and made optional in schema
    * Fixed  ShowPlatformSoftwareFedSwitchActiveOifset parser
        * Fixed parser to work on any switch id
    * Fixed ShowPlatformSoftwareFedSwitchActiveIpMfibVrf parser
        * Fixed schema and added regex to match output for any number of asics
    * Modified ShowLicenseTechSupport
        * Modified the regex pattern
    * Fixed ShowPlatformSoftwareFedQosInterfaceSuperParser parser
        * Added new way of parsing cli with command option
    * Added  ShowPlatformHardwareQfpActiveFeatureAlgStatistics parser
        * Added schema and parser for 'show platform hardware qfp active feature alg statistics'
    * Modified ShowXfsuStatus
        * Added optional argument 'xfsu_platform_status' to capture "xFSU PLATFORM Status Stack reloaded, all nodes connected"
        * Made other variables optional to avoid KeyError
    * cat9k
        * fixed parser ShowL2ProtocolTunnelSummary - initialised port_dict
    * Modified ShowIpDhcpSnooping
        * Modified the regex pattern
    * Modified ShowPlatformSoftwareFedActiveMonitor
        * Made "encap" optional
    * Fix parser ShowCtsPolicyServerDetails
        * Modified regex pattern
    * Modified ShowPlatformHardwareFedSwitchActiveFwdAsicInsightSdkObjects parser
        * Added support cli to work on all platforms
    * Modified ShowPlatformHardwareFedSwitchActiveFwdAsicInsightSdkObject parser
        * Added support cli to work on all platforms

* <nxos>
    * Modified ShowBgpSessions
    * Updated regex pattern <p6_1> to accommodate port-channel neighbors

* nxos
    * Modified the DPU name and model in show module
        * DPU name has changed from SAM to DPU.
        * DPU module has changed from Service Accelerator Module to DPU.
    * Show module values are taken from non rv1/show_platform.py
        * Updated the rv1/show_platform.py and show_platform.py same for 'show module'
    * Fixed the 'show inventory' slot for FAN
        * FAN slot is returning as None as the definition there twice.

* viptela
    * Modified ShowSystemStatus parser to cast engineering_signed to boolean.
    * Added logic to safely convert string true/false values to Python bool.
    * Ensures schema validation passes for engineering_signed field.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformHardwareFedSwitchL2SwitchMacTable parser.
        * Added parser for cli show platform hardware fed switch {switch_no} fwd-asic insight l2_switch_mac_table({vlan_or_switch_gid}).
    * Added Parser 'ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfHostRoute'
        * 'show platform hardware fed {switch} {state} fwd-asic insight vrf_host_routes'
    * Added Parser 'ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfForUsRoute'
        * 'show platform hardware fed {switch} {state} fwd-asic insight vrf_for_us_routes'
    * Added Parser 'ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfNextHop'
        * 'show platform hardware fed {switch} {state} fwd-asic insight vrf_next_hops'
    * Added ShowPlatformSoftwareMplsFpActiveEos
        * Added schema and parser for 'show platform software mpls fp active eos'
    * Added ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSmtp
        * show platform hardware qfp active feature alg statistics smtp
        * show platform hardware qfp active feature alg statistics smtp {clear}
    * Added ShowEthernetCFMEFDMeps parser
        * Added schema and parser for 'show ethernet cfm efd meps'
    * Added ShowPlatformSoftwareFedSwitchActiveSecurityFedDhcpSnoopVlanDetail parser
        * Added schema and parser for 'show platform software fed switch {active} security-fed dhcp-snoop vlan {vlan} detail' command.
    * Added ShowPlatformDhcpSnoopingClientStats parser
        * Added schema and parser for 'show platform dhcp snooping client stats' command.
    * Added ShowIpv6PimNeighborIntf
        * Added schema and parser for 'Parser for show ipv6 pim neighbor {interface}'
    * Added 'show crypto pki crls' parser.
    * Added parser for cli 'show crypto pki crls'.
    * Added 'show crypto pki crls download' parser.
    * Added parser for cli 'show crypto pki crls download'.
    * Added ShowPlatformHardwareQfpActiveFeatureNatDatapathStats
        * Added schema and parser for 'show platform hardware qfp active feature nat datapath stats'
    * Added ShowPlatformHardwareQfpActiveFeatureFirewallMemory
        * Added schema and parser for 'show platform hardware qfp active feature firewall memory'
    * Added ShowIpNatTranslationUdpTotal
        * show ip nat translation udp total
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfProperties
        * Added schema and parser for'show platform hardware fed switch active fwd asic insight vrf properties'
    * Added ShowPlatformHardwareQfpActiveInterfaceIfName
        * Added schema and parser for 'show platform hardware qfp active interface if-name Port-channel1'
    * Added ShowPlatformSoftwareFedSwitchIpv6MldSnoopingGroup
        * Added schema and parser for
            * 'show platform software fed {switch} {state} ipv6 mld snooping group'
    * Added show loggging count
    * Added ShowPlatformSoftwareNatFpActiveQfpStats parser
        * Added schema and parser for 'show platform software nat fp active qfp-stats'
    * Added ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableUsage parser
        * Added rv1 schema and parser for 'show platform software access-security table usage'
    * Added ShowPlatformHostAccessTableIntf parser
        * Added rv1 schema and parser for 'show platform host access-table <interface>'
    * Added ShowIpVirtualReassemblyInterface parser
        * Added schema and parser for the command 'show ip virtual-reassembly {interface}'
    * Added ShowPlatformSoftwareFedSwitchActiveIpTypeMfibVrfDetail parser
        * Added schema and parser for cli 'show platform software fed {switch} {active} {ip_type} mfib vrf {vrf_name} {group} {source} detail'
    * Added ShowIpDhcpSnoopingBinding parser
        * Added latest ShowIpDhcpSnoopingBinding parser in rv1 and reverted the changes in original file.
    * Added ShowMerakiConfigMonitor parser
        * Added schema and parser for cli 'show meraki config monitor'
    * Added ShowMerakiConfigUpdater parser
        * Added schema and parser for cli 'show meraki config updater'
    * Added ShowMerakiMigration parser
        * Added schema and parser for cli 'show meraki migration'
    * Added ShowRunningConfigFlowMonitorExpand parser
        * Added schema and parser for 'show running-config flow monitor {monitor_name} expand' command.
    * Added ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSunrpc
        * show platform hardware qfp active feature alg statistics sunrpc
        * show platform hardware qfp active feature alg statistics sunrpc {clear}
    * Added ShowPlatformSoftwareNatFpActiveInterface
    * 'show platform software nat fp active interface'
    * Added ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadBalanceMacAddr parser
        * Added schema and parser for CLI commands
            * 'show platform software fed {switch} {switch_type} etherchannel {eth_channel_id} load-balance mac-addr {src} {dst}'
            * 'show platform software fed {switch_type} etherchannel {eth_channel_id} load-balance mac-addr {src} {dst}'
    * Added ShowPlatformHardwareQfpActiveFeatureNatDataStats
        * Added 'show platform hardware qfp active feature nat data stats' command and schema for the command.
    * Added ShowPlatformSoftwareFedSwitchIpv6MldSnoopingGroupsVlan
        * Added schema and parser for
            * 'show platform software fed {switch} {state} ipv6 mld snooping groups vlan {vlan_id}'
    * Added ShowPlatformSoftwareMemoryDatabaseForwardingManager
    * 'show platform software memory database forwarding-manager {slot} active brief | include {options}'
    * Added ShowPlatformSoftwareFedOifsetL2m parser
        * Added schema and parser for CLI
            * 'show platform software fed {switch} {module} oifset l2m'
            * 'show platform software fed {switch} {module} oifset l2m hash {hash_data}'
    * Added  ShowPlatformHardwareFedSwitchActiveFwdAsicInsightAclEthPortSpecialLkupOrder
        * Added schema and parser for cli "show platform hardware fed switch active fwd-asic insight acl_eth_port_special_lkup_order()
    * Added ShowPlatformSoftwareFedActiveSdmFeature parser
        * Added schema and parser for 'show platform software fed active sdm feature'
    * Fixed ShowSdmPreferred parser
        * Added schema and parser for 'show sdm preferred' to handle qos_acl_in and qos_acl_out as optional fields
    * Added  ShowPlatformHardwareFedSwitchFwdAsicInsightL3mGroups parser
        * Added schema and parser for cli "show platform software fed switch {swith_id} fwd-asic insight l3m-groups"
    * Added ShowPlatformSoftwareFedSecurityArpSnoopVlan parser
        * Added schema and parser for 'show platform software fed switch security-fed arp-snoop vlan {vlan}'
    * Added ShowPlatformSoftwareFedSecurityArpSnoopStats parser
        * Added schema and parser for 'show platform software fed switch security-fed arp-snoop statistics'
    * Added ShowApphostingUtil parser
        * Added schema and parser for 'show app-hosting utilization appid {appid}' command.
    * Added ShowHwModuleSubslotAllOir
    * show hw-module subslot all oir
    * Added ShowIpSlaConfiguration parser
        * Added schema and parser for cli 'show ip sla configuration'
    * Added ShowIpNatTranslationFilterRange
    * show ip nat translation filter range inside global 5.1.1.2 5.1.1.2 total
    * Added ShowIpSubscriberMac parser
        * Added schema and parser for 'show ip subscriber mac {mac_address}'
    * Added  ShowParameterMapTypeSubscriberAttributeToService parser
        * Added schema and parser for cli "show parameter-map type subscriber attribute-to-service name {template_name}"
    * Added ShowFlowInterface parser
        * Added schema and parser for 'show flow interface' command.
    * Added ShowPlatformSoftwareFedSwitchFnfProfileMapsDump parser
        * Added schema and parser for cli 'show platform software fed switch {switch_num} fnf profile-maps-dump'
    * Added show platform software fed switch acl man key profile egress all
    * Added ShowSoftwareAuthenticityKeys schema and parser
        * Added schema and parser for show software authenticity keys
    * Added ShowPlatformSoftwareFedQosInterfaceIngressSdkDetailedAsicAll parser
        * Added parser for cli "show platform software fed {switch} {mode} qos interface {interface} ingress sdk detailed asic {asic}"
        * Added parser for cli "show platform software fed {mode} qos interface {interface} ingress sdk detailed asic {asic}"
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightGroupMembers
        * Added schema and parser for
            * 'show platform hardware fed switch active fwd-asic insight l3m_group_members'
            * 'show platform hardware fed switch active fwd-asic insight l2m_group_members'
    * Added ShowPlatformSoftwareInterfaceFpActive
        * Added schema and parser for 'show platform software interface fp active name Port-channel32'
    * Added ShowIpv6MfibVrfSummary parser
        * added schema and parser for cli 'show ipv6 mfib vrf {vrf_name} summary'
    * Added show platform software fed switch acl man key profile ingress all
    * Added ShowPlatformSoftwareMulticastStats parser
        * Added schema and parser for 'show platform software multicast stats'
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightL2mGroupMembers parser
        * Added schema and parser for cli "show platform hardware fed {switch} {module} fwd-asic insight l2m_group_members"
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightL3mGroupMembers parser
        * Added schema and parser for cli "show platform hardware fed {switch} {module} fwd-asic insight l3m_group_members"
    * Added ShowPlatformHardwareQfpActiveFeatureIpsecState
        * Added schema and parser for 'show platform hardware qfp active feature ipsec state'
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightL2AttachmentCircuitL2 parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight l2_attachment_circuit_l2({sys_port_gid}).
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightL2AttachmentCircuitL2Detail parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight l2_attachment_circuit_l2_detail({l2_ac_gid}).

* iosxr
    * Added ShowControllersOpticsDb
        * show controllers optics {port} db
    * Added ShowProcessesBlocked
        * show processes blocked
    * Added ShowInventoryRaw
        * show inventory raw
    * Added ShowControllersOpticsFecThresholds
        * show controllers optics {port} fec-thresholds
    * Added ShowControllersOpticsBreakoutDetails
        * show controllers optics {port} breakout-details
    * Added ShowControllersOpticsDwdmCarrierMap
        * show controllers optics {port} dwdm-carrier-map

* linux
    * Added CurlMinusV parser class
        * Parse "curl -V"


