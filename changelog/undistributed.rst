* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowIpBgpRouteDistributer for:
        * show ip bgp {route}
        * show ip bgp {address_family}
    * Added ShowLldpNeighbors for
        * show lldp neighbors
* NXOS
    * Added ShowIpRouteSummary for:
        * show ip route summary
        * show ip route summary vrf {vrf}
    * Added ShowInterfaceStatus for:
        * show interface status
        * show interface {interface} status
* ASA 
    * Added ShowVPNSessionDBSummary for:
        * show vpn-sessiondb summary
    * Added ShowVPNLoadBalancing for:
        * show vpn load-balancing
    * Added ShowIpLocalPool for:
        * show ip local pool {pool}
    * Added ShowServicePolicy for:
        * show service-policy
    * Added ShowVpnSessiondb for:
        * show vpn-sessiondb
        * show vpn-sessiondb anyconnect
        * show vpn-sessiondb anyconnect sort inactivity
        * show vpn-sessiondb webvpn
    * Added ShowResourceUsage for:
        * show resource usage
    * Added ShowAspDrop for
        * show asp drop


--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowMplsForwardingTable:
        * Modified wrong regex
    * Updated ShowIpCef:
        * Modified regex to support SID
        * update regex and schema to support local sid
    * Updated ShowMplsForwardingTableDetail:
        * show mpls forwarding-table {route} detail
    * Updated Traceroute:
        * Updated regex to support various outputs.
        * Updated schema and regex to support AS number.
    * Updated ShowBootvar
        * Fixed crash
        * Added unittest
    * Updated ShowInterfacesStatus
        * Change key mandatory 'type' into optional
        * Updated regex to support various output
    * Updated ShowNveEthernetSegment
        * Updated regex to support various output
    * Updated ShowIpInterfaceVrfAll
        * Update regex to support more various output
    * Update ShowEnvironment
        * Update regex to support more various output
    * Update ShowIpNatTranslations
        * Fix typo in cli_command
    * Update ShowNveInterfaceDetail
        * Update regex to support more various output
    * Update ShowIpOspfNeighborDetail
        * Update regex to support more various output
    * Update ShowCdpNeighborsDetail
        * Change key mandatory 'capabilities' into optional
    * Update ShowMacAddressTable
        * Update regex to support various output
    * Update ShowAccessLists
        * Update regex to support various output
    * Update ShowLldpEntry
        * Fix typo in the code

* NXOS
    * Updated ShowInterface
        * Update regex to cover both 'IP' and 'ip', both 'Rx' and 'RX'
        * Clean code and correctly assign values to the key 'enabled'
    * Updated ShowIpRoute
        * Add keys into the schema, modify regex
    * Updated ShowRouting
        * Change its parent class from ShowRoutingVrfAll into ShowIpRoute
    * Update ShowIpInterfaceVrfAll
        * Changed wccp_* keys to be optional from mandatory to support new output
    * Update ShowPlatformInternalHalPolicyRedirdst:
        * Changed keys rewrite_mac, rewrite_vnid, outgoing_l2_ifindex, 
            outgoing_ifname, packets_hash as optional
    * Update ShowSystemInternalSysmgrServiceName:
        * Enhanced 'tag' key to support more output

* IOSXR
    * Update ShowBgpInstanceSummary
        * Update regex to support various output

--------------------------------------------------------------------------------
                                common.py
--------------------------------------------------------------------------------
* updated _find_command to find command for nxos in aci mode
