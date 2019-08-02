| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 19.7.0        |

-----------------------------------------------------------------------------
                                   platform
-----------------------------------------------------------------------------
* JunOS
    * Added parser for 'file list' and 'file list {filename}'

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
* IOSXE
    * Fix ShowIpRoute
        * updated regex to handle the output more flexibly
    * Fix ShowIpv6Route
        * updated command
    * Fix ShowIpRouteSummary
        * updated regex to support table name containing a dash

--------------------------------------------------------------------------------
                                Interface
--------------------------------------------------------------------------------
* IOSXE
    * Fix ShowIpInterfaceBrief short name issue
    * Fix ShowInterfacesSwitchport
        changed 'trun_vlan' schema type to support multiple values
    * Fix ShowInterfacesAccounting interface name issue
    * Fix ShowInterfaces
        changed schema type to support multiple outputs of interface

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
    * Updated ShowIpOspfTraffic to support different outputs
    * Enhanced regex to support more patterns
    * Updated regex in ShowIpOspfMplsLdpInterface to support more output
    * Added ShowIpOspfInterfaceBrief for:
        * show ip ospf interface brief
* NXOS
    * Fix ShowIpOspf
        added inserting key to avoid missing key error without duplicate output
* JUNOS
    * Added ShowOspfInterfaceBrief for:
        * show ospf interface brief
        * show ospf interface brief instance master
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
    * Updated showProcessCpuPlatform to support different outputs

* IOSXE
    * Fix ShowPlatform
        added regEx in the condition for 'lc_type' to handle outputs flexibly

--------------------------------------------------------------------------------
                                ARP
--------------------------------------------------------------------------------
* IOSXE
    * Fix ShowIpTraffic to parser customer's output

* IOSXR
    * Updated ShowArpTrafficDetail to support more outputs
    * Updated regex to support more patterns

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
    * Updated ShowBgpNeighborsAdvertisedRoutesSuperParser for:
        * issue to parse with VRF
        * issue parsing more than one of the same advertised address
    * Updated ShowBgpSummary for:
        Support for more VRF values
    * Updated ShowBgpAllSummary for:
        Support for more VRF values
    * Updated ShowIpBgpSummary for:
        Support for more VRF values
    * Updates ShowIpBgpAllSummary for:
        Support for more VRF values
    * added restricted list for ShowBgpAll
    * Updates ShowIpBgpNeighbors for:
        Support for more Message statistics values
    * Updated ShowBgpAllNeighborsRoutesSuperParser for parsing of more status codes
    * Updated regexes in ShowBgpSuperParser to support more output
* NXOS
    * Updated ShowBgpProcessVrfAll, ShowBgpVrfAllAll, ShowBgpVrfAllNeighbors,
        ShowBgpVrfAllAllNextHopDatabase, ShowBgpVrfAllAllSummary,
        ShowBgpVrfAllAllDampeningParameters, ShowBgpVrfAllNeighborsAdvertisedRoutes,
        ShowBgpVrfAllNeighborsRoutes, ShowBgpVrfAllNeighborsReceivedRoutes
        to support custom vrf, address_family and neighbor
    * Updated ShowBgpProcessVrfAll to remove vrf checks

* Optimized parser by moving all regex outside of for loop

--------------------------------------------------------------------------------
                                protocols
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpProtocols to fix parsing issue of unbound variable

--------------------------------------------------------------------------------
                                    STP
--------------------------------------------------------------------------------
* NXOS
        * Added ShowSpanningTreeMstDetails to show_stp parser
        * Added ShowSpanningTreeDetails, ShowSpanningTreeSummary and addressed ShowSpanningTreeMstDetails comments

--------------------------------------------------------------------------------
* ASA
    * Added ShowInventory for:
        show inventory
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

* IOSXE
    * Fix for ShowEthernetServiceInstanceDetail
        updated code to handle multiple outputs properly and fixed incorrect UT

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

--------------------------------------------------------------------------------
                              vpc
--------------------------------------------------------------------------------
* NXOS
    * Added ShowVpc for "show vpc"

--------------------------------------------------------------------------------
                                fdb
--------------------------------------------------------------------------------
* IOSXE
    * Added "entry", "learn", and "age" for ShowMacAddressTable to handle additional columns

* NXOS
    * Updated for ShowMacAddressTableBase to fix parsing issue with vPC Peer-Link(R) in 'ports' and regEx for 'age'


--------------------------------------------------------------------------------
                              bridge-domain
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowBridgeDomain:
      Parser will parse outputs even when Bridge-domain has 0 ports

--------------------------------------------------------------------------------
                                ntp
--------------------------------------------------------------------------------
* IOS
    * Updated ShowNtpAssociations:
        Fixed parsing wrong data in different order and added regExs to handle old version of device output as well
* IOSXE
    * Updated ShowNtpAssociationsDetail:
        Updated regex to support more output
    * Update ShowNtpStatus:
        Added leap second field in schema

--------------------------------------------------------------------------------
                               RIP
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpv6RipDatabase to support more outputs

--------------------------------------------------------------------------------
                                LAG
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowLacpNeighborDetail to support more outputs
* NXOS
    * Updated ShowLacpNeighborDetail to support more outputs
* IOSXR
    * Updated ShowLacpNeighborDetail to support more outputs

--------------------------------------------------------------------------------
                                SYSTEM
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowClock to support more outputs

--------------------------------------------------------------------------------
                                MPLS
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowMplsLdpIgpSync:
        updated regex to support more outputs

--------------------------------------------------------------------------------
                                CDP
--------------------------------------------------------------------------------
* NXOS
    * Fixed ShowCdpNeighbors:
        updated regex to support outputs in different order

--------------------------------------------------------------------------------
                                VTP
--------------------------------------------------------------------------------
* IOSXE
    * Fixed ShowVtpStatus:
        updated regex to support more flexible output
