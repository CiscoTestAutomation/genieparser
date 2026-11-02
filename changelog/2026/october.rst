--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* nxos
    * Added ShowIpOspfNeighbor
        * show ip ospf neighbors
        * show ip ospf neighbors vrf {vrf}
    * Added ShowNxsecureLog
        * show nxsecure log {policy_id}
    * Added ShowIpMrouteSr
        * show ip mroute sr {group}
    * Added ShowNxsecureLogfiles
        * show nxsecure logfiles
    * Added ShowForwardingRouteDetail
        * show forwarding route {prefix} detail module {module}
    * Added ShowClock
        * show clock
    * Modified ShowIpv6MrouteVrfAll
        * show ipv6 mroute
    * Added ShowNxsecurePackages
        * show nxsecure packages
    * Added ShowIpNatMax
        * show ip nat max
    * Added ShowIpMrouteSrUmnat
        * show ip mroute sr umnat
    * Added ShowMvrMembers
        * show mvr members
    * Added ShowSegmentRoutingMpls
        * show segment-routing mpls
    * Added ShowForwardingDistributionIpv6MulticastRoute
        * show forwarding distribution ipv6 multicast route
    * Added ShowNxsecurePolicyStatus
        * show nxsecure policy status
    * Added ShowHardwareInternalErrorsAll
        * show hardware internal errors all
        * Parsed multiple device records per slot with per-instance counters.
        * Supports multi-word device names and range or annotated port values.
        * Excludes formatting delimiters from parsed output.
    * Added ShowMvrGroups
        * show mvr groups
    * Added ShowBgpIpv4UnicastPrefix
        * show bgp ipv4 unicast {prefix}
        * Added schema and regex support for IPv4 unicast prefix detail paths, labels, extended communities, originator, cluster list, and advertised peers.
    * Added ShowSystemInternalNbmInfoShmTableContext
        * show system internal nbm info shm table context

* iosxe
    * Added ShowAccessSessionCount
        * Parse switch-side filtered access-session counts without serializing the full session table; empty output is not accepted as a zero count.
        * Added captured zero-count golden and empty-output fixtures.
    * Added ShowPlatformSoftwareFedSwitchActiveFnfRecordCountAllAsic
        * show platform software fed switch {switch_type} fnf record-count all-asic
        * Parse per-ASIC current flow counts, total flows added, and total flows removed.
    * Added ShowSdwanOmpPeersDetail
        * show sdwan omp peers detail
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightSgaclUsageAux
        * Added parser for 'show platform hardware fed {switch} {switch_var} fwd-asic insight sgacl_usage_aux({device_id})' command.
        * Added parser for 'show platform hardware fed {switch_var} fwd-asic insight sgacl_usage_aux({device_id})' command.
    * Added C9050 abstraction wrappers that inherit C9350 parsers for
        * show platform hardware fed qos scheduler sdk interface
        * show platform hardware fed qos queue stats interface
        * show platform hardware fed qos queue config interface
        * show platform hardware fed qos queue stats internal port_type punt queue
        * show platform software fed switch active matm macTable
        * show platform software fed active acl info db detail
        * show platform software fed active punt asic cause brief
        * show platform hardware fed ... fwd-asic resource tcam utilization
        * show inventory
        * show switch stack-ports summary
    * Modified ShowLispDatabaseSuperParser
        * Added ``multihoming_site_id`` parsing for Ethernet database entries.
    * Modified ShowLispSiteDetailSuperParser
        * Added ETR-level ``l2_multihoming_site_id`` parsing.
    * Added ShowPlatformSoftwareCpuAlloc
        * 'show platform software cpu alloc'
    * Modified ShowPlatformResources
        * Added support for Service Processor data.
    * Modified ShowProcessesCpuPlatformProfile
        * Added support for sorted CPU profile commands
            * 'show processes cpu platform sorted profile {profile_name}'
            * 'show processes cpu platform sorted {sort_interval} ' 'profile {profile_name}'

