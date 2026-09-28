--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformHardwareFedSwitchActiveNpuSlotPortInfo
        * Added parser for 'show platform hardware fed switch {mode} npu slot 1 port {port} port-info' command.
    * Added ShowPlatformHardwareAuthenticationStatus for C9400
        * show platform hardware authentication status
    * Added ShowPlatformHardwareAuthenticationStatus for C9550
        * show platform hardware authentication status
    * Added ShowWirelessInterfaceSummary
        * Added parser for ``show wireless interface summary``.
        * Added support for IPv6 continuation addresses.
    * Added ShowPlatformSoftwareProcessDatabaseResourceManagerSwitchR0Summary
        * Added parser for 'show platform software process database resource-manager switch {switch_id} r0 summary'.
    * Added ShowIpInterfaceBriefExclude
        * Added parser for 'show ip interface brief | exclude {exclude}' command.
    * Added ShowPlatformStormControlMode
        * Added Schema and parser for 'show platform storm-control mode'.
    * Added ShowPlatformFedActiveTcamUtilization for c9400
        * Added schema and parser for 'show platform hardware fed active fwd-asic resource tcam utilization'
        * Added schema and parser for 'show platform hardware fed active fwd-asic resource tcam utilization {asic}'
    * Added ShowPlatformFedStandbyTcamUtilization for c9400
        * Added schema and parser for 'show platform hardware fed standby fwd-asic resource tcam utilization'
        * Added schema and parser for 'show platform hardware fed standby fwd-asic resource tcam utilization {asic}'

* nxos
    * Added ShowIpMrouteSourceTreeVrfAll
        * show ip mroute 225.1.1.7 47.1.1.2 source-tree vrf all
    * Added ShowIpIgmpSnoopingGroups
        * show ip igmp snooping groups

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowLicenseTechSupport
        * Added support for PolicyV2 output and additional optional fields.
    * Modified ShowPlatformSoftwareFedQosInterfaceSuperParser
        * Added new fields in schema and parser according to new output
    * Modified ShowSpanningTree
        * Updated show spanning-tree parser
    * Modified ShowSpanningTreeDetail
        * Updated show spanning-tree detail parser
    * Modified ShowSpanningTreeInconsistentports
        * Updated show spanning-tree inconsistentports parser
    * Modified ShowSpanningTreeInterface
        * Updated show spanning-tree interface {interface} parser
    * Added ShowSpanningTreeVlanInconsistentports
        * Added schema and parser for 'show spanning-tree vlan {vlan} inconsistentports'
    * Modified ShowDeviceTrackingDatabase
        * Fixed device_info_capture_database regex to handle time_left values with a trailing 'try N' suffix (e.g. 'try 0 1710 s try 0').
    * Modified ShowIpRoute parser
        * Fix show ip route parsing for replicated OSPF external routes with combined codes like O E2+.
    * Modified ShowVersionRunning
        * Updated <p1> to capture hyphenated package names in the package key.
    * Modified ShowPlatformSoftwareFedSwitchActiveIpRoute parser
        * Enhancement added for "show platform software fed {active} ip route".
    * Modified ShowPlatformSoftwareFedSwitchActiveIpv6Route parser
        * Enhancement added for "show platform software fed {active} ipv6 route".
    * Modified ShowTemplateBrief
        * Made the `service_template` key optional when the Service Templates table is present but contains no entries.
        * Added a golden output testcase for the empty Service Templates table.
    * Modified ShowIpv6ProtocolsSchema schema
        * Added support for application and ND protocols
    * Modified ShowIpv6Protocols parser
        * REGEX update to match application and ND
        * Add application and ND protocols info in the dict
    * Modified ShowPlatformSoftwareFedMatmMacTable
        * Updated the short MATM row regex to parse C9250 output consistently.
        * Added a C9250 regression test for secure client and SVI MAC entries.
    * Modified ShowUACUplink
        * Changed the IPv4 and IPv6 `configured_interface` schema keys to Optional when configured uplink interface lines are absent.
        * Updated the <p3> and <p4> match handling to initialize the IPv4 or IPv6 section directly from the active uplink interface line.
        * Added golden output testcases for routing-platform output without configured uplink interface lines.
    * Modified ShowPlatformSoftwareFedQosInterfaceSuperParser
        * Changed ``qos_profile_information`` in the schema to Optional so NPD and SDK detailed output without QoS profile details can be parsed.
    * Modified ShowPlatformSoftwareFedSwitchActiveNatAcl
        * Added support for the optional ``VRF`` column introduced in IOS XE 27.1.1 while retaining support for legacy output without the column.
        * Added golden parser coverage for NAT ACL entries containing a VRF ID.
    * Added support for standby CLI variants in the ShowPlatformSoftwareFedActiveSdmFeature parser.
        * show platform software fed switch standby sdm feature
        * show platform software fed standby sdm feature
    * Modified ShowIpIgmpGroupsDetail
        * Updated the source-row regex patterns for ``v3_exp`` and ``csr_exp`` to support colon-delimited timer values.
        * Added test coverage for source and forwarding information when ``v3_exp`` contains a value such as ``00:02:49``.
    * Modified ShowPlatformSoftwareFedSwitchFnfMonitorsDump
        * Added support for the C9550 colon-separated FNF monitor attributes and pipe-separated record table.
        * Added optional schema fields for monitor identifiers, cache details, record details, and monitor handles.
        * Added support for multiple monitor-statistics blocks while retaining the existing legacy ``Monitor (0x...)`` format.
    * Modified ShowPlatformSoftwareFedSwitchActiveFnfAttachPointsDump
        * Added support for the C9500 legacy ``ap(...)`` attach-point format.
        * Added extraction of non-null FNF ``monitor0`` and ``monitor1`` pointers as integer ``monitor_ids``.
        * Added IPv4, IPv6, INGRESS, and EGRESS support while retaining the existing C9550 tabular format.
        * Updated the schema to use ``ListOf(int)`` for ``monitor_ids`` and made C9550-only fields optional.
