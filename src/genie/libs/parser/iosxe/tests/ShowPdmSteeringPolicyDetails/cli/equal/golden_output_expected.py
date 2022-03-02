expected_output = {
    'policy': 'Contract2',
    'policy_id': '577677153',
    'policy_entries': {
        1: {
            'dst_port': '15000',
            'firewall_mode': 'routed',
            'no_of_rlocs': 1,
            'owner': 'GPP',
            'counters': 0,
            'protocol': 6,
            'rloc': {
                1: {
                    'priority': 0,
                    'rloc_ip': '60.60.60.62',
                    'weight': 10
                }
            },
            'rloc_status': 'Received',
            'service': 'service_INFRA_VN',
            'service_ip': '172.18.0.2',
            'service_locator': '255',
            'service_name': 'service_INFRA_VN',
            'src_port': 'any',
            'vnid': 4097,
            'vrf_id': 0
        },
        2: {
            'dst_port': 'any',
            'firewall_mode': 'routed',
            'no_of_rlocs': 1,
            'owner': 'GPP',
            'counters': 0,
            'protocol': 17,
            'rloc': {
                1: {
                    'priority': 0,
                    'rloc_ip': '60.60.60.62',
                    'weight': 10
                }
            },
            'rloc_status': 'Received',
            'service': 'service_INFRA_VN',
            'service_ip': '172.18.0.2',
            'service_locator': '255',
            'service_name': 'service_INFRA_VN',
            'src_port': 'any',
            'vnid': 4097,
            'vrf_id': 0
        },
    }
}