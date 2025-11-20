--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added hw-module beacon slot {slot_num} port {port_num} status
        * hw-module beacon slot {slot_num} port {port_num} status
    * Added show firmware version fantray
        * show firmware version fantray
    * Added show logging onboard slot {slot_num} voltage
        * show logging onboard slot {slot_num} voltage
    * Added show logging onboard slot {slot_num} termperature
        * show logging onboard slot {slot_num} temperature
    * Added show platform hardware chassis fantray detail
        * show platform hardware chassis fantray detail
    * Added ShowPlatformHardwareQfpActiveFeatureFirewallUcodeZonepair
        * Added schema and parser for 'show platform hardware qfp active feature firewall ucode zonepair {zone1} {zone2}' command.
    * Added ShowEnvAll
        * Added parser for "show env all" for 9610 platform.
    * Added ShowLoggingOnboardRpUptimeDetail
    * Added parser for Show logging onboard rp active uptime detail command
    * Added ShowIpPimRp
        * show ip pim rp
    * Added parser for ShowIpSsh
        * 'show ip ssh'
    * Added ShowPlatformHardwareQfpActiveFeatureAlgStatisticsLoginClear
        * show platform hardware qfp active feature alg statistics login clear
    * Added ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSip
        * show platform hardware qfp active feature alg statistics sip
    * Added parser for ShowPlatformHardwareQfpActiveInfrastructureBqsScheduleOutputDefault
        * 'show platform hardware qfp active infrastructure bqs schedule output default interface {interface}'
    * Added parser ShowSwitch for cat9kv
        * show switch
    * Added ShowPlatformHardwareIomdEthernetControllersPhyHistogram
        * Added parser for 'show platform hardware iomd {iomd} ethernet_controllers phy {phy} histogram'
    * Added ShowPlatformManagementInterface
        * show platform management-interface
    * Added  ShowPlatformSoftwareSubslotModuleFirmware schema and parser
        * Added schema and parser for show platform software subslot {subslot} module firmware
    * Added ShowPlatformHardwareQfpActiveFeatureNatDatapathPool and ShowPlatformHardwareQfpNatDatapathSessDump schema and parser
        * Added schema and parser for show platform hardware qfp active feature nat datapath pool and show platform hardware qfp active feature nat datapath sess-dump
    * Added ShowPlatformHardwareQfpActiveFeatureNatDatapathTime schema and parser
        * Added schema and parser for show platform hardware qfp active feature nat datapath time
    * Added Parser for command
        * show platform hardware qfp active feature firewall zonepair {id}
    * Added ShowCryptoPkiServerCrl
        * show crypto pki server {servername} crl
    * Added ShowPlatformHardwareSubslotModuleInterfaceStatistics
        * show platform hardware subslot {subslot} module interface {interface} statistics
    * Added ShowLoggingOnboardRpActiveUptimeDetail
        * Added schema and parser for 'show logging onboard rp active uptime detail' command.
    * Added ShowPlatformSoftwareStatusControlProcessor
        * Added schema and parser for 'show platform software status control-processor' command.
    * Added Parser for parsers for below commands
        * 'show platform software audit monitor status'
        * 'show platform software audit ruleset'
    * Added Schema and Parser for ShowPlatformSoftwareSubslotModuleStatus
        * 'show platform software subslot <subslot> module status'
    * Fixed Parser for Parser for show crypto pki trustpool
        * Added a new schema and parser for the show crypto pki trustpool command.
    * Added parser ShowPlatformSoftwareBPCrimsonContentOper
        * show platform software bp crimson content oper
    * Added Schema and Parser for ShowPolicyMapMultipoint
        * Added 'show policy-map multipoint'
    * Added parser for ShowPlatformHardwareQfpActiveDatapathUtilization
        * 'show platform hardware qfp active datapath utilization'
    * Added parser for 'show fcs-threshold' command
    * Added parser for ShowClassMapTypeInspect
        * 'show class-map type inspect {name}'
    * Added class ShowCryptoDatapathIpv4SnapshotNonZero parser in show_crypto.py
        * Added schema and parser for cli 'show crypto datapath ipv4 snapshot non-zero'
    * Added ShowCryptoEli parser in show_crypto.py
        * Added schema and parser for cli 'show crypto eli'
    * Added ShowDmvpnIpv6
        * Added schema and parser for cli 'show dmvpn ipv6' and 'show dmvpn ipv6 interface {interface}'.
    * Added ShowHosts parser in show_hosts.py
        * Added schema and parser for cli 'show hosts'
    * Modified ShowInterfaceAccount
        * show interface Te0/1/0 acoount
    * Added ShowIpBgpAllLabel parser in show_ip_bgp.py
        * Added schema and parser for cli 'show ip bgp {address_family} all label'
    * Added ShowIpBgpAllLabel parser in show_ip_bgp.py
        * Added schema and parser for cli 'show ip bgp vpnv4 all label'
    * Modified ShowIpMrmInt
        * sh ip mrm int
    * Added ShowNat64Routes
        * show nat64 routes
    * Added parser for ShowPlatformHardwareQfpActiveFeatureFirewallRuntimeRstSegment
        * 'show platform hardware qfp active feature firewall runtime | sec RST segment'
    * Added ShowPlatformHardwareQfpActiveFeatureEssSession parser in show_platform_hardware.py
        * Added schema and parser for cli 'show platform hardware qfp active feature ess session'
    * Modified ShowPlatformHardwareCppActiveFeatureFirewallSession parser in show_platform_hardware.py
        * Modified schema and parser for cli 'show platform hardware cpp active feature firewall session create 1 10'
    * Modified ShowPlatformHardwareQfpActiveFeatureNat66DatapathStatistics
        * show platform hardware qfp active feature nat66 datapath statistics
    * Added ShowPlatformHardwareSubslotModuleHostIfStatistics parser in show_platform_hardware_subslot.py
        * Added schema and parser for cli 'show platform hardware subslot 0/1 module host-if statistics'
    * Added ShowPlatformHardwareSubslotModuleHostIfStatus
        * show platform hardware subslot <subslot> module host-if status
    * Added ShowPlatformSoftwareFirewallRPActiveParameterMaps
        * show platform software firewall RP active parameter-maps
    * Added ShowPlatformSoftwareObjectManagerFpActiveStatistics
        * show platform software object-manager FP standby statistics
    * Added ShowPlatformSoftwareObjectManagerF0PendingAckUpdate
        * show platform software object-manager FP active pending-ack-update
    * Added parser for ShowPlatformSoftwareAccessListFpActiveSummary
        * 'show platform software access list fp active summary'
    * Added parser for ShowPlatformSoftwareNatFpActiveCppStats
        * 'show platform software nat fp active cpp-stats'
    * Added ShowPlatformSoftwareFedSwitchSwcStatistics
        * show platform software fed switch active swc statistics
    * Added ShowPlatformSoftwareFirewallFPActiveParameterMaps parser in show_platform_software.py
        * Added schema and parser for cli 'show platform software firewall FP active parameter-maps'
    * Modified ShowPlatformSoftwareInfrastructureThreadFastpath
        * show platform software infrastructure thread fastpath.
    * Modified ShowPlatformSoftwareNat66RpActivePrefix-translation
        * show platform software nat66 rp active prefix-translation
    * Added ShowPrivilege parser in show_privilege.py
        * Added schema and parser for cli 'show privilege'
    * Added parser for ShowVoiceDspGroupAll
        * 'show voice dsp group all'
    * Modified ShowVoiceDspA
        * show voice dsp a.

