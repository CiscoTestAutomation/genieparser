--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxr
    * Modified ShowPceIPV4PeerDetail
        * Added Instantiation option for Capabiities to schema as Optional.
        * Added MD5 option to schema as Optional.
        * Added Maximum SID depth option to schema as Optional.
        * Added Last pcerror option to schema as Optional.
    * Modified ShowIsisInterface
        * Added Total bandwidth as Optional parameter to schema.
        * Added Delay normalization as Optional parameter to schema.
        * Added Interval and Offset options in delay normalization to schema.
        * Added Link loss as Optional parameter to schema.
        * Added Metric fallback as Optional parameter to schema.
        * Added Bandwidth and Anomaly options in metric fallback to schema.
        * Modified Adjacency formation, State, Prefix advertisement, Metric, Weight and Mpls as Optional under topology in schema.
        * Added Status option in Ldp sync as Optional parameter to schema.
        * Modified Forwarding address, Global prefix as Optional under address_family in schema.
        * Added <r56> to parse the optional line with the format "LDPv4 Sync Status    Achieved".
        * Added <r57> to parse the optional line with the format "Total bandwidth                1000000".
        * Added <r58> to parse the optional line with the format "Metric fallback".
        * Added <r59> to parse the optional line with the format "Bandwidth (L1/L2)    Inactive/Inactive".
        * Added <r60> to parse the optional line with the format "Anomaly (L1/L2)    Inactive/Inactive".
        * Added <r61> to parse the optional line with the format "Delay Normalization      Interval0 Offset0".
        * Added <r62> to parse the optional line with the format "Link Loss                1".

* iosxe
    * Modified ShowLispAR
        * changed the regular expression P2 to match any type of ipv6 address
    * Modified ShowDeviceTrackingDatabaseDetails
        * Enhanced the regex to match "time_left" with format "224 s(7177 s)"
    * Modified Ping
        * Added 'extended_data' variable to Ping.
    * Modified ShowIpProtocols
        * Fixed to capture ISIS enabled interfaces properly
    * Modified ShowIpv6Protocols
        * Fixed to capture ISIS enabled interfaces properly
    * Modified ShowCryptoIkev2Stats Added Quantum resistance line to parser.
    * Modified ShowInventoryRaw
        * changed the regular expression P1 to work Temp values.
    * Modified ShowIpOspf
        * Updated regex p12_4 to match warning-only
        * Update regex p33 to match warning-only
    * Modified ShowCdpNeighbors parser
        * Added a new command "show cdp neighbors {interface}" in the existing schema.
    * Modified ShowSwitch
        * Made hw_ver parameter as optional to support some of the outputs witout hw_ver.
    * Modified ShowVersion
        * Added system_fpga_version parameter as optional to support some of the outputs with System FPGA Version.
    * Modified ShowHardwareLed
        * modified code to match code for not having SWITCH match or non stack devices, also for IE3x00 devices
    * Modified ShowIdpromInterface.
    * Added the parser in the proper file show_idprom.py.

* nxos
    * Modified ShowIpv6MrouteVrfAll
        * Updated regex pattern p5_1  to accommodate bridge only outputs as well.
        * Moved the regex patterns outside of the for loop so that they will
    * Modified ShowRouting
        * Updated regex pattern to match nextop line attr "tunnelid" to match hex properly [0-9a-fA-Fx].
        * Updated regex pattern to match nextop line attr "segid" to only optionally match colon.
    * Modified ShowBgpSessions
        * Added regexes p7_1 and p7_2 in order to correctly parse the outputs where there is a line break due to large AS numbers
    * Modified ShowBgpVrfAllAll
        * Reordered <p3_4> to match after <p3_1>, <p3_2>, and <p3_3> to avoid matching nexthop when a network is the only value on the line.

* cheetah
    * Modified show_capwap_client_rcb
        * Modified capwap image download, hyperlocation options to schema as Optional.

