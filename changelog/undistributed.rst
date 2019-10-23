* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |


* Removed type `EUI` from the following show commands under IOSXR:
    * ShowL2routeEvpnMac
    * ShowL2routeEvpnMacIp
    * ShowL2vpnMacLearning
    * ShowEvpnEviMac
    * ShowControllersFiaDiagshellL2show

--------------------------------------------------------------------------------
                                CLNS
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowClnsProtocol tu support outputs without:
        * Interfaces
        * Manual area address
        * Routing for area address
    * Updated ShowClnsInterface to support more outputs        
    * Changed "type" type from string to integer on the following commands
        * 'show clns is-neighbors detail'
    * Saving type as string in schema on:
        * ShowClnsIsNeighborsDetail
    * Made some keys optionals in schema for ShowClnsTraffic
    * Saving as empty instance when instance not present in output on:
        * show clns protocol
    * Updates ShowIsisHostname to support outputs without hostnames
--------------------------------------------------------------------------------
                                Interface
--------------------------------------------------------------------------------
* NXOS
    * Update ShowInterfaceBrief
        * Add command 'show interface {interface} brief'
        * Rewrite parser for speed optimization
        * Change parsed interface name to be complete/whole interface name
    * Update ShowRunningConfigInterface
        * Update regex to support more interface names
        * Updated schema to support more outputs
* IOSXR
    * Update ShowIpv6VrfAllInterface
        * Update regex to avoid empty lines and command itself
    * Removed ShowInterfaceSwitchport for:
        * show interface switchport
    * Added parser for ShowInterfacesDescription
* IOSXE
    * Update ShowInterfaceAccounting
        * Change {intf} and argument 'intf' into {interface} and 'interface'
    * Added parser for ShowInterfacesDescription
* NXOS
    * Update ShowRunningConfigInterface:
        * Change {intf} and argument 'intf' into {interface} and 'interface'
    * Update ShowNveInterface:
        * Change {intf} and argument 'intf' into {interface} and 'interface'
    * Update ShowInterface
        * Fixed parser ShowInterface to match duplex and speed line
--------------------------------------------------------------------------------
                                EIGRP
--------------------------------------------------------------------------------
* IOS
        * Added ShowIpEigrpNeighbors for commands
                * 'show ip eigrp vrf {vrf} neighbors'
                * 'show ip eigrp neighbors'
        * Added ShowIpv6EigrpNeighbors for commands:
                * 'show ipv6 eigrp vrf {vrf} neighbors'
                * 'show ipv6 eigrp neighbors'
        * Added ShowIpEigrpNeighborsDetail for commands:
                * 'show ip eigrp neighbors detail'
                * 'show ip eigrp vrf {vrf} neighbors detail'
        * Added ShowIpv6EigrpNeighborsDetail for commands:
                * 'show ipv6 eigrp neighbors detail'

--------------------------------------------------------------------------------
                                MPLS
--------------------------------------------------------------------------------
* IOSXE
    * Update ShowMplsForwardingTable
        * Add command 'show mpls forwarding-table {prefix}'
        * update regex to support local label 'None'
        * update schema to support 'Merged' key
    * Update ShowMplsForwardingTableDetail
        * Add command 'show mpls forwarding-table labels {label} detail'
* IOSXR
    * Added ShowMplsLabelTableDetail for:
        'show mpls label table detail'

