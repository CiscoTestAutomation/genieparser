* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                   LAG
--------------------------------------------------------------------------------
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
        *  show clns traffic

----------------------------------------------------------------------------------
                                   ACL
----------------------------------------------------------------------------------
* IOSXR
    * Add ShowAclAfiAll for:
        show access-lists afi-all
    * Add ShowAclEthernetServices for:
        show access-lists ethernet-services
