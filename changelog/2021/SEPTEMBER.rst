--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareFedSwitchActiveIfmMappingsLpn to support
        * show platform software fed switch active ifm mappings lpn
        * show platform software fed switch active ifm mappings lpn {interface}
    * Added ShowPlatformSoftwareFedSwitchActivePtpDomain to support
        * show platform software fed switch active ptp domain
    * Added ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterface to support
        * show platform software fed switch active ptp Interface {interface}
    * Added ShowPlatformSoftwareFedActiveAclUsage to support
        * show platform software fed active acl usage
        * show platform software fed active acl usage | include {acl_name}
    * Modified ShowBgpDetailSuperParser
        * Fixed p3_3 match logic to allow multicast src to be * when the multicast src len is 0.
    * Modified ShowMplsTrafficEngTunnelBrief
        * Moved to 'show_mpls.py'
    * Modified ShowMplsTrafficEngTunnelTunnelid
        * Moved to 'show_mpls.py'
    * Modified ShowMplsTrafficEngTunnel
        * Moved to 'show_mpls.py'
    * Modified ShowBgpDetailSuperParser
        * Fixed p2 to allow for cases in show output that have same tableids in different locations.
    * Modified ShowAuthenticationSessionsInterfaceDetails
        * show authentication sessions interface {interface} details switch {switch} r0
    * Modified ShowSegmentRoutingTrafficEngPolicy
        * Fixed regex, added unit tests, and added to the schema
    * Modified ShowinterfacesStatus to support
        * show interfaces {interface} status
    * Added ShowPlatformSoftwareDpidIndex
        * show platform software dpidb index
    * Added ShowMplsTrafficEngTunnelBrief
        * Added ShowMplsTrafficEngTunnelBrief in IOSXE c9400 folder
        * Add folder based unittests
    * Modified ShowEnvironmentAll
        * subclass of ShowEnvironmentSuperParser
    * Modified ShowPlatformSoftwareFedActiveAclUsage to support
        * show platform software fed active acl usage
        * show platform software fed active acl usage | include {acl_name}
    * Modified ShowIpRouteSummary
        * Added parsing support for devices that don't record 'Replicates' in the routing table
    * Modified ShowRouteMapAll to support
        * show route-map {name}
    * Modified ShowLicenseSummary
        * Updtaed regex pattern for <license> capturing group to accommodate various outputs
    * Modified ShowRomVarSchema
        * Changed mcp_startup_traceflags field to Optional
    * Modified ShowRomVar
        * Added other  keyword CRYPTO_BI_THPUT for thrput parameter
    * Modified ShowVersion
        * Fixed regex for capturing correct build_label, added unit tests,
    * Modified ShowIpv6Route
        * Fixed p6 match logic to allow % in case of leaked route in current vrf table.
    * Modified ShowIpRoute
        * Fixed p3 match logic for Ipv6 and Ipv6 to properly parse code 1 (in cases such as replicated routes or additional codes). Ipv6 routes now properly parsed as well
    * Modified ShowMonitor
        * Made the status key optional.
    * Modified ShowMplsForwardingTable
        * Fixed code logic
    * Modified  ShowLicenseSummary
        * modified regex pattern to support other types of licenses
    * Modified ShowStackPower
        * Modified multiple schema keys to accept either float or int data types
    * Added ShowStackPowerBudgeting
        * show stack-power budgeting
    * Modified ShowL2routeEvpnMacIp
        * Updated logic for the order of specific filter use
        * Added show l2route evpn mac ip host-ip {ip}
        * Updated Schemas in show_l2route.py to use evi, mac addr and etag as keys
        * Added support to all allow all classes in show_l2route to support multiple next hops
        * Updated function arguments to allow evi and etag to be passed in as one argument, evi_etag
        * Added support for long ipv6 addresses for all show_l2route parsers
        * Added and updated tests
    * Modified ShowL2routeEvpnMacIpDetail
        * Added and updated tests
        * Updated Schemas to use evi, mac addr and etag as keys. NOT BACKWARDS COMPATIBLE.
        * Updated function arguments to allow evi and etag to be passed in as one argument, evi_etag
            * show l2route evpn mac ip topology <evi_etag> detail
            * Updated logic for the specific filter use
    * Modified ShowL2routeEvpnImetDetail
        * Added and updated tests
        * Updated function arguments to allow evi and etag to be passed in as one argument, evi_etag
            * show l2route evpn imet topology {evi_etag} detail
            * Updated logic for the specific filter use
        * Updated Schemas to use evi, mac addr and etag as keys. NOT BACKWARDS COMPATIBLE.
    * Modified ShowBgpNeighborsReceivedRoutesSuperParser
        * Made neighbor_id and original_address_family have default values in parser class
    * Modified ShowDeviceTrackingPolicies
        * Removed a misplaced empty dictionary test from cli/equal test folder (raised SchemaEmptyParserError)
    * Added ShowPtpBrief to support
        * show ptp brief
        * show ptp brief | exclude {ptp_state}
    * Added ShowPtpClock to support
        * show ptp clock
    * Added ShowPtpParent to support
        * show ptp parent
    * Added ShowPtpPortInterface to support
        * show ptp port {interface}
    * Added new parser for 'show run all | sec {interface}'
    * Modified ShowBoot
        * Added regex to accommodate resolve corner case
    * Modified ShowL2vpnEvpnMac
        * changed schema to support vary outputs
            * added evi, eth_tag and bd_id as key
        * updated test cases
        * added cli filter and tests for vlan_id
            * show l2vpn evpn mac vlan {vlan_id}
            * show l2vpn evpn mac vlan {vlan_id} address {mac_addr}
            * show l2vpn evpn mac vlan {vlan_id} duplicate
            * show l2vpn evpn mac vlan {vlan_id} local
            * show l2vpn evpn mac vlan {vlan_id} remote
    * Modified ShowL2vpnEvpnMacIp
        * changed schema
            * added evi, mac_addr and bd_id as key
        * updated test cases
        * added cli filter and tests for vlan_id
            * show l2vpn evpn mac ip vlan {vlan_id}
            * show l2vpn evpn mac ip vlan {vlan_id} address {ipv4_addr}
            * show l2vpn evpn mac ip vlan {vlan_id} address {ipv6_addr}
            * show l2vpn evpn mac ip vlan {vlan_id} duplicate
            * show l2vpn evpn mac ip vlan {vlan_id} local
            * show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr}
            * show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr} address {ipv4_addr}
            * show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr} address {ipv6_addr}
            * show l2vpn evpn mac ip vlan {vlan_id} remote
    * Modified ShowL2vpnEvpnMacDetail
        * changed schema
            * added evi, eth_tag, mac_addr and bd_id as key
        * updated test cases
    * Modified ShowL2vpnEvpnMacIpDetail
        * changed schema
            * added evi, mac_addr, eth_tag and bd_id as key
        * updated test cases
    * Modified ShowL2fibPathListId
        * changed schema key 'path_ids' to 'pathlist_id'
        * updated tests
    * Modified ShowL2routeEvpnImetDetail
        * updated regex logic
        * updated testcase
    * Modified ShowL2fibPathListId
        * updated incorrect logic
    * Modified ShowL2routeEvpnMacIp
        * The c code has changed, the full length ipv6 addresses and next hop is now on the same line.
        * updated logic
        * updated test cases
    * Modified ShowFlowMonitorSdwanFlowMonitorStatistics
        * Added line.strip() and Optional("high_watermark")
    * Modified ShowVersion
        * Adding backspace to list of whitespace characters stripped from output lines

