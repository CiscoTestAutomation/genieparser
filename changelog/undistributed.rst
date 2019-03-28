* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

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
    	'show platform hardware port <x/x/x> plim statistics'
    	'show platform hardware slot <x> plim statistics'
    	'show platform hardware slot <x> plim statistics internal'
    	'show platform hardware subslot <x/x> plim statistics'
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
        show platform hardware qfp active bqs <x> opm mapping
        show platform hardware qfp standby bqs <x> opm mapping
    * Add ShowPlatformHardwareQfpBqsIpmMapping for;
        show platform hardware qfp active bqs <x> ipm mapping
        show platform hardware qfp standby bqs <x> ipm mapping
    * Add ShowPlatformHardwareQfpInterfaceIfnameStatistics for;
        show platform hardware qfp active interface if-name <interface> statistics
        show platform hardware qfp standby interface if-name <interface> statistics
    * Add ShowPlatformHardwareQfpStatisticsDrop for;
            show platform hardware qfp active statistics drop
            show platform hardware qfp standby statistics drop
    * Add ShowPlatformHardwareSerdes for 'show platform hardware slot <x> serdes statistics'
    * Add ShowPlatformHardwareSerdesInternal for 'show platform hardware slot <x> serdes statistics internal'
    * Add ShowProcessesCpuHistory for 'show processes cpu history'

    * Update ShowVersion to support more output

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
    * Add ShowBfdNeighborsDetails
        show bfd neighbors client <client> details
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
        show service-group traffic-stats <group>

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

