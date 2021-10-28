--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* nxos
    * Modified ShowTrackBrief
        * Added parser for
            * show track interface brief
            * show track ip sla brief
            * show track ip route brief
            * show track ipv6 route brief
    * added ShowTrackListBrief
        * show track list boolean and brief
        * show track list boolean or brief
        * show track list threshold percentage brief
        * show track list threshold weight brief

* iosxe
    * Added ShowEnvironmentStatus
        * show environment status
    * Added ShowPlatformSudiCertificate
        * show platform sudi certificate sign nonce {signature}
    * Added class ShowLispIpv6Publication
        * show lisp instance-id {instance_id} ipv6 publication
        * show lisp {lisp_id} instance-id {instance_id} ipv6 publication
        * show lisp eid-table {eid-table} ipv6 publication
        * show lisp eid-table vrf {vrf} ipv6 publication
        * show lisp locator-table {vrf} instance-id {instance-id} ipv6 publication
    * Added ShowStormControl
        * added a new parser to parse 'show storm-control {interface}' output on IOS XE devices
    * Added class ShowLispEthernetPublication
        * show lisp instance-id {instance_id} ethernet publication
        * show lisp {lisp_id} instance-id {instance_id} ethernet publication
        * show lisp locator-table {vrf} instance-id {instance-id} ethernet publication
    * Added class ShowLispEthernetPublicationPrefix
        * show lisp instance-id {instance_id} ethernet publication {eid_prefix}
        * show lisp {lisp_id} instance-id {instance_id} ethernet publication {eid_prefix}
        * show lisp eid-table vlan {vlan} ethernet publication {eid_prefix}
        * show lisp locator-table {vrf} instance-id {instance_id} ethernet publication {eid_prefix}
        * show lisp locator-table vrf {vrf} instance-id {instance_id} ethernet publication {eid_prefix}
    * Added ShowUdldInterface
        * show udld interface {interface}
    * Added ShowUdldNeighbor
        * show udld neighbor
    * ShowLispIpv4PublisherRloc
        * show lisp {lisp_id} instance-id {instance_id} ipv4 publisher {publisher_id}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 publisher {publisher_id}
        * show lisp instance-id {instance_id} ipv4 publisher {publisher_id}
        * show lisp eid-table {eid_table} ipv4 publisher {publisher_id}
        * show lisp eid-table vrf {vrf} ipv4 publisher {publisher_id}
        * show lisp eid-table vrf ipv4 publisher {publisher_id}
    * Added ShowLispPrefixList
        * show lisp prefix-list
        * show lisp prefix-list {prefix_list_name}
        * show lisp {lisp_id} prefix-list
        * show lisp {lisp_id} prefix-list {prefix_list_name}
    * Added ShowParser
        * show parser encrypt file status
    * Added ShowBootSystem
        * show boot system
    * Added ShowPost
        * show post
    * Added ShowPlatformHardwareQfpActiveFeatureSdwanDpFecGlobal
        * show platform hardware qfp active feature sdwan datapath fec global
    * Added ShowPlatformHardwareQfpActiveFeatureSdwanDpFecSessionSummary
        * show platform hardware qfp active feature sdwan datapath fec session summary
    * Added ShowSdwanAppRouteSlaClass
        * show sdwan app-route sla-class
        * show sdwan app-route sla-class name <name>
    * Added ShowSdwanAppRouteStatistics
        * show sdwan app-route stats local-color <color>
        * show sdwan app-route stats remote-color <color>
        * show sdwan app-route stats remote-system-ip <ip>
    * Added ShowSdwanTunnelSla
        * show sdwan tunnel sla
        * show sdwan tunnel sla index <index>
        * show sdwan tunnel sla name <name>
        * show sdwan tunnel remote-system-ip <ip> sla
    * Added ShowSdwanTunnelStatistics
        * show sdwan tunnel statistics
        * show sdwan tunnel statistics fec
        * show sdwan tunnel statistics bfd
        * show sdwan tunnel statistics ipsec
        * show sdwan tunnel statistics pkt-dup
        * show sdwan tunnel statistics table
    * Added ShowSdwanSystemOnDemand
        * show sdwan system on-demand
        * show sdwan system on-demand remote-system
        * show sdwan system on-demand remote-system system-ip <ip>
    * Added ShowSdwanAppqoeServiceControllers
        * show sdwan appqoe service-controllers
    * Added ShowServiceInsertionTypeAppqoeClusterSummary
        * show service-insertion type appqoe cluster-summary
    * Added class ShowLispARDetailParser
        * show lisp instance-id {instance_id} ethernet server address-resolution {eid}
        * show lisp {lisp_id} instance-id {instance_id} ethernet server address-resolution {eid}
        * show lisp eid-table vlan {vlan} ethernet server address-resolution {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server address-resolution {eid}
        * show lisp locator-table vrf {vrf} instance-id {instance_id} ethernet server address-resolution {eid}
        * show lisp instance-id {instance_id} ethernet server address-resolution detail
        * show lisp {lisp_id} instance-id {instance_id} ethernet server address-resolution detail
        * show lisp eid-table vlan {vlan} ethernet server address-resolution detail
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server address-resolution detail
        * show lisp locator-table vrf {vrf} instance-id {instance_id} ethernet server address-resolution detail
    * Added ShowPowerInlineConsumption
        * show power inline consumption
        * show power inline consumption {interface}
    * Added ShowLispIpv4RouteImportMapCache
        * 'show lisp instance-id {instance_id} ipv4 route-import map-cache'
        * 'show lisp instance-id {instance_id} ipv4 route-import map-cache {eid}'
        * 'show lisp instance-id {instance_id} ipv4 route-import map-cache {eid_prefix}'
        * 'show lisp {lisp_id} instance-id {instance_id} ipv4 route-import map-cache'
        * 'show lisp {lisp_id} instance-id {instance_id} ipv4 route-import map-cache {eid}'
        * 'show lisp {lisp_id} instance-id {instance_id} ipv4 route-import map-cache {eid_prefix}'
        * 'show lisp eid-table vrf {vrf} ipv4 route-import map-cache'
        * 'show lisp eid-table vrf {vrf} ipv4 route-import map-cache {eid}'
        * 'show lisp eid-table vrf {vrf} ipv4 route-import map-cache {eid_prefix}'
        * 'show lisp eid-table {eid_table} ipv4 route-import map-cache'
        * 'show lisp eid-table {eid_table} ipv4 route-import map-cache {eid}'
        * 'show lisp eid-table {eid_table} ipv4 route-import map-cache {eid_prefix}'
        * 'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 route-import map-cache'
        * 'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 route-import map-cache {eid}'
        * 'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 route-import map-cache {eid_prefix}'
    * Added ShowLispV4PublicationPrefix
        * Added 'show lisp {lisp_id} instance-id {instance_id} ipv4 publication {eid_prefix}'
        * Added 'show lisp eid-table {eid_table} ipv4 publication {eid_prefix}'
        * Added 'show lisp {lisp_id} eid-table vrf {vrf} ipv4 publication {eid_prefix}'
        * Added 'show lisp locator-table {vrf} instance-id {instance_id} ipv4 publication {eid_prefix}'
        * Added 'show lisp locator-table vrf {vrf} instance-id {instance_id} ipv4 publication {eid_prefix}'
        * Added 'show lisp instance-id {instance_id} ipv4 publication detail'
        * Added 'show lisp {lisp_id} instance-id {instance_id} ipv4 publication detail'
        * Added 'show lisp eid-table {eid_table} ipv4 publication detail'
        * Added 'show lisp {lisp_id} eid-table vrf {vrf} ipv4 publication detail'
        * Added 'show lisp locator-table {vrf} instance-id {instance_id} ipv4 publication detail'
        * Added 'show lisp locator-table vrf {vrf} instance-id {instance_id} ipv4 publication detail'
    * Added ShowLispV6PublicationPrefix
        * Added 'show lisp {lisp_id} instance-id {instance_id} ipv6 publication {eid_prefix}'
        * Added 'show lisp eid-table {eid_table} ipv6 publication {eid_prefix}'
        * Added 'show lisp {lisp_id} eid-table vrf {vrf} ipv6 publication {eid_prefix}'
        * Added 'show lisp locator-table {vrf} instance-id {instance_id} ipv6 publication {eid_prefix}'
        * Added 'show lisp locator-table vrf {vrf} instance-id {instance_id} ipv6 publication {eid_prefix}'
        * Added 'show lisp instance-id {instance_id} ipv6 publication detail'
        * Added 'show lisp {lisp_id} instance-id {instance_id} ipv6 publication detail'
        * Added 'show lisp eid-table {eid_table} ipv6 publication detail'
        * Added 'show lisp {lisp_id} eid-table vrf {vrf} ipv6 publication detail'
        * Added 'show lisp locator-table {vrf} instance-id {instance_id} ipv6 publication detail'
        * Added 'show lisp locator-table vrf {vrf} instance-id {instance_id} ipv6 publication detail'
    * Added ShowL2vpnEvpnDefaultGatewayDetail
        * show l2vpn evpn default-gateway detail
        * show l2vpn evpn default-gateway evi {evi_id} detail
        * show l2vpn evpn default-gateway bridge-domain {bd_id} detail
        * show l2vpn evpn default-gateway vlan {vlan_id} detail
    * Added ShowL2vpnEvpnDefaultGatewaySummary
        * show l2vpn evpn default-gateway summary
        * show l2vpn evpn default-gateway evi {evi_id} summary
        * show l2vpn evpn default-gateway bridge-domain {bd_id} summary
        * show l2vpn evpn default-gateway vlan {vlan_id} summary
    * Added ShowL2vpnEvpnPeersVxlanDetail
        * show l2vpn evpn peers vxlan detail
        * show l2vpn evpn peers vxlan address {peer_addr} detail
        * show l2vpn evpn peers vxlan global detail
        * show l2vpn evpn peers vxlan global address {peer_addr} detail
        * show l2vpn evpn peers vxlan vni {vni_id} detail
        * show l2vpn evpn peers vxlan vni {vni_id} address {peer_addr} detail
        * show l2vpn evpn peers vxlan interface {nve_interface} detail
        * show l2vpn evpn peers vxlan interface {nve_interface} address {peer_addr} detail
    * Added ShowLispSessionRedundancy
        * for 'show lisp session redundancy'
    * Added ShowSnmpMibIfmibIfindexSchema
        * show snmp mib ifmib ifindex
        * show snmp mib ifmib ifindex | include {interface}
    * Added ShowVlansDot1qVlanIdSecondDot1qVlanId
        * show vlans dot1q {first_vlan_id} second-dot1q {second_vlan_id}
    * ShowLispIpv4Subscriber
        * show lisp {lisp_id} instance-id {instance_id} ipv4 subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 subscriber
        * show lisp instance-id {instance_id} ipv4 subscriber
        * show lisp eid-table {eid_table} ipv4 subscriber
        * show lisp eid-table vrf {vrf} ipv4 subscriber
    * ShowLispIpv6Subscriber
        * show lisp {lisp_id} instance-id {instance_id} ipv6 subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 subscriber
        * show lisp instance-id {instance_id} ipv6 subscriber
        * show lisp eid-table {eid_table} ipv6 subscriber
        * show lisp eid-table vrf {vrf} ipv6 subscriber
    * ShowLispEthernetSubscriber
        * show lisp {lisp_id} instance-id {instance_id} ethernet subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet subscriber
        * show lisp instance-id {instance_id} ethernet subscriber
        * show lisp eid-table vlan {vlan} ethernet subscriber
    * Added ShowArchiveLogConfig
        * show archive log config all
        * show archive log config {include}
    * Added  ShowArchiveLogStatistics
        * show archive log config statistics
    * Added ShowPlatformSoftwareFedQosPolicyTarget
        * show platform software fed active qos policy target brief
    * Added ShowIpMrouteCount
        * show ip mroute count
    * Added ShowMplsLabelRange
        * show mpls label range
    * Added class ShowLispSessionCapability
        * show lisp vrf {vrf} session capability
    * Modified ShowRunPolicyMap
        * Added set cos
        * Added set precedence
        * Added set dscp
        * Added priority percent
    * Added ShowLispAR
        * show lisp {lisp_id} instance-id {instance_id} ethernet server address-resolution
    * Added ShowL2vpnAtomPreferredPath
        * show l2vpn atom preferred-path
    * Added ShowLispIpv4Publisher
        * show lisp {lisp_id} instance-id {instance_id} ipv4 publisher
        * show lisp locator-table {vrf} instance-id {instance_id} ipv4 publisher
        * show lisp instance-id {instance_id} ipv4 publisher
        * show lisp eid-table {eid_table} ipv4 publisher
        * show lisp eid-table vrf {vrf} ipv4 publisher
    * Added ShowLispIpv6Publisher
        * show lisp {lisp_id} instance-id {instance_id} ipv6 publisher
        * show lisp locator-table {vrf} instance-id {instance_id} ipv6 publisher
        * show lisp instance-id {instance_id} ipv6 publisher
        * show lisp eid-table {eid_table} ipv6 publisher
        * show lisp eid-table vrf {vrf} ipv6 publisher
    * Added ShowLispEthernetPublisher
        * show lisp {lisp_id} instance-id {instance_id} ethernet publisher
        * show lisp locator-table {vrf} instance-id {instance_id} ethernet publisher
        * show lisp instance-id {instance_id} ethernet publisher
        * show lisp eid-table vlan {vlan} ethernet publisher
    * Added ShowCryptoSession
        * show crypto session
    * Added ShowCryptoSessionDetail
        * show crypto session detail
    * Added class ShowLispIpv4Publication
        * show lisp instance-id {instance_id} ipv4 publication
        * show lisp {lisp_id} instance-id {instance_id} ipv4 publication
        * show lisp eid-table {eid-table} ipv4 publication
        * show lisp eid-table vrf {vrf} ipv4 publication
        * show lisp locator-table {vrf} instance-id {instance-id} ipv4 publication
    * Added ShowSegmentRoutingTrafficEngFirstHopResolution
        * show segment-routing traffic-eng first-hop-resolution
        * show segment-routing traffic-eng first-hop-resolution {label}
    * Added ShowLispIpv4Away
        * show lisp instance-id {instance_id} ipv4 away
        * show lisp instance-id {instance_id} ipv4 away {eid}
        * show lisp instance-id {instance_id} ipv4 away {eid_prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 away
        * show lisp {lisp_id} instance-id {instance_id} ipv4 away {eid}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 away {eid_prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away {eid_prefix}
        * show lisp eid-table {eid_table} ipv4 away
        * show lisp eid-table {eid_table} ipv4 away {eid}
        * show lisp eid-table {eid_table} ipv4 away {eid_prefix}
        * show lisp eid-table vrf {eid_table} ipv4 away
        * show lisp eid-table vrf {eid_table} ipv4 away {eid}
        * show lisp eid-table vrf {eid_table} ipv4 away {eid_prefix}
    * Added ShowLispDatabaseEID
        * for 'show lisp instance-id {instance-id} {address-family} database {prefix}'
        * for 'show lisp {lisp_id} instance-id {instance-id} {address-family} database {prefix}'
        * for 'show lisp locator-table {vrf} instance-id {instance-id} {address-family} database {prefix}'
        * for 'show lisp locator-table vrf {vrf} instance-id {instance-id} {address-family} database {prefix}'
        * for 'show lisp eid-table {vrf} {address-family} {prefix}'
        * for 'show lisp eid-table vrf {vrf} {address-family} database {prefix}'
        * for 'show lisp eid-table vlan {vlan_id} {address_family} database {prefix}'
    * Added class ShowLispV4SMRParser
        * show lisp instance-id {instance_id} ipv4 smr
        * show lisp {lisp_id} instance-id {instance_id} ipv4 smr
        * show lisp eid-table {eid_table} ipv4 smr
        * show lisp eid-table vrf {vrf} ipv4 smr
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 smr
    * Added class ShowLispV6SMRParser
        * show lisp instance-id {instance_id} ipv4 smr
        * show lisp {lisp_id} instance-id {instance_id} ipv4 smr
        * show lisp eid-table {eid_table} ipv4 smr
        * show lisp eid-table vrf {vrf} ipv4 smr
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 smr
    * Added ShowDiagnosticEvent
        * show diagnostic events
    * Added ShowDiagnosticDescriptionModuleTestAll
        * show diagnostic description module {include} test all
    * Added ShowDiagnosticContentModule
        * show diagnostic content module {mod_num}
    * Added ShowDiagnosticResultModuleTestDetail
        * show diagnostic result module {mod_num} test {include} detail

* aireos
    * Added class ShowBoot
        * show boot
    * Added class Ping
        * ping command

* iosxr
    * Added ShowLpts
        * show lpts pifib hardware police

* ios
    * Added ShowEnvironment for ASR901 platform
        * show environment

* show lisp instance-id {instance_id} ethernet server address-resolution


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxr
    * Modified ShowOspfv3VrfAllInclusiveNeighborDetailSchema
        * Changed 'bfd_enable' key in schema to str type from bool.
    * Modified ShowOspfv3VrfAllInclusiveNeighborDetail
        * Added support for 'bfd_enable' and 'bfd_mode'
    * Modified ShowBgpInstanceNeighborsAdvertisedRoutes
        * Modified RegEx <p4>,<5_1> to capture dotted Notation ASN
    * Modified ShowIpv6Interface
        * Added 'show ipv6 interface'
    * Modified ShowStaticTopologyDetail
        * Correctly match IPv6 addresses

* iosxe
    * Modified ShowModule
        * Modified show module parser for supporting 9500 device.
    * Modified ShowPlatformIntegrity
        * show platform integrity {signature}
    * Modified ShowServiceInsertionTypeAppqoeServiceNodeGroup
        * Changed schema to support varied iosxe output. Not backwards compatible
    * Modified ShowPlatformHardwareQfpActiveFeatureAppqoe
        * Changed schema to support varied iosxe output. Chnages are backward compatible.
    * Modified ShowSslProxyStatistics
        * Output of the CLI is enhanced with new addtional keys in latest release. Added
    * Modfied ShowTcpProxyStatistics
        * Output of the CLI is enhanced with new addtional keys in latest release. Added
    * Modified ShowPlatformHardwareQfpActiveDatapathUtilSum
        * Changed schema to support varied iosxe output. Chnages are backward compatible.
    * Modified ShowRunInterface
        * Added keepalive key in schema
    * Modified ShowPowerInline
        * Fixed regex pattern <p1> for adding '-' support in oper_state string.
    * ShowIpMrouteCount
        * Added the key type for average
    * ShowMplsLabelRange
        * Coreected merge conflict
    * ShowPlatformSoftwareFedQosPolicyTarget
        * Added state_cfg,state_opr and address keyies
    * Modified ShowIpOspfDatabaseTypeParser
        * Fixed overwritten af variable
        * Fixed issue where sub_tlv variables were referenced before assignment
    * Modified ShowMemoryStatistics
    * Modified ShowRunInterface
        * Added regex pattern <p42 and p43> to accommodate policy config lines
    * Modified ShowRunInterface
        * Corrected merge conflict
    * Modified ShowMplsLabelRange
        * Corrected merge conflict
    * Modified ShowPlatformSoftwareFedQosPolicyTarget
        * Corrected merge conflict
    * Modified ShowLogging
        * Fixed to ignore 'show logging' command syntax line in case it's included
    * Added ShowIpv6Routers
        * show ipv6 routers
    * Added ShowMabAllSummary
        * show mab all summary
    * Modified ShowIsisFlexAlgo
        * Fixed regex, code logic, added additional fields to the schema, and added unit tests
    * Modified ShowStormControl
        * Corrected merge conflict
    * Modified ShowPlatformSoftwareFed
        * Removed ShowPlatformSoftwareFed since it is failing on Jenkin test
    * Modified ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterface
        * Changed "if_id" data type from int to str
        * Changed the following keys to optional
            * log_mean_delay_interval
            * log_mean_sync_interval
            * num_delay_requests_received
            * num_delay_responses_received
            * num_delay_requests_transmitted
            * num_delay_responses_transmitted
    * Modified ShowIsisRib
        * Fixed regexes and added new fields to the schema
    * Modified ShowMacsecInterface
        * Changed parser to support multiple receive channels. NOT BACKWARDS COMPATIBLE.
    * Modified Ping
        * Updated parser to support timeout 0 seconds.
    * Modified ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterface
        * show platform software fed switch active ptp interface {interface}
    * Modified ShowMplsL2TransportDetail
        * Updated regex to decode multiple labels in imposed label stack
        * Added regex to properly decode output when LDP is down
    * Fixed conflict merge on ShowIpMrouteCount, ShowMplsLabelRange, ShowPlatformSoftwareFedQosPolicyTarget and ShowRunPolicyMap classes
    * Modified ShowL2routeEvpnPeers
        * Updated regex to support varying time format
    * Modified ShowLispAR
        * Fixed UnboundLocalError local variable 'cmd' referenced before assignment
    * Updated ShowInventory
        * Fixed error where subslot dictionary wasn't initialized before accessing
    * Modified ShowMplsForwaringTable
        * Corrected blank label entries going to No Label rather than the correct label
        * Corrected where single entry is split across 2 lines being put into wrong label information
        * Updated parser to handle new "algo" filter
        * Updated parser to ahdnle new flex algo information that may or may not be present
    * Modified ShowVlanAccessMap
        * Changed regexp patter for <p1,p2> to gerp the access-map name and protocol name and value proper
    * Modified ShowVlanFilter
        * Changed regexp patter for <p1> to gerp the vlan_access_map_tag proper

* changed regex to grep 'reserve p'.

* aireos
    * Modified class ShowBoot
        * Fixed accommodate the new output

* common
    * Added 'Wl' 'Wlan-GigabitEthernet' interface mapping in convert_intf_name

* nxos
    * Modified ShowInterface
        * Fix pattern p1 and p1_1 to handle empty 'type'
    * Modified ShowIpv6StaticRoute
        * Correctly match IPv6 addresses


