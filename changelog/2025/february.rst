--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareFedSwitchActiveIpMfibVrf parser
        * Added schema and parser for cli
            * 'show platform software fed switch active ip mfib vrf {vrf_name} {group} {source}'
            * 'show platform software fed switch active ip mfib {group} {source}'
            * 'show platform software fed active ip mfib vrf {vrf_name} {group} {source}'
            * 'show platform software fed active ip mfib {group} {source}'
    * Added ShowPlatformSoftwareFedPuntAsicCauseBrief
        * show platform software fed switch {mode} punt asic-cause brief
    * Added ShowAutoInstTrace parser
        * Added schema and parser for cli 'show auto inst trace'
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightIfmPortAn37Status parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_an37_status({system_port_gid}).
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightIfmPortAnltStatus parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_anlt_status({system_port_gid}).
    * Added
        * show raw-socket tcp sessions local
    * Added  ShowPlatformSoftwareRouteMap parser
        * Added schema and parser for cli "show platform software route-map R0 map"
    * Added ShowPlatformHardwareAuthenticationStatus
        * Added parser "show platform hardware authentication status" under c9610
    * Added support for parsing the 'show access method dot1x details'
    * Added ShowHardwareLed schema and parser
        * Added schema and parser for show hardware led
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightIfmPortStatus parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_status({system_port_gid}).
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightPortSerdesStatus parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_serdes_status({system_port_gid}).
    * Added ShowRunningConfigAAARadiusServer
        * Added schema and parser for 'Show Running Config AAA Radius Server'
    * Added support for parsing the 'show cts policy sgt {sgt}'
    * Added parser ShowPlatformSoftwareFedSwitchActivePortIfId
        * Added parser for 'show platform software fed {switch} {mode} port if_id {if_id}'
    * Added ShowInterfacesCountersPort parser
        * Added schema and parser for cli 'show interfaces counters port'
    * Added ShowIPDhcpImport Parser in show_ip.py
        * show ip dhcp import
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightL2AttachmentCircuitStatus and ShowPlatformHardwareFedSwitch1FwdAsicInsightIfmLagMembers parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight l2_attachment_circuit_status().
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight ifm_lag_members({lag_gid}).
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightL2mRoutes parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight l2m_routes({switch_gid}).
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightL2mGroups parser.
        * Added parser for cli sshow platform hardware fed switch {switch_id} fwd-asic insight l2m_groups({l2_mcg_gid}).
    * Added ShowIpv6GeneralPrefix Parser in show_ipv6.py
        * show ipv6 general-prefix
    * Added schema and parser for 'show spanning-tree mst interface {interface}'
    * Added schema and parser for 'show switch stack-ports summary'
    * Added ShowAuthenticationSessionMethodDetails parser.
        * 'show authentication sessions method {method} details'
        * 'show authentication sessions method {method} interface GigabitEthernet2/0/3 details'
        * 'show authentication sessions method {method} policy'
    * Added support for parsing the 'show platform software fed {switch} {active} ip mfib vrf {vrf_name} {group} {source}',
    * Added ShowPlatformSoftwareFedActiveIfmInterfaceNameTunnel5 parser
        * Added schema and parser for cli 'show platform software fed active ifm interface_name tunnel5'
    * Added ShowPlatformSoftwareFedSwitchActiveIpMulticastInterface parser
        * Added parser for cli show platform software fed switch {module} ip multicast interface {if_id}
        * Added parser for cli show platform software fed switch {module} ipv6 multicast interface {if_id}
    * Added ShowPlatformSoftwareFedSwitchActiveOifsetL3mHash parser
        * Added parser for cli show platform software fed switch active oifset l3m hash {hash} detail
    * Added  ShowPlatformSoftwareFedSwitchFnfMonitorRulesAsic0 parser
        * Added schema and parser for cli "show platform software fed switch {switch_num} fnf monitor rules asic 0"
    * Added support for parsing the following commands
        * 'show authentication sessions interface GigabitEthernet2/0/3'
        * 'show authentication sessions interface GigabitEthernet2/0/3 switch standby R0'
        * 'show authentication sessions interface GigabitEthernet2/0/3 switch active R0'
        * 'show authentication sessions database interface GigabitEthernet2/0/3 switch active R0'
        * 'show authentication sessions database interface GigabitEthernet2/0/3 switch standby R0'
        * 'show authentication sessions database interface GigabitEthernet2/0/3 switch 1 R0'
    * Added ShowMonitorCaptureFileDetailed
        * Added schema and parser for'show monitor capture file flashfile1.pcap packet-number 7 detailed'
    * Added ShowIPDhcpConflict Parser in show_ip.py
        * show ip dhcp conflict
    * Added ShowIpPolicy Parser in show_ip.py
        * show ip policy
    * Added schema and parser for cli
        * 'show mac address-table dynamic',
        * 'show mac address-table dynamic interface {intf_name}'
    * Added ShowIpv6OspfDatabase
        * Added schema and parser for 'ShowIpv6OspfDatabase'
    * Added ShowIpDhcpSnoopingStatisticsDetail parser
        * Added schema and parser for cli 'show ip dhcp snooping statistics detail'

