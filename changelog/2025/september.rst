--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added parser for ShowMonitorEventTraceCryptoIpsecEventAll
        * 'show monitor event-trace crypto ipsec event all'
    * Added ShowPlatformHardwareQfpActiveFeatureIpsecSa3
        * Added schema and parser for 'show platform hardware qfp active feature ipsec sa 3'
    * Added  ShowIdpromFantrayEepromDetail schema and parser
        * Added schema and parser for show idprom fan-tray {fantray_num} eeprom detail
    * Added ShowPlatformHardwareQfpActiveFeatureFirewallDrop
        * show platform hardware qfp active feature firewall drop
        * show platform hardware qfp active feature firewall drop all
        * show platform hardware qfp active feature firewall drop clear
        * show platform hardware qfp active feature firewall drop verbose
    * Added ShowL2tp
        * show l2tp
    * Added ShowPlatformHardwareQfpActiveFeatureNatDatapathGate parser.
        * Added parser for cli 'show platform hardware qfp active feature nat datapath gatein'.
        * Added parser for cli 'show platform hardware qfp active feature nat datapath gateout'.
    * Modified ShowInterfacesTransceiverSupportedlist
        * Added new Cisco p/n min format parser for show interfaces transceiver supported list
    * Added ShowMonitorEventTraceCryptoAllDetail Parser for
        * Parser for 'show monitor event-trace crypto all detail'
    * Added ShowMonitorEventTraceCryptoFromBoot Parser for
        * Parser for 'show monitor event-trace crypto from-boot'
        * Parser for 'show monitor event-trace crypto from-boot {timer}'
    * Added Parser for show platform hardware cpp active system state
        * Added a new schema and parser for the show platform hardware cpp active system state command.
        * Supports parsing CPP system state information including component status, platform state, HA state, client state, image information, load count, active threads, and fault manager flags.
        * Handles component initialization status (cpp_cp, cpp_sp, FMAN-FP, cpp_driver0).
        * Parses hierarchical state information with proper data type conversion.
    * Added ShowVlans
    * 'show vlans <vlan-id>'
    * Added  ShowPlatformHardwareQfpActiveFeatureNatDatapathEsp schema and parser
        * Added schema and parser for show platform hardware qfp active feature nat datapath esp
    * Added ShowPlatformHardwareChassisRpFanSpeedControlData
    * Added parser for Show Platform Hardware Chassis Rp FanSpeedControlData
    * Added parser for hw-module beacon fan-tray fantray_num status
    * Added ShowX25Vc parser in show_x25.py
        * Added schema and parser for cli 'show x25 vc'
    * Added ShowPlatformSoftwareNatFpActiveMappingStatic
        * Added ShowPlatformSoftwareNatFpActiveMappingStaticSchema
        * Added parser for "show platform software nat fp active mapping static"
    * Added ShowCefTableConsistencyCheck parser in show_cef.py
        * Added schema and parser for cli 'show cef table consistency-check'
    * Added parser for ShowAlignment
        * 'show alignment'
    * Added ShowMkaSessionDetail
        * show mka session detail
            * *New**
    * Added** ShowCtsCredentials *parser.**
        * Added parser for cli 'show cts credentials'.**
    * Added ShowRunningConfigVrf
        * show running-config vrf
    * Added ShowPlatformHardwareQfpActiveFeatureFirewallRuntime
        * show platform hardware qfp active feature firewall runtime
    * Added ShowPlatformSoftwareFirewallRPActiveZones
        * sh ipv6 mfib {group} active
    * Modified ShowVoiceDsp
        * show voice dsp
    * Added ShowPlatformHardwareQfpActiveFeatureTdDatapathStatistics parser
        * Added schema and parser for 'show platform hardware qfp active feature td datapath statistics'
    * Added ShowPlatformHardwareQfpActiveFeatureEvcClientL2cpActionsInterface
    * 'show platform hardware qfp active feature evc client l2cp-actions interface GigabitEthernet0/0/4.EFP1'
    * Added ShowRomMonitor parser in show_romvar.py
        * Added schema and parser for cli 'show rom-monitor 0'
    * Added ShowIpBgpNeighborReceivedPrefixFilter schema and parser
        * Added schema and parser for show ip bgp neighbors {neighbor} received prefix-filter and show ip bgp {address_family} vrf {vrf} neighbors {neighbor} received prefix-filter
    * Added ShowPlatformHardwareChassisFantrayDetailAll
        * Added parser for "show platform hardware chassis fantray detail all"
    * Added ShowPowerDetail
        * Added schema and parser for'show power detail' under 9610c folder for iosxe

