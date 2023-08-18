--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowWirelessMeshApBackhaul
        * show wireless mesh ap backhaul
    * Added ShowWirelessTagSiteSummary
        * show wireless tag site summary
    * Added ShowWirelessProfileFlexSummary
        * show wireless profile flex summary
    * Added ShowNmspStatus
        * show nmsp status
    * Added ShowAppHostingDetail
        * show app=hosting detail
    * Added ShowApBleSummary
        * show ap ble summary
    * Added ShowAwipsStatus
        * show awips status {mac_address}
    * Added ShowRomMonSwitchR0
        * parser for show rom-mon switch {switch_num} {process}
    * Added ShowIpOspfRibRedistribution
        * added parser for "show ip ospf rib redistribution"
    * Fixed ShowIpOspfDatabaseExternal
        * added metric_type to the parser "show ip ospf database external"
    * Added ShowIpv6OspfInterface
        * Parser for show ipv6 ospf interface {interface}
    * Added ShowIpv6OspfNeighborDetail
        * Parser for show ipv6 ospf neighbor detail
    * Added ShowL2vpnAtomVc
        * Parser show l2vpn atom vc
    * Added ShowLispPlatformSmrKnownLocatorsParser
        * Parser for "show lisp platform smr known locators"
    * Added ShowLispDecapsulationFilterParser
        * Parser for "show lisp instance-id <iid> decapsulation filter"
    * Updated ShowLispServiceRlocMembers
        * Made field "members" optional in ShowLispServiceRlocMembersSchema
        * Fixed incorrect CLI
    * Updated ShowLispServiceSmr
        * Fixed incorrect CLI
        * Made field "prefixes" optional in ShowLispServiceSmrSchema
    * Updated ShowLispPublisherSuperParser
        * Added support for "?" for field "type"
    * Updated ShowIpv6CefInternal parser
        * Added support for parsing LISP smr state "smr_enabled" in "subblocks"
    * Updated ShowLispIpMapCachePrefixSuperParser
        * Added support for parsing 2-digit expiration time in the format of xdxxh
    * Added ShowPlatformHardwareFedSwitchQosQueueStatsInterface
        * parser for 'show platform hardware fed active qos queue stats interface {interface}'
        * parser for 'show platform hardware fed switch {switch_num} qos queue stats interface {interface}'
    * Added ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear
        * parser for 'show platform hardware fed active qos queue stats interface {interface} clear'
        * parser for 'show platform hardware fed switch {switch_num} qos queue stats interface {interface} clear'
    * Added ShowPerformanceMeasurementSrPolicy
        * show performance-measurement sr-policy
        * show performance-measurement sr-policy detail
        * show performance-measurement sr-policy private
        * show performance-measurement sr-policy verbose
        * show performance-measurement sr-policy detail verbose
        * show performance-measurement sr-policy detail private
        * show performance-measurement sr-policy private verbose
        * show performance-measurement sr-policy detail private verbose
        * show performance-measurement sr-policy name <name>
    * Added ShowControllerVDSLlocal parser
        * Parser for "show controller vdsl {interface} local "
    * Added ShowIpNatRedundancy Parser
        * Parser for "show ip nat redundancy"
    * Added ShowIpPimAutorp Parser
        * Parser for "show ip pim vrf {vrf ID} autorp"
    * Added ShowSdwanClientInterface Parser
        * Parser for "show platform hardware qfp active feature sdwan client interface <interface name>"
    * Added ShowSdwanOmpMulticastRoutes Parser
        * Parser for "show sdwan omp multicast-routes"
    * Added ShowSdwanOmpMulticastAutoDiscover Parser
        * Parser for "show sdwan omp multicast-auto-discover"
    * Added ShowSdwanSecurityInfo Parser
        * Parser for "show sdwan security-info"

* iosxr
    * Added ShowSegmentRoutingSrv6Locator
        * parser for 'show segment-routing srv6 locator'
        * parser for 'show segment-routing srv6 locator {locator_name}'

* nxos
    * Added ShowHardwareInternalTctrlUsdDpllState
        * parser for 'show hardware internal tctrl_usd dpll state'

