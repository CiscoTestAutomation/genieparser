--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Modified ShowIpIgmpSnooping
        * Added 'ip_address' and 'state' as Optional parameter to schema
        * Modified pattern <p10> to match 'Switch-querier enabled, address XXX.XXX.XXX.XXX, currently running'
    * Modified ShowEnvironment
        * Updated regex pattern <p6> to accommodate various outputs.
    * Modified ShowModule
        * Updated p4 regex pattern to handle slot in case the serial number doesnt start with letters.

* iosxe
    * Modified ShowAAACacheGroup
        * fixed username regex pattern to handle special characters
    * Modified ShowCispInterface
        * Added support for parsing Auth State
    * Modified ShowFipsStatus
        * made sesa_ready as optional and added reg ex pattern to match switch and stack fips status
    * Modified ShowRunInterface
        * added switchport_trunk_native_vlan optional key
    * Modified ShowVersion
        * Update schema for show version to support older IOS devices
            * 'gigabit_ethernet' interfaces is now an optional key
    * Modified ShowCtsRoleBasedSgtMapAll
        * Added optional parameters 'total_l3if' and 'total_vlan'.
    * Enhanced ShowDeviceTrackingDatabaseDetails
        * Updated optional keys 'creating' and 'tentative' in schema
    * Added ShowLispServiceDatabase
        * Fix for "UnboundLocalError local variable 'lisp_id_dict' referenced before assignment"
    * Added ShowClnsTraffic
        * Fix for "UnboundLocalError local variable 'isis_dict' referenced before assignment"
    * Modified ShowPlatformSoftwareFedSwitchActivePtpDomain
        * Added few schema kesy to grep optional information.
    * Modified ShowPlatformSoftwareAuditSummary
        * Modified schema to support standalone output
    * Modified ShowStandbyBrief
        * Modified this PARSER to capture all the ipv6 entry from the output of command "show standby brief"
        * Saparate the ipv4 and ipv6 dictionary by "interface" and "ipv6_interface" name
        * change the schema for interface as "Any()"
    * Modified ShowOspfv3vrfNeighbor
        * changed vrf ID to be string instead of  integer
        * change regexp pattern
        * vrf_id was not sent as argument
    * Modified ShowBgpDetailSuperParser
        * Fix regex pattern for Extended Community to match dot
    * Modified ShowCdpInterface
        * Fix p0 regex pattern
    * Modified ShowInventoryRaw
        * Updated regex pattern <p1> to accommodate plus sign
    * Modified ShowOspfv3Neighbor
        * Updated regex pattern p2 to accommodate various outputs
    * Modified ShowOspfv3InterfaceSchema
        * Changed state, transmit_delay, retransmit, state, dead, hello, priority to optional
        * Added optional keys cost_hysteresis and neighbor_cost
    * Modified ShowOspfv3Interface
        * Modified regex patterns p1_1, p1_3, p1_4 and p1_15 to accommodate various outputs
        * Added parsing for cost_hysteresis and neighbor_cost
    * Modified ShowDlepNeighborsSchema
        * Made dlep_server, sid optional
        * Added dlep_local optional key
    * Modified ShowDlepNeighbors
        * Modified regex patterns to accommodate various inputs
    * Modified ShowDlepClientsSchema
        * Made dlep_server key optional
        * Modified dlep_client key
    * Modified ShowDlepClients
        * Updated regex patterns to accommodate various inputs
    * Modified ShowCispSummary
        * modified parser to handle cisp enabled, running state
    * Modified ShowL2vpnEvpnDefaultGatewayDetailSchema
        * Made eth_tag as optional parameter to support ShowL2vpnEvpnDefaultGateway
    * Modified ShowPlatformSoftwareFedQosInterfaceSuperParser
        * Modified parser to match sub interfaces and unit test added
    * Modified ShowL2vpnEvpnEviDetail
        * Made 'mac_routes' and 'mac_ip_routes' as optional. Added unit test.
    * Modified ShowTemplateBindingTarget
        * Fixed regular expression and unit test added
    * Modified ShowIdpromInterface
        * parsing more information from the output
    * Modified ShowL2fibBridgeDomainDetail Parser
        * Fixed p10 regex pattern
    * Modified ShowDerivedConfigInterface
        * Added some more parsing capabilities
    * Modified ShowIpNatTranslations
        * Fixed parser to hadle sigle table entry for show ip nat translations
    * Modified ShowIpHttpServerAll
        * Fix p21_3, p21_5, p21_9 regex
    * Modified ShowPlatformSudiCertificateNonce
        * Updated pattren <p5> to accommodate other outputs
    * Modified ShowPolicyMap
        * Added rate key under policy and added unit test.
    * Modified ShowPlatformSoftwareFedQosInterfaceSuperParser
        * Fix regex pattern to match sub interface
    * Modified ShowPlatformHardwareFedSwitchQosQueueStatsInterface
        * Fix regex pattern to match sub interface
    * Modified ShowBgp
        * Added support for parser show bgp {address_family} evi {evi}
    * Modified ShowDeviceSensor
        * Fixed Regex patterns p1 and p2
    * Modified ShowDeviceTrackingCountersInterface
        * Added optional key "reason"
    * Modified ShowDeviceTrackingCountersVlan
        * Added optional key "reason"
    * Modified ShowPlatformSoftwareFedActiveAclInfoSummary
        * added 'feature' key as Optional and added unit test. New change in 17.12
    * Modified ShowControllerEthernetController
        * Modified cli as show controllers ethernet-controller {interface} previously it is like show controller ethernet-controller {interface}. Due to controller getting error as ambiguous command.
    * Modified ShowIpDhcpSnoopingBinding
        * added 'show ip dhcp snooping binding interface {interface}'
        * added 'show ip dhcp snooping binding {mac}'
        * added 'total_bindings' key to parser total number of bindings
    * Modified ShowPlatformSoftwareWiredClientSwitchR0.
    * modified the parser file show_platform.py.
    * Modified ShowAccessSession.
    * modified the parser file show_access_session.py.
    * Modified ShowPlatformSoftwareFedSwitchActiveMatmAdjacenciesAdjkey
        * Added "show platform software fed active matm adjacencies adjkey {adj_key}"
    * Modified ShowPlatformSoftwareFedSwitchActiveMatmAdjacenciesVlan
        * Added "show platform software fed active matm adjacencies vlan {vlan_id}"
    * Modified ShowIdpromTanSchema and ShowIdpromTanParser
        * Modified schema class to change revision_num type from int to str
        * Modified parser class to store revision_num as str
        * Modified parser class p3 regex pattern for revision_num to accept hex values with '\w+'.

