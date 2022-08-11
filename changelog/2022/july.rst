--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowNat64Translations
        * added new parser for below cli's
    * Added ShowCryptoGdoiGmIdentifierDetail
        * added new parser for cli 'show crypto gdoi gm identifier detail'
    * Added ShowInstallVersion superparser
        * show install  version all
        * show install  version summary
        * show install  version  value <value>
    * Added ShowInstallVersionAll parser
        * show install  version all
    * Added ShowInstallVersionSummary parser
        * show install  version summary
    * Added ShowInstallVersionValue parser
        * show install  version  value <value>
    * Added ShowMemoryDeadTotal
        * show memory dead total
    * Added  show crypto gdoi ks identifier and show crypto gdoi ks identifier detail
        * show crypto gdoi ks identifier
        * show crypto gdoi ks identifier detail
    * Added ShowCryptoGdoiKsCoopIdentifier
        * show crypto gdoi gm identifier detail
    * Added ShowIpNhrpSummary
        * show ip nhrp summary
    * Added ShowCryptoIkev2StatsPsh
        * show crypto ikev2 stats psh
    * Added ShowFabricApSummary
        * Added new parser for "show fabric ap summary".
    * Added ShowAccessTunnelSummary
        * Added new parser for "show access tunnel summary".
    * Added ShowProcessesPlatformCProcess
        * Added new parser for "show processes platform | c wncd".
    * Added ShowProcessesPlatformIProcess
        * Added new parser for "show processes platform | i wncd".
    * Added ShowPlatformSoftCProcess
        * Added new parser for "show plat soft proc slot sw standby r0 monitor | c wncd".
    * Added ShowPlatformSoftIProcess
        * Added new parser for "show plat soft proc slot sw standby r0 monitor | i wncd".
    * Added ShowPlatformSoftwarePuntPolicer
        * show platform software punt-policer
    * Added ShowCryptoGdoiKsCoopDetail
        * show crypto gdoi ks coop detail
    * Added ShowCryptoGdoiGmRekeyDetail
        * added new parser for cli 'show crypto gdoi gm rekey detail'
    * Added ShowPlatformHardwareChassisPowerSupplyDetailAll parser
        * show platform hardware chassis power-supply detail all
    * Added ShowPlatformHardwareChassisFantrayDetail parser
        * show platform hardware chassis fantray detail
    * Added ShowPlatformHardwareChassisFantrayDetailSwitch parser
        * show platform hardware chassis fantraySwitch detail
    * Added ShowPlatformHardwareChassisPowerSupplyDetailSwitchAll parser
        * show platform hardware chassis power-supply detail switch {mode} all
    * Added ShowPlatformFedTcamPbrNat parser
        * show platform hardware fed switch active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}
    * Added ShowCryptoGdoiGmIdentifier
        * added new parser for cli 'show crypto gdoi gm identifier'
    * Added ShowIpAccessListDumpReflexive
        * added new parser for cli "show ip access-lists <reflect_acl_name> dump-reflexive"
    * Added ShowPlatformFedActiveFnfRecordCountAsicNum
        * added new parser for cli "show platform software fed active fnf record-count asic <asic_num>"
        * added new parser for cli "show platform software fed <switch> active fnf record-count asic <asic_num>"
    * Modified ShowPlatformHardwareFedActiveTcamUtilization
        * Added new parser for cli "show platform hardware fed <switch> active fwd-asic resource tcam utilization"
        * Modified parser for cli "show platform hardware fed active fwd-asic resource tcam utilization"
    * Modified ShowAccessLists
        * Added space in ShowAccessLists parser
    * Added ShowIpAccessListDumpReflexive
        * added new parser for cli "show platform software fed switch active ifm mappings"
    * Inherited ShowPlatformFedTcamPbrNat parser for c9600 from c9500
        * show platform hardware fed switch active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}
    * Added ShowCryptoGdoiGmPubkey
        * added new parser for cli 'show crypto gdoi gm pubkey'
    * Added ShowNat64Timeouts
        * Added new schema and parser for cli show nat64 timeouts
    * Added ShowNat64Statistics
        * Added new schema and parser for cli show nat64 statistics
        * Added new schema and parser for cli show nat64 statistics <global>
        * Added new schema and parser for cli show nat64 statistics mapping <dynamic>
        * Added new schema and parser for cli show nat64 statistics mapping dynamic acl <acl_name>
        * Added new schema and parser for cli show nat64 statistics mapping dynamic pool <pool_name>
    * Added ShowNat64MappingsStaticAddresses
        * Added new schema and parser for cli show nat64 mappings static addresses
        * Added new schema and parser for cli show nat64 mappings static addresses <ip_address>
        * Added new schema and parser for cli show nat64 mappings static addresses <ipv6_address>
    * Added ShowNat64MappingsDynamic
        * Added new schema and parser for cli show nat64 mappings dynamic
        * Added new schema and parser for cli show nat64 mappings dynamic id <number>
        * Added new schema and parser for cli show nat64 mappings dynamic list <access_list_name>
        * Added new schema and parser for cli show nat64 mappings dynamic pool <pool_name>
    * Added ShowNat64StatisticsPrifixStateful
        * Added new schema and parser for cli show nat64 statistics prefix stateful <ipv6>/<prefix_length>
    * Added ShowNat64MappingsStatic
        * Added new schema and parser for cli show nat64 mappings static
    * Added ShowMemoryPlatformInformation
        * show memory platform information
    * Added ShowProcessesCpuPlatformSorted
        * show processes cpu platform sorted
    * Added ShowUtdEngineStandardStatisticsUrl
        * for 'show utd engine standard statistics url'


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpMfib
        * Updated regex pattern <p8> to include "LISPv4 Decap".
    * Modified ShowAAServers
        * Fixed cli_command location. So that device.parse() could pick up.
    * Modified ShowAAAUserAll
        * Fixed cli_command location. So that device.parse() could pick up.
    * Modified ShowAaaFqdnAll
        * Fixed cli_command location. So that device.parse() could pick up.
    * Modified ShowPlatformResources
        * Added one more golden_output and golden_expected_output
        * Modified the key 'tcam' under 'qfp' to Optional
        * Removed keys 'pkt_buf_mem_0' and 'pkt_buf_mem_1'. Replaced it with 'Any()'
    * Modified ShowCryptoIkev2StatsExt
        * Updated parser class. Marked parameters gkm_operation, ppk_sks_operation and ike_preroute as Optional.
    * Modified ShowCryptoIpsecPALHWcreate_ipsec_sa_by_q
        * Updated parser class. Modified regex to reflect behaviour.
    * Modified ShowIpRoute parser
        * Added support for m-OMP
        * Fixed local variable 'source_protocol' referenced before assignement
    * Fixed ShowNat64Translations
        * Modified parser schema to grep multiple outputs under the same key.
        * Removed 'proto' dict and capturing values in index_dict instead as per modified schema. This change is not backwards compatible
    * Modified ShowEnvironmentStatus parser
        * Updated regex pattern <P1> to accommodate various outputs
    * Modified ShowIpMroute
        * Added optional key <lisp_vrf> under incoming_interface_list for lisp specific information.
        * Updated regex pattern <p3> to accommodate various above changes.
        * Added optional key <e_rp> under extranet_rx_vrf_list for additional lisp specific information.
        * Updated regex pattern <p8> to accommodate various above changes.
    * Modified ShowInterfacesTransceiverDetail
        * Removed the line 'stat = None'
        * Fixed <p3_0> regex to include the whole line
    * Modified ShowNat64Translations
        * Updated parser regex to match white space characters.
    * Modified ShowProcessesCpuPlatform
        * Updated regex pattern <p2> to grep the utilization even when its 100%
    * Modified ShowLoggingOnboardRpActiveTemperatureContinuous
        * Added show logging onboard switch {switch_num} rp active {include} continuous as new cli to support stack
    * Modified ShowLoggingOnboardRpActiveUptime
        * Added show logging onboard switch {switch_num} rp active uptime as new cli to support stack
        * Modified the  regex pattern <p6> to accomodate current reset reason change
    * Modified ShowInvetory
        * Added  'GigabitEthernet', 'TwoGigabitEthernet' in code of schema .
        * Updated few lines of code under p2 pattern to accommodate various outputs of IE platform.
    * Modified ShowPlatform
        * Changed state from schema to Optional.
        * Updated regex pattern p3 to accommodate various outputs for IE platforms.

* nxos
    * Modified ShowIpRoute
        * Fix for UnboundLocalError local variable 'route_dict' referenced before assignment
        * Updated the p2 regex to capture 'all-best' key
    * Modified ShowBgpVrfAllAllSummary
        * Added regex pattern <p8_3> and <p8_4> to accommodate output of neighbors with 4byte asn.
    * Modified ShowBgpVrfAllAllSummary
        * Added regex pattern <p8_3> and <p8_4> to accommodate output of neighbors with 4byte asn.





