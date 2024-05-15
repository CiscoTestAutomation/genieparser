--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowFlowMonitorCache
        * Added patterns <P34> to <P38> to capture datalink and interface inputs
    * Modified ShowBannerMotd
        * Enhanced parser to capture multiple line messages.
    * Modified ShowInterfaceStatusModule Parser
        * Modified the regular expression for value of vlan to allow not only numbers but also str (i.e. routed), so routed ports can be matched.
    * Modified ShowDiagnosticResultModuleTestDetail Parser
        * Modified the schema to have a new optional key 'port_status'
        * Modified the parser to always use the test name as the index key for the test
    * Modified the show inventory parser.
        * Modified the regexp p1_8 to support the latest changes in 17.15 and to  support the  old  releases.
    * Modified ShowLispPrefixList
        * Added support for parsing additional fields
        * Added support for parsing entry sources as a list
    * Fixed ShowMonitor
        * Fixed regex and support for new attribute Source EFPs
    * Modified ShowLispDatabaseSuperParser
        * Fixed p2 regex to make value optional
    * Modified ShowLispIpMapCachePrefixSuperParser
        * Fixed typo for parsing rloc_probe_in in regex.
    * Modified ShowLispPrefixList
        * Made entries optional in schema.
    * Modified ShowOspfv3NeighborInterface Parser
        * Fix p2 regex to capture when dead time is -
    * Modified ShowAuthenticationSessionsInterfaceDetails Parser
        * Added execute timout of 300 seconds to cater large output
    * Modified ShowPlatformSoftwareFedActiveMonitor Parser
        * fix p2 regex
    * Modified ShowHardwareLed Parser
        * Modified the Metadata for beacon value as optional and added alarm-in3 and alarm-in4 values to support for ie9k devices
    * Modified ShowEeeStatusInterface Parser
        * Added few more optional arguments to the schema.
    * Modified ShowFacilityAlarmStatus
        * Added <p3> and <p4> regex
        * Added key 'index' as optional parameter to schema
    * Modified parser ShowPlatformSoftwareFedIgmpSnooping
        * Enhanced the parser to get Snoop State, Added schema and regex pattern <p1_1>
    * Modified parser ShowPolicyMapControlPlaneClassMap
        * Modified arguments bytes and bps as optional in schema
    * Modified show_vtp_password
        * Enhanced the parser by adding '^VTP +Password +is +configured.$' to each line in the output
    * Fix for TracerouteIpv6
        * Fixed strig split to remove *
    * Added New Parser
        * Added New Parser ShowSmartPowerDomain
        * Added New Parser ShowSmartPowerVersion
    * Modified ShowPlatformTcamPbr
        * Added switch_type same as in iosxe/c9600/c9606r
    * Modified ShowLispPublicationPrefixSuperParser
        * Added support for parsing the same locator from different source addresses.

* nxos
    * Modified ShowAccessListsSummary
        * Modified regex pattern <p1> and <p3> to accommodate various outputs.
    * Modified ShowMacAddressTableBase
        * updated mac_type and age in drop section.

* iosxr
    * Update baud_rate key same as iosxe schema
    * Modified fix for ShowInstallCommitSummary
        * Added schema and code for fix the new output

* iosxe/c9500
    * Modified ShowPlatformFedTcamPbrNat
        * Added switch_type same as in iosxe/c9600/c9606r


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowMeraki
        * added new parser for cli 'show meraki'
        * added new parser for cli 'show meraki connect'
    * Added ShowPlatformSoftwareFedSwitchActiveNatInterfaces
        * Parser for cli 'show platform software fed switch active nat interfaces'
    * Added ShowPlatformSoftwareFedSwitchActiveNatRules
        * Parser for cli 'show platform software fed switch active nat rules'
    * Added ShowL2vpnSdwanAll
        * parser for ShowL2vpnSdwanAll
    * Modified existing Parser
        * Added New 33 and 34 regex
    * c9400
        * Added ShowPost
            * parser for 'show post' on modular platform c9400
    * Added ShowIpSockets
        * parser for 'show ip sockets'
    * Added ShowPlatformSoftwareMemoryDatabaseFedSwitchActiveCallsite Parser.
    * Added ShowDiagnosticStatus Parser.
    * Added ShowPlatformSoftwareFedSwitchActivePuntBrief Parser.
    * Added ShowL2ProtocolTunnelSummary
        * added new parser for cli 'show l2protocol-tunnel summary'
    * Added ShowPlatformHardwareIomdMacsecPortSubport
        * Added parser for show platform hardware iomd {lc_no} macsec port {port_no} sub-port {sub_port1} {sub_port2} | i Free" and schema
    * Modified ShowBgpNeighborsAdvertisedRoutes
        * Added show bgp address_family vrf vrf neighbors neighbor advertised-routes to accommodate various outputs.
    * Added ShowPlatformSoftwareIomdMacsecInterfaceDetail
        * Added parser for show platform software iomd {lc_no} macsec interface {port_no} detail and schema
    * Added ShowPlatformHardwareQfpInterfaceIfnamepath parser
        * Parser for "show platform hardware qfp <status> interface if-name <interface> path"
    * Added parser ShowPlatformSoftwareFedSwitchActiveFnfSwStatsShow
        * show platform software fed {switch} {switch_var} fnf sw-stats-show
        * show platform software fed {switch_var} fnf sw-stats-show
    * Added class ShowSdroutingControlLocalPropertiesSummary
        * show sd-routing control local-properties summary
    * Added class ShowSdroutingControlLocalPropertiesWanDetail
        * show sd-routing control local-properties wan detail
    * Added class ShowSdroutingControlLocalPropertiesWanIpv4
        * show sd-routing control local-properties wan ipv4
    * Added class ShowSdroutingControlLocalPropertiesWanIpv6
        * show sd-routing control local-properties wan ipv6
    * Added class ShowSdroutingControlLocalPropertiesVbond
        * show sd-routing control local-properties vbond

* cheetah
    * Updated parsers for ShowInterfacesDot11radio to support vap_rx and vap_tx statistics
    * Added parsers for ShowInterfacesDot11radio, ShowInterfacesWired, ShowVersion

* iosxr
    * Modified Ping
        * Modified regex pattern <p1> to accommodate various outputs.
    * Added ShowSegmentRoutingTrafficEnggPccLsp
        * parser for show segment-routing traffic-eng pcc lsp

* generic
    * Added pid to ShowVersion


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* ios
    * Added ShowLispInstanceIdService
        * show lisp instance-id {instance_id} {service}
        * show lisp all instance-id {instance_id} {service}
        * show lisp {lisp_id} instance-id {instance_id} {service}
        * show lisp locator-table {locator_table} instance-id {instance_id} {service}