* nxos
    * added new parser ShowIpDhcpSnoopingBindingDynamicEvpn
        * Added new parser for the cli "show ip dhcp snooping binding dynamic evpn"
        * Added new parser for the cli "show ip dhcp snooping binding interface <intf> dynamic evpn"
        * Added new parser for the cli "show ip dhcp snooping binding vlan <vlan> dynamic evpn"
        * Added new parser for the cli "show ip dhcp snooping binding interface <intf> vlan <vlan> dynamic evpn"
    * added new parser ShowIpDhcpSnoopingBindingStaticEvpn
        * added new parser for the cli "show ip dhcp snooping binding static evpn"
        * added new parser for the cli "show ip dhcp snooping binding interface {intf} static evpn"
        * added new parser for the cli "show ip dhcp snooping binding vlan {vlan} static evpn"
        * added new parser for the cli "show ip dhcp snooping binding interface {intf} vlan {vlan} static evpn"
    * added new parser ShowIpDhcpSnoopingBindingDynamic
        * Added new parser for the cli "show ip dhcp snooping binding dynamic"
        * Added new parser for the cli "show ip dhcp snooping binding interface <intf> dynamic"
        * Added new parser for the cli "show ip dhcp snooping binding vlan <vlan> dynamic"
        * Added new parser for the cli "show ip dhcp snooping binding interface <intf> vlan <vlan> dynamic"
    * added new parser ShowIpDhcpSnoopingBindingStatic
        * added new parser for the cli "show ip dhcp snooping binding static"
        * added new parser for the cli "show ip dhcp snooping binding interface {intf} static"
        * added new parser for the cli "show ip dhcp snooping binding vlan {vlan} static"
        * added new parser for the cli "show ip dhcp snooping binding interface {intf} vlan {vlan} static"
    * added new parser ShowL2routeFhs
        * added new parser for the cli "show l2route fhs all"
        * added new parser for the cli "show l2route fhs topology {vlan}"
    * added new parser ShowForwardingRouteIpsgVrf
        * added new parser for the cli 'show forwarding route ipsg vrf all'
        * added new parser for the cli 'show forwarding route ipsg vrf {vrf}'
        * added new parser for the cli 'show forwarding route ipsg max-display-count {max_count} vrf {vrf}'
        * added new parser for the cli 'show forwarding route ipsg module {ipsg_module} vrf all'
        * added new parser for the cli 'show forwarding route ipsg module {ipsg_module} vrf {vrf}'
        * added new parser for the cli 'show forwarding route ipsg max-display-count {max_count} module {ipsg_module} vrf all'
        * added new parser for the cli 'show forwarding route ipsg max-display-count {max_count} module {ipsg_module} vrf {vrf}'
        * added new parser for the cli 'show forwarding route ipsg max-display-count {max_count} vrf all'
    * added new parser ShowIpDhcpSnoopingStatistics
        * added new parser for the cli 'show ip dhcp snooping statistics'
        * added new parser for the cli 'show ip dhcp snooping statistics vlan {vlan}'
    * added new parser ShowIpDhcpRelayStatisticsInterfaceVlan
        * added new parser for the cli 'show ip dhcp relay statistics interface vlan {vlan}'
    * added new parser ShowIpv6DhcpRelayStatisticsInterfaceVlan
        * added new parser for the cli 'show ipv6 dhcp relay statistics interface vlan {vlan}'
    * Added ShowIpv6RouteSummary
        * show ipv6 route summary
        * show ipv6 route summary vrf {vrf}

