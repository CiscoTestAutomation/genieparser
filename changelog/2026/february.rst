--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe/cat9k
    * Add ShowPlatformSoftwareFedSwitchActiveMatmMactable parser
        * Added schema and parser for show platform software fed switch active matm macTable command for C9610, C9350 and C9550 devices.

* iosxe
    * Modified ShowAccessList parser
        * Added regex patterns to match the fqdn output format for the command 'show access-lists' on IOS-XE devices.
    * Modified ShowPlatformHardwareFedSwitchActiveSgaclResourceUsage parser
        * Added regex patterns to match the new output format for the command 'show platform hardware fed switch active sgacl resource usage' on IOS-XE devices.
    * Modified ShowCryptoPkiTrustpointsSchema
        * "serial_number_in_hex" is now optional
    * Modified ShowCtsSxpSgtMap
        * 'show cts sxp sgt-map vrf <vrf>' cli included.
    * Modified ShowNtpConfig
        * Modified regex pattern to support ntp servers configured with keys
        * Changed schema to include "key_id"
    * Modified class ShowInterfacesAccounting
        * Modified regex pattern to support interface descriptions with multiple spaces
        * Only right-strip whitespace from lines and modify regex for lines containing counters to add explicit leading whitespace
    * Modified ShowIpNatTranslations
        * 'show ip nat translations verbose'
    * Modified ShowPlatformSoftwareFirewallFPActiveParameterMaps
        * 'show platform software firewall FP active parameter-maps'
    * Modified ShowDiagSubslotEepromDetailSchema
        * Change 'clei_code' as optional key.
    * Modified ShowPlatformPacketSumm parser
        * Parser now correctly handles packet states and reasons.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowHsrRingDetail
        * Added schema and parser for 'show hsr ring detail' command.
    * Added ShowHsrRingAllowedVlan
        * Added schema and parser for 'show hsr ring allowed-vlan' command.
    * Added ShowHsrRingMulticastFilter
        * Added schema and parser for 'show hsr ring multicast-filter' command.
    * Added ShowHsrRingMulticastFilterDrop
        * Added schema and parser for 'show hsr ring multicast-filter-drop' command.
    * Added ShowHsrRingVlanFilterDropCount
        * Added schema and parser for 'show hsr ring vlan-filter-drop-count' command.
    * Added ShowPlatformFpgaProfileActive
        * Added schema and parser for 'show platform fpga-profile active' command.
    * Added ShowFQDNSummary
        * Added schema and parser for 'show fqdn summary' command.
    * Added ShowFQDNDatabaseStatistics
        * Added schema and parser for 'show fqdn database statistics' command.
    * Added ShowPlatformSoftwareFedSecurityStormControlIfId
        * Added schema and parser for 'show platform software fed security storm-control if-id' command.
    * Added ShowPlatformSoftwareFedSwitchIfmInterfaceName
        * Added schema and parser for 'show platform software fed switch ifm interface name' command.
    * Added ShowPlatformSoftwareFedSwitchIfmInterfaceNameVlan
        * Added schema and parser for 'show platform software fed switch ifm interface name vlan' command.
    * Modified ShowRunInterface
        * Updated schema and parser for 'show run interface' command to include storm-control configuration.
    * Added ShowPlatformSoftwareFedSwitchActiveSgaclVlanMapping
        * Added schema and parser for 'show platform hardware fed {switch_type} sgacl vlan-mapping {vlan}' command.
    * Added ShowPlatformHardwareFedSwitchActiveSgaclTableVlanMapping
        * Added schema and parser for 'show platform hardware fed {switch_type} sgacl table vlan-mapping {vlan}' command.
    * Added ShowAdjacencyTunnelTunnelInternal
        * Added schema and parser for 'show adjacency tunnel {tunnel} internal'
    * Added ShowIpAccessListInbound
        * Added schema and parser for 'show ip access-list inbound'
    * Added ShowIpAccessListOutbound
        * Added schema and parser for 'show ip access-list outbound'
    * Added ShowIpMribRouteSummary
        * Added schema and parser for 'show ip mrib route summary'
    * Added ShowIpRsvpSenderDetailFilterDstPort30
        * Added schema and parser for 'show ip rsvp sender detail filter dst-port 30'
    * Added ShowPlatformHardwareQfpActiveFeatureTunnelInterfaceTunnel
        * Added schema and parser for 'show platform hardware qfp active feature tunnel interface {tunnel}'
    * Added ShowPolicyMapTypeAccessControlInterfaceInterfaceIn
        * Added schema and parser for 'show policy-map type access-control interface {interface} in'
    * Added show ip rib vrf {vrf} database detail
        * Parse "show ip rib vrf {vrf} database detail"
    * Added show platform software fed active acl policy parser
        * Parse "show platform software fed active acl policy"


--------------------------------------------------------------------------------
                                     Fixed                                      
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowMonitorCaptureBufferDetailed
        * Added Optional fields in schema for 'show monitor capture buffer {capture_buffer} detailed' command.


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe/rv1
    * Added support for show stackwise-virtual link parser with full name mapping.
    * c9500x
        * Added support for show stackwise-virtual link parser.


