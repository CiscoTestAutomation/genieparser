--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* iosxe

    * Added ShowPlatformTcamUtilization Parser
        * added 'show platform hardware fed {switch} {mode} fwd-asic resource tcam utilization' for c9500
    * Added ShowInterfaceCountersEtherchannel Parser
        * added 'show interface {interface} counters etherchannel'
    * Added ShowHardwareLed parser
        * Added parser for 'show hardware led' for c9400 switch.

    * Added ShowPerformanceMeasurementPaths
        * show performance-measurement paths
    * Added ShowPerformanceMeasurementSummary
        * show performance-measurement summary
        * show performance-measurement summary {detail}
        * show performance-measurement summary {detail} {private}
    * Added ShowIpv6DhcpInterface Parser
        * Parser for 'show ipv6 dhcp interface'
        * Parser for 'show ipv6 dhcp interface {interface}'
    * Added ShowPlatformSoftwareFedSwitchActiveMatmMacTableVlanMac
        * show platform software fed {state} matm macTable vlan {vlan} mac {mac}
        * show platform software fed {switch} {state} matm macTable vlan {vlan} mac {mac}
    * Added ShowSdwanPolicyServicePath Parser
        * Parser for 'show sdwan policy service-path vpn {vpn} interface {interface} source-ip {source_ip} dest-ip {destination_ip} protocol {protocol}'
        * Parser for 'show sdwan policy service-path vpn {vpn} interface {interface} source-ip {source_ip} dest-ip {destination_ip} protocol {protocol} {all}'
    * Added show platform software fed switch {switch} fnf flow-record asic {asic} start-index {index} num-flows {flow} parser
    * Added ShowIpNatTranslationsTotal parser
        * Parser for "show ip nat translations total"
        * Parser for "show ip nat translations vrf <vrf name> total"
    * Added ShowMdnsSdCache
        * parser for 'show mdns-sd cache'
    * Added ShowTimeRange
    * Added ShowOspfv3vrfNeighborInterfaceSchema
        * parser for 'show ospfv3 vrf {vrf_id} neighbor interface'
    * Added ShowFlowMonitorCacheFilterInterfaceIPv4 Parser
        * Parser for 'show flow monitor {name} cache filter interface {direction} {interface_name} ipv4 {address_direction} address {address}'
    * Added ShowDropsHistoryQfp
        * show drops history qfp
    * Added ShowDropsHistoryQfpClear
        * show drops history qfp clear
    * Added ShowPlatformHardwareQfpStatisticsDropHistory
        * show platform hardware qfp {status} statistics drop history
    * Added ShowPlatformHardwareQfpStatisticsDropHistoryClear
        * show platform hardware qfp {status} statistics drop history clear
    * Added ShowFileInformation
        * Added schema and parser for ShowFileInformation

* iosxr
    * Added ShowIsisIpv4Topology
        * Parser for cli 'show isis ipv4 topology'
    * Added ShowRibIpv6Iid
        * parser for 'show rib ipv6 iid all'
    * Added ShowPlatformSoftwareFedSwitchActiveAclInfoDbSummary
        * parser for 'Show Platform Software Fed Switch Active Acl Info Db Summary'

* iosxe showsdwanappqoeadstatistics
    * Added
        * parser for 'show sdwan appqoe ad-statistics'

* iosxe showsdwanappqoedreoptstatistics
    * Added
        * parser for 'show sdwan appqoe dreopt statistics'

* iosxe showsdwanappqoermstatistics
    * Added
        * parser for 'show sdwan appqoe rm-statistics'