* viptela
    * Modified ShowSystemStatus
        * Add vManage storage options to schema as Optional.
        * Modified Optional cpu_allocation dict order to align with the device output.
        * Updated p1 regex to accomodate various single line output.
        * Updated p3 regex to accomodate for vManage/vController output and keep existing router output support.
        * Updated how p3/m3 dict group was parsed to build schema to support vManage along with existign router support.
        * Updated p7 and p8 to fix matching and parsing issues.
        * Fixed spacing within the conditional m8 business logic.
        * Added p9 and m9 to support the new vManage storage options Optional schema.
        * Updated comments throughout to be the same spacing/format.

* iosxr
    * Removed ShowL2VpnXconnectSummary
        * Class uses TCL and is replaced by ShowL2vpnXconnectSummary
    * Modified ShowControllersOptics
        * Added Optional key <fec_state> to schema
        * Added regex pattern <p4_1> to accommodate new <fec_state> schema key
        * Updated regex pattern <p3> to accommodate various outputs.
        * Updated regex pattern <p4> to accommodate various outputs.
        * Updated regex pattern <p40> to accommodate various outputs.
    * Modified ShowBgpInstanceNeighborsRoutesSchema
        * Modified key 'local_as' to capture dotted Notation ASN.
    * Modified ShowBgpInstanceNeighborsReceivedRoutesSchema
        * Modified key 'local_as' to capture dotted Notation ASN.
    * Modified ShowBgpInstanceNeighborsReceivedRoutes
        * Modified RegEx <p3>,<p13>,<p13_1>, (<m1><m2><m3>) under <p13>, <p17> to capture dotted Notation ASN in BGP
    * Modified ShowRouteIpv4
        * Handle nexthop without an outgoing interface
    * Modified ShowControllersFiaDiagshellL2showLocation
        * Remove extra bracket from regular expression
    * Modified ShowRSVPSession
        * Modified schema and changed respective parser logic
    * Modified ShowRSVPNeighbor
        * Replaced '-' with '_' in schema
    * Modified ShowRSVPGracefulRestartNeighbors
        * Replaced '-' with '_' in schema

