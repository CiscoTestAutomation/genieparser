--------------------------------------------------------------------------------
                                NEW
--------------------------------------------------------------------------------
* IOSXE
  * New command parsers:
    * show ipv6 eigrp interfaces
    * show ipv6 eigrp interfaces detail
    * show ip eigrp interfaces detail
    * show ipv6 protocols
    * show key chain
  * Modified command parsers:
    * show ip eigrp interfaces
      * Adjusting p1 regex to support IPv6 too
      * Offloading parser to a SuperParser class
      * adding optional keys to ShowIpEigrpInterfacesSchema schema to support `show ip eigrp interfaces detail parser`
* IOS
  * New command parsers:
    * show ipv6 eigrp interfaces
    * show ipv6 eigrp interfaces detail
    * show ip eigrp interfaces detail
    * show ipv6 protocols
    * show key chain
  * Modified command parsers:
    * show ip eigrp interfaces
      * Adjusting p1 regex to support IPv6 too
      * Offloading parser to a SuperParser class
      * adding optional keys to ShowIpEigrpInterfacesSchema schema to support `show ip eigrp interfaces detail parser`
* ASA
  * New command parsers:
    * show crypto ikev2 sa
    * show nameif
    * show failover
    * show failover interface
