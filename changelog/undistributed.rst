* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

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
