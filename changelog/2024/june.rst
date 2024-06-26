--------------------------------------------------------------------------------
                                     Modify                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowLispPlatform
        * Updated the schema to account for new section in show cli output.
    * Modified ShowLispServerSubscriptionPrefix
        * Updated the schema to allow to have optional keys.
    * Modified ShowLispSubscriber
        * Updated the schema and parser to allow to have optional keys.
            * Revision structure incorporated.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* utils
    * Modified unittests.py
        * Enhanced the unittests script to search local folders for a tests folder instead of using the root tests folder with symlinks

* general
    * Cleaned up existing unittests and brought to light a few that were never being picked up

* iosxe
    * Modified ShowMkaStatistics
        * Changed mkpdu-failures key from schema to Optional.
    * Modified ShowFlowMonitorCache
        * Added <datalink_mac_dst_output> key to schema as Optional.
        * Added regex pattern <p39> to accommodate various outputs.
    * Modified ShowIsisRib
        * Changed algo key from schema to Optional.
        * Updated code to accomodate various outputs.
    * Modified fix for ShowLogging
        * Modified patterns p11 regex to match user's data.
    * Modified ShowNtpAssociations
        * Updated regex pattern <p1> to accommodate various outputs.
    * Modified fix for ShowDlepClients
        * Modified parser to accomodate various outputs
    * Modified ShowIsisNodeLevel
        * Updated regex pattern p4 to accommodate various outputs.
    * Modified ShowPlatformSoftwareFedSwitchActiveNatFlows
        * Added elif condition to parser 'show platform software fed {switch} {mode} nat flows {flow_based_on}' and 'show platform software fed {switch} {mode} nat flows {flow_based_on} {flow_based_on_value}'
    * Modified ShowPlatformSoftwareFedSwitchMatmStats parser
        * Added cli show platform software fed {act_mode} matm stats
    * Modified ShowLispInstanceIdService
        * Fixed incorrect regex for ETR Map-Server and ITR Map-Resolver
    * Modified ShowModule
        * Added optional variables under module
        * Modified p3 and p4 regex
    * Fixed ShowDiagnosticResultModuleTestDetail parser
        * Fixed one regex pattern to match for all the conditions for 'Show diagnostic result module {mod_num} test {include} detail'
    * Modified fix for ShowMkaPolicy
        * Reverted the name expansion changes introduced in the last PR #3292.
    * Modified fix for ShowInterfaces
        * Modified the Regex pattern p<12> to correctly retrieve the send and receive status and accommodate varios outputs.
    * Modified fix for ShowIsisTopology
        * Modified patterns p5 and p6 to accommodate various outputs
    * Modified ShowSystemIntegrityAllMeasurementNonce parser
        * Updated regex to match LOCATION FRU=fru-rp SLOT=0 BAY=0 CHASSIS=-1 NODE=0
    * Modified ShowSystemIntegrityAllComplianceNonce parser
        * Updated regex to match LOCATION FRU=fru-rp SLOT=0 BAY=0 CHASSIS=-1 NODE=0
    * Modified ShowSystemIntegrityAllTrustChainNonce parser
        * Updated regex to match LOCATION FRU=fru-rp SLOT=0 BAY=0 CHASSIS=-1 NODE=0
    * Modified ShowL2vpnBridgeDomain
        * Added revised version 1 for ShowL2vpnBridgeDomain parser
        * Added <p10> and <p11> regex pattern to decide where to store neighbour values
        * Update <p7> parser to accommodate various outputs

* nxos
    * Modified ShowFex
        * Updated regex pattern <p1> to accommodate various outputs.
    * Modified ShowLldpNeighbors
        * Changed <interfaces> key from schema to Optional.

