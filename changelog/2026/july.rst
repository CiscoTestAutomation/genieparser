--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareFedIpRouteSummary
        * Parser for 'show platform software fed {switch_var} {state} ip route summary' command.
    * Added ShowPlatformSoftwareIpsecPolicyStatistics
        * Added schema and parser for 'show platform software ipsec policy statistics'
    * Added ShowPlatformSoftwareIpsecSwitchFlowAll
        * Added schema and parser for 'show platform software ipsec {switch} {switch_var} f0 flow all'
    * Added ShowPlatformSoftwareIpsecSwitchSadbAll
        * Added schema and parser for 'show platform software ipsec {switch} {switch_var} f0 sadb all'
    * Added ShowPlatformHardwareFedSwitchFwdAsicResourceFeatureIdMapping
        * Added schema and parser for 'show platform hardware fed {switch} {switch_var} fwd-asic resource feature-id-mapping'
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicResourceUtilizationFeature
        * Added schema and parser for 'show platform hardware fed {switch} {switch_var} fwd-asic resource utilization feature {feature_id}'
    * Added ShowCryptoIkev2Profile
        * Added schema and parser for 'show crypto ikev2 profile {profile_name}'
    * Added ShowRunningConfigFormatNetconfXml
        * show running-config | format netconf-xml
    * Added ShowYangSyncStatus
        * show yang sync status
    * Added ShowPlatformHardwareFedSwitchQosQueueConfig
        * Added schema and parser for 'show platform hardware fed switch active qos queue config interface {interface}'
    * Added ShowSubscriberDefaultSession
        * show subscriber default-session
    * Added ShowTopology, ShowTopologyAll, ShowTopologyDetailAll, ShowTopologyDetailAfi, ShowTopologyDetailVrf
        * show topology
        * show topology all
        * show topology detail all
        * show topology detail {ipv4 | ipv6} all
        * show topology detail {ipv4 | ipv6} topo <topo_name>
        * show topology detail {ipv4 | ipv6} multicast all
        * show topology detail {ipv4 | ipv6} multicast topo {topo_name}
        * show topology detail vrf {vrf} all
        * show topology detail vrf {vrf} {ipv4 | ipv6} all
        * show topology detail vrf {vrf} {ipv4 | ipv6} topo <topo_name>
        * show topology detail vrf {vrf} {ipv4 | ipv6} {multicast} all
        * show topology detail vrf {vrf} {address_family} {multicast} topo {topo_name}
    * Added ShowVpdnGroupSelectDefault
        * show vpdn group-select default
    * Added ShowVpdnSession
        * Added schema and parser for 'show vpdn session'
    * Added ShowCloudMgmtMigration
        * show cloud-mgmt migration
    * Added ShowCloudMgmtCompatibility
        * show cloud-mgmt compatibility
    * Added ShowPlatformHardwareQfpActiveClassificationClassGroupAll
        * show platform hardware qfp active classification class-group-manager class-group all
    * Added ShowSubscriberSessionFeatureAccessList
        * show subscriber session feature access-list
        * show subscriber session uid {uid} feature access-list
    * Added ShowSubscriberSessionFeatureL4Redirect
        * show subscriber session feature l4redirect
        * show subscriber session uid {uid} feature l4redirect
    * Modified ShowSubscriberSessionDetailed
        * show subscriber session uid {uid} detailed

* iosxr
    * Added ShowInventoryVendorType
        * Added schema and parser for 'show inventory vendor-type' command.