--------------------------------------------------------------------------------
                                Segment Routing
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowSegmentRoutingMplsConnectedPrefixSidMapLocal for:
        'show segment-routing mpls connected-prefix-sid-map local ipv4'
        'show segment-routing mpls connected-prefix-sid-map local ipv6'
    * Added ShowSegmentRoutingTrafficEngTopology for:
        'show segment-routing traffic-eng topology ipv4'
    * Added ShowSegmentRoutingTrafficEngPolicy for:
        'show segment-routing traffic-eng policy all'
        'show segment-routing traffic-eng policy name {name}'
    * Added ShowSegmentRoutingTrafficEngPolicyDetail for:
        'show segment-routing traffic-eng policy all detail'
        'show segment-routing traffic-eng policy name {name} detail'
    * Added ShowSegmentRoutingMplsMappingServer for:
        'show segment-routing mpls mapping-server ipv4'
        'show segment-routing mpls mapping-server ipv6'
    * Added ShowSegmentRoutingMplsLbAssignedSids for:
        'show segment-routing mpls lb assigned-sids'
    * Update ShowPceIPV4PeerPrefix
        * Removed typo from 'pcs' to 'pce' in show command

* IOSXR
    * Updated ShowPceIpv4TopologySummary:
        * Updated schema and add regex



--------------------------------------------------------------------------------
                              Controllers
--------------------------------------------------------------------------------
* IOSXR
    * Updated ShowControllersFiaDiagshellL2show:
        - renamed class to ShowControllersFiaDiagshellL2showLocation
        - modified regex
        - added schema
        - added unittest

--------------------------------------------------------------------------------
                                ISSU
--------------------------------------------------------------------------------
* IOS
    Added ShowIssuStateDetail for:
        * show issu state detail
    Added ShowIssuRollbackTimer for:
        * show issu rollback-timer

--------------------------------------------------------------------------------
                              Virtual-Service
--------------------------------------------------------------------------------
* NXOS
    * Added ShowVirtualServiceUtilization for "show virtual-service utilization name {name}"

--------------------------------------------------------------------------------
                                BGP
--------------------------------------------------------------------------------
* IOSXR
    * Updated ShowBgpVrfDbVrfAll:
        - modified regex
        - added schema
        - added unittest
    * Updated ShowBgpInstanceAllAll:
        - modified regex
        - added unittest
    * Updated ShowBgpL2vpnEvpnAdvertised:
        - modified regex
        - added schema
        - added unittest
    * Updated ShowBgpL2vpnEvpn for:
        added a schema and unittest, and updated based on the schema
    * Updated ShowBgpInstanceAllAll for address family regex issue
    * Updated ShowBgpL2vpnEvpn:
        * updated schema to support more output
        * Fixed parser logic when there is no path type available
    * Updated ShowBgpL2vpnEvpnAdvertised:
        * Fixed dict key values of type `set`
    * Added ShowBgpSessions for:
        * show bgp sessions
    * Added ShowBgpInstanceAllSessions for:
        * show bgp instance all sessions
    * Added ShowBgpInstanceSessions for:
        * show bgp instance {instance} sessions
    * Updated ShowBgpL2vpnEvpn to parse more varied output
    * Updated ShowL2vpnBridgeDomainDetail to parse more varied output
    * Updated ShowBgpL2vpnEvpn to parse more varied output

* IOS
    * Added ShowBgpSummary for:
        * show bgp summary
        * show bgp all summary
    * Added ShowIpBgp for:
        * show ip bgp

* IOSXE
    * Updated ShowBgpSuperParser for parsing of more varied output
    * Updated ShowIpBgp for parsing of more varied output
    * Updated ShowIpBgpNeighbors schema to support more varied output
    * Updated ShowBgpNeighborsAdvertisedRoutesSuperParser to parse more vrf value
    

--------------------------------------------------------------------------------
                                OSPF
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpOspfSegmentRoutingLocalBlock to add:
        * show ip ospf segment-routing local-block
    * Added ShowIpOspfDatabaseOpaqueAreaTypeExtLink for:
        * show ip ospf database opaque-area type ext-link
    * Added ShowIpOspfDatabaseOpaqueAreaTypeExtLinkSelfOriginate for:
        * show ip ospf database opaque-area type ext-link self-originate
    * Added ShowIpOspfDatabaseOpaqueAreaTypeExtLinkAdvRouter for:
        * show ip ospf database opaque-area type ext-link adv-router {address}
    * Updated ShowIpOspfDatabaseTypeParser to parse more varied output
    * Added ShowIpOspfSegmentRoutingAdjacencySid for:
        * show ip ospf segment-routing adjacency-sid
        * show ip ospf {process_id} segment-routing adjacency-sid
    * Updated ShowIpOspfInterface:
        * change {intf} and argument 'intf' into {interface} and 'interface'
    * Updated ShowIpOspfInterface:
        * added 'teapp' section to parse more varied output