* cheetah
    * Added ShowIpInterfaceBrief
        * show ip interface brief
    * Added ShowIpDhcpLease
        * show ip dhcp lease

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Modified ShowNxsecurePackages
        * Updated ``show nxsecure packages`` to support LPS, RPM, SHD, PKG, and BIN package filename extensions.
    * Modified ShowNxsecureLogfiles
        * Updated ``show nxsecure logfiles`` to support ``.tar.gz`` files.
    * Modified ShowNxsecureLog
        * Updated ``show nxsecure log {policy_id}`` to support process names containing spaces.
    * Modified ShowIpv6MrouteVrfAll
        * Moved regular expression compilation outside the line-processing loop.
        * Updated regex patterns to parse IPv6 route entries, incoming interfaces, outgoing interface counts, and outgoing interface flags.
        * Updated command execution to use the resolved command argument.
        * Added support for outgoing interface count lines with Fabric OIF.

* iosxe
    * Modified ShowRomvar
        * Added support for parsing ``TFTP_SERVER`` as the optional ``tftp_server`` field.
        * Added coverage for default and revision 1 active/standby output.
    * Modified ShowAccessSessionMacDetails
        * Retain optional multiline blocked_on reasons in targeted client details.
        * Accept captured details with no Server Policies section.
        * Preserve the existing command variants and positional signature.
        * Added captured pending-deletion golden coverage.
    * Modified ShowAuthenticationSessionsDetailsSuperParser
        * Added optional per-client blocked_on entries, including multiline Pending Deletion and SM Accounting Feature reasons.
        * ShowAccessSessionInterfaceDetails inherits this support without a command or positional signature change.
        * Added captured-output regression coverage and validated existing authentication/access-session golden fixtures.
    * Modified ShowPlatformSoftwareMemoryCallsite
        * Added command: show platform software memory {process} {hw} {switch_type} alloc callsite brief
        * Support active and standby command forms without a slot.
        * Parse supplied output without executing a device command.
        * Accept callsite tables without a tracekey header and preserve hexadecimal callsite identifiers.
        * Preserve the positional order of process, slot, hw, and output; switch_type is keyword-only.
        * Add slotless active/standby and supplied-output golden coverage using unchanged existing captures.
    * Modified ShowPlatformSoftwareMemoryBacktrace
        * Added command: show platform software memory {process} switch {switch_type} alloc backtrace
        * Support active and standby command forms without a slot.
        * Preserve hexadecimal callsite identifiers as strings while retaining decimal callsite support.
        * Preserve the positional order of process, slot, and output; switch_type is keyword-only.
        * Add slotless active/standby and supplied-output golden coverage using unchanged existing captures.
    * Modified ShowPlatSwObjectManagerF0ErrorObject
        * Added command: show platform software object-manager switch {switch} fp active error
    * Modified ShowPlatformSoftwareFedSwitchActiveFnfAttachPointsDump
        * Support DATALINK TRAFFIC rows in addition to existing IPv4 and IPv6 traffic rows.
        * Preserve parsing of input/output directions and attachment status for active and standby switches.
    * Modified ShowIpRouteDistributor, ShowIpv6RouteDistributor, ShowIpRoute, ShowIpv6Route parsers
        * Fix show ip/ipv6 route argument handling by separating protocol selectors from route selectors and rejecting invalid combinations
        * Support multicast routing-table names containing ':' symbol
    * Added ShowIpRouteMulticastDistributor and ShowIpv6RouteMulticastDistributor
        * New classes support show ip{v6} route multicast .. family of CLIs
    * Modified ShowIpNbarDiscovery
        * Added support for TwoGigabitEthernet interface headers in ``show ip nbar protocol-discovery protocol``.
        * Added golden output coverage for TwoGigabitEthernet and GigabitEthernet interfaces.
        * Fixed continuation row parsing to return the actual byte counts, current bit rates, and maximum bit rates without overwriting them.
        * Corrected existing golden expectations to match captured CLI values.
    * Modified ShowIpRouteDistributor and ShowIpv6RouteDistributor parsers
        * Added multicast fallback handling
    * Modified ShowLicenseTechSupport
        * Added support for pla_reporting output.
    * Modified ShowIpRouteSchema schema
        * Added boolean field possibly_down
        * Update ShowIpRoute parser to match and store `possibly down` routing table output
    * Modified ShowSdwanOmpPeersDetail
        * Added support for whitespace-separated headers in show sdwan omp peers detail.
        * Updated schema with optional tenant, peer status, packet, route, TLOC, service, and multicast fields.
        * Preserved legacy colon-separated output and added golden fixtures for both new output samples.
    * Modified ShowPlatformTcamUtilization
        * Added support for the six-slice TCAM utilization output on C9050.
    * Modified ShowPlatformSoftwareFedSwitchActivePbrInfoRouteMap parser
        * Updated p5 regex.
    * Modified ShowMkaSessions
        * Added support for the Probe Count and CA-Type columns introduced by MACsec key rotation enhancements.
        * Retained parsing support for the legacy output format.
    * Modified ShowPlatformSoftwareFedQosInterfaceSuperParser
        * Added optional MAC ACE schema coverage and recognized MAC ACE headers.
        * Captured class IDs, source and destination MAC addresses and masks, ethertype, COS, VLAN ranges, result actions, and meter fields.
        * Preserved IPv4/IPv6 ACE parsing, including outputs without ACE headers.
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressNpdDetailed
        * Preserved the MAC ACE capture alongside existing IPv4 regression data.
    * Modified ShowPlatformHardwareFedSwitchQosQueueStatsInterface
        * Retained C9250 numbered-switch regression coverage while preserving the parser implementation and existing fixtures from dev.
    * Modified ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear
        * Retained C9250 numbered-switch clear regression coverage.
    * Modified ShowPlatformTcamUtilization
        * Retained C9250 TCAM utilization regression coverage.
    * Modified ShowPlatformSoftwareFedActiveAclInfoDbDetail
        * Retained C9250 ACL detail coverage for headers with a feature prefix.
    * Modified ShowEnvironment
        * Added new optional key ``critical_alarms`` in parser and golden parser coverage.
        * Added six p4 states: ``Minor_Low``, ``Minor_High``, ``Major_Low``, ``Major_High``, ``Critical_Low``, and ``Critical_High``.
        * Added golden parser coverage for the ``Minor_Low`` environmental sensor state.
    * Modified ShowPlatform (rv1)
        * Updated p6 state pattern for ``fail, badinput``, ``fail, badoutput``, and ``fail, badcookie``.
        * Added golden parser coverage for the ``fail, badinput`` platform state.
    * Modified ShowMkaPolicy
        * Support the Probe Count column in show mka policy output from 27.1.1.
        * Add optional probe_count while preserving older policy output formats.
        * Parse wrapped interface lists for both older and newer policy rows.
        * Handle a single space between the cipher suite and applied interface.
    * Modified ShowMkaSessionsInterfaceDetails
        * Parse PSK Probing and Probe Count in show mka sessions interface {interface} detail output from 27.1.1.
        * Add optional psk-probing and probe-count keys for older output support.
    * Modified ShowAuthenticationSessionsDetailsSuperParser
        * Restored the legacy server_policies layout when Vlan Group follows Session-Timeout: both values share one numbered policy entry and subsequent policies retain their legacy indices.
        * Preserved separate VLAN entries for VLAN-only output and VLAN following other policies, including ACS ACL, without overwriting repeated VLANs.
        * Added interface-details regression coverage from multi-client and service-template authentication CLI, including MAC and switch variants.
        * Verified inherited IOS authentication and IOS/IOSXE access-session interface-details parsing and command dispatch.

* viptela
    * Modified ShowSystemStatus
        * Made build optional and parsed empty boot loader version, services, and configuration template fields.
        * Added a golden fixture for the 27.1 system status output.

* cheetah
    * Modified ShowInterfacesDot11radio
        * Allow AP output that omits the separate ``mac_address``/``HWaddr`` line while retaining the required ``radio_mac_address``.
        * Changed ``attributes``, ``mtu``, ``metric``, ``rx``, ``tx``, ``collisions``, ``txqueuelen``, ``rx_bytes``, and ``tx_bytes`` to Optional because they are not present on all AP outputs.

* ios
    * Modified ShowEnvironment
        * Added new optional key ``critical_alarms`` in golden parser coverage.
