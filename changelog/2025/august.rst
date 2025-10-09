--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added acm merge parser
        * Added Acm merge
        * Added Acm replcae]
        * Added Acm rollback
    * Added ShowPlatformMrpMappings
        * Added  schema and parser for 'show platform mrp mappings' command.
    * Added Parser for parsers for below commands
        * Added show mrp ring <ring-id>statistics all
    * Added Parser for parsers for below commands
        * show platform software fed switch {switch_num} wdavc flows
        * show platform software fed switch {switch_num} wdavc function wdavc_ft_show_all_flows_seg_ui
    * Added ShowPlatformHardwareFedActiveQosQueueConfigInternalPortTypeRecyclePortPortNumAllAsic parser
        * Added schema and parser for 'show platform hardware fed {state} qos queue config internal port_type recycle-port port_num all asic {asic_number}''
    * Added below parser for c9550 by inheriting from c9350
        * ShowPlatformTcamUtilization
        * ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear
        * ShowPlatformSoftwareFedActiveAclInfoDbDetail
        * ShowPlatformHardwareFedQosSchedulerSdkInterface
    * Added Parser for below command
        * show tcp brief numeric
    * Modified ShowInventory
        * Added logic support if name is a digit
    * Added ShowSubsysNameIpfib
        * show subsys name ipfib
    * Added ShowIpv6VirtualReassemblyFeatures parser
        * Added schema and parser for 'show ipv6 virtual-reassembly features'
    * Added ShowPlatformStatus schema in iosxe/ie3k
        * Added parser for show platform status in iosxe/ie3k
    * Added ShowFlowMonitorCacheSortOrderSuperParser
        * show flow monitor {name} cache sort counter bytes layer2 long top {value} format table
        * show flow monitor {name} cache sort counter bytes long top {value} format table
        * show flow monitor {name} cache sort counter packets long top {value} format table
        * show flow monitor {name} cache sort flow direction top {value} format table
        * show flow monitor {name} cache sort timestamp absolute {time} top {value} format table
        * show flow monitor {name} cache sort datalink dot1q priority top {value} format table
        * show flow monitor {name} cache sort datalink dot1q vlan {direction} top {value} format table
        * show flow monitor {name} cache sort datalink ethertype top {value} format table
        * show flow monitor {name} cache sort datalink mac {destination} address {direction} top {value} format table
        * show flow monitor {name} cache sort datalink vlan {direction} top {value} format table
        * show flow monitor {name} cache sort ipv4 {destination} address top {value} format table
        * show flow monitor {name} cache sort ipv4 protocol top {value} format table
        * show flow monitor {name} cache sort ipv4 tos top {value} format table
        * show flow monitor {name} cache sort ipv4 ttl top {value} format table
        * show flow monitor {name} cache sort ipv4 version top {value} format table
        * show flow monitor {name} cache sort ipv6 {destination} address top {value} format table
        * show flow monitor {name} cache sort ipv6 protocol top {value} format table
        * show flow monitor {name} cache sort ipv6 hop-limit top {value} format table
        * show flow monitor {name} cache sort ipv6 traffic-class top {value} format table
        * show flow monitor {name} cache sort ipv6 version top {value} format table
        * show flow monitor {name} cache sort transport tcp flags top {value} format table
        * show flow monitor {name} cache sort transport {port} top {value} format table
        * show flow monitor {name} cache sort {order} counter bytes layer2 long top {value} format table
        * show flow monitor {name} cache sort {order} counter bytes long top {value} format table
        * show flow monitor {name} cache sort {order} counter packets long top {value} format table
        * show flow monitor {name} cache sort {order} flow direction top {value} format table
        * show flow monitor {name} cache sort {order} timestamp absolute {time} top {value} format table
        * show flow monitor {name} cache sort {order} datalink dot1q priority top {value} format table
        * show flow monitor {name} cache sort {order} datalink dot1q vlan {direction} top {value} format table
        * show flow monitor {name} cache sort {order} datalink ethertype top {value} format table
        * show flow monitor {name} cache sort {order} datalink mac {destination} address {direction} top {value} format table
        * show flow monitor {name} cache sort {order} datalink vlan {direction} top {value} format table
        * show flow monitor {name} cache sort {order} ipv4 {destination} address top {value} format table
        * show flow monitor {name} cache sort {order} ipv4 protocol top {value} format table
        * show flow monitor {name} cache sort {order} ipv4 tos top {value} format table
        * show flow monitor {name} cache sort {order} ipv4 ttl top {value} format table
        * show flow monitor {name} cache sort {order} ipv4 version top {value} format table
        * show flow monitor {name} cache sort {order} ipv6 {destination} address top {value} format table
        * show flow monitor {name} cache sort {order} ipv6 protocol top {value} format table
        * show flow monitor {name} cache sort {order} ipv6 hop-limit top {value} format table
        * show flow monitor {name} cache sort {order} ipv6 traffic-class top {value} format table
        * show flow monitor {name} cache sort {order} ipv6 version top {value} format table
        * show flow monitor {name} cache sort {order} transport tcp flags top {value} format table
        * show flow monitor {name} cache sort {order} transport {port} top {value} format table
    * Added ShowFlowMonitorCacheSortOrderCounter
        * show flow monitor {name} cache sort {order} counter bytes layer2 long top {value} format table
        * show flow monitor {name} cache sort {order} counter bytes long top {value} format table
        * show flow monitor {name} cache sort {order} counter packets long top {value} format table
        * show flow monitor {name} cache sort counter bytes long top {value} format table
        * show flow monitor {name} cache sort counter bytes layer2 long top {value} format table
        * show flow monitor {name} cache sort counter packets long top {value} format table
    * Added ShowFlowMonitorCacheSortOrderFlow
        * show flow monitor {name} cache sort {order} flow direction top {value} format table
        * show flow monitor {name} cache sort flow direction top {value} format table
    * Added ShowFlowMonitorCacheSortOrderTimestamp
        * show flow monitor {name} cache sort {order} timestamp absolute {time} top {value} format table
        * show flow monitor {name} cache sort timestamp absolute {time} top {value} format table
    * Added ShowFlowMonitorCacheSortOrderTransport
        * show flow monitor {name} cache sort {order} transport tcp flags top {value} format table
        * show flow monitor {name} cache sort {order} transport {port} top {value} format table
        * show flow monitor {name} cache sort transport tcp flags top {value} format table
        * show flow monitor {name} cache sort transport {port} top {value} format table
    * Added ShowFlowMonitorCacheSortOrderDatalink
        * show flow monitor {name} cache sort {order} datalink dot1q priority top {value} format table
        * show flow monitor {name} cache sort {order} datalink dot1q vlan {direction} top {value} format table
        * show flow monitor {name} cache sort {order} datalink ethertype top {value} format table
        * show flow monitor {name} cache sort {order} datalink mac {destination} address {direction} top {value} format table
        * show flow monitor {name} cache sort {order} datalink vlan {direction} top {value} format table
        * show flow monitor {name} cache sort datalink dot1q priority top {value} format table
        * show flow monitor {name} cache sort datalink dot1q vlan {direction} top {value} format table
        * show flow monitor {name} cache sort datalink ethertype top {value} format table
        * show flow monitor {name} cache sort datalink mac {destination} address {direction} top {value} format table
        * show flow monitor {name} cache sort datalink vlan {direction} top {value} format table
    * Added ShowFlowMonitorCacheSortOrderIPv4
        * show flow monitor {name} cache sort {order} ipv4 {destination} address top {value} format table
        * show flow monitor {name} cache sort {order} ipv4 protocol top {value} format table
        * show flow monitor {name} cache sort {order} ipv4 tos top {value} format table
        * show flow monitor {name} cache sort {order} ipv4 ttl top {value} format table
        * show flow monitor {name} cache sort {order} ipv4 version top {value} format table
        * show flow monitor {name} cache sort ipv4 {destination} address top {value} format table
        * show flow monitor {name} cache sort ipv4 protocol top {value} format table
        * show flow monitor {name} cache sort ipv4 tos top {value} format table
        * show flow monitor {name} cache sort ipv4 ttl top {value} format table
        * show flow monitor {name} cache sort ipv4 version top {value} format table
    * Added ShowFlowMonitorCacheSortOrderIPv6
        * show flow monitor {name} cache sort {order} ipv6 {destination} address top {value} format table
        * show flow monitor {name} cache sort {order} ipv6 protocol top {value} format table
        * show flow monitor {name} cache sort {order} ipv6 hop-limit top {value} format table
        * show flow monitor {name} cache sort {order} ipv6 traffic-class top {value} format table
        * show flow monitor {name} cache sort {order} ipv6 version top {value} format table
        * show flow monitor {name} cache sort ipv6 {destination} address top {value} format table
        * show flow monitor {name} cache sort ipv6 protocol top {value} format table
        * show flow monitor {name} cache sort ipv6 hop-limit top {value} format table
        * show flow monitor {name} cache sort ipv6 traffic-class top {value} format table
        * show flow monitor {name} cache sort ipv6 version top {value} format table
    * Added Parser for parsers for below commands
        * 'show flow monitor {monitor_name} cache sort application name top {top_count}',
        * 'show flow monitor {monitor_name} cache sort connection {connetion_type} counter bytes network long top {top_count}'
    * Added
        * Added schema and parser for show ip ospf neighbor summary
        * Added schema and parser for show ipv6 ospf neighbor summary
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightAclTableStatistics parser
        * Added schema and parser for cli "show platform hardware fed {state} fwd-asic insight acl-table statistics"
    * Modified ShowPlatformSoftwareFedSwitchActiveAclInfoSdkDetail parser
        * Added optional keys in schema and p15 regex for "show platform software fed {state} switch active acl info sdk detail"
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightSanetAccsecClientTable parser.
        * Added parser for cli 'show platform hardware fed switch {switch} fwd-asic insight sanet_accsec_client_table()'.
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightAccsecClientClassificationEnablement parser.
        * Added parser for cli 'show platform hardware fed switch {switch_id} fwd-asic insight accsec_client_classification_enablement()'.
    * Added Parser for show platform hardware fed {mode} qos queue stats internal port_type recycle-port port_num {port_num} asic {asic}
        * Added a new schema and parser for the show platform hardware fed {mode} qos queue stats internal port_type recycle-port port_num {port_num} asic {asic} command.
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightL2SwitchAttachmentCircuit parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight l2_attachment_circuit_status({sys_port_gid}).
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight l2_switch_attachment_circuits({l2_ac_gid}).
    * Modified ShowPlatformSoftwareObjectManagerFpActiveStatistics
        * Added new cli in parser for show platform software object manager
    * Modified ShowClock
        * Added new time format parser for show clock
    * ShowConnection
        * show connection name 1.
    * ShowControllerT1
        * show controller T1
    * Modified ShowIpNatBpa
        * show ip nat bpa
    * Modified ShowIpOspfDatabaseNssa
        * show ip ospf database nssa.
    * Added ShowPlatformSoftwareFirewallRPActiveZones
        * sh ipv6 mfib FF03111 count
        * sh ipv6 mfib FF03111 1011200 count
    * Added ShowIsdnStatusSerial parser in show_isdn.py
    * Added schema and parser for cli 'show isdn status serial {interface}'
    * Added ShowMonitorEventTraceCryptoIkev2EventAll parser in show_monitor.py
    * Added schema and parser for cli 'show monitor event-trace crypto ikev2 event all'
    * Added ShowPlatformHardwareQfpActiveFeatureFirewallDatapathScbDetail
        * show platform hardware qfp active feature firewall datapath scb any any any any any all any detail
    * Added ShowPlatformHardwareQfpActiveFeatureNatDatapathEdm
    * 'show platform hardware qfp active feature nat datapath edm'
    * Added ShowPlatformHardwareQfpActiveFeatureNatDatapathPor parser in show_platform.py
        * Added schema and parser for cli 'Schema for show platform hardware qfp active feature nat datapath port'
    * Added howPlatformHardwareQfpActiveFeatureNatDatapathMap parser in show_platform.py
        * Added schema and parser for cli 'Parser for show platform hardware qfp active feature nat datapath map'
    * Added ShowPlatformSoftwareFirewallRPActiveZones
        * show platform software firewall RP active zones
        * show platform software firewall FP active zones
    * Added ShowPlatformSoftwareWccpWebCacheCounters parser in show_platform.py
    * Added schema and parser for cli 'show platform software wccp web-cache counters'
    * ShowPolicyMapTypeInspectPmap
        * show policy-map type inspect pmap
    * Added class ShowSubsysName parser in show_subsys.py
        * Added schema and parser for cli 'show subsys name {name}'
    * Added ShowSubsysNamePgen parser in show_subsys.py
        * Added schema and parser for cli 'show subsys name pgen'
    * Modified ShowVpdnTunnelPptpAll
        * show vpdn tunnel pptp all
    * Added class ShowXdrLinecard parser in show_platform.py
        * Added schema and parser for cli 'show xdr linecard'
    * Added class ShowZonePairSecurity parser in show_paltform.py
        * Added schema and parser for cli 'show zone-pair security'

