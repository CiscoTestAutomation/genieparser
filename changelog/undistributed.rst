* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

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
                                OSPF
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpOspf for more varied router-LSAs

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