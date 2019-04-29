| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 19.4.0        |

--------------------------------------------------------------------------------
                                   MSDP
--------------------------------------------------------------------------------
* IOSXE
  * Add ShowIpMsdpPeer for:
    show ip msdp peer
    show ip msdp vrf {vrf} peer
  * Add ShowIpMsdpSaCache for:
    show ip msdp sa-cache
    show ip msdb vrf {vrf} sa-cache
--------------------------------------------------------------------------------
                                   POLICY-MAP
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowPolicyMapControlPlane for:
        show policy-map control-plane
    * Add ShowPolicyMapInterface for:
        show policy-map interface {interface}
        show policy-map interface
    * Add ShowPolicyMapInterfaceInput for:
        show policy-map interface {interface} input class {class_name}
        show policy-map interface {interface} input
    * Add ShowPolicyMapInterfaceOutput for:
        show policy-map interface {interface} output class {class_name}
        show policy-map interface {interface} output
    * Add ShowPolicyMapInterfaceClass for:
        show policy-map interface class {class_name}
    * Add ShowPolicyMapTargetClass for:
        show policy-map target service-group {num}
    * Add ShowPolicyMap for :
        show policy-map
        show policy-map {name}

--------------------------------------------------------------------------------
                                   BGP
--------------------------------------------------------------------------------
* IOSXE
  * Removed support for cmd in SuperParser classes

--------------------------------------------------------------------------------
                                   ISIS
--------------------------------------------------------------------------------
* IOSXR
  * Add ShowIsisAdjacency for:
        show isis adjacency
  * Add ShowIsisNeighbors for:
        show isis neighbors
* IOSXE
  * Add ShowIsisNeighbors for:
        show isis neighbors

--------------------------------------------------------------------------------
                                   
--------------------------------------------------------------------------------
* IOSXE
  * Add ShowXconnectAll for:
        show xconnect all

--------------------------------------------------------------------------------
                                   MPLS
--------------------------------------------------------------------------------
* IOSXR
  * Add ShowMplsLdpNeighborBrief for:
        show mpls ldp neighbor brief

--------------------------------------------------------------------------------
                                   MRIB
--------------------------------------------------------------------------------
* IOSXR
  * Add ShowMribVrfRouteSummary for:
        show mrib vrf route summary

--------------------------------------------------------------------------------
                                   PLATFORM
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowInstallInactiveSummary for:
        show install inactive summary
    * Add ShowInstallCommitSummary for:
        show install commit summary
* IOSXE
    * ShowInventory enhanced to support ASR901 platform
    * Updated ShowPlatform to support different models
* IOS
    * Add ShowEnvironment for:
        show environment
    * Add ShowEnvironmentAll for:
        show environment all
    * Add ShowModule for:
        show module
    * Add ShowSwitch for:
        show switch
    * Add ShowSwitchDetail for:
        show switch detail

--------------------------------------------------------------------------------
                                   RUN
--------------------------------------------------------------------------------
* IOSXR
  * Add ShowRunKeyChain for:
        show run key chain
  * Add ShowRunRouterIsis for:
        show run router isis

--------------------------------------------------------------------------------
                                   BGP
--------------------------------------------------------------------------------
* IOSXE
  * ShowBgpNeighborSuperParser enhanced to support 'Multisession Capability'
  * Updated ShowBgpAllNeighbors to support different session states
* NXOS
  * Add ShowBgpL2vpnEvpnNeighborsAdvertisedRoutes for:
    show bgp l2vpn evpn neighbors {neighbor} advertised-routes

* NXOS
  * Add ShowBgpVrfIpv4Unicast for:
      * show bgp vrf {vrf} ipv4 unicast

----------------------------------------------------------------------------------
                                  EIGRP
----------------------------------------------------------------------------------
* IOSXE
    * Add ShowIpEigrpNeighbors for:
            show ip eigrp neighbors
            show ip eigrp vrf {vrf} neighbors

      * Add ShowIpv6EigrpNeighbors for:
            show ipv6 eigrp neighbors
            show ipv6 eigrp vrf {vrf} neighbors

      * Add ShowIpEigrpNeighborsDetail for:
            show ip eigrp neighbors detail
            show ip eigrp vrf {vrf} neighbors detail

      * Add ShowIpv6EigrpNeighborsDetail for:
            show ipv6 eigrp neighbors detail
            show ipv6 eigrp vrf {vrf} neighbors detail

