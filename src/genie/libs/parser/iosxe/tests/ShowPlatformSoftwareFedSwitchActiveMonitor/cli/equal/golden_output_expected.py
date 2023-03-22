expected_output = {
    'session_type': 'ERSPAN Source Session',
    'source_ports': {
        'rx': ['GigabitEthernet1/0/1', 'GigabitEthernet1/0/2', 'GigabitEthernet1/0/3', 'TenGigabitEthernet1/1/2', 'TenGigabitEthernet1/1/4'],
        'tx': ['None']
    },
    'source_rspan_vlan': 0,
    'destination_rspan_vlan': 0,
    'encap': 'Native',
    'ingress_forwarding': 'Disabled',
    'erspan_enable': 1,
    'erspan_hw_programmed': 1,
    'erspan_mandatory_cfg': 1,
    'erspan_id': 3,
    'gre_protocol': '88be',
    'mtu': 9000,
    'ip_tos': 0,
    'ip_ttl': 255,
    'cos': 0,
    'vrf_id': 0,
    'tunnel_if_id': 65,
    'destination_ip': '1.1.3.2',
    'org_ip': '1.1.3.1'
}