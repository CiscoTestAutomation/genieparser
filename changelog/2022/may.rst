--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowNhrpStats
        * show nhrp stats
    * Added ShowNhrpStatsDetail
        * show nhrp stats detail
    * Added ShowMatmMacTable
        * show platform software fed {state} matm macTable vlan {vlan}
    * Added ShowIgmpSnooping
        * show platform software fed {state} ip igmp snooping vlan {vlan}
    * Added ShowIgmpSnoopingGroups
        * show platform software fed {state} ip igmp snooping groups vlan {vlan}
    * Added ShowIpv6MldSnoopingGroups
        * show platform software fed {state} ipv6 mld snooping groups vlan {vlan}
    * Added ShowFedActiveIpv6MldSnoopingVlan
        * show platform software fed {state} ipv6 mld snooping vlan {vlan}
    * Added ShowBfdSummaryHost
        * Added new parser for cli "show bfd summary host"
    * Added ShowCryptoGdoiGm
        * Added new parser for cli "show crypto gdoi gm"
    * Added ShowCryptoIkev2SaRemoteDetail parser
        * show crypto ikev2 sa remote {ip_address} detail
    * Added ShowCryptoIkev2SaRemote parser
        * show crypto ikev2 sa remote {ip_address}
    * Added ShowCryptoSocketsInternal
        * show crypto sockets internal
    * Added ShowDmvpnCountStatus
        * added new parser for cli "show dmvpn | count Status {service}"
    * Added ShowIpNhrp
        * show ip nhrp
    * Added ShowIpNhrpDetail
        * show ip nhrp detail
    * Added ShowIpNhrpNhs
        * show ip nhrp nhs
        * show ip nhrp nhs {tunnel}
    * Added ShowIpNhrpNhsDetail
        * show ip nhrp nhs detail
        * show ip nhrp nhs {tunnel} detail
    * Adding new schema and parser in Show_platform.py
        * Added schema and parser for ShowPlatformSoftwareFedIpsecCounter
    * Added ShowU2MSR
        * show plshow platform hardware qfp active feature uni-sr
    * Added ShowPowerInlineDetail
        * show power inline {interface} detail
    * Added ShowPowerInlinePolice
        * show power inline police
        * show power inline police {interface}
    * Added 'ShowRunIncludePtp' schema and parser
        * show run | include ptp
    * Added ShowSdwanAppHostingOperData
        * for 'show sdwan app-hosting oper-data'
    * Added ShowUtdEngineStandardStatistics
        * show utd engine standard statistics
    * Added ShowUtdEngineStandardStatisticsDaqAll
        * show utd engine standard statistics daq all
    * Added ShowModule
        * show module
    * Added ShowRedundancyRpr
        * show redundancy rpr
    * Added subclass ShowLispInstanceIdEthernetMapCacheRAR and ShowLispInstanceIdEthernetMapCachePrefixRAR for parsing Map-Cache RAR and Map-Cache RAR prefix inheriting from Superparsers
    * Modified superparser ShowLispMapCacheSuperParser and ShowLispIpMapCachePrefixSuperParser
    * Added ShowPlatformHardwareVoltageMarginSwitch
        * show platform hardware voltage margin switch {mode} rp active
    * Modified the ShowLogging
        * Fix for local variable referenced before assignment
    * Added ShowIpv6NhrpSummary
        * added new parser for cli "show ipv6 nhrp summary"
    * Added parsers for the following show commands
        * ShowLispInstanceServerRAR
            * show lisp {lisp_id} instance-id {instance_id} ethernet server reverse-address-resolution parser
            * show lisp instance-id {instance_id} ethernet server reverse-address-resolution
        * ShowLispInstanceServerRARDetail
            * show lisp {lisp_id} instance-id {instance_id} ethernet server reverse-address-resolution detail
            * show lisp {lisp_id} instance-id {instance_id} ethernet server reverse-address-resolution {mac}
            * show lisp instance-id {instance_id} ethernet server reverse-address-resolution detail
            * show lisp instance-id {instance_id} ethernet server reverse-address-resolution detail {mac}
    * Added ShowDerivedConfigInterface
        * Added show derived-config interface <>  parser
    * Added ShowMemoryDebugLeaksChunks parser
        * Parser for 'show memory debug leaks chunks' command
    * Added ShowIpNhrpStats
        * show ip nhrp stats
        * show ip nhrp stats {tunnel}
    * Added ShowIpNhrpStatsDetail
        * show ip nhrp stats detail
        * show ip nhrp stats {tunnel} detail

