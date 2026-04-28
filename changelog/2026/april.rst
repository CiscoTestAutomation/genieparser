--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowTelemetryIETFSubscription
        * Handling renamed column header
    * Modified ShowTelemetryIETFSubscriptionAllReceivers
        * Handling added field
    * Modified ShowTelemetryReceiverName
        * Handling renamed column header
    * Modified ShowTelemetryReceiverAll
        * Handling renamed column header
    * Added ShowIpv6Dhcp
        * Added schema and parser for 'show ipv6 dhcp'
    * Added ShowPlatformHardwareQfpActiveInterfaceAllStatistics parser in show_platform_hardware.py
        * Added schema and parser for cli 'show platform hardware qfp active interface all statistics'
    * Added ShowPlatformSoftwareLiveProtectShield
        * show platform software live-protect shield
    * Added ShowIpSshPubkeyServerAll
        * Added schema and parser for 'show ip ssh pubkey server all'
    * Created ShowSystemInsecureConfiguration
        * Added schema and parser implementation for "show system insecure-configuration".
    * Created ShowSystemSecurityMode
        * Added schema and parser implementation for "show system security-mode".
    * Added SnmpGetBulk
        * Added schema and parser for 'snmp get-bulk v{version} {ip} vrf {vrf} {community_str} non-repeaters {non_repeaters} max-repetitions {max_repetitions} oid {oid}' command.
        * Added schema and parser for 'snmp get-bulk v{version} {ip} {community_str} non-repeaters {non_repeaters} max-repetitions {max_repetitions} oid {oid}'
        * Added timeout parsing support for invalid VLAN community strings.
    * Added ShowPlatformSoftwareAccessListFpActiveStatistics
        * Added schema and parser for 'show platform software access-list fp active statistics'
    * Added ShowRepTopology
        * Added schema and parser for 'show rep topology'
    * Added ShowPlatformHardwareSlotSlotSensorConsumerAll
        * Added schema and parser for 'show platform hardware slot {slot} sensor consumer all'
    * Modified ShowTelemetryIETFSubscriptionDetail
        * Adding parsing of reciever information
    * Added ShowPlatformSoftwareFedSwitchFnfFlowTableMonId
        * Parser for 'show platform software fed switch {switch} fnf flow-table mon-id {mon_id} asic {asic} start-index {start_index} {num_flows}'
    * Added ShowPlatformHardwareSlotSlotSensorProducerAll
        * Added schema and parser for 'show platform hardware slot {slot} sensor producer all'
    * Added ShowRedundancyInterchassis parser in show_redundancy.py
        * Added schema and parser for cli 'show redundancy interchassis'
    * Added ShowPlatformSoftwareFedSwitchActiveVmapAll parser.
        * Added parser for cli 'show platform software fed switch active vmap all'.
    * Added ShowPlatformSoftwareFedSwitchActiveVpKeyDetail parser.
        * Added parser for cli 'show platform software fed switch active vp key {iif_id} {vlan_id} detail'.
    * Added ShowPolicyMapControlPlaneAll
        * Added schema and parser for 'show policy-map control-plane all'
    * Added show platform software selinux
        * Added schema and parser for show platform software selinux
    * Added ShowInterfacesInterfaceStat
        * Added schema and parser for 'show interfaces {interface} stat'
    * Added Parser for show cts keystore
        * Added a new schema and parser for the show cts keystore command.
    * Added show ipv6 route vrf {vrf} summary internal
        * Parse "show ipv6 route vrf {vrf} summary internal"
    * Added ShowHwModuleSubslotSubslotTransceiverTransceiverStatus
        * Added schema and parser for 'show hw-module subslot {subslot} transceiver {transceiver} status'

* iosxr
    * Added ShowControllersInterface
        * Added schema and parser for 'show controllers {interface}' command.
    * Added ShowControllersOpticsAppselAdvertised
        * Added schema and parser for 'show controllers optics {port} appsel advertised' command.
        * Added schema and parser for 'show controllers optics * appsel advertised' command.
    * Added ShowControllersOpticsObservableInfo
        * Added schema and parser for 'show controllers optics {port} observable-info' command.
        * Added schema and parser for 'show controllers optics * observable-info' command.
    * Added ShowControllersOpticsAppselDetailed
        * Added schema and parser for 'show controllers optics {port} appsel detailed' command.
        * Added schema and parser for 'show controllers optics * appsel detailed' command.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowPlatformSoftwareFedActiveMonitor
        * Updated regex pattern and code the fetch the valn name.
    * Modified ShowPlatformSoftwareFedSwitchActiveMatmMactable
        * Updated regex pattern to handle "machandle", "sihandle", "rihandle", "dihandle" values.
    * Modified ShowCryptoIpsecSaInterface
        * Updated regex pattern p3 and p30 to handle missing remaining_key_lifetime values.
    * Modified ShowModule
        * Updated show module parsing to correctly match module entries for multiple entries also(switch number 1 and 2).
    * Modified ShowIpv6cefExactRouteSchema parser
        * changed regex to take both ip and ipv6 addresses
    * Modified ShowPlatformHardwareFedSwitchActiveVlanIngress
        * Modified parser by adding cli 'show platform hardware fed switch active vlan {num} egress'
    * Modified ShowPlatformSoftwareFedSwitchActiveMatmMactable
        * Made 'machandle', 'sihandle', 'rihandle', 'dihandle' fields optional in schema
        * Updated regex to handle output format without handle columns
    * Modified ShowPlatformSoftwareFedIpv6RouteSummaryInclude
        * Added support to make available of below clis for all cat9k.
    * show platform software fed {switch} {mode} ipv6 route summary | include {match}
    * show platform software fed {mode} ipv6 route summary | include {match}
    * Modified ShowDeviceTrackingDatabase
        * Updated regex pattern to handle parenthesized time_left values from DHCPv6 prefix delegation entries.

* iosxr
    * Modified ShowPlatform
        * Modified parser for 'show platform' command to include '[]' in Type column


--------------------------------------------------------------------------------
                                    Command.                                    
--------------------------------------------------------------------------------


