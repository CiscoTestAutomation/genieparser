* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* IOSXR
    * Added ShowControllersNpuInterfaceInstanceLocation for:
        * show controllers npu {npu} interface {interface} instance {instance} location {location}
    * Added ShowControllersFiaDiagshellDiagEgrCalendarsLocation for:
        * show controllers fia diagshell {diagshell} "diag egr_calendars" location {location}
    * Added ShowControllersFiaDiagshellDiagCosqQpairEgpMap for:
        * show controllers fia diagshell 0 "diag cosq qpair egq map" location all
    * Added ShowInstallSummary for
        * show install summary

* IOSXE
    * Added ShowIpBgpRouteDistributer for:
        * show ip bgp {route}
        * show ip bgp {address_family}
    * Added ShowLldpNeighbors for
        * show lldp neighbors
    * Added ShowInstallSummary for
        * show install summary
    * Added ShowPlatformIntegrity for
        * show platform integrity
    * Added ShowDmvpn for
        * show dmvpn
        * show dmvpn interface {interface}

* NXOS
    * Added ShowIpRouteSummary for:
        * show ip route summary
        * show ip route summary vrf {vrf}
    * Added ShowInterfaceStatus for:
        * show interface status
        * show interface {interface} status
* ASA
    * Added ShowVPNSessionDBSummary for:
        * show vpn-sessiondb summary
    * Added ShowVPNLoadBalancing for:
        * show vpn load-balancing
    * Added ShowIpLocalPool for:
        * show ip local pool {pool}
    * Added ShowServicePolicy for:
        * show service-policy
    * Added ShowVpnSessiondb for:
        * show vpn-sessiondb
        * show vpn-sessiondb anyconnect
        * show vpn-sessiondb anyconnect sort inactivity
        * show vpn-sessiondb webvpn
    * Added ShowResourceUsage for:
        * show resource usage
    * Added ShowAspDrop for
        * show asp drop

* JUNOS
    * Added ShowBgpGroupBrief for:
        * show bgp group brief
    * Added ShowBgpGroupBriefNoMore for:
        * show bgp group brief | no-more
    * Added ShowBgpGroupDetail for:
        * show bgp group detail
    * Added ShowBgpGroupDetailNoMore for:
        * show bgp group detail | no-more
    * Added ShowBgpGroupSummary for:
        * show bgp group summary
    * Added ShowBgpGroupSummaryNoMore for:
        * show bgp group summary | no-more
    * Added ShowOspfNeighbor for:
        * show ospf neighbor
    * Added ShowRouteProtocol for:
        * show route protocol {protocol}
        * show route protocol {protocol} {ip_address}
        * show route protocol {protocol} table {table}
    * Added ShowRouteProtocolNoMore for:
        * show route protocol {protocol} {ip_address} | no-more
    * Added ShowOspf3Interface for:
        * show ospf3 interface
    * Added ShowOspf3Neighbor for:
        * show ospf3 neighbor
    * Added ShowOspf3NeighborExtensive for:
        * show ospf3 neighbor extensive
    * Added ShowArp for:
        * show arp
    * Added ShowArpNoMore for:
        * show arp | no-more
    * Added ShowOspf3Overview for:
        * show ospf3 overview
    * Added ShowOspf3OverviewExtensive for:
        * show ospf3 overview extensive
    * Added ShowKrtState for:
        * show krt state
    * Added ShowKrtQueue for:
        * show krt queue
    * Added ShowRouteProtocolExtensive for:
        * show route protocol {protocol} extensive
        * show route protocol {protocol} table {table} extensive
    * Added ShowOspf3Database for:
        * show ospf3 database
    * Added Ping for:
        * ping {addr}
        * ping {addr} count {count}
    * Added ShowOspf3DatabaseExternalExtensive for:
        * show ospf3 database external extensive
    * Added ShowOspf3InterfaceExtensive for:
        * show ospf3 interface extensive
    * Added ShowSystemBuffer for:
        * show system buffers
    * Added ShowPfeStatisticsTraffic for:
        * show pfe statistics traffic
    * Added ShowSystemUsers for:
        * show system users
    * Added ShowChassisFpcDetail for:
        * show chassis fpc detail