* iosxr
    * Added ShowControllersOpticsPRBSInfo parser.
        * Added parser for cli 'show controllers optics prbs-info'.
    * Added ShowControllersOpticsPRBSCapability parser.
        * Added parser for cli 'show controllers optics prbs-capability-info'.
    * Added Parsers for below lslib show commands
        * show lslib server topology-db protocol ospf nlri-type link detail
        * show lslib cache ospf <process_id> links attributes
    * Modified Parsers for below OSPF show commands
        * Modified parser for 'show ospf vrf all-inclusive database opaque-area'
    * Added parser for "show platform security tam device-info" command

* nxos
    * Added MroutepdL3Show
        * dchal module 1 "mroutepd l3 show"
        * Parser for multicast routing protocol daemon L3 information.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxr
    * Modified existing Parsers for below ospfv3 show commands to accomodate changes in
        * show ospfv3 topology detail
        * show ospfv3 topology prefixes

* iosxe
    * Modified ShowPolicyMapTypeInspectZonePairSession
    * Added support to Terminating Sessions in addition to Established Session
    * Fixed ShowCryptoPkiServer
        * 'show crypto pki server'
    * Modified ShowMplsLdpNeighbor parser
        * Fix the regex p5 to handle different interfaces
        * Added new regex p8_1 and p8_2 to fetch ldp session details
    * changed one parameter datatype for parser command
        * show platform software fed switch <switch> wdavc function wdavc_ft_show_all_flows_seg_ui
    * Modified ShowPolicyMapTypeInspectZonePair
    * Added support to match new output 0 packets,0 bytes that appear before class_map_action
    * Modified parser ShowUdldNeighbor
        * Updated regex pattern p1 to match the interface name
    * Modified parser ShowPlatformSoftwareCpmSwitchB0ControlInfo
        * Updated regex pattern p3 to make 'Preferred Link' field optional
    * Modified ShowIpv6NhrpSummary
        * updated the regex to parser the nhrp entries with singular form.
    * Modified ShowIpv6NhrpSummary
        * updated the regex to parser the nhrp entries with singular form.
    * Modified ShowInstallState parser
        * Updated the ShowInstallState parser to handle empty output when show install active returns no packages.
    * IE3k
        * Added support to parse LED status for EIP-MOD and EIP-NET in 'show hardware led' command output.
    * Modified ShowPlatformSoftwareYangManagementProcessState
        * Reverted changes made by removing a command from cli_command list.
    * Modified ShowInterfacesTransceiverSupportedlist
        * updated regex pattern p1, p2, and p3 for various output formats.
    * Modified ShowPlatform
        * updated regex pattern p6 for Fatray failures
    * Modified ShowPlatformSoftwareYangManagementProcessState
        * updated regex pattern <p1> for various output formats.
    * Modified ShowCryptoIkev2SaDetail
        * Added keys ake into the schema.
    * Modified ShowDeviceTrackingDatabase
        * 'show device tracking database' - Added support for timeleft in the output parsing.
    * Modified ShowCtsRoleBasedSgtMapAll
        * 'show cts role-based sgt-map all' - Added support for CLI-HI SGT bindings.
    * Modified ShowCtsServerList
        * 'show cts server list' - Added support for parsing server entries without asterisk (*) prefix.
    * Modified ShowIpv6AccessLists
        * 'show ipv6 access-list {acl}'
    * Modified ShowControllerT1
        * 'show controller Serial1/0/0'
    * Modified ShowDiagSubslotEepromDetail
        * 'show diag subslot {subslot} eeprom detail'
    * Modified ShowDmvpn
        * updated the regex to parser ipv6 fields correctly.
    * Modified ShowDmvpnCountStatus
        * fixed the CLI commands with correct format.
    * Modified ShowProcessesCpu
        * 'show processes cpu'
    * Modified ShowTimeRange
        * 'show time-range <name>'
    * Modified ShowPlatformPacketTracePacket
        * 'show platform packet-trace packet {packet_id}'
    * Modified ShowPlatformHardwareQfpActiveFeatureFirewallMemory
        * 'show platform hardware qfp {rpname} feature firewall memory'
    * Modified ShowPlatformHardwareQfpActiveFeatureTdDatapathStatistics
        * 'show platform hardware qfp active feature td datapath statistics'

* genieparser
    * Removed all usage of deprecated pkg_resources module in favor of importlib.metadata where possible.


--------------------------------------------------------------------------------
                                     Added                                      
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPost in iosxe/Cat9k/c9610
        * Added parser for show post


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIdprom
        * show idprom all
    * Updated ShowLispIpv4Publisher parser in show_lisp.py
        * Added support for additional character in 'type' field.


--------------------------------------------------------------------------------
                                    Removed                                     
--------------------------------------------------------------------------------

* iosxe
    * Removed ShowPlatformHardwareQfpActiveFeatureFirewallDatapathScbAnyAnyAnyAnyAnyAllAnyDetail
        * 'show platform hardware qfp active feature firewall datapath scb any any any any any all any detail'


