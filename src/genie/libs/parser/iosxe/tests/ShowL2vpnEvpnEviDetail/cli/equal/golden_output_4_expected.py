expected_output = {
    '1': {
        'bridge_domain': {
            '201': {
                'access_if': 'Vlan201',
                'core_if': 'Vlan200',
                'core_vlan': 200,
                'etag': 0,
                'ipv4_irb': True,
                'ipv6_irb': True,
                'l2vni': 6000,
                'l3vni': 5000,
                'mcast_ip': '232.1.1.1',
                'nve_if': 'nve10',
                'pseudo_port': {
                    'GigabitEthernet1/0/1 service instance 201': {
                    }
                },
                'rmac': 'a0f8.4910.bce2',
                'state': 'Established',
                'vrf': 'green',
                'vtep_ip': '10.1.1.10',
            }
        },
        'encap_type': 'vxlan',
        'evi_type': 'VLAN Based',
        'export_rt': '10:1',
        'import_rt': '10:1',
        'ip_local_learn': True,
        'per_evi_label': 'none',
        'rd': '10.1.1.10:1',
        'rd_type': 'auto',
        'replication_type': 'Static',
        'state': 'Established',
    }
}