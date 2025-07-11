--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPost Parser
        * Added ShowPost parser for c9200
    * Added ShowIpv6MldSnoopingAddress Parser
        * Added schema and parser for cli "show ipv6 mld snooping address vlan {vlan} {group}"
    * Added ShowPlatformSoftwareFedIpRouteSummary parser
        * Added c9610 schema and parser for 'show platform software fed {switch} ip route summary'
    * Added Schema and Parser for ShowPlatformHardwareFedSwitchFwdAsicInsightAclL2AclAttachmentCircuits
        * show platform hardware fed switch {state} fwd-asic insight acl_l2_acl_attachment_circuits()
    * Added ShowPlatformSoftwareIgmpSnoopingGroupsVlanCount
        * Added schema and parser for 'show platform software fed {state} ip igmp snooping groups vlan {vlan} count' command.
    * Added ShowIpv6MfibInterface
    * 'show ipv6 mfib interface'
    * Added ShowPlatformSoftwareFirewallFPActivePairs
        * show platform software firewall FP active pairs
    * Added acm log parser
        * Added Acm Log {command}
        * Added Acm Log IndexNumber
    * Added ShowPlatformHardwareQfpActiveFeatureFirewallClientStatistics
        * show platform hardware qfp active feature firewall client statistics
    * Added ShowCryptoIpsecSaIpv6Detailed Parser
        * Parser for 'show crypto ipsec sa ipv6 detailed'
    * Added ShowCryptoIkev2DiagnoseError Parser
        * Parser for 'show crypto ikev2 diagnose error'
    * ShowIpMrmStatus
        * show ip mrm status.
    * Added ShowMplsTpTunnelTp parser in show_mpls.py
    * Added schema and parser for cli 'show mpls tp tunnel-tp 1 lsps detail'
    * Added ShowPlatformHardwareFedFwdAsicInsightAclEthPortMixMode
        * Added schema and parser for 'show platform hardware fed {switch} {state} fwd-asic insight acl_eth_port_mix_mode'
    * Added ShowPlatformHardwareFedFwdAsicInsightAclEthPortDense
        * Added schema and parser for 'show platform hardware fed {switch} {state} fwd-asic insight acl_eth_port_dense'
    * Added ShowPlatformHardwareFedFwdAsicInsightAclGroupDetails
        * Added schema and parser for 'show platform hardware fed {switch} {state} fwd-asic insight acl_group_details'
    * Added ShowPlatformHardwareFedFwdAsicInsightAclAttachmentCircuit
        * Added schema and parser for 'show platform hardware fed {switch} {state} fwd-asic insight acl_attachment_circuit'
    * Added ShowPlatformSoftwareNatFpActiveMappingDynamic
    * 'show platform software nat fp active mapping dynamic'
    * Added ShowControlCpu
        * Added schema and parser for 'show control cpu'
    * Added ShowIpvMldVrfGroup parser in show_ip.py
    * Added schema and parser for cli 'show ipv mld vrf {vrf} groups {group}'
    * Added ShowParameterMapTypeInspect
        * 'show parameter-map type inspect {param}'
    * Added acm merge <configlet_file> validate parser
        * Parse "acm merge demo validate"
    * Added ShowL2vpnServiceAll
        * show l2vpn service vfi all
    * Added ShowIpWccpWebCacheDetail parser in show_ip.py
    * Added schema and parser for cli 'show ip wccp web-cache detail'
    * Added Parser for dir crashinfo
        * Added a new schema and parser for the dir crashinfo command.
    * Added ShowMplsL2transportSummary
        * show mpls l2transport summary
    * Added show platform hardware fed switch {switch_id} fwd-asic insight l2_attachment_circuit_status(lag_gid={lag_gid})
    * cat9k
        * Added ShowLoggingOnboardSlotStatus parser
            * Added schema and parser for cli "show logging onboard slot {slot} status"
    * Added show platform software fed switch <active/stby> acl manager acl-group interface <interface>
        * Added show platform software fed switch <active/stby> acl manager acl-group iif_id <if_id_num>
    * Added support for ShowPlatformHardwareFedSwitchFwdAsicInsightL2SwitchMacTable parser
    * Added ShowPlatformSoftwareNatFpActivePool
    * 'show platform software nat fp active pool'
    * Modified ShowIpPimInterfaceCount
        * show ip pim int count.
    * Added ShowPlatformSudiCertificateNonce schema in iosxe/ie3k
        * Added parser for show software platform sudi certificate sign in iosxe/ie3k
    * Added ShowPlatformIntegrity schema
        * Added parser for show platform integrity sign in iosxe/ie3k
    * Added ShowPlatformUplinks parser.
        * Added parser for cli 'show platform uplink'.
    * Added ShowPlatformSoftwareFedActiveAclBindDbSummary parser
        * Added rv1 schema and parser for 'show platform software fed active acl bind db summary'
    * Added ShowPlatformSoftwareFedActiveAclBindDbDetail parser
        * Added rv1 schema and parser for 'show platform software fed active acl bind db detail'
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightS1TrapStatus
        * Added schema and parser for
            * 'show platform hardware fed switch {state} fwd-asic insight s1_trap_status()'
    * Added ShowPlatformSoftwareMemoryForwardingManager
    * 'show platform software memory forwarding-manager F0 brief | include {option}'
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightAclTableDef
        * Added schema and parser for 'show platform hardware fed {switch} {state} fwd-asic insight acl_table_def()'.
    * Added ShowPlatformSoftwareFedSwitchAclBindSdkInterfaceFeatureDirDetailAsic
        * Added schema and parser for 'show platform software fed {switch} {state} acl bind sdk interface {interface} feature {feature} dir {dir} detail asic {asic}'
    * Added ShowPlatformSoftwareFedSwitchAclParallelKeyProfileIngress
        * Added schema and parser for 'show platform software fed {switch} {state} acl man parallel-key-profile ingress all'
    * Added ShowPlatformSoftwareAccessListFpActiveStatistics
        * Added 'show platform software access-list fp active statistics' command and schema for the command.
    * ShowVoiceCallSummary
        * show voice call summary.
    * Added ShowMplsTpLspsDetail parser in show_mpls.py
    * Added schema and parser for cli 'show mpls tp lsps detail'
    * Added ShowCallHomeProfileAll
        * show call-home profile {include}
    * Added ShowIpIgmpSnoopingGroupsVlanCount
        * Added schema and parser for 'show ip igmp snooping groups vlan {vlan} count' command.
    * Added show platform hardware fed switch active fwd-asic insight acl_svi_attachment_circuits
    * Added acm configlet status parser
        * Parse "acm configlet status"


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressNpdDetailed
        * Calling super parser cli with command argument
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressNpd
        * Calling super parser cli with command argument
    * Modified ShowPlatformSoftwareFedQosInterfaceEgressSdkDetailed
        * Calling super parser cli with command argument
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressSdk
        * Calling super parser cli with command argument
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressSdkDetailed
        * Calling super parser cli with command argument
    * Modified ShowPlatformSoftwareFedQosInterfaceEgressNpdDetailed
        * Calling super parser cli with command argument
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressSdkDetailedAsicAll
        * Calling super parser cli with command argument
    * Modified parser ShowPlatformSoftwareFedSwitchActiveAclOgPcl
        * Added support for show platform software fed active acl og-pcl
        * Added mode to support switch numbers
    * Fixed parser ShowPlatformSoftwareFedActiveAclInfoDbDetail
        * Added "show platform software fed {switch} {mode} acl info db feature {feature_name} dir {in_out} detail" to the command
        * modified switch as variable for flexibility
    * Modified ShowProcessesCpuSorted
    * 'show processes cpu sorted'  #Changed timeout from default to timeout 300 for this cli
    * Fixed parser ShowLoggingOnboardSlotUptime
        * Added 'show logging onboard slot {slot} uptime latest'.
    * Modified ShowPlatformHardwareFedSwitchFwdAsicInsightIfmLagStatus parser
        * Modified parser for CLI
            * 'show platform hardware fed switch {switch_id} fwd-asic insight ifm_lag_status({lag_gid})',
            * 'show platform hardware fed {switch} {switch_id} fwd-asic insight ifm_lag_status({lag_gid})'
        * Modified parser for arguments
            * 'switch_id'"1" to "Any"
    * Removed ShowPlatformHardwareFedSwitchFwdAsicInsightIfmLagStatus parser
        * due to dublication of the parser
    * Modified ShowFlowMonitor
        * Modified regexn and parser schema
    * Fixed ShowFlowInterface parser
        * Fixed regex pattern p4 to match the output of the command.
    * Modified ShowPlatformHardwareFedSwitchQosQueueConfig parser
        * Removed duplicate parser code.
        * addded kwargs and command to detect the correct parser.
    * Fixed ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL2MirrorCommandStatus parser.
        * Modified parser for cli show platform hardware fed switch {switch_id} fwd-asic insight l2_mirror_command_status({mirror_gid}).
    * Fixed ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL2MirrorCommandL2 parser.
        * Modified parser for cli show platform hardware fed switch {switch_id} fwd-asic insight l2_mirror_command_l2({mirror_gid}).
    * show_route_map
        * Modified ShowRouteMapAll
            * Added regex pattern for ipv6 next-hop verify-availability
            * Added regex pattern for ipv6 next-hop recursive
    * Modified ShowPlatformSoftwareFedSwitchActiveOifset parser
        * Added support for show platform software fed active oifset
    * Modified ShowPolicyMapTypeInspectZonePair
    * Added show policy-map type inspect zone-pair new-trusted-untrusted cli
    * IE3K
        * Modified ShowHardwareLed
            * Modified the regex pattern
    * Added ShowPlatform
        * Added ShowPlatform parser in rv1
    * Modified parser Ping
        * Added the "B" flag as the indicator for the IPv6 Packet Too Big result
    * Modified ShowPlatformSoftwareFedSwitchAclBindDbInterfaceFeatureDirDetailAsic
        * Modified schema and parser for 'show platform software fed {switch} {state} acl bind db interface {interface} feature {feature} dir {dir} detail asic {asic}'
    * Modified ShowPlatformSoftwareFedSwitchAclParallelKeyProfileEgress
        * Modified schema and parser for'show platform software fed {switch} {state} acl man parallel-key-profile egress all'
    * Modified ShowPlatformSoftwareFedSwitchActiveAclBindSdkDetail
        * Modified schema and parser for'show platform software fed {switch} {switch_var} acl {acl} sdk detail'
        * Modified schema and parser for'show platform software fed {switch} {switch_var} acl {acl} sdk feature {feature_name} dir {dir} cgid {cg_id} detail'
        * Modified schema and parser for'show platform software fed {switch} {switch_var} acl {acl} sdk feature {feature_name} dir {dir} detail asic {asic_no}'
        * Modified schema and parser for'show platform software fed {switch} {switch_var} acl {acl} sdk feature {feature_name} detail'
        * Modified schema and parser for'show platform software fed {switch} {switch_var} acl {acl} sdk if-id {if_id} detail'
    * Modified ShowPlatformSoftwareFedActiveIpMfibVrf parser
        * Modified p1 regex to match the correct line
    * Modified ShowPlatformSoftwareFedSwitchActiveIpMfibVrf parser
        * Modified p1 regex to match the correct line
    * Modified parser ShowRunInterface
        * Added support for pnp startup-vlan 1200
    * Modified parser ShowPlatformHardwareFedSwitchActiveFwdAsicInsightS1SecGroupsMatrixMapStatus
        * changed 'switch' as a variable for flexibility
    * IE3K
        * Modified ShowHardwareLed
            * Modified the show hardware led for support additional field
    * Modified ShowInstallRollbackId
        * Modified regex p1

* modified parser for 'show platform hardware fed switch active fwd-asic insight vrf_for_us_routes'.

* updated cli output handling to generalize parsing for all vrfs.

* iosxr
    * Modified ShowInventoryRaw
        * Upadted the regex
    * Modified ShowProcesses
        * Added regex for 'level' & 'mandatory'
        * Updated type for 'instance' from str to int

* nxos
    * Modified ShowVersion
        * Added the new regex pattern for supporting system version


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowPolicyMapTypeInspectZonePair
    * Have added the new golden expected output for the clishow policy-map type inspect zone-pair in-out
    * Added ShowInterfacesTransceiverModule
        * Added ShowInterfacesTransceiverModule parser

* iosxr
    * Added ShowInterfacesTransceiverDetail
        * Added  ShowInterfacesTransceiverDetail in rv1 for supporting multiplle lanes


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Enhanced ShowMerakiConnect parser
        * Added support for delta fields in meraki_tunnel_interface section
        * Fields with "(Last Xs)" pattern are now converted to "*_delta" format