* iosxr
    * Added parser for show inventory sparse


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowInterface
        * Added line
    * Modified ShowMonitorCaptureBufferDetailed
        * Modified schema and parser for'show monitor capture file {path} packet-number {number} detailed'
    * Modified ShowPlatformHardwareFpgaSwitch
        * Modified parser to handle spaces flexibly in the output
        * Added regular expression p0 which skips the table tile line
    * Modified ShowIpDhcpBinding
        * Added "show ip dhcp binding vrf {vrf_name} {ip_address}" cli
        * Added "show ip dhcp binding {ip_address}" cli
    * Fixed parser ShowLine
        * Fixed regex pattern for show line for int field to be optional"
    * Fix ShowPlatformSoftwareFedActiveMonitor parser
        * Removed duplicate parser for show platform software fed active monitor and modified the existing parser regex p2 to handle the output of the command.
    * cat9k
        * c9610
            * Fixed parser ShowHardwareLed
                * Modified the parser regex p6 to handle the output of the command.
                * Added optional "beacon" keyword to the parser schema.
    * Fixed the regex p1 for new output.
    * rv1
        * Added few keys for the ShowPlatform parser schema.
        * Added 'IE-35' as part of the condition for lc_type 'rp'.
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveIfmMappingsLpn
        * Added fed active and fed switch commands to the parser.
    * Fixed parser ShSoftwareFed
        * Added fed active and fed switch commands to the parser.
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveCpuInterfaces
        * Modified switch as optional in the parser.
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveIfmMappingsL3if_le
        * Modified switch as optional in the parser.
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveIfmMappingsGpn
        * Modified switch as optional in the parser.
    * Modified ShowPlatformSoftwareFedSwitchActiveSgaclPort parser
        * Added optional parameters "ingress" and "egress" , modified "interface_state" to be OPtional
        * Added new regex pattern p2 to accomodate output for sgacl port details for all catalyst platfroms 9200,0300,9400 etc
    * Modified ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableSummary
        * added support parser should work on active and standby
    * Modified ShowPlatformSoftwareFedActiveAclBindDbDetail
        * added support cg_name filed to accepct ! and
    * Modified ShowPlatformSoftwareFedSwitchActiveAclBindDbIfid
        * added support parser should work on active and standby
    * Modified ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableUsage
        * added support parser should work on active and standby
    * Modified ShowPowerInline schema and parser to support on IE3K platforms
        * Modified schema and parser for 'show power inline interface' command
    * Modify parser ShowRunInterface
        * Modified URPF Features.
    * cat9k
        * c9400
            * Fixed parser show boot to make the standby details optional.
    * cat9k
        * c9350
            * Modified ShowPlatformHardwareFedSwitchQosQueueConfig
                * modified switch_var to swich_num to match parser under iosxe.
    * Modified parser ShowHardwareLed
        * Enhanced the parser to get LED auto-off status, Added schema and regex pattern <p12_1>
        * Enhanced the parser to get LED Hardware State, Added schema and regex pattern <p12_2>
    * Fix ShowPlatformSoftwareFedSwitchStateIfmIfIdIf_id
        * Added fed active and fed switch commands to the parser.
    * Modify parser ShowCefInterfaceInternal
        * Added IP unicast RPF check is enabled.
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveStatisticsInit
        * Added fed active and fed switch commands to the parser.
    * Fixed parser ShowPlatformSoftwareFedSwitchNumberIfmMappingsPortLE
        * Added fed active and fed switch commands to the parser.
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveIfmInterfacesDetail
        * Modified switch as optional in the parser.
    * Modified ShowRepTopologyDetail
        * Modified  regex to support new device output.
    * Modified ShowDiagnosticContentModule
        * Added parser supprot for 'show diagnostic content module' command
        * Added regular expression p0 which extracts the module number
    * Fixed parser ShowWirelessClientMacDetail
        * Modified current_rate and max_client_protocol_capability to be optional
        * Allowed space within Device Type (e.g. 'Un-Classified Device')
    * Fixed parser ShowPlatformSoftwareAccessListSwitchActiveF0Summary
        * Added parser support for 'show platform software access-list f0 summary' command

* nxos
    * Fixed parser ShowNveEthernetSegment
        * Fixed the case where df_vni_list will be populated.
    * Modified ShowVdcMembershipStatus
        * Updated regex <p4> to allow for a space between interface name and status.
    * Modified ShowIpRoute
        * Updated regex pattern <p3> to handle the following cases

* generic
    * Modified ShowVersion
        * Added os_flavor field to the parser output

* iosxr
    * Fixed parser ShowInterfacesDetail
        * Fixed regex pattern p9_3 to match "flow control"


