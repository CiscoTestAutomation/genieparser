--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added Parser for parsers for below commands
        * show platform hardware qfp active feature firewall drop clear
        * show platform hardware qfp active feature firewall datapath scb any any any any any all any
        * show platform hardware qfp active feature firewall datapath scb any any any any any all any detail
    * Added Show pki commands
        * show crypto pki counters
        * show crypto pki trustpool count downloaded
        * show monitor event-trace crypto pki event all
        * show logging process ios module pki level notice
        * show monitor event-trace crypto pki error all
        * show platform software trace level ios rp active | in pki
    * Added ShowDebug
        * Added  schema and parser for 'show debug' command.
    * Added ShowEnvironmentalTemperatureAll
        * Added  schema and parser for 'show environmental temperature all' command.
    * Added Parser for show facility-alarm relay major
        * Added a new schema and parser for the show facility-alarm relay major command.
    * Added ShowPlatformDiag
        * show platform diag
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightSanetClientDefinition parser
        * Added schema and parser for show platform hardware fed switch active fwd asic insight sanet client definition
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightSanetClientAcl parser
        * Added schema and parser for show platform hardware fed switch active fwd asic insight sanet client acl
    * Added Parser for parsers for below commands
        * show policy-firewall config
        * show policy-firewall config zone-pair in-out
    * Modified show inventory parser
        * Modified the regex patterns to support new output format
    * Modified show platform resources parser
        * Modified the parser schema to support new output format
    * Added ShowPlatformHardwareQfpActiveFeatureAlgStatisticsDns
        * show platform hardware qfp active feature alg statistics dns
        * show platform hardware qfp active feature alg statistics dns {clear}
    * Added ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSmtp
        * show platform hardware qfp active feature alg statistics msrpc
        * show platform hardware qfp active feature alg statistics msrpc {clear}
    * Added ShowPlatformHardwareQfpActiveFeatureAlgStatisticsPop3
        * show platform hardware qfp active feature alg statistics pop3
    * Added ShowPlatformSoftwareNatIpalias
        * show platform software nat ipalias
    * Added ShowMonitorEventTraceCryptoIpsec
        * show monitor event-trace crypto ipsec event latest
        * show monitor event-trace crypto ipsec event back 110
    * Added  ShowMonitorEventTraceCryptoLatestDetail
        * show monitor event-trace crypto latest detail
    * Added ShowMonitorEventTraceCryptoMerged
        * show monitor event-trace crypto merged {word} {lines_count} {detail}
        * show monitor event-trace crypto merged {word} {detail}
        * show monitor event-trace crypto merged {word}
    * Added ShowPlatformHardwareFedActiveFwdAsicInsightHcamUsageSlice Parser
        * Added schema and parser for cli "show platform hardware fed {state} fwd-asic insight hcam_usage(1,1) | begin Slice"
    * Added ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocolsSchema
        * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance ip-fl-nh-port-v6 {sourcemac} {destinationmac}',
        * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance ip-fl-nh-v6 {sourcemac} {destinationmac} {flow_label} {next_header}',
        * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance ip-protocol-port-v4 {source} {destinatio} {protocol} {sour_port} {dest_port}',
        * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance ip-protocol-v4 {source} {destination} {protocol}',
        * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-addr {sourcemac} {destinationmac}',
        * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-fl-nh-port-v6 {sourcemac} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header} {sour_port} {dest_port}',
        * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-fl-nh-v6 {sourcemac} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header}'
        * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-protocol-v4 {sourcemac} {sourceip} {destinationip} {protocol}',
        * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-protocol-port-v4 {sourcemac} {sourceip} {destinationip} {protocol} {sour_port} {dest_port}',
        * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-fl-nh-port-v6 {sourcemac} {vlan_id} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header} {sour_port} {dest_port}',
        * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-fl-nh-v6 {sourcemac} {vlan_id} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header}',
        * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-protocol-port-v4 {sourcemac} {vlan_id} {sourceip} {destinationip} {protocol} {sour_port} {dest_port}',
        * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-protocol-v4 {sourcemac} {vlan_id} {sourceip} {destinationip} {protocol}',
        * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlanid {sourcemac} {vlan_id}'.
    * Added ShowEnvironmentAll schema in iosxe/ie3k
        * Added parser for show environment all in iosxe/ie3k
    * Added ShowEnvironmentPower schema in iosxe/ie3k
        * Added parser for show environment power in iosxe/ie3k
    * Added ShowEnviornmentTemperature schema in iosxe/ie3k
        * Added parser for show environment temperature in iosxe/ie3k
    * Added ShowEnvironmentAlarmContact schema in iosxe/ie3k
        * Added parser for show environment alarm contact in iosxe/ie3k
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicTrapsTmTrapsAsic schema and parser
        * Added parser for show platform hardware fed {switch} {state} fwd-asic traps tm-traps asic {asic}
    * Added show acm rules parser
        * Parse "show acm rules"
    * Added acm replace validate parser
        * Parse "acm replace flashday1 validate"
    * Added  ShowCtsHaSyncStatus parser
        * Added schema and parser for cli "show cts ha sync-status"
    * Added  ShowCtsProvisioningQueue parser
        * Added schema and parser for cli "show cts provisioning queue"
    * Added ShowIpPolicy
        * Add parser for 'show ip policy' in revision 1
    * Added ShowIpv6MfibCount Parser
        * Parser for 'show ipv6 mfib count'
    * Added ShowMacsecStatusInterface
        * Added schema and parser for show macsec status interface {interface}
    * Added show platform hardware fed switch {switch_id} fwd-asic insight ifm_ingress_vlan_member_tbl({npp_attrib_index},{vlan_id},{stp_learn_type},{stp_state_block})
    * Added show platform hardware fed switch {switch_id} fwd-asic insight l2_attachment_circuit_l2(lag_gid={lag_gid})
    * Added supported for zbfw feature for ShowPlatformPacketTracePacket
    * Added ShowPolicyMapTypeInspectZonePairSessions
        * show policy-map type inspect zone-pair {zone_pair_name} sessions
            * show policy-map type inspect zone-pair sessions
    * Added ShowPolicyMapTypeInspectZonePairSession
        * show policy-map type inspect zone-pair {zone_pair_name} session
    * Added ShowFirmwareVersionAll
        * Added schema and parser for 'show firmware version all' command.
    * Added Parser for show interface transceiver properties
        * Added a new schema and parser for the show interface transceiver properties command.
    * Added ShowDiagSubslotEepromDetail
    * 'show diag subslot 0/1 eeprom detail'
    * Added ShowHwModuleSubslotEntity
    * 'show hw-module subslot 0/1 entity'
    * Added Parser ShowIpNatPoolName in show_ip.py
    * show ip nat pool name {pool_name}
    * Added Parser for show loopdetect
        * Added a new schema and parser for the show loopdetect command.
    * Added ShowMplsTrafficEngLinkManagementSummary parser in show_mpls.py
    * Added schema and parser for cli 'show mpls traffic-eng link-management summary'
    * Added ShowNat64MapT parser in show_nat.py
        * Added schema and parser for cli 'show nat64 map-t'
    * Added ShowNat64MapTDomain parser in show_nat.py
        * Added schema and parser for cli 'show nat64 map-t domain <domain_id>'
    * Added ShowNat64MappingsStaticTcp parser in show_nat.py
        * Added schema and parser for cli 'show nat64 mappings static tcp'
    * Added ShowNat64MappingsStaticKeyPort parser in show_nat.py
        * Added schema and parser for cli 'show nat64 mappings static key-port {port}'
    * Added ShowNat64MappingsStaticKeyAddress parser in show_nat.py
        * Added schema and parser for cli 'show nat64 mappings static key-address {address}'
    * Added ShowIpNatLimitsAllHost
    * 'show ip nat limits all-host'
    * Added ShowParameterMapTypeInspectZone
    * 'show parameter-map type inspect-zone {zone_name}'
    * Added show parameter-map type inspect-global parser
    * Added ShowParameterMapTypeInspectVrf
    * 'show parameter-map type inspect-vrf test_vrf'
    * Added ShowPlatformFedStandbyTcamUtilization
        * Parser for 'show platform hardware fed standby fwd-asic resource tcam utilization'
    * Added ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSipClear
    * 'show platform hardware qa active fe alg sta sip clear
    * Added ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSipL7data
        * show platform hardware qfp active feature alg statistics sip l7data
    * Added ShowPlatformSoftwareFirewallRPActiveVrfPmapBinding
        * show platform software firewall RP active vrf-pmap-binding
        * show platform software firewall FP active vrf-pmap-binding
    * Added class ShowPolicyFirewallStatsVrf parser in show_policy_firewall.py
        * Added schema and parser for cli 'show policy-firewall stats vrf {vrf}'
    * Added ShowPolicyFirewallStatsZone parser in show_policy_firewall.py
        * Added schema and parser for cli 'show policy-firewall stats zone {zone}'
    * Added ShowIpWccpWebCacheClients parser in show_ip.py
    * Added schema and parser for cli 'show ip wccp web-cache clients'
    * Added ShowMplsTrafficEngFastRerouteDatabase parser in show_mpls.py
    * Added schema and parser for cli 'show mpls traffic-eng fast-reroute database'

