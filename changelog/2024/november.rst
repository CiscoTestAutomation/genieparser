--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowSoftwareAuthenticityRunning
        * Added schema and parser for 'show software authenticity running'
    * Added ShowPlatformHardwareFedXcvrRegisters parser
        * Added parser for cli show platform Hardware Fed XCVR Registers
    * Added ShowPlatformHardwareFedSwitchActiveNpuSlotPortRecreate parser
        * Added parser for cli show platform Hardware NPUSlot PortCreate
    * Added `ShowPlatformSoftwareFedSwitchActiveIfmMappingsL3if_le` parser.
    * Added parser for CLI `show platform software fed switch active ifm mappings l3if-le`.
    * Added ShowPlatformSoftwareFedSwitchNumberIfmMappingsPortLE parser.
        * Added parser for CLI `show platform software fed switch active ifm mappings port-le`.
    * Added ShowDnsLookup Parser in show_dns_lookup.py
        * show dns-lookup cache
        * show dns-lookup hostname {hostname}
    * Added ShowControllerEthernetControllerInterfaceMac parser
        * Added parser for cli show controller interface mac
    * Added ShowIdpromEeprom parser
        * Added parser for cli show idprom all eeprom
    * added ShowPlatformSoftwareFedPuntEntriesInclude Parser
        * parser for show platform software fed {switch} {port_num} punt entries | include {match}
    * Added ShowPlatformSoftwareFedSwitchActiveStatisticsInit parser.
        * Added parser for CLI 'show platform software fed switch active statistics init'
    * Added revision1 for ShowProcessesCpuPlatformSorted parser.
        * Added revision1 for CLI `show processes cpu platform sorted`.
    * Added ShowPlatformSoftwareFedSwitchActiveCpuInterfaces parser.
        * Added parser for CLI `show platform software fed switch active cpu-interfaces`.
    * Added ShowPlatformSoftwareWiredClientID parser.
        * Added parser for cli 'show platform software wired-client {client_id}'.

* utils
    * Added revision keyword and handling to get_parser.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified fix for golden_output_expected.py
        * fixed the regex spaces fixes
    * Modified fix for show_platform_software_fed.py
        * removed unnecessary blank lines
        * added pattern as a comment for regex
        * conflict for show_platform_software_fed.py resolved
        * test commit done
        * added comment for match line
    * Modified fix for ShowIdprom.
        * Modified the key value as optional to accomodate various outputs.
    * Modified fix for ShowLispDatabaseConfigPropSuperParser
        * Modified the regex patterns <p3> to accommodate different output.
    * Modified ShowIpNbarVersion
        * made file and creation_time optional
    * Modified fix for ShowPolicyMapInterface
        * added rate_bps and burst_bytes under child policy-name section.
    * Modified ShowIpIgmpSnoopingGroups
        * Modified <vlan_id>, <type>, <version> and <port> in the schema as Optional.
        * Added regex pattern <p1_0> to accommodate various outputs.
    * Modified ShowLispExtranet
        * Changed <home_instance>, <total> from schema to Optional.
    * Modified ShowPlatformSoftwareCpmCountersInterfaceIsis
        * Added BP  command for the same schema and output.
    * Modified ShowPlatformSoftwareCpmSwitchB0CountersPuntInject
        * Added BP command for the same schema and output.
    * Modified ShowPlatformSoftwareCpmSwitchActiveB0CountersInterfaceLacp
        * Added BP command for the same schema and output.
    * Modified ShowPlatformSoftwareCpmSwitchB0CountersDrop
        * Added BP command for the same schema and output.
    * Update revision1 for ShowProcessesCpuPlatformSorted parser.
        * Made cpu_utilization, five_sec_cpu_total, one_min_cpu, five_min_cpu optional.

* viptela
    * Modified ShowControlConnections
        * Updated regex pattern <p1> to accommodate string length changes in rows.
    * Modified ShowIpRoutes
        * Updated regex pattern <p1> to accommodate the nh_if_name column running into the nh_addr column.
    * Modified ShowOmpPeers
        * Updated regex pattern <p1> to accommodate tenant id and region id.
    * Modified ShowSystemStatus
        * Updated regex pattern <p10> to accommodate matching key values correctly when additional colons are in values.

* iosxr
    * Modified ShowLacp
        * Changed <rate> key from schema to Optional.
        * Updated regex pattern <p1> and <p2> to accommodate various outputs.

* nxos
    * Modified ShowIpIgmpGroups
        * Updated regex pattern <p2> and <p3> to accommodate various outputs.
    * Modified ShowPimRp
        * Updated regex pattern <p8_3> to accommodate various outputs.
    * Modified ShowIpv6MldGroups
        * Updated regex pattern p4, p6 and p7 to handle white space.
        * Modified line.strip() to rstrip().
        * Modified the logic to handle different output

* common
    * Modified _fuzzy_search_command and _is_regular_token functions to make it work for commands which contains arguments inside parenthesis.


