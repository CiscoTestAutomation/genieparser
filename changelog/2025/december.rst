--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowBgpNeighbors
        * Updated parser and schema for Showbgp neighbour to support tcp aco keychain
    * Modified ShowInterfaces
        * 'show interfaces <interface>'
    * Modified ShowIpVirtualReassemblyInterface
        * 'show ip virtual-reassembly {interface}'
    * Modified ShowCryptoPkiTimerDetail parser
    * Modified ShowPlatformSoftwareInfrastructureThreadFastpath
        * show platform software infrastructure thread fastpath.
    * Modified ShowControllerVDSL
        * 'show controller VDSL {interface}'
    * Modified ShowParameterMapInspectGlobalScema
    * Added Optional keyword for log_flow_export_template_timeout_rate variable to support new cli output
    * Modified ShowKeyChain
        * updated parser and schema for ShowKeyChain parser to support TCP key chain and MACsec Key Table (MKT) features.
    * Modified ShowPlatformHardwareQfpActiveFeatureFirewallDrop
        * 'show platform hardware qfp active feature firewall drop {actions}'
    * Modified ShowRedundancyApplicationGroup
        * Fixed UnboundLocalError by initializing media_active_peer dictionary before use.
        * Added Optional "local" key to active_peer schema.
        * Changed authentication, authentication_failures, reload_peer, resign keys in stats to Optional.
        * Changed all keys in active_peer (pkts, bytes, ha_seq, seq_number, pkt_loss, status, hold_timer) to Optional.
        * Added regex pattern p47 to accommodate "Standby Peer" output lines.
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveIpv6Route
        * Updated handle additional lines in the show platform software fed switch active ipv6 route command.
    * Fixed parser ShowPlatformSoftwareFedActiveIpRoute
        * Updated handle additional lines in the show platform software fed active ip route command.
    * Fixed parser ShowCtsServerList
        * Updated to handle radius server group configuration with IPv6 interface.
    * Fixed parser ShowIpSlaStatistics
        * Updated  handle additional lines in the show ip sla statistics {probe_id} command.

* nxos
    * Modified ShowIsis, ShowIsisAdjacency, ShowIsisHostname, ShowIsisHostnameDetail, ShowIsisInterface
        * Adjust area address regex to account for addresses that are hex or None
        * Adjust schemas to account for valid VRF configurations that do not have all information
    * Modified ShowBgpVrfAllAllSummary
        * Handle cases where BGP neighbor information is spread over 3 lines


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareFedSwitchActiveStpVlan parser
        * show platform software fed switch {switch_num} stp-vlan {vlan_id}
        * show platform software fed active stp-vlan {vlan_id}
    * Added Parser for show ipv6 traffic
        * Added a new schema and parser for the show ipv6 traffic command.
    * Enhanced ShowCtsSxpConnectionsBrief parser.
        * Enhanced parser for cli show cts sxp connections brief.
    * Added ShowCtsSxpSgtMap parser.
        * Added parser for cli show cts sxp sgt-map.
    * Added ShowPlatformHardwareQfpActiveInfrastructurePuntStatisticsTypePerCauseClear
        * 'show platform hardware qfp active infrastructure punt statistics type per-cause clear'
    * Added Parser for show platform software firewall qfp active runtime
        * Added a new schema and parser for the show platform software firewall qfp active runtime command.
    * Added ShowIpv6MfibActive parser in show_mfib.py
        * Added schema and parser for cli 'show ipv6 mfib active'
    * Modified ShowHwModuleSubslotAttribute
        * 'show hw-module subslot {slot} attribute'
    * Added ShowPolicyFirewallStatsGlobal
        * 'show policy-firewall stats global'
    * Added ShowLocateSwitch
        * Added show locate switch parser and tests for IOSXE IE3K platform
    * Added ShowPlatformHardwareQfpActiveFeatureFirewallUcodeScbDetail
        * 'show platform hardware qfp {instance} feature firewall ucode scb a a a a a a a detail'
    * Added showidprom
        * Added parser for "show idprom supervisor eeprom detail"
    * Added ShowDiagSubslotEeprom
    * 'show diag subslot 1/0 eeprom'
    * Added ShowHardwareLed
        * Added show hardware led parser and tests for C9610R platform, revision 1

* nxos
    * Added ShowSystemInternalFlash
        * show system internal flash
    * Modified ShowIpMrouteSummary
        * Updated regex pattern p8 to capture bitrate_unit with optional k/m/g/t prefixes.
        * Added conversion logic to normalize bitrate values to bps format.
    * Modified ShowIpv6MrouteSummary
        * Updated regex pattern p8 to capture bitrate_unit with optional k/m/g/t prefixes.
        * Added conversion logic to normalize bitrate values to bps format.


--------------------------------------------------------------------------------
                                     Added                                      
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformHardwareChassisPowerSupplyDetailAll in iosxe/Cat9k/c9550
        * Added parser for show platform hardware chassis power supply detail all
    * Added ShowPlatformHardwareChassisFantrayDetail in iosxe/Cat9k/c9550
        * Added parser for show platform hardware chassis fantray detail


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added new parameters show cloud-mgmt connect
    * Added new parameters show uac uplink, show uac Active-vlan, show uac Active-port


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowCefInterfacePolicyStatistics parser in show_cef.py
        * Modified ShowCefInterfacePolicyStatistics for cli 'show cef interface {interface_name} policy-statistics {direction}'