* show platform hardware qfp active feature alg statistics pop3 {clear}

* iosxr
    * Added ShowControllersOpticsAppselActive
        * Added schema and parser for 'show controllers optics {port} appsel active' command.
    * Added ShowImDatabaseBriefLocation
        * Added schema and parser for 'show im database brief location {location}' command.
        * Added schema and parser for 'show im database brief location all' command.


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxr
    * Added  ShowCryptoPkiCertificates in rv1
        * Added  ShowCryptoPkiCertificates in rv1 for supporting multiple ca_certificates

* iosxe
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightAclTableRules parser
        * Added schema and parser for 'show platform hardware fed switch active fwd-asic insight acl-table-rules' command
    * Modified ShowEtherchannelPortChannel parser
        * Added optional keys in schema
    * Added new parser for 'show facility-alarm status' command


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowPlatformFedActiveTcamUtilization parser
        * Added new cli command 'show platform hardware fed active fwd-asic resource tcam utilization {asic} slice-id {slice_id}'
    * Modified ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfPorts parser
        * Split parser into two separate classes for different command formats
    * Modified ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfRouteTable parser
        * Fixed parsing logic to ensure all values from the output are included in the returned dictionary.
        * Improved handling of edge cases and verified parsing against multiple output


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowVersion
        * Added is_standby argument to the parser to execute the show version command on the standby device
    * Modified fix for ShowSoftwareAuthenticityRunning parser.
        * Modified the regex pattern to fetch all the fields'.
    * Modified fix for ShowControllersEthernetControllersPhyDetail parser.
        * Modified the regex to match all necessary patterns'.
    * Modified fix for ShowControllerEthernetControllerLinkstatus parser.
        * Modified the schema to support all the output'.
    * Modified fix for ShowControllerEthernetControllerInterfaceMac parser.
        * Modified the schema to support all the output'.
    * Added ShowPlatformSoftwareCpmSwitchActiveB0PacketsControlIpc parser.
        * Added parser for cli 'show platform software cpm switch {mode} BP {mode2} packets {controlmode} {transmitmode}'.
    * Modified fix for ShowPlatformHardwareFedNpuDscDump parser.
        * Modified the schema to support all the output'.
    * Added ShowPlatformHardwareFedSwitchActiveNpuSlotPortLinkstatus parser.
        * Added parser for cli 'show platform hardware fed switch {mode} npu slot 1 port {port_num} link_status'.
    * Removed ShowPlatformHardwareFedSwitchActiveNpuSlotPortLinkstatus parser.
        * Removed duplicate parser for resolving conflict.
    * Modified ShowApConfigGeneral
        * Modified schema 'show ap config general' to also allow int return type for 'rogue_ap_minimum_rssi'
    * Modified ShowControllersEthernetControllerPortInfo
        * Modified regex p5
    * Added support ShowCryptoIpsecSaDetail
        * Changes made for <p1> regex to match `GigabitEthernet0/0/0`
    * Modified ShowIssuStateDetail parser
        * Fixed regex p19 to capture "In Progress" status
    * Modified ShowPlatformSoftwareFedQosInterfaceSuperParser parser
        * Fixed regex p7 to capture "Asic" number
    * Modified ShowPlatformHardwareFedSwitch1FwdAsicInsightIfmLagMembers parser
        * Modified parser for CLI
            * 'show platform hardware fed switch {switch_id} fwd-asic insight ifm_lag_members({lag_gid})'
            * 'show platform hardware fed {switch} {switch_id} fwd-asic insight ifm_lag_members({lag_gid})'
        * Modified parser for arguments
            * 'switch_id'"1" to 'switch_id'"Any"
        * Modified regex pattern (p1) to correctly handle empty or missing 'sysport_cookie' values, ensuring all LAG members are parsed even if some fields are empty.
        * Added test output for the parser
            * 'show platform hardware fed switch 1 fwd-asic insight ifm_lag_members(lag_gid=263)'
    * Modified ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfProperties parser
        * Modified parser for CLI
            * 'show platform hardware fed switch {switch_type} fwd-asic insight vrf-properties',
            * 'show platform hardware fed {switch} {switch_type} fwd-asic insight vrf-properties'
        * Modified parser for arguments
            * 'switch'"Any" to 'switch_type'"Any"
    * Modified ShowPlatformSoftwareFedSwitchQosPolicyTargetStatus parser
        * fix the logic to handle the cli_command
    * Added few fields to 'show hardware led' command output
    * Fix for show hardware led state
    * Modified ShowAlarmSettings
        * Modified the parser to include the following fields
            * Rep
            * License-File-Corrupt
            * Alarm Logger Level
    * Modified parser ShowPlatformHardwareFedSwitchActiveFwdAsicInsightS1SgtMappingStatusV4 and ShowPlatformHardwareFedSwitchActiveFwdAsicInsightS1SgtMappingStatusV6
        * changed 'switch' and 'mode' as variables for flexibility
    * Modified ShowProcessesPid
        * Updated regex pattern <p1> to allow "-" in the process name.
        * Updated regex pattern <p7> to allow "()" in the process state.
    * Modified parser ShowPlatformSoftwareFedSwitchActiveSecurityFedDhcpSnoopVlanDetail
        * Updated the parser to handle the new output format for DHCP snooping VLAN details.
    * Modified ShowIpNatTranslationUdpTotal
    * 'show ip nat translations {protocol} total'  #Added support to handle both tcp/udp protocol.

* iosxr
    * Modified ShowControllersOptics
        * Added regex for new fields host_squelch_status, media_linkdown_pre_fec_degrade, power_mode, dom_data_status, last_link_flapped, loopback_host, loopback_media & hardware_version
        * Fix regex for 'controller_state' field
    * Modified ShowControllersOptics
        * Added schema and parser for the 'show controllers optics *' command
    * Modified ShowControllersOpticsDb
        * Added schema and parser for the 'show controllers optics * db' command
    * Modified ShowControllersOpticsDwdmCarrierMap
        * Added schema and parser for the 'show controllers optics * dwdm-carrier-map' command
    * Modified ShowControllersOpticsFecThresholds
        * Added schema and parser for the 'show controllers optics * fec-thresholds' command

* nxos
    * Modified ShowNveInterfaceDetail
        * Fixed regex pattern for multisite dci-advertise-pip configuration.
        * Enhanced regex patterns to accommodate whitespace in CLI output.


--------------------------------------------------------------------------------
                                     Update                                     
--------------------------------------------------------------------------------

* iosxe
    * Updated ShowIpv6MldGroupsDetail Parser for
        * Parser for 'show ipv6 mld groups <group> <interface> detail'


