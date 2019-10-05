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
    * Changed "type" type from string to integer on the following commands
        * 'show clns neighbors detail'
        * 'show clns is-neighbors detail'
--------------------------------------------------------------------------------
                                Interface
--------------------------------------------------------------------------------
* NXOS
    * Update ShowInterfaceBrief
        * Add command 'show interface {interface} brief'
    * Update ShowRunningConfigInterface
        * Update regex to support more interface names
        * Updated schema to support more outputs
* IOSXR
    * Update ShowIpv6VrfAllInterface
        * Update regex to avoid empty lines and command itself
* IOSXE
    * Update ShowInterfaceAccounting
        * Change {intf} and argument 'intf' into {interface} and 'interface'
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

* IOS
    * Added ShowBgpSummary for:
        * show bgp summary
        * show bgp all summary
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
* IOSXR
    * Updated ShowOspfVrfAllInclusiveInterface:
        * change {intf} and argument 'intf' into {interface} and 'interface'
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

--------------------------------------------------------------------------------
                                INVENTORY
--------------------------------------------------------------------------------
* IOS
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
                                VERSION
--------------------------------------------------------------------------------
* IOS
    * Optimization of ShowVersion moving regex compilation out of loop
* IOSXE
    * Optimization of ShowVersion moving regex compilation out of loop

--------------------------------------------------------------------------------
                                Routing
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpCef to parse outputs without routes
* IOSXR
    * Updated ShowL2routeTopology for:
        * show l2route topology
    * Updated ShowL2routeEvpnMacAll for:
        * show l2route evpn mac all
    * Updated ShowL2routeEvpnMacIpAll for:
        * show l2route evpn mac-ip all

--------------------------------------------------------------------------------
                                X-Connect
--------------------------------------------------------------------------------
* IOSXR
    * Added ShowL2vpnXconnectDetail for:
        * show l2vpn xconnect detail
    * Added ShowL2vpnXconnect for:
        * show l2vpn xconnect
    * Added ShowL2vpnXconnectSummary for:
        * show l2vpn xconnect summary
    * Added ShowL2vpnXconnectMp2mpDetail for:
        * show l2vpn xconnect mp2mp detail

--------------------------------------------------------------------------------
                                EVPN
--------------------------------------------------------------------------------
* IOSXR
    * Added ShowEvpnEvi for:
        * show evpn evi
    * Added ShowEvpnEviDetail for:
        * show evpn evi detail
* IOSXR:
    * Added ShowEvpnEthernetSegment for:
        * show evpn ethernet-segment
    * Added ShowEvpnEthernetSegmentDetail for:
        * show evpn ethernet-segment detail
    * Added ShowEvpnEthernetSegmentPrivate for:
        * show evpn ethernet-segment private
    * Added ShowEvpnEthernetSegmentEsiDetail for:
        * show evpn ethernet-segment esi {esi} detail

--------------------------------------------------------------------------------
                                Route
--------------------------------------------------------------------------------
* JUNOS
    * Updated ShowRouteTable for:
        * better matching of table name and parsing of more varied output

--------------------------------------------------------------------------------
                                TRACEROUTE
--------------------------------------------------------------------------------
* IOSXE
    * Updated Traceroute to support more output

--------------------------------------------------------------------------------
                                L2VPN
--------------------------------------------------------------------------------
* IOSXR
    * Added ShowL2vpnBridgeDomain for:
        * show l2vpn bridge-domain
    * Added ShowL2vpnMacLearning for:
        * show l2vpn mac-learning {mac_type} all location {location}
    * Added ShowL2vpnForwardingBridgeDomainMacAddress for:  
        * show l2vpn forwarding bridge-domain mac-address location {location}
        * show l2vpn forwarding bridge-domain {bridge_domain} mac-address location {location}
    * Added ShowL2vpnForwardingProtectionMainInterface for:  
        * show l2vpn forwarding protection main-interface location {location}

--------------------------------------------------------------------------------
                                MODULE
--------------------------------------------------------------------------------
* IOS
    * Changed schema for ShowModule for Cat6k platform to reflect ops

--------------------------------------------------------------------------------
                                LLDP
--------------------------------------------------------------------------------
* IOSXR
    * Fixed parser ShowLldpEntry to support different port descriptions

--------------------------------------------------------------------------------
                                NTP
--------------------------------------------------------------------------------
* IOSXR
    * Fixed parser ShowRunningConfigNtp to support different vrfs output

--------------------------------------------------------------------------------
                                ISIS
--------------------------------------------------------------------------------
* IOSXR
    * Fixed parser ShowRunRouterIsis to support different outputs
    * Added ShowIsisSegmentRoutingLabelTable for:
        * show isis segment-routing label table
    * Added parser ShowIsis for:
        * show isis
