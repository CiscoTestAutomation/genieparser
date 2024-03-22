--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareFedActiveAclInfoDbDetail
        * Added schema and parser for show platform software fed switch active acl info db detail
    * Added ShowPlatformSoftwareIlppowerPortSchema
        * Added parser for show platform software ilpower port {interface}
    * Added ShowPtpTimeProperty
        * parser for 'show ptp time-property'
    * Added ShowPlatformHardwareFpgaSwitch
        * Parser for show platform hardware fpga switch {switch_num}
    * Added ShowPlatformSoftwareWiredClientFpActive
        * show platform software wired-client {process} active
    * Added ShowEtherchannelSwportAuto
        * show etherchannel swport auto
    * show etherchannel swport <port_channel> auto
    * New Parser for TestVdslRawcli
        * Parser for 'test vdsl rawcli "basic show summary {number}"'
    * Added ShowNveVniDetail
        * added parser for "show nve vni <vni_id> detail"
    * Added ShowMacAddresstableDynamicVlanCount
        * Added schema and parser for ShowMacAddresstableDynamicVlanCount
    * Added show ap image
        * Added new parser for show ap image under iosxe
    * Added ShowPlatformSoftwareFedSwitchActiveAclOgPcl Parser
        * parser for show platform software fed switch active acl og-pcl

* staros
    * Added ShowVersion
        * show version

* added showetherchannelswloadbalance
    * show etherchannel swport load-balancing

* iosxr
    * Added ShowMplsLdpInterfaceBrief
        * show mpls ldp interface brief


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Modified show_interface
        * Modify 'mode' as optional in p11 regex.
    * Fix for ShowBgpVrfAllNeighborsReceivedRoutes parser
        * Updated regex p3_2 for new output format.
    * Fix for ShowBgpVrfAllNeighborsRoutes parser
        * Updated regex p3_2 for new output format.
    * Modified ShowHardwareInternalTctrlUsdDpllState
        * parser for 'show hardware internal tctrl_usd dpll state'

* iosxe
    * Fixed error with TestVdslRawCli unittests
    * Modified ShowLispSiteSuperParser
        * Added additional field port to schema
        * Added split function to get port and ip on matching lines<p2> <p3_1> <p3_2>
        * Modified test files for the parsers which uses ShowLispSiteSuperParser
    * Modified ShowLoggingOnboardRpActiveTemperatureContinuous
        * Added show logging onboard rp {rp_standby} {include} continuous to support standby
    * Modified ShowLoggingOnboardRpActiveUptime
        * Added show logging onboard rp {rp_standby} uptime to support standby
    * Modified ShowLoggingOnboardRpActiveStatus
    * Modified ShowCableTdrInterface
        * Modified parser for "show cable tdr interface {inetrface}"
    * Modified ShowIsisDatabaseVerbose
        * Added support for parsing segment routing features in any order
    * Modified ShowPlatformHardwareRegisterReadAsic
        * Fixed the issue in command by changing 'register-name' to 'register'
    * Updated ShowVrf
        * Ordered elements for comparison failure
    * Updated ShowBgpAllSummary
        * Added `input_queue` and `output_queue` to exclude as dynamic value
    * Modified ShowBeaconall parser as per the output change.
        * Added power_supply_beacon_status and fantray_beacon_status in schema and in parser.
    * Modified ShowMacAddressTable Parser
        * typecast 'preferred_lifetime' and 'valid_lifetime' key int or str.
        * Made 'expires' key as optional.
        * Modified p8 regex.
    * Fix for ShowLispIpv4Publicatioin parser
        * Updated regex for new output format without locators
    * Fix for ShowLispIpv6Publicatioin parser
        * Updated regex for new output format without locators
    * Fix for ShowLispEthernetPublicatioin parser
        * Updated regex for new output format without locators
    * Modified ShowMacAddressTable Parser
        * parser for 'show mac address-table interface {interface} vlan {vlan}'
    * Added ShowEnvironmentAll
        * Made power_supply, state and system_temperature_state key optional in schema.
    * Modified ShowDerivedConfigInterfaceSchema
        * Added fields vrf, ipv4_unnumbered_intf, ipv6_unnumbered_intf, autostate into the schema.
    * Modified ShowDerivedConfigInterface
        * Added regexps for vrf, ipv4_unnumbered_intf, ipv6_unnumbered_intf, autostate.
    * Fix for ShowNveInterfaceDetail parser
        * Split tunnel interfaces line in two fields if needed
    * Fix for ShowNvePeers parser
        * Peer state regex does not include all possible state values
    * Modified ShowDeviceTrackingDatabaseInterface Parser
        * Fixed made "network_layer_address" optional in schema
    * Added ShowFileDescriptorsDetail
        * Added schema and parser for ShowFileDescriptorsDetail
    * Added ShowPlatformSoftwareFedActiveAclBindDbDetail
        * Added schema and parser for show platform software fed active acl bind db detail
    * Added ShowPlatformSoftwareFedActiveAclBindDbSummary
        * Added schema and parser for show platform software fed switch active acl bind db feature {feature_name} summary
    * Modified  ShowLicenseTechSupport
        * Modified the schema for the proxy port from str to Or(int, str)
    * Modified ShowIpAccessLists parser.
        * Modified regx. p_ip pattern.

