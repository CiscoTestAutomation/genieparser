| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |    20.10      |

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowVersion
        * Modified regex to support different output
    * Modified ShowLogging:
    * To support various outputs
    * Updated ShowSpanningTreeSummary mapping dict
        * to parse 'Platform PVST Simulation' information
    * Modified ShowIpNbarDiscovery
        * Fixed parser and testcase
    * Updated ShowSpanningTreeMstDetail regex and schema to parse more output
    * Updated ShowPlatform to support C9200 output
    * Updated ShowRedundancySchema to set config_register as optional
    * C9500
        * Updated ShowVersionSchema to set curr_config_register as optional
        * Updated ShowRedundancySchema to set config_register as optional
* JUNOS
    * Modified ShowLDPOverview:
    * Updated var_dict to capture missing CLI output
    * Updated schema for interface-address from a str to list
    * Updated code to capture interface-address correctly
    * Modified ShowClassOfService:
    * Updated regex pattern to support various output
    * Optional keys updated in schema
    * Modified ShowRouteAdvertisingProtocol:
    * Update regex pattern p2 to support more outputs
    * Modified ShowLdpSessionIpaddressDetail:
    * captured all interface address's if there was more than one 
    * Set ldp-up-time as Optional key
    * Updated p14 regex pattern to capture Reconnect Time
    * Changed "ldp-interface-local-address" to Optional.
    * Updated regex pattern p1 to accommodate various outputs.
    * Modified ShowSystemUptimeSchema
        * Made time-source optional
    * Modified ShowPfeStatisticsTrafficSchema
        * Made tcp-header-error-discard optional
        * Made pfe-fabric-input optional
        * Made pfe-fabric-input-pps optional
        * Made pfe-fabric-output optional
        * Made pfe-fabric-output-pps optional
    * Modified ShowInterface:
    * Optional added to some keys not appearing in output
    * Modified ShowRouteTable:
    * Updated regex pattern to support 'tag'
* IOSXR
    * Updated AdminShowDiagChassis regex and schema to parse more output
    * Modified ShowPimVrfInterfaceDetail:
        * update dr regexp to match more output
    * Modified ShowMribVrfRoute:
        * update interface regexp to match more output
    * Updated ShowLldpNeighborsDetail not to convert junos interface name
* IOSXE:
    * ShowIsisNeighbors
        * Made it work in case no tag line in the output 
    * ShowInterfaces
        * Updated so it picks media_types more flexibly 
        * Made the following keys optional
        * ldp-remote-address, ldp-keepalive-time, ldp-local-address, ldp-session-address
        * Added new unit tests
* IOS
    * Modified ShowLogging:
        * Fixed Unittest failures
    * Updated to inherit parser class from IOSXE
* JUNOS:
    * ShowRSVPNeighborDetailSchema
        * Made fields below optional
    * Updated ShowChassisFpc:
    * Added support for comment in output
    * Updated ShowLogFilename:
    * Added support for match in command
