--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* nxos
    * Added ShowNxsecureStatus
        * show nxsecure status
    * Modified ShowIpMrouteSummary
        * show ip mroute summary count
    * Added ShowHardwareProfileForwardingMode
        * show hardware profile forwarding-mode
    * Added ShowMvrInterface
        * show mvr interface
    * Added ShowSystemRoutingMode
        * show system routing mode
    * Added ShowProcessesMemoryShared
        * show processes memory shared
    * Added ShowIpv6PimStatistics
        * show ipv6 pim statistics
    * Added ShowDampeningInterface
        * show dampening interface
    * Added ShowPolicyMapInterfaceControlPlane
        * show policy-map interface control-plane
        * Added schema and parser support for byte and packet transmitted and dropped counters.
        * Added regex handling for byte and packet counter units.
        * Added optional schema support for offered, conformed, violate, and violated rate sections.
        * Added golden fixtures for byte counter, packet-only, and empty output.
    * Added ShowIcamScaleMulticastRouting
        * show icam scale multicast-routing
    * Added ShowCandidateSummary
        * show candidate summary
        * show candidate summary committed
        * show candidate summary pending
    * Added ShowIpPimVrfInternal
        * show ip pim vrf internal
        * Parsed RP change and PFM SD state as booleans
    * Added ShowIpNatTimeout
        * show ip nat timeout
    * Added ShowIpMrouteDetail
        * show ip mroute detail
        * Added schema and regex support for detailed multicast route counters, route client counts, data-created state, statistics, incoming interfaces, and outgoing interfaces.

* iosxe
    * Modified ShowInventory revision 1
        * Added a member inventory view that preserves member-qualified chassis, supervisor, line-card, and descendant records without changing the existing main and slot trees.
    * Added C9250 support for C9350-compatible parsers
        * show platform hardware fed qos scheduler sdk interface
        * show platform hardware fed qos queue stats interface
        * show platform hardware fed qos queue config interface
        * show platform hardware fed qos queue stats internal port_type punt queue
        * show platform software fed active acl info db detail
        * show platform software fed active punt asic cause brief
        * show platform software fed switch active matm macTable
        * show inventory
        * show switch stack-ports summary
    * Added ShowDeviceTrackingAnchors
        * show device-tracking anchors
        * show device-tracking anchors vlan {vlan}
    * Added ShowPlatformSoftwareFedSwitchActivePbrUsageRouteMap
        * Added parser for 'show platform software fed switch {switch_var} pbr usage route-map {route_map}' command.
    * Added ShowPlatformSoftwareFedSwitchActivePbrInfoRouteMap
        * Added parser for 'show platform software fed switch {switch_var} pbr info route-map {route_map}' command.
    * Added C9250 support to ShowPlatformTcamUtilization
        * show platform hardware fed {switch} {mode} fwd-asic resource tcam utilization
        * show platform hardware fed active fwd-asic resource tcam utilization
        * show platform hardware fed switch {mode} fwd-asic resource tcam utilization
        * show platform hardware fed {switch} {mode} fwd-asic resource tcam utilization {asic}
        * show platform hardware fed active fwd-asic resource tcam utilization {asic}
        * show platform hardware fed switch {mode} fwd-asic resource tcam utilization {asic}
    * Added ShowIpPortsAll
        * show ip ports all
    * Added ShowPlatformHardwareFedSwitchQosQueueStatsInterface
        * Added schema and parser for 'show platform hardware fed switch {switch_num} qos queue stats interface {interface}'
        * Added schema and parser for 'show platform hardware fed active qos queue stats interface {interface}'
    * Added ShowEnvironmentAll
        * show environment all
    * Added ShowPlatformHardwareVoltageMarginRpActive
        * show platform hardware voltage margin rp active
    * Added ShowDhcpServerTrackingDatabase
        * show dhcp-server-tracking database
        * show dhcp-server-tracking database vlan {vlan_id}
    * Added ShowDhcpServerTrackingDatabaseDetail
        * show dhcp-server-tracking database detail
        * show dhcp-server-tracking database vlan {vlan_id} detail

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* ios
    * Modified ShowInventory
        * Accept inventory records whose NAME field is empty.
        * Initialize record context so a malformed orphan PID line is ignored instead of raising an unbound-local exception.

* iosxe
    * Modified ShowPlatformHardwareFedSwitchForwardLastSummary parser
        * Updated fields Optional.
    * Modified ShowMonitorCaptureBufferDetailed
        * Added support for parsing "request_frame" and "response_time"
    * Modified ShowIpInterface
        * Added support for parsing the optional ``(host-routing)`` suffix on the Local Proxy ARP status line.
        * Added the optional ``local_proxy_arp_host_routing`` field.
    * Added ShowPlatformHardwareFedSwitchQosQueueStatsInterface to C9400
        * Reused the C9610 VOQ/ASIC queue statistics parser for c9400 devices.
    * Modified ShowIpRouteSchema schema
        * Added optional vrf under next_hop.outgoing_interface.<interface>.
    * Modified ShowIpRoute parser
        * Updated parsing logic in the shared route parser: %vrf suffixes are now split from outgoing interface names and stored as vrf.
    * Modified ShowEnvironmentAll
        * Added support for C9400 output with optional power-supply summaries and table-based fantray states.
    * Added ShowPlatformSoftwareFedSwitchActiveAclInfoSdkDetail
        * Fix the regex to capture the asic number in the output of 'show platform software fed switch {switch_num} acl info sdk detail'
    * Fix ShowPlatformSoftwareFedQosInterfaceIngressNpd
        * Fix the regex to capture the port_oid and system_port_oid
    * ShowPlatformSoftwareFedQosInterfaceIngressSdkDetailed
        * Fix regex p7 to use (Asic|ASIC) to capture the asic number in the output of 'show platform software fed switch {switch_num} qos interface ingress sdk detailed'
    * ShowFlowMonitorCache
        * Added timeout optional variable with default value of 300 seconds
    * Modified ShowSdmPrefer
        * Updated the L3 Multicast entries regex to support the optional ``(Stats)`` label and numeric statistics annotation.
    * Modified ShowRouteMapAllSchema schema
        * Added support for ip tos and ipv6 precedence set clauses
    * Modified ShowRouteMapAll parser
        * REGEX logic update to match ip tos <value> and ipv6 precedence <value>
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressNpdDetailed
        * Added support for ACL ACE details that begin with ``Class id`` when the ``IPV4/IPv6 ACE Key/Mask`` marker is absent.
        * Prevented an ``UnboundLocalError`` while parsing this output format.
        * Added corresponding golden parser coverage.

* iosxr
    * Modified ShowVrfAllDetail
        * Modified regex <p4_1> to capture all interface names
            * Replaced the previous regex that relied on specific interface prefixes (e.g., Gi, Bun, Ten, etc.) with a more general pattern.
        * Introduced `in_interfaces_section` flag for accurate section tracking
    * Modified ShowControllersOpticsAppselAdvertised
        * Updated parser to revise the pattern to accept any non-pipe content in each table cell. This basically means to allow letters, digits, whitespace, parentheses, dots, hyphens, '/', comma etc

* nxos
    * Modified ShowNveInterfaceDetail
        * Added fabric_convergence_time, fabric_convergence_time_left, and multisite_fabric_advertise_pip_l3 keys to the schema.
        * Added regex patterns p27, p28, and p29 to parse Fabric convergence time, Fabric convergence time left, and Multisite fabric-advertise-pip l3 configured output.
