--------------------------------------------------------------------------------
                            New
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowRunInterface:
        * Added parsing support (schema and parsers) for following output
            * spanning-tree portfast trunk
--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowRunInterface:
        * Removed duplicate schema variables
                * Optional('snmp_trap_link_status'): bool,
                * Optional('snmp_trap_mac_notification_change_added'): bool,
                * Optional('snmp_trap_mac_notification_change_removed'): bool,
                * Optional('spanning_tree_bpduguard'): str,
                * Optional('spanning_tree_portfast'): bool,
                * Optional('spanning_tree_bpdufilter'): str,
                * Optional('switchport_access_vlan'): str,
                * Optional('switchport_trunk_vlans'): str,
                * Optional('switchport_mode'): str,
                * Optional('switchport_nonegotiate'): str,
                * Optional('vrf'): str,

        * Added the following schema variable
                * Optional('spanning_tree_portfast_trunk'): bool,
