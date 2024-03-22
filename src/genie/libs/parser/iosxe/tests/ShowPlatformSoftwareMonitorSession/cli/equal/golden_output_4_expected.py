expected_output = {
    'ingress_source_ports': 'FiftyGigE2/0/3',
    'span_session': '1',
    'fed_session': '1',
    'type': 'ERSPAN Source',
    'prev_type': 'ERSPAN Source',
    'rspan': {
        'destination_vlan': 0,
        'source_vlan': 0,
        'source_vlan_sav': 0
    },
    'destination_port_encap': '0x0000',
    'destination_port_ingress_encap': '0x0000',
    'destination_port_ingress_vlan': '0x0',
    'source_session': '1',
    'destination_session': '0',
    'destination_port_cfgd': '0',
    'rspn_destination_cfg': '0',
    'rspn_source_vld': '0',
    'dstination_cli_cfg': '0',
    'dstination_prt_init': '0',
    'pslclcfgd': '0',
    'flags': ['0x00000001', 'PSPAN'],
    'remote_destination_port': '0',
    'destination_port_group': '0',
    'erspan': {
        'id': '101',
        'destination_ip': '40.1.1.2',
        'destination_ipv6': '::',
        'dscp': 0,
        'ip_ttl': 255,
        'ipv6_flow_label': 0,
        'org_ip': '40.1.1.1',
        'org_ipv6': '::',
        'state': 'Enabled',
        'tun_id': 1263,
        'vrfid': 0
    }
}