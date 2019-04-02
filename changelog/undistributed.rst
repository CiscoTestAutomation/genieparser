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