* IOSXR
    * Add ShowEigrpIpv4Neighbors for:
            show eigrp ipv4 neighbors
            show eigrp ipv4 vrf {vrf} neighbors
    * Add ShowEigrpIpv6Neighbors for:
            show eigrp ipv6 neighbors
            show eigrp ipv6 vrf {all} neighbors
    * Add ShowEigrpIpv4NeighborsDetail for:
            show eigrp ipv4 neighbors detail
            show eigrp ipv4 vrf {vrf} neighbors detail
    * Add ShowEigrpIpv6NeighborsDetail for:
            show eigrp ipv6 neighbors detail
            show eigrp ipv6 vrf {all} neighbors detail
* NXOS
    * Add ShowIpv4EigrpNeighbors for:
        show ip eigrp neighbors vrf {vrf}
    * Add ShowIpv6EigrpNeighbors for:
        show ipv6 eigrp neighbors vrf {all}
    * Add ShowIpv4EigrpNeighborsDetail for:
        show ip eigrp neighbors detail vrf {all}
    * Add ShowIpv6EigrpNeighborsDetail for:
        show ipv6 eigrp neighbors detail vrf {all}

----------------------------------------------------------------------------------
                                   CDP
----------------------------------------------------------------------------------
* IOSXE
  * Add ShowCdpNeighbors for:
      show cdp neighbors
  * Add ShowCdpNeighborsDetail for:
      show cdp neighbors detail
* NXOS
  * Add ShowCdpNeighbors for:
      show cdp neighbors
  * Add ShowCdpNeighborsDetail for:
      show cdp neighbors detail

--------------------------------------------------------------------------------
                                   TRACEROUTE
--------------------------------------------------------------------------------
* IOSXE
  * Enhanced Traceroute to parse URL along with the Ip Address

--------------------------------------------------------------------------------
                                   LAG
--------------------------------------------------------------------------------
* IOSXE
    * Enhancement on ShowEtherchannelSummary for:
        show etherchannel summary

* IOS
    * Add ShowLacpSysId for:
        show lacp sys-id
    * Add ShowLacpCounters for:
        show lacp counters
        show lacp {channel-group} counters
    * Add ShowLacpInternal for:
        show lacp internal
        show lacp {channel-group} internal
    * Add ShowLacpNeighbor for:
        show lacp neighbor
        show lacp {channel-group} neighbor
    * Add ShowPagpCounters for:
        show pagp counters
        show pagp {channel-group} counters
    * Add ShowPagpNeighbor for:
        show pagp neighbor
        show pagp {channel-group} neighbor
    * Add ShowPagpInternal for:
        show pagp internal
        show pagp {channel-group} internal
    * Add ShowEtherchannelSummary for:
        show etherchannel summary
    * Add ShowEtherChannelLoadBalancing for:
        show etherchannel load-balancing
    * Add ShowLacpNeighborDetail for:
        show lacp neighbor detail

* IOSXR
    * Add ShowLacpSystemId for:
        show lacp system-id
    * Add ShowBundle for:
        show lacp bundle
    * Add ShowLacp for:
        show lacp

--------------------------------------------------------------------------------
                                   INTERFACE
--------------------------------------------------------------------------------
* IOS
    * Add ShowInterfacesCounters for:
        show interfaces {interface} counters
    * Add ShowInterfacesSwitchport for:
        show interfaces switchport
    * Add ShowInterfacesTrunk for:
        show interfaces trunk
    * Add ShowInterfacesStats for:
        show interface {interface} stats
        show interface stats

* IOSXE
    * Update ShowInterfaces to support carrier delay

--------------------------------------------------------------------------------
                                  LISP
--------------------------------------------------------------------------------
* IOS
    * Add ShowLispSession for:
        show lisp session
    * Add ShowLispPlatform for:
        show lisp platform
    * Add ShowLispExtranet for:
        show lisp all extranet {extranet} instance-id {instance_id}
    * Add ShowLispDynamicEidDetail for:
        show lisp all extranet {extranet} instance-id {instance_id}
    * Add ShowLispService for:
        show lisp all instance-id {instance_id} {service}
        show lisp all service {service}
    * Add ShowLispServiceMapCache for:
        show lisp all instance-id {instance_id} {service} map-cache
    * Add ShowLispServiceRlocMembers for:
        show lisp all instance-id {instance_id} {service} rloc members
    * Add ShowLispServiceSmr for:
        show lisp all instance-id {instance_id} {service} smr
    * Add ShowLispServiceSummary for:
        show lisp all {service} summary
    * Add ShowLispServiceDatabase for:
        show lisp all instance-id {instance_id} {service} dabatase
    * Add ShowLispServiceServerSummary for:
        show lisp all instance-id {instance_id} {service} server summary
    * Add ShowLispServiceServerDetailInternal for:
        show lisp all instance-id {instance_id} {service} server detail internal
    * Add ShowLispServiceStatistics for:
        show lisp all instance-id {instance_id} {service} statistics

