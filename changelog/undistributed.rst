* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

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

--------------------------------------------------------------------------------
                                     CONFIG
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowArchiveConfigDifferences for:
        show archive config differences
        show archive config differences {fileA} {fileB}
        show archive config differences {fileA}
    * Add ShowArchiveConfigIncrementalDiffs for:   
        show archive config incremental-diff {fileA}
