--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* iosxr
    * Added ShowBgpBrief
        * Added 'show bgp {address_family} {ip_address} brief'
    * Modified show_mpls
        * added 'ShowMplsLdpDiscoveryDetails'
    * Added ShowWatchdogMemoryState
        * show watchdog memory-state
        * show watchdog memory-state Location {location}
    * Added ShowVariablesBoot
        * show variables boot
    * Added ShowVariablesSystem
        * 'show variables system'
    * Modified show_bgp
        * Added 'ShowBgpAllAllNexthops'
    * Added ShowShmwinSummary
        * Add show shmwin summary command

* nxos
    * Added ShowIpMrouteSummaryVrfAll
        * added 'show ip mroute summary vrf all'
    * Added ShowSystemInternalKernelMeminfo
        * show system internal kernel meminfo
    * Added ShowSystemResources
        * added 'show system resources'

* iosxe
    * Modified ShowRunInterface
        * Added parsing support (schema and parsers) for following outputs
            * power inline port priority high
            * power inline static max 30000
            * spanning-tree bpdufilter enable
            * ip flow monitor IPv4NETFLOW input
            * switchport protected
            * switchport block unicast
            * switchport block multicast
            * switchport trunk allowed vlan 820,900-905
            * ip dhcp snooping trust
            * ip arp inspection trust
    * Added ShowIpDhcpSnoopingDatabase
        * show ip dhcp snooping database
    * Added ShowIpDhcpSnoopingDatabaseDetail
        * show ip dhcp snooping database detail
    * Modified ShowStackPower
        * show stack-power budgeting
        * Added keys and regexes to incorporate a new cli_command
    * Added ShowPowerInlinePriority
        * show power inline priority
        * show power inline priority {interface}
    * Added ShowPowerInlineUpoePlus
        * show power inline upoe-plus
        * show power inline upoe-plus {interface}
    * Added ShowL2vpnEvpnEthernetSegment
        * show l2vpn evpn ethernet-segment
    * Added ShowL2vpnEvpnEthernetSegmentDetail
        * show l2vpn evpn ethernet-segment detail
        * show l2vpn evpn ethernet-segment interface {id} detail
    * Added ShowDeviceTrackingCountersInterface
    * Added ShowDeviceTracking
        * show device-tracking features
        * show device-tracking events
    * Added ShowIpv6
        * show ipv6 dhcp guard policy {policy name}
        * show flooding-suppression policy {policy name}
    * Added ShowDeviceTracking
        * show device-tracking database details
        * show device-tracking policy {policy_name}
        * show device-tracking counters vlan {vlanid}
    * Added ShowIpv6
        * show ipv6 nd raguard policy {policy_name}
        * show ipv6 source-guard policy {policy_name}
    * Modified ShowMplsLdp
        * Added ShowMplsLdpParameters
    * Added Parser
        * For "show sdwan tunnel sla index 0"
    * Added ShowL2fibPathListId
        * show l2fib path-list {id}
        * show l2fib path-list detail
    * Added ShowL2routeEvpnMacIpDetail
        * show l2route evpn mac ip detail
        * show l2route evpn mac ip host-ip <ip> detail
        * show l2route evpn mac ip host-ip <ip> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> mac-address <mac_addr> detail
        * show l2route evpn mac ip host-ip <ip> mac-address <mac_addr> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> next-hop <next_hop> detail
        * show l2route evpn mac ip host-ip <ip> next-hop <next_hop> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> next-hop <next_hop> mac-address <mac_addr> detail
        * show l2route evpn mac ip host-ip <ip> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> producer <producer> mac-address <mac_addr> detail
        * show l2route evpn mac ip host-ip <ip> producer <producer> mac-address <mac_addr> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> mac-address <mac_addr> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> mac-address <mac_addr> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> mac-address <mac_addr> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> producer <producer> mac-address <mac_addr> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> producer <producer> mac-address <mac_addr> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> mac-address <mac_addr> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> mac-address <mac_addr> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> next-hop <next_hop> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> next-hop <next_hop> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> next-hop <next_hop> mac-address <mac_addr> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> producer <producer> mac-address <mac_addr> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> producer <producer> mac-address <mac_addr> esi <esi> detail
    * Added ShowNvePeers
        * 'show nve peers'
        * 'show nve peers interface nve {nve}'
        * 'show nve peers peer-ip {peer_ip}'
        * 'show nve peers vni {vni}'
    * Added ShowPlatformSoftwareFedactiveFnfEtAnalyticsFlows
        * 'show platform software fed active fnf et-analytics-flows'
    * Added ShowL2vpnEvpnMacIp
        * show l2vpn evpn mac ip
        * show l2vpn evpn mac ip address {ipv4_addr}
        * show l2vpn evpn mac ip address {ipv6_addr}
        * show l2vpn evpn mac ip bridge-domain {bd_id}
        * show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv4_addr}
        * show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv6_addr}
        * show l2vpn evpn mac ip bridge-domain {bd_id} duplicate
        * show l2vpn evpn mac ip bridge-domain {bd_id} local
        * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr}
        * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv4_addr}
        * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv6_addr}
        * show l2vpn evpn mac ip bridge-domain {bd_id} remote
        * show l2vpn evpn mac ip duplicate
        * show l2vpn evpn mac ip evi {evi_id}
        * show l2vpn evpn mac ip evi {evi_id} address {ipv4_addr}
        * show l2vpn evpn mac ip evi {evi_id} address {ipv6_addr}
        * show l2vpn evpn mac ip evi {evi_id} duplicate
        * show l2vpn evpn mac ip evi {evi_id} local
        * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr}
        * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv4_addr}
        * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv6_addr}
        * show l2vpn evpn mac ip evi {evi_id} remote
        * show l2vpn evpn mac ip local
        * show l2vpn evpn mac ip mac {mac_addr}
        * show l2vpn evpn mac ip mac {mac_addr} address {ipv4_addr}
        * show l2vpn evpn mac ip mac {mac_addr} address {ipv6_addr}
        * show l2vpn evpn mac ip remote
    * Added ShowL2vpnEvpnMacIpDetail
        * show l2vpn evpn mac ip address {ipv4_addr} detail
        * show l2vpn evpn mac ip address {ipv6_addr} detail
        * show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv4_addr}  detail
        * show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv6_addr} detail
        * show l2vpn evpn mac ip bridge-domain {bd_id} detail
        * show l2vpn evpn mac ip bridge-domain {bd_id} duplicate detail
        * show l2vpn evpn mac ip bridge-domain {bd_id} local detail
        * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv4_addr} detail
        * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv6_addr} detail
        * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} detail
        * show l2vpn evpn mac ip bridge-domain {bd_id} remote detail
        * show l2vpn evpn mac ip detail
        * show l2vpn evpn mac ip duplicate detail
        * show l2vpn evpn mac ip evi {evi_id} address {ipv4_addr} detail
        * show l2vpn evpn mac ip evi {evi_id} address {ipv6_addr} detail
        * show l2vpn evpn mac ip evi {evi_id} detail
        * show l2vpn evpn mac ip evi {evi_id} duplicate detail
        * show l2vpn evpn mac ip evi {evi_id} local detail
        * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv4_addr} detail
        * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv6_addr} detail
        * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} detail
        * show l2vpn evpn mac ip evi {evi_id} remote detail
        * show l2vpn evpn mac ip local detail
        * show l2vpn evpn mac ip mac {mac_addr} address {ipv4_addr} detail
        * show l2vpn evpn mac ip mac {mac_addr} address {ipv6_addr} detail
        * show l2vpn evpn mac ip mac {mac_addr} detail
        * show l2vpn evpn mac ip remote detail
    * Added ShowL2vpnEvpnMacIpSummary
        * show l2vpn evpn mac ip bridge-domain {bd_id} duplicate summary
        * show l2vpn evpn mac ip bridge-domain {bd_id} local summary
        * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} summary
        * show l2vpn evpn mac ip bridge-domain {bd_id} remote summary
        * show l2vpn evpn mac ip bridge-domain {bd_id} summary
        * show l2vpn evpn mac ip duplicate summary
        * show l2vpn evpn mac ip evi {evi_id} duplicate summary
        * show l2vpn evpn mac ip evi {evi_id} local summary
        * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} summary
        * show l2vpn evpn mac ip evi {evi_id} remote summary
        * show l2vpn evpn mac ip evi {evi_id} summary
        * show l2vpn evpn mac ip local summary
        * show l2vpn evpn mac ip mac {mac_addr} summary
        * show l2vpn evpn mac ip remote summary
        * show l2vpn evpn mac ip summary
    * Modified ShowL2vpnEvpnMac
        * show l2vpn evpn mac
        * show l2vpn evpn mac address {mac_addr}
        * show l2vpn evpn mac bridge-domain {bd_id}
        * show l2vpn evpn mac bridge-domain {bd_id} address {mac_addr}
        * show l2vpn evpn mac bridge-domain {bd_id} duplicate
        * show l2vpn evpn mac bridge-domain {bd_id} local
        * show l2vpn evpn mac bridge-domain {bd_id} remote
        * show l2vpn evpn mac duplicate
        * show l2vpn evpn mac evi {evi_id}
        * show l2vpn evpn mac evi {evi_id} address {mac_addr}
        * show l2vpn evpn mac evi {evi_id} duplicate
        * show l2vpn evpn mac evi {evi_id} local
        * show l2vpn evpn mac evi {evi_id} remote
        * show l2vpn evpn mac local
        * show l2vpn evpn mac remote
    * Modified ShowL2vpnEvpnMacDetail
        * show l2vpn evpn mac address {mac_addr} detail
        * show l2vpn evpn mac bridge-domain {bd_id} address {mac_addr} detail
        * show l2vpn evpn mac bridge-domain {bd_id} detail
        * show l2vpn evpn mac bridge-domain {bd_id} duplicate detail
        * show l2vpn evpn mac bridge-domain {bd_id} local detail
        * show l2vpn evpn mac bridge-domain {bd_id} remote detail
        * show l2vpn evpn mac detail
        * show l2vpn evpn mac duplicate detail
        * show l2vpn evpn mac evi {evi_id} address {mac_addr} detail
        * show l2vpn evpn mac evi {evi_id} detail
        * show l2vpn evpn mac evi {evi_id} duplicate detail
        * show l2vpn evpn mac evi {evi_id} local detail
        * show l2vpn evpn mac evi {evi_id} remote detail
        * show l2vpn evpn mac local detail
        * show l2vpn evpn mac remote detail
    * Added ShowL2vpnEvpnMac
        * show l2vpn evpn mac
        * show l2vpn evpn mac address {mac_addr}
        * show l2vpn evpn mac bridge-domain {bd_id}
        * show l2vpn evpn mac bridge-domain {bd_id} address {mac_addr}
        * show l2vpn evpn mac bridge-domain {bd_id} duplicate
        * show l2vpn evpn mac bridge-domain {bd_id} local
        * show l2vpn evpn mac bridge-domain {bd_id} remote
        * show l2vpn evpn mac duplicate
        * show l2vpn evpn mac evi {evi_id}
        * show l2vpn evpn mac evi {evi_id} address {mac_addr}
        * show l2vpn evpn mac evi {evi_id} duplicate
        * show l2vpn evpn mac evi {evi_id} local
        * show l2vpn evpn mac evi {evi_id} remote
        * show l2vpn evpn mac local
        * show l2vpn evpn mac remote
    * Added ShowL2vpnEvpnMacDetail
        * show l2vpn evpn mac address {mac_addr} detail
        * show l2vpn evpn mac bridge-domain {bd_id} address {mac_addr} detail
        * show l2vpn evpn mac bridge-domain {bd_id} detail
        * show l2vpn evpn mac bridge-domain {bd_id} duplicate detail
        * show l2vpn evpn mac bridge-domain {bd_id} local detail
        * show l2vpn evpn mac bridge-domain {bd_id} remote detail
        * show l2vpn evpn mac detail
        * show l2vpn evpn mac duplicate detail
        * show l2vpn evpn mac evi {evi_id} address {mac_addr} detail
        * show l2vpn evpn mac evi {evi_id} detail
        * show l2vpn evpn mac evi {evi_id} duplicate detail
        * show l2vpn evpn mac evi {evi_id} local detail
        * show l2vpn evpn mac evi {evi_id} remote detail
        * show l2vpn evpn mac local detail
        * show l2vpn evpn mac remote detail
    * Added ShowL2vpnEvpnMacSummary
        * show l2vpn evpn mac bridge-domain {bd_id} duplicate summary
        * show l2vpn evpn mac bridge-domain {bd_id} local summary
        * show l2vpn evpn mac bridge-domain {bd_id} remote summary
        * show l2vpn evpn mac bridge-domain {bd_id} summary
        * show l2vpn evpn mac duplicate summary
        * show l2vpn evpn mac evi {evi_id} duplicate summary
        * show l2vpn evpn mac evi {evi_id} local summary
        * show l2vpn evpn mac evi {evi_id} remote summary
        * show l2vpn evpn mac evi {evi_id} summary
        * show l2vpn evpn mac local summary
        * show l2vpn evpn mac remote summary
        * show l2vpn evpn mac summary