--------------------------------------------------------------------------------
                                   MPLS LDP
--------------------------------------------------------------------------------

* IOS
    * Add ShowMplsLdpParameters for:
          show mpls ldp parameters
    * Add ShowMplsLdpNsrStatistic for:
          show mpls ldp nsr statistics
    * Add ShowMplsLdpNeighbor for:
          show mpls ldp neighbor
          show mpls ldp neighbor vrf {vrf}
    * Add ShowMplsLdpNeighborDetail for:
          show mpls ldp neighbor detail
          show mpls ldp neighbor vrf {vrf} detail
    * Add ShowMplsLdpBindings for:
          show mpls ldp bindings
          show mpls ldp bindings all
          show mpls ldp bindings all detail
    * Add ShowMplsLdpCapabilities for:
          show mpls ldp capabilities
          show mpls ldp capabilities all
    * Add ShowMplsLdpDiscovery for:
          show mpls ldp discovery
          show mpls ldp discovery detail
          show mpls ldp discovery all
          show mpls ldp discovery all detail
          show mpls ldp discovery vrf {vrf}
          show mpls ldp discovery vrf {vrf} detail
    * Add ShowMplsLdpIgpSync for:
          show mpls ldp igp sync
          show mpls ldp igp sync all
          show mpls ldp igp sync interface {interface}
          show mpls ldp igp sync vrf {vrf}
    * Add ShowMplsForwardingTable for:
          show mpls forwarding-table
          show mpls forwarding-table detail
          show mpls forwarding-table vrf {vrf}
          show mpls forwarding-table vrf {vrf} detail
    * Add ShowMplsInterface for:
          show mpls interfaces
          show mpls interfaces {interface}
          show mpls interfaces {interface} detail
          show mpls interfaces detail

--------------------------------------------------------------------------------
                                   SESSION
--------------------------------------------------------------------------------
* IOS
    * Add ShowLine for:
        show line
    * Add ShowUsers for:
        show users

--------------------------------------------------------------------------------
                                   ACCESS
--------------------------------------------------------------------------------
* IOS
    * Add ShowAccessSession for:
        show access-session

--------------------------------------------------------------------------------
                                   SYSTEM
--------------------------------------------------------------------------------
* IOS
    * Add ShowClock for:
        show clock

--------------------------------------------------------------------------------
                                   VTP
--------------------------------------------------------------------------------
* IOS
    * Add ShowVtpStatus for:
        show vtp status

--------------------------------------------------------------------------------
                                   SNMP
--------------------------------------------------------------------------------
* IOS
    * Added ShowSnmpMib for:
        'show snmp mib'

--------------------------------------------------------------------------------
                                   RPF
--------------------------------------------------------------------------------
* IOS
    * Add ShowIpRpf for:
        show ip rpf {mroute address}
        show ip rpf vrf {vrf} {mroute address}
    * Add ShowIpv6Rpf for:
        show ipv6 rpf {mroute address}
        show ipv6 rpf vrf {vrf} {mroute address}

--------------------------------------------------------------------------------
                                   ROUTING
--------------------------------------------------------------------------------
* IOS
    * Add ShowIpv6RouteWord for:
        show ipv6 route {Hostname or A.B.C.D}
        show ipv6 route vrf {vrf} {Hostname or A.B.C.D}
* NXOS
    * Updated ShowRoutingIpv6VrfAll to support different vrf
    * Updated ShowIpRoute for:
        show ip route
        show ip route vrf {vrf}
        show ip route vrf all
    * Updated ShowIpv6Route for:
        show ipv6 route
        show ipv6 route vrf {vrf}
        show ipv6 route vrf all
* IOSXR
    * Add ShowRouteIpv4 for:
        show route ipv4
        show route vrf {vrf} ipv4
    * Add ShowRouteIpv6 for:
        show route ipv6
        show route vrf {vrf} ipv6

--------------------------------------------------------------------------------
                                   ISSU
--------------------------------------------------------------------------------
* IOS
    * Add ShowIssuStateDetail for:
          show issu state detail
    * Add ShowIssuRollbackTimer for:
          show issu rollback-timer

--------------------------------------------------------------------------------
                                   POWER
--------------------------------------------------------------------------------
* IOS
    * Add ShowStackPower for:
          show stack-power
    * Add ShowPowerInlineInterface for:
          show power inline {interface}

--------------------------------------------------------------------------------
                                   DOT1X
