| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 19.0.1        |

--------------------------------------------------------------------------------
                                    ND
--------------------------------------------------------------------------------
* NXOS
    * Updated  ShowIpv6Routers parser

--------------------------------------------------------------------------------
                                    MCAST
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowForwardingDistributionMulticastRoute parser

--------------------------------------------------------------------------------
                                    VLAN
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowVlan parser

--------------------------------------------------------------------------------
                                    Interface
--------------------------------------------------------------------------------
* IOSXE
    * Enhanced  ShowIpInterface and ShowInterface

--------------------------------------------------------------------------------
                                    ACL
--------------------------------------------------------------------------------
* IOSXE
    * Enhanced  ShowAcessLists

--------------------------------------------------------------------------------
                                    BGP
--------------------------------------------------------------------------------
* NXOS
    * Enhanced  ShowBgpVrfAllNeighbors


| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 19.0.0        |

--------------------------------------------------------------------------------
                                    SYSTEM
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowClock for 'show clock'

--------------------------------------------------------------------------------
                                    SESSION
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowLine for 'show line'
    * Add ShowUsers for 'show users'

--------------------------------------------------------------------------------
                                    ARP
--------------------------------------------------------------------------------
* NXOS
    * Fixed ShowIpArpstatisticsVrfAll for 'show ip arp statistics'

--------------------------------------------------------------------------------
                                    PLATFORM
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowProcessesCpuPlatform for 'show processes cpu platform'
    * Add ShowProcessesCpu for 'show processes cpu'
    * Enhanced ShowProcessesCpuSorted for 'show processes cpu sorted'
    * Add ShowEnvironmentAll for 'show environment all' - ASR1K
    * Add ShowEnvironment for 'show environment'

* NXOS
    * Fixed ShowInstallActive for 'show install active'

--------------------------------------------------------------------------------
                                    NTP
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowNtpAssociationsDetailSchema for 'show ntp associations detail'

--------------------------------------------------------------------------------
                                    RIP
--------------------------------------------------------------------------------
* IOSXE
    * Added below parsers
        * ShowIpRipDatabase
        * ShowIpv6RipDatabase
        * ShowIpv6Rip

--------------------------------------------------------------------------------
                                    Protocol
--------------------------------------------------------------------------------
* IOSXE
    * Added below parsers:
        * ShowIpProtocolsSectionRip
        * ShowIpv6ProtocolsSectionRip

--------------------------------------------------------------------------------
                                    IOS
--------------------------------------------------------------------------------
* Added below IOS parsers:
    *  ShowAccessLists
    *  ShowArchive
    *  ShowIpArp:
    *  ShowAccessLists
    *  ShowBgpAllDetail
    *  ShowBgpAllNeighborsPolicy
    *  ShowBgpAllNeighborsAdvertisedRoutes
    *  ShowBgpAllSummary
    *  ShowBgpAllClusterIds
    *  ShowBgpAllNeighbors
    *  ShowBgpAllNeighborsReceivedRoutes
    *  ShowIpBgpTemplatePeerSession
    *  ShowBgpAllNeighborsRoutes
    *  ShowIpBgpTemplatePeerPolicy
    *  ShowIpBgpAllDampeningParameters
    *  ShowBgpAll
    *  ShowDot1xAllDetail
    *  ShowDot1x
    *  ShowDot1xAllSummary
    *  ShowDot1xAllCount
    *  ShowIpIgmpInterface
    *  ShowIpIgmpGroupsDetail
    *  ShowIpRoute
    *  ShowIpv6Route
    *  ShowLldp
    *  ShowLldpEntry
    *  ShowLldpNeighborsDetail
    *  ShowLldpTraffic
    *  ShowLldpInterface
    *  ShowIpMroute
    *  ShowIpv6Mroute
    *  ShowIpMrouteStatic
    *  ShowIpMulticast
    *  ShowMemoryStatistics
    *  ShowIpv6MldInterface
    *  ShowIpv6MldGroupsDetail
    *  ShowIpv6MldSsmMap
    *  ShowIpOspf
    *  ShowIpOspfInterface
    *  ShowIpOspfShamLinks
    *  ShowIpOspfVirtualLinks
    *  ShowIpOspfNeighborDetail
    *  ShowIpOspfDatabaseRouter
    *  ShowIpOspfDatabaseExternal
    *  ShowIpOspfDatabaseNetwork
    *  ShowIpOspfDatabaseSummary
    *  ShowIpOspfDatabaseOpaqueArea
    *  ShowIpOspfMplsLdpInterface
    *  ShowIpOspfMplsTrafficEngLink
    *  ShowIpv6PimInterface
    *  ShowIpv6PimBsrElection
    *  ShowIpv6PimBsrCandidateRp
    *  ShowIpPimInterface
    *  ShowIpPimBsrRouter
    *  ShowIpPimRpMapping
    *  ShowIpPimInterfaceDetail
    *  ShowPimNeighbor
    *  ShowIpPimNeighbor
    *  ShowIpv6PimNeighbor
    *  ShowIpv6PimNeighborDetail
    *  ShowIpPimInterfaceDf
    *  ShowIpPrefixListDetail
    *  ShowIpv6PrefixListDetail
    *  ShowIpProtocols
    *  ShowRouteMapAll
    *  ShowIpRoute
    *  ShowIpv6RouteUpdated
    *  ShowSpanningTreeSummary
    *  ShowSpanningTreeDetail
    *  ShowSpanningTree
    *  ShowSpanningTreeMstDetail
    *  ShowErrdisableRecovery
    *  ShowSpanningTreeMstConfiguration
    *  ShowStandbyInternal
    *  ShowStandbyAll
    *  ShowStandbyDelay
    *  ShowIpStaticRoute
    *  ShowIpv6StaticDetail
    *  ShowVlan
    *  ShowVlanMtu
    *  ShowVlanAccessMap
    *  ShowVlanRemoteSpan
    *  ShowVlanFilter