* IOSXR
    * Updated ShowOspfVrfAllInclusiveInterface:
        * change {intf} and argument 'intf' into {interface} and 'interface'
    * Updated ShowOspfVrfAllInclusiveDatabaseOpaqueArea:
        * update schema and add regex
        * to support more varied tlv blocks
    * Updated ShowOspfMplsTrafficEngLink:
        * updated schema and regex
* NXOS
    * Updated ShowIpOspfMplsLdpInterface
        * add custom interface argument
    * Updated ShowIpOspfInterface
        * add custom interface argument
    * Updated ShowIpOspfNeighborDetail
        * added custom neighbor argument

--------------------------------------------------------------------------------
                                dot1x
--------------------------------------------------------------------------------
* IOSXE
    * removed tab, replace with space
        'show dot1x all statistics'

--------------------------------------------------------------------------------
                                PIM
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowRunningConfigPim:
        changed logic to support calling from device.parse
* IOSXR
    * Updated ShowPimVrfInterfaceDetail:
        For handling more varied output

--------------------------------------------------------------------------------
                                VRF
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowRunningConfigVrf:
        changed logic to support calling from device.parse

--------------------------------------------------------------------------------
                                common.py
--------------------------------------------------------------------------------
* updated _find_command to escape "^"
* disallow spaces in key "feature"

--------------------------------------------------------------------------------
                                MPLS
--------------------------------------------------------------------------------
* IOS
        * Added ShowIpMsdpSaCache for commands:
                * show ip msdp sa-cache
                * show ip msdb vrf {vrf} sa-cache
        * Added ShowIpMsdpPeer for commands:
                * show ip msdp peer
                * show ip msdp vrf {vrf} peer
* IOSXE
        * Update ShowMplsLdpNeighborDetail:
                * fix cli wrong command parser error
        * Update ShowMplsForwardingTable:
                * update regex to support more output pattern

--------------------------------------------------------------------------------
                                vlan
--------------------------------------------------------------------------------
* IOSXE
    * Fixed regex in ShowVlan
--------------------------------------------------------------------------------
                                FLOW
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowFlowMonitor for:
        * show flow monitor {name} cache format table
    * Added ShowFlowExporterStatistics for:
        * show flow exporter statistics
        * show flow exporter {exporter} statistics

--------------------------------------------------------------------------------
                                ROUTING
--------------------------------------------------------------------------------
* IOSXE
    * Update ShowIpCef
        * update regex to support outgoing_label_backup and outgoing_label_info
    * ShowIpRouteWord
        * update regex to support more varied output
* IOSXR
    * Updated ShowRouteIpv4:
        * Matching more routes
        * Optimized parser moving regex compilation out of for loop
    * Updated ShowStaticTopologyDetail:
        * Support more varied output
        * Update regex
    * Updated ShowRouteIpv6:
        * Updated logic and add regex to support varies output
