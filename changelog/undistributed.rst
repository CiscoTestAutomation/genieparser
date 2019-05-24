* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

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
    * Added ShowVrf for:
        show vrf
        show vrf {vrf}

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
                                   ARCHIVE
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowArchiveConfigDifferences for more varied output matching

--------------------------------------------------------------------------------
                                   interface
--------------------------------------------------------------------------------
* IOSXE
    * Fixed issues for ShowInterfaceSwitchport where some output are not parsed
* IOSXR
    * Updated ShowInterfaceDetail to support custom interface
        show interface <interface> detail
    * Updated ShowEthernetTag to support custom interface
        show ethernet tag <interface>