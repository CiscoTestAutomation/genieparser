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