* iosxe
    * Added output changes in show meraki config updater command to include new fields for better visibility of configuration updates.
    * Added output changes in show cloud_mgmt config updater command to include new fields for better visibility of configuration updates.

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowInventory (rv1)
        * Recognize StackWise-Virtual ``Switch N Slot M Linecard/Supervisor/Router`` inventory names so ``slot_dict`` is bound for chassis such as the C9600 SVL.
        * Guard the pluggable/transceiver branch to prevent ``UnboundLocalError`` when ``slot_dict`` has not been assigned.
        * Recognize ``SM subslot <slot>/<subslot>`` inventory lines.
    * Modified ShowIpCefInternal
        * Added support for parsing Lookup in table output chain entries
    * Modified ShowIpv6CefInternal
        * Added support for parsing Lookup in table output chain entries
    * Modified ShowPlatformSoftwareFedSwitchActiveIpRouteDetail
        * Added parsing support for VRF route detail output with VXLAN next-hop information.
        * Added parsing support for global leaked route `LOOKUP` object output.
    * Added ShowPlatformSoftwareFedSwitchActiveIpv6RouteDetail
        * Added parsing support for IPv6 FED route detail output.
        * Added parsing support for IPv6 VRF VXLAN next-hop details.
        * Added parsing support for IPv6 global leaked route `LOOKUP` object output.
    * Added golden output testcases for EVPN route leaking IPv4 and IPv6 FED route detail validation.
    * Modified ShowPlatformRewriteUtilization
        * Modified parser by adding cli 'show platform hardware fed {switch} {active} fwd-asic resource rewrite utilization' and 'show platform hardware fed {active} fwd-asic resource rewrite utilization'
    * Modified ShowPlatformSoftwareFedIfm
        * Modified parser by adding cli 'show platform software fed {switch} {active} ifm interfaces tunnel' and 'show platform software fed {active} ifm interfaces tunnel'
    * Added fix for ShowPlatformSoftwareFedActiveAclBindDbSummary parser.
        * Added this fix to support multiple entries.
    * Added fix for ShowPlatformSoftwareFedSwitchActiveAclInfoSdkDetail parser.
        * Added this fix to support multiple entries.
    * Modified <ShowCtsEnvironmentData>
        * Added support to parse the transport_type field.
    * Modified ShowPlatformSoftwareFedIpv6MldSnoopingSummary parser
        * Enhancement added for "show platform software fed switch active ipv6 mld snooping summary".
    * Modified ShowPlatformHardwareFedSwitchFwdAsicInsightIpSourceGuardAcl
        * Added support for parsing IPv6 SIP entries without Source MAC (delegated/PD prefix entries)
    * Modified ShowPlatformSoftwareFedSwitchIfmInterfaceName
        * Added support for parsing "Mpp port oid"
    * Modified ShowIpNbarDiscovery
        * Modified P1 regex to match "Five gigabit" interface
    * Modified ShowAuthenticationSessionsDetailsSuperParser
        * Added server_policies vlan_group parsing and schema support for 'show authentication sessions interface {interface} details'.
        * Refined UT expected data for interface details to align with real output containing dual MAC sessions and per-session server_policies vlan_group values.
    * Modified ShowIpv6MldSnoopingVlan
        * Made 'mld' key Optional at global level
        * Added Optional 'oper_state' key at global level
        * Added Optional 'admin_state' and 'oper_state' keys at VLAN level
        * Added vlan-level 'max_response_time' parsing
        * Improved parsing logic to separate global and VLAN level fields
    * Modified ShowIpv6ProtocolsSchema schema
        * Added support for connected and static protocols
    * Modified ShowIpv6Protocols parser
        * REGEX update to match connected and static
        * Add connected and static protocols info in the dict
    * Modified ShowParameterMapTypeInspectParam
        * Changed keys `audit_trail`, `max_incomplete`, `one_minute`, `sessions_rate`, `udp`, `icmp`, `dns_timeout`, `tcp`, `zone_mismatch_drop`, `application_inspect`, and `sessions_maximum` from schema to Optional.
        * Added parsing support for `lisp inner packet inspection <state>` and exposed it as `lisp_inner_packet_inspection`.
        * Added a golden output testcase for `show parameter-map type inspect global` to validate parsing when those sections are absent.
    * Modified ShowPlatformHardwareFedSwitchFwdAsicInsightL2AttachmentCircuit parser
        * Enhancement added for "show platform hardware fed switch fwd asic insight l2 attachment circuit".
    * Modified ShowPlatformSoftwareFedSwitchIfmInterfaceName parser
        * Added support for parsing "speed"
    * Modified ShowPlatformSoftwareFedIpIgmpSnoopingSummary parser
        * Enhancement added for "show platform software fed switch active ip igmp snooping summary".
    * Modified ShowPlatformSoftwareFedSwitchWdavcFlows
        * Updated regex pattern p1 to match software-handled (SW) flows in addition to hardware-handled (HW) flows.
    * Modified ShowSdmPreferNew parser
        * Updated schema for missing fields and made those fields Optional.
        * Updated parser for 'show sdm prefer' and 'show sdm prefer custom' on C9500 to handle generic current/proposed feature lines and proposed-only feature lines.
    * Modified ShowPlatformSoftwareFedMatmMacTable
        * Added support for MATM output without machandle, siHandle, riHandle, and diHandle columns.
    * Modified ShowPlatformSoftwareFedSwitchActiveMatmMacTableVlanMac
        * Added support for MATM vlan/mac output without machandle, siHandle, riHandle, and diHandle columns.
    * Modified ShowPortSecurityAddress
        * Updated port field parsing to support short interface names.
    * Modified ShowLldpNeighborsInterfaceDetail
        * Made 'compiled' field as optional in schema to support outputs that do not contain 'compiled' field.
        * Added 'age_sec' and 'time_since_last_update_sec' fields as optional.
    * Modified ShowCloudMgmtConnect
        * Fixed section header regex (p2) to match Cloud-Mgmt prefixed section headers
        * Fixed p3 pattern to match 'service cloud-mgmt connect is disabled'
    * Modified ShowCloudMgmtConfigUpdater
        * Renamed p4_1/p4_2 to p4a/p4b to align with ShowMerakiConfigUpdater naming convention
        * Fixed p0 pattern to match 'service cloud-mgmt connect is disabled'
    * Modified ShowCloudMgmtCompatibility
        * Changed cloud_mgmt_cloud_monitoring and cloud_mgmt_cloud_management to Optional in schema to support empty output

