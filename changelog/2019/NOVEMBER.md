| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 19.11.0       |


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
    * cat9500
        * Added ShowIssuStateDetail
            * show issu state detail
        * Added ShowIssuRollbackTimer
            * show issu rollback-timer
        * Added ShowVersion
            * show version
        * Added ShowRedundancy
            * show redundancy
        * Added ShowInventory
            * show inventory
        * Added ShowPlatform
            * show platform

* NXOS
    * Added ShowInterfacesDescription for commands;
        * 'show interface description'
        * 'show interface {interface} description'
    * Added ShowAccessLists for commands:
        * 'show access-lists'
        * 'show access-lists {acl}'
        * 'show access-lists summary'
    * Enhanced Dir
        * added 'dir {directory}' support
    * Added ShowIsis for commands:
        * 'show isis'
        * 'show isis vrf {vrf}'
    * Added ShowIsisInterface for commands:
        * 'show isis interface'
        * 'show isis interface vrf {vrf}'
    * Added ShowIsisSpfLogDetail for commands:
        * 'show isis spf-log detail'
        * 'show isis spf-log detail vrf {vrf}'
    * Added ShowIsisAdjacency for commands:
        * 'show isis adjacency'
        * 'show isis adjacency vrf {vrf}'
    * Added ShowIsisHostname for commands:
        * 'show isis hostname'
        * 'show isis hostname vrf {vrf}'
    * Added ShowIsisDatabaseDetail for commands:
        * 'show isis database detail'
        * 'show isis database detail vrf {vrf}'

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
        * 'show msdp peer {peer}'
        * 'show msdp vrf {vrf} peer'
        * 'show msdp vrf {vrf} peer {peer}'
    * Added ShowMsdpContext for commands:
        * 'show msdp context'
        * 'show msdp vrf {vrf} context'
    * Added ShowMsdpSummary for commands:
        * 'show msdp summary'
        * 'show msdp vrf {vrf} summary'
    * Added ShowMsdpSaCache for commands:
        * 'show msdp sa-cache'
        * 'show msdp sa-cache {group}'
        * 'show msdp vrf {vrf} sa-cache'
        * 'show msdp vrf {vrf} sa-cache {group}'
    * Added ShowMsdpStatisticsPeer for commands:
        * 'show msdp statistics peer'
        * 'show msdp statistics peer {peer}'
        * 'show msdp vrf {vrf} statistics peer'
        * 'show msdp vrf {vrf} statistics peer {peer}'
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
    * Added ShowIpv4InterfaceBrief for commands:
        * 'show ipv4 interface brief | include {ip}'
        * 'show ipv4 interface brief'


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
    * Updated ShowIgmpGroupsDetail
        * Updated schema and patten match for source list

* NXOS
    * ShowIpOspf
        * Added missing keys to schema
        * Added regex to capture more outputs
    * Updated ShowVpc for:
        * Parser schema and regex to support more output
    * Updated ShowVersion:
	    * Updated regex matching for platform:chassis and platform:model
    * Updated ShowIpOspfInterfaceVrfAll
        * Changed keywords schema to optional

* IOSXE
    * Updated ShowAuthenticationSessions
        * Changed keyword to Optional
        * Added keyword to schema
        * Added regex to support new output
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
    * Updated ShowIpCefInternal for:
        * show ip cef internal
        * show ip cef {prefix} internal
        * show ip cef vrf {vrf} {prefix} internal
    * Updated ShowBgpDetailSuperParser for:
        * show ip bgp {address_family} vrf {vrf} detail
    * Updated ShowVersion:
        * Added keywords to schema
        * Added regex for unparsed outputs
	    * Removed extra spaces in platform keyword
    * Updated ShowPlatform
        * Updated parser logic to support c8300 platform
    * Updated ShowIpOspfSegmentRoutingSidDatabase for:
        * Supporting more than one entry under one sid
    * Updated ShowAuthenticationSessionsInterfaceDetails
        * Added keywords to schema
        * Added and changed regex to accommodate different outputs
    * Updated ShowSegmentRoutingTrafficEngPolicy for:
        * Better support for hop configurations
    * Updated ShowSegmentRoutingTrafficEngPolicy
        * Updated regex and added optional key to support more outputs
    * Updated ShowClnsProtocol
        * Changed keyword 'process_handle' to Optional

* IOS
    * Updated ShowInventory
        * Added regex to support various outputs
    * Updated ShowIpOspfSegmentRoutingProtectedAdjacencies for:
        * changed backup_nexthop and backup_nexthop to optional
    * Updated ShowVersion
	    * Corrected the value in os key
    * Updated ShowVtpStatus
	    * Updated schema to fix customer issue for show vtp status

* JUNOS
    * Enhanced ShowOspfInterfaceBrief:
        * Added command 'show ospf interface {interface} brief'
    * Enhanced ShowInterfacesTerse:
        * Added command 'show interfaces {interface} terse'
