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
    * Added ShowIpNatTranslations
        * show ip nat translations
        * show ip nat translations verbose
        * show ip nat translations vrf {vrf}
        * show ip nat translations vrf {vrf} verbose
    * Added ShowIpNatStatistics
        * show ip nat statistics
    * Added ShowIpCefInternal
        * show ip cef {ip} internal
        * show ip cef internal

    * Added ShowFlowMonitorCache for command;
        * show flow monitor {name} cache
    * Added ShowFlowMonitorCacheRecord for command;
        * show flow monitor {name} cache format record
	* Enhanced Dir
		* added 'dir {directory}' support


    * Updated ShowIpBgpDetail for:
        * show ip bgp {address_family} all detail


* NXOS
    * Added ShowInterfacesDescription for commands;
        * 'show interface description'
        * 'show interface {interface} description'
	* Enhanced Dir
		* added 'dir {directory}' support

* IOS
    * Added ShowInterfacesDescription for commands;
        * 'show interfaces description'
        * 'show interfaces {interface} description'
    * Added ShowIpNatTranslations for commands:
        * show ip nat translations
        * show ip nat translations verbose
        * show ip nat translations vrf {vrf}
        * show ip nat translations vrf {vrf} verbose
    * Added ShowIpNatStatistics
        * show ip nat statistics
    * Added ShowIgmp for commands:
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

* IOSXR
    * Added ShowMsdpPeer for commands:
        * 'show msdp peer'
        * 'show msdp vrf {vrf} peer'
    * Added ShowMsdpContext for commands:
        * 'show msdp context'
        * 'show msdp vrf {vrf} context'
    * Added ShowMsdpSummary for commands:
        * 'show msdp summary'
        * 'show msdp vrf {vrf} summary'
    * Added ShowMsdpSaCache for commands:
        * 'show msdp sa-cache'
        * 'show msdp vrf {vrf} sa-cache'
    * Added ShowMsdpStatisticsPeer for commands:
        * 'show msdp statistics peer'
        * 'show msdp vrf {vrf} statistics peer'
    * Added ShowBgpNeighbors for commands:
        * 'show bgp neighbors'
        * 'show bgp neighbors {neighbor}'
        * 'show bgp vrf {vrf} neighbors'
        * 'show bgp vrf {vrf} neighbors {neighbor}'
        * 'show bgp {address_family} neighbors'
        * 'show bgp {address_family} neighbors {neighbor}'
        * 'show bgp vrf {vrf} {address_family} neighbors'
        * 'show bgp vrf {vrf} {address_family} neighbors {neighbor}'
    * Added ShowBgpSummary for commands:
        * 'show bgp summary'
        * 'show bgp {address_family} summary'
	* Enhanced Dir
		* added 'dir {directory}' support

* JUNOS
    * Added ShowOspfInterface for commands:
        * 'show ospf interface'
        * 'show ospf interface {interface}'
        * 'show ospf interface instance {instance}'
    * Added ShowOspfInterfaceDetail for commands:
        * 'show ospf interface detail'
        * 'show ospf interface {interface} detail'
        * 'show ospf interface detail instance {instance}'
        * 'show ospf interface {interface} detail instance {instance}'
    * Added ShowTedDatabaseExtensive for commands:
        * 'show ted database extensive'
        * 'show ted database extensive {node_id}'

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
    * Updated ShowBgpSessions
        * Updated regex to accommodate different formats

* NXOS
    * ShowIpOspf
        * Added missing keys to schema
        * Added regex to capture more outputs
    * Updated ShowVpc for:
        * Parser schema and regex to support more output

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
    * Updated ShowMplsForwardingTable for:
        * show mpls forwarding-table
        * show mpls forwarding-table {prefix}
        * show mpls forwarding-table vrf {vrf}
    * Updated ShowBgpDetailSuperParser for:
        * show ip bgp {address_family} vrf {vrf} detail 

* IOSXR
    * Updated ShowBgpSessions
        * Updated regex to accommodate different formats

* IOSXE
    * Updated ShowVersion
        * Added keywords to schema
        * Added regex for unparsed outputs
* IOS
    * Updated ShowInventory
        * Added regex to support various outputs
    * Updated ShowIpOspfSegmentRoutingProtectedAdjacencies for:
        * changed backup_nexthop and backup_nexthop to optional

* JUNOS
    * Enhanced ShowOspfInterfaceBrief:
        * Added command 'show ospf interface {interface} brief'
    * Enhanced ShowInterfacesTerse:
        * Added command 'show interfaces {interface} terse'


* NXOS
    * Updated ShowIpOspfInterfaceVrfAll
        * Changed keywords schema to optional
* IOSXE
    * Updated ShowAuthenticationSessionsInterfaceDetails
        * Added keywords to schema
        * Added and changed regex to accommodate different outputs
    
    * Updated ShowAuthenticationSessions
        * Added keyword to schema
        * Added regex to support new output

