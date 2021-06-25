--------------------------------------------------------------------------------
                                NEW
--------------------------------------------------------------------------------
* ASA
    * Added ShowCryptoIkev2Sa:
        * show crypto ikev2 sa
    * Added ShowNameif:
        * show nameif
    * Added ShowFailover:
        * show failover
    * Added ShowFailoverInterface:
        * show failover interface
        
* IOSXE
    * Added ShowIpv6EigrpInterfaces:
        * show ipv6 eigrp interfaces
    * Added ShowIpEigrpInterfacesDetail:
        * show ip eigrp interfaces detail
    * Added ShowIpv6EigrpInterfacesDetail:
        * show ipv6 eigrp interfaces detail
    * Added ShowKeyChain:
        * show key chain
    * Added ShowIpv6Protocols:
        * show ipv6 protocols
        * show ipv6 protocols vrf {vrf}

* IOS
    * Added ShowIpv6EigrpInterfaces:
        * show ipv6 eigrp interfaces
    * Added ShowIpEigrpInterfacesDetail:
        * show ip eigrp interfaces detail
    * Added ShowIpv6EigrpInterfacesDetail:
        * show ipv6 eigrp interfaces detail
    * Added ShowKeyChain:
        * show key chain
    * Added ShowIpv6Protocols:
        * show ipv6 protocols
        * show ipv6 protocols vrf {vrf}


--------------------------------------------------------------------------------
                                FIX
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowIpEigrpInterfaces:
        * Adjusting p1 regex to support IPv6 too
        * Offloading parser to a SuperParser class
        * Support eigrp named mode
        * Added Optional keys to ShowIpEigrpInterfacesSchema schema to support `show ip eigrp interfaces detail parser`