* NXOS
    * Modified ShowInterface regex:
    * To match 'XCVR not inserted' in output
    * Modified ShowInterface:
    * Updated regex to support more output for last_link_flapped


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowWlanSummary:
    * show wlan summary
    * Added ShowCtsRoleBasedPermissions
        * show cts role-based permissions
    * Modified ShowLogging:
    * show logging | exclude {exclude}
    * Added ShowCtsRbacl
        * show cts rbacl
    * Added ShowNetconfSession
        * show netconf session
    * Added ShowNetconfYangSessions
        * show netconf-yang sessions
    * Added ShowNetconfYangSessionsDetail
        * show netconf-yang sessions detail
    * Added ShowWirelessClientSummary:
    * show wireless client summary
    * Added ShowPlatformSoftwareMemoryRpActive:
    * show platform software memory mdt-pubd RP active
    * Added ShowPlatformSoftwareMemoryRpActiveBrief:
    * show platform software memory mdt-pubd RP active brief
    * Added ShowPlatformSoftwareMemoryRpActiveAllocCallsite:
    * show platform software memory mdt-pubd RP active alloc callsite
    * Added ShowPlatformSoftwareMemoryRpActiveAllocCallsiteBrief:
    * show platform software memory mdt-pubd RP active alloc callsite brief
    * Added ShowPlatformSoftwareMemoryRpActiveAllocType:
    * show platform software memory mdt-pubd RP active alloc type <type>
    * Added ShowPlatformSoftwareMemoryRpActiveAllocTypeBrief:
    * show platform software memory mdt-pubd RP active alloc type <type> brief
    * Added ShowPlatformSoftwareMemorySwitchActive:
    * show platform software memory mdt-pubd switch active <slot>
    * Added ShowPlatformSoftwareMemorySwitchActiveBrief:
    * show platform software memory mdt-pubd switch active <slot> brief
    * Added ShowPlatformSoftwareMemorySwitchActiveAllocCallsite:
    * show platform software memory mdt-pubd switch active <slot> alloc callsite
    * Added ShowPlatformSoftwareMemorySwitchActiveAllocType:
    * show platform software memory mdt-pubd switch active <slot> alloc type component
    * Added ShowPlatformSoftwareMemorySwitchActiveAllocTypeBrief:
    * show platform software memory mdt-pubd switch active <slot> alloc type component brief
    * Added ShowPlatformSoftwareMemoryChassisActive:
    * show platform software memory mdt-pubd chassis active <slot>
    * Added ShowPlatformSoftwareMemoryChassisActiveBrief:
    * show platform software memory mdt-pubd chassis active <slot> brief
    * Added ShowMemoryDebugLeaks:
        * show memory debug leaks
    * Added ShowCtsEnvironmentData
        * show cts environment-data
    * Added ShowPlatformSoftwareYangManagementProcess:
        * show platform software yang-management process
    * ShowPlatformSoftwareYangManagementProcessMonitor:
        * show platform software yang-management process monitor
    * ShowPlatformSoftwareYangManagementProcessState:
        * show platform software yang-management process state
    * Added ShowShowApDot115GhzSummary:
    * show ap dot11 5ghz summary
    * Added ShowWirelessMobilityApList:
    * show wireless mobility ap-list
    * Updated ShowPolicyMapTypeSuperParser:
    * Enhanced regex to support new output
    * Added ShowDeviceTrackingDatabase:
    * show device-tracking database
    * Added ShowApLedBrightnessLevelSummary:
    * show ap led-brightness-level summary
    * Added ShowApCdpNeighbor:
    * show ap cdp neighbor
    * Added ShowIpNbarDiscovery:
        * show ip nbar protocol-discovery protocol
    * Added ShowTelemetryIETFSubscription:
        * 'show telemetry ietf subscription all'
        * 'show telemetry ietf subscription all brief'
        * 'show telemetry ietf subscription {sub_id} brief'
        * 'show telemetry ietf subscription dynamic'
        * 'show telemetry ietf subscription {sub_id}'
    * Added ShowTelemetryIETFSubscriptionDetail:
        * 'show telemetry ietf subscription all detail'
        * 'show telemetry ietf subscription {sub_id} detail'
        * 'show telemetry ietf subscription dynamic detail'
    * Added ShowTelemetryIETFSubscriptionReceiver:
        * 'show telemetry ietf subscription {sub_id} receiver'
        * 'show telemetry ietf subscription receiver'
    * Added ShowShowApDot115GhzChannel:
    * show ap dot11 5ghz channel
    * Added ShowWirelessFabricClientSummary
    * show wireless fabric client summary
    * Added ShowSnmpUser:
    * show snmp user
* ADDED SHOWCHASSIS:
    * show chassis
* IOSXR
    * Modified ShowRouteIpv4:
    * Updated regex pattern <p6> to support OSPF output
    * Added ShowImDampening:
        * show im dampening
    * Added ShowImDampeningIntf:
        * show im dampening {interface}
    * Added ShowRibTables:
        * show rib tables
    * Added ShowRibTablesSummary:
        * show rib tables summary
* ASA
    * Created Show Traffic ASA
* IOS
    * Modified ShowLogging:
    * show logging | exclude {exclude}
    * Added ShowModule:
        * show module
* ADDED SHOWAPCONFIGGENERAL:
    * show ap config general
* JUNOS
    * Updated Ping for:
    * ping {addr} source {source} size {size} do-not-fragment
    * Added ShowSnmpConfiguration:
    * show configuration snmp
    * Added ShowSnmpStatistics
        * show snmp statistics
    * Added ShowRSVPSessionTransit
        * subclass of ShowRSVPSession: Handle command 'show rsvp session transit'
    * Added ShowTaskMemory:
        * show task memory
* ADDED SHOWCTS:
    * show cts
* ADDED SHOWWIRELESSPROFILEPOLICYDETAILED:
    * show wireless profile policy detailed
* COMMON
    * Updated ci_parsing_folder script to accept argument '--number' or '-n' to specify which test output to run
* ADDED SHOWSERVICEINSERTIONTYPEAPPQOESERVICENODEGROUP FOR:
    * show service-insertion type appqoe service-node-group
* LINUX
    * Added VimCmdVmsvcGetAllVms
        * vim-cmd vmsvc/getallvms
    * Added VimCmdVmsvcSnapshotGetVmId
        * vim-cmd vmsvc/snapshot.get {vm_id}
* ADDED SHOWREDUNDANCYSWITCHOVERHISTORY:
    * show redundancy switchover history
* ADDED SHOWWIRELESSSTATSAPJOINSUMMARY:
    * show wireless stats ap join summary
* ADDED SHOWWLANALL:
    * show wlan all
* VIPTELA
    * Added ShowBootPartition
        * show boot-partition
* ADDED SHOWCLASSMAP:
    * show class-map {name}
* ADDED SHOWROMVAR:
    * show romvar
* ADDED SHOWWIRELESSCTSSUMMARY:
    * show wireless cts summary
* ADDED SHOWWIRELESSPROFILEPOLICYSUMMARY:
    * show wireless profile policy summary
* ADDED SHOWWIRELESSSTATSMOBILITY:
    * show wireless stats mobility
* JUNOS:
    * Added ShowConfigurationFamilyBridgeVlanId:
    * show configuration interfaces {interface} unit {unit} family bridge vlan-id
* ADDED SHOWSNMP:
    * show snmp
* ADDED SHOWWIRELESSFABRICSUMMARY:
    * show wireless fabric summary