* nxos/aci
    * Add parser for `ls -l` command

* utils
    * Modified unittest.py
        * Changed from json.dumps() to format_output() for showing parsed output
    * Modified Common.convert_intf_name
        * Added Fi and Fiv for FiveGigabitEthernet

* nxos
    * Modified ShowVxlan
        * Added new patterns ShowL2routeMacAllDetail.
        * Updated regex pattern to validate new ESI outputs.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* viptela
    * Created ShowOmpRoutes
        * Added ShowOmpRoutesSchema
        * Added ShowOmpRoutes parser
            * Added p1 and p2 regex pattern to match OMP routes table
            * Added conditional to handle variants of omp routes command that yields same output

* iosxe
    * Created ShowSdwanOmpRoutes
        * Added ShowSdwanOmpRoutes
        * Added unit test
    * Added ShowL2routeEvpnDGW
        * show l2route evpn default-gateway
        * show l2route evpn default-gateway host-ip {ip}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} mac-address {macaddr}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} mac-address {macaddr}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} mac-address {macaddr}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} {macaddr} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} producer {prod}
        * show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop}
        * show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} mac-address {macaddr}
        * show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} producer {prod} mac-address {macaddr}
        * show l2route evpn default-gateway host-ip {ip} producer {prod} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} producer {prod} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} next-hop {next_hop}
        * show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} mac-address {macaddr}
        * show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} mac-address {macaddr}
        * show l2route evpn default-gateway host-ip {ip} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} esi {esi}
        * show l2route evpn default-gateway topology {evi_etag}
        * show l2route evpn default-gateway topology {evi_etag} producer {prod}
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop}
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr}
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} esi {esi}
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} mac-address {macaddr}
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} esi {esi}
        * show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop}
        * show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} mac-address {macaddr}
        * show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} esi {esi}
        * show l2route evpn default-gateway topology {evi_etag} mac-address {macaddr}
        * show l2route evpn default-gateway topology {evi_etag} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway topology {evi_etag} esi {esi}
        * show l2route evpn default-gateway producer {prod}
        * show l2route evpn default-gateway producer {prod} next-hop {next_hop}
        * show l2route evpn default-gateway producer {prod} next-hop {next_hop} mac-address {macaddr}
        * show l2route evpn default-gateway producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway producer {prod} next-hop {next_hop} esi {esi}
        * show l2route evpn default-gateway producer {prod} mac-address {macaddr}
        * show l2route evpn default-gateway producer {prod} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway producer {prod} esi {esi}
        * show l2route evpn default-gateway next-hop {next_hop}
        * show l2route evpn default-gateway next-hop {next_hop} mac-address {macaddr}
        * show l2route evpn default-gateway next-hop {next_hop} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway next-hop {next_hop} esi {esi}
        * show l2route evpn default-gateway mac-address {macaddr}
        * show l2route evpn default-gateway mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway esi {esi}
    * Added ShowL2routeEvpnDGWDetail
        * show l2route evpn default-gateway detail
        * show l2route evpn default-gateway host-ip {ip} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} mac-address {macaddr} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} mac-address {macaddr} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} mac-address {macaddr} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} {macaddr} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} producer {prod} detail
        * show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} detail
        * show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} mac-address {macaddr} detail
        * show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} producer {prod} mac-address {macaddr} detail
        * show l2route evpn default-gateway host-ip {ip} producer {prod} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} producer {prod} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} detail
        * show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} mac-address {macaddr} detail
        * show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} mac-address {macaddr} detail
        * show l2route evpn default-gateway host-ip {ip} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} esi {esi} detail
        * show l2route evpn default-gateway topology {evi_etag} detail
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} detail
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} detail
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} detail
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} esi {esi} detail
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} mac-address {macaddr} detail
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} esi {esi} detail
        * show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} detail
        * show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} mac-address {macaddr} detail
        * show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} esi {esi} detail
        * show l2route evpn default-gateway topology {evi_etag} mac-address {macaddr} detail
        * show l2route evpn default-gateway topology {evi_etag} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway topology {evi_etag} esi {esi} detail
        * show l2route evpn default-gateway producer {prod} detail
        * show l2route evpn default-gateway producer {prod} next-hop {next_hop} detail
        * show l2route evpn default-gateway producer {prod} next-hop {next_hop} mac-address {macaddr} detail
        * show l2route evpn default-gateway producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway producer {prod} next-hop {next_hop} esi {esi} detail
        * show l2route evpn default-gateway producer {prod} mac-address {macaddr} detail
        * show l2route evpn default-gateway producer {prod} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway producer {prod} esi {esi} detail
        * show l2route evpn default-gateway next-hop {next_hop} detail
        * show l2route evpn default-gateway next-hop {next_hop} mac-address {macaddr} detail
        * show l2route evpn default-gateway next-hop {next_hop} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway next-hop {next_hop} esi {esi} detail
        * show l2route evpn default-gateway mac-address {macaddr} detail
        * show l2route evpn default-gateway mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway esi {esi} detail
    * Added ShowL2routeEvpnPeers
        * show l2route evpn peers
        * show l2route evpn peers topology {evi_etag}
        * show l2route evpn peers topology {evi_etag} peer-ip {peer_ip}
        * show l2route evpn peers peer-ip {peer_ip}
    * Added ShowL2routeEvpnPeersDetail
        * show l2route evpn peers detail
        * show l2route evpn peers topology {evi_etag} detail
        * show l2route evpn peers topology {evi_etag} peer-ip {peer_ip} detail
        * show l2route evpn peers peer-ip {peer_ip} detail
    * Added ShowAuthenticationSessionsDetailsSuperSchema
        * show authentication sessions interface {interface} details
        * show authentication sessions interface {interface} details switch {switch} r0
        * show authentication sessions mac {mac_address} details
        * show authentication sessions mac {mac_address} details switch {switch} r0
    * Added ShowAuthenticationSessionsDetailsSuperParser
        * show authentication sessions interface {interface} details
        * show authentication sessions interface {interface} details switch {switch} r0
        * show authentication sessions mac {mac_address} details
        * show authentication sessions mac {mac_address} details switch {switch} r0
    * Added ShowAuthenticationSessionsMACDetails
        * show authentication sessions mac {mac_address} details
        * show authentication sessions mac {mac_address} details switch {switch} r0
    * Added ShowLispDynamicEid
        * Added 'show lisp {lisp_id} instance-id {instance_id} dynamic-eid'
        * Added 'show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid'
        * Added 'show lisp instance-id {instance_id} dynamic-eid'
        * Added 'show lisp eid-table {eid_table} dynamic-eid'
        * Added 'show lisp eid-table vrf {vrf} dynamic-eid'
        * Added 'show lisp eid-table vlan {vlan} dynamic-eid'
    * Added ShowLispDynamicEidAllDetail
        * Added 'show lisp {lisp_id} instance-id {instance_id} dynamic-eid detail'
        * Added 'show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid detail'
        * Added 'show lisp instance-id {instance_id} dynamic-eid detail'
        * Added 'show lisp eid-table {eid_table} dynamic-eid detail'
        * Added 'show lisp eid-table vrf {vrf} dynamic-eid detail'
        * Added 'show lisp eid-table vlan {vlan} dynamic-eid detail'
    * Added ShowEnvironmentSuperParser
        * 'show env all'
        * 'show env fan'
        * 'show env power'
        * 'show env power all'
        * 'show env rps'
        * 'show env stack'
        * 'show env temperature'
        * 'show env temperature status'
        * 'show environment all'
    * Added ShowEnvAll
        * 'show env all'
    * Added ShowEnvFan
        * 'show env fan'
    * Added ShowEnvPower
        * 'show env power'
    * Added ShowEnvPowerAll
        * 'show env power all'
    * Added ShowEnvRPS
        * 'show env rps'
    * Added ShowEnvStack
        * 'show env stack'
    * Added ShowEnvTemperature
        * 'show env temperature'
    * Added ShowEnvTemperatureStatus
        * 'show env temperature status'
    * Added ShowPlatformSoftware under c9600
        * for 'show platform software object-manager {serviceprocessor} statistics'
        * for 'show platform software object-manager switch {switchvirtualstate} {serviceprocessor} statistics'
    * Added ShowInterfacesStatusErrDisabled
        * show interfaces status err-disabled
    * Added ShowTemplateBindingTarget
        * show template binding target {interface}
    * Added ShowLispDynamicEidSummary
        * Added 'show lisp {lisp_id} instance-id {instance_id} dynamic-eid summary'
        * Added 'show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid summary'
        * Added 'show lisp instance-id {instance_id} dynamic-eid summary'
        * Added 'show lisp eid-table vrf {vrf} dynamic-eid summary'
        * Added 'show lisp eid-table vlan {vlan} dynamic-eid summary'
        * Added 'show lisp eid-table {eid_table} dynamic-eid summary'
        * Added 'show lisp all instance-id * dynamic-eid summary'
    * Added ShowPlatformSoftwareFedactiveAclCountersHardware
        * 'show platform software fed active acl counters hardware'
    * Added ShowLicenseRumIdAll
        * show license rum id all
    * Added new parser for 'show platform software fed active inject packet-capture detailed'
    * Added new parser for 'show ip dhcp snooping binding'
    * Added ShowNetconfYangDatastores
        * show netconf-yang datastores
    * Added ShowNetconfYangStatus
        * show netconf-yang status
    * Modified ShowBgpNeighborsReceivedRoutes
        * 'show bgp {address_family} vrf {vrf} neighbors {neighbor} received-routes'
    * Added ShowCtsInterface for
        * show cts interface
    * Added ShowIpIgmpSnoopingGroups for
        * show ip igmp snooping groups
    * Added ShowIpIgmpSnoopingMrouter for
        * show ip igmp snooping mrouter
    * Added ShowIpIgmpSnoopingQuerier for
        * show ip igmp snooping querier
    * Added ShowMacsecSummary for
        * show macsec summary
    * Added ShowMacroAutoInterface for
        * show macro auto interface
    * Added ShowGlbpBrief for
        * show glbp brief
    * Added ShowL2routeEvpnMacDetail
        * show l2route evpn mac detail
        * show l2route evpn mac esi {esi} detail
        * show l2route evpn mac mac-address {mac_addr} detail
        * show l2route evpn mac mac-address {mac_addr} esi {esi} detail
        * show l2route evpn mac next-hop {next_hop} detail
        * show l2route evpn mac next-hop {next_hop} esi {esi} detail
        * show l2route evpn mac next-hop {next_hop} mac-address {mac_addr} detail
        * show l2route evpn mac next-hop {next_hop} mac-address {mac_addr} esi {esi} detail
        * show l2route evpn mac producer {producer} detail
        * show l2route evpn mac producer {producer} esi {esi} detail
        * show l2route evpn mac producer {producer} mac-address {mac_addr} detail
        * show l2route evpn mac producer {producer} mac-address {mac_addr} esi {esi} detail
        * show l2route evpn mac producer {producer} next-hop {next_hop} detail
        * show l2route evpn mac producer {producer} next-hop {next_hop} esi {esi} detail
        * show l2route evpn mac producer {producer} next-hop {next_hop} mac-address {mac_addr} detail
        * show l2route evpn mac producer {producer} next-hop {next_hop} mac-address {mac_addr} esi {esi} detail
        * show l2route evpn mac topology {evi_etag} detail
        * show l2route evpn mac topology {evi_etag} esi {esi} detail
        * show l2route evpn mac topology {evi_etag} mac-address {mac_addr} detail
        * show l2route evpn mac topology {evi_etag} mac-address {mac_addr} esi {esi} detail
        * show l2route evpn mac topology {evi_etag} next-hop {next_hop} detail
        * show l2route evpn mac topology {evi_etag} next-hop {next_hop} esi {esi} detail
        * show l2route evpn mac topology {evi_etag} next-hop {next_hop} mac-address {mac_addr} detail
        * show l2route evpn mac topology {evi_etag} next-hop {next_hop} mac-address {mac_addr} esi {esi} detail
        * show l2route evpn mac topology {evi_etag} producer {producer} mac-address {mac_addr} detail
        * show l2route evpn mac topology {evi_etag} producer {producer} mac-address {mac_addr} esi {esi} detail
    * Added ShowL2routeEvpnMac
        * show l2route evpn mac
        * show l2route evpn mac esi {esi}
        * show l2route evpn mac mac-address {mac_addr}
        * show l2route evpn mac mac-address {mac_addr} esi {esi}
        * show l2route evpn mac next-hop {next_hop}
        * show l2route evpn mac next-hop {next_hop} esi {esi}
        * show l2route evpn mac next-hop {next_hop} mac-address {mac_addr}
        * show l2route evpn mac next-hop {next_hop} mac-address {mac_addr} esi {esi}
        * show l2route evpn mac producer {producer}
        * show l2route evpn mac producer {producer} esi {esi}
        * show l2route evpn mac producer {producer} mac-address {mac_addr}
        * show l2route evpn mac producer {producer} mac-address {mac_addr} esi {esi}
        * show l2route evpn mac producer {producer} next-hop {next_hop}
        * show l2route evpn mac producer {producer} next-hop {next_hop} esi {esi}
        * show l2route evpn mac producer {producer} next-hop {next_hop} mac-address {mac_addr}
        * show l2route evpn mac producer {producer} next-hop {next_hop} mac-address {mac_addr} esi {esi}
        * show l2route evpn mac topology {evi_etag}
        * show l2route evpn mac topology {evi_etag} esi {esi}
        * show l2route evpn mac topology {evi_etag} mac-address {mac_addr}
        * show l2route evpn mac topology {evi_etag} mac-address {mac_addr} esi {esi}
        * show l2route evpn mac topology {evi_etag} next-hop {next_hop}
        * show l2route evpn mac topology {evi_etag} next-hop {next_hop} esi {esi}
        * show l2route evpn mac topology {evi_etag} next-hop {next_hop} mac-address {mac_addr}
        * show l2route evpn mac topology {evi_etag} next-hop {next_hop} mac-address {mac_addr} esi {esi}
        * show l2route evpn mac topology {evi_etag} producer {producer} mac-address {mac_addr}
        * show l2route evpn mac topology {evi_etag} producer {producer} mac-address {mac_addr} esi {esi}

* junos
    * Added ShowSecurityPoliciesHitCount
        * show security policies hit-count

* iosxr
    * Added ShowMplsTrafficEngTunnelsTabular
        * show mpls traffic-eng tunnels tabular
    * Added ShowMplsTrafficEngTunnelsTunnelid
        * Added show mpls traffic-eng tunnels {tunnel_id}
    * Added ShowRSVPSession
        * Added 'show rsvp session'
        * Added 'show rsvp session destination {ipaddress}'
    * Added ShowRSVPNeighbor
        * Added 'show rsvp neighbor'
    * Added ShowRSVPGracefulRestartNeighbors
        * Added 'show rsvp graceful-restart neighbors'
    * Added MonitorInterfaceInterface
        * Added 'monitor interface {interface}'
    * Added ShowRSVPGracefulRestartNeighborsDetail
        * Added 'show rsvp graceful-restart neighbors detail'
    * Added ShowRSVPSessionDetail
        * Added 'show rsvp session detail'
        * Added 'show rsvp session destination {ip_address} detail dst-port {tunnel_id}'

* nxos
    * Added ShowTrack
        * show track
        * show track {id}
        * show track brief

* utils
    * Modified common.py
        * Added telemetry data collection within get_parser()


