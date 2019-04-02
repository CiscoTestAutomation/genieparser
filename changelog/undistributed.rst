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
        show bfd neighbors details
        show bfd neighbors client <client> details

* IOS
    * Add ShowBfdNeighborsDetails for:
        show bfd neighbors details
        show bfd neighbors client <client> details
----------------------------------------------------------------------------------
                                   ARP
----------------------------------------------------------------------------------
* IOSXE
    * Add ShowArpApplication for:
        show arp application
    * Add ShowArpSummary for:
        show arp summary
* IOS
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
        show service-group traffic-stats <group>
        
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
* IOSXE
    * Add ShowBridgeDomain for:
            show bridge-domain
            show bridge-domain <WORD>
            show bridge-domain | count <WORD>
    * Add ShowEthernetServiceInstanceDetail for:
            show ethernet service instance detail
            show ethernet service instance interface <interface> detail
    * Add ShowEthernetServiceInstanceStats for:
            show ethernet service instance stats
            show ethernet service instance interface <interface> stats
    * Add ShowEthernetServiceInstanceSummary for:
            show ethernet service instance summary
    * Add ShowL2vpnVfi for:
            show l2vpn vfi

* IOS
    * Add ShowL2vpnVfi for:
            show l2vpn vfi
--------------------------------------------------------------------------------
                                   LAG
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowEtherChannelLoadBalancing for:
        show etherchannel load-balancing
    * Add ShowLacpNeighborDetail for:
        show lacp neighbor detail

--------------------------------------------------------------------------------
                                   INTERFACE
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowInterfaceStats for:
        show interface <interface> stats
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
        show mrib vrf <vrf> <address-family> route summary

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