* iosxr
    * Added `ShowSubscriberSessionAllSummary` Parser
        * Added schema and parser for `show subscriber session all summary` command.
    * Added Parsers for below OSPFv3 show commands
        * show ospfv3 vrf all-inclusive database ext-router
        * show ospfv3 topology detail
        * show ospfv3 topology prefixes
    * Added Parsers for below lslib_server show commands
        * show lslib server producer detail
        * show lslib server producer {name} instance-id {id}
        * show lslib server topology-db protocol ospfv3 instance-id {id} nlri-type node detail
        * show lslib server topology-db protocol ospfv3 instance-id {id} nlri-type link detail
        * show lslib server topology-db protocol ospfv3 instance-id {id} nlri-type ipv6-prefix detail

* nxos
    * Added ShowKeyChain parser.
        * Added parser for cli show key chain {key_chain_name}.
        * Added parser for cli show key chain {key_chain_name} detail.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Added fix for ShowPlatformHardwareFedSwitchFwdAsicInsightAclTableDef parser.
        * Added this fix to support multiple acl_entries.
    * Modified ShowInterfaceEtherchannel
        * 'show interface {interface_id} etherchannel'
    * Modified ShowInterfaces
    * 'show interfaces Serial0/3/1'
    * genie.libs.parser.iosxe.rv1.show_platform
        * Added regex to parse platform output when model, hw_ver and sw_ver are N/A
    * Modified ShowPolicyMapTypeInspectZonePairSessions
        * 'show policy-map type inspect zone-pair sessions'
    * Modified ShowPlatformPacketTracePacket
        * 'show platform packet-trace packet {packet_id}'
    * Added YANG parser for ShowSystemIntegrityAllCompliance
    * Modified ShowPlatformHardwareAuthenticationStatus
        * Added missing optional attributes to schema for 10-slot chassis.
    * Modified ShowStandbyAll parser
        * Updated regex for the state changes line and improved parsing of the last state change time to accommodate various output formats.

* iosxr
    * Modified ShowPlatform for `ASR-9903` with `IOS-XR v7.8.2`
        * Updated regex pattern <p1> to accommodate various outputs
            * Changed whitespace before <plim> to use \s+ (was a single space) for variable spacing.
            * Made <config_state> optional by wrapping it in a non-capturing group.
        * Ensures lines without a "Config state" column are parsed (e.g., `0/0/1             A9903-20HG-PEC             OK`).

* nxos
    * Fixed ShowEnvironmentPowerDetail parser.
        * Fixed parser for cli show environment power detail.


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified show environment power cache parser in iosxe/ie3k
        * Modified parser for show environment power in iosxe/ie3k
    * Updated ShowUACUplinkDB parser
        * Added support for "IPV4 Preferred Uplink" and "IPV6 Preferred Uplink".
        * Added support for optional "Allowed" field in interface tables.
        * Improved parsing logic for various output formats.
    * Modified ShowIpRouteWord parser
        * Fixed p5 where the parser was not correctly handling routes with specific keywords such as "directly connected" and "via".
        * Fixed p8 where the parser was not correctly capturing the metric and next-hop information for certain route types.
    * Modified ShowIpPolicy parser
        * Added support for IPv6 policy parsing in addition to existing IPv4 policy parsing.

* fix resolve syntaxwarnings from invalid escape sequences
    * Updated regex patterns to use raw strings (r"...") or escaped backslashes
    * Eliminated SyntaxWarnings (e.g., '\d', '\S') during runtime


--------------------------------------------------------------------------------
                                     Modify                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowEnvironmentAlarmContact in iosxe/ie3k
        * Modified parser for "show environment alarm-contact" in iosxe/ie3k


