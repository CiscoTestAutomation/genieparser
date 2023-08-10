--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* nxos
    * Added ShowDiagnosticContentModule
        * show diagnostic content module {mod_num}
    * Added ShowDiagnosticResultModuleTestDetail
        * show diagnostic result module {mod_num} test {include} detail

* iosxe
    * Added ShowPlatformSoftwareFedQosInterfaceEgressNpdDetailed
        * parser for show platform software fed {switch} {mode} qos interface {interface} egress npd detailed
    * Added ShowInterfacesVlanMapping
        * show interface {interface} vlan mapping
    * Added ShowLoggingProcessSmdReverse
        * parser for show logging process smd reverse
        * show logging process smd {switch} {mode} reverse
    * Added ShowPolicyMapTypeQueueingPolicyname
        * parser for show policy-map type queueing {policy_name}
    * Added ShowEeeCapabilitiesInterface
        * show eee capabilities interface <interface-id>
    * Added ShowEeeStatusInterface
        * show eee status interface <interface-id>
    * Added ShowIpv6cefExactRoute Parser
        * parser for show ipv6 cef exact route
    * Added ShowConsistencyCheckerMcastStartAll
        * "show consistency-checker mcast {layer} start all"
        * "show consistency-checker mcast {layer} start {address} {source}"
        * "show consistency-checker mcast {layer} start vrf {instance_name} {address} {source}"
        * "show consistency-checker mcast {layer} start vlan {vlan_id} {address}"
    * Added ShowConsistencyCheckerRunIdDetail
        * "show consistency-checker run-id {id} detail"
    * Added ShowConsistencyCheckerRunId
        * "show consistency-checker run-id {id}"
    * Added SnmpGetIfIndex Parser
        * Parser for "snmp get v{version} {ip} {community_str} oid {mibifindex}"
    * Added ShowPlatformSoftwareCefIpVrf Parser
        * Parser for show platform software cef {protocol} vrf {option} {ip} {mask} feature-all
    * Added ShowOspfv3RibRedistribution
        * added parser for show ospfv3 rib redistribution
    * Added ShowPlatform
        * updated regex for p6 to capture state
    * Modified ShowPlatformHardwareAuthenticationStatus
        * Added Line card 4 authentication status for 9400 switch.
    * Added ShowControllersEthernetController
        * parser for show controllers ethernet-controller
    * Added ShowPlatformHardwareFedQosQueueStatsOqMulticast
        * parser for show platform hardware fed {switch} {mode} qos queue stats oq multicast interface {interface} oq_id {oq_id}
    * Added ShowPlatformHardwareFedQosQueueStatsOqMulticastOqId
        * parser for show platform hardware fed {switch} {mode} qos queue stats oq multicast interface {interface} oq_id {oq_id} clear-on-read
    * Added ShowL2routeEvpnMulticastSmet
        * show l2route evpn multicast smet
        * show l2route evpn multicast smet topology <evi>
        * show l2route evpn multicast smet topology <evi> group <group>
        * show l2route evpn multicast smet topology <evi> group <group> local
        * show l2route evpn multicast smet topology <evi> group <group> local interface <interface>
        * show l2route evpn multicast smet topology <evi> group <group> local interface <interface> service-instance <serviceInstance>
        * show l2route evpn multicast smet topology <evi> group <group> remote
        * show l2route evpn multicast smet topology <evi> group <group> remote originator <originator-addr>
        * show l2route evpn multicast smet topology <evietag>
        * show l2route evpn multicast smet topology <evietag> group <group>
        * show l2route evpn multicast smet topology <evietag> group <group> local
        * show l2route evpn multicast smet topology <evietag> group <group> local interface <interface>
        * show l2route evpn multicast smet topology <evietag> group <group> local interface <interface> service-instance <serviceInstance>
        * show l2route evpn multicast smet topology <evietag> group <group> remote
        * show l2route evpn multicast smet topology <evietag> group <group> remote originator <originator-addr>
    * Added ShowL2routeEvpnMulticastRoute
        * show l2route evpn multicast route
        * show l2route evpn multicast route topology <evi>
        * show l2route evpn multicast route topology <evi> group <group>
        * show l2route evpn multicast route topology <evi> group <group> source <source>
        * show l2route evpn multicast route topology <evietag>
        * show l2route evpn multicast route topology <evietag> group <group>
        * show l2route evpn multicast route topology <evietag> group <group> source <source>
    * Added ShowL2routeEvpnImet
        * show l2route evpn imet
        * show l2route evpn imet topology <evi>
        * show l2route evpn imet topology <evi> producer <producer>
        * show l2route evpn imet topology <evi> producer <producer> origin-rtr <originator-addr>
    * Added ShowPlatformSoftwareFedPuntEntries Parser
        * Parser for show platform software fed {switch} {mode} punt entries
    * Added ShowPlatformHardwareFedQosSchedulerSdkInterface Parser
        * parser for 'show platform hardware fed {mode} qos scheduler sdk interface {interface}'
        * 'show platform hardware fed {switch} {mode} qos scheduler sdk interface {interface}'
    * Added ShowLoggingOnboardSwitchMessageDetail
        * for 'show logging onboard rp {switch_type} message detail'
    * Added ShowLoggingOnboardSwitchEnvironmentDetail
        * for 'show logging onboard rp {switch_type} environment detail'
    * Added ShowLoggingOnboardSwitchCounterDetail
        * show logging onboard rp {switch_type} counter detail'
    * Added ShowLoggingOnboardSwitchClilogDetail
        * for 'show logging onboard rp {switch_type} clilog detail'
    * Added ShowFileSys
        * parser for show {filesystem} filesys
    * Added ShowInterfaceCounterErrors Parser
        * Parser for show interfaces {interface} counters errors
    * Added ShowSdwanTenantOmpRoutes Parser
        * Parser for show sdwan tenant {tenant} omp routes
    * Added ShowSdwanTenantOmpPeers Parser
        * Parser for show sdwan tenant {tenant} omp peers
    * Added ShowSdwanTenantSumary Parser
        * Parser for show sdwan tenant-summary
    * Added ShowL2fibBdTableMulticast
        * show l2fib bridge-domain {id} table multicast
    * Added ShowL2fibBdAddressMulticast
        * show l2fib bridge-domain {id} address multicast {address/prefix}
    * Added ShowL2fibBdTableUnicast
        * show l2fib bridge-domain {id} table unicast
    * Modified ShowL2fibBridgeDomainDetail
        * Added missing fields back, added missing Optionals
    * Modified ShowCryptoIkev2Stats
        * show crypto ikev2 stats
    * Added ShowInterfaceFlowControl
        * show show interface flowcontrol
    * Added ShowDot1xInterfaceStatistics Parser
        * Parser for "show dot1x interface {interface} statistics"
    * Added ShowFlowMonitorCacheFilterInterface
        * parser for show flow monitor {name} cache filter {int_type} {direction} {interface_name} sort highest {int_type} {direction} {top}
    * Added ShowIpOspfDatabaseOpaqueAreaTypeTrafficEngineeringSelfOriginate Parser
        * Parser for "show ip ospf database opaque-area type traffic-engineering self-originate"
    * Added new parser 'show ipv6 dhcp relay binding'
    * Added ShowPlatformHardwareCryptoDeviceUtilization Parser
        * Parser for show platform hardware crypto-device utilization
    * Added ShowPlatformHardwareQfpActiveClassificationFeatureTcamUsage Parser
        * Parser for show platform hardware qfp active classification feature tcam-usage
    * Added ShowSdwanServiceChainStats parser
        * Parser for "show platform hardware qfp active feature sdwan datapath service-chain stats"
    * Added ShowSdwanPolicyDataPolicyFilter parser
        * Parser for "show sdwan policy data-policy-filter"
    * Added ShowSdwanMulticastRemoteNodes Parser
        * Parser for "show platform software sdwan multicast remote-nodes vrf {vrf ID}"
    * Added ShowSdwanMulticastReplicators Parser
        * Parser for "show platform software sdwan multicast replicators vrf {vrf_ID}"
    * Added  ShowMgmtTrafficControlIpv4 parser
        * Parser for "show mgmt-traffic control ipv4"
    * Added ShowPlatformSoftwareFedSwitchQosPolicyTargetStatus
        * show platform software fed switch {switch} qos policy target status
    * Added ShowDhcpLease Parser
        * Parser for "show dhcp lease"
    * Added ShowPerformanceMeasurementInterfaces
        * show performance-measurement interfaces
        * show performance-measurement interfaces detail
        * show performance-measurement interfaces private
        * show performance-measurement interfaces {multiple}
        * show performance-measurement interfaces name <name>
        * show performance-measurement interfaces name <name> {multiple}