* iosxr
    * Added show vrrp commads
        * Show vrrp detail
        * show vrrp statistics
        * show vrrp summary
    * Adding new schema and parser in Show_lldp.py
        * Added schema and parser for ShowLldpNeighborsInterfaceIdDetail
    * Added Showhsrpbfd
        * show hsrp bfd
        * show hsrp bfd {interface}
        * show hsrp bfd {interface} {destination_ip}
    * Modified ShowHsrpDetail
        * show hsrp {address_family} {interface} {group_number} detail
    * Added ShowHsrpStatistics
        * show hsrp statistics
        * show hsrp {interface} statistics
        * show hsrp {interface} {group_number} statistics
    * Added ShowHsrpStatus
        * show hsrp status


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpOspfInterface
        * Changed regex pattern <p2> to cover the case where Interface is unnumbered
    * Modified ShowIpOspfInterface2
        * Changed regex pattern <p2> to cover the case where Interface is unnumbered
        * Change <cmd> to <cli_command> so that the class ShowIpOspfInterface2 is reached
        * Update json file for the class ShowIpOspfInterface2
        * Create folder-based testing files
    * Modified ShowPowerInlinePriority
        * Added optional power_inline_auto_shutdown for 9400 Platform.
        * Updated regex pattern <p1a> <p2> for 9400 Platform.
        * Converted the interface name to use long name to align with other POE parsers.
    * Modified ShowPowerInlineUpoePlus
        * Updated regex pattern <p1> to match 'n/a' for type.
    * Modified ShowPowerInlineUpoePlusModule
        * Changed ieee_mode to optional.
        * Added regex pattern <p1a> for 9400 Platform.
        * Converted the interface name to use long name to align with other POE parsers.
    * Modified ShowVersion
        * Updated regex to parse build information
    * Fixed an error in show lisp instance-id <> ethernet server reverse-address-resolution mac <> command.
    * Modified ShowCryptoIkev2StatsExchange
        * Added key Any to schema, to take into account variations in output.
        * Updated regex to take into consideration, spaces in output.
        * Updated ShowCryptoIkev2StatsExchange class with respect to change in schema.
    * Modified ShowDmvpnCountStatus
        * Updated parser class to incorporate IPv6 variant.
    * Modified ShowIpMroute
        * Changed the code to handle multiple interface of different name to escape suffix appending
    * Modified ShowIpNhrpStats
        * Added code for "show nhrp stats",'show ipv6 nhrp stats','show nhrp stats {tunnel}','show ipv6 nhrp stats {tunnel}' CLI commands
        * Updated ShowIpNhrpStats class with respect to addition of commands included.
    * Modified ShowMdnsSdSummary
        * Updated regex to verify entire output
    * Modified ShowLispEidWatch
    * Modified ShowLispIpMapCachePrefixSuperParser
    * Modified ShowLispDatabaseEid
    * Modified ShowLispSiteDetailSuperParser
    * Modified ShowLispMapCacheSuperParser
    * Modified ShowLispIpv4PublisherRloc
    * Modified ShowLispIpv4PublisherRlocSchema
    * Modified ShowLispService
    * Modified ShowLispPublicationPrefixSchema
    * No backward compatible
    * Modified ShowLispEthernetMapCachePrefix
    * Modified ShowLispSiteDetailSuperParser
    * No backward compatible
    * Modified ShowLispMapCacheSuperParser
        * Changed "metric" in Schema to accept int and None
        * Changed regex for "metric" to accept '-' along with integers
    * Modified ShowTelemetryIETFSubscription/ShowTelemetryIETFSubscriptionDetail
        * added keywords "all", "configured", "dynamic", "permanent", "brief" to list of supported CLIs
    * Modified ShowMdnsSdSummary
        * Updated regex to verify latest release output
    * Modified ShowPlatformNatTranslations
        * Modify the regular expression to accept any number of digits
    * Modified ShowIsisDatabaseVerbose
        * Non-backwards compatible change Removed the segment routing key from the flex algo sub dictionary as it does not belong in that location
    * Modified ShowIsisDatabaseVerbose
        * Added new keys for uni link loss and appl spec uni link loss in the show isis database parser
    * Modified ShowRunInterface
        * Updated in schema "cdp enable" optional in the output
    * Modified ShowIpNhrpTrafficDetail
        * Added new argument to support ipv6.
    * Modified ShowIpNhrpTraffic
        * Added new argument to support ipv6
    * Modified ShowPost
        * Modified ShowPost parser and schema to fetch details of two devices.
    * Modified ShowPlatformIfmMapping
        * Removed the int data type from optional variables ifg_id, first_serdes, last_serdes
    * Modified ShowInventory
        * Added two more interfaces in if condition.
    * Modified ShowLicenseTechSupport
        * Added optional key <smartagenttelemetryrumreportmax> to schema.
        * Added optional key <smartagentrumtelemetryrumstoremin> to schema.
    * Modified ShowTcpProxyStatistics
        * Added optional key dre_bypass_received_from_peer to schema
        * Added optional key dre_bypass_hints_sent to schema
        * Added optional key dre_smb_bypass_success_received to schema
        * Added optional key dre_http_bypass_success_received to schema
    * Modified ShowIpMroute
        * Added keys iif_lisp_rloc, iif_lisp_group under incoming_interface_list
        * Added keys extranet_vrf and {e_src,e_grp,e_uptime,e_expire,e_oif_count,e_flags} under newly created extranet_rx_vrf_list
        * Modified incoming_interface_list regex to include parsing of the two above mentioned additional keys
    * Modified ShowSystemIntegrityAllMeasurementNonce
        * Modified the regex pattern of p5 to support smu package
    * Modified ShowPlatformTcamPbrNat
        * Modified ShowPlatformTcamPbrNat cli_command to run on SVL and HA setup

* nxos
    * Modified RunBashTop
        * Modified regex pattern in Cpu, Mib mem and swap for fixing missing key error.
        * For <p4_1>, <p5_1> and <p6> added conversion to support k to Mib and m to Mib

* utils
    * common
        * Removed duplicated key Two
    * common
        * Added new keys Fif, Fifty, Two, TwoH

* updated argument.json class to include changes for ipv6.

* added golden_output_arguments.json file

* iosxr
    * modified ShowPimVrfInterfaceDetail
        * Updated regex pattern p9 and p10 to accommodate for optional output "(config  xx)" for Propagation delay and Override Interval
    * Modified ShowLldpTrafficInterfaceId
        * Added last_clear in a schema.
    * Modified ShowVrrpDetail
        * Updated regex pattern <p20> to accommodate master_name and number_of_slave.
        * Updated regex pattern <p21> to accommodate slave_to
        * Updated regex pattern <p22> to accommodate authentication_string
        * Updated regex pattern <p23> to accommodate master_router_ip and master_router_priority


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Updated ShowCryptoIkev2Session
        * Modified show crypto ikev2 session parser for the latest output change in 17.9


