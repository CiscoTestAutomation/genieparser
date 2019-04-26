* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |


--------------------------------------------------------------------------------
                                   MSDP
--------------------------------------------------------------------------------
* IOSXE
  * Add ShowIpMsdpPeer for:
    show ip msdp peer
    show ip msdp vrf <vrf> peer
  * Add ShowIpMsdpSaCache for:
    show ip msdp sa-cache
    show ip msdb vrf <vrf> sa-cache
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
      * show bgp vrf <vrf> ipv4 unicast

----------------------------------------------------------------------------------
                                  EIGRP
----------------------------------------------------------------------------------
* IOSXE
    * Add ShowIpEigrpNeighbors for:
            show ip eigrp neighbors
            show ip eigrp vrf <vrf> neighbors

      * Add ShowIpv6EigrpNeighbors for:
            show ipv6 eigrp neighbors
            show ipv6 eigrp vrf <vrf> neighbors

      * Add ShowIpEigrpNeighborsDetail for:
            show ip eigrp neighbors detail
            show ip eigrp vrf <vrf> neighbors detail

      * Add ShowIpv6EigrpNeighborsDetail for:
            show ipv6 eigrp neighbors detail
            show ipv6 eigrp vrf <vrf> neighbors detail

* IOSXR
    * Add ShowEigrpIpv4Neighbors for:
            show eigrp ipv4 neighbors
            show eigrp ipv4 vrf <vrf> neighbors
    * Add ShowEigrpIpv6Neighbors for:
            show eigrp ipv6 neighbors
            show eigrp ipv6 vrf <all> neighbors
    * Add ShowEigrpIpv4NeighborsDetail for:
            show eigrp ipv4 neighbors detail
            show eigrp ipv4 vrf <vrf> neighbors detail
    * Add ShowEigrpIpv6NeighborsDetail for:
            show eigrp ipv6 neighbors detail
            show eigrp ipv6 vrf <all> neighbors detail
* NXOS
    * Add ShowIpv4EigrpNeighbors for:
        show ip eigrp neighbors vrf <vrf>
    * Add ShowIpv6EigrpNeighbors for:
        show ipv6 eigrp neighbors vrf <all>
    * Add ShowIpv4EigrpNeighborsDetail for:
        show ip eigrp neighbors detail vrf <all>
    * Add ShowIpv6EigrpNeighborsDetail for:
        show ipv6 eigrp neighbors detail vrf <all>

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
        show lacp <channel-group> counters
    * Add ShowLacpInternal for:
        show lacp internal
        show lacp <channel-group> internal
    * Add ShowLacpNeighbor for:
        show lacp neighbor
        show lacp <channel-group> neighbor
    * Add ShowPagpCounters for:
        show pagp counters
        show pagp <channel-group> counters
    * Add ShowPagpNeighbor for:
        show pagp neighbor
        show pagp <channel-group> neighbor
    * Add ShowPagpInternal for:
        show pagp internal
        show pagp <channel-group> internal
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
        show interfaces <interface> counters
    * Add ShowInterfacesSwitchport for:
        show interfaces switchport
    * Add ShowInterfacesTrunk for:
        show interfaces trunk
    * Add ShowInterfacesStats for:
        show interface <interface> stats
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
        show lisp all extranet <extranet> instance-id <instance_id>
    * Add ShowLispDynamicEidDetail for:
        show lisp all extranet <extranet> instance-id <instance_id>
    * Add ShowLispService for:
        show lisp all instance-id <instance_id> <service>
        show lisp all service <service>
    * Add ShowLispServiceMapCache for:
        show lisp all instance-id <instance_id> <service> map-cache
    * Add ShowLispServiceRlocMembers for:
        show lisp all instance-id <instance_id> <service> rloc members
    * Add ShowLispServiceSmr for:
        show lisp all instance-id <instance_id> <service> smr
    * Add ShowLispServiceSummary for:
        show lisp all <service> summary
    * Add ShowLispServiceDatabase for:
        show lisp all instance-id <instance_id> <service> dabatase
    * Add ShowLispServiceServerSummary for:
        show lisp all instance-id <instance_id> <service> server summary
    * Add ShowLispServiceServerDetailInternal for:
        show lisp all instance-id <instance_id> <service> server detail internal
    * Add ShowLispServiceStatistics for:
        show lisp all instance-id <instance_id> <service> statistics

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
          show mpls ldp neighbor vrf <vrf>
    * Add ShowMplsLdpNeighborDetail for:
          show mpls ldp neighbor detail
          show mpls ldp neighbor vrf <vrf> detail
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
          show mpls ldp discovery vrf <vrf>
          show mpls ldp discovery vrf <vrf> detail
    * Add ShowMplsLdpIgpSync for:
          show mpls ldp igp sync
          show mpls ldp igp sync all
          show mpls ldp igp sync interface <interface>
          show mpls ldp igp sync vrf <vrf>
    * Add ShowMplsForwardingTable for:
          show mpls forwarding-table
          show mpls forwarding-table detail
          show mpls forwarding-table vrf <vrf>
          show mpls forwarding-table vrf <vrf> detail
    * Add ShowMplsInterface for:
          show mpls interfaces
          show mpls interfaces <interface>
          show mpls interfaces <interface> detail
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
        show ip rpf <mroute address>
        show ip rpf vrf <vrf> <mroute address>
    * Add ShowIpv6Rpf for:
        show ipv6 rpf <mroute address>
        show ipv6 rpf vrf <vrf> <mroute address>

--------------------------------------------------------------------------------
                                   ROUTING
--------------------------------------------------------------------------------
* IOS
    * Add ShowIpv6RouteWord for:
        show ipv6 route <Hostname or A.B.C.D>
        show ipv6 route vrf <vrf> <Hostname or A.B.C.D>
* NXOS
    * Updated ShowIpRoute for:
        show ip route
        show ip route vrf {vrf}
        show ip route vrf all
* IOSXR
    * Add ShowRouteIpv4 for:
        show route ipv4
        show route vrf <vrf> ipv4
    * Add ShowRouteIpv6 for:
        show route ipv6
        show route vrf <vrf> ipv6

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
          show power inline <interface>

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
        show service-group traffic-stats <group>

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
        show bfd neighbors client <client> details

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
        show clns interface <interface>
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
            show ip cef vrf <vrf>
            show ip cef <prefix>
            show ip cef vrf <vrf> <prefix>
    * Add ShowIpv6Cef for :
            show ipv6 cef
            show ipv6 cef vrf <vrf>
            show ipv6 cef <prefix>
            show ipv6 cef vrf <vrf> <prefix>

----------------------------------------------------------------------------------
                                 ROUTING
----------------------------------------------------------------------------------
* NXOS
  * Updated ShowRoutingIpv6VrfAll to support different vrf

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
          show ip access-lists <acl>
  * Add ShowIpv6AccessLists for :
          show ipv6 access-list
          show ipv6 access-list <acl>

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
        show rip vrf <vrf> database
    * Add ShowRipInterface for:
        show rip interface
        show rip vrf {vrf} interface

--------------------------------------------------------------------------------
                                PREFIX_LIST
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowRplPrefixSet for:
        show rpl prefix-set
        show rpl prefix-set <name>

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
        show l2route evpn mac-ip evi <evi>

--------------------------------------------------------------------------------
                                VRF
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowVrfDetail to support more varied output