--------------------------------------------------------------------------------
* IOS
    * Add ShowDot1xAllStatistics for:
          show dot1x all statistics

--------------------------------------------------------------------------------
                                   CRYPTO
--------------------------------------------------------------------------------
* IOS
    * Add ShowCryptoPkiCertificates for:
          show crypto pki certificates
          show crypto pki certificates <WORD>

--------------------------------------------------------------------------------
                                   SERVICE
--------------------------------------------------------------------------------
* IOS
    * Add ShowServiceGroupTrafficStats for:
        show service-group traffic-stats
        show service-group traffic-stats {group}

--------------------------------------------------------------------------------
                                   FDB
--------------------------------------------------------------------------------
* IOS
    * Add ShowMacAddressTable for:
        show mac address-table
    * Add ShowMacAddressTableAgingTime for:
        show mac address-table aging-time
    * Add ShowMacAddressTableLearning for:
        show mac address-table learning

--------------------------------------------------------------------------------
                                   BFD
--------------------------------------------------------------------------------
* IOS
    * Add ShowBfdNeighborsDetails for:
        show bfd neighbors details
        show bfd neighbors client {client} details

----------------------------------------------------------------------------------
                                   ARP
----------------------------------------------------------------------------------
* IOS
    * Add ShowArpApplication for:
        show arp application
    * Add ShowArpSummary for:
        show arp summary
    * Add ShowArp
        show arp
* NXOS
    * Updated ShowIpArp for:
        show ip arp
        show ip arp {vrf}
        show ip arp all

--------------------------------------------------------------------------------
                                   L2VPN
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowMplsL2TransportVC for:
        show mpls l2transport vc
* IOS
    * Add ShowMplsL2TransportVC for:
        show mpls l2transport vc

----------------------------------------------------------------------------------
                                   ISIS
----------------------------------------------------------------------------------
* IOSXE
    * Add ShowClnsInterface for:
        show clns interface
        show clns interface {interface}
    * Add ShowClnsProtocol for:
        show clns protocol
    * Add ShowClnsNeighborDetail for:
        show clns neighbor detail
    * Add ShowClnsIsNeighborDetail for:
        show clns is-neighbor detail
    * Add ShowClnsTraffic for:
        show clns traffic
    * Add ShowIsisHostname for:
        show isis hostname
    * Add ShowIsisLspLog for:
        show isis lsp-log
    * Add ShowIsisDatabaseDetail for:
        show isis database detail

----------------------------------------------------------------------------------
                                   ISIS
----------------------------------------------------------------------------------
* IOSXE
    * Add ShowIpCef for :
            show ip cef
            show ip cef vrf {vrf}
            show ip cef {prefix}
            show ip cef vrf {vrf} {prefix}
    * Add ShowIpv6Cef for :
            show ipv6 cef
            show ipv6 cef vrf {vrf}
            show ipv6 cef {prefix}
            show ipv6 cef vrf {vrf} {prefix}

----------------------------------------------------------------------------------
                                 OSPF
----------------------------------------------------------------------------------
* IOSXR
  * Updated ShowOspfVrfAllInclusiveNeighborDetail to have bfd mode/status

----------------------------------------------------------------------------------
                                 PROTOCOLS
----------------------------------------------------------------------------------
* IOSXE
  * Fixed ShowProtocols for bgp and ospf

* IOS
  * Add ShowIpProtocolsSectionRip for:
      show ip protocols | sec rip
      show ip protocols vrf {vrf} | sec rip
  * Add ShowIpv6ProtocolsSectionRip for:
      show ipv6 protocols | sec rip
      show ipv6 protocols vrf {vrf} | sec rip
* IOSXR
  * Fixed ShowProtocolsAfiAllAll for bgp and ospf

----------------------------------------------------------------------------------
                                 ACL
----------------------------------------------------------------------------------
* IOSXE
  * Updated ShowAccessLists
  * Add ShowIpAccessLists for :
          show ip access-lists
          show ip access-lists {acl}
  * Add ShowIpv6AccessLists for :
          show ipv6 access-list
          show ipv6 access-list {acl}

* IOSXR
    * Add ShowAclAfiAll for:
        show access-lists afi-all
    * Add ShowAclEthernetServices for:
        show access-lists ethernet-services

----------------------------------------------------------------------------------
                                   LLDP
----------------------------------------------------------------------------------
* IOSXR
    * Add ShowLldp for:
        show lldp
    * Add ShowLldpEntry for:
        show lldp entry *
    * Add ShowLldpNeighborsDetail for:
        show lldp neighbors detail
    * Add ShowLldpTraffic for:
        show lldp traffic
    * Add ShowLldpInterface for:
        show lldp interface