--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxe
    * Modified  ShowPowerInlineModule
        * Modified in the p2 regular expression to match the poe names
    * Modified  ShowIpBgpNeighbors
        * Added New variables in Restricted address families to validate "l2vpn evpn" Neighbor
    * Modified ShowPlatformTcamUtilization Parser
        * Added mode variable
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressNpiDetailed Parser
        * Fix p1 regular expression to match port-channel
    * Modified ShowPolicyMapTypeSuperParser Parser
        * Fix p1 regular expression to match port-channel
    * Modified ShowPlatformIfmMapping c9500 Parser
        * Fix p1 regular expression to match IFG_ID, First Serdes, Last Serdes
    * Modified ShowPlatformSoftwareFedQosInterfaceSuperParser Parser
        * added timeout value to execute command and fix p5 with if condition on the counter
    * Modified ShowDerivedConfigInterface Parser
        * Made violation key as Optional
    * Modified ShowCallHomeProfileAll Parser
        * Fix p7 regex
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressNpiDetailed Parser
        * Added regex p4_12, p4_13, p4_14, p4_15, p4_16, p4_17, p4_18
    * Modified ShowLldpNeighborsInterfaceDetail Parser
        * Made 'management_addresses' as optional
    * Modified ShowInterfacesTransceiverSchema Parser
        * Added 'max_power' as optional key
    * Modified ShowSwitchStackMode Parser
        * Fix p1 regular expression pattern
    * Added ShowUSB
        * Added schema and parser for ShowUSB
    * Modified ShowPolicyMapInterface
        * Modified qos sets
            * Added cos cos table t1
            * Added traffic-class cos table t1
    * Modified ShowDeviceTrackingCountersVlan
        * Added new dict in the schema for the 'reason' variable with multiple
        * Modified the existing golden_ouputs to match the schema
    * Modified ShowDeviceTrackingDatabase
        * Added 'show device-tracking database vlan {vlan_id}' cli
        * Added New regex for vlan_db_capture
        * Added New variables in Schema and made existing Optional
    * Modified ShowLispEthernetMapCache
        * Added new regex p3_1 for new pattern output,and changed schema as Optional
        * Modified p3 regex to match the output
    * Modified ShowIpMfib
        * Modified p8 regex to match the output
    * Modified show_derived.py
        * Modificiation for show derived-config interface nve1
            * Added regex to handle configuration under nve1
    * Modified show_vrf.py
        * Modificiation for show vrf detail
            * Added regex to handle vnid, vni and core-vlan
    * Modified ShowPlatformHardwareAuthenticationStatus
        * Modified parser for "show platform hardware authentication status"
    * Modified ShowPlatformSoftwareFedIfm
        * Fixed TunnelID range and support for both modular and stack platforms
    * Modified ShowFlowMonitorCache
        * Added additional field fw_fw_event to schema
        * Added regex pattern <p33> to accomodate fw_fw_event outputs
    * Added ShowCableDiagnosticsTdrInt
        * Parser for show cable diagnostics tdr int {interface}
        * modified regex. p1,p2 and p3
    * Modified show l2route evpn multicast smet
        * Fixed issue of wrong index used for cli_command list in cli method of class ShowL2routeEvpnMulticastSmet
    * Added ShowHwProgrammableAll
        * Added schema and parser for ShowHwProgrammableAll
    * Added ShowAuthenticationSessionsDetailsSuper
        * Added <webauth> in p6 regex as Optional
    * Modified ShowLicenseTechSupport as per the output change in latest polaris version.
    * Added the key smartagentcompliancestatus in schema.
    * Modified ShowLogging
        * Local variable 'trap_dict' referenced before assignment
    * Modified ShowAccessSessionMacDetails
        * Modified keys <session_timeout>, <vlan_group>, <acs_acl>, <timeout_action> , <session_timeout> as Optional in the schema.

* asa
    * Fix for ShowVersion parser
        * Updated regex p7

* nxos
    * Fix for ShowModule parser
        * Updated regex for much more tightly controlled matching
    * Modified ShowVpc
        * Updated show vpc parser to include Virtual-peerlink mode status
    * Fix for ShowBgpVrfAllNeighbors parser
        * modify regex to handle new pattern.
    * Fix for ShowInterfaceBrief parser
        * add regex to handle tunnel interfaces

* iosxr
    * Modified ShowRouteIpv6
        * Added pattern <p15> to match 'ffff50.1.1.1, from ffff50.1.1.8'
    * Modified ShowL2vpnBridgeDomainBrief
        * Added p2 and p3 pattern
    * Modified ShowBfdSessionDestination
        * Added Interfaces as key under dest value and moved complete schema which was under dest to interfaces key.
        * Modified async_detection_time_ms as optional parameter under timer_vals in schema.
        * Modified echo_detection_time_ms as optional parameter under timer_vals in schema.
        * Added <p3> to parse the format "No                  n/a             n/a              n/a              UP".
        * Added <p4> to parse the format "BE10                1.1.1.1         n/a              n/a              DOWN".








