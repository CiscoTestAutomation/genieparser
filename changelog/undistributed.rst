* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                   Routing
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowRoutingVrfAll
        * added show routing vrf {vrf} to support custom vrf
    * Updated ShowRoutingIpv6VrfAll
        * added show ipv6 routing vrf {vrf} to support custom vrf
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
    
--------------------------------------------------------------------------------
                                protocols
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpProtocols to fix parsing issue of unbound variable

