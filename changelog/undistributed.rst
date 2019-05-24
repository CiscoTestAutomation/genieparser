* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                   LOGGING
--------------------------------------------------------------------------------
* NXOS
    * Added ShowLoggingLogfile for:
      'show logging logfile'
      'show logging logfile | include {include}'

--------------------------------------------------------------------------------
                                   IPV6
--------------------------------------------------------------------------------
* NXOS
     * Added ShowIpv6NeighborsDetailVrfAll for:
        show ipv6 neighbor detail vrf all
     * Added ShowIpv6NdInterfaceVrfAll for:
        show ipv6 nd interface vrf all
     * Added ShowIpv6RoutersVrfAll for:
        show ipv6 routers vrf all
* IOSXE
     * Added ShowIpv6Neighbors for:
        show ipv6 neighbors detail
        show ipv6 neighbors vrf {vrf}
     * Added ShowIpv6NeighborsDetail for:
        show ipv6 neighbors detail
        show ipv6 neighbors vrf {vrf} detail
* IOSXR
     * Added ShowIpv6NeighborsDetail for:
        show ipv6 neighbors detail

--------------------------------------------------------------------------------
                                   VLAN
--------------------------------------------------------------------------------
* NXOS
     * Updated ShowVlan to support different names
     
--------------------------------------------------------------------------------
                                   INTERFACE
--------------------------------------------------------------------------------
* IOSXE
     * Added interface value under convert_intf_name method of common file

--------------------------------------------------------------------------------
                                BGP
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowBgpAllNeighbors for more varied neighbor capabilities
        * vrf default value handled   
    * Updated ShowIpBgpNeighbors to support different Address families
    * Updated ShowIpBgp to support different status codes 
    * Updated ShowIpBgpNeighborsRoutes to support VRF
    * Updated ShowBgpNeighborsRoutes to support VRF
    * Updated ShowBgpAllNeighborsAdvertisedRoutes to support Ips addresses without subnet mask
* IOSXR
    * Updated ShowBgpAllAll for more variations of parameters
    * Updated ShowBgpAllNeighbors for more varied neighbor capabilities
    * Update ShowBgpAllNeighbors to support device.parse

--------------------------------------------------------------------------------
                                  POLICY-MAP
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowPolicyMapInterface to support more policy action type
    
--------------------------------------------------------------------------------
                                   PLATFORM
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowPlatform to support optional output

--------------------------------------------------------------------------------
                                   RIP
--------------------------------------------------------------------------------
* IOSXR
    * Updated ShowRipInterface for more varied interface name and status
* NXOS
    * Added ShowIpRipVrfAll for:
        show ip rip
        show ip rip vrf <vrf>
        show ip rip vrf all

    * Added ShowIpv6RipVrfAll for:
        show ipv6 rip
        show ipv6 rip vrf <vrf>
        show ipv6 rip vrf all

    * Added ShowIpRipRouteVrfAll for:
        show ip rip route
        show ip rip route vrf <vrf>
        show ip rip route vrf all

    * Added ShowIpv6RipRouteVrfAll for:
        show ipv6 rip route
        show ipv6 rip route vrf {vrf}
        show ipv6 rip route vrf all
    
    * Added ShowIpRipInterfaceVrfAll for:
        show ip rip interface
        show ip rip interface vrf {vrf}
        show ip rip interface vrf all

--------------------------------------------------------------------------------
                                   IP_VRF
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowIpVrf for:
      * show ip vrf
      * show ip vrf <vrf>
      * show ip vrf detail
      * show ip vrf detial <vrf>

--------------------------------------------------------------------------------
                                   IP
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowIpAlias for:
       show ip aliases
       show ip aliases vrf {vrf}
    * Added ShowIPAliasDefaultVrf:
       show ip aliases default-vrf

--------------------------------------------------------------------------------
                                   OSPF
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpOspfNeighbor for more varied states
    * Enhanced ShowIpOspf

--------------------------------------------------------------------------------
                                   VRF
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowVrf for:
      * show vrf detail
      * show vrf detail <vrf>
      * show vrf
      * show vrf <vrf>
* IOSXR
    * Updated ShowVrfAllDetail to support custom vrf argument
* IOS
    * Updated ShowVrf for:
      * show vrf
      * show vrf <vrf>
    * Updated ShowVrfDetail unittest

--------------------------------------------------------------------------------     
                                xconnect
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowL2VpnXconnect for:
        show l2vpn xconnect 

--------------------------------------------------------------------------------
                                   FDB
--------------------------------------------------------------------------------
* NXOS
    * Added ShowMacAddressTable for:
        show mac address-table
    * Added ShowMacAddressTableAgingTime for:
        show mac address-table aging-time
    * Added ShowMacAddressTableLimit for:
        show mac address-table limit
    * Added ShowSystemInternalL2fwderMac for:
        show system internal l2fwder mac
    * Updated ShowMacAddressTableVni for:
        show mac address-table vni <WORD> | grep <WORD>
        show mac address-table local vni <WORD>
* IOSXE
    *Updated ShowMacAddressTable to make total_mac_addresses optional
--------------------------------------------------------------------------------
                                   LLDP
--------------------------------------------------------------------------------
* NXOS
    * Added ShowLldpAll for:
        show lldp all
    * Added ShowLldpTimers for:
        show lldp timers
    * Added ShowLldpTlvSelect for:
        show lldp tlv-select
    * Added ShowLldpNeighborsDetail for:
        show lldp neighbors detail
    * Added ShowLldpTraffic for:
        show lldp traffic

--------------------------------------------------------------------------------
                                   LAG
--------------------------------------------------------------------------------
* NXOS
    * Added ShowLacpSystemIdentifier for:
        show lacp system-identifier
    * Added ShowLacpCounters for:
        show lacp counters
    * Added ShowLacpNeighbor for:
        show lacp neighbor
    * Added ShowPortChannelSummary for:
        show port-channel summary
    * Added ShowPortChannelDatabase for:
        show port-channel database
--------------------------------------------------------------------------------
                                   ARCHIVE
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowArchiveConfigDifferences for more varied output matching

--------------------------------------------------------------------------------
                                   interface
--------------------------------------------------------------------------------
* IOSXE
    * Fixed issues for ShowInterfaceSwitchport where some output are not parsed

--------------------------------------------------------------------------------
                                   MLD
--------------------------------------------------------------------------------
* IOSXR
    * Added ShowMldSummaryInternal for:
        show mld summary internal
        show mld vrf {vrf} summary internal
    * Added ShowMldInterface:
        show mld interface
        show mld vrf {vrf} interface
    * Added ShowMldGroupsDetail:
        show mld groups detail
        show mld vrf {vrf} groups detail
        show mld groups {group} detail

--------------------------------------------------------------------------------
                                   ARP
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowIpArp for:
        show ip arp
        show ip arp vrf {vrf}