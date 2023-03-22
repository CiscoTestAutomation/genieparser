--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowCableRpd
        * show cable rpd
        * show cable rpd {rpd_mac_or_ip}
    * Added ShowControllersEthernetControllerPortAsicStatisticsExceptionsSwitchAsicInRpf parser
        * for 'show controllers ethernet-controller port-asic statistics exceptions switch 1 asic 1 | in RPF'
    * Added ShowIpArpInspectionInterfaces
        * show ip arp inspection interfaces {interface}
    * Added Parser as below
        * ShowCispInterface
        * ShowCispSummary
        * ShowDeviceClassifierAttachedInterface
        * ShowDeviceClassifierAttachedMacAddress
        * ShowPlatformSoftwareFedSwitchActiveVpSummaryVlan
        * ShowPlatformSoftwareWiredClientSwitchActiveFo
        * ShowCispClients
    * Modified parser
        * ShowDeviceSensor to include 2 more commands with same output
    * Added ShowIsisMicroloopAvoidance
        * show isis microloop-avoidance flex-algo
    * Added ShowCdp Parser
        * Parser for "show cdp"
    * Added ShowMacAddressTableNotificationChange parser
        * show mac address-table notification change
    * Added ShowMacAddressTableNotificationChangeInterface parser
        * show mac address-table notification change interface {interface}
    * Added ShowPlatformPmInterfaceNumbers
        * 'show platform pm interface-numbers'
    * Added ShowLoggingOnboardSwitchDetail parser
        * for 'Show logging onboard switch {switch_num} {feature} detail'
    * Added ShowLoggingOnboardSwitchMessageDetail parser
        * for 'Show logging onboard switch {switch_num} Message detail'
    * Added ShowIpIgmpSnoopingDetail
        * show ip igmp snooping detail
    * Added ShPlatformSoftwareFedActiveVpSummaryInterfaceIf_id
        * show platform software fed active vp summary interface if_id {interface_id}
    * Added ShSoftwareFed
        * 'show platform software fed switch active ifm if-id'
    * Added parser ShowDeviceClassifierAttachedInterfaceDetail
        * show device classifier attached interface {interface} detail
    * Added ShowEtherChannelDetail Parser
        * Parser for "show etherchannel {channel_group} detail"
    * Added ShowIpIgmpVrfSnoopingGroups Parser
        * Parser for "show ip igmp vrf {vrf} snooping groups"
    * Added PingIpv6 Parser
        * Parser for "ping ipv6 {addr}"
    * Added ShowCallHome
        * show call-home parser
    * Added ShowInstallUncommitted
        * show install uncommitted
    * Added ShowVtemplate parser
        * Parser for "show vtemplate"
    * Added ShowProductAnalyticsKpiSummary
        * show product-analytics kpi summary
    * Added ShowProductAnalyticsReportSummary
        * show product-analytics report summary
    * Added ShowProductAnalyticsKpiReportId
        * show product-analytics kpi report {report}
    * Added ShowL2fibOlist
        * show l2fib output-list {id}
    * Added ShowLoggingOnboardSwitchEnvironmentContinuous Parser
        * Parser for "show logging onboard switch {switch_num} environment continuous"
    * Added ShowIpDhcpExcludedAddresses Parser
        * show ip dhcp excluded-addresses all
        * show ip dhcp excluded-addresses vrf {vrf}
        * show ip dhcp excluded-addresses pool {pool}
    * Added ShowLoggingOnboardSwitch Parser
        * Parser for "show logging onboard switch {switch_num} {feature}"
    * Added ShowLicenseAuthorization Parser
        * Parser for "ShowLicenseAuthorization"
        * Parser for "ShowDiagnosticStatus"
        * Parser for "ShowPlatformHardwareFedSwitchActiveFwdAsicResourceAsicAllCppVbinAll"
    * Added ShowPlatformUsbStatus Parser
        * Parser for "show platform usb status"
    * Added ShowHwModuleUsbflash1Security Parser
        * Parser for "show hw-module usbflash1 security status"
    * Added ShowVmiNeighborsDetail parser
        * Parser for "show vmi neighbors detail"
    * Added ShowPlatformSoftwareFedSwitchActiveAcl
        * show platform software fed switch active acl counters hardware | include Ingress IPv4 Forward
    * Added ShowPlatformSoftwareBpCrimsonStatistics
        * show platform software bp crimson statistics
    * Added parser
        * Added ShowInterfacesCountersErrors
    * Added ShowCableRpd
        * show cable rpd {rpd_mac_or_ip} spectrum-capture-capabilities
    * Added ShowCallHomeStatistics
        * show call-home statistics
    * Added ShowTemplateTemplate
        * show template {template}
    * Added ShowIpv6MldSnoopingMrouter vlan
        * Added parser for "show ipv6 mld snooping mrouter vlan {vlan id}"
    * Added ShowInstallCommitted
        * show install committed
    * Added ShowLoggingOnboardRpActiveUptimeDetail parser
        * show logging onboard Rp active uptime detail
    * Added ShowSdmPreferCustom
        * added new parser for cli 'show sdm prefer custom'
    * Added ShowMonitorCaptureBufferDetailed
        * added new parser for cli 'show monitor capture {capture_name} buffer detailed'
    * Added ShowCableRpdIpv6
        * show cable rpd ipv6
        * show cable rpd {rpd_mac} ipv6
        * show cable rpd {rpd_ip} ipv6
        * show cable rpd {tengig_core_interface} ipv6
        * show cable rpd slot {lc_slot_number}  ipv6
    * Added ShowCefInterface Parser
        * Parser for "show ipv6 mld groups summary"
    * Added ShowControllersPowerInlineModule
        * show controllers power inline module <module_number>
    * Added ShowEigrpAddressFamilyIpv6VrfNeighbors Parser
        * Parser for "show eigrp address-family ipv6 vrf {vrf} {num} neighbors {interface}"
    * Added  ShowInstallInactive
        * show install inactive
    * Added ShowIpOspfNeighbor
        * Added parser support for 'show ip ospf <proccess_id> neighbor'
        * Added parser support for 'show ip ospf <proccess_id> neighbor {interface}'
    * Added ShowPppAll parser
        * Parser for "show ppp all"
    * Added ShowEtherchannelPortChannel
        * Parsre for "show etherchannel <number> port-channel"
    * Added ShowEtherchannelProtocol
        * Parser for "show etherchannel protocol"
    * Added ShowPortSecurityInterfacesAddressVlan
        * show port-security interfaces {interface} address vlan
    * Added ShowMemoryDebugIncrementalLeaks Parser
        * Parser for "show memory debug incremental leaks"
    * Added ShowPlatformSoftwareMonitorSession
        * Added parser for "show platform software monitor session {session}"
    * Added ShowVlanPrivate-Vlan
        * Added parser for "Show Vlan Private-Vlan"
        * Added parser for "Show Vlan Private-Vlan Type"
    * Added ShowIpMfibSummary
        * Added parser for "Show Ip Mfib Summary"

