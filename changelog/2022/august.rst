--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowCryptogdoiIpsecSa
        * added new parser for cli "show crypto gdoi ipsec sa"
    * Added ShowDeviceSensor
        * show device sensor cache interface {interface}
    * Added ShowIpDhcpSnoopingBindingTotalNumber
        * show ip dhcp snooping binding | include Total number of bindings
    * Added ShowIpDhcpSnoopingGleaning
        * show ip dhcp snooping | include gleaning
    * Added ShowFileSystems Parser in show_platform.py
        * show file systems
    * Added ShowException parser in show_install.py
        * show exception
    * Added ShowIssuClients parser in show_issu.py
        * show issu clients
    * Added ShowPlatformHardwareQfpActiveInfraPuntStatTypePer
        * show platform hardware qfp active infra punt stat type per | ex _0_
    * Added ShowSwitchStackPortSummary
        * Created parser for show switch stack port summary to check the stack port summary status.
    * Added ShowSdwanPolicyFromVsmart
        * added new parser for cli "show sdwan policy from-vsmart"
    * Added ShowPlatformSoftInfraBipc
        * show platform soft infra bipc | inc buffer
    * Added ShowLispDatabaseConfigPropV4Parser
        * 'show lisp instance-id {instance_id} ipv4 database config-propagation {eid_prefix}',
        * 'show lisp instance-id {instance_id} ipv4 database config-propagation',
        * 'show lisp {lisp_id} instance-id {instance_id} ipv4 database config-propagation',
        * 'show lisp all instance-id * ipv4 database config-propagation'
    * Added ShowLispDatabaseConfigPropV6Parser
        * 'show lisp instance-id {instance_id} ipv6 database config-propagation {eid_prefix}',
        * 'show lisp instance-id {instance_id} ipv6 database config-propagation',
        * 'show lisp {lisp_id} instance-id {instance_id} ipv6 database config-propagation',
        * 'show lisp all instance-id * ipv6 database config-propagation'
    * Added ShowPlatformHardwareQfpActiveDatapathPmdIfdev
        * show platform hardware qfp active datapath pmd ifdev
    * Added ShowSdmPrefer
        * added new parser for cli 'show sdm prefer'
    * Added ShowPlatformHardwareAuthenticationStatus
        * Created show platform hardware authentication status parser to check switch, stackAdaptor and FRU status
    * Added ShowRunSectionBgp
        * added new parser for cli "show running-config | section bgp"
    * Added ShowSpanningTreeInstances
        * show spanning-tree instances
    * Added ShowPlatformHardwareThroughputLevel
        * show platform hardware throughput level
    * Added ShowPlatformHardwareQfpActiveInfraDatapathInfraSwDistrib
        * show platform hardware qfp active datapath infra sw-distrib
    * Added ShowCtsServerList
        * added new parser for cli "show cts server-list"
    * Added ShowPlatformSoftwareFedSwitchStandbyAclUsage
        * added new parser for cli "show platform software fed switch standby acl usage"
    * Added ShowPlatformSwitchStandbyTcamUtilization
        * added new parser for cli "show platform hardware fed switch standby fwd-asic resource tcam utilization"
    * Modified ShowPlatformFedActiveFnfRecordCountAsicNum
        * Modified parser for cli "show platform software fed switch <state> fnf record-count asic <asic num>"
    * Added ShowPlatformHardwareFedSwitchActiveFwdResourceUtilizationLabel
        * for 'show platform hardware fed switch active fwd resource utilization | include {label}'
    * Added ShowPlatformHardwareQfpActiveSystemState
        * show platform hardware qfp active system state
    * Added ShowPlatformHardwareQfpActiveFeatureIpsecDatapathDropsAll
        * show platform hardware qfp active feature ipsec datapath drops all
    * Added ShowOspfv3vrfNeighbor
        * show ospfv3 vrf {vrf} neighbor
    * Added ShowNat64Pools
        * show nat64 pools
        * show nat64 pools {routes}
        * show nat64 pools hsl-id {hsl_id}
        * show nat64 pools hsl-id {hsl_id} {routes}
        * show nat64 pools name {pool_name}
        * show nat64 pools name {pool_name} {routes}
        * show nat64 pools range {pool_start_ip} {upper_range}
        * show nat64 pools range {pool_start_ip} {upper_range} {routes}
    * Added ShowNat64PrefixStatefulGlobal
        * show nat64 prefix stateful global
    * Added ShowNat64PrefixStatefulInterfaces
        * show nat64 prefix stateful interfaces
        * show nat64 prefix stateful interfaces prefix {prefix}
    * Added ShowNat64PrefixStatefulStaticRoutes
        * show nat64 prefix stateful static-routes
        * show nat64 prefix stateful static-routes prefix {prefix}
    * Added ShowPlatformHardwareQfpActiveDatapathInfraSwCio
        * show platform hardware qfp active datapath infra sw-cio
    * Added ShowPlatformHardwareQfpActiveDatapathInfraSwNic
        * show platform hardware qfp active datapath infra sw-nic
    * Added ShowPlatformHardwareQfpActiveInterfaceAllStatisticsDropSummary
        * show platform hardware qfp active interface all statistics drop_summary
    * Added ShowGnxiState
        * show gnxi state
    * Added ShowGnxiStateDetail
        * show gnxi state detail
    * Added ShowUtdEngineStandardConfig
        * show utd engine standard config
    * Added ShowBdDatapath
        * show platform hardware qfp active feature bridge-domain datapath {bd_id}
    * Added ShowLispServerConfigPropV4Parser parser
        * show lisp instance-id {instance_id} ipv4 server config-propagation
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server config-propagation
        * show lisp all instance-id {instance_id} ipv4 server config-propagation
    * Added ShowLispServerConfigPropV6Parser parser
        * show lisp instance-id {instance_id} ipv6 server config-propagation
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server config-propagation
        * show lisp all instance-id {instance_id} ipv6 server config-propagation
    * Added ShowLispPublicationConfigPropV4Parser
        * 'show lisp {lisp_id} instance-id {instance_id} ipv4 publication config-propagation {eid_prefix}',
        * 'show lisp instance-id {instance_id} ipv4 publication config-propagation {eid_prefix}',
        * 'show lisp instance-id {instance_id} ipv4 publication config-propagation detail',
        * 'show lisp all instance-id * ipv4 publication config-propagation'
    * Added ShowPlatformSoftwareFactoryResetSecureLog
        * Added show platform software factory-reset secure log
    * Added ShowLispV4ServerConfigPropagation parser
        * show lisp instance-id {instance_id} ipv4 server config-propagation
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server config-propagation
    * Added ShowLispV6ServerConfigPropagation parser
        * show lisp instance-id {instance_id} ipv6 server config-propagation
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server config-propagation
    * Added ShowCryptoGdoiKsAcl
        * show crypto gdoi ks acl
    * Added ShowCryptoGdoiGmAclLocal
        * show crypto gdoi gm acl local
    * Added ShowCryptoGdoiKsMembers
        * show crypto gdoi ks members
    * Added ShowCryptoGdoiKsMembersIp
        * show crypto gdoi ks members {member_ip}
    * Added ShowCryptoGdoiKsMembersSummary
        * show crypto gdoi ks members summary
    * Added ShowIpv6CefInternal parser
        * 'show ipv6 cef internal'
        * 'show ipv6 cef {prefix} internal'
        * 'show ipv6 cef vrf {vrf} {ip} internal'