* nxos
    * Added ShowInterfaceCountersTable
        * Added  schema and parser for 'show interface counters table' command.


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowMrpPorts
        * Updated  regex pattern in ShowMrpPorts.
    * Modified show flow monitor {name} cache parser
        * added one more type of output with connection_initiator, connection_server_nw_bytes_counter, connection_client_nw_bytes_counter parameter
    * Updated ShowMerakiConnect parser
        * Added support for "VRF" field in meraki_tunnel_interface section

* nxos
    * Modified ShowInterface
        * Updated  regex pattern in ShowInterface.
        * Updated  regex pattern in ShowCdpNeighbors and ShowCdpNeighborsDetail.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Show Intrface parser
        * Added regex to match port channel.
    * Modified Show ip mroute vrf all and show ipv6 mroute vrf all
        * Added <router_id> option.

* iosxe
    * Modified ShowFlowMonitor parser
        * Modified parser for CLI
            * 'show flow monitor {name} cache format table'
    * Modified regex pattern P1 for the given ie3k output
    * Added few fields to 'show env temperature' command output to support 'Inlet Temp Sensor' and 'HotSpot Temp Sensor' temperature readings.
    * Fixed parsing of temperature thresholds to handle spaces and units correctly.
    * Updated regex patterns to ensure accurate matching of temperature readings and thresholds.
    * Modified ShowLispInstanceIdServiceStatistics
        * Made itr_map_resolvers and etr_map_servers optional in schema.
    * Modified ShowPlatformPacketTracePacket
    * 'show platform packet-trace packet all'
    * Modified ShowBgpSummarySuperParser
        * Supported more variant output
    * Modified Dir
        * Added p2_2 regex to support dir drec0 command for c9200 devices.

* viptela/show_control
    * Updated ShowControlLocalPropertiesSchema
        * Made the port_hopped key optional to accommodate various outputs

* iosxr
    * Modified ShowControllersOpticsDb
        * Fix Parser for 'show controllers optics *' to extract multi-word Vendor Name

* parser
    * Modified Show Processes Memory Doc Value ()
        * Updated doc value for "show processes memory" to match this, instead of "show switch detail"


