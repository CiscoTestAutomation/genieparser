--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Fixed parser ShowIpv6MldGroups
        * Fixed regex pattern p1 to work for different uptime format
    * Fixed parser ShowIpPimRpMapping
        * Fixed the logic under p3 regex to match "protocol" for new output
    * Fix ShowIpv6Mfib parser
        * Updated regex pattern p7 to accomodate various outputs.
        * Updated regex pattern p8 to accomodate various outputs.
        * Added optional keys 'ingress_mdt_ip', 'egress_mdt_ip' to the parser.
    * Modified ShowIpEigrpInterfacesDetail
        * Modified parser for 'show ip eigrp interfaces detail' and added <interface> option
    * Fixed the regex p1 for new output.
    * ShowIpRouteWord
        * Added line parsing for `Default gateway is 172.27.147.1`
    * Fixed parser ShowVersion
        * Fixed regex pattern - p1_1 for show version in IOS device
    * Modified ShowPlatformSoftwareFedIgmpSnoopingGroups
        * Modified schema and parser for 'show platform software fed {state} ip igmp snooping groups vlan {vlan}'
    * ShowInterfaces
        * Fixed p2_2 regex to correctly match this line `Hardware is BUILT-IN-4x2_5GE, address is 8c1e.8068.9f6c (bia 8c1e.8068.9f6c)`
    * Modified parser ShowIpMroute
        * Updated regex pattern p3 to accomodate various outputs
        * Added optional key 'iif_mdt_ip' to schema
    * Added ShowMacAddressTableDynamicVlan to support show mac address-table dynamic vlan
        * Added a parser
    * Modified ShowDhcpLease
        * Added regex <p5_1> to handle Infinite lease time.
    * Modified ShowIpDhcpBinding
        * Added regex <p2> to match multiline Client-ID
    * Show Platform
        * Made `chassis` optional
    * Fixed schema parser ShowIpMfib
        * In regex p7, added optional parameters - 'ingress_mdt_ip'
        * In regex p8, added optional parameters - 'egress_mdt_decap' and 'egress_mdt_ip'
    * Fixed parser ShowPlatformSoftwareFedIgmpSnooping
        * Added p14_3 regex to match the output of the command
    * Fixed parser ShowLispMapCacheSuperParser
        * Added support for parsing optional keyword 'self' as part of 'via' capture group.
    * cat9k
        * fixed parser ShowL2ProtocolTunnelSummary - initialised last_port
    * Fixed parser ShowPimNeighbor
        * Fixed regex pattern p2 to accomodate different output
    * Fixed parser ShowVersion
        * Fixed regex pattern - p1_1 for show version in IOS device
    * Modified ShowIpIgmpGroups
        * Modified parser for 'show ip igmp groups {interface}'
    * Modified ShowIpIgmpGroupsDetail
        * Modified parser for 'show ip igmp groups  {ip} detail'
    * Modified ShowIpIgmpInterface
        * Modified parser for 'show ip igmp interface {interface}'
    * Modified ShowIpEigrpNeighbors
        * Modified parser for 'show ip eigrp neighbors' and added <interface> option
    * Fixed the regex p1 to handle the last entry in the output.
    * Fixed the unittest that was failing to parse the last line of the output.

* added cli command 'show platform software fed {switch_var} {state} ip igmp snooping groups vlan {vlan}'

* sonic
    * Added multiple regex and conditions for output in golden_output_3_output.txt

* iosxr
    * Modified ShowBgpInstanceNeighborsReceivedRoutes
        * Modified regex pattern
        * Added testfolder for  ShowBgpInstanceNeighborsReceivedRoutes
    * Modified ShowMonitorCaptureBufferDetailed
        * Modified schema and parser for'show monitor capture file {path} packet-number {number} detailed'
    * Modified ShowVrfAllDetail
        * Modified regex pattern to support multiple interfaces

