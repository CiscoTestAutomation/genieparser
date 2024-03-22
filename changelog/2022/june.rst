--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowCryptoGdoiKsCoopVersion
        * show crypto gdoi ks coop version
    * Adding new schema and parser in Show_platform.py
        * Added schema and parser for ShowPlatformSoftwareBPCrimsonContentConfig
    * Added ShowCryptoGdoiRekeySa
        * show crypto gdoi rekey sa
    * Added ShowCryptoGdoiRekeySaDetail
        * show crypto gdoi rekey sa detail
    * Added ShowCryptoGdoiKsDetail
        * show crypto gdoi ks detail
    * Added 'show platform hardware qfp active infrastructure bqs status | include QOS|QFP' schema and parser
        * show platform hardware qfp active infrastructure bqs status | include QOS|QFP
    * Added 'show platform hardware qfp active feature qos interface < interface> hierarchy detail | include sub' schema and parser
        * show platform hardware qfp active feature qos interface < interface> hierarchy detail | include sub
    * Added ShowSdwanPolicyAppRoutePolicyFilter
        * added new parser for cli "show sdwan policy app-route-policy-filter"
    * Added ShowSubscriberSession parser
        * show subscriber session
    * Added ShowSubscriberLiteSession parser
        * show subscriber lite-session
    * Added ShowSubscriberStatistics parser
        * show subscriber statistics
    * Added ShowTunnelProtectionStatistics
        * show tunnel protection statistics
    * Added ShowCryptoGdoiKs
        * show crypto gdoi ks
    * Added ShowDiagnosticResultSwitchModuleTestDetail
        * show diagnostic result switch {switch_num} module {mod_num} test {include} detail
    * Added ShowIpDhcpBindingActiveCount Parser
        * show ip dhcp binding | count Active
    * Added ShowCableTdrInterface
        * Added parsing support (schema and parsers) for show cable tdr {interface}
    * Added ShowPppAtmSession
        * show pppatm session
    * Added ShowLslibProducerAllLscacheLinksDetail
        * show lslib producer all lscache links detail

* iosxr
    * Added Parser
        * For 'show tacacs'

* linux
    * Added DockerStatsNoStream
        * added new parser for cli "docker stats --no-stream"

* nxos
    * Updated ShowInterface
        * Updated <p1>, <p12>, <p13> and <p19> regex


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Modified ShowInterface
        * Adjusted <p10> to capture port speed unit
    * Modified ShowInterface
        * Added key fec_mode into the schema
        * Updated regex pattern p12, p12_1 to accommodate additional output for fec_mode
    * Modified ShowSpanningTreeMstSchema
        * Converted 'bridge_assurance_inconsistent' to optional in Line 46
        * Converted 'vpc_peer_link_inconsistent' to optional in Line 47
        * Converted 'designated_regional_root_cost' to optional in Line 54
        * Converted 'designated_regional_root_priority' to optional in Line 55
        * Converted 'designated_regional_root_address' to optional in Line 56
    * Modified ShowSpanningTreeMst
        * Updated Regex p1_1 to match multiple VLAN pairs in line 99
        * Updated Regex p5_1 to match Non-VPC port-channel, physical interfaces (inaddition to VPC port-channel) in line 114
        * Updated p5_1.match code to reflect aforementioned changes in regex p5_1 in line 197, 201 to 205

* iosxe
    * Modified ShowFlowMonitorCache
        * Fixed local variable 'entry_dict' referenced before assignment
        * Fixed p10 match condition, changed 'entries' schema keys as optional
    * Fixed ShowIpv6Routers
    * Fixed ShowLispSessionRLOC
    * Fixed ShowLispSubscriberSuperParser
    * Fixed ShowLispDatabaseEid
    * Fixed ShowLispPublicationPrefixSuperParser
    * Fixed ShowLispMapCacheSuperParser
    * Fixed ShowLispSession
    * Added ShowLispSessionAll
    * Added ShowLispSessionEstablished
    * No backward compatibility
    * Modified ShowRunInterface
        * Fixed local variable 'inbound_dict' referenced before assignment
        * Fixed parser returning empty dict
    * Modified the ShowLogging
        * Fix for local variable referenced before assignment
    * Fixed ShowPolicyMapInterface
        * Fixed the parser to support multilevel indentation.
        * Updated regex for dscp.
        * Added regex to support service group as optional key.
        * Added new regex to support cir, bc, be in police.
        * Added <p47>, <p48>, <p49>, <p50> missing regex.
        * no backward compatibility.
    * Made number_of_prefixes as Optional,generic for "show ipv6 route summary"
        * show ipv6 route summary
        * show ipv6 route vrf <vrf> summary
    * Modified ShowTrack
        * Updated the parser schema with type, latest operation return code and latest rtt
        * Added <p1_1>, <p3_1>, <p8> and <p9> regex
    * Modified ShowRunInterface
        * Added ip dhcp snooping information option allow-untrusted
        * Added regex pattern <p83> <P84> to accommodate outputs
    * Modified ShowRunAllSectionInterface
        * Added ip dhcp snooping information option allow-untrusted
        * Added regex pattern <p39> <P40> to accommodate outputs
    * Modified ShowVrrp
        * Modified the code to work for BACKUP as it was working only for MASTER
        * Added optional key <master_down_expiration_secs> to schema
        * Updated regex pattern <p2> to accommodate state BACKUP
        * Updated regex pattern <p11> to accommodate priority configured
        * Updated regex pattern <p16> to accommodate when server not present with priority
        * Updated regexp pattern <p17> to accommodate adv interval (learned)
        * Updated regexp pattern <p18> to accommodate down interval expiration details

* iosxr
    * Modified the ShowOspfInterface
        * Fix for local variable 'ospf_dict' referenced before assignment
        * Added the missing authentication key in the schema.
    * Modified ShowL2VpnXconnect
        * Updated parser to support version 7.2.2
    * Modified ShowHsrpDetail
        * changed <timers> and <redirects_disable> to optional to accommodate MGO outputs
        * Added optional string <configured> to pattern <p13> to accommodate config mac address


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpDhcpBinding Parser
        * show ip dhcp binding