* NXOS:
    * Updated ShowIpRoute for:
        * show ip route {route} {protocol} interface {interface} vrf {vrf}
        * show ip route {route} {protocol} interface {interface}
        * show ip route {protocol} interface {interface} vrf {vrf}
        * show ip route {route} interface {interface} vrf {vrf}
        * show ip route {route} {protocol}
        * show ip route {protocol} interface {interface}
        * show ip route {protocol} vrf {vrf}
        * show ip route {route} interface {interface}
        * show ip route {route} vrf {vrf}
        * show ip route interface {interface} vrf {vrf}
        * show ip route {protocol}
        * show ip route {route}
        * show ip route interface {interface}
        * show ip route vrf {vrf}
        * show ip route vrf all
        * show ip route
    * Updated ShowIpv6Route for:
        * show ipv6 route {route} {protocol} interface {interface} vrf {vrf}
        * show ipv6 route {route} {protocol} interface {interface}
        * show ipv6 route {protocol} interface {interface} vrf {vrf}
        * show ipv6 route {route} interface {interface} vrf {vrf}
        * show ipv6 route {route} {protocol}
        * show ipv6 route {protocol} interface {interface}
        * show ipv6 route {protocol} vrf {vrf}
        * show ipv6 route {route} interface {interface}
        * show ipv6 route {route} vrf {vrf}
        * show ipv6 route interface {interface} vrf {vrf}
        * show ipv6 route {protocol}
        * show ipv6 route {route}
        * show ipv6 route interface {interface}
        * show ipv6 route vrf {vrf}
        * show ipv6 route vrf all
        * show ipv6 route
        * Updated regex
    * Updated ShowRoutingVrfAll:
        * To match non-best routes

--------------------------------------------------------------------------------
                                INVENTORY
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowInventory:
        * Matching more slots
* IOS
    * Updated ShowInventory:
        * Matching more slots
* NXOS
    * Updated ShowInventory:
        * Matching more slots

--------------------------------------------------------------------------------
                                Spanning-tree
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowSpanningTreeSummary to:
        * regex to accommodate different formats
        * changed some fields in schema to Optional
    * Updated ShowSpanningTreeDetail to:
        * updated regex to accommodate more formats
        * add support for rstp
        * chnaged some fields in schema to Optional

--------------------------------------------------------------------------------
                                Spanning-Tree
--------------------------------------------------------------------------------
* IOSXE
    * Update ShowIpv6Neighbors
        * Add command 'show ipv6 neighbors {interface}'
        * Add command 'show ipv6 neighbors vrf {vrf} {interface}'
    * Update ShowIpv6Interface
        * Add 'suppress' key to schema
* NXOS
    * Update ShowIpv6MldInterfaceSchema
        * Added support for 'show ipv6 mld interface vrf all'

--------------------------------------------------------------------------------
                                CDP
--------------------------------------------------------------------------------
* IOS
    * Added ShowCdpNeighbors for command:
        * show cdp neighbors
        * show cdp neighbors detail

* IOSXR
    * Added ShowCdpNeighbors for command:
        * show cdp neighbors
        * show cdp neighbors detail

--------------------------------------------------------------------------------
                                Nd
--------------------------------------------------------------------------------
* NXOS
    * Update ShowIpv6NdInterface:
        * Add command 'show ipv6 nd interface {interface}'
        * Add command 'show ipv6 nd interface {interface} vrf {vrf}'
    * Update ShowIpv6IcmpNeighborDetail:
        * Add command 'show ipv6 icmp neighbor {interface} detail'
        * Add command 'show ipv6 icmp neighbor {interface} detail vrf {vrf}'

--------------------------------------------------------------------------------
                                Interface
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowRunningConfigNvOverlay for more varied output
    * Updated ShowNveInterfaceDetail:
        * Change {intf} and argument 'intf' into {interface} and 'interface'
    * Update ShowIpv6MldInterfaceSchema
        * Added support for 'show ipv6 mld interface vrf all'

--------------------------------------------------------------------------------
                                IPv6
--------------------------------------------------------------------------------
* IOSXR
    * Added ShowIpv6Neighbors for commands:
        * 'show ipv6 neighbors'
        * 'show ipv6 neighbors vrf {vrf}'
        * 'show ipv6 neighbors {interface}'
        * 'show ipv6 neighbors vrf {vrf} {interface}'
    * Updated ShowIpv6NeighborsDetail:
        * Added 'origin' key to schema

--------------------------------------------------------------------------------

                                Ethernet
--------------------------------------------------------------------------------
* IOS
    * Added ShowModule parse for Cat6k devices


