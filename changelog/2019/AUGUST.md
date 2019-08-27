| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 19.8.0        |
--------------------------------------------------------------------------------
                                CEF
--------------------------------------------------------------------------------
* IOSXE
    * Fixed ShowIpCef
        * Changed parser to match more 'outgoing_label' values
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

* Linux
    * Add Ifconfig for
        'ifconfig'
        'ifconfig {interface}'

--------------------------------------------------------------------------------
                                Controllers
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowControllersCoherentDSP for
        'show controllers coherentDSP {port}'
    * Add ShowControllersOptics for
        'show controllers optics {port}'

--------------------------------------------------------------------------------
                                BGP
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowBgpL2vpnEvpnNeighbors for
        'show bgp l2vpn evpn neighbors'
        'show bgp l2vpn evpn neighbors {neighbor}'

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
    * Added ShowSegmentRoutingMplsConnectedPrefixSidMapLocal for:
        'show segment-routing mpls connected-prefix-sid-map local ipv4'
        'show segment-routing mpls connected-prefix-sid-map local ipv6'

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
    * Added ShowIpOspfSegmentRouting for:
        * show ip ospf segment-routing
    * Update ShowIpOspfSegmentRoutingSidDatabase
        to handle missing keys
    * Added ShowIpOspfDatabaseOpaqueAreaSelfOriginate for:
        * show ip ospf database opaque-area self-originate
    * Added ShowIpOspfDatabaseOpaqueAreaAdvRouter for:
        * show ip ospf database opaque-area adv-router {address}

--------------------------------------------------------------------------------
                                Routing
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpRouteWord
        * Added parsing ability for: 'SR Incoming Label', 'MPLS label', 'MPLS Flags', 'Repair Path'
* NXOS
    * Updated ShowIpRoute
        * Updated regex to match more varied output

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

--------------------------------------------------------------------------------
                                BGP
--------------------------------------------------------------------------------
* IOSXE
    * Update ShowBgpAllNeighborsSchema
    * Update ShowBgpNeighborSuperParser
        updated regEx to handle different outputs

--------------------------------------------------------------------------------
                                VXLAN
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowL2routeEvpnImetAllDetail for
        'show l2route evpn imet all detail'

--------------------------------------------------------------------------------
                                VRF
--------------------------------------------------------------------------------
* IOSXR
    * Updated ShowVrfAllDetailSchema
        updated the schema due to missing key error

--------------------------------------------------------------------------------
                                BGP
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowBgpAllSummary
        removed cmd as param due to missing key error

--------------------------------------------------------------------------------
                                VRF
--------------------------------------------------------------------------------
* IOSXE
    * Updated utils.common
        Added vl = vasileft; vr = vasiright
    * Updated test_show_vrf.py
        Replaced output similar to customer's output

--------------------------------------------------------------------------------
                                Platform
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowModule
        added abstraction for Cat4k (c4507)

--------------------------------------------------------------------------------
                                VXLAN
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowL2routeMacIpAllDetail
        fixed regEx to parse properly

--------------------------------------------------------------------------------
                                VRF
--------------------------------------------------------------------------------
* IOSXR
    * Updated ShowVrfAllDetail
        updated regEx to parse 'ip_address' properly

--------------------------------------------------------------------------------
                                Interface
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowInterfacesSwitchport
        fixed regEx to parse complex output
--------------------------------------------------------------------------------
                                Segment Routing
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowSegmentRoutingMplsConnectedPrefixSidMapLocal for:
        'show segment-routing mpls connected-prefix-sid-map local ipv4'
        'show segment-routing mpls connected-prefix-sid-map local ipv6'
