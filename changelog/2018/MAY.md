# May 8th

* Normalized all the ats.tcl imports in the package.

* New parsers added and their corresponding unittests:
    * ShowLacpSysId
    * ShowLacpCounters - 'show lacp <channel_group> counters'
    * ShowLacpInternal - 'show lacp <channel_group> internal'
    * ShowLacpNeighbor - 'show lacp <channel_group> neighbor'
    * ShowPagpCounters - 'show pagp <channel_group> counters'
    * ShowPagpNeighbor - 'show pagp <channel_group> neighbor'
    * ShowPagpInternal - 'show pagp <channel_group> internal'
    * ShowEtherchannelSummary
    * show access-session
    * show access-lists
    * show dot1x
    * show dot1x all details
    * show dot1x all statistics
    * show dot1x all summary
    * show dot1x all count
    * show mac address-table
    * show mac address-table aging-time
    * show mac address-table learning
    * ShowIpv6NeighborDetail
    * ShowIpv6NdInterface
    * ShowIpv6IcmpNeighborDetail
    * ShowIpv6Routers

* Fixed the following parsers.
    * ShowBgpVrfAllAllNextHopDatabase

# May 22nd

* Added new parsers and unittests for the following ISSU commands:
    * ShowIssuStateDetail - 'show issu state detail'
    * ShowIssuRollbackTimer - 'show issu rollback timer'

* Added package library to CesMonitor.

# May 24th

* New Vxlan parsers and their related unittests
   * ShowNvePeers
   * ShowNveVniSummary
   * ShowNveVni
   * ShowNveInterfaceDetail
   * ShowNveMultisiteFabricLinks
   * ShowNveMultisiteDciLinks
   * ShowNveEthernetSegment
   * ShowL2routeEvpnEternetSegmentAll
   * ShowL2routeTopologyDetail
   * ShowL2routeMacAllDetail
   * ShowL2routeMacIpAllDetail
   * ShowL2routeSummary
   * ShowL2routeFlAll
   * ShowBgpL2vpnEvpnSummary
   * ShowBgpL2vpnEvpnRouteType
   * ShowBgpL2vpnEvpnNeighbors

* Fixed the following parsers.
    * ShowIpRoute
    * ShowIpOspf
    * ShowRunningConfigBgp

# May 28th

* Added new parsers and unittests for the following commands:
    * ShowRunningConfigInterface - 'show running-config interface \<WORD>'
    * ShowSystemInternalL2fwderMac - 'show system internal l2fwder Mac'
    * ShowVxlan - 'show vxlan'
    * ShowL2routeEvpnMac - 'show l2route evpn mac all'
    * ShowMacAddressTableVni
        * 'show mac address-table vni \<WORD> | grep \<WORD>'
        * 'show mac address-table local vni \<WORD>'
    * ShowL2routeEvpnMacEvi - 'show l2route evpn mac evi \<WORD> mac \<WORD>'
    * ShowBgpL2vpnEvpnWord
        * 'show bgp l2vpn evpn \<WORD> | be "best path, in rib" n \<WORD>'
        * 'show bgp l2vpn evpn \<WORD> | grep -b \<WORD> -a \<WORD> "best path"'
    * ShowNveInterface - 'show nve interface \<WORD> detail | grep Source-Interface'
