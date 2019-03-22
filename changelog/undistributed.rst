* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                    OSPF
--------------------------------------------------------------------------------
* IOSXE
    * Added parsers:
        * ShowIpOspfNeighbor
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

--------------------------------------------------------------------------------
                                    MPLS LDP
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowMplsLdpParameters for:
        'show mpls ldp parameters'
    * Add ShowMplsLdpNsrStatistic for:
        'show mpls ldp nsr statistics'
    * Add ShowMplsLdpNeighbor for:
         'show mpls ldp neighbor
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

--------------------------------------------------------------------------------
                                    L2VPN
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowBridgeDomain for:
            show bridge-domain
            show bridge-domain <WORD>
            show bridge-domain | count <WORD>