* iosxr
    * Modified ShowProcessesMemoryDetail
        * Added optional pid key to the schema.
        * Updated regex pattern to accommodate show processes memory detail output with PID column.
    * Modified ShowPlatform
        * Modified parser for 'show platform' command for new State

* linux
    * Modified Ls
        * Updated command execution to build ``ls -{args}`` and ``ls -{args} {directory}`` from parser arguments.
        * Added ``l`` to supplied option arguments when long-listing output is not requested so the parser receives the expected output shape.
        * Added golden fixture coverage for ``ls -{args}`` and ``ls -{args} {directory}``.

* apic
    * Modified Ls
        * Updated command execution to build ``ls -{args}`` and ``ls -{args} {directory}`` from parser arguments.
        * Added ``l`` to supplied option arguments when long-listing output is not requested so the parser receives the expected output shape.
        * Added golden fixture coverage for ``ls -{args}`` and ``ls -{args} {directory}``.

* nxos
    * Modified Ls
        * Added golden fixture coverage for the inherited NXOS ACI ``Ls`` command forms.

* common
    * Modified package metadata
        * Added SDK generator parser datafiles to installed package data for ``make json_all``.
        * Updated the parser development package version to satisfy the current ``genie`` dependency range during CI installs.
    * Modified _fuzzy_search_command
        * Added exact command lookup after command preprocessing so normalized commands still resolve to their exact parser when available.
        * Updated fuzzy token scoring to prefer exact token matches over argument captures.
        * Added unittest coverage for fuzzy matching and argument extraction regressions.

--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowInterfaceCounterErrors
        * show interfaces counters errors
        * show interfaces {interface} counters errors
    * Modified ShowIpCefDetail
        * Added support for parsing LISP related nexthops and remote EID stats
    * Modified ShowSubscriberSessionDetailed
        * Updated regex to support multi-word Access-type and Client values in the config history section
    * Modified ShowPlatformSoftwareFedSwitchActiveStpVlan
        * Made 'ingress' and 'egress' fields as optional in schema to support outputs that do not contain the 'ingress' and 'egress' fields.
