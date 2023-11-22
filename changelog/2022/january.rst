--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added MonitorCaptureStop parser
        * monitor capture {capture_name} stop
    * Added ShowCryptoPkiTimerDetail
        * show crypto pki timer detail
    * Added ShowCryptoPkiServerRequests
        * show crypto pki server {server} request
    * Added ShowIpv6MldSnoopingGroups
        * show ipv6 mld snooping address vlan {vlan_id}
    * Added class ShowLispPlatformStatistics
        * show lisp platform statistics
    * Added ShowLispSiteDetail
        * show lisp site detail
        * show lisp site name {site_name}
        * show lisp site {eid}
        * show lisp site {eid} instance-id {instance_id}
        * show lisp site {eid} eid-table {eid_table}
        * show lisp site {eid} eid-table vrf {vrf}
        * show lisp {lisp_id} site detail
        * show lisp {lisp_id} site name {site_name}
        * show lisp {lisp_id} site {eid}
        * show lisp {lisp_id} site {eid} instance-id {instance_id}
        * show lisp {lisp_id} site {eid} eid-table {eid_table}
        * show lisp {lisp_id} site {eid} eid-table vrf {vrf}
        * show lisp locator-table {locator_table} site detail
        * show lisp locator-table {locator_table} site name {site_name}
        * show lisp locator-table {locator_table} site {eid}
        * show lisp locator-table {locator_table} site {eid} instance-id {instance_id}
        * show lisp locator-table {locator_table} site {eid} eid-table {eid_table}
        * show lisp locator-table {locator_table} site {eid} eid-table vrf {vrf}
    * Added ShowLispEthernetServerDetail
        * show lisp instance-id {instance_id} ethernet server detail
        * show lisp instance-id {instance_id} ethernet server name {site_name}
        * show lisp instance-id {instance_id} ethernet server {eid}
        * show lisp instance-id {instance_id} ethernet server etr-address {etr_address}
        * show lisp {lisp_id} instance-id {instance_id} ethernet server detail
        * show lisp {lisp_id} instance-id {instance_id} ethernet server name {site_name}
        * show lisp {lisp_id} instance-id {instance_id} ethernet server {eid}
        * show lisp {lisp_id} instance-id {instance_id} ethernet server etr-address {etr_address}
        * show lisp eid-table vrf {vrf} ethernet server detail
        * show lisp eid-table vrf {vrf} ethernet server name {site_name}
        * show lisp eid-table vrf {vrf} ethernet server {eid}
        * show lisp eid-table vrf {vrf} ethernet server etr-address {etr_address}
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server detail
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server name {site_name}
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server etr-address {etr_address}
    * Added ShowLispIpv4ServerDetail
        * show lisp instance-id {instance_id} ipv4 server detail
        * show lisp instance-id {instance_id} ipv4 server name {site_name}
        * show lisp instance-id {instance_id} ipv4 server { }
        * show lisp instance-id {instance_id} ipv4 server etr-address {etr_address}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server detail
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server name {site_name}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server {eid}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server etr-address {etr_address}
        * show lisp eid-table {eid_table} ipv4 server detail
        * show lisp eid-table {eid_table} ipv4 server name {site_name}
        * show lisp eid-table {eid_table} ipv4 server {eid}
        * show lisp eid-table {eid_table} ipv4 server etr-address {etr_address}
        * show lisp eid-table vrf {vrf} ipv4 server detail
        * show lisp eid-table vrf {vrf} ipv4 server name {site_name}
        * show lisp eid-table vrf {vrf} ipv4 server {eid}
        * show lisp eid-table vrf {vrf} ipv4 server etr-address {etr_address}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server detail
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server name {site_name}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server etr-address {etr_address}
    * Added ShowLispIpv6ServerDetail
        * show lisp instance-id {instance_id} ipv6 server detail
        * show lisp instance-id {instance_id} ipv6 server name {site_name}
        * show lisp instance-id {instance_id} ipv6 server {eid}
        * show lisp instance-id {instance_id} ipv6 server etr-address {etr_address}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server detail
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server name {site_name}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server {eid}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server etr-address {etr_address}
        * show lisp eid-table {eid_table} ipv6 server detail
        * show lisp eid-table {eid_table} ipv6 server name {site_name}
        * show lisp eid-table {eid_table} ipv6 server {eid}
        * show lisp eid-table {eid_table} ipv6 server etr-address {etr_address}
        * show lisp eid-table vrf {vrf} ipv6 server detail
        * show lisp eid-table vrf {vrf} ipv6 server name {site_name}
        * show lisp eid-table vrf {vrf} ipv6 server {eid}
        * show lisp eid-table vrf {vrf} ipv6 server etr-address {etr_address}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server detail
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server name {site_name}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server etr-address {etr_address}
    * Added class ShowDlepClients
    * Added class ShowDlepNeighbors
    * Modified ShowLispExtranet
        * Updated schema,regex patterns and logic to handle updated device output from show command
    * Added ShowCryptoEntropyStatus
        * show crypto entropy status
    * Added ShowPlatformSudiPki
        * show platform sudi pki
    * Added ShowPlatformHardwareAuthenticationStatus
        * show platform hardware authentication status
    * Added ShowCryptoIkev2StatsExt
        * show crypto ikev2 stats ext-service
    * Added ShowCryptoPkiServer
        * show crypto pki server
    * Added ShowCryptoSessionRemoteDetail
        * show crypto session remote {remote_ip} detail
    * Added ShowCryptoSessionRemote
        * show crypto session remote {remote_ip}
    * Added class ShowCtsRoleBasedSgtMapAll
        * show cts role-based sgt-map all
        * show cts role-based sgt-map all vrf <vrf> all
    * Added class ShowCtsSxpConnections
        * show cts sxp connections
        * show cts sxp connections vrf <vrf>
    * Added class ShowCtsSxpSgtMapBrief
        * show cts sxp sgt-map brief
        * show cts sxp sgt-map vrf <vrf> brief
    * Added ShowInterfacesSummary
        * show interfaces summary
        * show interfaces {interface} summary
    * Added ShowIpv6Mfib
        * show ipv6 mfib
        * show ipv6 mfib {group}
        * show ipv6 mfib {group} {source}
        * show ipv6 mfib verbose
        * show ipv6 mfib {group} verbose
        * show ipv6 mfib {group} {source} verbose
        * show ipv6 mfib vrf {vrf}
        * show ipv6 mfib vrf {vrf} {group}
        * show ipv6 mfib vrf {vrf} {group} {source}
        * show ipv6 mfib vrf {vrf} verbose
        * show ipv6 mfib vrf {vrf} {group} verbose
        * show ipv6 mfib vrf {vrf} {group} {source} verbose
    * Added ShowIpv6Mrib
        * added the new parser for cli "show ipv6 mrib route"
        * show ipv6 mrib route
        * show ipv6 mrib route {group}
        * show ipv6 mrib route {group} {source}
        * show ipv6 mrib vrf {vrf} route
        * show ipv6 mrib vrf {vrf} route  {group}
        * show ipv6 mrib vrf {vrf} route  {group} {source}
    * Added ShowIsisRibRedistribution
        * show isis rib redistribution
    * Added ShowLicenseTechSupport
        * show license tech support
    * Added ShowLispRegistrationHistory
        * 'show lisp {lisp_id} instance-id {instance_id} {address_family} server {eid} registration-history'
        * 'show lisp {lisp_id} instance-id {instance_id} {address_family} server registration-history'
        * 'show lisp {lisp_id} instance-id {instance_id} {address_family} server {address_resolution} {eid} registration-history'
        * 'show lisp instance-id {instance_id} {address_family} server registration-history'
        * 'show lisp server registration-history'
    * Added ShowPlatformHardwareChassisFantrayDetailSwitch
        * show platform hardware chassis fantray detail switch {mode}
    * Added ShowPlatformHardwareChassisPowerSupplyDetailSwitchAll
        * show platform hardware chassis power-supply detail switch {mode} all
    * Added ShowPlatformSoftwareCpmSwitchB0CountersDrop
        * show platform software cpm switch {mode} B0 counters drop
    * Added ShowPlatformSoftwareCpmSwitchB0CountersPuntInject
        * show platform software cpm switch {mode} B0 counters punt-inject
    * Added ShowPlatformSoftwareCpmSwitchB0IpcDetail
        * show platform software cpm switch {mode} B0 ipc detail
    * Added ShowPlatformSoftwareCpmSwitchB0IpcBrief
        * show platform software cpm switch {mode} B0 ipc brief
    * Added ShowPlatformSoftwareCpmSwitchB0ControlInfo
        * show platform software cpm switch {mode} B0 control-info
    * Added ShowPlatformSoftwareCpmSwitchB0Resource
        * show platform software cpm switch {mode} B0 resource
    * Added ShowIdpromInterface
        * show idprom interface {mode}
    * Added ShowPlatformSoftwareBpCrimsonContentConfig
        * show platform software bp crimson content config
    * Added ShowPlatformSoftwareNodeClusterManagerSwitchB0Node
        * show platform software node cluster-manager switch {mode} B0 node {node}
    * Added ShowPlatformSoftwareNodeClusterManagerSwitchB0Local
        * show platform software node cluster-manager switch {mode} B0 local
    * Added ShowPlatformSoftwareTdlContentBpConfig
        * show platform software tdl-database content bp config {mode}
    * Added ShowPlatformSoftwareTdlContentBpOper
        * show platform software tdl-database content bp oper {mode}
    * Added ShowPlatformSoftwareNodeClusterManagerSwitchB0Counters
        * show platform software node cluster-manager switch {mode} B0 counters
    * Added ShowPlatformSoftwareBpCrimsonCounterOper
        * show platform software bp crimson content oper
    * Added ShowPlatformSoftwareBpCrimsonStatistics
        * show platform software bp crimson statistics
    * Added ShowStackwiseVirtualBandwidth
        * show stackwise-virtual bandwidth
    * Added ShowMdnsSdControllerDetail
        * Parser for Show Mdns-Sd Controller Detail
    * Fixed ShowDeviceTrackingDatabaseInterface parser
        * Modified regexp to match network_layer_address and link_layer_address
    * Fixed  ShowRunInterface parser
        * Added regexp to grep ipv6_nd_raguard_attach_policy and device_tracking_attach_policy
    * ShowIsisRib
        * Added the ability to parser the cli command `show isis rib flex-algo`
    * Added ShowLispIpv4ServerExtranetPolicyEid
        * show lisp instance-id {instance_id} ipv4 server extranet-policy {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server extranet-policy {prefix}
        * show lisp eid-table {eid_table} ipv4 server extranet-policy {prefix}
        * show lisp eid-table vrf {vrf} ipv4 server extranet-policy {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server extranet-policy {prefix}
    * Added ShowLispIpv6ServerExtranetPolicyEid
        * show lisp instance-id {instance_id} ipv6 server extranet-policy {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server extranet-policy {prefix}
        * show lisp eid-table {eid_table} ipv6 server extranet-policy {prefix}
        * show lisp eid-table vrf {vrf} ipv6 server extranet-policy {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server extranet-policy {prefix}
    * Added ShowPolicyMapTypeInspectZonePair
        * show policy-map type inspect zone-pair {zone_pair_name}
        * show policy-map type inspect zone-pair
    * Modified ShowVlanId
        * Added support vlan-name to be more diverse, including " ", "-", "_"

* iosxr
    * Added ShowEventManagerEnv
        * show event manager environment
        * show event manager environment all
        * show event manager environment | include {event_name}
    * Added ShowEventManagerPolicyRegistered
        * show event manager policy registered
        * show event manager policy registered {type}
        * show event manager policy registered {type} | include {eemfile_name}
    * Added ShowEventManagerPolicyAvailable
        * show event manager policy available
        * show event manager policy available {type}
        * show event manager policy available {type} | include {eemfile_name}
    * Added ShowRipIpv6
        * show rip ipv6
        * show rip ipv6 vrf {vrf}
    * Added ShowRipIpv6Statistics
        * show rip ipv6 statistics
        * show rip ipv6 vrf {vrf} statistics
    * Added ShowRipIpv6Database
        * show rip ipv6 database
        * show rip ipv6 vrf {vrf} database
    * Added ShowRipIpv6Interface
        * show rip ipv6 interface
        * show rip ipv6 vrf {vrf} interface

* generic
    * Modified ShowVersion
        * Added Optional <os_flavor> key to schema to better handle IOSXR show version output

* nxos
    * Added ShowForwardingIpv4Recursive
        * show forwarding ipv4 recursive
        * show forwarding ipv4 recursive vrf {vrf}

* ios
    * Added ShowPolicyMapTypeInspectZonePair
        * show policy-map type inspect zone-pair {zone_pair_name}
        * show policy-map type inspect zone-pair


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowMdnsSdSpSdgStatistics
        * Added support to agent and sp
    * Modified ShowMdnsSdSummaryVlan
        * Added support to agent and sp
    * Added TracerouteMPLSIPv4 parser
        * traceroute mpls ipv4 {addr} {mask}
    * Fixed ShowInterfacesStatusErrDisabled parser
        * Modified regexp to grep all kind of reasons
    * Fixed ShowFlowRecord Schema
        * Modified match_list and collect_list to Optional arg in schema as those are not mandate
    * Modified ShowAccessLists
        * Add support to role-based acl
    * Modified ShowIpPimTunnel
        * Modified to support different address family and vrf
    * Modified ShowIsisRibSchema
        * Added a new key to differentiate output by level type
        * Changed the flex algo key to contain a set of associated prefixes
        * No backwards compatibility
    * Modified ShowIsisRib
        * Modified a regex to parse lines starting with `Prefix-SID index`
    * Modified ShowSegmentRoutingTrafficEngPolicy
        * Added regex pattern p3_1 to handle different output
        * Added regex pattern p6_1 to handle different output
    * Modified ShowStormControl
        * Added support for pps/bps
        * Added support for command "show storm-control"
    * Modified ShowStormControl
        * Added support for Unknown-Unicast
    * Modified ShowInterfacesSwitchport
        * Fixed issue when parsing single interface that belongs to a port channel
    * Modified ShowLispServiceSummary
        * Fixed missing router ID when no banner
        * Added support for maximum db and map-cache values
    * Modified ShowRomVarSchema
        * Added "default_gateway,ip_address,crashinfo,subnet_mask" field to schema.
    * Modified ShowRomVar
        * Modified Regular Expression to handle if any value is provided with "" or without codes. Also modified to deal spaces in regular expression.
        * For few variables added len check for value. if value for that key is empty then that key will not be added to master key i.e rommon_variable.
    * Modified ShowBgpAllDetail
        * Updated the Schema to handle 'binding_sid' field
        * Added regex p20 and p20_1 to match the binding_sid

* generic
    * Modified ShowVersion
        * Modified schema key <model> to <pid>

* viptela
    * Modified ShowSystemStatus
        * Refactored parser to adhere to standard parser format
        * Modified almost all regexes and logic

* nxos
    * Modified ShowBgpSessions
        * Updated regex pattern p6_1 to split up 'nei' from 'linklocal_interfaceport'