* common
    * Modified interface conversion method
        * Added `ignore_case` option to match interface name case insensitive

* iosxr
    * Modified ShowIsisInterface
        * Added <r63> pattern to match 'Measured Delay           Min- Avg- Max- usec'
        * Added <r63> pattern to match 'Normalized Delay         Min- Avg- Max- usec'
        * Added 'measured_delay' parameter as optional parameter to schema
        * Added 'normalized_delay' parameter as optional parameter to schema
    * Modified ShowIsisDatabaseDetail
        * Added 'mt_srv6_locator' as Optional parameter to schema
        * Added 'locator_prefix', 'locator_prefix_length', 'd_flag', 'metric', and 'algorithm' parameters inside 'mt_srv6_locator' in schema
        * Added <r25> pattern to match 'SRv6 Locator   MT (IPv6 Unicast) fc00c0001001/48 D0 Metric 0 Algorithm 0'
    * Added ShowMkaPolicy
        * Added parser for show mka policy
    * Modified ShowRouteIpv6
        * Added behaviour as Optional parameter to schema.
        * Modified pattern <p2> to match 'L    fc00c0001001/64, SRv6 Endpoint uN (PSP/USD)'
        * Modified pattern <p3> to match '[0/0] via ffff0.0.0.0 (nexthop in vrf SRV6_L3VPN_BE), 230919'

* modified the showplatformsoftwarewiredclientswitchr0 regex pattern to proper output.