* iosxr
    * Added ShowIsisInterfaceBrief Parser
        * Parser for "show isis interface brief"
    * Added ShowIpBgp
        * Parser for cli 'show ip bgp {route}'
    * Added ShowIsisDatabase
        * Parser for cli 'show isis databse'


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowLicenseRumIdDetail
        * The schema is changed to make the 'feature_name' and 'metric_value'
    * Modified ShowCtsRoleBasedPermissions Parser
        * Fix parser issue with p1, p2 and formatted to new parser format.
    * Modified ShowRunInterface
        * added addtional optional keys to schema
    * Modified ShowSpanningTree
        * Fix p10 reg ex
    * Modified ShowArp
        * Fix p1 reg ex and added optional variable private_vlan
    * Modified ShowL2vpnEvpnMac
        * added local and remote optional variables to consider local and remote commands
    * Modify ShowIpv6MldSnoopingMrouterVlan
        * show ipv6 mld snooping mrouter vlan {vlanid}
    * Modified ShowCispRegistrations Parser
        * Added support to extract dot1x value
    * Modified ShowCdpEntry Parser
        * Made native_vlan as optional
    * Modified ShowInterfacesSwitchport
        * Fixed the schema by making 'switchport_mode' key optional
    * Modified ShowTelemetryIETFSubscriptionAllReceivers
        * fixed parser issue when "explanation" field is empty
    * Modified ShowIsisRib
        * Modified parser to handle subinterfaces
    * Modified ShowPolicyMapTypeSuperParser
        * Fix p11_2 and p41
    * Modified ShowPlatformSoftwareFedQosInterfaceSuperParser
        * Modified regex p1 and p7_1
    * Modified ShowLispSiteSuperParser
        * Added support for 2-line display of registration when ETR address is too long
    * Modified ShowLispSiteDetailSuperParser
        * Added support for parsing 'any-mac' as EID-prefix
    * Modified ShowCryptoCallAdmissionStatistics
        * Modified schema to support new values for SA Strength Enforcement Rejects
    * Added ShowLispIpv4Publisher
        * Updated regex pattern p2 for ipv4 publisher output with ems type
    * Added ShowLispIpv6Publisher
        * Updated regex pattern p2 for ipv6 publisher output with ems type
    * Added ShowLispEthernetPublisher
        * Updated regex pattern p2 for ethernet publisher output with ems type
    * Modified ShowPlatformSoftwareWiredClientSwitchR0
        * fix p1 regular expression
    * Modified ShowCdpNeighborsDetail Parser
        * Added support for show cdp neighbors {interface} detail
    * Modified ShowIpv6Mfib Parser
        * Fix p8 regex
        * added optional variables 'egress_vxlan_vni' and 'egress_vxlan_nxthop'
    * Added parames as optional for few keys.
        * Made fail_close_revert, pfs_rekey_received, anti_replay_count are optional.
        * Fixed regexp more generic to match G-IKEv2 syntax.
    * Updated ShowRomvar Parser to support new keys real_mgmte_dev, sr_mgmt_vrf,

* iosxr
    * Modified ShowCefDetail
        * Added support for cli 'show cef vrf {vrf_name} {ip_type} {prefix} detail' in ShowCefDetail
    * Modified ShowIsisProtocol
        * Modified 'level' parameter as optional parameter in schema
    * Modified show_static_routing and show rpl route-policy
        * Updated pattren <p2> for show_static_routing to accommodate with other outputs
        * Updated regex pattern <route-type> for show rpl route-policy to accommodate various outputs.
    * Modified ShowOspfInterface
        * Added <p30> pattern to match 'LDP Sync Enabled, Sync Status Achieved'
        * Modified <p3> pattern to support 'GigabitEthernet0/0/0/2 is administratively down, line protocol is down'

* ios/iosxe
    * Modified ShowVersion
        * Updated regex pattern p1_1 to accommodate legacy platform


--------------------------------------------------------------------------------
                                     Modify                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterface
        * added support for 'show platform software fed active ptp interface'


