--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowBgpNeighborsAdvertisedRoutesSuperParser
        * Updated regex pattern <p3_1> to accommodate various outputs.
    * Modified ShowClnsIsNeighborsDetail
        * Updated regex pattern <p2> to accommodate various outputs.
    * Modified ShowInterfaces
        * Added regex pattern <p53> to capture value of carrier transitions
    * Modified ShowPlatformSoftwareFedSwitchActiveVpSummaryVlan Parser
        * Fixed parser to execute show comman on svl, HA and SA devices
    * Modified ShowEnvironment Parser
        * Modified the p4 regex pattern to capture missing data.
    * Modified ShowRunningConfigNve
        * Fixed regex <p2> and <p3> to accomodate various values and to fix MAC value regex.
        * Changed key <serial> in schema to optional
    * Modified ShowRunningConfigNve
        * Added regex <p5_4> and <p5_5>.
        * Update code for <p3_8> to include space between 'ipv4' and 'mask' key.
    * Modify ShowPlatformSoftwareDistributedIpsecTunnelInfo
        * Updated parser to validate per tunnel info
    * Modified ShowIpNhrpNhsDetail Parser
        * parser for 'show ip nhrp nhs {tunnel} detail' Modified schema and regex pattern
    * Fix for ShowSpanningTreeInterface
        * Modified regular expression in order to satisfy P2p Peer (STP)
    * Modified parser ShowHardwareLed
        * Enhanced the parser to get LED Ecomode status, Added schema and regex pattern <p12_1>
    * Modified parser ShowProcessesCpuSorted
        * Fixed schema and regex pattern
    * Fix for ShowEnvironmentSuperParser
        * added p1_3 match pattern
    * Modified ShowIpMfib
        * To support interface port-channel type in iif and oif
        * Additional handling for egress_data
        * Sample output for iif  Port-channel5 Flags RA A MA
        * Sample output for oif  Port-channel5 Flags RF F NS
    * Modified ShowIpv6Mfib
        * To support interface port-channel type in iif and oif
        * Additional handling for egress_data
        * Sample output for iif  Port-channel5 Flags RA A MA
        * Sample output for oif  Port-channel5 Flags RF F NS
    * Modified ShowLispEthernetMapCachePrefix Parser
        * Made prefix-location optional
    * Added
        * Added condition for channel_group in pagp_dad_obj
    * Fixed ShowControllerVDSLSchema parser
        * Fixed schema for 'modem_fw__version' & 'modem_phy_version' for show controller vdsl {slot_no}
    * Modified ShowEtherchannelProtocol
        * Fix P1_1 regular expression.
    * Adding parser for ShowIpOspfRibRoute
        * Added ShowIpOspfRibRoute for "show ip ospf rib <>"
    * Modified ShowIpv6RouteWord
        * Added support for parsing output with LISP interfaces
    * Modified ShowRunningConfigNve
        * Added regex <p5_6> and <p5_7> for keys 'data_mdt_group', 'data_mdt_group_mask' and 'data_mdt_threshold'
    * Modified ShowMplsForwardingTable
        * Added bytes_label_switched to exclude

* nxos
    * Fix for ShowRunningConfigInterface
        * Added p20 regex to match the user's data.
    * Modified ShowRunningConfigBgp
        * Updated code for <p32> to match the list of values.
    * Modified ShowInterfaceStatus
        * Refactored regex pattern to accommodate modern outputs from Nexus 9000 series and be easier to maintain overall.
    * Added
        * Updated regex pattern for <p31>
    * Modified ShowRunningConfigInterface
        * Modified schema to store secondary ip address
        * Improved p17 regex to capture proper ip address
        * Added p21 regex to capture secondary ip address

* iosxr
    * Modified ShowBgpL2vpnEvpnSummary Parser
        * Added regex p8a and p8b
        * Added code in pattern <p8a> and <p8b>
    * Modified ShowIsisDatabaseDetail
        * Added pattern <r26> to parse line 'Metric 10         MT (IPv6 Unicast) IPv6-Ext-InAr fc00a00020003/128'
        * Modified pattern <r25> code to parse multiple srv6 locator lines
    * Modified ShowOspfNeighbor
        * Modified schema and code to store multiple neighbor values into a list
    * Modified ShowL2vpnBridgeDomainDetail
        * Modified schema and existing code to have separate entry for access pw
        * Modified regex p27 to fix mismatch pw_class and xc_id value
    * Modified ShowBgpVrfAfPrefix Parser
        * Added code in pattern <p11>
        * Added keys <group_best, backup, add_path, import_candidate, imported, redistributed> in schema as optional parameters
        * Modified 'r_value' key as optional parameter

* viptela
    * Modified ShowOmpRoutes
        * Added tenant key as option.
        * Updated regex pattern p1 and p2 to accommodate various outputs.

* iosxe/c9600/c9606r
    * Modified ShowPlatformHardwareFedActiveTcamUtilization
        * Added command for switch mode standby
    * Modified ShowPlatformTcamPbrNat
        * Added command for switch mode active

* common
    * Updated pyats configuration import
    * Modified .gitignore
        * Added the `venv/` directory to the .gitignore file. Common convention dictates that Python virtual environments are stored in a directory named `venv`, which should not be committed to a repository.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* ios
    * Added ShowVlanInternalUsage
        * show vlan internal usage

* iosxe
    * Added ShowPlatformSoftwareMatmSwitchTable
        * Parser for cli 'show platform software matm switch {switch} {slot} table'
    * Added ShowIsisNeighborSuperParser
        * Added super parser for show isis neighbor and schema
        * Added parser for show isis neighbor and show isis neighbor detail
    * Added ShowMdnsSdCache
        * parser for 'show mdns-sd cache remote'
    * Added ShowPlatformSoftwareMemoryDatabaseFedSwitchActiveCallsite
        * show platform software memory database fed {switch} {switch_var} callsite
    * Added ShowIPNameServer Parser in show_ip.py
        * show ip name-servers
            * show ip name-servers vrf {vrf}
    * Added ShowPlatformSoftwareFedSwitchActiveNatAcl
        * Parser for cli 'show platform software fed switch active nat acl'
    * Added ShowPlatformSoftwareFedSwitchActiveNatFlows
        * Parser for cli 'show platform software fed switch active nat flows'
    * Added ShowPlatformSoftwareFedSwitchActivePuntBrief
        * Parser for cli 'show platform software fed switch active punt ios-cause brief'
    * Added ShowIsisIpv6RibParser
        * Added parser for show isis ipv6 rib and schema
    * Added ShowDiagnosticStatus
        * Added parser for show diagnostic status
    * Added ShowL2routeEvpnEs
        * show l2route evpn es
        * show l2route evpn es esi {esi}
        * show l2route evpn es origin-rtr {origin_rtr}
        * show l2route evpn es origin-rtr {origin_rtr} esi {esi}
        * show l2route evpn es producer {producer}
        * show l2route evpn es producer {producer} origin-rtr {origin_rtr}
        * show l2route evpn es producer {producer} origin-rtr {origin_rtr} esi {esi}

* iosxr
    * Added ShowBgpL2vpnEvpnSummary
        * Added parser for show bgp l2vpn evpn summary
    * Added ShowBgpAddressFamily
        * Added parser for show bgp
        * Added parser for show bgp {address_family}
    * Modified ShowBgpInstanceSummary
        * Modified pattern <p11> to parse both lines 'Table ID 0x0' and 'Table ID 0x0   RD version 0'
        * Modified pattern <p15> to parse line 'BGP scan interval 60 secs'

* generic
    * Show version
        * Added support for cheetah/ap


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowTerminal Parser