* viptela
    * Added ShowOrchestratorReverseProxyMapping Parser
        * Parser for "show orchestrator reverse-proxy-mapping"


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowAvcSdServiceInfoSummary
        * Added support for secondary address
        * Added support for Never in last connection
        * Added support for case when status is DISCONNECTED but IP is given
        * Simplified parsing
    * Modified ShowFabricApSummary
        * Added support for IPv6 for IP address
        * Added support for spaces by creating more adecuate regex
        * Added support for different join states
        * Simplified parsing
    * Modified ShowLispIpMapCachePrefixSuperParser
        * Added some enhancement
    * Modified ShowLisp
        * Added some enhancement for capability list
    * Modified ShowLispInstanceIdService
        * Added some enhancement
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressNpiDetailed
        * made 'mark_value' and 'mark_type' as optional keywords
    * Modified ShowKeyChain Parser
        * Modified key id regex to accept both string and numeric keys
        * Added 3 new fields - whether keychain is macsec, cryptographic algorithm of key chain and lifetime of macsec keychain
    * Modified ShowPolicyMapTypeSuperParser Parser
        * Fixed p14_1 regex
    * Modified ShowDeviceTrackingCountersVlan Parser
        * Fixed dropped_message_info regex
    * Modified ShowDlepNeighbors
        * Updated schema and parser to accommodate multiple neighbors under same interface
    * Modified ShowIpv6Mfib Parser
        * Fix p8 regex
        * Added support for L2LISP v6 decapsulation on interface L2LISP0.1502
    * Modified ShowMonitorCaptureBufferDetailed Parser
        * Added new cli
        * Added 3 new keys in Schema
    * Modified ShowMonitorCaptureBuffer Parser
        * Added new cli
    * Modified ShowSdmPrefer Parser
        * Modified macsec_spd_entries key as Optional to support NAT template
    * Modified ShowPolicyMapTypeQueueingPolicyname Parser
        * parsing some more data 'cir_bps', 'bandwidth_remaining_ratio', 'priority_level'
        * made 'class_val' as optional
    * Modified ShowRunInterface
        * Added 109 and 110 regex for sampler outputs
    * Modified ShowRunAllSectionInterface Parser
        * Added 6 new fields - macsec_enabled,macsec_access_control, mtu, mka_policy, mka_primary_keychain, mka_fallback_keychain
    * Modified ShowRunInterface Parser
        * Added 6 new fields - macsec_enabled,macsec_access_control, mtu, mka_policy, mka_primary_keychain, mka_fallback_keychain
    * Modified ShowRunningConfigNve
        * added optional key 'arp_ndp_suppression'
        * extended optional key 'learn_ip_addr' to l2vpn_global dictionary
    * Modified ShowVersion Parser
        * Modified key id regex to accept optional string
    * Modified ShowLispPublisherSuperParser and ShowLispPublisherSuperParserSchema
        * Making "type" optional for backward compatibility
        * Adding unit test for output without the type column
    * Modified show l2route evpn multicast smet
        * Removed <evi_etag> containing CLI commands which are not required anymore
    * Fix for ShowCryptoIkev2SaDetail parser
        * IOS Change in output syntax "Quantum-safe Encryption using Manual PPK" and "Quantum-safe Encryption using Dynamic PPK"
    * Modified ShowIpv6Mfib
        * Modified p8 to support ipv6 vxlan nexthop address
    * Modified ShowOspfv3Interface
        * Updated regex pattern <p1_1> to accommodate all types of interface indices.

* ios
    * Modified ShowKeyChain Parser
        * Added old parser code here as that code is matching output of ios show command

* iosxr
    * Modified show cef details

* added <drop>, <source_rib> keywords in schema as optional and changed <load_distribution>, <weight_distribution> as optional.
    * Changed the regex pattern for <p1>, <p4>, <p8>, <p9>.

* nxos
    * Modified show access-lists summary
    * Modified ShowModule
        * Modified the line of code and regex pattern for p3,p4
        * Changed the golder_output2_expected.py file value
    * Modified ShowInterfaceStatus
        * Modified the line code and regex pattern for p1
    * Modified ShowIpEigrpTopology
        * Fix issue in cli command list
    * Modified ShowIpv6EigrpTopology
        * Fix issue in cli command list
    * Fix for ShowModule parser
        * Updated regex for much more tightly controlled matching

* updated <statistics>, <fragments> in schema as optional.
    * Changed the regex pattern for output.

* fixed unexpected argument error when cli method of class showl2routeevpnmulticastsmet called


--------------------------------------------------------------------------------
                                    New/Fix                                     
--------------------------------------------------------------------------------

* iosxe
    * Added ShowLispSubscription
        * show lisp instance-id {instance_id} ipv4 subscription
        * show lisp {lisp_id} instance-id {instance_id} ipv4 subscription
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 subscription
        * show lisp eid-table {eid_table} ipv4 subscription
        * show lisp eid-table vrf {eid_table} ipv4 subscription
        * show lisp instance-id {instance_id} ipv6 subscription
        * show lisp {lisp_id} instance-id {instance_id} ipv6 subscription
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 subscription
        * show lisp eid-table {eid_table} ipv6 subscription
        * show lisp eid-table vrf {eid_table} ipv6 subscription
        * show lisp instance-id {instance_id} ethernet subscription
        * show lisp {lisp_id} instance-id {instance_id} ethernet subscription
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet subscription
        * show lisp eid-table {eid_table} ethernet subscription
        * show lisp eid-table vrf {eid_table} ethernet subscription
    * Added ShowLispServerSubscription
        * show lisp instance-id {instance_id} ipv4 server subscription
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server subscription
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server subscription
        * show lisp eid-table {eid_table} ipv4 server subscription
        * show lisp eid-table vrf {eid_table} ipv4 server subscription
        * show lisp instance-id {instance_id} ipv6 server subscription
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server subscription
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server subscription
        * show lisp eid-table {eid_table} ipv6 server subscription
        * show lisp eid-table vrf {eid_table} ipv6 server subscription
        * show lisp instance-id {instance_id} ethernet server subscription
        * show lisp {lisp_id} instance-id {instance_id} ethernet server subscription
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server subscription
        * show lisp eid-table vlan {eid_table} ethernet server subscription


