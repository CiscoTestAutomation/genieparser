--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformTcamPbrNat
        * show platform hardware fed active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}
    * Added ShowNatTranslations
        * show ip nat translations
    * Added ShowRunRoute
        * for 'show running-config | section route'
    * Added configure_bgp_sso_route_refresh_enable
        * bgp sso route referesh-enable
    * Added configure_bgp_refresh_max_eor_time
        * bgp refresh max-eor-time {max_eor_time}
    * Added ShowCryptoGdoi
        * Parser for show crypto gdoi
    * Added ShowCryptoGdoiDetail
        * Parser for show crypto gdoi detail
    * Added class ShowCryptoGdoiGroup
        * Parser for show crypto gdoi group {group_name}
    * Added ShowCryptoGkm
        * Parser for show crypto gkm
    * Added ShowCryptoGdoiKsPolicy
        * Parser for show crypto gdoi ks policy
    * Added ShowCryptoGdoiGmDataplanCounter
        * Parser for show crypto gdoi gm dataplan counter
    * Added ShowCryptoSessionInterfaceDetail
        * show crypto session interface {interface} detail
    * Added ShowEthernetCfmMaintenancePointsRemoteDetail
        * for 'show ethernet cfm maintenance-points remote detail'
    * Added ShowEthernetCfmStatistics
        * for 'show ethernet cfm statistics'
    * Added 'ShowInterfacesMtu' schema and parser
        * show interfaces mtu
        * show interfaces { interface } mtu
        * show interfaces mtu module {mod}
    * Added ShowIpNhrpTraffic
        * show ip nhrp traffic
        * show ip nhrp traffic interface {interface}
    * Added ShowIpNhrpTrafficDetail
        * show ip nhrp traffic detail
        * show ip nhrp traffic interface {interface} detail
    * Added 'ShowPlatformSoftwareFedIfm' schema and parser
        * show platform software fed switch active ifm interfaces tunnel
    * Added ShowCryptoEliAll
        * show crypto eli all
    * Added ShowPlatformHardwareQfpIpsecDrop
        * show platform hardware qfp active feature ipsec data drop
    * Added ShowIsisNodeSummary
        * show isis node summary
    * Added ShowIsisTopologyLevel
        * show isis topology {level}
    * Added ShowSystemMtu
        * show system mtu
    * Added ShowIdpromInterface for C9300
        * show idprom interface {interface}
    * Added ShowStackwiseVirtualNeighbors
        * Added 'show stackwise-virtual neighbors'
    * Added ShowSystemIntegrityMeasurement
        * Parser to support new kgv measurement cli
    * Added ShowSystemIntegrityCompliance
        * Parser to support new kgv compliance cli
    * Added ShowSystemIntegrityTrustChain
        * Parser to support new kgv trust chain cli
    * Modified ShowSystemIntegrityAllTrustChainNonce
        * Added yang parser for ShowSystemIntegrityAllTrustChainNonce
    * Added ShowPlatformHardwarefedActiveQosQueueStats parser
        * show call Show Platform Hardware fed Active Qos Queue Stats
    * Added ShowPlatformHardwareFedActiveQosQueuelabel2qmapQmapegressdataInterface  parser
        * show call Show Platform Hardware Fed Active Qos Queue label2qmap Qmap egress data Interface

* iosxr
    * Added ShowEvpnGroup
        * 'show evpn group'
        * 'show evpn group {group_id}'
    * Added ShowEvpnEviMacDetail
        * show evpn evi mac detail
        * show evpn evi vpn-id {vpn-id} mac detail
    * Modified ShowOspfInterfaceBrief
        * Fixed to get instance value properly

* nxos
    * Added ShowInterfaceCounters
        * show interface counters
        * show interface {interface} counters
    * Added ShowHsrpEventHistoryErrors for
        * 'show hsrp internal event-history errors'
    * Added ShowHsrpEventHistoryDebugs for
        * 'show hsrp internal event-history debugs'
    * Added ShowHsrpEventHistoryMsgs for
        * 'show hsrp internal event-history msgs'

