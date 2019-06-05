* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                logging
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowLogging for:
    	show logging
    	show logging | include {Word}
    
--------------------------------------------------------------------------------
                                BGP
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpBgpDetail for:
        show ip bgp {address_family} rd {rd} {route}
    * Updated ShowIpBgpAllDetail for:
        show ip bgp {address_family} vrf {vrf} {route}
    * Updated parser for ShowBgpAllDetail:
        show bgp vrf {vrf} {route}
        show bgp {address_family} vrf {vrf} {route}

--------------------------------------------------------------------------------
                                Routing
--------------------------------------------------------------------------------
* IOSXE
    * added ShowIpRouteDistributor and ShowIpv6RouteDistributor class
* IOS
    * added ShowIpRouteDistributor and ShowIpv6RouteDistributor class

--------------------------------------------------------------------------------
                                OSPF
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpOspf for more varied router-LSAs

--------------------------------------------------------------------------------
                                   interface
--------------------------------------------------------------------------------
* IOSXR
    * Updated ShowIpv4VrfAllInterface to support custom vrf
        * show ipv4 vrf {vrf} interface
    * Updated ShowIpv6VrfAllInterface to support custom vrf
        * show ipv6 vrf {vrf} interface