* nxos
    * Added Service-Ethernet interface
        * This will be used to convert the SEth to Service-Ethernet


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformHardwareCppActiveStatisticsDrop
        * Updated schema and parser for cli show platform hardware cpp active statistics drop


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowCallerSummary
        * show caller summary
    * Added ShowPlatformSoftwareFedIpIgmpSnoopingGroupsVlan parser
        * 'show platform software fed {switch} {module} ip igmp snooping group vlan {vlan_id} {group}',
        * 'show platform software fed {switch} {module} ip igmp snooping group vlan {vlan_id} {group} detail'
    * Added ShowPlatformSoftwareFedSwitchActiveOifset parser
        * Added schema and parser for cli 'show platform software fed switch active oifset'
    * Added ShowPlatformSoftwareFedSwitchFnfSwStatsShow
        * Added schema and parser for'show platform software fed switch fnf sw stats show'
    * Added revision 2 for "show inventory" parser
        * Modified code to add slot number as key under slots dict
        * Supervisor cards added under RP dict
    * Added ShowIpNhrpSelf parser
        * Added schema and parser for cli 'show ip nhrp self'
    * Added ShowAutoInstStat parser
        * Added schema and parser for cli 'show auto inst stat'
    * Added ShowPlatformHardwareFedSwitchFwdAsicResourceTcamTableNflAclFormat0
        * Added schema and parser for'show platform hardware fed switch fwd asic resource tcam table nfl acl format 0'
    * Added ShowIpEigrpTimers Parser in show_eigrp.py
        * Added schema and parser for 'show ip eigrp timers'
    * Added ShowIpNhrpVrf parser
        * Added schema and parser for cli
            * 'show ip nhrp vrf {vrf}'
            * 'show ip nhrp vrf {vrf} {ip}'
    * Added ShowCryptoIsakmpSaStatus
        * show crypto isakmp sa {status}
    * Added ShowCryptoIsakmpPeer
        * show crypto isakmp peer {peer_ip}
    * Added ShowIpPimVrfMdtBgpSchema parser
        * Added schema and parser for cli 'show ip pim vrf {vrf_name} mdt bgp'
    * Added ShowEthernetRingG8032Brief schema and parser.
        * Added schema and parser for show ethernet ring g8032 brief.
    * Added ShowCryptoIpsecSpiLookupDetail
        * show crypto ipsec spi-lookup detail
    * Added ShowCryptoIsakmpDefaultPolicy
        * show crypto isakmp default policy
    * Added ShowIpMfibActive parser
        * Added schema and parser for cli 'show ip mfib active'
    * Added ShowPlatformSoftwareFedIpv6RouteSummaryInclude
        * Added schema and parser for 'show platform software fed ipv6 route summary'
    * Added  ShowPlatformSoftwareFedSwitchFnfMonitorsDump parser
        * Added schema and parser for cli "show platform software fed Switch {Switch_num} fnf monitors dump"
    * Added ShowIpIgmpMembership parser
        * Added schema and parser for cli 'show ip igmp membership'
    * Added ShowIpv6PimMdtSend
        * show ipv6 pim mdt send
        * show ipv6 pim vrf {vrf} mdt send
    * Added ShowPlatformSoftwareFedActivePuntAsicCauseBrief parser
        * Added schema and parser for cli
            * 'show platform software fed {switch} active punt asic-cause brief'
    * Added ShowPlatformHardwareFedSwitchActiveQosQueueStatsInternalPortTypePuntQueue parser
        * Added schema and parser for cli
            * 'show platform hardware fed {switch} active qos queue stats internal port_type punt queue {voq_id}'
    * Added parser  ShowPlatformHardwareQfpActiveFeatureCtsClientInterface
        * Added parser for cli show platform hardware qfp active feature cts client interface.
    * Added ShowIpNhrpRedirect parser
        * Added schema and parser for cli 'show ip nhrp redirect'
    * Added ShowPlatformSoftwareFedSwitchActiveOifsetUrid parser
        * Added schema and parser for cli 'show platform software fed switch active oifset urid {id}'
        * Added schema and parser for cli 'show platform software fed switch active oifset urid {id} detail'
    * Added schema and parser for show platform hardware cpp active feature firewall session create {session_context} {num_sessions}

* showcryptoisakmpsacount
    * show crypto isakmp sa count


