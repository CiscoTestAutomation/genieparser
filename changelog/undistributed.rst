* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                Route
--------------------------------------------------------------------------------
* Junos
    * Add ShowRouteTable for:
        * show route table {table}
        * show route table {table} {prefix}
--------------------------------------------------------------------------------
                                Interface
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowInterfaces for:
        'show interfaces'
        'show interfaces {interface}'

* IOSXE
    * Fix ShowRedundancyStates
        changed 'maintenance_mode' key to optional to support more output

--------------------------------------------------------------------------------
                                Controllers
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowControllersCoherentDSP for
        'show controllers coherentDSP {unit}'
    * Add ShowControllersOptics for
        'show controllers optics {unit}'

--------------------------------------------------------------------------------
                                Lag
--------------------------------------------------------------------------------
* IOSXE
    * Fix ShowPagpNeighbor
        added 'show pagp neighbor' key to cli command for Ops
* IOSXR
    * Update ShowBundle
        to support 'show bundle {interface}'

--------------------------------------------------------------------------------
                                traceroute
--------------------------------------------------------------------------------
* IOSXE
    * Update TraceRoute
        schema changed for multi paths support

--------------------------------------------------------------------------------
                                Cdp
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowCdpNeighborsDetail
        * Fixed regEx to avoid omitting after '/' in the 'port_id'

--------------------------------------------------------------------------------
                                Platform
--------------------------------------------------------------------------------
* NXOS
    * Fix ShowVersion
        updated schema and regEx to support more outputs
* IOSXE
    * Update ShowPlatform
        to parse 'lc_type' more clearly and flexibly based on updated schema

--------------------------------------------------------------------------------
                                Lldp
--------------------------------------------------------------------------------
* IOSXR
    * Update ShowLldpEntry
        added a key 'show lldp entry' for Ops

--------------------------------------------------------------------------------
                                Prefix_list
--------------------------------------------------------------------------------
* IOSXR
    * Update ShowIpv6PrefixListDetail
        updated cli for Ops

--------------------------------------------------------------------------------
                                Segment Routing
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowSegmentRoutingMplsLB for
        'show segment-routing mpls lb'
    * Added ShowSegmentRoutingMplsState for
        'show segment-routing mpls state'
    * Added ShowSegmentRoutingMplsLbLock for
        'show segment-routing mpls lb lock'
    * Added ShowSegmentRoutingMplsGbLock for:
        'show segment-routing mpls gb lock'

--------------------------------------------------------------------------------
                                Pim
--------------------------------------------------------------------------------
* IOSXR
    * Update ShowPimNeighbor
        updated cli and added exclude for Ops
    * Update ShowIpPimNeighbor
        updated cli and added exclude for Ops
    * Update ShowIpv6PimNeighbor
        updated cli and added exclude for Ops
    * Update ShowIpv6PimNeighborDetail
        updated cli and added exclude for Ops

--------------------------------------------------------------------------------
                                Bgp
--------------------------------------------------------------------------------
* IOSXE
    * Fix ShowIpBgpTemplatePeerSession
        added a key to cli command for Ops
    * Fix ShowIpBgpTemplatePeerPolicy
        added a key to cli command for Ops

--------------------------------------------------------------------------------
                                Ospf
--------------------------------------------------------------------------------
* IOSXE
    * Update ShowIpOspfNeighborDetail
        to parse 'SR adj label' in output
    * Added ShowIpOspfSegmentRouting for command:
        * show ip ospf {process_id} segment-routing adjacency-sid
    * Added ShowIpOspfFastRerouteTiLfa for
        'show ip ospf fast-reroute ti-lfa'
    * Added ShowIpOspfSegmentRoutingProtectedAdjacencies for
        show ip ospf segment-routing protected-adjacencies
    * Added ShowIpOspfSegmentRoutingSidDatabase for:
        * show ip ospf segment-routing sid-database
    * Added ShowIpOspfSegmentRoutingGlobalBlock for
        * show ip ospf segment-routing global-block
        * show ip ospf {process_id} segment-routing global-block

--------------------------------------------------------------------------------
                                Routing
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpRouteWord
        * Added parsing ability for: 'SR Incoming Label', 'MPLS label', 'MPLS Flags', 'Repair Path'

--------------------------------------------------------------------------------
                                Authentication Sessions
--------------------------------------------------------------------------------
* IOSXE
   * ShowAuthenticationSessions for: 
        * 'show authentication sessions'
        * 'show authentication sessions interface {interface}'
   * ShowAuthenticationSessionsInterfaceDetails for:
        * 'show authentication sessions interface {interface} details'
--------------------------------------------------------------------------------
                                Mcast
--------------------------------------------------------------------------------
* IOSXE
    * Update ShowIpMroute
        added a key to cli command for Ops
    * Update ShowIpv6Mroute
        added a key to cli command for Ops