* added show logging onboard rp {rp_standby} status to support standby
    * Modified ShowLoggingOnboardRpActiveEnvironmentContinuous
        * Added show logging onboard rp {rp_standby} environment continuous to support standby

* modified showloggingonboardswitchmessagedetail

* added show logging onboard rp {rp} message detail to support modular

* added showloggingonboardrpclilog
    * Added show logging onboard rp {rp} clilog to support modular

* iosxr
    * Fix for ShowL2vpnBridgeDomainDetail parser
        * Added flow_label_flags key in schema
    * Modified ShowL2VpnXconnectDetail
        * Modified folder name from ShowL2VpnXconnectDetail to ShowL2vpnXconnectDetail to match with class name in iosxr/show_xconnect.py
        * Added support for srv6 in cli 'show l2vpn xconnect detail' in ShowL2VpnXconnectDetail
        * Modified pattern <p14> to support 'SRv6         Local                          Remote'
        * Modified pattern <p43> to support 'Encap type Ethernet'
        * Added new pattern <p45> to support 'Ignore MTU mismatch Enabled'
        * Added new pattern <p46> to support 'Transmit MTU zero Enabled'
        * Added new pattern <p47> to support 'Reachability Up'
        * Modified folder name from ShowL2VpnXconnectMp2mpDetail to ShowL2vpnXconnectMp2mpDetail to match with class name in iosxr/show_xconnect.py
        * Modified folder name from ShowL2VpnXconnect to ShowL2vpnXconnect to match with class name in iosxr/show_xconnect.py
    * Modified ShowCefDetail
        * Modified regex <p1> to support pattern 'ffff10.0.0.1/128, version 189, SRv6 Headend, IID (EVPN-MH), internal 0x1000001 0x0 (ptr 0x8afff4a8) [3], 0x0 (0x0), 0x0 (0x8c2c70a8)'
        * Readded regex <p8> as it is not supporting pattern 'LDI Update time Oct 13 181819.691' properly in <p9> regex
        * Modified regex <p10> to support pattern 'via fc00c0001002/128, 8 dependencies, recursive, backup [flags 0x100]'
        * Modified regex <p11> to support pattern 'path-idx 0 NHID 0x0 [0x8b001f38 0x0], Internal 0x89d70af0'
        * Modified regex <p18> to support pattern '0     Y   Bundle-Ether313           fe8096aef0fffe726cda'
        * Added new regex <p21> to support pattern 'next hop VRF - 'default', table - 0xe0800000'
        * Added new regex <p22> to support pattern 'SRv6 H.Encaps.L2.Red SID-list {fc00c0001001e006}'
        * Modified schema according to the latest code and updated all unittest cases


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified Parser for ShowPppAll
        * Parser for show ppp all cli


--------------------------------------------------------------------------------
                                     Modify                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowLispV4PublicatioinPrefix
        * Added support for parsing sgt value
    * Modified ShowLispV6PublicatioinPrefix
        * Added support for parsing sgt value
    * Modified ShowLispEidTableServiceDatabase
        * Added support for parsing 'do not register', both for total count and per-prefix info
    * Modified ShowLispServiceDatabase
        * Added support for parsing 'do not register', both for total count and per-prefix info


