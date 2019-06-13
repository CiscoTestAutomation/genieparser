* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

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
    * fixed a bug in ShowBgpAllDetail parsing same vrf twice
    * Updated ShowBgpAllNeighborsAdvertisedRoutes to support:
        show ip bgp {address_family} vrf {vrf} neighbors {neighbor} advertised-routes
    * Updated ShowBgpNeighborsAdvertisedRoutesSuperParser issue to parse with VRF
    
--------------------------------------------------------------------------------
                                protocols
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpProtocols to fix parsing issue of unbound variable