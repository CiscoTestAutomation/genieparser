* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

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
                                   PLATFORM
--------------------------------------------------------------------------------
* IOSXE
  * ShowInventory enhanced to support ASR901 platform

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
    * Add ShowRipStatistics for:
        show rip statistics
        show rip vrf {vrf} statistics

--------------------------------------------------------------------------------
                                PREFIX_LIST
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowRplPrefixSet for:
        show rpl prefix-set
        show rpl prefix-set <name>
