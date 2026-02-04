--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformHardwareCppActiveFeatureNatDatapathPool schema and parser
        * Added schema and parser for show platform hardware cpp active feature nat datapath pool
    * Added ShowIpv6VirtualReassembly parser
        * 'show ipv6 virtual-reassembly'
    * Added ShowPlatformHardwareCppActiveFeatureNatDatapathTime parser.
        * Added parser for cli 'show platform hardware cpp active feature nat datapath time'.
    * Added ShowPlatformSoftwareFedSwitchSecurityFedIpsgIfIdDetail
        * Added parser for 'show platform software fed switch security fed ipsg if-id {if-id} detail' command.
    * Added ShowPlatformSoftwareFedSwitchSecurityFedIpv6sgIfId
        * Added parser for 'show platform software fed switch security fed security-fed ipv6sg if-id {if-id}' command.
    * Added ShowPlatformHardwareQfpActiveClassificationCceInterfaceBrief
        * Added show platform hardware qfp active classification cce interface brief parser and tests
    * Fixed parsing issue in ShowPlatformSoftwareAdjacencyNexthopIpfrr
        * Adj-ID field now supports hexadecimal values to prevent nexthop parsing failures
    * Added ShowIpOspfFast-reroutePrefix-summary
        * Added show ip ospf fast-reroute prefix-summary parser and tests
    * Added ShowCryptoAutovpnSession
        * Added schema and parser for show crypto autovpn session command.
    * Added ShowCryptoAutovpnSessionPeerno
        * Added schema and parser for show crypto autovpn session peerno {peerno} command.
    * Added ShowPlatformSoftwareNatFpActiveTranslation
        * 'show platform software nat fp active translation'
    * Added ShowPlatformSoftwareFedSwitchSecurityFedIpv6sgClear
        * Added parser for 'show platform software fed switch security fed ipv6sg clear' command.
    * Added ShowPlatformSoftwareFedSwitchSecurityFedIpsgClear
        * Added parser for 'show platform software fed switch security fed ipsg clear' command.
    * Added ShowLoggingProcessFedInternalStartLastClearSwitchActive
        * Added schema and parser for show logging process fed internal start last clear switch active command.
    * Added ShowLoggingProcessFedInternalStartLastClearSwitchActive
        * Added schema and parser for show logging process fed internal start last clear switch active command.
    * Added ShowPolicyFirewallSessionsPlatformV6SourceAddress
        * show policy-firewall sessions platform v6-source-address {address}
    * Parser Updates
        * show running-config | section alarm
        * Added support for parsing 'show running-config | section alarm' command output.
    * Added Parser for parsers for below commands
        * 'show processes cpu platform profile DP'
        * 'show processes cpu platform profile CP'
        * 'show processes cpu platform profile SP'
    * Added ShowPlatformSoftwareAdjacencyNexthop-ipfrr
        * Added show platform software adjacency nexthop-ipfrr parser and tests
    * Added ShowPlatformHardwareCppActiveFeatureNatDatapathMap
        * 'show platform hardware cpp active feature nat datapath map'
    * Added ShowPlatformHardwareCppActiveFeatureNatDatapathStats parser.
        * Added parser for cli 'show platform hardware cpp active feature nat datapath stats'.
    * Fixed parsing of external OSPF routes in show ip ospf rib
        * Added support for Ext/NSSA routes with forward cost and tag fields
    * Added ShowPlatformHardwareCppActiveFeatureNatDatapathSessDump parser
        * 'show platform hardware cpp active feature nat datapath sess-dump'
    * Added ShowAccessListFqdnClient
        * Added parser for 'show access-list fqdn client' command.
    * Added ShowFQDNDatabaseFqdn
        * Added parser for 'show fqdn database fqdn' command.
    * Added ShowFQDNDebugStatistics
        * Added parser for 'show fqdn debug statistics' command.
    * Added ShowPlatformHardwareFedSwitchFwdAsicAbstractionPrintResourceHandle
        * Added parser for 'show platform hardware fed switch fwd asic abstraction print resource handle' command.
    * Solve parsing of repair path entries in show isis rib
        * Improved handling of repair path attributes to support both single and multiple flags (e.g. DS,DS,SR)
    * Added ShowCtsSxpExportImportGroupDetailed parser.
        * Added parser for cli 'show cts sxp export-import-group {role} detailed'.
    * Enchanced ShowCtsSxpConnections parser.
        * Enchanced parser for cli'show cts sxp connections'.
    * Added ShowPolicyFirewallSessionsPlatformDestinationPort
        * show policy-firewall sessions platform destination-port {port}
    * Added ShowPlatformHardwareCppActiveFeatureNatDatapathBind schema and parser
        * Added schema and parser for show platform hardware cpp active feature nat datapath bind
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightIpSourceGuardAcl parser
        * Added rv1 parser for 'show platform hardware fed switch 1 fwd-asic insight ip_source_guard_acl' command.
    * Added ShowPlatformSoftwareIpFpActiveCefSummary
        * Added show platform software ip FP active cef summary parser and tests

