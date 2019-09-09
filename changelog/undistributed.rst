* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                MPLS
--------------------------------------------------------------------------------
* IOSXE
    * Update ShowMplsForwardingTable
        * Add command 'show mpls forwarding-table {prefix}'
        * update regex to support local label 'None'

--------------------------------------------------------------------------------
                                Segment Routing
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowSegmentRoutingMplsConnectedPrefixSidMapLocal for:
        'show segment-routing mpls connected-prefix-sid-map local ipv4'
        'show segment-routing mpls connected-prefix-sid-map local ipv6'
    * Added ShowSegmentRoutingTrafficEngTopology for:
        'show segment-routing traffic-eng topology ipv4'
    * Added ShowSegmentRoutingTrafficEngPolicy for:
        'show segment-routing traffic-eng policy all'
        'show segment-routing traffic-eng policy name {name}'
    * Added ShowSegmentRoutingMplsMappingServer for:
        'show segment-routing mpls mapping-server ipv4'
        'show segment-routing mpls mapping-server ipv6'

--------------------------------------------------------------------------------
                                ISSU
--------------------------------------------------------------------------------
* IOS
	Added ShowIssuStateDetail for:
		* show issu state detail
	Added ShowIssuRollbackTimer for:
	 	* show issu rollback-timer
--------------------------------------------------------------------------------
                              Virtual-Service
--------------------------------------------------------------------------------
* NXOS
    * Added ShowVirtualServiceUtilization for "show virtual-service utilization name {name}"

--------------------------------------------------------------------------------
                                BGP
--------------------------------------------------------------------------------
* IOSXR
    * Updated ShowBgpL2vpnEvpn for:
        added a schema and unittest, and updated based on the schema

--------------------------------------------------------------------------------
                                OSPF
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpOspfSegmentRoutingLocalBlock to add:
        * show ip ospf segment-routing local-block
    * Added ShowIpOspfDatabaseOpaqueAreaTypeExtLink for:
        * show ip ospf database opaque-area type ext-link
    * Added ShowIpOspfDatabaseOpaqueAreaTypeExtLinkSelfOriginate for:
        * show ip ospf database opaque-area type ext-link self-originate
    * Added ShowIpOspfDatabaseOpaqueAreaTypeExtLinkAdvRouter for:
        * show ip ospf database opaque-area type ext-link adv-router {address}
    * Updated ShowIpOspfDatabaseTypeParser to parse more varied output

--------------------------------------------------------------------------------
                                dot1x
--------------------------------------------------------------------------------
* IOSXE
    * removed tab, replace with space
    	'show dot1x all statistics'

--------------------------------------------------------------------------------
                                MPLS
--------------------------------------------------------------------------------
* IOS
        * Added ShowIpMsdpSaCache for commands:
                * show ip msdp sa-cache
                * show ip msdb vrf {vrf} sa-cache
        * Added ShowIpMsdpPeer for commands:
                * show ip msdp peer
                * show ip msdp vrf {vrf} peer

--------------------------------------------------------------------------------
                                vlan
--------------------------------------------------------------------------------
* IOSXE
    * Fixed regex in ShowVlan
    
--------------------------------------------------------------------------------
                                FLOW MONITOR
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowFlowMonitor for:
        * show flow monitor {name} cache format table

--------------------------------------------------------------------------------
                                ROUTING
--------------------------------------------------------------------------------
* IOSXR
    * Updated ShowRouteIpv4:
        * Matching more routes
        * Optimized parser moving regex compilation out of for loop