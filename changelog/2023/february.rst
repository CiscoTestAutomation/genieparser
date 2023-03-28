--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpMroute
        * To support vxlan v6 enacap and ipv6 address
        * Sample output (Vlan500, VXLAN v6 Encap (50000, FF131), Forward/Sparse, 001731/stopped, flags)
    * Modified ShowIpMfib
        * To support vxlan v6 enacap and ipv6 address
        * Sample output (Vlan500, VXLAN v6 Encap (50000, FF131) Flags F)
    * Modified ShowIpv6MfibSchema
        * To support optional multicast group and source addresses, Where "show ipv6 mfib" output can be empty.
        * Sample output ((66666,FF131) entry not found)
    * Modified ShowFlowMonitoreCache
        * Added more parameters to the entry dict.
        * Made the existing variables optional in the schema.
    * Modified ShowIpDhcpBinding
        * Added "show ip dhcp binding vrf {vrf_name}" cli.
    * Modified ShowIdpromInterface
        * Fixed parser for ParserNotFound error.
            * Changed 'mode' to 'interface'
    * Fixed ShowIpIgmpSnoopingDetail
        * Changed 'cgmp_inter_mode' key as optional in schema and added unit test.
    * Fixed ShowIpIgmpSnoopingGroups
        * Fixed regular expression to fetch multiple ports as a string for 'port' key.
    * Fixed ShowIpMroute
        * Fixed 'flags' regular expression pattern and supporting unit tests files are added
    * Modified showIpv6MldSnooping
        * Added optional key 'explicit_host_tracking' and unit tests
    * Modified ShowIsisNeighbors
        * updated regex to account for the new cli output when there is a long hostname
    * Modified ShowLldpEntry
        * Fixed the parser by making 'chassis_id' as optional and unit test case is added.
    * Enhanced ShowMonitorCaptureBufferDetailed
        * Enhanced the parser by adding the optional argument 'display-filter' to the existing cli show command, and included 'dscp_value' in the parser output.
    * Deleted ShowPlatformHardwareFedSwitchActiveQosDscpCosCountersInterface
        * Duplicate parser for show platform hardware fed switch {switch_type} qos dscp-cos counters interface {interface} deleted.
    * Modified ShowProcessesPlatformCProcess
        * Moved up the class from iosxe/cat9k to iosxe
        * Moved also UTs from iosxe/cat9k/tests to iosxe/tests
    * Modified ShowProcessesPlatformIProcess
        * Moved up the class from iosxe/cat9k to iosxe
        * Moved also UTs from iosxe/cat9k/tests to iosxe/tests
    * Modified ShowSdmPrefer
        * Made some parameters as Optional and fixed regular expressions.
    * Modified ShowSpanningTreeInterfaceDetail
        * Made couple of schema variables optional and added unit test case.
    * Fixed ShowSpanningTreeInterface
        * Fix the command from "show spanning tree interface {interface}" to "show spanning-tree interface {interface}"
    * Modified ShowTemplate
        * Fixed groupdict None type error and added bound and nested template keys support.
    * Fixed ShowVlanSummary
        * Made "existing_extend_vlans" as optional and added "existing_extend_vtp_vlans" optional key
    * Modified ShowVrrp
        * Fixed parser error for Ipv6 vrrp show command.
    * Modified ShowWirelessFabricClientSummary
        * Removed duplicated class entry
        * Added <l2_vnid> and <rloc_ip> keys as Optional.
        * Added regex pattern <p_client_info_n> to accommodate new version of show command.
        * Added UT covering new version of show commands and new keys
    * Modified ShowVtpStatus
        * fixed genie.metaparser.util.exceptions.SchemaMissingKeyError Missing keys [['vtp', 'pruning_mode']]
    * Modified ShowNat64Translations
        * Added new show cli 'show nat64 translations vrf {vrf_name}'
    * Modified ShowNat64Statistics
        * Added regexp to match vrf and vrf name
    * Modified ShowNat64PrefixStatefulGlobal
        * Added regexp to match vrf and vrf name
    * Modified ShowNat64PrefixStatefulStaticRoutes
        * Added new show cli 'show nat64 prefix stateful static-routes prefix {prefix} vrf {vrf_name}' and regexp to match vrf and vrf name
    * Modified ShowRunInterface
        * Added p87 and p88 for  speed  and speed  nonegotiate under interface  running  configurations.
    * Modified ShowLispIpv4ServerDetail
        * Added RDP info as per the output change in latest polaris version.
        * Added Merged Locator info as per the output change in latest polaris version.
    * Modified ShowLispIpv6ServerDetail
        * Added RDP info as per the output change in latest polaris version.
        * Added Merged Locator info as per the output change in latest polaris version.
    * Modified ShowLispV4PublicationPrefix
        * Added RDP info as per the output change in latest polaris version.
        * Added Merged Locator info as per the output change in latest polaris version.
    * Modified ShowLispV6PublicationPrefix
        * Added RDP info as per the output change in latest polaris version.
        * Added Merged Locator info as per the output change in latest polaris version.
    * Added ShowLispIpv4ServerSHD
        * Added new parser for ipv4 registrations for silent-host
    * Added ShowLispIpv6ServerSHD
        * Added new parser for ipv6 registrations for silent-host
    * Modified ShowLispServiceServerDetailInternal
        * Added support for split-line output format for longer ETR addresses
    * Modified ShowLispPublisherSuperParser
        * Added support for new state string No ETR MS
    * Modified ShowLispPublicationPrefixSuperParser
        * Added support for split-line output format for longer publisher addresses
    * Modified ShowLispSiteDetailSuperParser
        * Added support for split-line output format for longer ETR addresses
    * Modified ShowPlatform
        * added show platform software fed {switch} active vt counter
        * show platform software fed switch active vt all
    * Added ShowPlatformSoftwareFedSwitchActiveMatmAdjacencies
        * added show platform software fed switch active matm adjacencies

