| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |    20.9       |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* IOS
    * Added ShowLoggingSchema
    * Added ShowLogging
    * Added ShowProcessesMemory
        * show processes memory

* IOSXE
    * Added ShowApDot11DualBandSummary:
        * For 'show ap dot11 dual-band summary'
    * Added ShowApSummary:
        * show ap summary
    * Added ShowSdwanOmpTlocs
        * show sdwan omp tlocs
    * Added ShowSdwanOmpPeers
        * show sdwan omp peers
    * Added ShowSdwanOmpTlocPath
        * show sdwan omp tloc path
    * Added ShowPlatformResources
        * show platform resources
    * Added ShowPlatformHardwareQfpActiveTcamResourceManagerUsage
        * show platform hardware qfp active tcam resource-manager usage
    * Updated ShowPlatformHardwareQfpActiveFeatureAppqoe to support 17.4 release output.
        * show platform hardware qfp active feature appqoe stats all
    * Added ShowSdwanUtdEngine
        * show sdwan utd engine
    * Added ShowUtdEngineStandardStatus
        * show utd engine standard status
    * Added c9300 ShowEnvironmentAll:
        * for command 'show environment all'

* Viptela
    * Added ShowOmpTlocs
        * show omp tlocs
    * Added ShowOmpPeers
        * show omp peers
    * Added ShowOmpTlocPath
        * show omp tloc path

* IOSXR
    * Added show_mfib file to parsers
    * Added ShowLogging
    * Added ShowMfibRouteSummary
        * show mfib route summary
        * show mfib route summary location {location}
        * show mfib vrf {vrf} route summary
        * show mfib vrf {vrf} route summary location {location}
    * Added ShowProcessesMemory
        * show processes memory

* JUNOS
    * Added ShowRouteReceiveProtocolExtensive:
        * 'show route receive-protocol bgp {peer_address} {target_address} extensive'
    * Added ShowRouteReceiveProtocolPeerAddressExtensive
        * show route receive-protocol bgp {peer_address} extensive
    * Added ShowOspfNeighborInstanceAll
        * show ospf neighbor instance all
    * Added ShowOspf3NeighborInstanceAll
        * show ospf3 neighbor instance all
    * Added ShowRouteProtocolProtocolExtensiveIpaddress
        * show route protocol {protocol} extensive {ipaddress}
    * Added ShowSystemConnections
        * show system connections
    * Added ShowSystemInformation
        * show system information
    * Added ShowFirewallLog
        * show firewall log

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------

* UTILS
    * Modified add_parser:
        * Now properly accepts parsers with 'cli_command' defined as a string.

* IOSXR
    * Modified AdminShowDiagChassis:
        * Added support for new style of output
        * Changed serial_number, part_revision, mfg_deviation, hw_version, and mfg_bits to Optional
    * Modified ShowPlatform:
        * Added support for OPERATIONAL state and for fan/power
    * Modified ShowIsisStatisticsSchema:
        * updated queue_size as optional
    * Modified ShowControllersNpuInterfaceInstanceLocation:
        * Changed parser to account for hexidecimal values rather than only integers
    * Modified AdminShowDiagChassis:
        * Added support for new style of output
        * Changed serial_number, part_revision, mfg_deviation, hw_version, and mfg_bits to Optional
    * Modified ShowPlatform:
        * Added support for OPERATIONAL state and for fan/power
    * Modified ShowRouteIpv6:
        * Updated regex pattern p2 to accommodate various outputs

* IOSXE
    * Updated ShowBgpSummarySuperParser
        * Updated Regex in p9 to capture '*'
    * Updated test_show_ip_bgp_all_summary_golden2
        * Added '*' in test case
    * Updated ShowChassisRoutingEngine
        * Updated Regex and code to parse wider range of CLI output
    * Updated TestShowChassisRoutingEngine
        * Added golden_output2/golden_parsed_output2 data for unit test
    * Modified ShowAccessListsSchema
        * matched_packets key can be a str or int
    * Modified ShowAccessLists
        * matched_packets captured group in p_ip_acl_standard can
          now capture a str or int
        * use captured group sequence if access list value exists
    * Modified golden_output_2_expected.py
        * matched correct output
    * Modified golden_output_customer_expected.py
        * matched correct output
    * Modified ShowBgpDetailSuperParser:
        * changed regrex pattern p2_1 and p3_1
    * Updated ShowPlatform
        * Added code to accomodate wider variety of CLI output
    * Updated TestShowInventory
        * Added golden_output3/golden_parsed_output3 data for unit test
    * Fixed ShowPolicyMapTypeSuperParser
        * Modified regex p2 and p5 to support various outputs
    * Fixed ShowPolicyMap
        * Added regex p2_4 and modified p8_3 and p11 to support various outputs
    * Modified ShowIpInterface:
    	* Added new patterns supporting various outputs based on the user device output
    	* Added the corresponding unit tests reflecting the applied changes
    * Updated c9300 ShowInventory:
        * Fix regex p2 to match more various ouput
    * Modified ShowLoggingSchema:
        * Added new schema
    * Modified ShowLogging:
        * Added regex patterns to capture data in new schema

* NXOS
    * Modified ShowInterface:
        * Update p1 regex to match more output
    * Modified ShowIpMrouteVrfAll:
        * Handles internal in output
    * Fixed ShowIpMrouteVrfAll:
        * Also handles flags in outgoing interfaces
    * Modified ShowInterfaceStatus:
        * Fix to parse Nve interface
    * Modified ShowIpMrouteVrfAll:
       * Updated regex p5 to support various outputs.
    * Modified ShowInterfaceBrief:
        * Updated regex pattern p6 to accommodate various outputs.
    * Modified ShowSpanningTreeDetail:
        * Updated regrex pattern p14 to capture negative values
    * Modified ShowLldpTimersSchema:
        * Added new keys and make to Optional

* Junos
    * Modified ShowRouteProtocolExtensive:
        * Handles AS Path better
    * Modified ShowSystemUptime:
        * Updated regex pattern {p6} to accommodate various outputs.
    * Modified ShowRouteReceiveProtocolExtensive:
        * Changed key 'active-tag' into Optional.
    * Modified ShowRouteReceiveProtocol
        * Updated regex p2 to support more outputs.
        * Added 'show route receive-protocol {protocol} {peer} {target}' in cli_command
    * Modified ShowRouteReceiveProtocol
        * Enhanced regex pattern p2, as well as proceeding
          code to develop parser
        * Created regex patterns p3 and p4
    * Modified ShowRouteAdvertisingProtocol
        * Enhanced regex pattern p2, as well as proceeding
          code to develop parser
        * Created regex patterns p3 and p4
    * Modified Ping:
        * ping {addr} source {source} count {count}
    * Modified ShowBgpNeighbor
        * Modified p36 code block in if condition
    * Updated ShowSystemUsers
        * Fixed regex for output of show system user
    * Fixed ShowFirewallCounterFilter
        * Fixed Cli command to accept options for filter and counter_name
    * Rewrote ShowFirewall
    * Modified ShowBgpNeighbor
        * Added regex to support more output
    * Modified ShowRouteProtocolExtensive
        * Added regex to support accepted tag
        * Added regex to support peer-as tag
    * Modified ShowBgpNeigbor
        * show bgp neighbor {neighbor}
    * Modified ShowRouteProtocolExtensive
        * Added more support by adding regex