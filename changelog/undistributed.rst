* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

-----------------------------------------------------------------------------
                                   Dot1x
-----------------------------------------------------------------------------
* NXOS
        * Added show_dot1x_Summary and modified show_dot1x_Statistics parsers
        * Added all_details and test_all_details & adressed show_dot1x comments
        * Modification to show_Dot1x schema and adressed show_dot1x comments

----------------------------------------------------------------------------
                                   OSPF
----------------------------------------------------------------------------
* OSPF
        * Optimized parser by moving all regex outside of for loop
* IOSXE
    * Updated ShowIpOspfInterface to support command 'show ip ospf interface {interface}'

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

* Optimized parser by moving all regex outside of for loop

--------------------------------------------------------------------------------
                                protocols
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpProtocols to fix parsing issue of unbound variable