* iosxr
    * Modified ShowBgpAddressFamily
        * New Show Command - show bgp {address_family} community {community}
        * New Show Command - show bgp {address_family} community {community} {exact_match}
        * Updated regex for handling IPv6 adresses/prefixes
        * Updated regex pattern for handling new lines in IPv6 address family output
    * Modified ShowBgpVrfAfPrefix
        * adding new schema key srv6_pn_sid
        * adding new line p1_1 regex
        * adding p1_1 parser
    * Fixed ShowOspfInterface
        * Modified the p5 regex to handle optional field `cost`.
    * Modified fix for ShowVlanId
        * Modified parser to accomodate various outputs
    * Modified Traceroute
        * Added support for new traceroute command

* sonic
    * Modified ShowVersion
        * Refactored the code to current standard

* modified showplatformsoftwarefedswitchactivelearningstats parser
    * Added cli show platform software fed {rp} learning stats

* added regex for parsing itr map-resolver reachability, prefix-list and etr map-server doman-id and last map-register info.

* common
    * Modified format_output
        * Updated sorted function to sort the data in string and integer order
    * Modified _load_parser_json
        * Updated code to use correct variables


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxr
    * Added class ShowPtpForeignMastersInterface
        * Parser for show ptp foreign-masters {interface}
    * Added ShowOspfProcessIdVrfName
        * parser for 'show ospf {process_name} vrf {vrf_name} interface {interface}'
    * Added class ShowPoolAddressFamilyPool
        * show pool {address_family} name {pool_name}
    * Added show frequency synchronization interfaces brief
        * parser for 'show frequency synchronization interfaces brief'

* iosxe
    * Updated ShowRomvar
        * Added support to parse switch_ignore_startup_config.
    * Added ShowPlatformHardwareFedSwitchActiveNpuSlotPortLinkstatus
        * Added schema and parser for 'show platform hardware fed switch {mode} npu slot 1 port {port_num} port link_status'
    * Added ShowPlatformTcamUtilization
        * Added schema and parser for 9350 'show platform hardware fed active fwd-asic resource tcam utilization'
    * Added ShowMonitorCaptureStatistics
        * Added schema and parser for 'show monitor capture {capture_name} capture-statistics'
    * Added TestPlatformHardwareFepSwitchDumpStatistics
        * Added 'test platform hardware fep switch {switch_num} {fep_slot} dump-statistics' cat9k/c9300.
    * Added ShowPlatformSoftwareCpmSwitchActiveB0CountersInterfaceIsisSchema
        * Added parser for "show platform software cpm switch active B0 counters interface isis" and schema
    * Modified ShowPlatformSoftwareCpmSwitchB0CountersPuntInject
        * Updated to support timestamps  in the output
    * Added ShowDeviceTrackingDatabase
        * Added timeout 300 to parse bigger output
    * Added ShowLispInstanceIdIpv4MapCache
        * Added timeout 300 to parse bigger output
    * Added ShowLispInstanceIdIpv6MapCache
        * Added timeout 300 to parse bigger output
    * Added ShowLispServiceDatabase
        * Added timeout 300 to parse bigger output
    * Added ShowLispEthernetMapCache
        * Added timeout 300 to parse bigger output
    * Added ShowLispEidTableServiceDatabase
        * Added timeout 300 to parse bigger output
    * Added ShowPlatformSoftwareFedSwitchActiveNatPools
        * Parser for cli 'show platform software fed switch active nat pools'
    * Added ShowPlatformSoftwareFedActiveAclInfoDbDetail
        * Added schema and parser for 9350 'show platform show platform software fed switch active acl info db detail'

* nxos
    * Added show_ngoam.py
        * added new parser for cli 'show ngoam loop-detection status'
        * added new parser for cli 'show ngoam loop-detection summary'
    * Modidy show_vxlan.py
        * Fixed parser for ShowRunningConfigNvOverlay to include peer-ip command
    * Added ShowVlanCounters
        * added new parser for cli 'show vlan counters'
        * added new parser for cli 'show vlan id <id> counters'

* sonic
    * Added ShowPlatformInventory parser
        * show platform inventory
    * Added ShowInteraces
        * show interfaces transceiver eeprom


