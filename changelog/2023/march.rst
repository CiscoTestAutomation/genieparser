--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowDerivedConfigInterface
        * added couple of optional parameters.
    * Added ShowControllerEthernetController
        * show controller ethernet-controller {interface}
    * Added ShowCallHomeAlertGroup
        * show call-home alert-group
    * Added ShowCallHomeDiagnosticSignature
        * show call-home diagnostic-signature
    * Added ShowCallHomeEvents
        * show call-home events
    * Added ShowCallHomeDetail
        * show call-home detail
    * Added ShowAccessSessionInterface
        * show access-session interface {interface}
    * Added ShowIpv6MldSnoopingQuerier
        * show ipv6 mld snooping querier
    * Added show platform software fed switch {active} vp key {if_id} {vlan_id}
        * Parsre for "show platform software fed switch {active} vp key {if_id} {vlan_id}
    * Added ShowDiagnosticResultSwitchTestDetail parser
        * Parser for "show diagnostic result {switch_number} test {include} detail"
    * Added ShowPlatformSoftwareFedSwitchMatmStats Parser
        * Parser for "show platform software fed switch {mode} matm stats"
    * Added ShowAlarmProfile parser
        * parser for show alarm profile in the device
    * Added ShowAlarmSettings parser
        * parser for show alarm settings in the device
    * Added ShowFacilityAlarmStatus parser
        * parser for show facility-alarm status in the device
    * Added ShowPlatformSoftwareFedActiveVtHardwareIfId
        * show platform software fed active vt hardware if-id {if_id}
    * Added Parser ShowPlatformSoftwareInstallManagerChassisActiveR0OperationHistorySummary
        * 'show platform software install-manager chassis active r0 operation history summary'
    * Added ShowCryptoPkiTrustpoints parser
        * Parser for "show crypto pki trustpoints"
    * Modified ShowIpDhcpServerStatistics Parser
        * Parser lines added for the drop counters
    * Added ShowL2fibBridgeDomainDetail Parser
        * Parser for show l2fib bridge-domain {bd_id} detail
    * Added ShowTemplateInterfaceSourceUser
        * show template interface source user {user}
    * Added ShowTemplateServiceSourceUser
        * show template service source user {user}
    * Added ShowAutoConfigurationTemplateBuiltIn
        * show auto configuration template builtin
    * Added ShowFlowMonitor
        * "show flow monitor" for 9500 devices
    * Added ShowPlatformSoftwareFedSwitchQosPolicyTargetStatus
        * show platform software fed switch {switch} qos policy target status
    * Added ShowBgpL2vpnEvpnEviRouteType
        * show bgp l2vpn evpn evi {evi_id} route-type {route_type}
    * Added ShowPlatformSoftwareFedSwitchActiveVpSummaryInterfaceIfId
        * show platform software fed switch active vp summary interface if_id {if_id}
    * Added ShowPlatformSoftwareFedIfmInterfaces Parser
        * Parser for "show platform software fed {switch} active ifm interfaces vlan"
        * Parser for "show platform software fed active ifm interfaces vlan"
    * Added ShowL2fibOutputList Parser
        * Parser for "show l2fib output-list"
    * Added ShowL2fibOutputListId Parser
        * Parser for "show l2fib output-list {output_id}"
    * Added ShowVRFIPv6
        * show vrf ipv6 {vrf}
        * To verify the IPv6 configuration on device
    * Added ShowPlatformSoftwareFedActiveQosPolicySummary
        * Parser for show platform software fed active qos policy summary

* iosxr
    * Added ShowDhcpIpv4ProxyBinding
        * Parser for cli 'show dhcp ipv4 proxy binding'
        * Parser for cli 'show dhcp ipv4 proxy binding interface {interface_name}'
    * Added ShowDhcpIpv4ServerBinding
        * Parser for cli 'show dhcp ipv4 server binding'
        * Parser for cli 'show dhcp ipv4 server binding interface {interface_name}'
    * Added ShowPtpPlatformServo
        * added new parser for cli 'show ptp platform servo'
    * Added ShowPlatformHwFedActiveQosQStatsInternalCpuPolicer
        * added new parser for cli 'show platform hardware fed switch active qos queue stats internal cpu policer'
    * Modified ShowIsisNeighbors
        * Parser for 'show isis instance {process_id} neighbors'

