* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 20.4          |

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
    * Added ShowInventory in subdirectory 'C9300' for
        * show inventory

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
    * Added ShowBgpSummary for:
        * show bgp summary
    * Added ShowOspfNeighbor for:
        * show ospf neighbor
    * Added ShowRoute for:
        * show route
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
    * Added ShowArpNoResolve for:
        * show arp no-resolve
    * Added ShowOspfDatabase for:
        * show ospf database
    * Added ShowOspfDatabaseSummary for:
        * show ospf database summary
    * Added ShowOspfDatabaseExternalExtensive for:
        * show ospf database external extensive
    * Added ShowOspfOverview for:
        * show ospf overview
    * Added ShowOspfOverviewExtensive for:
        * show ospf overview extensive
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
        * show route protocol {protocol} table {table} extensive {destination}
    * Added ShowOspf3Database for:
        * show ospf3 database
    * Added Ping for:
        * ping {addr}
        * ping {addr} count {count}
    * Added ShowOspf3DatabaseExternalExtensive for:
        * show ospf3 database external extensive
    * Added ShowOspf3InterfaceExtensive for:
        * show ospf3 interface extensive
    * Added ShowRouteInstanceDetail for:
        * show route instance detail
    * Added ShowRouteSummary for:
        * show route summary
    * Added ShowRouteAdvertisingProtocol for:
        * show route advertising-protocol {protocol} {neighbor}
    * Added ShowRouteReceiveProtocol for:
        * show route receive-protocol {protocol} {peer}
    * Added ShowRouteForwardingTableSummary for:
        * show route forwarding-table summary
    * Added ShowOspf3DatabaseExtensive for:
        * show ospf3 database extensive
    * Added ShowSystemBuffers for:
        * show system buffers
    * Added ShowSystemBuffersNoForwarding for:
        * show system buffers no-forwarding
    * Added ShowSystemCommit for:
        * show system commit
    * Added ShowSystemQueues for:
        * show system queues
    * Added ShowSystemStorage for:
        * show system storage
    * Added ShowSystemStorageNoForwarding for:
        * show system storage no-forwarding
    * Added ShowSystemQueuesNoForwarding for:
        * show system queues no-forwarding
    * Added ShowPfeStatisticsTraffic for:
        * show pfe statistics traffic
    * Added ShowSystemUpdate for:
        * show system uptime
    * Added ShowSystemUpdateNoForwarding for:
        * show system uptime no-forwarding
    * Added ShowSystemCoreDumps for:
        * show system core-dumps
    * Added ShowSystemCoreDumpsNoForwarding for:
        * show system core-dumps no-forwarding
    * Added ShowSystemUsers for:
        * show system users
    * Added ShowChassisFpcDetail for:
        * show chassis fpc detail
    * Added ShowChassisFirmware for:
        * show chassis firmware
    * Added ShowChassisFirmwareNoForwarding for:
        * show chassis firmware no-forwarding
    * Added ShowChassisEnvironmentRoutingEngine for:
        * show chassis environment routing-engine
    * Added ShowChassisHardware for:
        * show chassis hardware
    * Added ShowChassisHardwareDetail for:
        * show chassis hardware detail
    * Added ShowChassisHardwareDetailNoForwarding for:
        * show chassis hardware detail no-forwarding
    * Added ShowChassisHardwareExtensive for:
        * show chassis hardware extensive
    * Added ShowChassisHardwareExtensiveNoForwarding for:
        * show chassis hardware extensive no-forwarding
    * Added ShowOspfDatabaseAdvertisingRouterSelfDetailSchema for:
        * show ospf database advertising-router self detail
    * Added ShowOspfInterfaceExtensiveSchema for:
        * show ospf interface extensive
    * ShowOspfNeighborExtensive
        * show ospf neighbor extensive
    * ShowOspfNeighborDetail
        * show ospf neighbor detail
    * Added ShowSnmpMibWalkSystem for:
        * show snmp mib walk system
    * Added ShowFirewall for:
        * show firewall
    * Added ShowFirewallCounterFilter for:
        * show firewall counter filter v6_local-access-control v6_last_policer
    * Added ShowOspfDatabaseExtensive for:
        * show ospf database extensive
    * ShowTaskReplication for:
        * show task replication
    * Added ShowVersion in show_platform.py for:
        * show version
    * Added ShowIpv6Neighbors for:
        * show ipv6 neighbors



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
    * Updated ShowRoute
        * Updated regex and modified parser class to support various device outputs.

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
    * Update ShowIpInterface:
        * Fixed the typo in the keys 'broadcast_address' and 'security_level'

* NXOS
    * Updated ShowAccessLists
        * Update regex to support various outputs.
    * Updated ShowInterface
        * Update regex to cover both 'IP' and 'ip', both 'Rx' and 'RX'
        * Update regex to support various outputs.
        * Clean code and correctly assign values to the key 'enabled'
    * Updated ShowIpRoute
        * Add keys into the schema, modify regex
    * Updated ShowRouting
        * Change its parent class from ShowRoutingVrfAll into ShowIpRoute
    * Update ShowIpInterfaceVrfAll
        * Changed wccp_* keys to be optional from mandatory to support new output
        * Updated regex to support device outputs that contain secondary interfaces
    * Update ShowPlatformInternalHalPolicyRedirdst:
        * Changed keys rewrite_mac, rewrite_vnid, outgoing_l2_ifindex,
            outgoing_ifname, packets_hash as optional
    * Update ShowSystemInternalSysmgrServiceName:
        * Enhanced 'tag' key to support more output

* IOSXR
    * Update ShowBgpInstanceSummary
        * Update regex to support various output
    * Update ShowRouteIpv4
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
    * Update Ping
        * only the keys are changed into Optional
    * Update ShowRouteProtocol
        * Update regex to support various output