* iosxr
    * Modified ShowOspfNeighbor
        * Modified up_time as Optional parameter in schema.

* common
    * Refactor parser loading, deprecate entrypoint callable function
    * Add support for multiple parser packages via environment variable `PYATS_LIBS_EXTERNAL_PARSER` using comma separated syntax.

* nxos
    * Modified ShowBgpL2vpnevpnSummary
        * Updated regex to support ipv6 neighbors
    * Modified ShowNveInterfaceDetail
        * Added regex pattern to support ipv6


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added
        * show idprom tan switch {switch_num}
        * show idprom tan switch all


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowIpVerifySource Parser
        * Parser for "show ip verify source interface"
        * Parser for "show ip verify source"
    * Added ShowPlatformHardwareFedSwitchActiveQosDscpCosCountersInterface
        * show platform hardware fed switch active qos dscp-cos counters interface {interface}
    * Added ShowPlatformSoftwareFedActiveMonitor Parser
        * Parser for "show platform software fed active monitor {session}"
    * Added ShowPlatformSoftwareFedSwitchActiveMonitor Parser
        * Parser for "show platform software fed switch active monitor {session}"
    * Added ShowRedundancyLinecardAll
        * show redundancy linecard all
    * Added ShowTemplateInterfaceBindingTarget
        * show template interface binding target {interface}
    * Added ShowPlatformSoftwareFedActiveVtIfId
        * show platform software fed active vt if-id {if_id}
    * Added ShowWirelessMulticast
        * show wireless multicast
    * Added showIpv6MldSnooping
        * show ipv6 mld snooping
    * Added ShowIpcefExactRoute
        * show ip cef exact-route {source} {destination}
    * Added ShowPmPortInterface parser
        * adding ShowPmPortInterface parser
    * Modified ShowLoggingOnboardSwitchClilog
        * show logging onboard switch {switch} clilog
    * Modified ShowAuthenticationSessionsDetailsSuperParser
        * Added 'interface_template', 'device_type' and 'device_name' keys support to super parser
    * Modified ShowHwModuleUsbflash1Security
        * show hw-module usbflash1 switch {switch_num} security status

* iosxr
    * Added ShowCdpInterface
        * Added parser for show cdp interface
        * Added parser for show cdp interface {interface}

* showplatformifmmapping
    * iosxe
        * Changed switch key from dynamic to static
    * c9500
        * Changed switch key from dynamic to static


