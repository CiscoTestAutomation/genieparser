--------------------------------------------------------------------------------
                                FIX
--------------------------------------------------------------------------------
* iosxe
    * Modified ShowIpRoute:
        * Updated src_protocol_dict to contain new key codes including '+', '%', 'p', '&' for static, connected, BGP, OSPF, EIGRP routes
        * Modified regex pattern p3 for both IPv4 and IPv6 tables to include above symbols when parsing
        * Modified regex pattern p3 to include next hop vrf. Before vrf was in brackets and was being treated as an outgoing interface which was incorrect
        * Added vrf field for next hop in output dictionary of show ip route.