* sros
    * Added ShowServiceSdpUsing
        * show service sdp-using

* nxos
    * Added ShowFex
        * show fex

* updated <state> as argument to validate stack device active or standby commands. now the parser will work for both standlone and stack devices.

* added showlisppublicationconfigpropv6parser
    * 'show lisp {lisp_id} instance-id {instance_id} ipv6 publication config-propagation {eid_prefix}',
    * 'show lisp instance-id {instance_id} ipv6 publication config-propagation {eid_prefix}',
    * 'show lisp instance-id {instance_id} ipv6 publication config-propagation detail',
    * 'show lisp all instance-id * ipv6 publication config-propagation'

* iosxr
    * Added ShowRcmdNode
        * show rcmd node
    * Added ShowRcmdMemory
        * show rcmd memory


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Added ShowFabricApSummary
        * Moved new parser for "show fabric ap summary" from iosxe to iosxe/cat9k.
    * Added ShowAccessTunnelSummary
        * Moved new parser for "show access tunnel summary" from iosxe to iosxe/cat9k.
    * Added ShowProcessesPlatformCProcess
        * Moved new parser for "show processes platform | c wncd" from iosxe to iosxe/cat9k.
    * Added ShowProcessesPlatformIProcess
        * Moved new parser for "show processes platform | i wncd" from iosxe to iosxe/cat9k.
    * Added ShowPlatformSoftCProcess
        * Moved new parser for "show plat soft proc slot sw standby r0 monitor | c wncd" from iosxe to iosxe/cat9k.
    * Added ShowPlatformSoftIProcess
        * Moved new parser for "show plat soft proc slot sw standby r0 monitor | i wncd" from iosxe to iosxe/cat9k.
    * Modified ShowApSummary
        * Modified parser "show ap summary" to handle 0 APs and new output change in 17.10 release.
    * Modified ShowBootvat Parser in show_platform.py
        * show bootvar
    * Modified ShowBoot Parser in show_platform.py
        * show boot
    * Modified ShowBoot Parser in show_issu.py
        * show boot
    * Modified ShowApSummary
        * Fixed show ap summary to handle both outputs.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Updated /d to /d+ in compile for the following Parsers to match the numbers correctly
        * ShowNat64Statistics
            * Modified <p8> to accommodate values with 2 or more digits
        * ShowNat64MappingsStaticAddresses
            * Modified <p2> to accommodate values with 2 or more digits
        * ShowNat64MappingsDynamic
            * Modified <p2> and <p4> to accommodate values with 2 or more digits
        * ShowNat64MappingsStatic
            * Modified <p5> to accommodate values with 2 or more digits
    * Modified ShowVersion
        * Updated regex pattern p16_1 to accommodate a license_type with a spaces, e.g. "Type Permanent Right-To-Use"
    * Modified ShowCryptoGdoiGmIdentifier
        * changed schema and parsers to handle multiple group-member per group
    * Modified ShowCryptoGdoiGmIdentifierSchema
        * changed schema and parsers to handle multiple group-member per group
    * Modified ShowCryptoGdoiGmIdentifierDetail
        * changed schema and parsers to handle multiple group-member per group
    * Modified ShowCryptoGdoiGmIdentifierDetailSchema
        * changed schema and parsers to handle multiple group-member per group
    * Modified ShowCryptoGdoiKsCoopDetail
        * changed schema and parsers to handle multiple ks-member per group
    * Modified ShowCryptoGdoiKsCoopDetailSchema
        * changed schema and parsers to handle multiple ks-member per group
    * Modified ShowCryptoGdoiGmPubkey
        * changed schema and parsers to handle multiple sessions per group
    * Modified ShowCryptoGdoiGmPubkeySchema
        * changed schema and parsers to handle multiple sessions per group
    * Modified ShowBgpSummarySuperParser
        * Changed p9 and p11 to work with 4 byte BGP AS number
    * Modified ShowBgpSummarySchema
        * Changed field 'as' to return type int or str in case of 4 byte BGP AS.
    * Modified ShowLslibProducerAllLscacheLinksDetail
        * updated regexp pattern p36 to accomodate A bit
    * Modified ShowCtsRoleBasedPermissions
        * added support to options of the show cts role-based permissions
    * Modified ShowCtsRoleBasedCounters
        * added support to options of the show cts role-based counters
    * Modified ShowNat64Statistics
        * Added the new command show nat64 statistics interface <interface_name>
    * Modified ShowNat64MappingsDynamic
        * Corrected the show command "show nat64 mappings dynamic"
    * Modified ShowNat64MappingsStaticSchema
        * Corrected the show command in schema "show nat64 mappings static"
    * Modified ShowRunningConfigNve
        * Made the key 'l2vpn_global' optional
        * Made the keys 'l2vni' and 'l3vni' under 'nve_interfaces' optional
    * Modified ShowTelemetryIETFSubscription, ShowTelemetryIETFSubscriptionDetail
        * Parsers for 'all', 'configured', 'dynamic', and 'permanent' variants of 'show telemetry ietf subscription' were broken by the previous change. Fix by moving them to separate classes that inherit from the base class for this CLI.
    * Modified ShowCryptoGdoiKsCoopIdentifierDetail class
        * Changed Regex to include spaces, which was missing.
    * Modified Expected and Golden output
        * Changed Expected and Golden output, in line with actual device output.
    * Modified ShowLoggingOnboardRpActiveUptime
        * Added show logging onboard switch {switch_num} uptime as new cli to support stack

* generic
    * Add debug log message showing which parser is being used

* iosxr
    * Added ShowRouteIpv4
        * Updated the regex <p11> to fix local variable 'outgoing_interface_dict' referenced before assignment

* nxos
    * Modified ShowIpArpDetailVrfAll
        * Updated regex pattern p1 to support VRF in output
    * Modified ShowRunningConfigBgp
        * Updated regex pattern <p45> to accommodate more than just letters and numbers in BGP neighbor description.  E.g.  []-"_' '
    * ShowRunningConfigBgp
        * Fix for Schema missing key error
    * Modified ShowIpRoute
        * Add Regex <p7> to match multiple lines not captured in existing code
    * Modified ShowModule
        * Updated schema/parser to add new header type `lem` to accommodate edelweiss platform output variant.




