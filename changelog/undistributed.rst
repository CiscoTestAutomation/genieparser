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
    * Updated ShowBgpDetailSuperParser for:
        better handling of extended community

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
    * Updated ShowIpOspfDatabaseRouter to parse TOS metrics

--------------------------------------------------------------------------------
                                Platform
--------------------------------------------------------------------------------
* IOSXE
    * Updates ShowVersion to make last_reload_reason an optional key

--------------------------------------------------------------------------------
                                  SPT
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowSpanningTreeMst for:
        show spanning-tree mst <mst_id>
    * Add ShowSpanningTreeMstag for:
        show spanning-tree mstag <mag_domain>
    * Add ShowSpanningTreePvrst for:
        show spanning-tree pvrst <pvst_id>
    * Add ShowSpanningTreePvrsTag for:
        show spanning-tree pvrstag <pvrstag_domain>
    * Add ShowSpanningTreePvsTag for:
        show spanning-tree pvstag <pvstag_domain>
