--------------------------------------------------------------------------------
<<<<<<< HEAD
                                      Fix
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpMroute
        * add lisp_mcast_source/lisp_mcast_group to outgoing interface ip mroute schema.
        * add '-' as additional possible character in "state"
        * Modified regex pattern to accomodate state with lowercase letters
    * Modified ShowAuthenticationSessionsInterfaceDetails
        * Added optional key unauth_timeout to schema.
            * Added regex pattern p13 to accept all type of inputs for restart_timeout.
            * Added regex pattern p14 for unauth_timeout key.
            * Added keys unauth_timeout into the schema.
    * Modified ShowAuthenticationSessionsInterfaceDetails
        * Removed session_timeout from known_list on p1 to fix incorrect match
    * Added ShowInterfaceTransceiver for
        * show interfaces {interface} transceiver
    * Modified ShowInterfaceTransceiverDetail to
        * Parse transceiver information
    * Modified ShowVrfDetailSuperParser
        * Added keys <import_route_map> and <export_route_map> to schema.
        * Added regex patterns <p7_2> and <p8_2> to accommodate various outputs.
    * Modified ShowIpStaticRoute
        * Fixed line stripping issue that broke Ops unittests.
    * Modified
        * Modified show_device_tracking.py to fix a bug in show_device_tracking
        * Now able to match entries with time left
    * Modified ShowUsers
        * Bug workaround to capture location data when it's forced onto a newline.
    * Modified ShowPolicyMapTypeSuperParser
        * Changed <pattern> from schema to Optional.
        * Updated regex patterns <p0> and <p12> to accommodate various outputs.
        * Added regex patterns <p3_1>, <p8_0>, <p9_0> to accommodate various outputs.
    * Modified ShowPlatformSoftwareMemoryBacktraceSchema
        * Changed type for callsite from int to str
    * Modified ShowIpStaticRoute
        * Added support for dashes in names
    * Modified ShowIpv6StaticDetail
        * Added support for dashes in names
    * Modified ShowPlatformResourcesSchema
        * Made 'esp' optional
    * Modified ShowLogging
        * Fixed patterns to support show logging parser when monitor logging is disabled
        * Fixed pattern p11 to recognize vrf information
    * Modified ShowLoggingSchema
        * Made monitoring keys (level, message_logged, xml and filtering) optional
    * Modified ShowVersion
        * only accepted digits for Motherboard Revision Number now accept all characters.
    * Added Parser for ShowRedundancyApplicationGroup
        * show redundancy application group {group_id}
    * Modified ShowIpEigrpInterfaces
        * Adjusting p1 regex to support IPv6 too
        * Offloading parser to a SuperParser class
        * Support eigrp named mode
        * Added Optional keys to ShowIpEigrpInterfacesSchema schema to support `show ip eigrp interfaces detail parser`
    * Modified ShowInterfaces
        * Updated regex pattern p11 to accomodate media types with a period (ex 2.5G)

* nxos
    * Modified ShowRunningConfigNvOverlay
        * Added key <ingress_replication_protocol_bgp> to schema
        * Added regex pattern <p17> and related code
    * Modified ShowInterface
        * Modified regex pattern <p1> to accomodate different link states
        * Added regex pattern <p4_1> to process various VLAN description outputs
        * Added unit test to support changes
    * Modified ShowInterfaceTransceiverDetails
        * Added regex pattern <p37_1> as a catch-all for when <p37> doesn't match.
    * Modified ShowIpRoute
        * Added key <asymmetric> to schema
        * Added regex pattern <p3> and related code
    * Modified ShowIpInterfaceBriefVrfAll
        * Added in workaround for vrf information not being output
    * Modified ShowInterface
        * Added regex pattern p3_1 to process MAC address and type for VLAN.
    * Modified ShowIpInterfaceBriefVrfAll
        * Changed Schema to record vrf info
        * Changed parser to capture vrf info
    * Modified ShowCdpNeighbors
        * Added regex patterns p6 and p7 to accept Linux interface names
        * Added unittest
        * Added folder based unittest
    * Modified ShowInterface
        * Fixed issue where incoming storm supression being measured in bytes would cause in_jumbo_packets to not be parsed.
    * Modified ShowInterfaceBrief
        * Fixed issue with parser when speed for 'mgmt0' wasn't a digit

* iosxr
    * Modified ShowL2vpnBridgeDomainDetail
        * Fixed variable referenced before assignment error
        * Added support for outputs where MPLS data wants to be inside the LSP dict
        * Added support for more keys in the schema to match sample output
    * Modified ShowOspfv3VrfAllInclusiveNeighborDetail
        * changed 'state' to return lowercase instead of the default uppercase.

* ios
    * Added ShowInterfaceTransceiver for
        * show interface {interface} transceiver

* added showinterfacetransceiverdetail for
    * show interface {interface} transceiver detail

* unittest
    * Modified SuperFileBasedTesting
        * Added check to skip classes that do not contain a cli_command. This serves to skip outdated tcl based parsers.

