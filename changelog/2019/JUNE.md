| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 19.6.0        |

-----------------------------------------------------------------------------
                                   Dot1x
-----------------------------------------------------------------------------
* NXOS
        * Added show_dot1x_Summary and modified show_dot1x_Statistics parsers
        * Added all_details and test_all_details & adressed show_dot1x comments
        * Modification to show_Dot1x schema and adressed show_dot1x comments
--------------------------------------------------------------------------------
                                   Routing
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowRoutingVrfAll
        * added show routing vrf {vrf} to support custom vrf
    * Updated ShowRoutingIpv6VrfAll
        * added show ipv6 routing vrf {vrf} to support custom vrf

--------------------------------------------------------------------------------
                                Interface
--------------------------------------------------------------------------------
* IOSXE
    * Fix ShowIpInterfaceBrief short name issue

----------------------------------------------------------------------------
                                   OSPF
----------------------------------------------------------------------------
* OSPF
        * Optimized parser by moving all regex outside of for loop
* IOSXE
    * Updated ShowIpOspfInterface to support command 'show ip ospf interface {interface}'
    * Updated ShowIpOspfNeighbor for:
        * show ip ospf neighbor {interface}
    * Enhanced ShowIpOspfMaxMetric to support different outputs
--------------------------------------------------------------------------------
                                policy-map
--------------------------------------------------------------------------------
* IOSXE
    * Fix ShowPolicyMap
        changed regex to support more patterns
    * Fix ShowPolicyMapInterface
        changed key for output with kbps

--------------------------------------------------------------------------------
                                platform
--------------------------------------------------------------------------------
* IOSXE
    * Update ShowEnvironment to support:
        show environment | include {include}

--------------------------------------------------------------------------------
                                ARP
--------------------------------------------------------------------------------
* IOSXE
    * Fix ShowIpTraffic to parser customer's output

--------------------------------------------------------------------------------
                                interface
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowInterfaceSwitchport to support custom interface argument

* NXOS
    * Updated ShowInterface
        * added show interface {interface} to support custom interface
    * Updated ShowIpInterfaceVrfAll
        * added show ip interface vrf {vrf},
                show ip interface {intf} vrf all,
                show ip interface {intf} vrf {vrf} to support custom interface and vrf
    * Updated ShowVrfAllInterface
        * added show vrf {vrf} interface {interface},
                show vrf {vrf} interface,
                show vrf all interface {interface} to support custom interface and vrf
    * Updated ShowInterfaceSwitchport
        * added show interface {interface} switchport to support custom interface
    * Updated ShowIpv6InterfaceVrfAll
        * added show ipv6 interface vrf {vrf},
                show ipv6 interface {intf} vrf all,
                show ipv6 interface {intf} vrf {vrf} to support custom interface and vrf
* ASA
    * Added ShowInterfaceSummary for:
      show interface summary
    * Added ShowInterfaceIpBrief for:
      show interface ip brief
    * Added ShowInterfaceDetail for:
      show interface detail

--------------------------------------------------------------------------------
                               VRF
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowVrfDetail to support description

--------------------------------------------------------------------------------
                               BGP
--------------------------------------------------------------------------------
* IOSXE
    * fixed a bug in ShowBgpAllSummary not executing the right command
    * fixed regex in ShowBgpAllDetail
    * Updated ShowBgpAllNeighborsAdvertisedRoutes to support:
        show ip bgp {address_family} vrf {vrf} neighbors {neighbor} advertised-routes
    * Updated ShowBgpNeighborsAdvertisedRoutesSuperParser issue to parse with VRF
    * Updated ShowBgpSummary for:
        Support for more VRF values
    * Updated ShowBgpAllSummary for:
        Support for more VRF values
    * Updated ShowIpBgpSummary for:
        Support for more VRF values
    * Updates ShowIpBgpAllSummary for:
        Support for more VRF values
* NXOS
    * Updated ShowBgpProcessVrfAll, ShowBgpVrfAllAll, ShowBgpVrfAllNeighbors,
        ShowBgpVrfAllAllNextHopDatabase, ShowBgpVrfAllAllSummary,
        ShowBgpVrfAllAllDampeningParameters, ShowBgpVrfAllNeighborsAdvertisedRoutes,
        ShowBgpVrfAllNeighborsRoutes, ShowBgpVrfAllNeighborsReceivedRoutes
        to support custom vrf, address_family and neighbor

* Optimized parser by moving all regex outside of for loop

--------------------------------------------------------------------------------
                                protocols
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpProtocols to fix parsing issue of unbound variable

--------------------------------------------------------------------------------
                                Inventory
--------------------------------------------------------------------------------
* ASA
    * Added ShowInventory for:
        show inventory

--------------------------------------------------------------------------------
                            routing
--------------------------------------------------------------------------------
* IOSXE
    * added ShowIpRouteSummary:
        show ip route vrf {vrf} summary
        show ip route summary
* IOS
    * added ShowIpRouteSummary:
        show ip route vrf {vrf} summary
        show ip route summary

* NXOS
    * Updated ShowRoutingVrfAll to support custom vrf
    * added ShowRouting for:
        show routing
        show routing {ip}

* ASA
    * Added ShowRoute for:
      show route
--------------------------------------------------------------------------------
                                L2VPN
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowEthernetServiceInstanceStats for:
        show ethernet service instance id {service_instance_id} interface {interface} stats
    * Added ShowEthernetServiceInstance for:
        show ethernet service instance
    * Updated ShowEthernetServiceInstanceDetailSchema
    * Added ShowEthernetServiceInstanceDetail for:
        show ethernet service instance id {service_instance_id} interface {interface} detail

--------------------------------------------------------------------------------
                                context
--------------------------------------------------------------------------------
* ASA
    * Added ShowContext for:
      show context
    * Added ShowContextDetail for:
      show context detail
      
--------------------------------------------------------------------------------
                                    BFD
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowBfdNeighborsDetails to add:
        show bfd neighbors interface {interface} details

--------------------------------------------------------------------------------
                              VIRTUAL-SERVICE
--------------------------------------------------------------------------------
* NXOS
    * Added ShowVirtualServiceGlobal for "show virtual-service global"
    * Added ShowVirtualServiceList for "show virtual-service list"
    * Added ShowVirtualServiceCore for "show virtual-service core [name {name}]"
    * Added ShowVirtualServiceDetail for "show virtual-service detail [name {name}]"
    * Added ShowGuestshell for "show guestshell"