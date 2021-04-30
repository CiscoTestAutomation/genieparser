--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* ASA
    * Modified ShowRoute
        * Added regex pattern <p5_1> to accommodate newer outputs.

* IOSXE
    * Modified ShowSslProxyStatistics
        * Updated schema to accommodate the 17.5 release output.
    * Modified ShowTcpProxyStatistics
        * Updated schema to accommodate the 17.5 release output.
    * Modified ShowInterfaces
        * Update schema to include optional line protocol err-disabled state if it exists
        * Update condition to display line protocol err-disabled state if it exists
        * Update 3 of the existing golden_output2_expected to accomodate schema changes
        * Add folder based unittests
    * Modified ShowInventory
        * Modified regex pattern <p1_6> to accommodate various outputs.
    * Modified ShowWlanAll
        * Added Optional keys <wifi_direct_policy>, <multicast_buffer_frames>, <dual_neighbor_list>, <client_scan_report_11k_beacon_radio_measurement>, <request_on_association>, and <request_on_roam> into the schema.
        * Changed <multicast_buffer_size> from schema to Optional.
        * Updated regex pattern <p_multi_buffer_frames> to correctly accommodate outputs.
    * Modified ShowBgp
        * Update cli_command list to display address family correctly
    * Modified ShowWirelessMobilitySummary
        * Updated regex pattern <pmtu> to accommodate various outputs.
    * Modified
        * Modified show_interface.py to fix a bug in ShowInterfacesSwitchport
        * Also modified iosxe current tests because they were wrong

* NXOS
    * Modified ShowIpRoute
        * Added sorting of next_hop_list
        * ShowIpv6Route, ShowRouting are affected by this change as well
    * Modified ShowPortChannelDatabase
        * Support for 'on' activity of interface member
    * Modified ShowRunningConfigNvOverlay
        * added support for multisite_ingress_replication_optimized under l3 vni in nve interface
    * Modified ShowVlan
        * Updated regex pattern <p1> to accommodate various outputs.
    * Modified ShowIpv6PrefixList
        * Support for 'af' argument of cli command

* IOSXR
    * Modified ShowBgp
        * Add try/except when assigning <remote_as> as an int
    * Modified ShowIsisInterface
        * Now capable of handling CLNS MTU field with an error message
        * Correctly handles the 'protocol_state' field under each AF / Topology
    * Modified ShowPlatform
        * Update regex p1 - to accept additional states for 'show platform' command
        * Update logic to include missing subslots
        * Add folder based unittests

* Utils
    * Modified Unittesting
        * Unittests have more features for testing
        * Fixed all broken unittests

* UTILS
    * Fixed issue with parser json loading by moving load time from import to first call

* IOS
    * Modified
        * Modified show_interface.py to fix a bug in ShowInterfacesSwitchport
        * Also modified ios current tests because they were wrong


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* Comware
    * Added DisplayInterfaces for:
        * 'display interface'
        * 'display interface <interface>'

* IOSXE
    * Added ShowSdwanAppqoeFlowAll
        * 'show sdwan appqoe flow all'
    * Added ShowIox
        * show iox-service
    * Added ShowApphostingInfra
        * show app-hosting infra

* Check Point Gaia OS
    * New platform added called 'gaia'
        * Note This name aligns with with netmiko driver name ('gaia') and is similar to the napalm driver ('gaiaos')
    * Included parsers
        * show interface
        * show users
        * show ntp
        * show arp
        * show version
    * Parsers are for clish commands only. Expert mode commands are not currently supported.
    * Tested under Check Point Gaia R80.40
    * All parsers include tests, and all module tests passing.

* JUNOS
    * Added ShowMplsLdpParameters
        * show mpls ldp parameters

* IOSXR
    * Added ShowMplsLdpBindings
        * show mpls ldp bindings
    * Added ShowProtocols
        * show protocols {protocol}
        * folder based unittests
    * Added ShowBgpNexthops
        * Add Show command 'show bgp nexthops {ipaddress}'
    * Added ShowArmIpv4Conflicts
        * show arm ipv4 conflicts
    * Added ShowCefDetail
        * show cef {afi} {prefix} detail
        * folder based unittests

* UTILS
    * Modified Common
        * Added ParserNotFound custom exception class when parser is not found
    * Modified Common
        * Added 'tu' 'Tunnel' to convert list of interfaces

* APIC
    * Added ShowVersion
        * added parser for `show version`
    * refactored unittests to be folder based

* Junos
    * Added ShowMplsLdpDiscoveryDetail
        * show mpls ldp discovery detail
        * folder based unittests