* modified the parser name to showsystemintegrityalltrustchainnonce


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpRoute
        * Updated the key and value of "source_protocol_dict" dict
    * Modified ShowLispDatabaseEid
        * Changed <srvc_ins_type> from schema to Optional
        * Changed <srvc_ins_id> from schema to Optional
    * Modified ShowLispIpMapCachePrefixSuperParser
        * Fixed regex for "unknown-eid-forward"
    * Modified ShowLispEthernetDatabase
        * Changed <srvc_ins_type> from schema to Optional
        * Changed <srvc_ins_id> from schema to Optional
    * Modified ShowLispEthernetMapCache
        * Updated regex pattern due to change in output
    * Modified ShowLisp
        * Updated regex pattern due to change in output
    * Modified ShowLispSession
        * Added cmd 'show lisp session {established}'
    * Modified ShowLispServiceSchema
        * Changed <xtr_id> to Optional
        * Changed <site_id> to Optional
    * Modified ShowLispInstanceIdService
        * Updated regex pattern due to change in output
    * Modified ShowLispRemoteLocatorSetSchema
        * Updated <instance_id> type as str
    * Modified ShowLispPublicationPrefixSuperParser
        * Updated regex pattern due to change in output
    * Modified ShowLispIpMapCachePrefixSuperParser
        * Updated regex pattern
    * No backward compatibility
    * Modified ShowIdpromInterface
        * Changed the key <nominal_bitrate_per_channel>' to optional
        * Updated regex <p2>, <p3>, <p4>, <p5>, <p8>, <p13>, <p14>, and <p15>
    * Modified ShowIpStaticRoute
        * Add the optional `owner_code` key under `next_hop.outgoing_interface`
    * Modified ShowIpv6DhcpBinding
        * Add the optional client 'interface' key to the schema
        * Make the existing client 'ia_na' key optional
        * Add the optional client 'ia_pd' key to the schema
        * Update existing regex processing for 'Address' under 'IA NA' to
        * Fix populating of schema so that multiple keys for IA ID are
    * Modified ShowIpv6Route
        * Add "ND" and "NDp" to the dict of accepted protocol codes
        * Modify the regular expression to accept 3-character long protocol
    * Modified ShowIsisDatabaseVerbose
        * Modified the regex to parse the flex algo portion of a prefix sid
    * Modified ShowNveVni
        * Added the functionality to run parser with vni id
    * Modified ShowStandbyBrief
        * Updated regex <p0> to parse IP addresses as active addresses
    * Modified ShowIpNhrpTrafficDetail
        * Added return statement for parser output to return
    * Modified ShowIpRpf
        * Added optional key <directly_connected>
        * Modified regex <p3_1>
    * Modified ShowL2vpnServiceAll
        * Fixed regex <p2> to match more patterns in output
    * Modified ShowDeviceTrackingMessages
        * Added option for `show device-tracking messages | section {message}`
    * Modified ShowInterfaces
        * Added optional keys <tunnel_source_interface>
        * Updated regex pattern p46 to accommodate various outputs.
    * Modified ShowLicenseEventlog2
        * Added proper no_event_log key  to schema
    * Modified ShowLicenseTechSupport
        * Added optional key <autorization_renewal> to schema
        * Added optional key <failures_reason> to schema
        * Added the key <local_device> to schema
        * Modified the expression for p11_data1_3 to work on all scenario.
    * Modified ShowIpMfib
        * Updated ShowIpMfibSchema with optional keys <ingress_vxlan_version>,<ingress_vxlan_vni>,<ingress_vxlan_nxthop>,<ingress_vxlan_cap>,<egress_vxlan_version>,<egress_vxlan_vni>,<egress_vxlan_nxthop>,<egress_vxlan_cap>
        * Updated regex pattern of "show ip mfib" by changing the existing one to accomodate optional incoming interfaces, entries with no flags, no preceding spaces in flags output and adding another line to parse vxlan related information
    * Modified ShowIpMrib
        * Updated ShowIpMribSchema to make incoming_interface_list and egress_interface_list as optional keys
        * Updated regex pattern of ShowIpMrib parser to accomodate vxlan related keywords
    * Modified ShowSystemIntegrityAllMeasurementNonce
        * Minor correction to match bundle boot output in regex pattern <p5>
    * Modified ShowVersion
        * All switches (active and standby) now appear in the switch_num dictionary
    * Modified ShowIpRoute
        * Updated the key and value of "source_protocol_dict" dict

* ios
    * Modified ShowIpStaticRoute
        * Add the optional `owner_code` key under `next_hop.outgoing_interface`

* iosxr
    * Modified ShowPolicyMapInterface Parser, update pattern p4 output direction
    * Modified ShowInterfacesDescription
        * Match interfaces only after table header (prevent matching timestamp)
        * Use iosxr interface naming (ex MgmtEth or nVFabric interface)
    * Modified ShowMplsLdpIgpSync
        * Fixed regex <p1>, <p3>, and <p5> to match more patterns in output
    * Modified ShowEvpnEviMac
        * Changed 'label' from int to str.
        * Added 'sid', 'sid_flags', 'endpt_behavior', 'sid_struct', 'transposition', 'local_e_tree', 'remote_e_tree', 'remote_matching_e_tree_rt', 'local_ac_id', 'remote_ac_id', 'ext_flags' and 'stamped_xcid' key to the schema
        * Updated regex pattern p1 and p1_1 to accommodate various outputs.
        * Added new regex pattern and match for all the new keys
    * Modified ShowEvpnEviMacPrivate
        * Updated cli to accept vpn-id key
        * show evpn evi vpn-id {vpn-id} mac private
    * Modified ShowMplsForwarding
        * Added command filtering with prefix (ex show mpls forwarding prefix 1.1.1.1/32)

* common
    * Modified Common
        * Modified convert_intf_name to allow letter in interface port (ex 0/RP0/CPU0/0)

* nxos
    * Modified ShowSystemInternalSysmgrServiceName
        * Updated regex pattern <p2> to accept 'no SAP'


--------------------------------------------------------------------------------
                                 Compatibility)                                 
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowSystemIntegrityAllMeasurementNonce
        * Added yang parser for ShowSystemIntegrityAllMeasurementNonce