* iosxe/rv1
    * Added ShowInterfacesTransceiver
        * Added show interfaces transceiver parser in rv1 for new device output format.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowLoggingOnboardRpActiveUptime
    * Added regex pattern to accept chassis type
    * Modified ShowPlatformHardwareModuleInterfaceStatus
        * Schema supports both Optional l2_network and Optional l3_network keys
    * Modified ShowPlatformHardwareQfpActiveInterfaceIfName
        * 'show platform hardware qfp active interface if-name {interface}'
    * Modified ShowCableDiagnosticsTdrInt
        * Modified parser ShowCableDiagnosticsTdrInt in iosxe for show cable diagnostics tdr interface <interface name>
    * Modified ShowPlatformHardwareModuleInterfaceStatus
        * Schema supports both Optional vlan_mode and Optional native_vlan keys
    * Modified ShowMkaSessionDetail
        * 'show mka session detail'
    * Add ShowConnectionName parser
        * Added schema and parser for show connection name command.
    * Modified ShowPlatformHardwareQfpActiveFeatureFirewallDatapathScbDetail
        * 'show platform hardware qfp active feature firewall datapath scb any any any any any all any detail'
    * Modified ShowInterfacesTrunk
        * Parser supports show interfaces <interface> trunk command.
    * Modified ShowPlatformSoftwareFedSwitchActiveStpVlan
        * Added the keys stp_state_hw, gid, mac_learn in schema
        * Added the regexp p1_1 and the corresponding code.
    * Modified ShowMacsecStatusInterface
        * 'show macsec status interface {interface}'
    * Fixed parsing issue in 'show environment power all' command for IE9k devices
    * Modified ShowPolicyMapTypeInspectZonePairSession
    * Added regex pattern to match the ipv6 support for zonepair session
    * Modified ShowPlatformSoftwareInterfaceFpActive
        * 'show platform software interface fp active name {interface}'
    * ShowRomvar
        * Updated the variable random_num to optional
    * ShowCryptoIkev2SaDetail
    * Modified ShowCdp
    * Modified regex pattern to match the cdpv2 for "show cdp" command
    * Modified ShowCryptoSessionRemoteSchema
        * Modified parser ShowCryptoSessionRemoteSchema in iosxe for show crypto session remote <remote-ip>
    * Modified ShowNat64Statistics
        * 'show nat64 statistics interface {interface_name}'

* iosxe ie3k
    * Modified ShowEnvironmentAll
        * Fixed ShowEnvironmentAll parser in IOSXE IE3K platform.

* fixed parser to work with new funtionality changes
    * ShowCryptoIkev2Session

* fixed parser to work with new funtionality changes
    * ShowCryptoIpsecSaDetail

* fixed parser to work with new funtionality changes
    * ShowCryptoIpsecProfile
        * Fixed parser to work with new funtionality changes
    * ShowCryptoIkev2Proposal
        * Fixed parser to work with new funtionality changes
    * ShowCryptoIkev2Sa
        * Fixed parser to work with new funtionality changes
    * ShowCryptoIpsecSaIpv6Detailed
        * Fixed parser to work with new funtionality changes

    * Modified ShowPolicyMapTypeSuperParser parser in show_policy_map.py
        * Add support for 'match' criteria and 'match_stats' under each class in policy map