--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxr
    * Modified ShowRouteAllSummary
        * Fixed pattern p3 to accept routed source instances with '.'
    * Modified ShowPlatformi(show redundancy)
        * Added regex p3_2 to accomodate standby RP for eXR
    * Modified ShowOspfv3Neighbor
        * updated regex pattern p1 to handle hyphens in VRF name
    * Modified ShowRouteIpv4
        * updated regex pattern p6 to handle 'type' after 'candidate default path'
        * updated class to folder based unit tests
    * Modified ShowProcesses
        * Added Location data if not applicable
    * Modified ShowHsrpDetail
        * Updated regex pattern <p1> to accommodate various outputs.
        * Moved regexes outside of loop
    * Modified ShowHsrpSummary
        * Moved regexes outside of loop

* iosxe
    * Modified ShowRunInterface
        * Fixed channel_group (was not working).
            * Added channel_group to ShowRunInterfaceSchema
            * Updated intf_dict to make it work properly
    * Modified ShowPolicyMapTypeSuperParser
        * Added patterns p43..p47 for AFD WRED stats
    * Modified ShowEtherchannelSummary
        * Added regex pattern p6 to accommodate various port outputs.
    * Modified ShowDeviceTrackingDatabaseInterface
        * Made `limit` key optional on binding_table and refactored code to support this change.
    * Modified ShowStandbyAll
        * Optimized parser and fixed issue with multiple group numbers under same interface
    * Modified ShowDeviceTrackingCountersVlan
        * Fix parsing of faults
        * Fix parsing of dropped message to account for more cases
    * Modified ShowBgpDetailSuperParser
        * modified p10 to cover scenario where EVPN ESI is in output, but not paired with gateway address or local_vtep information
    * Modified ShowLispEidTableVrfIpv4Database
        * Changed key <User> to Any() in schema
    * Modified ShowStandbyAll
        * Updated regex pattern <p11> to accommodate various outputs.
        * Updated format of parser and moved regexes out of loop
    * Modified ShowStandbyInternal
        * Updated format of parser and moved regexes out of loop
    * Modified ShowStandbyDelay
        * Updated format of parser and moved regexes out of loop
    * Modified ShowWirelessClientMacDetail
        * rewrote parser for better stability
        * added missing argument to cli command
        * added new optional keys, made several keys in schema optional
        * some schema entries are now int or string
        * added new test to cover schema changes
    * Modified ShowPlatformSoftwareFed
        * Update regex P36 to include objidADJ SPECIAL0
        * Update regex P25 and corresponding schema to include bwalk parameters
        * Modify regex P11 and corresponding schema to modify flags and pdflags from str to
        * Modify regex P14 to include label_aal
        * Add blank lines and comments between regex
        * Add full syntax of commands
        * Modify capital letters to small letters in key name in Schema and parser class
        * Delete Optional Keyword in some of key names in Schema
        * Modify nobj0 and nobj1 from str to list in regex P9 and corresponding Schema
        * Add folder based unittests
    * Delete iosxe/show_platform_software_fed.py instead content is Appended in iosxe/show_platform.py
    * Modified ShowPlatformSoftwareYangManagementProcessState
        * Fixed pattern p1 to accept `Not Running` as valid state
        * Fixed patter p2 to accept `Down` and `Reset` as valid states

* nxos
    * Modified ShowInterface
        * Updated regex pattern <p1> to accommodate various outputs.
    * Modify ShowSpanningTreeDetail
        * Added schema key 'peer_type'
    * Modified ShowMacAddressTableBase
        * updated regex to handle NA for age value
        * added test golden_output_3 to test changes
    * Updated RunBashTop
        * updated p1 regex to support various output for uptime

* junos
    * Modified ShowRouteReceiveProtocolExtensive()
        * Modified Regex to also match IPv6 Nethops.
    * Modified ShowRouteReceiveProtocolPeerAddressExtensive()
        * Modified Regex to also match IPv6 Destinations.
        * Modified Regex to also match IPv6 Nexthops.


