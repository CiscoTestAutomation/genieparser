--------------------------------------------------------------------------------
                                FIX
--------------------------------------------------------------------------------
* iosxe
    * Modified ShowIpRoute:
        * Updated src_protocol_dict to contain new key codes including '+', '%', 'p', '&' for static, connected, BGP, OSPF, EIGRP routes
        * Modified regex pattern p3 for both IPv4 and IPv6 tables to include above symbols when parsing