* iosxe
    * Modified ShowVrrp
        * Added schema key <address family> to handle new device output
        * Added <master_advertisement_expiration_secs> key to schema
        * Added <state_duration> key to schema
    * Modified ShowPolicyMapTypeSuperParser
        * Updated regex pattern p3 to make bytes optional
    * Modified ShowDeviceTrackingDatabase
        * Update regex to capture output related to 'time left' for 'show device-tracking database'
    * Added ShowPolicyMapTypeControlSubscriberBindingPolicyName
        * show policy-map type control subscriber binding {policy_map_name}

* nxos
    * Modified ShowIsisAdjacency
        * Fixed p2 regex to match lines with SNPA N/A and level 1-2
    * Modified ShowNveInterfaceDetailSchema
        * Added anycast_if key to the schema

* nx-os
    * Modified ShowLldpNeighborsDetail
        * If an NX-OS device is connected to an IOS-XR device the interface formats will be processed

* utils
    * Modified Common.py - Common.convert_intf_name
        * Dictionary containing interface conversions is now nested.
        * Created *generic* key as a catchall for previous code.
        * Edited logic to check if a specific operating system is mentions in the os= argument

* iosxr
    * Modified ShowIpInterfaceBrief class
        * Updated regex to make VRF optional
        * IOSXE
            * Modified ShowClassMap
                * Added missing quotes to cli_command


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* iosxe
    * Added ShowMabAllDetails
        * show mab all details
    * Added ShowIpDhcpDatabase
        * show ip dhcp database
    * Added ShowIpBgpL2VPNEVPN
        * Added parser for "show ip bgp l2vpn evpn detail"
        * Added parser for "show ip bgp {address_family} evi {evi}
        * Added parser for "show ip bgp {address_family} route-type {rt}"
        * Added parser for "show ip bgp {address_family} evi {evi} route-type {rt}"
        * Added nlri_data object under prefixes in "ShowBgpAllDetailSchema"
        * Added pmsi_data object under prefixes in "ShowBgpAllDetailSchema"
        * Added igmpmld object under prefixes in "ShowBgpAllDetailSchema"
        * Added 4 regexp in ShowBgpDetailSuperParser
            * p3_3 to handle all EVPN route-types
            * p8_6 to handle PMSI attribute Flags
            * p19 to handle IGMP/MLD filter
        * Modified 3 regexp in ShowBgpDetailSuperParser
            * p11 to handle local IRB vxlan vtep
            * p12 to handle core bdi
            * p13 to handle evpn l3-vni
        * Added folder based unittests
    * Added ShowPortSecurity
        * show port-security
        * show port-security interface <interface>
    * Added ShowPlatformSoftware
        * for 'show platform software object-manager switch {switchvirtualstate} {serviceprocessor} statistics'
    * Added ShowIpv6EigrpInterfaces
        * show ipv6 eigrp interfaces
    * Added ShowIpEigrpInterfacesDetail
        * show ip eigrp interfaces detail
    * Added ShowIpv6EigrpInterfacesDetail
        * show ipv6 eigrp interfaces detail
    * Added ShowKeyChain
        * show key chain
    * Added ShowIpv6Protocols
        * show ipv6 protocols
        * show ipv6 protocols vrf {vrf}
    * Added ShowInterfacesLink
        * show interfaces link
        * show interfaces {interface} link

* iosxr
    * Added ShowOspfInterface
        * show ospf interface
        * show ospf interface <interface_name>
        * show ospf <process_name> interface
        * show ospf <process_name> interface <interface_name>
    * Added ShowOspfv3VrfAllInclusiveDatabasePrefix
        * show ospfv3 vrf all-inclusive database prefix
    * Added ShowOspfv3VrfAllInclusiveDatabaseRouter
        * show ospfv3 vrf all-inclusive database router
    * Added ShowOspfNeighbor
        * show ospf neighbor
        * show ospf {process_name} neighbor
        * show ospf vrf all-inclusive neighbor

* nxos
    * Added RunBashTop
        * Added 'top -n 1' command under 'run bash' mode
    * Added ShowSystemInternalProcessesMemory
        * 'show system internal processes memory'

* ios-xr
    * Added ShowOspfDatabaseRouter
        * show ospf database {process-id} router
        * show ospf database all-inclusive router

* ios
    * Added ShowLldpNeighbors
        * show lldp neighbors
    * Added ShowIpv6EigrpInterfaces
        * show ipv6 eigrp interfaces
    * Added ShowIpEigrpInterfacesDetail
        * show ip eigrp interfaces detail
    * Added ShowIpv6EigrpInterfacesDetail
        * show ipv6 eigrp interfaces detail
    * Added ShowKeyChain
        * show key chain
    * Added ShowIpv6Protocols
        * show ipv6 protocols
        * show ipv6 protocols vrf {vrf}

* iosxe
    * Added ShowDeviceTrackingPolicies
        * add show command 'show device-tracking policies'

* asa
    * Added ShowCryptoIkev2Sa
        * show crypto ikev2 sa
    * Added ShowNameif
        * show nameif
    * Added ShowFailover
        * show failover
    * Added ShowFailoverInterface
        * show failover interface


=======
                                      New                                       
--------------------------------------------------------------------------------

* asa
        * Added ShowVersion
>>>>>>> 7b91b71fa (Added ASA ShowVersion)
