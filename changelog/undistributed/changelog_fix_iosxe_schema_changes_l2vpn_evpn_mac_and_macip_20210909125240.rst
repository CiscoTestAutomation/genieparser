--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowL2vpnEvpnMac:
        * changed schema to support vary outputs
            * added evi, eth_tag and bd_id as key
        * updated test cases
        * added cli filter and tests for vlan_id
            * show l2vpn evpn mac vlan {vlan_id}
            * show l2vpn evpn mac vlan {vlan_id} address {mac_addr}
            * show l2vpn evpn mac vlan {vlan_id} duplicate
            * show l2vpn evpn mac vlan {vlan_id} local
            * show l2vpn evpn mac vlan {vlan_id} remote
    * Modified ShowL2vpnEvpnMacIp:
        * changed schema
            * added evi, mac_addr and bd_id as key
        * updated test cases
        * added cli filter and tests for vlan_id
            * show l2vpn evpn mac ip vlan {vlan_id}
            * show l2vpn evpn mac ip vlan {vlan_id} address {ipv4_addr}
            * show l2vpn evpn mac ip vlan {vlan_id} address {ipv6_addr}
            * show l2vpn evpn mac ip vlan {vlan_id} duplicate
            * show l2vpn evpn mac ip vlan {vlan_id} local
            * show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr}
            * show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr} address {ipv4_addr}
            * show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr} address {ipv6_addr}
            * show l2vpn evpn mac ip vlan {vlan_id} remote
    * Modified ShowL2vpnEvpnMacDetail:
        * changed schema
            * added evi, eth_tag, mac_addr and bd_id as key
        * updated test cases
    * Modified ShowL2vpnEvpnMacIpDetail:
        * changed schema
            * added evi, mac_addr, eth_tag and bd_id as key
        * updated test cases
    * Modified ShowL2fibPathListId:
        * changed schema key 'path_ids' to 'pathlist_id'
        * updated tests
    * Modified ShowL2routeEvpnImetDetail
        * updated regex logic
        * updated testcase
    * Modified ShowL2fibPathListId
        * updated incorrect logic
    * Modified ShowL2routeEvpnMacIp
        * The c code has changed, the full length ipv6 addresses and next hop is now on the same line.
        * updated logic
        * updated test cases
