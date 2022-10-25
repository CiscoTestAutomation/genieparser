--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* hvrp
    * Added DisplayBgpPeer
        * display bgp {address_family} vpn-instance {vrf} peer
        * display bgp {address_family} all peer
        * display bgp {address_family} peer
        * display bgp peer
    * Added DisplayBgpPeerSummary
        * display bgp all summary
    * Added DisplayBgpPeerVerbose
        * display bgp {address_family} peer {peer_address} verbose
        * display bgp {address_family} peer verbose
        * display bgp {address_family} all peer {peer_address} verbose
        * display bgp {address_family} all peer verbose
        * display bgp {address_family} vpn-instance {vrf} peer {peer_address} verbose
        * display bgp {address_family} vpn-instance {vrf} peer verbose
        * display bgp peer {peer_address} verbose
        * display bgp peer verbose

* iosxe
    * Added ShowTelemetryIETFSubscriptionAllReceivers
        * show telemetry ietf subscription all receivers
    * Added ShowCallHomeVersion
        * show call-home version
    * Added ShowCallHomeSmartLicensing
        * show call-home smart-licensing
    * Added ShowCallHomeMailServerStatus
        * show call-home mail-server status
    * Added ShowCallHomeProfileAll
        * show call-home profile all
    * Added ShowPlatformHardwareRegisterReadAsic
        * show platform hardware fed active fwd-asic register read register-name xyz asic n core m
        * show platform hardware fed switch x fwd-asic register read register-name xyz asic n core m
    * Added ShowInterfaces
        * Added is_deleted key to schema to identify deleted interfaces.
    * Added ShowPlatformSoftwareMemorySwitchAllocCallsite
        * 'show platform software memory fed switch {switch_num} alloc callsite brief'
        * 'show platform software memory fed {switch_type} alloc callsite brief'
    * Added ShowPlatformSoftwareMemorySwitchAllocBacktrace
        * 'show platform software memory fed switch {switch_num} alloc backtrace'
        * 'show platform software memory fed {switch_type} alloc backtrace'
    * Added ShowPlatformHardwareFedSwitchQosDscpcosCounters
        * 'show platform hardware fed switch {switch_num} qos dscp-cos counters interface {interface}'
        * 'show platform hardware fed switch {switch_type} qos dscp-cos counters interface {interface}'
    * Added ShowPlatformSoftwareFedSwitchActivEAclUsage
        * added new parser for cli "show paltform software fed switch active acl usage"
    * Added ShowPlatformSwitchActiveTcamUtilization
        * added new parser for cli "show platform hardware fed switch active fwd-asic resource tcam utilization"
    * Added ShowPlatformHardwareIomdQosPortIngressQueueStats
        * added new parser for clis
            * 'show platform hardware iomd <slot> qos port <no> ingress queue stats'
            * 'show platform hardware iomd switch <switch_no> <slot> qos port <no> ingress queue stats'
    * Added ShowPlatformHardwareIomdPortgroups
        * added new parser for clis
            * 'show platform hardware iomd <slot> portgroups'
            * 'show platform hardware iomd switch <switch_no> <slot> portgroups'
    * Added ShowPlatformHardwareFedActiveQosQueueConfigInterface
        * added new parser for clis
            * 'show platform hardware fed active qos queue config interface'
            * 'show platform hardware fed switch <no> qos queue config interface'
    * Added ShowPlatformHardwareQfpActiveInfrastructureExmemStatistics
        * show platform hardware qfp active infrastructure exmem statistics
    * Added ShowCryptoKeyMypubkeyMasterSchema
    * Added ShowCryptoKeyMypubkeyAll
        * show crypto key mypubkey all
    * Added ShowCryptoKeyMypubkeyRsa
        * show crypto key mypubkey rsa
    * Added ShowCryptoKeyMypubkeyEc
        * show crypto key mypubkey ec
    * Added ShowCryptoKeyMypubkeyRsaKeyName
        * show crypto key mypubkey rsa {key_name}
    * Added ShowCryptoKeyMypubkeyEcKeyName
        * show crypto key mypubkey ec {key_name}
    * Modified ShowLicenseTechSupport
        * Updated to parse new keys added in show license tech support. i.e. telemetry_report_summary
    * Added ShowCryptoIkev2Performance
        * show crypto ikev2 performance
    * Added ShowIpOspfDatabaseSummaryDetail
        * show ip ospf database database-summary detail
        * show ip ospf {process_id} database database-summary detail
    * Added ShowMonitorCaptureBuffer
        * show monitor capture {capture_name} buffer
    * Added ShowFQDNDatabase
        * added new parser for cli "show fqdn database"
    * Added ShowIpv6NdRaPrefix
        * added new parser for cli "show ipv6 nd ra nat64-prefix"


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowCtsInterface
        * Updated regex pattern <p2> to support Tunnel and Ethernet subinterfaces
    * Modified ShowIpInterface
        * Fixed bug where first line of the command is the output and the hostname contains an IP.
        * Improved Multicast reserved groups parsing when the IPs span multiple lines
    * Modified ShowModule
        * Added regex to match switches to support svl devices"
    * Modified ShowIsisNode
        * Changed the schema to match the 9500-X output"
    * Modified ShowL2vpnEvpnEthernetSegmentDetail
        * Fix bug in parser where CLI was being invoked twice
        * Change type of the 'interface' key in schema to 'list' (NOT BACKWARDS COMPATIBLE)
        * Change type of the 'ordinal' key to also allow 'str'
        * Fix bug when RD takes multiple lines in raw output
    * Modified ShowArp
        * Allow 'type' key to include '.' in regex pattern. E.g. '802.1Q'
    * Modified ShowPlatformFedActiveIfmMapping
        * Modified "group['ifgId'] is not None,
    * Created cat9k test symbolic link
    * Modified ShowPlatformSoftwareFedActiveAclSgacl
        * Fixed format for missing variable"
    * c9400
        * Modified ShowModule
            * Updated regex pattern <p2> to accommodate various outputs
    * Modified MonitorCaptureStopSchema
        * changed the parameter bytes_dropped_in_asic in MonitorCaptureStopSchema as optional, since it is not collected in silicon devices

* nxos
    * Modified ShowBgpL2vpnEvpnRouteType
        * Modified ShowBgpL2vpnEvpnRouteType to include VRF option in cli command.
        * Added Optional keys "pathtype", "as_path", "imported_from", and "gateway_ip" to schema.
        * Added path_type, which was matched in <p8> but unused previously, to dictionary output.
        * Added as_path, which was matched in <p9> but unused previously, to dictionary output.
        * Updated <p9> to accommodate AS-Paths that are not 'NONE'.
        * Added <p20> to parse the optional line with the format "Imported from 99.99.99.9910[5][0][0][32][100.4.1.2]/224".
        * Added <p21> to parse the optional line with the format "Gateway IP 0.0.0.0".

* iosxr
    * Modified ShowMplsLdpBindings
        * Modified Local bindings options to schema as Optional.


