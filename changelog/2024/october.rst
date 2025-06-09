--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareFedSwitchActiveifmMappingsgid parser
        * Added parser for cli show platform software fed switch {switch} ifm mappings gid {gid_num}
    * Added ShowPlatsoftwaremcumanager
        * Added 'show platform software mcu switch {switch_num} R0 manager 0' command and schema.
    * Add ShowL2vpnEvpnAllActiveMh
        * There is a keyword change in show commands. So added new parser with the keyword change but rest of the content is same.
        * show l2vpn evpn esi-mlag summary has changed to show l2vpn evpn all-active-mh summary
        * show l2vpn evpn esi-mlag vlan brief has changed to show l2vpn evpn all-active-mh vlan brief
        * show l2vpn evpn esi-mlag mac ip deleted has changed to show l2vpn evpn all-active-mh mac ip
    * Added ShowPlatformHardwareFedSwitchStandbyVlanIngress
        * parser for show platform hardware fed switch standby vlan ingress
    * Added howPlatformHardwareFedSwitchActiveVlanIngress
        * parser for 'show platform hardware fed switch active vlan {num} ingress'
    * Added ShowPlatformSoftwareFedSwitchActiveSecurityFedSisfStatistics parser.
        * Added parser for CLI `show platform software fed switch active security-fed sisf statistics`.
    * Added ShowPlatformHardwareFedSwitchActiveSgaclResourceUsage parser.
        * Added parser for CLI `show platform hardware fed switch active sgacl resource usage`.
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL3unexthop
        * show platform hardware fed switch {switch} fwd-asic insight l3u_nexthop {nh_gid}
    * Added ShowLoggingProcess parser
        * Added parser for cli show Logging Process
    * Added  ShowPlatformsoftwareFedActiveXcvrLpnLinkstatusSchema
        * Added parser for show platform software fed {switch} {mode} xcvr lpn {lpn_value} link_status
    * Added ShowPlatsoftwaremcuversionSchema
        * Added parser for show platform software mcu  switch  {switch_num} R0 version  0
    * Added ShowPlatsoftwaremcusubordinateSchema
        * Added parser for show platform software mcu  switch  {switch_num} R0 version  0
    * Added ShowPlatformfrontendcontroller parser
        * Added parser for cli show Platform Frontend Controller
    * Added ShowControllersEthernetControllerPortInfoSchema
        * Added parser for show controllers ethernet-controller tenGigabitEthernet {interface} port-info
    * Modified ShowDeviceTrackingDatabase
        * show device-tracking database address {address}
    * Added ShowAccessSessionMacDetails parser.
        * Added parser for cli 'show access-session mac {mac} details {rp_slot}'.
    * Added ShowIpDhcpSnoopingTrackServer
        * Added schema and parser for show ip dhcp snooping track server


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIsisNeighborsDetail
        * Added <algo> into schema as Optional
        * Added regex pattern <p22a> to accommodate recent changes.
    * Modified ShowPimNeighbor
        * Updated regex pattern <p1> to accommodate various outputs.
    * Modified ShowIpRpf
        * Updated regex pattern <p5> to accommodate various outputs.
    * Modified ShowRepTopologySegment
        * Changed <edge> from schema to Optional.
        * Updated regex pattern <p1> to accommodate various outputs.
    * Modified ShowLogging
        * Added optional keys <authentication>, <encryption> in schema.
        * Updated regex pattern <p12> to accommodate various outputs.
    * Modified fix for ShowCryptoSessionSuper
        * Modified the regex patterns <p8>, <p12> and <p18> to accommodate various outputs.
    * Modified fix for ShowLispSiteDetailSuperParser
        * Modified the regex patterns <p4>, <p5> and <p17> to accommodate various outputs.
    * Modified fix for ShowPlatformFedActiveTcamUtilization under c9600
        * Added a regex p4 to match additional output from the show command.
    * Modified ShowIpMulticast
        * Added <algorithm> key to schema as Optional.
        * Updated regex pattern <p2> to accommodate various outputs.
    * Modified ShowCryptoIpsecProfile
        * Updated regex pattern <p1> and <p8> to accommodate various outputs.
    * Modified ShowLispPublicationPrefixSuperParser
        * Changed rdp_len in schema from int to str.
        * Fixed incorrect regex for parsing domain_id and multihoming_id.
        * Added support for merged rloc programming verification (new field 'selected').
    * Modified ShowLispSiteDetailSuperParser
        * Made regex for parsing rdp more restrictive.
    * Modified fix for ShowRplRoutePolicy
        * Updated logic to track NTP peer synchronization state and update overall clock state based on synchronized peers.
    * Modified ShowLispExtranet
        * Updated regex to parse 'Config-Propagation' as source
    * Modified ShowLispDatabaseSuperParser
        * Add support for parsing 'dbmap_src'
        * Add support for parsing 'publish_mode'
    * Modified ShowLispPublicationPrefixSuperParser
        * Add support for parsing 'publish_mode'
    * Modified ShowLispSiteDetailSuperParser
        * Add support for parsing 'publish_mode'
    * Modified ShowLispMapCacheSuperParser
        * Fix regex to parse 'up, self' for locator
    * Modified ShowInstallSummary
        * added fields 'location', 'Switch 1 2', 'auto_abort_timer' in proper place

* common
    * Modified _fuzzy_search_command
        * Made a fix to handle when we have an exact match in the tree, but no actual implementation


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowRunningConfigAllClassMap parser.
        * added show running-config all | section class {class_map}
    * Added ShowPlatformSoftwareFedActiveIpUrpf parser under iosxe.
        * added show platform software fed active ip urpf
        * added show platform software fed switch {mode} ip urpf
    * Added ShowInventory parser under c9350.
        * added show inventory
    * Added ShowPlatformHardwareFedQosSchedulerSdkInterface parser under c9610.
        * added show platform hardware fed {mode} qos scheduler sdk interface {interface}
        * added show platform hardware fed {switch} {mode} qos scheduler sdk interface {interface}
    * Added ShowPlatformHardwareFedSwitchQosQueueStatsInterface parser under c9610.
        * added show platform hardware fed switch {switch_num} qos queue stats interface {interface}
        * added show platform hardware fed active qos queue stats interface {interface}
    * Added ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear parser under c9610.
        * added show platform hardware fed active qos queue stats interface {interface} clear
        * added show platform hardware fed switch {switch_num} qos queue stats interface {interface} clear