* IOSXE
    * Add ShowLldpNeighborsDetail for:
        show lldp neighbors detail
----------------------------------------------------------------------------------
                                   IGMP
----------------------------------------------------------------------------------
* IOS
    * Add ShowIpIgmpSsmMapping for:
        show ip igmp ssm-mapping <WORD>
        show ip igmp vrf <WORD> ssm-mapping <WORD>

----------------------------------------------------------------------------------
                                   RIP
----------------------------------------------------------------------------------
* IOS
    * Add ShowIpRipDatabase for:
        show ip rip database
        show ip rip database vrf {vrf}
    * Add ShowIpv6RipDatabase for:
        show ipv6 rip database
        show ipv6 rip database vrf {vrf}
    * Add ShowIpv6Rip for:
        show ipv6 rip
        show ipv6 rip vrf {vrf}
* IOSXR
    * Add ShowRip for:
        show rip
        show rip vrf {vrf}
    * Add ShowRipStatistics for:
        show rip statistics
        show rip vrf {vrf} statistics
    * Add ShowRipDatabase for:
        show rip database
        show rip vrf {vrf} database
    * Add ShowRipInterface for:
        show rip interface
        show rip vrf {vrf} interface

--------------------------------------------------------------------------------
                                PREFIX_LIST
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowRplPrefixSet for:
        show rpl prefix-set
        show rpl prefix-set {name}

--------------------------------------------------------------------------------
                                L2ROUTE
--------------------------------------------------------------------------------
* NXOS
    * Add ShowL2routeEvpnMac for:
        show l2route evpn mac evi {evi}

--------------------------------------------------------------------------------
                                VXLAN
--------------------------------------------------------------------------------
* NXOS
    * Add ShowL2routeEvpnMacIpAll for:
        show l2route evpn mac-ip all
    * Add ShowL2routeEvpnMacIpEvi for:
        show l2route evpn mac-ip evi {evi}

--------------------------------------------------------------------------------
                                VRF
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowVrfDetail to support more varied output


| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 19.0.3        |

* Fixing logging new stream handler issue.


| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 19.0.2        |

--------------------------------------------------------------------------------
                                   BGP
--------------------------------------------------------------------------------
* IOSXE
    * Added parsers for:
        * 'show bgp all'
        * 'show bgp {address_family} all'
        * 'show bgp {address_family} rd {rd}'
        * 'show bgp {address_family} vrf {vrf}'
        * 'show ip bgp all'
        * 'show ip bgp {address_family} all'
        * 'show ip bgp'
        * 'show ip bgp {address_family}'
        * 'show ip bgp {address_family} rd {rd}'
        * 'show ip bgp {address_family} vrf {vrf}'
        * 'show bgp all detail'
        * 'show ip bgp all detail'
        * 'show bgp {address_family} vrf {vrf} detail'
        * 'show bgp {address_family} rd {rd} detail'
        * 'show ip bgp {address_family} vrf {vrf} detail'
        * 'show ip bgp {address_family} rd {rd} detail'
        * 'show bgp summary'
        * 'show bgp {address_family} summary'
        * 'show bgp {address_family} vrf {vrf} summary'
        * 'show bgp {address_family} rd {rd} summary'
        * 'show bgp all summary'
        * 'show bgp {address_family} all summary'
        * 'show ip bgp summary'
        * 'show ip bgp {address_family} summary'
        * 'show ip bgp {address_family} vrf {vrf} summary'
        * 'show ip bgp {address_family} rd {rd} summary'
        * 'show ip bgp all summary'
        * 'show ip bgp {address_family} all summary'
        * 'show bgp all neighbors'
        * 'show bgp all neighbors {neighbor}'
        * 'show bgp {address_family} all neighbors'
        * 'show bgp {address_family} all neighbors {neighbor}'
        * 'show bgp neighbors'
        * 'show bgp neighbors {neighbor}'
        * 'show bgp {address_family} neighbors'
        * 'show bgp {address_family} neighbors {neighbor}'
        * 'show bgp {address_family} vrf {vrf} neighbors'
        * 'show bgp {address_family} vrf {vrf} neighbors {neighbor}'
        * 'show ip bgp all neighbors',
        * 'show ip bgp all neighbors {neighbor}'
        * 'show ip bgp {address_family} all neighbors'
        * 'show ip bgp {address_family} all neighbors {neighbor}'
        * 'show ip bgp neighbors'
        * 'show ip bgp neighbors {neighbor}'
        * 'show ip bgp {address_family} neighbors'
        * 'show ip bgp {address_family} neighbors {neighbor}'
        * 'show ip bgp {address_family} vrf {vrf} neighbors'
        * 'show ip bgp {address_family} vrf {vrf} neighbors {neighbor}'
        * 'show bgp all neighbors {neighbor} advertised-routes'
        * 'show bgp {address_family} all neighbors {neighbor} advertised-routes'
        * 'show bgp neighbors {neighbor} advertised-routes'
        * 'show bgp {address_family} neighbors {neighbor} advertised-routes'
        * 'show ip bgp all neighbors {neighbor} advertised-routes'
        * 'show ip bgp {address_family} all neighbors {neighbor} advertised-routes'
        * 'show ip bgp neighbors {neighbor} advertised-routes'
        * 'show ip bgp {address_family} neighbors {neighbor} advertised-routes'
        * 'show bgp all neighbors {neighbor} received-routes'
        * 'show bgp {address_family} all neighbors {neighbor} received-routes'
        * 'show bgp neighbors {neighbor} received-routes'
        * 'show bgp {address_family} neighbors {neighbor} received-routes'
        * 'show ip bgp all neighbors {neighbor} received-routes'
        * 'show ip bgp {address_family} all neighbors {neighbor} received-routes'
        * 'show ip bgp neighbors {neighbor} received-routes'
        * 'show ip bgp {address_family} neighbors {neighbor} received-routes'
        * 'show bgp all neighbors {neighbor} routes'
        * 'show bgp {address_family} all neighbors {neighbor} routes'
        * 'show bgp neighbors {neighbor} routes'
        * 'show bgp {address_family} neighbors {neighbor} routes'
        * 'show ip bgp all neighbors {neighbor} routes'
        * 'show ip bgp {address_family} all neighbors {neighbor} routes'
        * 'show ip bgp neighbors {neighbor} routes'
        * 'show ip bgp {address_family} neighbors {neighbor} routes'

