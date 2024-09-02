--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareFedSwitchActiveIpRouteDetail
        * Added Show Platform Software Fed Switch Active IpRoute Detail
    * Added ShowPlatformSoftwareFedActiveMatmMacTableVlanMacDetail
        * Added 'show platform software fed {switch} {mode} matm macTable vlan {vlan_id} mac {dynamic_mac} detail'
    * Added ShowNetworkClocksSynchronizationDetail
        * Added schema and parser for show network-clocks synchronization detail
    * Added ShowNetworkClocksSynchronization
        * Added schema and parser for show network-clocks synchronization
    * Added ShowNetworkClocksSynchronizationGlobalDetail
        * Added schema and parser for show network-clocks synchronization global detail
    * Added ShowNetworkClocksSynchronizationGlobal
        * Added schema and parser for show network-clocks synchronization global
    * Added ShowNetworkClocksSynchronizationInterface
        * Added schema and parser for show network-clocks synchronization interface {interface}
    * Added ShowNetworkClocksSynchronizationT0Detail
        * Added schema and parser for show network-clocks synchronization t0 detail
    * Added ShowNetworkClocksSynchronizationT0
        * Added schema and parser for show network-clocks synchronization t0
    * Added ShowESMCDetail
        * Added schema and parser for show esmc detail
    * Added ShowESMC
        * Added schema and parser for show esmc
    * Added ShowESMCInterfaceDetail
        * Added schema and parser for show esmc interface {interface} detail
    * Added ShowESMCInterface
        * Added schema and parser for show esmc interface {interface}
    * Added ShowHardwareLed
        * Added schema and parser for 'show hardware led' under c9600
    * Added HardwareModuleBeaconFanTrayStatus
        * Added schema and parser for 'hw-module beacon fan-tray status'
    * Added HardwareModuleBeaconSlotStatus
        * Added schema and parser for 'hw-module beacon slot {slot_num} status'
    * Added ShowPlatformSoftwareFedSwitchActivePuntPacketcaptureStatus
        * Added schema and parser for 'show platform software fed switch active punt packet-capture status'
    * Added ShowPlatformSoftwareFedIgmpSnoopingGroupsCount
        * Added 'show Platform Software fed ip igmp snooping groups count' command and schema for the command.
    * Added ShowPlatformSoftwareFedIpMfibCount
        * Added 'show platform software fed switch active ip mfib count' command and schema for the command.
    * Added ShowPlatformSoftwareFedIpMfibSummary
        * Added 'show platform software fed switch active ip mfib summary' command and schema for the command.
    * Added ShowIpIgmpSnoopingGroupsVlanGroup
        * Added 'show ip igmp snooping groups vlan {vlan} {group}' command and schema for the command.
    * Added ShowPlatformSoftwareFedSwitchActiveIpAdj
        * Added schema and parser for 'show platform software fed switch active ip adj'
    * Added ShowPlatformSoftwareFedSwitchActiveIpRoute
        * Added schema and parser for 'show platform software fed switch active ip route'
    * Added ShowPlatformSoftwareMountSwitchActiveRpTmpfs
        * Added schema and parser for 'show platform software mount switch active rp active | include {tmpfs}'
    * Added ShownMonitorEventTraceDmvpnAll
        * Added schema and parser for show monitor event-trace dmvpn all
    * cat9k
        * c9500
            * show_platform_software_fed_switch_active_punt_packet_capture_display_filter_key_brief.py
                * ShowPlatformSoftwareFedSwitchActivePuntPacketCaptureDisplayFilterKeyBrief


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowL2vpnEvpnMacIpDetail
        * Added '(' ')' characters to regrex for next-hop
    * Modified ShowL2vpnEvpnEviDetail
        * parser for 'show l2vpn evpn evi {evi} detail'
    * Modified ShowMonitorCaptureBufferDetailed
        * Added revised version 1 for ShowMonitorCaptureBufferDetailed parser
        * Added <p9>, <p10>, <p11>, <p12> and <p13> to accommodate various outputs
    * Modified ShowIsisNodeLocators
        * added support for new cli show isis node locators
    * Modified ShowIsisNodeLocatorsSchema
        * added schema for new cli show isis node locators
    * Modified fix for ShowInterfaces
        * Modified the Regex pattern p<11> to accomodate various outputs
    * Modified fix for ShowMplsTrafficEngTunnelTunnelid
        * Added the frr_outlabel key to the schema and modified the regex patterns p<1> and p<3> to accommodate various outputs
    * Modified ShowLicenseAll Parser
        * Made miscellaneous, policy, and usage_reporting optional
        * Made smart_licensing_status non-optional as some of its members are not optional
    * Modified ShowLicenseStatus Parser
        * removed matching for <none> in parsing trust_code_installed as it is not specific enough
    * Modified ShowLldpNeighborsInterfaceDetail Parser
        * Made media_attachment_unit_type optional
    * Modified ShowPlatformSoftwareFedSwitchActivEAclUsage Parser
        * Added switch_num variable to the show command
    * Modified ShowPlatformSoftwareFedSwitchActiveStpVlan
        * Added switch variable to the command
    * Added ShowIpDhcpSnoopingBinding
        * Make {interfaces} key as Optional to handle the key error
    * Modified init file in c9350
        * Updated model token
    * cat9k
        * 9300
            * Modified ShowPlatformHardwareAuthenticationStatus
                * Added support for RoT
            * Modified ShowEnvironmentAll
                * Modified to support more than 2 PSs in a switch
    * Modified ShowLispInstanceIdService
        * Fixed incorrect regex for Publisher(s)
    * Modified ShowLispInstanceIdService
        * Added support for parsing publisher addresses without ETR Map-Servers
    * Modified ShowMkaStatistics
        * Changed tx-sc-creation key in schema from `0` to `int`.
    * Modified ShowLoggingOnboardRpClilog parser
        * Modified ShowLoggingOnboardRpClilog parser
    * Modified ShowLoggingOnboardRpActiveStatus parser
        * Modified ShowLoggingOnboardRpActiveStatus parser
    * Modified ShowLoggingOnboardRpActiveTemperatureContinuous parser
        * Modified ShowLoggingOnboardRpActiveTemperatureContinuous parser
    * Modified ShowLoggingOnboardRpActiveTemperature parser
        * Modified ShowLoggingOnboardRpActiveTemperature parser
    * Modified ShowIsisIpv6Rib
        * added support for new cli show isis ipv6 rib flex-algo {flex_id} {prefix}
        * added new key flex_algo under tag key
        * added new key src_rtr_id under prefix key
        * added new key pfx_algo under prefix key
    * Modified ShowIsisIpv6RibSchema
        * added new optional keys flex_algo,src_rtr_id,pfx_algo
    * Modified ShowLispSiteSummarySchema
        * made configured_registered_prefixes.ipv6 optional
    * Modified ShowLispPlatformSchema
        * made make remote_eid_idle and mapping_cache_full optional optional
    * MOdified ShowHardwareLedPortMode parser
        * Modified current_mode & status parameters in schema as Optional
    * Modified ShowWatchdogMemoryState parser
        * Adjusted to missing spaces in CLI output
        * Do not fail parser if there is no node location appearing in output
    * Modified ShowVrf
        * updated schema to support additional `route_distinguisher_auto`
    * Modified cat9k/c9800/ewc_ap
        * Changed parameter pid to submodel in __init__.py file.
    * Modified cat9k/c9600/c9606r
        * Changed parameter pid to submodel in __init__.py file.

* iosxr
    * Modified ShowPceIPV4PeerDetail
        * Modified schema and adding optional to the keys
    * Modified ShowRouteIpv6
        * Modified parer and defined outgoing dict
    * Modified ShowOspfVrfAllInclusive
        * Added <current_lsa>, <threshold>, <ignore_time>, <reset_time>, <allowed_ignore_count>, <current_ignore_count>, <max_external_prefix>, <warning_threshold> keys to schema.
    * Modified ShowPlatform
        * Updated regex pattern p1 to allow for both IN-RESET and SW_INACTIVE as valid states.

* staros
    * Modified init file
        * Updated os token

* sonic
    * Modified init file
        * Updated os token

* rdp
    * Modified init file
        * Updated os token

* various
    * Split large parser files (>10000 lines) into smaller files


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformHardwareModuleInterfaceStatus
        * Added support for command "show platform hardware subslot {id} module interface {intf} status"