* deleted the duplicate parser under iosxe/show_platform.py and iosxe/c9300/show_platform.py.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowIpArpInspectionInterfaces
        * show ip arp inspection interfaces {interface}
    * Added ShowTemplateBrief
        * show template brief
    * Added ShowSwitchStackRingSpeed
        * Parser for show switch stack-ring speed
    * Added ShowPlatformMatmMacTable Parser
        * Parser for "show platform hardware fed switch active matm macTable"
    * Added ShowOspfv3Gracefulrestart
        * added new parser for cli "show ospfv3 {pid} graceful-restart"
    * Added ShowOspfv3FloodList
        * added new parser for cli "show ospfv3 {pid} flood-list"
    * Added ShowOspfv3Events
        * added new parser for cli "show ospfv3 {pid} events"
    * Added ShowOspfv3Neighbor
        * show ospfv3 {pid} neighbor
    * Added ShowOspfv3RetransmissionList
        * show ospfv3 {pid} retransmission-list
    * Added ShowOspfv3RequestList
        * show ospfv3 {pid} request-list
    * Added ShowSdwanAppFwdDpiFlows
        * show sdwan app-fwd dpi flows parser
    * Fixed ShowSdwanAppfwdCflowdStatistics
        * Whole method was under "if output" statement - fixed it
    * Added ShowVlanDot1qTagNative
        * show vlan dot1q tag native
    * Added ShowCefInterfaceVlanBrief
        * show cef interface Vlan {id} brief
    * Added ShowCefInterfacePolicyStatistics
        * Parser for show cef interface policy-statistics
    * Added ShowEnvironmentStack
        * show environment stack
    * Added ShowCableDiagnosticsTdrInt
        * show cable-diagnostics tdr interface {interface}
    * Added ShowSnmpEngineid
        * Parsef for show snmp engineid
    * Added ShowSnmpCommunity
        * Parsef for show snmp community
    * Added ShowSnmpMibBulkstatTransfer
        * Parsef for show snmp mib bulkstat transfer
    * Added ShowLicenseHistoryMessage
        * show license history message
    * Added ShowSdwanUtdDataplaneConfig
        * show sdwan utd dataplane config
    * Added ShowPlatformHardwareFedSwitchStateFwdAsicAbstractionPrintResourceHandleClient_le parser
        * Added ShowPlatformHardwareFedSwitchStateFwdAsicAbstractionPrintResourceHandleClient_le parser
    * Added ShowIpOspfNsr
        * added new parser for cli 'show ip ospf nsr'
    * Added ShowInterfacesTransceiverSupportedlist
        * Parser for show interfaces transceiver supported-list
    * Added ShowIpArpInspectionStatisticsVlan
        * show ip arp inspection statistics vlan {num}
    * Added ShowTemplateInterfaceSourceBuiltInOriginalAll Parser
        * Parser for "show template interface source built-in Original all"
    * Added ShowlldpErrors
        * added new parser for cli "show lldp errors"
    * Modified ShowBoot and ShowBootSystem
        * Modified regexp of boot mode in ShowBoot parser to display boot mode other then 'device'.
        * Modified regexp of boot mode and boot variable in ShowBootSystem parser.
    * Added ShowIpv6MldSnoopingVlan
        * show ipv6 mld snooping vlan
    * Added ShowIpv6MldSnoopingMrouter
        * show ipv6 mld snooping mrouter
    * Added ShowSpanningTreeInterfaceDetail
        * Parser for "show spanning-tree interface detail"
    * Added ShowSpanningTreeInterface
        * Parser for "show spanning-tree interface"
    * Added ShowSpanningTreeInconsistentports
        * Parser for "show spanning-tree inconsistentports"
    * Added ShowOspfv3Interface
        * show ospfv3 {pid} interface
    * Added ShowMacroAutoDevice Parser
        * Parser for "show macro auto device"
    * Added ShowPlatformSoftwareNodeClusterManagerSwitchB0Node
        * show platform software node cluster-manager switch {mode} B0 node {node}
    * Added ShowPlatformSoftwareFedStateVpSummaryInterfaceIf_id parser
        * Added ShowPlatformSoftwareFedStateVpSummaryInterfaceIf_id parser
    * Added ShowIpCefSummary
        * Parser for show ip cef summary
    * Added ShowPlatformRewriteUtilization
        * parser for chec the rewrite utilization
    * Added ShowAdjacencySummary
        * parser for show adjacency summary
    * Added ShowOspfv3
        * show ospfv3
        * show ospfv3 vrf {vrf_id}
    * Added ShowOspfv3DatabaseSummaryDetail
        * show ospfv3 database database-summary detail
        * show ospfv3 {process_id} database database-summary detail
    * Added ShowRunSectionOspfv3
        * show running-config | section ospfv3
    * Added ShowPmVpInterfaceVlan parser
        * Added ShowPmVpInterfaceVlan parser
    * Added ShowMacAddressTableCount
        * show mac address-table count
    * Added ShowOspfv3StatisticDetail
        * New parser for "show ospfv3 {pid} statistic detail"
    * Added ShowInstallCommitted
        * show install committed
    * Added ShowLoggingOnboardSwitchClilog parser
        * for 'Show logging onboard switch {switch} clilog'
    * Added ShowLoggingOnboardSwitchActiveStatus parser
        * for 'show logging onboard switch active status'
    * Added ShowLoggingOnboardSwitchActiveUptimeDetail parser
        * for 'show logging onboard switch active uptime detail'
    * Added ShowLoggingOnboardSwitchContinuous parser
        * for 'show logging onboard switch {switch_num} {include} continuous'
    * Added ShowPlatformPmPortDataInt parser
        * Added ShowPlatformPmPortDataInt parser
    * Added ShowMacAddressTableCountVlan
        * Parser for show mac address space
    * Added ShowIpDnsView
        * show ip dns view parser
    * Added ShowAccessSessionsInfo
        * show access-session info
    * Added ShowAaaDeadCriteriaRadius Parser
        * Parser for "show aaa dead-criteria radius"
    * Added ShowCdpTraffic Parser
        * Parser for "show cdp traffic"
    * Added ShowCdpInterface Parser
        * Parsre for "show cdp interface"
    * Added ShowCdpEntry Parser
        * Parser for "show cdp entry"
    * Added ShowCefInterface Parser
        * Parser for "show cef interface {interface}"
    * Added ShowCefInterfaceInternal Parser
        * Parser for "show cef interface {interface} internal"
    * Added parser
        * Added ShowIpAdmissionCache parser
    * Added parser
        * Added ShowAccessSessionEventLoggingMac parser
    * Added ShowAaaSessions parser
        * Added ShowAaaSessions parser
    * Added ShowDot1xStatistics parser
        * Added ShowDot1xStatistics parser
    * Added ShowAaaMemory parser
        * Added ShowAaaMemory parser
    * Added ShowPlatformSoftwareWiredClientSwitchR0 parser
        * Added ShowPlatformSoftwareWiredClientSwitchR0 parser
    * Added ShowPlatformAuthenticationSbinfoInterface parser
        * Added ShowPlatformAuthenticationSbinfoInterface parser
    * Added ShowPlatformHostAccessTableIntf parser
        * Added ShowPlatformHostAccessTableIntf parser
    * Added ShowPlatformSoftwareFedSwitchStateIfmIfIdIf_id parser
        * Added ShowPlatformSoftwareFedSwitchStateIfmIfIdIf_id parser

* added showiparpinspectionlog
    * show ip arp inspection log

* iosxr
    * Modified ShowRcmdIsisEventSpf
        * show rcmd isis {isis} event spf {spf_run_no}
    * Modified ShowRcmdIsisEventPrefix
        * show rcmd isis {isis} event prefix {prefix_name}
    * Added ShowRcmdIsisEventPrefixLastDetail
        * show rcmd isis {isis} event prefix {prefix_name} last {event_no} detail
        * show rcmd isis {isis} event prefix {prefix_name} detail
    * Added ShowRcmdIsisEventSpfLastDetail
        * show rcmd isis {isis} event spf last {event_no} detail
        * show rcmd isis {isis} event spf {spf_run_no} detail
    * Added ShowRcmdProcess
        * show rcmd process
    * Added ShowRcmdInterfaceEvent
        * show rcmd interface event

* show access-session info switch {switch} r0


