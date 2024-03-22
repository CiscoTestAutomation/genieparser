expected_output = {
    'derived_config': {
        'Tunnel1': {
            'ip_address': '192.168.1.1', 
            'ip_access_group_in': 'Tu1-ipsec-ds-ipv4-in', 
            'ip_access_group_out': 'Tu1-ipsec-ds-ipv4-out', 
            'ipv6': 'enabled', 
            'ipv6_access_group_in': 'Tu1-ipsec-ds-ipv6-in', 
            'ipv6_access_group_out': 'Tu1-ipsec-ds-ipv6-out', 
            'tunnel_source': 'GigabitEthernet1', 
            'tunnel_mode': 'ipsec dual-overlay', 
            'tunnel_destination': '30.30.30.2', 
            'tunnel_ipsec_profile': 'prof'
        }
    }
}