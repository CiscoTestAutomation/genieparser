    --------------------------------------------------------------------------------
                                New
    --------------------------------------------------------------------------------
    * IOSXE
        * Modified ShowRunInterface:
            * Added parsing support (schema and parsers) for following outputs
                * power inline port priority high
                * power inline static max 30000
                * spanning-tree bpdufilter enable
                * ip flow monitor IPv4NETFLOW input
                * switchport protected
                * switchport block unicast
                * switchport block multicast
                * switchport trunk allowed vlan 820,900-905
                * ip dhcp snooping trust
                * ip arp inspection trust
    
    --------------------------------------------------------------------------------
                                Fix
    --------------------------------------------------------------------------------
    * IOSXE
        * Modified ShowRunInterface:
            * Fixed channel_group (was not working).
                * Added channel_group to ShowRunInterfaceSchema
                * Updated intf_dict to make it work properly