* added showplatformsoftwarefedswitchactivematmadjacenciesadjkey
    * show platform software fed switch active matm adjacencies adjkey {adj_key}


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowIpIgmpSnoopingGroupsVlanHosts
        * show ip igmp snooping groups vlan <vlan> <group> hosts
    * Added ShowIpIgmpSnoopingGroupsVlanSources
        * show ip igmp snooping groups vlan <vlan> <group> sources
    * Added
        * show platform hardware fed switch {switch} fwd-asic resource utilization
    * Added ShowL2vpnEvpnEviDetail
        * show l2vpn evpn evi detail
        * show l2vpn evpn evi <evi> detail
    * Added ShowL2vpnEvpnSummary
        * show l2vpn evpn summary
    * Added ShowIsisTeapp
    * Added ShowIsisTeappPolicy


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Added
        * show stack-power load-shedding
        * show switch stack-mode
    * Modified ShowCryptoIke2SaDetail
        * Updated regex pattern <r8> to support not just IP addresses for Remote id
    * Modified ShowL2vpnServiceAll
        * Updated schema to allow for incomplete configuration with no interface
    * Modified ShowIpRoute
        * Updated regex patterns to allow next_hop vrf to contains '-' in vrf name
    * Modified ShowNetconfYangStatus
        * Updated schema to accommodate the latest release output.
        * Updated parser for latest release output
    * Fix ShowL2vpnServiceAll
        * CLI output was modified
        * show l2vpn service all
        * show l2vpn service interface {interface}
        * show l2vpn service name {name}
        * show l2vpn service xconnect all
        * show l2vpn service xconnect interface {interface}
        * show l2vpn service xconnect name {name}
    * Modified ShowPowerInlineDetail
        * Fixed 'operational_status' regular expression and added unit test
    * Modified ShowPowerInlineUpoePlus
        * Fixed regular expression and added unit test
    * Modified ShowIpVerifySource
        * Added mac_address optional key, fixed regex and unit test
    * Modified ShowBgpNeighbor
        * Update parsing to support VRF in bgp neighbors cli command instead of always setting 'default' VRF (parser p2_3)
    * Modified ShowFlowMonitorCache
        * Modified code to match protocol entires
    * Modified ShowMonitorCaptureBuffer
        * Modified code to match ipv4 and ipv6 protocol entires
    * Modified ShowPlatformHardwareFedSwitchQosDscpcosCounters
        * Modified code to get parse output for HA and standlone devices
    * Modified ShowRunningConfigNve
        * Updated the SVI schema for DHCP related data
        * Added regex <p3_16> and <p3_17>
    * Modified ShowPlatformHardwareFedSwitchActiveQosDscpCosCountersInterface
        * Updated command to match previous implementation for c9600 and fix fuzzy command search
    * Modified ShowLispService
        * Added ipv6 regex
    * Modified ShowLispSiteDetail
        * Added ipv6 regex
    * Modified ShowLispIpv6Publication
        * Added ipv6 regex
    * Modified ShowLispPublisherSuperParser
        * Added ipv6 regex
    * Modified ShowLispPublicationPrefixSuperParser
        * Added ipv6 regex
    * Modified ShowLispSubscriberSuperParser
        * Added ipv6 regex
    * Modified ShowLispIpv4PublisherRloc
        * Added ipv6 regex
    * Modified ShowLispInstanceIdService
        * Added ipv6 regex
    * Added ShowLispIpv6PublisherRloc
        * Added ShowLispIpv6PublisherRloc parser
    * Modified ShowParserStatistics
        * Changed date, time_with_seconds, time_zone from schema to Optional.
        * Updated regex pattern p7 to accommodate various outputs.

* iosxr
    * Modified ShowVrfAllDetail
        * Updated regex pattern p1 to allow '' in vrf name
    * Modified ShowOspfv3Neighbor
        * Modified up_time as Optional parameter in schema.
    * Modified ShowPolicyMapInterface
        * Added Optional parameter queue_exceed_packets to schema
        * Added Optional parameter queue_exceed_bytes to schema
        * Added Optional parameter queue_exceed_rate to schema
        * Added Optional parameter policing_statistics section to schema
        * Added Optional parameter policed_confirm to schema
        * Added Optional parameter policed_exceed to schema
        * Added Optional parameter policed_violate to schema
        * Added Optional parameter policed_and_dropped to schema
        * Added Optional parameter wred_profile section to schema
        * Added Optional parameter red_transmitted to schema
        * Added Optional parameter red_random_drops_packets to schema
        * Added Optional parameter red_random_drops_bytes to schema
        * Added Optional parameter red_maxthreshold_drops to schema
        * Added Optional parameter red_ecn_marked_transmitted to schema
        * Modified P2 pattern to support the format 'Bundle-Ether203 input SERVICE-BPS'
        * Modified P5 pattern to support the format 'Class IPV4-PACKET-IS-00'
    * Modified ShowBfdSession
        * Added <p5> pattern to match 'Gi0/0/0/1.10        192.168.1.2     0s               10s(2s*5)        INIT'
    * Modified ShowMplsLdpDiscovery
        * Added code to support 'passive' and 'active/passive' state
        * Added 'targeted_hellos' section as optional parameter to schema under 'local_ldp_identifier'.
        * Added 'xmit' as optional parameter under 'targeted_hellos' section to schema.
        * Added 'recv' as optional parameter under 'targeted_hellos' section to schema.
        * Added 'active' as optional parameter under 'targeted_hellos' section to schema.
        * Added 'passive' as optional parameter under 'targeted_hellos' section to schema.
        * Added 'active/passive' as optional parameter under 'targeted_hellos' section to schema.


--------------------------------------------------------------------------------
                                     Update                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowPolicyMapInterface parser
        * Added new keys 'burst_bytes' and 'rate_bps'


--------------------------------------------------------------------------------
                                     Modify                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified show cts interface
        * show cts interface {interface} added.


--------------------------------------------------------------------------------
                                       ~                                        
--------------------------------------------------------------------------------


