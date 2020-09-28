expected_output = {
    "interfaces": {
        "GigabitEthernet1/0/13": {
            "authentication_control_direction": "in",
            "authentication_event_fail_action": "next-method",
            "authentication_fallback": "dot1x",
            "authentication_host_mode": "multi-auth",
            "authentication_order": "dot1x mab",
            "authentication_periodic": True,
            "authentication_port_control": "auto",
            "authentication_priority": "dot1x mab",
            "authentication_timer_inactivity": "65535",
            "authentication_timer_reauthenticate_server": True,
            "authentication_violation": "restrict",
            "description": "ISE Controlled Port",
            "dot1x_pae_authenticator": True,
            "dot1x_timeout_quiet_period": "5",
            "dot1x_timeout_server_timeout": "10",
            "dot1x_timeout_tx_period": "5",
            "ip_arp_inspection_limit_rate": "1024",
            "ip_dhcp_snooping_limit_rate": "100",
            "load_interval": "30",
            "mab": True,
            "snmp_trap_link_status": False,
            "snmp_trap_mac_notification_change_added": True,
            "snmp_trap_mac_notification_change_removed": True,
            "spanning_tree_bpduguard": "enable",
            "spanning_tree_portfast": True,
            "switchport_access_vlan": "70",
            "switchport_mode": "access",
            "switchport_nonegotiate": "nonegotiate",
        }
    }
}