--------------------------------------------------------------------------------
                                AUTHENTICATION
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowAuthenticationSessionsSchema:
        * Change {intf} in doc string into {interface}
    * Updated ShowAuthenticationSessions:
        * Change {intf} and argument 'intf' into {interface} and 'interface'
    * Updated ShowAuthenticationSessionsInterfaceDetailsSchema:
        * Change {intf} in doc string into {interface}
    * Updated ShowAuthenticationSessionsInterfaceDetails:
        * Change {intf} and argument 'intf' into {interface} and 'interface'

--------------------------------------------------------------------------------
                                FDB
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowMacAddressTableVni:
        * Change {intf} and argument 'intf' into {interface} and 'interface'
* IOSXR  
    * Added ShowEthernetCfmMeps for:
        * show ethernet cfm peer meps

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowRouteIpDistributor for commands;
        * 'show route vrf {vrf} ipv4'
        * 'show route ipv4'
        * 'show route ipv4 {route}'
        * 'show route ipv4 {protocol}'
        * 'show route vrf {vrf} ipv4 {protocol}'
        * 'show route vrf {vrf} ipv4 {route}'
    * Added ShowRouteIpv6Distributor for commands;
        * 'show route vrf {vrf} ipv6'
        * 'show route ipv6'
        * 'show route ipv6 {route}'
        * 'show route ipv6 {protocol}'
        * 'show route vrf {vrf} ipv6 {protocol}'
        * 'show route vrf {vrf} ipv6 {route}'

* IOSXR
    * Added ShowMsdpPeer, ShowMsdpContext, ShowMsdpSummary, ShowMsdpSaCache, ShowMsdpStatisticsPeer for commands:
        * 'show msdp peer'
        * 'show msdp vrf {vrf} peer'
        * 'show msdp context'
        * 'show msdp vrf {vrf} context'
        * 'show msdp summary'
        * 'show msdp vrf {vrf} summary'
        * 'show msdp sa-cache'
        * 'show msdp vrf {vrf} sa-cache'
        * 'show msdp statistics peer'
        * 'show msdp vrf {vrf} statistics peer'
    * Added ShowIgmp for commands;
        * 'show igmp interface'
        * 'show igmp interface {interface}'
        * 'show igmp vrf {vrf} interface'
        * 'show igmp vrf {vrf} interface {interface}'
        * 'show igmp summary'
        * 'show igmp vrf {vrf} summary'
        * 'show igmp groups detail'
        * 'show igmp vrf {vrf} groups detail'
		
--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXR
    * Enhanced ShowBgpInstanceNeighborsReceivedRoutes;
        * Updated code to support various outputs
        * Added unittest corresponding to the new supported output
    * Enhanced ShowBgpInstanceSummary;
        * Updated code to support various outputs
        * Added unittest corresponding to the new supported output
    * Enhanced ShowRouteIpv6:
        * Updated regex to support various outputs

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* NXOS
    * ShowIpOspf
        * Added missing keys to schema
        * Added regex to capture more outputs

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowAuthenticationSessions
        * Changed keyword to Optional
    * Updated ShowIpRoute for:
        * show ip route vrf {vrf} {protocol}
        * show ip route vrf {vrf}
        * show ip route {protocol}
        * show ip route
    * Updated ShowIpRouteWord for:
        * show ip route {route}
        * show ip route vrf {vrf} {route}
    * Updated ShowIpv6Route for:
        * show ipv6 route vrf {vrf} {protocol}
        * show ipv6 route vrf {vrf}
        * show ipv6 route {protocol}
        * show ipv6 route
    * Updated ShowIpv6RouteWord for:
        * show ipv6 route {route}
        * show ipv6 route vrf {vrf} {route}


    * Updated ShowIpOspfSegmentRoutingProtectedAdjacencies for:
        * changed backup_nexthop and backup_nexthop to optional

* IOSXR
    * Updated ShowBgpSessions
        * Updated regex to accommodate different formats


