--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowIpBgpL2VPNEVPN:
      * Added parser for "show ip bgp l2vpn evpn detail"
      * Added parser for "show ip bgp {address_family} evi {evi}
      * Added parser for "show ip bgp {address_family} route-type {rt}"
      * Added parser for "show ip bgp {address_family} evi {evi} route-type {rt}"
      * Added nlri_data object under prefixes in "ShowBgpAllDetailSchema"
      * Added pmsi_data object under prefixes in "ShowBgpAllDetailSchema"
      * Added igmpmld object under prefixes in "ShowBgpAllDetailSchema"
      * Added 4 regexp in ShowBgpDetailSuperParser
        ** p3_3 to handle all EVPN route-types
        ** p8_6 to handle PMSI attribute Flags
        ** p19 to handle IGMP/MLD filter
      * Modified 3 regexp in ShowBgpDetailSuperParser
        ** p11 to handle local IRB vxlan vtep
        ** p12 to handle core bdi
        ** p13 to handle evpn l3-vni
      * Added folder based unittests