--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* ASA
    * Updated ShowVPNSessionDBSummary:
        * Added keys to the schema
        * Moved show command 'show vpn-sessiondb' into this class
        * Updated some mandatory keys's state in schema into Optional
    * Updated ShowVpnSessiondbSuper:
        * Added keys to the schema
        * Updated regex to support output in show vpn-sessiondb anyconnect

* IOSXE
    * Updated ShowMplsForwardingTable:
        * Modified wrong regex
    * Updated ShowIpCef:
        * Modified regex to support SID
        * update regex and schema to support local sid
    * Updated ShowMplsForwardingTableDetail:
        * show mpls forwarding-table {route} detail
    * Updated Traceroute:
        * Updated regex to support various outputs.
        * Updated schema and regex to support AS number.
    * Updated ShowBootvar
        * Fixed crash
        * Added unittest
    * Updated ShowInterfacesStatus
        * Change key mandatory 'type' into optional
        * Updated regex to support various output
    * Updated ShowNveEthernetSegment
        * Updated regex to support various output
    * Updated ShowIpInterfaceVrfAll
        * Update regex to support more various output
    * Update ShowEnvironment
        * Update regex to support more various output
    * Update ShowIpNatTranslations
        * Fix typo in cli_command
    * Update ShowNveInterfaceDetail
        * Update regex to support more various output
    * Update ShowIpOspfNeighborDetail
        * Update regex to support more various output
    * Update ShowCdpNeighborsDetail
        * Change key mandatory 'capabilities' into optional
    * Update ShowMacAddressTable
        * Update regex to support various output
    * Update ShowAccessLists
        * Update regex to support various output
    * Update ShowVrf
        * Update regex to support various output
    * Update ShowLldpEntry
        * Fix typo in the code
    * Update ShowIpMsdpPeer
        * Change key 'peer_as' into Optional to support various outputs
    * Update ShowBgpAllNeighbors:
        * Update regex to support various outputs.
    * Update ShowIpBgpAllDetail:
        * Fix the way that assigns value to key 'vrf'
    * Update ShowStandbyAll:
        * Update regex to support various outputs.
    * Update ShowInventory:
        * Added regex to support various outputs.
* NXOS
    * Updated ShowAccessLists
        * Update regex to support various outputs.
    * Updated ShowInterface
        * Update regex to cover both 'IP' and 'ip', both 'Rx' and 'RX'
        * Clean code and correctly assign values to the key 'enabled'
    * Updated ShowIpRoute
        * Add keys into the schema, modify regex
    * Updated ShowRouting
        * Change its parent class from ShowRoutingVrfAll into ShowIpRoute
    * Update ShowIpInterfaceVrfAll
        * Changed wccp_* keys to be optional from mandatory to support new output
    * Update ShowPlatformInternalHalPolicyRedirdst:
        * Changed keys rewrite_mac, rewrite_vnid, outgoing_l2_ifindex,
            outgoing_ifname, packets_hash as optional
    * Update ShowSystemInternalSysmgrServiceName:
        * Enhanced 'tag' key to support more output

* IOSXR
    * Update ShowBgpInstanceSummary
        * Update regex to support various output

* IOS
    * Update ShowInterfaces
        * Update regex to support various output
* JUNOS
    * Update ShowInterfacesTerse
        * show interfaces terse {interface}
        * show interfaces {interface} terse
    * Update ShowInterfacesTerseInterface
        * show interfaces terse {interface}

--------------------------------------------------------------------------------
                                common.py
--------------------------------------------------------------------------------
* updated _find_command to find command for nxos in aci mode
