--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareAdjFpActive
        * Added parser for 'show platform software adj fp active'
    * Added ShowPlatformHardwareQfpActiveDatapathInfrastructureSwPkt
        * show platform hardware qfp active datapath infrastructure sw-pktmem
    * Added ShowPlatformSoftwareFedSwitchActiveSgaclBdMapping
        * Added schema and parser for 'show platform hardware fed {switch_type} sgacl bd-mapping {vlan}' command.
    * Added ShowInterfacesTunnelCountersProtocolStatus
        * Added schema and parser for 'show interfaces {tunnel} counters protocol status'
    * Added ShowIpDhcpSipSessionDetail
        * Added schema and parser for 'show ip dhcp sip session detail'
    * Added ShowIpv6InterfaceBrief
        * Added schema and parser for 'show ipv6 interface brief'
    * Added ShowIpv6MrouteVrfVrfSummary
        * Added schema and parser for 'show ipv6 mroute vrf {vrf} summary'
    * Added ShowPlatformHardwareQfpActiveFeatureNat64DatapathStatistics
        * Added schema and parser for 'show platform hardware qfp active feature nat64 datapath statistics'
    * Added ShowPlatformHardwareSubslotModuleDeviceDebugMacfltShowRange and ShowStandbyCapability
        * Added schema and parser for 'show platform hardware subslot {subslot} module device "debug macflt show_range {start_index} {end_index}"'
        * Added schema and parser for 'show standby capability'
    * Added ShowPolicyMapInterface
        * Added schema and parser for 'show policy-map interface'
    * Added ShowPolicyMapTypeAccessControlAccessControl
        * Added schema and parser for 'show policy-map type access-control {access-control}'
    * Added ShowPolicyMapTypeAccessControlInterfaceInterfaceInput
        * Added schema and parser for 'show policy-map type access-control interface {interface} input'
    * Added ShowPolicyMapTypeAccessControlInterfaceInterfaceOutput
        * Added schema and parser for 'show policy-map type access-control interface {interface} output'
    * Added show interface {interface} platform
        * Parse "show interface {interface} platform"
    * Added parser for 'show facility-alarm relay major' command.
    * Added ShowPlatformHardwareQfpActiveInterfaceAllStatisticsDropSummarySubinterfaceClear
        * 'show platform hardware qfp active interface all statistics drop_summary subinterface clear_drop'
    * Added ShowXconnectInterface
    * 'show xconnect interface Gig0/0/7'
    * Added ShowInterfacesMacAccounting
        * Added schema and parser for 'show interfaces {interface} mac-accounting'
        * Added schema and parser for 'show interfaces mac-accounting'


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowRunInterface
        * Updated schema and parser of show running interface for datalink and ipv6 flow
    * Added fix for ShowRunInterface parser.
        * Added this fix to support multiple all_entries.
    * Modified ShowVlanMapping parser
        * Updated p3 regex pattren to also support vlan ranges
    * Modified ShowPlatformSoftwareFedMatm parser
        * Updated p regex pattern to support keys with spaces in them.
    * Modified ShowMonitorCaptureBuffer parser
        * Modified regex patterns to match the new output format for the command 'show monitor capture buffer' on IOS-XE devices.
    * Modified ShowPlatformSoftwareFedActiveMatmMacTableVlanMacDetail parser
        * Added regex pattern to match output
    * IE3K
        * ShowHardwareLed
            * Fix show hardware led parser for IE9K platform.
    * Modified ShowRunInterface
        * Added schema and parser to support parsing of ip address dhcp client-id <client_id>
    * Modified ShowIpv6RouteDistributor
        * Updated p6 regex pattern to match  via 100.0.0.2, NVI0
    * Modified ShowAppHostingDetailAppid
        * 'show app-hosting detail appid {appid}'
    * Modified ShowIox
        * 'show iox'
    * Modified ShowPlatformHardwareQfpActiveFeatureIpsecSa3 parser
        * Fixed CLI command to support dynamic SA handle
        * Updated cli_command to 'show platform hardware qfp active feature ipsec sa {sa_id}'
    * Modified ShowPlatformHardwareQfpActiveFeatureIpsecSa parser
        * Renamed schema class to ShowPlatformHardwareQfpActiveFeatureIpsecSaSchema
        * Made 'mtu' and 'mtu_adj' optional in schema
        * Updated regex to support 'mtu' and 'mtu_adj' output format
    * Modified ShowMplsL2TransportDetail parser
        * Parser enable multiple parsing without reporting errors.

* iosxr
    * Modified ShowRedundancy
        * Changed time_since_last_reload from schema to Optional.
        * Updated regex pattern p6 to handle missing time since last reload duration when reload timestamp is in the future.