--------------------------------------------------------------------------------
                                   POLICY MAP
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowPolicyMapControlPlane Parser for:
       'show policy map control plane'

--------------------------------------------------------------------------------
                                   MONITOR
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowMonitor Parser for:
       'show monitor'
       'show monitor session all'
       'show monitor session {session}'
       'show monitor capture'


--------------------------------------------------------------------------------
                                   OSPF
--------------------------------------------------------------------------------
* IOSXE
    * Added parsers:
        * ShowIpOspfDatabase
        * ShowIpOspfMaxMetric
        * ShowIpOspfTraffic
    * Updated parsers:
        * ShowIpOspfMplsLdpInterface
        * ShowIpOspfDatabaseRouter
        * ShowIpOspfDatabaseExternal
        * ShowIpOspfDatabaseNetwork
        * ShowIpOspfDatabaseSummary
        * ShowIpOspfDatabaseOpaqueArea

--------------------------------------------------------------------------------
                                   SNMP
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowSnmpMib for:
        'show snmp mib'

--------------------------------------------------------------------------------
                                   PLATFORM
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowPlatformHardwarePlim for;
        'show platform hardware port {x/x/x} plim statistics'
        'show platform hardware slot {x} plim statistics'
        'show platform hardware slot {x} plim statistics internal'
        'show platform hardware subslot {x/x} plim statistics'
    * Add ShowPlatformHardware for 'show platform hardware qfp active infrastructure bqs queue output default all'
    * Add ShowVersionRp for;
        show version RP active running
        show version RP active installed
        show version RP active provisioned
        show version RP standby running
        show version RP standby installed
        show version RP standby provisioned
    * Add ShowPlatformPower for 'show platform power'
    * Add ShowPlatformHardwareQfpBqsOpmMapping for;
        show platform hardware qfp active bqs {x} opm mapping
        show platform hardware qfp standby bqs {x} opm mapping
    * Add ShowPlatformHardwareQfpBqsIpmMapping for;
        show platform hardware qfp active bqs {x} ipm mapping
        show platform hardware qfp standby bqs {x} ipm mapping
    * Add ShowPlatformHardwareQfpInterfaceIfnameStatistics for;
        show platform hardware qfp active interface if-name {interface} statistics
        show platform hardware qfp standby interface if-name {interface} statistics
    * Add ShowPlatformHardwareQfpStatisticsDrop for;
            show platform hardware qfp active statistics drop
            show platform hardware qfp standby statistics drop
    * Add ShowPlatformHardwareSerdes for 'show platform hardware slot {x} serdes statistics'
    * Add ShowPlatformHardwareSerdesInternal for 'show platform hardware slot {x} serdes statistics internal'
    * Add ShowProcessesCpuHistory for 'show processes cpu history'
    * Add ShowPlatformHardwareQfpBqsStatisticsChannelAll for:
        show platform hardware qfp active bqs {x} ipm statistics channel all
        show platform hardware qfp standby bqs {x} ipm statistics channel all
        show platform hardware qfp active bqs {x} opm statistics channel all
        show platform hardware qfp standby bqs {x} opm statistics channel all

    * Update ShowVersion to support more output

