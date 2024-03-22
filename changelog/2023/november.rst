--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareFedSwitchActiveIFMInterfacesSVI
        * Added schema and parser for 'sh platform software fed {switch} {active} ifm interfaces svi'
    * Added ShowPlatformSoftwareFedSwitchActiveIFMMappingsEtherchannel
        * Added schema and parser for 'show platform software fed {switch} {mode} ifm mappings etherchannel'
    * Added ShowBfdInternal
        * Added schema and parser for 'show bfd internal'
    * Added ShowCryptoPkiCertificatesPemServer
        * Added new parser for cli 'show cry pki certificates pem server'
    * Added ShowObjectGroupName
        * added parser for "show object-group name {group_name}"
    * Added ShowOspfv3NeighborInterface
        * show ospfv3 neighbor {interface}
    * Added ShowPlatformSoftwareSteeringPolicyAomInfo
        * parser for cli 'show platform software steering-policy forwarding-manager switch {switch} F0 policy-aom-info'
    * Added ShowPlatformSoftwareObjectManagerF0Object
        * parser for cli 'show platform software object-manager switch {switch} F0 object {object}'
    * Added ShowLispVrf
        * parser for cli 'show lisp vrf {vrf}'
    * Added ShowPlatformSoftwareAccessListSwitchActiveFPActiveOgLkupIds
        * parser for Show Platform Software Access List Switch Active FP ActiveOgLkupIds
    * Added ShowQfpDropsThresholds
        * show qfp drops thresholds
    * Added ShowConsistencyCheckerMcastStartAll
        * "show consistency-checker mcast {layer} start all"
        * "show consistency-checker mcast {layer} start {address} {source}"
        * "show consistency-checker mcast {layer} start {address}"
        * "show consistency-checker mcast {layer} start vrf {instance_name} {address} {source}"
        * "show consistency-checker mcast {layer} start vlan {vlan_id} {address}"
    * Added ShowConsistencyCheckerRunIdDetail
        * "show consistency-checker run-id {id} detail"
    * Added ShowConsistencyCheckerRunId
        * "show consistency-checker run-id {id}"

* iosxe/c9300
    * Modified ShowEnvironmentAll
        * Added support for < Sensor List Environmental Monitoring >.

* iosxr
    * Added ShowOspfProcessName
        * Parser for cli 'show ospf {process_name}'
    * Added ShowOspfv3ProcessName
        * Parser for cli 'show ospfv3 {process_name}'
    * Added ShowPtpForeignMastersBrief
        * Added parser for show ptp foreign-masters brief

* nxos
    * Added ShowMacSecMkaSummary
        * parser for 'show macsec mka summary'
    * Added ShowMacSecMkaSession
        * parser for 'show macsec mka session'
    * Added ShowMacSecMkaSessionDetails
        * parser for 'show macsec mka session details'
    * Added ShowMacSecMkaStats
        * parser for 'show macsec mka statistics'

* sonic
    * Added ShowVersion
        * Added new OS SONiC and created ShowVersion parser
    * Inherited DockerStatsNoStream from Linux parsers


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Fix for ShowPlatformHardwareFedSwitchQosQueueConfig
        * Added str and list pattern to match all possible values
    * Modified ShowPlatformSoftwareFedActiveAclInfoDbDetail
        * Added ipv6 source and destination
    * Modified ShowIpv6Interface Parser
        * parser for 'show ipv6 inerface {interface}' added new regex p18_1.
    * Modified ShowSpanningTree Parser
        * parser for 'show spanning tree' added new regex p1_1,p1_2,p1_3,p1_4
    * Modified ShowPlatformFedActiveTcamUtilization
        * Modified cli_command
    * Modified ShowPlatform
        * show platform parser now recognizes 'init, active' state
    * Modified ShowPlatformSoftwareMemoryCallsite
        * Enhanced ShowPlatformSoftwareMemoryCallsite parser to work for show platform software memory fed switch active alloc callsite brief
    * Modified ShowCryptoPkiCertificatesPemServer
        * Enhanced the parser by adding '\n' to each line in the output
    * Fix for ShowPdmSteeringPolicy
        * fixed old parser for cli 'show pdm steering policy' to capture full contract name as contract name can be anything
    * Fix for ShowPlatformSoftwareFedActiveSecurityFed
        * fixed old parser for cli 'show platform software fed {switch} active security-fed sis-redirect firewall all' due to change in output
    * Modified ShowRunInterface
        * Added 112 regex for service-policy outputs
    * Fix for ShowSpanningTreeSummary
        * Added additional key "bpdu_sender_conflict"
    * Modified for ShowAccessSessionInterfaceDetails parser
        * Added new regex <p11_1> for matching ipv6 address '1555105ced6cc3825b39d' '1555102251fffe005'
    * Modified ShowLispIpv4Publication
        * Added support for missing locator addresses.
    * Modified ShowLispIpv6Publication
        * Added support for missing locator addresses.
    * Modified ShowLispServiceDatabase
        * Added support for optional Service-Insertion ID.
    * Modified ShowNat66Statistics
        * Changed enable_count from schema to Optional.
        * Updated regex pattern p0 to accommodate various outputs
    * Added ShowPlatformSoftwareDistributedIpsecTunnelInfo
        * Added ShowPlatformSoftwareDistributedIpsecTunnelInfo for CLI "show platform software distributed-ipsec tunnel-info".

* iosxr
    * Modified ShowIsisInterface Parser
        * Modified pattern r38 to support "Layer-2 Multicast"
        * Modified pattern r40 to support "All ISs              Listening"
        * Added key "lsp_rexmit_queue_size" in topology section in schema
    * Modified ShowBgpInstanceNeighborsDetail
        * Added Optional parameter configured_keepalive_interval to schema
        * Added Optional parameter configured_holdtime to schema
        * Added Optional parameter ttl_security to schema
        * Added Optional parameter external_bgp_neighbor_hop_count to schema
        * Added Optional parameter bfd to schema
        * Added Optional parameter bfd_status inside bfd to schema
        * Added Optional parameter session_status inside bfd to schema
        * Added Optional parameter mininterval inside bfd to schema
        * Added Optional parameter multiplier inside bfd to schema
        * Added Optional parameter messages to schema
        * Added Optional parameter messages_count inside messages to schema
        * Added Optional parameter notifications inside messages to schema
        * Added Optional parameter queue inside messages to schema
        * Added pattern for graceful_restart key
        * Added pattern for graceful_restart_restart_time key
        * Added pattern for graceful_restart_stalepath_time key
    * Modified ShowOspfDatabase
        * Modified Router Id option to schema as Optional.
        * Added regex pattern p5 to match lsa type 2 network link.

* nxos
    * Added
        * Updated regex <p1> with <.> in <type> field
    * Modified ShowInterfaceCounters
        * Modified regex to handle `--` in interface counters output.
    * Modified show_interface_status
        * Modified the p1 regex pattern to capture missing data and remove junk
    * Fixed ShowInterface Parser
        * Fixed regex for some failing output of show interface status command


