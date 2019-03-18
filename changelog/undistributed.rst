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
    * Add ShowPlatformHardwareSerdes for 'show platform hardware slot <x> serdes statistics'
    * Add ShowPlatformHardwareSerdesInternal for 'show platform hardware slot <x> serdes statistics internal'