* added showiparpinspectionlog
    * show ip arp inspection log

* iosxr
    * Added ShowCdp
        * added new parser for cli 'show cdp'

* rpd
    * Added new os type RPD
    * Added parser
        * Added ShowBcmRegisterWbfftConfig

* added showpowerinlinemodule
    * Parser for "show power inline module {module}"

* added show device classifier profile type custom
    * Added parser for "show device classifier profile type custom"


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpIgmpSnoopingGroups
        * Fixed reg ex pattern match and added a unit test
    * Added
    * Modified ShowIpMroute
        * Modified p5 to support ipv6 address too
    * Modified ShowCdpNeighbors
        * Added total_entries parameter.
    * Modified ShowPlatformSoftwareFactoryResetSecureLog
        * Added Optional parameter status to schema
    * Modified ShowChassis where redun_port_type is made optional key.
    * Modified ShowEtherchannelPortChannel
        * Changed one of the pattern to match port_channel properly
        * Made 'gc' key as optional
    * Modified ShowEtherChannelDetail
        * Made 'last_port_bundled' and 'last_port_unbundled' keys as optional
    * Modified ShowL2vpnEvpnEthernetSegmentDetail
        * Handle case where RD is shown as "Not set"
    * Modified ShowCryptoIkev2Stats Added Quantum resistance line to parser.
    * Modified ShowBgpSuperParser
        * Modified regexp to consider statuscode with astrick followed by m so that it will take other routes and rds
    * Modified ShowIpRoute
        * Updated source_protocol_dict to support nat dia routes with type "n" and "Nd"
    * Modified ShowCryptoIkev2SaDetail Added Quantum resistance line of code to parser.
    * Modified ShowIsisRib
        * updated regex to accept alphanumberic as isis level
    * Modified ShowL2fibBridgedomainAddressUnicast
        * Support Adjacency and PD_Adjacency with multiple PL (have trailing " ...")
    * Modified ShowPlatformResources
        * Added control Processor and rp/esp as optional
    * Modified ShowPlatformSoftwareCpmSwitchB0ControlInfo
        * Added regular expression p1_2 to accomodate the change in the ouput.
    * Modified ShowLoggingOnboardSwitchActiveStatus
        * modified code to match code for not having switch_num
    * Modified ShowLoggingOnboardSwitchActiveUptimeDetail
        * modified code to match code for not having switch_num
    * Modified ShowSpanningTreeInterfaceDetail
        * Fix the parser issue. Add additional key.
    * Modified ShowPlatformResources
        * updated to print full interface name instead of short form
    * Modified ShowPlatformSoftwareMonitorSession
        * Fixing optional keys and value format
    * Modified ShowArchive
        * Added total_entries parameter.
    * Modified ShowVrrpBrief
        * Parser for show vrrp brief
    * Added
        * show template
        * show service-template
        * show redundancy config-sync failures mcl
    * Modified ShowBgpDetailSuperParser
        * Fixed regex pattern p6_3 to accommodate 3 update-groups.
        * Added new golden output txt and expected.py with 3 update-groups.
        * Fixed golden output 4 with the right route info and update-groups.
        * Added update groups item to ShowIpBgpAllDetail and ShowIpBgpDetail expected outputs.
    * Modified ShowCallHomeMailServerStatus
        * Included exception in Show call-home mail-server status
    * Modified ShowWirelessClientMacDetail
        * added inital support for fabric-enabled clients
    * 9600
        * Modified ShowPlatformSwitchStandbyTcamUtilization
            * Modified switch to a dynamic variable to avoid conflicts
    * Modified ShowIdpromInterface.
    * Added the parser in the proper file show_idprom.py.
    * Modified ShowLicenseTechSupport as per the output change in latest polaris version.
    * Added the keys device_telemetry_report_summary, data_channel, reports_on_disk in schema.
    * Added  the regular  expression p14.
    * Implemented a nonbackwards compatible change in order to fix the ShowIsisDatabase parser
        * Fixed ShowIsisDatabase parser to handle multiple interfaces under a single device
        * Modified the Schema to store interfaces in a list instead of a dict ('is_dict' --> 'is_list')
        * Updated all ShowISISDatabaseVerbose, ShowIsisDatabaseDetail, and ShowIsisDatabase tests to verify output with multiple interfaces under a single device

* show romvar switch <switch_number>

* deleted the duplicate parser under iosxe/show_platform.py and iosxe/c9300/show_platform.py.


--------------------------------------------------------------------------------
                                     Update                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowInterfacesSwitchport parser
        * Corrected the ethertype section