*IOS
    * Add ShowProcessesCpu for:
        show processes cpu
        show processes cpu | include {WORD}
    * Add ShowVersionRp for:
        show version RP active [running|provisioned|installed]
        show version RP standby [running|provisioned|installed]
    * Add ShowPlatform for:
        show platform
    * Add ShowPlatformPower for:
        show platform power
    * Add ShowProcessesCpuHistory for:
        show processes cpu history
    * Add ShowProcessesCpuPlatform for:
        show processes cpu platform
    * Add ShowPlatformSoftwareStatusControl for:
        show platform software status control-processor brief
    * Add ShowPlatformSoftwareSlotActiveMonitorMem for:
        show platform software process slot switch active R0 monitor | inc Mem :|Swap:
    * Add ShowPlatformHardware for:
        show platform hardware qfp active infrastructure bqs queue output default all
    * Add ShowPlatformHardwarePlim for:
        show platform hardware port {x/x/x} plim statistics
        show platform hardware slot {x} plim statistics
        show platform hardware slot {x} plim statistics internal
        show platform hardware subslot {x/x} plim statistics
    * Add ShowPlatformHardwareQfpBqsOpmMapping for:
        show platform hardware qfp active bqs {x} opm mapping
        show platform hardware qfp standby bqs {x} opm mapping
    * Add ShowPlatformHardwareQfpBqsIpmMapping for:
        show platform hardware qfp active bqs {x} ipm mapping
        show platform hardware qfp standby bqs {x} ipm mapping
    * Add ShowPlatformHardwareSerdes for:
        show platform hardware slot {x} serdes statistics
    * Add ShowPlatformHardwareSerdesInternal for:
        show platform hardware slot {x} serdes statistics internal
    * Add ShowPlatformHardwareQfpBqsStatisticsChannelAll for:
        show platform hardware qfp active bqs {x} ipm statistics channel all
        show platform hardware qfp standby bqs {x} ipm statistics channel all
        show platform hardware qfp active bqs {x} opm statistics channel all
        show platform hardware qfp standby bqs {x} opm statistics channel all
    * Add ShowPlatformHardwareQfpInterfaceIfnameStatistics for:
        show platform hardware qfp active interface if-name {interface} statistics
        show platform hardware qfp standby interface if-name {interface} statistics
    * Add ShowPlatformHardwareQfpStatisticsDrop for:
        show platform hardware qfp active statistics drop
        show platform hardware qfp standby statistics drop
* IOSXR
    * Add ShowInstallInactiveSummary for:
          show install inactive summary
    * Add ShowInstallCommitSummary for:
          show install commit summary
--------------------------------------------------------------------------------
                                   MPLS LDP
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowMplsLdpParameters for:
          show mpls ldp parameters
    * Add ShowMplsLdpNsrStatistic for:
          show mpls ldp nsr statistics
    * Add ShowMplsLdpNeighbor for:
          show mpls ldp neighbor
          show mpls ldp neighbor vrf {vrf}
    * Add ShowMplsLdpNeighborDetail for:
          show mpls ldp neighbor detail
          show mpls ldp neighbor vrf {vrf} detail
    * Add ShowMplsLdpBindings for:
          show mpls ldp bindings
          show mpls ldp bindings all
          show mpls ldp bindings all detail
    * Add ShowMplsLdpCapabilities for:
          show mpls ldp capabilities
          show mpls ldp capabilities all
    * Add ShowMplsLdpDiscovery for:
          show mpls ldp discovery
          show mpls ldp discovery detail
          show mpls ldp discovery all
          show mpls ldp discovery all detail
          show mpls ldp discovery vrf {vrf}
          show mpls ldp discovery vrf {vrf} detail
    * Add ShowMplsLdpIgpSync for:
          show mpls ldp igp sync
          show mpls ldp igp sync all
          show mpls ldp igp sync interface {interface}
          show mpls ldp igp sync vrf {vrf}
    * Add ShowMplsForwardingTable for:
          show mpls forwarding-table
          show mpls forwarding-table detail
          show mpls forwarding-table vrf {vrf}
          show mpls forwarding-table vrf {vrf} detail
    * Add ShowMplsInterface for:
          show mpls interfaces
          show mpls interfaces {interface}
          show mpls interfaces {interface} detail
          show mpls interfaces detail
    * Add ShowMplsL2TransportDetail for:
          show mpls l2transport vc detail
