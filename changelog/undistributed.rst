* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                OSPF
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpOspfInterface to support command 'show ip ospf interface {interface}'
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
* ASA
    * Added ShowArp for:
        show arp
--------------------------------------------------------------------------------
                                interface
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowInterfaceSwitchport to support custom interface argument
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
* IOSXR
    * Updated ShowBgpInstanceProcessDetail, ShowBgpInstanceNeighborsDetail,
        ShowBgpInstanceNeighborsAdvertisedRoutes, ShowBgpInstanceNeighborsReceivedRoutes,
        ShowBgpInstanceNeighborsRoutes, ShowBgpInstanceSummary, and ShowBgpInstanceAllAll
        to support custom {vrf}, {instance}, and {neighbor}
    * Updated ShowBgpSummary for:
        Support for more VRF values
    * Updated ShowBgpAllSummary for:
        Support for more VRF values
    * Updated ShowIpBgpSummary for:
        Support for more VRF values
    * Updates ShowIpBgpAllSummary for:
        Support for more VRF values

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
