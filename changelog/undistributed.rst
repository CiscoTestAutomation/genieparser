* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowRouteIpDistributor for commands;
        * 'show route vrf {vrf} ipv4'
        * 'show route ipv4'
        * 'show route ipv4 {route}'
        * 'show route ipv4 {protocol}'
        * 'show route vrf {vrf} ipv4 {protocol}'
        * 'show route vrf {vrf} ipv4 {route}'
    * Added ShowRouteIpv6Distributor for commands;
        * 'show route vrf {vrf} ipv6'
        * 'show route ipv6'
        * 'show route ipv6 {route}'
        * 'show route ipv6 {protocol}'
        * 'show route vrf {vrf} ipv6 {protocol}'
        * 'show route vrf {vrf} ipv6 {route}'
    * Added ShowInterfacesDescription for commands;
        * 'show interfaces description'
        * 'show interfaces {interface} description'
		
* NXOS
    * Added ShowInterfacesDescription for commands;
        * 'show interface description'
        * 'show interface {interface} description'
		
* IOS
    * Added ShowInterfacesDescription for commands;
        * 'show interfaces description'
        * 'show interfaces {interface} description'

* IOSXR
    * Added ShowMsdpPeer, ShowMsdpContext, ShowMsdpSummary, ShowMsdpSaCache, ShowMsdpStatisticsPeer for commands:
        * 'show msdp peer'
        * 'show msdp vrf {vrf} peer'
        * 'show msdp context'
        * 'show msdp vrf {vrf} context'
        * 'show msdp summary'
        * 'show msdp vrf {vrf} summary'
        * 'show msdp sa-cache'
        * 'show msdp vrf {vrf} sa-cache'
        * 'show msdp statistics peer'
        * 'show msdp vrf {vrf} statistics peer'
    * Added ShowIgmp for commands;
        * 'show igmp interface'
        * 'show igmp interface {interface}'
        * 'show igmp vrf {vrf} interface'
        * 'show igmp vrf {vrf} interface {interface}'
        * 'show igmp summary'
        * 'show igmp vrf {vrf} summary'
        * 'show igmp groups detail'
        * 'show igmp vrf {vrf} groups detail'
    * Added ShowInterfacesDescription for commands;
        * 'show interfaces description'
        * 'show interfaces {interface} description'
    * Added ShowIsisPrivateAll for commands;
        * 'show isis private all'
		
--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXR
    * Enhanced ShowBgpInstanceNeighborsReceivedRoutes;
        * Updated code to support various outputs
        * Added unittest corresponding to the new supported output
    * Enhanced ShowBgpInstanceSummary;
        * Updated code to support various outputs
        * Added unittest corresponding to the new supported output
    * Enhanced ShowRouteIpv6:
        * Updated regex to support various outputs

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* NXOS
    * ShowIpOspf
        * Added missing keys to schema
        * Added regex to capture more outputs
    * Updated ShowVpc for:
        * Parser schema and regex to support more output

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowAuthenticationSessions
        * Changed keyword to Optional
    * Updated ShowIpRoute for:
        * show ip route vrf {vrf} {protocol}
        * show ip route vrf {vrf}
        * show ip route {protocol}
        * show ip route
    * Updated ShowIpRouteWord for:
        * show ip route {route}
        * show ip route vrf {vrf} {route}
    * Updated ShowIpv6Route for:
        * show ipv6 route vrf {vrf} {protocol}
        * show ipv6 route vrf {vrf}
        * show ipv6 route {protocol}
        * show ipv6 route
    * Updated ShowIpv6RouteWord for:
        * show ipv6 route {route}
        * show ipv6 route vrf {vrf} {route}


    * Updated ShowIpOspfSegmentRoutingProtectedAdjacencies for:
        * changed backup_nexthop and backup_nexthop to optional

* IOSXR
    * Updated ShowBgpSessions
        * Updated regex to accommodate different formats