* modified the showaccesssession to match when there is no session exist.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPerformanceMeasurementResponderCounters
        * show performance-measurement responder counters interface
        * show performance-measurement responder counters interfaces name {name}
    * Added ShowPerformanceMeasurementResponderInterfaces
        * show performance-measurement responder interfaces
        * show performance-measurement responder interfaces name {name}
    * Added ShowPerformanceMeasurementResponderSummary
        * show performance-measurement responder summary
    * Added ShowInterfacesCapabilities
        * parser for show interfaces {interface} capabilities
    * Added ShowPlatformSoftwareIgmpSnoopingGroupsCount
        * parser for ShowPlatformSoftwareIgmpSnoopingGroupsCount
    * Added ShowPlatformSoftwareMldSnoopingGroupsCount
        * parser for ShowPlatformSoftwareMldSnoopingGroupsCount
    * Added ShowVlanBrief
        * show vlan brief
    * Added ShowCryptoMap
        * parser for show crypto map
    * Added ShowAccessSessionMacDetails
        * parser for show access-session mac {mac} details
        * show access-session mac {mac} details switch {mode} {rp_slot}
        * show access-session interface {interface} details switch {mode} {rp_slot}
    * Added ShowIpHttpServerAll
        * parser for show ip http server all
    * Added ShowIpHttpServerSecureStatus
        * parser for show ip http server secure status
    * Modified ShPlatformSoftwareFedActiveVpSummaryInterfaceIf_id
        * Added 'switch' and 'mode' input variables to support switch command
    * Modified ShowFlowMonitorCache
        * Added 'ip_tos' optional key to grep ip tos
    * Added  ShowPlatformSoftwareBpCrimsonStatistics Parser
        * Parser for "show platform software bp crimson statistics"
    * Added ShowPlatformSoftwareNodeClusterManagerSwitchB0Local Parser
        * Parser for "show platform software node cluster-manager switch {mode} B0 local"
    * Added ShowSdwanServiceChainDatabase parser
        * Parser for "show platform software sdwan service-chain database"
    * Added ShowIdpromTan for 9500X
    * Added ShowIpv6NdRoutingProxy  parser
        * Parser for "show ipv6 nd routing-proxy"
    * Added ShowBgpL2vpnEvpnSummary
        * parser for show bgp l2vpn evpn summary
    * Added ShowIpVerifySource for c9300
        * parser for show ip verify source
    * Added ShowVersionMode
        * parser for show version {mode}
        * parser for show version {switch} {sw_number} {route_processor} {mode}
    * Added ShowPlatformSoftwareFedQosInterfaceIngressNpiDetailed Parser
        * Parser for show platform software fed {switch} {mode} qos interface {interface} ingress npi detailed
    * Added ShowPlatformSoftwareFedSecurityFedIpsgIfId
        * show platform software fed {switch} {mode} security-fed ipsg if-id {if_id}
        * show platform software fed {mode} security-fed ipsg if-id {if_id}
    * Added ShowIpv6EigrpTopologyEntrySchema
        * show ipv6 eigrp topology {ipv6_subnet}
    * Added ShowPlatformHardwareQfpStatisticsDropClear
        * show platform hardware qfp {status} statistics drop clear
    * Added ShowPlatformSoftwareAuditSummary
        * added parser for show platform software audit summary
    * Added ShowL2vpnEvpnDefaultGateway
        * parser for show l2vpn evpn default-gateway
    * Added ShowHardwareLedPortMode Parser
        * Parser for show hardware led port {port} {mode}
    * Added ShowCispRegistrations Parser
        * Parser for "show cisp registrations"
    * Added ShowLldpNeighborsInterfaceDetail
        * show lldp neighbors {interface} detail
    * Added ShowAdjacencyInterfaceDetail
        * show adjacency interface detail
        * show adjacency interface <interface> id <id> detail
        * show adjacency interface <interface> id <id> prefix <prefix> detail
    * Added ShowAdjacencyVlanLinkDetail
        * show adjacency vlan <id> detail
        * show adjacency vlan <id> prefix <prefix> detail'
        * show adjacency vlan <id> prefix <prefix> link protocol <protocol> detail
    * Added ShowAppHostingDetailAppid
        * parser for show app-hosting detail appid {appid}
    * Added ShowMplsTrafficEngTopology
        * parser for show mpls traffic-eng topology
    * Added ShowIpIgmpSnoopingVlan Parser
        * Parser for "show ip igmp snooping vlan {vlan}"
    * Added ShowPlatHardFedActiveQosQueueStatsOqMulticastAttach
        * show platform hardware fed active qos queue stats oq multicast attach
    * Modified ShowCryptoIkev2SaDetail parser
        * IOS Change in output syntax "Quantum-Safe Encryption using PPK is enabled" insted "Quantum Resistance Enabled"
    * Added ShowPost
        * 9300 parser for 'show post'
    * Added ShowXfsuStatus
        * parser for show xfsu status
    * Added ShowGracefulReload
        * parser for show graceful-reload
    * Added ShowFlowMonitorCheck
        * show flow monitor
    * Added ShowCryptoIpsecSaInterface Parser
        * Parser for show crypto ipsec sa interface {interface}
    * Added new parser 'show device-sensor details'
    * Added ShowBeaconAll
        * Parser for show beacon all to check the beacon status.
    * Added ShowAppHostingResource
        * parser for show app-hosting resource
    * Added ShowSpanningTreeSummaryTotals
        * parser for show spanning-tree summary totals

* iosxr
    * Added ShowFrequencySynchronizationInterfaces
        * Added new parser for cli show frequency synchronization interfaces
        * Added new parser for cli show frequency synchronization interfaces {interface}
    * Added ShowRunSectionMacAddress
        * Parser for cli 'show running-config | section mac address'
    * Added ShowBgpVrfAfPrefix Parser
        * Parser for "show bgp vrf {vrf_name} {address_family} {prefix}"
        * Parser for "show bgp {address_family} vrf {vrf_name} {prefix}"
    * Added ShowBgpVrfAfPrefixDetail Parser
        * Parser for "show bgp vrf {vrf_name} {address_family} {prefix} detail"


--------------------------------------------------------------------------------
                                     Modify                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpMfib
        * show ip mfib vrf {vrf}
            * Add if condition to handle the 'NA' as output
    * Modified ShowPlatformSoftwareFedSwitchMatmStats
        * added support for 'show platform software fed active matm stats'


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowDiagnosticPost parser
        * added parser for show diagnostic post


