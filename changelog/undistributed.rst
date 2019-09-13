* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                Interface
--------------------------------------------------------------------------------
* NXOS
    * Update ShowInterfaceBrief
        * Add command 'show interface {interface} brief'
    * Update ShowRunningConfigInterface
        * Update regex to support more interface names
        * Updated schema to support more outputs
* IOSXR
    * Update ShowIpv6VrfAllInterface
        * Update regex to avoid empty lines and command itself

--------------------------------------------------------------------------------
                                EIGRP
--------------------------------------------------------------------------------
* IOS
        * Added ShowIpEigrpNeighbors for commands
                * 'show ip eigrp vrf {vrf} neighbors'
                * 'show ip eigrp neighbors'
        * Added ShowIpv6EigrpNeighbors for commands:
                * 'show ipv6 eigrp vrf {vrf} neighbors'
                * 'show ipv6 eigrp neighbors'
        * Added ShowIpEigrpNeighborsDetail for commands:
                * 'show ip eigrp neighbors detail'
                * 'show ip eigrp vrf {vrf} neighbors detail'
        * Added ShowIpv6EigrpNeighborsDetail for commands:
                * 'show ipv6 eigrp neighbors detail'

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
    * Added ShowSegmentRoutingTrafficEngPolicyDetail for:
        'show segment-routing traffic-eng policy all detail'
        'show segment-routing traffic-eng policy name {name} detail'
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
    * Updated ShowBgpInstanceAllAll for address family regex issue
* IOS
    * Added ShowBgpSummary for:
        * show bgp summary
        * show bgp all summary
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
    * Added ShowIpOspfSegmentRoutingAdjacencySid for:
        * show ip ospf segment-routing adjacency-sid
        * show ip ospf {process_id} segment-routing adjacency-sid

--------------------------------------------------------------------------------
                                dot1x
--------------------------------------------------------------------------------
* IOSXE
    * removed tab, replace with space
    	'show dot1x all statistics'

--------------------------------------------------------------------------------
                                PIM
--------------------------------------------------------------------------------
* NXOS
	* Updated ShowRunningConfigPim:
		changed logic to support calling from device.parse

--------------------------------------------------------------------------------
								VRF
--------------------------------------------------------------------------------
* NXOS
	* Updated ShowRunningConfigVrf:
		changed logic to support calling from device.parse

--------------------------------------------------------------------------------
								common.py
--------------------------------------------------------------------------------
* updated _find_command to escape "^"
* disallow spaces in key "feature"

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
                                FLOW
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowFlowMonitor for:
        * show flow monitor {name} cache format table
    * Added ShowFlowExporterStatistics for:
        * show flow exporter statistics
        * show flow exporter {exporter} statistics

--------------------------------------------------------------------------------
                                ROUTING
--------------------------------------------------------------------------------
* IOSXE
    * Update ShowIpCef
        * update regex to support outgoing_label_backup and outgoing_label_info
* IOSXR
    * Updated ShowRouteIpv4:
        * Matching more routes
        * Optimized parser moving regex compilation out of for loop

--------------------------------------------------------------------------------
                                INVENTORY
--------------------------------------------------------------------------------
* IOS
    * Updated ShowInventory:
        * Matching more slots

--------------------------------------------------------------------------------
                                Spanning-tree
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowSpanningTreeSummary to:
        * regex to accommodate different formats
        * changed some fields in schema to Optional
    * Updated ShowSpanningTreeDetail to:
        * updated regex to accommodate more formats
        * add support for rstp
        * chnaged some fields in schema to Optional

--------------------------------------------------------------------------------
                                Spanning-Tree
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowSpanningTreeSummary:
        * Changed some schema keywords to Optional
        * Refined regex for various formats

--------------------------------------------------------------------------------
                                ARP
--------------------------------------------------------------------------------
* IOSXR
    * Updated ShowArpTrafficDetail to parse drop_adj key from output


--------------------------------------------------------------------------------
                                VTP
--------------------------------------------------------------------------------
* IOSXE:
    * Updated ShowVtpStatusSchema to:
        * Changed schema keywords to Optional

--------------------------------------------------------------------------------
                                IPV6
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowIpv6NdInterfaceVrfAll to parse more varied output