* IOS
    * Add ShowMplsL2TransportDetail for:
          show mpls l2transport vc detail
* IOSXR
    * Add ShowMplsLdpNeighborBrief for:
          show mpls ldp neighbor brief
---------------------------------------------------------------------------------
                                   BFD 
---------------------------------------------------------------------------------
* IOSXE
    * Add ShowBfdNeighborsDetails for:
        show bfd neighbors client {client} details
        show bfd neighbors details
----------------------------------------------------------------------------------
                                   ARP
----------------------------------------------------------------------------------
* IOSXE
    * Add ShowArpApplication for:
        show arp application
    * Add ShowArpSummary for:
        show arp summary
--------------------------------------------------------------------------------
                                   QOS
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowServiceGroupState for:
        show service-group state
    * Add ShowServiceGroupStats for:
        show service-group stats
    * Add ShowServiceGroupTrafficStats for:
        show service-group traffic-stats
        show service-group traffic-stats {group}
* IOS
    * Add ShowServiceGroupState for:
        show service-group state
    * Add ShowServiceGroupStats for:
        show service-group stats
--------------------------------------------------------------------------------
                                   CONFIG
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowArchiveConfigDifferences for:
        show archive config differences
        show archive config differences {fileA} {fileB}
        show archive config differences {fielA}
    * Add ShowArchiveConfigIncrementalDiffs for:
        show archive config incremental-diffs {fileA}
    * Add ShowConfigurationLock for:
        show configuration lock
* IOS
    * Add ShowArchiveConfigDifferences for:
        show archive config differences
        show archive config differences {fileA} {fileB}
        show archive config differences {fielA}
    * Add ShowArchiveConfigIncrementalDiffs for:
        show archive config incremental-diffs {fileA}
    * Add ShowConfigurationLock for:
        show configuration lock
--------------------------------------------------------------------------------
                                   L2VPN
--------------------------------------------------------------------------------
* IOSXE & IOS
    * Add ShowBridgeDomain for:
            show bridge-domain
            show bridge-domain {WORD}
            show bridge-domain | count {WORD}
    * Add ShowEthernetServiceInstanceDetail for:
            show ethernet service instance detail
            show ethernet service instance interface {interface} detail
    * Add ShowEthernetServiceInstanceStats for:
            show ethernet service instance stats
            show ethernet service instance interface {interface} stats
    * Add ShowEthernetServiceInstanceSummary for:
            show ethernet service instance summary
    * Add ShowL2vpnVfi for:
            show l2vpn vfi
    * Add ShowL2vpnServiceAll for:
            show l2vpn service all
--------------------------------------------------------------------------------
                                   LAG
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowEtherChannelLoadBalancing for:
        show etherchannel load-balancing
    * Add ShowLacpNeighborDetail for:
        show lacp neighbor detail
    * Fix for ShowPagpInternal
--------------------------------------------------------------------------------
                                   INTERFACE
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowInterfaceStats for:
        show interface {interface} stats
        show interface stats
    * Update ShowIpInterface to support more output
    * Update ShowIpInterfaceBrief for cli_command
----------------------------------------------------------------------------------
                                 NTP
----------------------------------------------------------------------------------
* IOSXE
    * Add ShowNtpAssociationsDetail for:
        show ntp associations detail
* IOS
    * Add ShowNtpAssociationsDetail for:
        show ntp associations detail
--------------------------------------------------------------------------------
                                   ISIS
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowIsisAdjacency for:
        show isis adjacency
    * Add ShowIsisNeighborsSchema for:
        show run isis neighbors
--------------------------------------------------------------------------------
                                   MRIB
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowMribVrfRouteSummary for:
        show mrib vrf {vrf} {address-family} route summary
--------------------------------------------------------------------------------
                                   RUNNING-CONFIG
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowRunKeyChain for:
        show run key chain
    * Add ShowRunRouterIsis for:
        show run router isis
--------------------------------------------------------------------------------
                                   ROUTING
--------------------------------------------------------------------------------
* IOSXE
    * Update ShowIpRoute for different output
--------------------------------------------------------------------------------
                                   PROTOCOLS
--------------------------------------------------------------------------------
* IOSXE
    * Fix for ShowIpProtocols
--------------------------------------------------------------------------------
                                   RIP
--------------------------------------------------------------------------------
* IOSXE
    * Fix for ShowIpv6Rip